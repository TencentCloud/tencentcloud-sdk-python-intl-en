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


class AccountInfo(AbstractModel):
    r"""Account information

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of postgres-lnp6j617
        :type DBInstanceId: str
        :param _UserName: Account
        :type UserName: str
        :param _Remark: Specifies the account remark.
        :type Remark: str
        :param _Status: Account status. valid values: 1-creating, 2-normal, 3-modifying, 4-resetting password, 5-locked, -1-deleting.
        :type Status: int
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _UpdateTime: Last update time of the account.
        :type UpdateTime: str
        :param _PasswordUpdateTime: Specifies the last modified time of the account.

This field will only take effect after 2025-10-31. No matter whether the password is modified before, the value will be the default value: 0000-00-00 00:00:00
Indicates that this field is updated only when the password is modified via the cloud API or the console.
        :type PasswordUpdateTime: str
        :param _UserType: Account type. valid values: normal, tencentDBSuper. normal references a general user, tencentDBSuper possesses the pg_tencentdb_superuser user role.
        :type UserType: str
        :param _OpenCam: Specifies whether CAM verification is enabled for the user account.
        :type OpenCam: bool
        """
        self._DBInstanceId = None
        self._UserName = None
        self._Remark = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._PasswordUpdateTime = None
        self._UserType = None
        self._OpenCam = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-lnp6j617
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""Account
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Remark(self):
        r"""Specifies the account remark.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        r"""Account status. valid values: 1-creating, 2-normal, 3-modifying, 4-resetting password, 5-locked, -1-deleting.
        :rtype: int
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
    def UpdateTime(self):
        r"""Last update time of the account.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PasswordUpdateTime(self):
        r"""Specifies the last modified time of the account.

This field will only take effect after 2025-10-31. No matter whether the password is modified before, the value will be the default value: 0000-00-00 00:00:00
Indicates that this field is updated only when the password is modified via the cloud API or the console.
        :rtype: str
        """
        return self._PasswordUpdateTime

    @PasswordUpdateTime.setter
    def PasswordUpdateTime(self, PasswordUpdateTime):
        self._PasswordUpdateTime = PasswordUpdateTime

    @property
    def UserType(self):
        r"""Account type. valid values: normal, tencentDBSuper. normal references a general user, tencentDBSuper possesses the pg_tencentdb_superuser user role.
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def OpenCam(self):
        r"""Specifies whether CAM verification is enabled for the user account.
        :rtype: bool
        """
        return self._OpenCam

    @OpenCam.setter
    def OpenCam(self, OpenCam):
        self._OpenCam = OpenCam


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._PasswordUpdateTime = params.get("PasswordUpdateTime")
        self._UserType = params.get("UserType")
        self._OpenCam = params.get("OpenCam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDBInstanceToReadOnlyGroupRequest(AbstractModel):
    r"""AddDBInstanceToReadOnlyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: RO group ID
        :type ReadOnlyGroupId: str
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""RO group ID
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDBInstanceToReadOnlyGroupResponse(AbstractModel):
    r"""AddDBInstanceToReadOnlyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task ID
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


class AnalysisItems(AbstractModel):
    r"""Detailed analysis of a slow query statement with abstract parameter values, which is returned by the `DescribeSlowQueryAnalysis` API

    """

    def __init__(self):
        r"""
        :param _DatabaseName: The name of the database queried by the slow query statement
        :type DatabaseName: str
        :param _UserName: The name of the user who executes the slow query statement
        :type UserName: str
        :param _NormalQuery: The slow query statement whose parameter values are abstracted
        :type NormalQuery: str
        :param _ClientAddr: The address of the client that executes the slow query statement
        :type ClientAddr: str
        :param _CallNum: The number of executions of the slow query statement during the specified period of time
        :type CallNum: int
        :param _CallPercent: The ratio (in decimal form) of the number of executions of the slow query statement to that of all slow query statements during the specified period of time
        :type CallPercent: float
        :param _CostTime: The total execution time of the slow query statement during the specified period of time
        :type CostTime: float
        :param _CostPercent: The ratio (in decimal form) of the total execution time of the slow query statement to that of all slow query statements during the specified period of time
        :type CostPercent: float
        :param _MinCostTime: The shortest execution time (in ms) of the slow query statement during the specified period of time
        :type MinCostTime: float
        :param _MaxCostTime: The longest execution time (in ms) of the slow query statement during the specified period of time
        :type MaxCostTime: float
        :param _AvgCostTime: The average execution time (in ms) of the slow query statement during the specified period of time
        :type AvgCostTime: float
        :param _FirstTime: The timestamp when the slow query statement starts to execute for the first time during the specified period of time
        :type FirstTime: str
        :param _LastTime: The timestamp when the slow query statement starts to execute for the last time during the specified period of time
        :type LastTime: str
        """
        self._DatabaseName = None
        self._UserName = None
        self._NormalQuery = None
        self._ClientAddr = None
        self._CallNum = None
        self._CallPercent = None
        self._CostTime = None
        self._CostPercent = None
        self._MinCostTime = None
        self._MaxCostTime = None
        self._AvgCostTime = None
        self._FirstTime = None
        self._LastTime = None

    @property
    def DatabaseName(self):
        r"""The name of the database queried by the slow query statement
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def UserName(self):
        r"""The name of the user who executes the slow query statement
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def NormalQuery(self):
        r"""The slow query statement whose parameter values are abstracted
        :rtype: str
        """
        return self._NormalQuery

    @NormalQuery.setter
    def NormalQuery(self, NormalQuery):
        self._NormalQuery = NormalQuery

    @property
    def ClientAddr(self):
        r"""The address of the client that executes the slow query statement
        :rtype: str
        """
        return self._ClientAddr

    @ClientAddr.setter
    def ClientAddr(self, ClientAddr):
        self._ClientAddr = ClientAddr

    @property
    def CallNum(self):
        r"""The number of executions of the slow query statement during the specified period of time
        :rtype: int
        """
        return self._CallNum

    @CallNum.setter
    def CallNum(self, CallNum):
        self._CallNum = CallNum

    @property
    def CallPercent(self):
        r"""The ratio (in decimal form) of the number of executions of the slow query statement to that of all slow query statements during the specified period of time
        :rtype: float
        """
        return self._CallPercent

    @CallPercent.setter
    def CallPercent(self, CallPercent):
        self._CallPercent = CallPercent

    @property
    def CostTime(self):
        r"""The total execution time of the slow query statement during the specified period of time
        :rtype: float
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def CostPercent(self):
        r"""The ratio (in decimal form) of the total execution time of the slow query statement to that of all slow query statements during the specified period of time
        :rtype: float
        """
        return self._CostPercent

    @CostPercent.setter
    def CostPercent(self, CostPercent):
        self._CostPercent = CostPercent

    @property
    def MinCostTime(self):
        r"""The shortest execution time (in ms) of the slow query statement during the specified period of time
        :rtype: float
        """
        return self._MinCostTime

    @MinCostTime.setter
    def MinCostTime(self, MinCostTime):
        self._MinCostTime = MinCostTime

    @property
    def MaxCostTime(self):
        r"""The longest execution time (in ms) of the slow query statement during the specified period of time
        :rtype: float
        """
        return self._MaxCostTime

    @MaxCostTime.setter
    def MaxCostTime(self, MaxCostTime):
        self._MaxCostTime = MaxCostTime

    @property
    def AvgCostTime(self):
        r"""The average execution time (in ms) of the slow query statement during the specified period of time
        :rtype: float
        """
        return self._AvgCostTime

    @AvgCostTime.setter
    def AvgCostTime(self, AvgCostTime):
        self._AvgCostTime = AvgCostTime

    @property
    def FirstTime(self):
        r"""The timestamp when the slow query statement starts to execute for the first time during the specified period of time
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def LastTime(self):
        r"""The timestamp when the slow query statement starts to execute for the last time during the specified period of time
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._UserName = params.get("UserName")
        self._NormalQuery = params.get("NormalQuery")
        self._ClientAddr = params.get("ClientAddr")
        self._CallNum = params.get("CallNum")
        self._CallPercent = params.get("CallPercent")
        self._CostTime = params.get("CostTime")
        self._CostPercent = params.get("CostPercent")
        self._MinCostTime = params.get("MinCostTime")
        self._MaxCostTime = params.get("MaxCostTime")
        self._AvgCostTime = params.get("AvgCostTime")
        self._FirstTime = params.get("FirstTime")
        self._LastTime = params.get("LastTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadRestriction(AbstractModel):
    r"""Restriction information for downloading a backup

    """

    def __init__(self):
        r"""
        :param _RestrictionType: Backup file download limit type. valid values: NONE (unlimited, allows download from both private and public networks), INTRANET (only allows private network download), CUSTOMIZE (custom limits for download by vpc or ip). when the parameter value is CUSTOMIZE, at least one item must be filled in for vpc or ip information.
        :type RestrictionType: str
        :param _VpcRestrictionEffect: Whether VPC is allowed. Valid values: `ALLOW` (allow), `DENY` (deny).
        :type VpcRestrictionEffect: str
        :param _VpcIdSet: Whether it is allowed to download the VPC ID list of the backup files.
        :type VpcIdSet: list of str
        :param _IpRestrictionEffect: Whether IP is allowed. Valid values: `ALLOW` (allow), `DENY` (deny).
        :type IpRestrictionEffect: str
        :param _IpSet: Whether it is allowed to download IP list of the backup files.
        :type IpSet: list of str
        """
        self._RestrictionType = None
        self._VpcRestrictionEffect = None
        self._VpcIdSet = None
        self._IpRestrictionEffect = None
        self._IpSet = None

    @property
    def RestrictionType(self):
        r"""Backup file download limit type. valid values: NONE (unlimited, allows download from both private and public networks), INTRANET (only allows private network download), CUSTOMIZE (custom limits for download by vpc or ip). when the parameter value is CUSTOMIZE, at least one item must be filled in for vpc or ip information.
        :rtype: str
        """
        return self._RestrictionType

    @RestrictionType.setter
    def RestrictionType(self, RestrictionType):
        self._RestrictionType = RestrictionType

    @property
    def VpcRestrictionEffect(self):
        r"""Whether VPC is allowed. Valid values: `ALLOW` (allow), `DENY` (deny).
        :rtype: str
        """
        return self._VpcRestrictionEffect

    @VpcRestrictionEffect.setter
    def VpcRestrictionEffect(self, VpcRestrictionEffect):
        self._VpcRestrictionEffect = VpcRestrictionEffect

    @property
    def VpcIdSet(self):
        r"""Whether it is allowed to download the VPC ID list of the backup files.
        :rtype: list of str
        """
        return self._VpcIdSet

    @VpcIdSet.setter
    def VpcIdSet(self, VpcIdSet):
        self._VpcIdSet = VpcIdSet

    @property
    def IpRestrictionEffect(self):
        r"""Whether IP is allowed. Valid values: `ALLOW` (allow), `DENY` (deny).
        :rtype: str
        """
        return self._IpRestrictionEffect

    @IpRestrictionEffect.setter
    def IpRestrictionEffect(self, IpRestrictionEffect):
        self._IpRestrictionEffect = IpRestrictionEffect

    @property
    def IpSet(self):
        r"""Whether it is allowed to download IP list of the backup files.
        :rtype: list of str
        """
        return self._IpSet

    @IpSet.setter
    def IpSet(self, IpSet):
        self._IpSet = IpSet


    def _deserialize(self, params):
        self._RestrictionType = params.get("RestrictionType")
        self._VpcRestrictionEffect = params.get("VpcRestrictionEffect")
        self._VpcIdSet = params.get("VpcIdSet")
        self._IpRestrictionEffect = params.get("IpRestrictionEffect")
        self._IpSet = params.get("IpSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPlan(AbstractModel):
    r"""Backup plan

    """

    def __init__(self):
        r"""
        :param _BackupPeriod: Backup cycle
        :type BackupPeriod: str
        :param _BaseBackupRetentionPeriod: Data backup retention duration
        :type BaseBackupRetentionPeriod: int
        :param _MinBackupStartTime: The earliest time to start a backup
        :type MinBackupStartTime: str
        :param _MaxBackupStartTime: The latest time to start a backup
        :type MaxBackupStartTime: str
        """
        self._BackupPeriod = None
        self._BaseBackupRetentionPeriod = None
        self._MinBackupStartTime = None
        self._MaxBackupStartTime = None

    @property
    def BackupPeriod(self):
        r"""Backup cycle
        :rtype: str
        """
        return self._BackupPeriod

    @BackupPeriod.setter
    def BackupPeriod(self, BackupPeriod):
        self._BackupPeriod = BackupPeriod

    @property
    def BaseBackupRetentionPeriod(self):
        r"""Data backup retention duration
        :rtype: int
        """
        return self._BaseBackupRetentionPeriod

    @BaseBackupRetentionPeriod.setter
    def BaseBackupRetentionPeriod(self, BaseBackupRetentionPeriod):
        self._BaseBackupRetentionPeriod = BaseBackupRetentionPeriod

    @property
    def MinBackupStartTime(self):
        r"""The earliest time to start a backup
        :rtype: str
        """
        return self._MinBackupStartTime

    @MinBackupStartTime.setter
    def MinBackupStartTime(self, MinBackupStartTime):
        self._MinBackupStartTime = MinBackupStartTime

    @property
    def MaxBackupStartTime(self):
        r"""The latest time to start a backup
        :rtype: str
        """
        return self._MaxBackupStartTime

    @MaxBackupStartTime.setter
    def MaxBackupStartTime(self, MaxBackupStartTime):
        self._MaxBackupStartTime = MaxBackupStartTime


    def _deserialize(self, params):
        self._BackupPeriod = params.get("BackupPeriod")
        self._BaseBackupRetentionPeriod = params.get("BaseBackupRetentionPeriod")
        self._MinBackupStartTime = params.get("MinBackupStartTime")
        self._MaxBackupStartTime = params.get("MaxBackupStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSummary(AbstractModel):
    r"""Instance backup statistics

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _LogBackupCount: Number of log backups of an instance
        :type LogBackupCount: int
        :param _LogBackupSize: Size of log backups of an instance
        :type LogBackupSize: int
        :param _ManualBaseBackupCount: Number of manually created instance data backups.
        :type ManualBaseBackupCount: int
        :param _ManualBaseBackupSize: Size of manually created instance data backups.
        :type ManualBaseBackupSize: int
        :param _AutoBaseBackupCount: Number of automatically created instance data backups.
        :type AutoBaseBackupCount: int
        :param _AutoBaseBackupSize: Size of automatically created instance data backups.
        :type AutoBaseBackupSize: int
        :param _TotalBackupCount: Total number of backups
        :type TotalBackupCount: int
        :param _TotalBackupSize: Total backup size
        :type TotalBackupSize: int
        """
        self._DBInstanceId = None
        self._LogBackupCount = None
        self._LogBackupSize = None
        self._ManualBaseBackupCount = None
        self._ManualBaseBackupSize = None
        self._AutoBaseBackupCount = None
        self._AutoBaseBackupSize = None
        self._TotalBackupCount = None
        self._TotalBackupSize = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def LogBackupCount(self):
        r"""Number of log backups of an instance
        :rtype: int
        """
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def LogBackupSize(self):
        r"""Size of log backups of an instance
        :rtype: int
        """
        return self._LogBackupSize

    @LogBackupSize.setter
    def LogBackupSize(self, LogBackupSize):
        self._LogBackupSize = LogBackupSize

    @property
    def ManualBaseBackupCount(self):
        r"""Number of manually created instance data backups.
        :rtype: int
        """
        return self._ManualBaseBackupCount

    @ManualBaseBackupCount.setter
    def ManualBaseBackupCount(self, ManualBaseBackupCount):
        self._ManualBaseBackupCount = ManualBaseBackupCount

    @property
    def ManualBaseBackupSize(self):
        r"""Size of manually created instance data backups.
        :rtype: int
        """
        return self._ManualBaseBackupSize

    @ManualBaseBackupSize.setter
    def ManualBaseBackupSize(self, ManualBaseBackupSize):
        self._ManualBaseBackupSize = ManualBaseBackupSize

    @property
    def AutoBaseBackupCount(self):
        r"""Number of automatically created instance data backups.
        :rtype: int
        """
        return self._AutoBaseBackupCount

    @AutoBaseBackupCount.setter
    def AutoBaseBackupCount(self, AutoBaseBackupCount):
        self._AutoBaseBackupCount = AutoBaseBackupCount

    @property
    def AutoBaseBackupSize(self):
        r"""Size of automatically created instance data backups.
        :rtype: int
        """
        return self._AutoBaseBackupSize

    @AutoBaseBackupSize.setter
    def AutoBaseBackupSize(self, AutoBaseBackupSize):
        self._AutoBaseBackupSize = AutoBaseBackupSize

    @property
    def TotalBackupCount(self):
        r"""Total number of backups
        :rtype: int
        """
        return self._TotalBackupCount

    @TotalBackupCount.setter
    def TotalBackupCount(self, TotalBackupCount):
        self._TotalBackupCount = TotalBackupCount

    @property
    def TotalBackupSize(self):
        r"""Total backup size
        :rtype: int
        """
        return self._TotalBackupSize

    @TotalBackupSize.setter
    def TotalBackupSize(self, TotalBackupSize):
        self._TotalBackupSize = TotalBackupSize


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._LogBackupCount = params.get("LogBackupCount")
        self._LogBackupSize = params.get("LogBackupSize")
        self._ManualBaseBackupCount = params.get("ManualBaseBackupCount")
        self._ManualBaseBackupSize = params.get("ManualBaseBackupSize")
        self._AutoBaseBackupCount = params.get("AutoBaseBackupCount")
        self._AutoBaseBackupSize = params.get("AutoBaseBackupSize")
        self._TotalBackupCount = params.get("TotalBackupCount")
        self._TotalBackupSize = params.get("TotalBackupSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseBackup(AbstractModel):
    r"""Database data backup information

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _Id: Unique ID of a backup file
        :type Id: str
        :param _Name: Backup file name.
        :type Name: str
        :param _BackupMethod: Specifies the backup method: physical - physical backup, logical - logical backup.
        :type BackupMethod: str
        :param _BackupMode: Backup mode: automatic - automatic backup, manual - manual backup.
        :type BackupMode: str
        :param _State: Backup task status. valid values: init, running, finished, failed, canceled.
        :type State: str
        :param _Size: Backup set size in bytes
        :type Size: int
        :param _StartTime: Backup start time
        :type StartTime: str
        :param _FinishTime: Backup end time
        :type FinishTime: str
        :param _ExpireTime: Backup expiration time
        :type ExpireTime: str
        """
        self._DBInstanceId = None
        self._Id = None
        self._Name = None
        self._BackupMethod = None
        self._BackupMode = None
        self._State = None
        self._Size = None
        self._StartTime = None
        self._FinishTime = None
        self._ExpireTime = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Id(self):
        r"""Unique ID of a backup file
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Backup file name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BackupMethod(self):
        r"""Specifies the backup method: physical - physical backup, logical - logical backup.
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupMode(self):
        r"""Backup mode: automatic - automatic backup, manual - manual backup.
        :rtype: str
        """
        return self._BackupMode

    @BackupMode.setter
    def BackupMode(self, BackupMode):
        self._BackupMode = BackupMode

    @property
    def State(self):
        r"""Backup task status. valid values: init, running, finished, failed, canceled.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Size(self):
        r"""Backup set size in bytes
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def StartTime(self):
        r"""Backup start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        r"""Backup end time
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def ExpireTime(self):
        r"""Backup expiration time
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupMode = params.get("BackupMode")
        self._State = params.get("State")
        self._Size = params.get("Size")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassInfo(AbstractModel):
    r"""Database instance specification

    """

    def __init__(self):
        r"""
        :param _SpecCode: Specification ID
        :type SpecCode: str
        :param _CPU: Number of CPU cores
        :type CPU: int
        :param _Memory: Memory size in MB
        :type Memory: int
        :param _MaxStorage: Maximum storage capacity in GB supported by this specification
        :type MaxStorage: int
        :param _MinStorage: Minimum storage capacity in GB supported by this specification
        :type MinStorage: int
        :param _QPS: Estimated QPS for this specification
        :type QPS: int
        """
        self._SpecCode = None
        self._CPU = None
        self._Memory = None
        self._MaxStorage = None
        self._MinStorage = None
        self._QPS = None

    @property
    def SpecCode(self):
        r"""Specification ID
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def CPU(self):
        r"""Number of CPU cores
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        r"""Memory size in MB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def MaxStorage(self):
        r"""Maximum storage capacity in GB supported by this specification
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def MinStorage(self):
        r"""Minimum storage capacity in GB supported by this specification
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def QPS(self):
        r"""Estimated QPS for this specification
        :rtype: int
        """
        return self._QPS

    @QPS.setter
    def QPS(self, QPS):
        self._QPS = QPS


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._MaxStorage = params.get("MaxStorage")
        self._MinStorage = params.get("MinStorage")
        self._QPS = params.get("QPS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBInstanceRequest(AbstractModel):
    r"""CloneDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: The source instance ID to be cloned. can be obtained through the DescribeDBInstances api (https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1).
        :type DBInstanceId: str
        :param _SpecCode: Purchasable code, which can be obtained from the `SpecCode` field in the return value of the [DescribeClasses](https://intl.cloud.tencent.com/document/api/409/89019?from_cn_redirect=1) API.
        :type SpecCode: str
        :param _Storage: Instance disk capacity size. set step size to 10. unit: GB.
        :type Storage: int
        :param _Period: Purchase duration, in months.

- Prepaid: Supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.
- Pay-as-you-go: Only supports `1`.

        :type Period: int
        :param _AutoRenewFlag: Specifies the auto-renewal flag. this parameter is valid only when the billing mode is prepaid.
Valid values:.

- `0`: specifies manual renewal.
-`1`: specifies auto-renewal.

Default value: 0
        :type AutoRenewFlag: int
        :param _VpcId: VPC ID in the format of `vpc-xxxxxxx`, which can be obtained in the console or from the `unVpcId` field in the return value of the [DescribeVpcEx](https://intl.cloud.tencent.com/document/api/215/1372?from_cn_redirect=1) API.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID in the format of `subnet-xxxxxxxx`, which can be obtained in the console or from the `unSubnetId` field in the return value of the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API.
        :type SubnetId: str
        :param _Name: Specifies the instance name for new purchase, only supports chinese/english/digits/"_"/"-" with length less than 60. displays "source instance name-Copy" by default if no instance name is specified.
        :type Name: str
        :param _InstanceChargeType: Instance billing type, which currently supports:

- PREPAID: Prepaid, i.e., yearly/monthly subscription
- POSTPAID_BY_HOUR: Pay-as-you-go, i.e., pay by consumption

Default value: PREPAID
        :type InstanceChargeType: str
        :param _SecurityGroupIds: Security group to which an instance belongs. obtain this parameter by calling the SecurityGroupId field in the return value of [DescribeSecurityGroups](https://www.tencentcloud.comom/document/api/215/15808?from_cn_redirect=1). if not specified, the default security group is bound.

        :type SecurityGroupIds: list of str
        :param _ProjectId: Project ID. default value is 0, which means it belongs to the default project.
        :type ProjectId: int
        :param _TagList: The information of tags to be bound with the instance, which is left empty by default. This parameter can be obtained from the `Tags` field in the return value of the [DescribeTags](https://intl.cloud.tencent.com/document/api/651/35316?from_cn_redirect=1) API.
        :type TagList: list of Tag
        :param _DBNodeSet: Deployment information of instance nodes. the availability zone of primary and secondary nodes is required. when multi-availability zone deployment is supported, the availability zone information for each node must be specified.
AZ information can be obtained by calling the DescribeZones api (https://www.tencentcloud.comom/document/api/409/16769?from_cn_redirect=1) and checking the Zone field in the returned value.
        :type DBNodeSet: list of DBNode
        :param _AutoVoucher: Whether to automatically use coupons:

- 0: No
- 1: Yes

Default value: 0
        :type AutoVoucher: int
        :param _VoucherIds: Voucher ID list.
        :type VoucherIds: str
        :param _ActivityId: Campaign ID.
        :type ActivityId: int
        :param _BackupSetId: Basic backup set ID. either `BackupSetId` or `RecoveryTargetTime` must be provided, and cannot include both.
        :type BackupSetId: str
        :param _RecoveryTargetTime: Specifies the recovery time point. either `BackupSetId` or `RecoveryTargetTime` must be provided, and cannot include both.
        :type RecoveryTargetTime: str
        :param _SyncMode: Primary-standby sync mode, which supports:
<li>Semi-sync: Semi-sync</li>
<li>Async: Asynchronous</li>
Default value for the primary instance: Semi-sync
Default value for the read-only instance: Async
        :type SyncMode: str
        :param _DeletionProtection: Specifies whether to enable deletion protection for the instance. valid values: true (enable deletion protection), false (disable deletion protection).
        :type DeletionProtection: bool
        """
        self._DBInstanceId = None
        self._SpecCode = None
        self._Storage = None
        self._Period = None
        self._AutoRenewFlag = None
        self._VpcId = None
        self._SubnetId = None
        self._Name = None
        self._InstanceChargeType = None
        self._SecurityGroupIds = None
        self._ProjectId = None
        self._TagList = None
        self._DBNodeSet = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ActivityId = None
        self._BackupSetId = None
        self._RecoveryTargetTime = None
        self._SyncMode = None
        self._DeletionProtection = None

    @property
    def DBInstanceId(self):
        r"""The source instance ID to be cloned. can be obtained through the DescribeDBInstances api (https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def SpecCode(self):
        r"""Purchasable code, which can be obtained from the `SpecCode` field in the return value of the [DescribeClasses](https://intl.cloud.tencent.com/document/api/409/89019?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Storage(self):
        r"""Instance disk capacity size. set step size to 10. unit: GB.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Period(self):
        r"""Purchase duration, in months.

- Prepaid: Supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.
- Pay-as-you-go: Only supports `1`.

        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoRenewFlag(self):
        r"""Specifies the auto-renewal flag. this parameter is valid only when the billing mode is prepaid.
Valid values:.

- `0`: specifies manual renewal.
-`1`: specifies auto-renewal.

Default value: 0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def VpcId(self):
        r"""VPC ID in the format of `vpc-xxxxxxx`, which can be obtained in the console or from the `unVpcId` field in the return value of the [DescribeVpcEx](https://intl.cloud.tencent.com/document/api/215/1372?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""VPC subnet ID in the format of `subnet-xxxxxxxx`, which can be obtained in the console or from the `unSubnetId` field in the return value of the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Name(self):
        r"""Specifies the instance name for new purchase, only supports chinese/english/digits/"_"/"-" with length less than 60. displays "source instance name-Copy" by default if no instance name is specified.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InstanceChargeType(self):
        r"""Instance billing type, which currently supports:

- PREPAID: Prepaid, i.e., yearly/monthly subscription
- POSTPAID_BY_HOUR: Pay-as-you-go, i.e., pay by consumption

Default value: PREPAID
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SecurityGroupIds(self):
        r"""Security group to which an instance belongs. obtain this parameter by calling the SecurityGroupId field in the return value of [DescribeSecurityGroups](https://www.tencentcloud.comom/document/api/215/15808?from_cn_redirect=1). if not specified, the default security group is bound.

        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ProjectId(self):
        r"""Project ID. default value is 0, which means it belongs to the default project.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TagList(self):
        r"""The information of tags to be bound with the instance, which is left empty by default. This parameter can be obtained from the `Tags` field in the return value of the [DescribeTags](https://intl.cloud.tencent.com/document/api/651/35316?from_cn_redirect=1) API.
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def DBNodeSet(self):
        r"""Deployment information of instance nodes. the availability zone of primary and secondary nodes is required. when multi-availability zone deployment is supported, the availability zone information for each node must be specified.
AZ information can be obtained by calling the DescribeZones api (https://www.tencentcloud.comom/document/api/409/16769?from_cn_redirect=1) and checking the Zone field in the returned value.
        :rtype: list of DBNode
        """
        return self._DBNodeSet

    @DBNodeSet.setter
    def DBNodeSet(self, DBNodeSet):
        self._DBNodeSet = DBNodeSet

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use coupons:

- 0: No
- 1: Yes

Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID list.
        :rtype: str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ActivityId(self):
        r"""Campaign ID.
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def BackupSetId(self):
        r"""Basic backup set ID. either `BackupSetId` or `RecoveryTargetTime` must be provided, and cannot include both.
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def RecoveryTargetTime(self):
        r"""Specifies the recovery time point. either `BackupSetId` or `RecoveryTargetTime` must be provided, and cannot include both.
        :rtype: str
        """
        return self._RecoveryTargetTime

    @RecoveryTargetTime.setter
    def RecoveryTargetTime(self, RecoveryTargetTime):
        self._RecoveryTargetTime = RecoveryTargetTime

    @property
    def SyncMode(self):
        r"""Primary-standby sync mode, which supports:
<li>Semi-sync: Semi-sync</li>
<li>Async: Asynchronous</li>
Default value for the primary instance: Semi-sync
Default value for the read-only instance: Async
        :rtype: str
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def DeletionProtection(self):
        r"""Specifies whether to enable deletion protection for the instance. valid values: true (enable deletion protection), false (disable deletion protection).
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._SpecCode = params.get("SpecCode")
        self._Storage = params.get("Storage")
        self._Period = params.get("Period")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Name = params.get("Name")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        if params.get("DBNodeSet") is not None:
            self._DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self._DBNodeSet.append(obj)
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._ActivityId = params.get("ActivityId")
        self._BackupSetId = params.get("BackupSetId")
        self._RecoveryTargetTime = params.get("RecoveryTargetTime")
        self._SyncMode = params.get("SyncMode")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBInstanceResponse(AbstractModel):
    r"""CloneDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order number.
        :type DealName: str
        :param _BillId: Order transaction number.
        :type BillId: str
        :param _DBInstanceId: Specifies the instance ID of the cloned instance. only support postpaid return this value.
        :type DBInstanceId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._BillId = None
        self._DBInstanceId = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order number.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def BillId(self):
        r"""Order transaction number.
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def DBInstanceId(self):
        r"""Specifies the instance ID of the cloned instance. only support postpaid return this value.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

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
        self._DealName = params.get("DealName")
        self._BillId = params.get("BillId")
        self._DBInstanceId = params.get("DBInstanceId")
        self._RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    r"""CloseDBExtranetAccess request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Specifies the instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en). such as postgres-6r233v55.
        :type DBInstanceId: str
        :param _IsIpv6: Specifies whether to close public network Ipv6. 1: yes. 0: no. default value: 0.
        :type IsIpv6: int
        """
        self._DBInstanceId = None
        self._IsIpv6 = None

    @property
    def DBInstanceId(self):
        r"""Specifies the instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en). such as postgres-6r233v55.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def IsIpv6(self):
        r"""Specifies whether to close public network Ipv6. 1: yes. 0: no. default value: 0.
        :rtype: int
        """
        return self._IsIpv6

    @IsIpv6.setter
    def IsIpv6(self, IsIpv6):
        self._IsIpv6 = IsIpv6


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._IsIpv6 = params.get("IsIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseDBExtranetAccessResponse(AbstractModel):
    r"""CloseDBExtranetAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID. FlowId is equivalent to TaskId.
        :type FlowId: int
        :param _TaskId: Task ID.
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Process ID. FlowId is equivalent to TaskId.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""Task ID.
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
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CloseServerlessDBExtranetAccessRequest(AbstractModel):
    r"""CloseServerlessDBExtranetAccess request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Unique ID of an instance
        :type DBInstanceId: str
        :param _DBInstanceName: Instance name
        :type DBInstanceName: str
        """
        self._DBInstanceId = None
        self._DBInstanceName = None

    @property
    def DBInstanceId(self):
        r"""Unique ID of an instance
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DBInstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._DBInstanceName

    @DBInstanceName.setter
    def DBInstanceName(self, DBInstanceName):
        self._DBInstanceName = DBInstanceName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._DBInstanceName = params.get("DBInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseServerlessDBExtranetAccessResponse(AbstractModel):
    r"""CloseServerlessDBExtranetAccess response structure.

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


class CreateAccountRequest(AbstractModel):
    r"""CreateAccount request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. can be obtained through the DescribeDBInstances api (https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _UserName: The name of the account created. Consists of letters (a-z, A-Z), numbers (0-9), underscores (_), starts with a letter or (_), up to 63 characters. Cannot use system reserved keywords, cannot be postgres, and cannot begin with pg_or tencentdb_
        :type UserName: str
        :param _Type: Account type. currently supported: normal, tencentDBSuper. normal references a general user, tencentDBSuper is an account that possesses the pg_tencentdb_superuser role.
        :type Type: str
        :param _Password: Specifies the corresponding password for the account. the password rules are as follows:.
<Li>Specifies a length of 8 to 32 characters. a password of more than 12 characters is recommended.</li>.
<Li>Cannot start with "/".</li>.
<Li>Specifies the following four items must be included.</li>.

Valid values: a to z (lowercase letters).           
Uppercase letters: A - Z.
Valid values: 0 - 9.
Special symbols: ()`~!@#$%^&*-+=_|{}[]:<>,.?/.

        :type Password: str
        :param _Remark: Account remark. only allow english letters, digits, underscore, hyphen, and chinese characters, limited to 60 characters.
        :type Remark: str
        :param _OpenCam: Specifies whether CAM verification is enabled for the account.
        :type OpenCam: bool
        """
        self._DBInstanceId = None
        self._UserName = None
        self._Type = None
        self._Password = None
        self._Remark = None
        self._OpenCam = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. can be obtained through the DescribeDBInstances api (https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""The name of the account created. Consists of letters (a-z, A-Z), numbers (0-9), underscores (_), starts with a letter or (_), up to 63 characters. Cannot use system reserved keywords, cannot be postgres, and cannot begin with pg_or tencentdb_
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Type(self):
        r"""Account type. currently supported: normal, tencentDBSuper. normal references a general user, tencentDBSuper is an account that possesses the pg_tencentdb_superuser role.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Password(self):
        r"""Specifies the corresponding password for the account. the password rules are as follows:.
<Li>Specifies a length of 8 to 32 characters. a password of more than 12 characters is recommended.</li>.
<Li>Cannot start with "/".</li>.
<Li>Specifies the following four items must be included.</li>.

Valid values: a to z (lowercase letters).           
Uppercase letters: A - Z.
Valid values: 0 - 9.
Special symbols: ()`~!@#$%^&*-+=_|{}[]:<>,.?/.

        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Remark(self):
        r"""Account remark. only allow english letters, digits, underscore, hyphen, and chinese characters, limited to 60 characters.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def OpenCam(self):
        r"""Specifies whether CAM verification is enabled for the account.
        :rtype: bool
        """
        return self._OpenCam

    @OpenCam.setter
    def OpenCam(self, OpenCam):
        self._OpenCam = OpenCam


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        self._Type = params.get("Type")
        self._Password = params.get("Password")
        self._Remark = params.get("Remark")
        self._OpenCam = params.get("OpenCam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    r"""CreateAccount response structure.

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


class CreateBackupPlanRequest(AbstractModel):
    r"""CreateBackupPlan request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _PlanName: Specifies the name of the backup plan.
        :type PlanName: str
        :param _BackupPeriodType: Specifies the schedule type of the backup created. currently only support month.
        :type BackupPeriodType: str
        :param _BackupPeriod: Backup date. example: enable backup on the 2nd of every month.
        :type BackupPeriod: list of str
        :param _MinBackupStartTime: Specifies the backup start time. if not passed, it follows the default backup plan.
        :type MinBackupStartTime: str
        :param _MaxBackupStartTime: Backup end time. follows the default plan if not specified.
        :type MaxBackupStartTime: str
        :param _BaseBackupRetentionPeriod: Specifies the data backup retention duration in days. value range: [0,30000).
BackupPeriodType defaults to 7 when set to week and 31 when set to month.
        :type BaseBackupRetentionPeriod: int
        """
        self._DBInstanceId = None
        self._PlanName = None
        self._BackupPeriodType = None
        self._BackupPeriod = None
        self._MinBackupStartTime = None
        self._MaxBackupStartTime = None
        self._BaseBackupRetentionPeriod = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def PlanName(self):
        r"""Specifies the name of the backup plan.
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def BackupPeriodType(self):
        r"""Specifies the schedule type of the backup created. currently only support month.
        :rtype: str
        """
        return self._BackupPeriodType

    @BackupPeriodType.setter
    def BackupPeriodType(self, BackupPeriodType):
        self._BackupPeriodType = BackupPeriodType

    @property
    def BackupPeriod(self):
        r"""Backup date. example: enable backup on the 2nd of every month.
        :rtype: list of str
        """
        return self._BackupPeriod

    @BackupPeriod.setter
    def BackupPeriod(self, BackupPeriod):
        self._BackupPeriod = BackupPeriod

    @property
    def MinBackupStartTime(self):
        r"""Specifies the backup start time. if not passed, it follows the default backup plan.
        :rtype: str
        """
        return self._MinBackupStartTime

    @MinBackupStartTime.setter
    def MinBackupStartTime(self, MinBackupStartTime):
        self._MinBackupStartTime = MinBackupStartTime

    @property
    def MaxBackupStartTime(self):
        r"""Backup end time. follows the default plan if not specified.
        :rtype: str
        """
        return self._MaxBackupStartTime

    @MaxBackupStartTime.setter
    def MaxBackupStartTime(self, MaxBackupStartTime):
        self._MaxBackupStartTime = MaxBackupStartTime

    @property
    def BaseBackupRetentionPeriod(self):
        r"""Specifies the data backup retention duration in days. value range: [0,30000).
BackupPeriodType defaults to 7 when set to week and 31 when set to month.
        :rtype: int
        """
        return self._BaseBackupRetentionPeriod

    @BaseBackupRetentionPeriod.setter
    def BaseBackupRetentionPeriod(self, BaseBackupRetentionPeriod):
        self._BaseBackupRetentionPeriod = BaseBackupRetentionPeriod


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._PlanName = params.get("PlanName")
        self._BackupPeriodType = params.get("BackupPeriodType")
        self._BackupPeriod = params.get("BackupPeriod")
        self._MinBackupStartTime = params.get("MinBackupStartTime")
        self._MaxBackupStartTime = params.get("MaxBackupStartTime")
        self._BaseBackupRetentionPeriod = params.get("BaseBackupRetentionPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupPlanResponse(AbstractModel):
    r"""CreateBackupPlan response structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Backup policy ID.
        :type PlanId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PlanId = None
        self._RequestId = None

    @property
    def PlanId(self):
        r"""Backup policy ID.
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

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
        self._PlanId = params.get("PlanId")
        self._RequestId = params.get("RequestId")


class CreateBaseBackupRequest(AbstractModel):
    r"""CreateBaseBackup request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBaseBackupResponse(AbstractModel):
    r"""CreateBaseBackup response structure.

    """

    def __init__(self):
        r"""
        :param _BaseBackupId: Data backup set ID
        :type BaseBackupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BaseBackupId = None
        self._RequestId = None

    @property
    def BaseBackupId(self):
        r"""Data backup set ID
        :rtype: str
        """
        return self._BaseBackupId

    @BaseBackupId.setter
    def BaseBackupId(self, BaseBackupId):
        self._BaseBackupId = BaseBackupId

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
        self._BaseBackupId = params.get("BaseBackupId")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceNetworkAccessRequest(AbstractModel):
    r"""CreateDBInstanceNetworkAccess request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Specifies the instance ID, such as postgres-6bwgamo3. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773).
        :type DBInstanceId: str
        :param _VpcId: Unified VPC ID.
        :type VpcId: str
        :param _SubnetId: Subnet ID.
        :type SubnetId: str
        :param _IsAssignVip: Whether to manually assign the VIP. Valid values: `true` (manually assign), `false` (automatically assign).
        :type IsAssignVip: bool
        :param _Vip: Target VIP address. when this parameter is not specified and IsAssignVip is true, the system automatically assigns a VIP by default.
        :type Vip: str
        """
        self._DBInstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._IsAssignVip = None
        self._Vip = None

    @property
    def DBInstanceId(self):
        r"""Specifies the instance ID, such as postgres-6bwgamo3. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def VpcId(self):
        r"""Unified VPC ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def IsAssignVip(self):
        r"""Whether to manually assign the VIP. Valid values: `true` (manually assign), `false` (automatically assign).
        :rtype: bool
        """
        return self._IsAssignVip

    @IsAssignVip.setter
    def IsAssignVip(self, IsAssignVip):
        self._IsAssignVip = IsAssignVip

    @property
    def Vip(self):
        r"""Target VIP address. when this parameter is not specified and IsAssignVip is true, the system automatically assigns a VIP by default.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._IsAssignVip = params.get("IsAssignVip")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceNetworkAccessResponse(AbstractModel):
    r"""CreateDBInstanceNetworkAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID. FlowId is equivalent to TaskId.
        :type FlowId: int
        :param _TaskId: Task ID.
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Process ID. FlowId is equivalent to TaskId.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""Task ID.
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
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    r"""CreateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _SpecCode: Purchasable specification ID, which can be obtained through the `SpecCode` field in the returned value of the `DescribeClasses` API.
        :type SpecCode: str
        :param _Storage: Instance capacity size in GB.
        :type Storage: int
        :param _InstanceCount: Number of instances purchased at a time. Value range: 1-100.
        :type InstanceCount: int
        :param _Period: Length of purchase in months. Currently, only 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36 are supported.
        :type Period: int
        :param _Zone: AZ ID, which can be obtained through the `Zone` field in the returned value of the `DescribeZones` API.
        :type Zone: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _DBVersion: PostgreSQL community major version + minor version number.
It's generally not recommended to pass in this parameter. If needed, only the latest minor version number under the current major version can be passed.
        :type DBVersion: str
        :param _InstanceChargeType: Instance billing type.
        :type InstanceChargeType: str
        :param _AutoVoucher: Whether to automatically use vouchers. 1: yes, 0: no. Default value: no.
        :type AutoVoucher: int
        :param _VoucherIds: Voucher ID list (only one voucher can be specified currently).
        :type VoucherIds: list of str
        :param _VpcId: VPC ID.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID.
        :type SubnetId: str
        :param _AutoRenewFlag: Renewal flag. 0: normal renewal (default), 1: auto-renewal.
        :type AutoRenewFlag: int
        :param _ActivityId: Activity ID
        :type ActivityId: int
        :param _Name: Instance name (which will be supported in the future)
        :type Name: str
        :param _NeedSupportIpv6: Whether to support IPv6 address access. Valid values: 1 (yes), 0 (no)
        :type NeedSupportIpv6: int
        :param _TagList: The information of tags to be associated with instances. This parameter is left empty by default.
        :type TagList: list of Tag
        :param _SecurityGroupIds: Security group ID
        :type SecurityGroupIds: list of str
        :param _DBMajorVersion: The major version number of PostgreSQL (this parameter is currently required), and the version information can be obtained from [DescribeDBVersions](https://intl.cloud.tencent.com/document/api/409/89018?from_cn_redirect=1). Currently major versions `10`, `11`, `12`, `13`, `14`, and `15` are supported. For details, see [Kernel Version Overview](https://intl.cloud.tencent.com/document/product/409/67018).
When this parameter is entered, an instance running the latest kernel version of the latest minor version will be created based on this major version number.
        :type DBMajorVersion: str
        :param _DBKernelVersion: PostgreSQL kernel version number.
It's generally not recommended to pass in this parameter. If needed, only the latest kernel version number under the current major version can be passed.
        :type DBKernelVersion: str
        """
        self._SpecCode = None
        self._Storage = None
        self._InstanceCount = None
        self._Period = None
        self._Zone = None
        self._ProjectId = None
        self._DBVersion = None
        self._InstanceChargeType = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._VpcId = None
        self._SubnetId = None
        self._AutoRenewFlag = None
        self._ActivityId = None
        self._Name = None
        self._NeedSupportIpv6 = None
        self._TagList = None
        self._SecurityGroupIds = None
        self._DBMajorVersion = None
        self._DBKernelVersion = None

    @property
    def SpecCode(self):
        r"""Purchasable specification ID, which can be obtained through the `SpecCode` field in the returned value of the `DescribeClasses` API.
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Storage(self):
        r"""Instance capacity size in GB.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceCount(self):
        r"""Number of instances purchased at a time. Value range: 1-100.
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Period(self):
        r"""Length of purchase in months. Currently, only 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36 are supported.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Zone(self):
        r"""AZ ID, which can be obtained through the `Zone` field in the returned value of the `DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def DBVersion(self):
        r"""PostgreSQL community major version + minor version number.
It's generally not recommended to pass in this parameter. If needed, only the latest minor version number under the current major version can be passed.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def InstanceChargeType(self):
        r"""Instance billing type.
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use vouchers. 1: yes, 0: no. Default value: no.
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID list (only one voucher can be specified currently).
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def VpcId(self):
        r"""VPC ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""VPC subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AutoRenewFlag(self):
        r"""Renewal flag. 0: normal renewal (default), 1: auto-renewal.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ActivityId(self):
        r"""Activity ID
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def Name(self):
        r"""Instance name (which will be supported in the future)
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NeedSupportIpv6(self):
        r"""Whether to support IPv6 address access. Valid values: 1 (yes), 0 (no)
        :rtype: int
        """
        return self._NeedSupportIpv6

    @NeedSupportIpv6.setter
    def NeedSupportIpv6(self, NeedSupportIpv6):
        self._NeedSupportIpv6 = NeedSupportIpv6

    @property
    def TagList(self):
        r"""The information of tags to be associated with instances. This parameter is left empty by default.
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SecurityGroupIds(self):
        r"""Security group ID
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def DBMajorVersion(self):
        r"""The major version number of PostgreSQL (this parameter is currently required), and the version information can be obtained from [DescribeDBVersions](https://intl.cloud.tencent.com/document/api/409/89018?from_cn_redirect=1). Currently major versions `10`, `11`, `12`, `13`, `14`, and `15` are supported. For details, see [Kernel Version Overview](https://intl.cloud.tencent.com/document/product/409/67018).
When this parameter is entered, an instance running the latest kernel version of the latest minor version will be created based on this major version number.
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBKernelVersion(self):
        r"""PostgreSQL kernel version number.
It's generally not recommended to pass in this parameter. If needed, only the latest kernel version number under the current major version can be passed.
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._Storage = params.get("Storage")
        self._InstanceCount = params.get("InstanceCount")
        self._Period = params.get("Period")
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        self._DBVersion = params.get("DBVersion")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ActivityId = params.get("ActivityId")
        self._Name = params.get("Name")
        self._NeedSupportIpv6 = params.get("NeedSupportIpv6")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
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
        :param _DealNames: Order number list. Each instance corresponds to an order number.
        :type DealNames: list of str
        :param _BillId: Bill ID of frozen fees
        :type BillId: str
        :param _DBInstanceIdSet: ID set of instances which have been created successfully. The parameter value will be returned only when the billing mode is postpaid.
        :type DBInstanceIdSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealNames = None
        self._BillId = None
        self._DBInstanceIdSet = None
        self._RequestId = None

    @property
    def DealNames(self):
        r"""Order number list. Each instance corresponds to an order number.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def BillId(self):
        r"""Bill ID of frozen fees
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def DBInstanceIdSet(self):
        r"""ID set of instances which have been created successfully. The parameter value will be returned only when the billing mode is postpaid.
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

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
        self._DealNames = params.get("DealNames")
        self._BillId = params.get("BillId")
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._RequestId = params.get("RequestId")


class CreateDatabaseRequest(AbstractModel):
    r"""CreateDatabase request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Specifies the instance ID, such as postgres-6fego161. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :type DBInstanceId: str
        :param _DatabaseName: Specifies the user-created database name.
Name specification: consists of letters (a-z, a-z), digits (0-9), and underscores (_), starting with a letter or underscore (_), up to 63 characters. system reserved keywords cannot be used, and 'postgres' is not allowed.
        :type DatabaseName: str
        :param _DatabaseOwner: Owner of the database. obtain through the api [DescribeAccounts](https://www.tencentcloud.com/document/api/409/18109?from_cn_redirect=1).
        :type DatabaseOwner: str
        :param _Encoding: Specifies the character encoding of the database.
Supported character sets include UTF8, LATIN1, LATIN2, WIN1250, WIN1251, WIN1252, KOI8R, EUC_JP, and EUC_KR.
Default value: UTF8.
        :type Encoding: str
        :param _Collate: Specifies the database sorting rule.
        :type Collate: str
        :param _Ctype: Specifies the character category of the database.
        :type Ctype: str
        """
        self._DBInstanceId = None
        self._DatabaseName = None
        self._DatabaseOwner = None
        self._Encoding = None
        self._Collate = None
        self._Ctype = None

    @property
    def DBInstanceId(self):
        r"""Specifies the instance ID, such as postgres-6fego161. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DatabaseName(self):
        r"""Specifies the user-created database name.
Name specification: consists of letters (a-z, a-z), digits (0-9), and underscores (_), starting with a letter or underscore (_), up to 63 characters. system reserved keywords cannot be used, and 'postgres' is not allowed.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatabaseOwner(self):
        r"""Owner of the database. obtain through the api [DescribeAccounts](https://www.tencentcloud.com/document/api/409/18109?from_cn_redirect=1).
        :rtype: str
        """
        return self._DatabaseOwner

    @DatabaseOwner.setter
    def DatabaseOwner(self, DatabaseOwner):
        self._DatabaseOwner = DatabaseOwner

    @property
    def Encoding(self):
        r"""Specifies the character encoding of the database.
Supported character sets include UTF8, LATIN1, LATIN2, WIN1250, WIN1251, WIN1252, KOI8R, EUC_JP, and EUC_KR.
Default value: UTF8.
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Collate(self):
        r"""Specifies the database sorting rule.
        :rtype: str
        """
        return self._Collate

    @Collate.setter
    def Collate(self, Collate):
        self._Collate = Collate

    @property
    def Ctype(self):
        r"""Specifies the character category of the database.
        :rtype: str
        """
        return self._Ctype

    @Ctype.setter
    def Ctype(self, Ctype):
        self._Ctype = Ctype


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._DatabaseName = params.get("DatabaseName")
        self._DatabaseOwner = params.get("DatabaseOwner")
        self._Encoding = params.get("Encoding")
        self._Collate = params.get("Collate")
        self._Ctype = params.get("Ctype")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatabaseResponse(AbstractModel):
    r"""CreateDatabase response structure.

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


class CreateInstancesRequest(AbstractModel):
    r"""CreateInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: <p>The primary availability zone of the instance, for example: ap-guangzhou-3. If needed to support multiple AZs, add primary and secondary AZ information in the DBNodeSet.N field.<br>AZ information can be obtained by calling the <a href="https://www.tencentcloud.com/document/api/409/16769?from_cn_redirect=1">DescribeZones</a> api and checking the Zone field in the returned value.</p>
        :type Zone: str
        :param _SpecCode: <p>Purchasable specification code. Obtain this parameter by calling the `SpecCode` field in the return value of <a href="https://www.tencentcloud.com/document/api/409/89019?from_cn_redirect=1">DescribeClasses</a>.</p>
        :type SpecCode: str
        :param _Storage: <p>Instance disk capacity size, unit: GB. The step length for parameter settings is 10.</p>
        :type Storage: int
        :param _InstanceCount: <p>Number of instances to purchase, value ranges from 1 to 10. Single transaction supports a maximum quantity of 10. If exceeding this quantity, multiple calls can be performed to purchase.</p>
        :type InstanceCount: int
        :param _Period: <p>Purchase duration, unit: month.</p><li>Prepaid: Supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.</li><li>Postpaid: Supports only `1`.</li>
        :type Period: int
        :param _Charset: <p>Instance character set, which currently supports only:</p><li>UTF8</li><li>LATIN1</li>
        :type Charset: str
        :param _AdminName: <p>Username of the instance root account. Specific specifications are as follows:</p><li>The username must consist of 1-16 characters, which can only be letters, digits, or underscores.</li><li>Cannot be postgres.</li><li>Cannot begin with digits or pg_.</li><li>All rules are case-insensitive.</li>
        :type AdminName: str
        :param _AdminPassword: <p>Password for the instance root account username, with a length of 8-32 characters. It is recommended to use a password of more than 12 characters and it cannot start with "/".<br>Must contain the following four character types:</p><li>Lowercase letter: [a-z]</li><li>Uppercase letter: [a-z]</li><li>Number: 0-9</li><li>Special character: ()`~!@#$%^&*-+=_|{}[]:;'<>,.?/</li>
        :type AdminPassword: str
        :param _DBMajorVersion: <p>PostgreSQL major version number (this parameter is currently required). Version information can be obtained from <a href="https://www.tencentcloud.com/document/api/409/89018?from_cn_redirect=1">DescribeDBVersions</a>. Currently supports major versions 10, 11, 12, 13, 14, and 15. For details, see <a href="https://www.tencentcloud.com/document/product/409/67018?from_cn_redirect=1">kernel version overview</a>.<br>When this parameter is entered, an instance running the latest kernel version of the latest minor version will be created based on this major version number.</p>
        :type DBMajorVersion: str
        :param _DBVersion: <p>PostgreSQL community major version + minor version number.<br>It's generally not recommended to pass in this parameter. If needed, only the latest minor version number under the current major version can be passed.</p>
        :type DBVersion: str
        :param _DBKernelVersion: <p>PostgreSQL kernel version number.<br>It's generally not recommended to pass in this parameter. If needed, only the latest kernel version number under the current major version can be passed.</p>
        :type DBKernelVersion: str
        :param _InstanceChargeType: <p>Instance billing type. Currently supports:</p><li>PREPAID: Prepayment, i.e., yearly/monthly subscription</li><li>POSTPAID_BY_HOUR: Postpaid, i.e., pay-as-you-go</li>Default value: PREPAID
        :type InstanceChargeType: str
        :param _VpcId: <p>VPC ID, such as vpc-xxxxxxxx (this parameter is currently required). A valid VPC ID can be obtained by logging in to the console to query or by calling the API <a href="https://www.tencentcloud.com/document/api/215/1372?from_cn_redirect=1">DescribeVpcEx</a> and acquiring the unVpcId field in the API return.</p>
        :type VpcId: str
        :param _SubnetId: <p>VPC subnet ID, such as subnet-xxxxxxxx (this parameter is currently required). Effective VPC subnet IDs can be queried by logging in to the console or by calling the API <a href="https://www.tencentcloud.com/document/api/215/15784?from_cn_redirect=1">DescribeSubnets</a> and acquiring the unSubnetId field in the API return.</p>
        :type SubnetId: str
        :param _DBNodeSet: <p>Instance node deployment information. When multi-availability zone deployment is supported, it requires specifying the AZ information for each node.<br>AZ information can be obtained from the Zone field in the returned value by calling the <a href="https://www.tencentcloud.com/document/api/409/16769?from_cn_redirect=1">DescribeZones</a> API.</p>
        :type DBNodeSet: list of DBNode
        :param _AutoRenewFlag: <p>Auto-renewal flag:</p><li>0: Manual renewal</li><li>1: Auto renewal</li>Default value: 0
        :type AutoRenewFlag: int
        :param _AutoVoucher: <p>Whether to automatically use a voucher:</p><li>0: No</li><li>1: Yes</li>Default value: 0
        :type AutoVoucher: int
        :param _VoucherIds: <p>Voucher ID list. Currently only support specifying one voucher.</p>
        :type VoucherIds: list of str
        :param _ProjectId: <p>Project ID. The default value is 0, which means it belongs to the default project.</p>
        :type ProjectId: int
        :param _ActivityId: <p>Activity ID.</p>
        :type ActivityId: int
        :param _Name: <p>Instance name only supports Chinese/English/number/"_"/"-" with length less than 60. If no instance name is specified, "unnamed" is displayed by default.</p>
        :type Name: str
        :param _TagList: <p>Tag information that should be bound to the instance is empty by default. You can get it by calling <a href="https://www.tencentcloud.com/document/api/651/35316?from_cn_redirect=1">DescribeTags</a> and checking the Tags field in the return value.</p>
        :type TagList: list of Tag
        :param _SecurityGroupIds: <p>Security group to which an instance belongs. Obtain this parameter by calling the sgId field in the returned value of <a href="https://www.tencentcloud.com/document/api/215/15808?from_cn_redirect=1">DescribeSecurityGroups</a>. If not specified, the default security group is bound.</p>
        :type SecurityGroupIds: list of str
        :param _NeedSupportTDE: <p>Whether data transparent encryption is required:</p><li>0: No</li><li>1: Yes</li>Default value: 0. See [Overview of Data Transparent Encryption](https://www.tencentcloud.com/document/product/409/71748?from_cn_redirect=1).
        :type NeedSupportTDE: int
        :param _KMSKeyId: <p>The KeyId of the custom key. If you select custom key encryption, you need to input the KeyId of the custom key. KeyId is the unique identifier of CMK.<br>For related reference on KeyId creation and retrieval, see <a href="https://www.tencentcloud.com/document/product/409/71749?from_cn_redirect=1">Enable Transparent Data Encryption</a></p>
        :type KMSKeyId: str
        :param _KMSRegion: <p>For regions using the KMS service, KMSRegion is empty by default and the local region KMS is used. If the local region is not supported, select another KMS supported region.<br>For details about KMSRegion, see <a href="https://www.tencentcloud.com/document/product/409/71749?from_cn_redirect=1">enable transparent data encryption</a></p>
        :type KMSRegion: str
        :param _KMSClusterId: <p>Designate the service cluster for KMS. If KMSClusterId is empty, use the KMS of the Default Cluster. To select the specified KMS cluster, require the input of KMSClusterId. For details about KMSClusterId, see enable transparent data encryption.</p>
        :type KMSClusterId: str
        :param _DBEngine: <p>Database engine, support:</p><li>`postgresql`: TencentDB for PostgreSQL</li><li>`mssql_compatible`: MSSQL compatible - TencentDB for PostgreSQL</li>Default value: postgresql
        :type DBEngine: str
        :param _DBEngineConfig: <p>Configuration information for the database engine. The configuration format is as follows:<br>{&quot;$key1&quot;:&quot;$value1&quot;, &quot;$key2&quot;:&quot;$value2&quot;}<br>Supported engines:<br>mssql_compatible engine:</p><li>migrationMode: Database schema, optional parameter. Valid values: single-db (single-database mode), multi-db (multi-database mode). Default is single-db.</li><li>defaultLocale: Sorting area rule, optional parameter, cannot be modified after initialization. Default is en_US. Valid values include: "af_ZA", "sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "hy_AM", "az_Cyrl_AZ", "az_Latn_AZ", "eu_ES", "be_BY", "bg_BG", "ca_ES", "zh_HK", "zh_MO", "zh_CN", "zh_SG", "zh_TW", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_BZ", "en_CA", "en_IE", "en_JM", "en_NZ", "en_PH", "en_ZA", "en_TT", "en_GB", "en_US", "en_ZW", "et_EE", "fo_FO", "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_MC", "fr_CH", "mk_MK", "ka_GE", "de_AT", "de_DE", "de_LI", "de_LU", "de_CH", "el_GR", "gu_IN", "he_IL", "hi_IN", "hu_HU", "is_IS", "id_ID", "it_IT", "it_CH", "ja_JP", "kn_IN", "kok_IN", "ko_KR", "ky_KG", "lv_LV", "lt_LT", "ms_BN", "ms_MY", "mr_IN", "mn_MN", "nb_NO", "nn_NO", "pl_PL", "pt_BR", "pt_PT", "pa_IN", "ro_RO", "ru_RU", "sa_IN", "sr_Cyrl_RS", "sr_Latn_RS", "sk_SK", "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY","es_PE", "es_PR", "es_ES", "es_TRADITIONAL", "es_UY", "es_VE", "sw_KE", "sv_FI", "sv_SE", "tt_RU", "te_IN", "th_TH", "tr_TR", "uk_UA", "ur_IN", "ur_PK", "uz_Cyrl_UZ", "uz_Latn_UZ", "vi_VN".</li><li>serverCollationName: Collation name, optional parameter, cannot be modified after initialization. Default is sql_latin1_general_cp1_ci_as. Valid values include: "bbf_unicode_general_ci_as", "bbf_unicode_cp1_ci_as", "bbf_unicode_CP1250_ci_as", "bbf_unicode_CP1251_ci_as", "bbf_unicode_cp1253_ci_as", "bbf_unicode_cp1254_ci_as", "bbf_unicode_cp1255_ci_as", "bbf_unicode_cp1256_ci_as", "bbf_unicode_cp1257_ci_as", "bbf_unicode_cp1258_ci_as", "bbf_unicode_cp874_ci_as", "sql_latin1_general_cp1250_ci_as", "sql_latin1_general_cp1251_ci_as", "sql_latin1_general_cp1_ci_as", "sql_latin1_general_cp1253_ci_as", "sql_latin1_general_cp1254_ci_as", "sql_latin1_general_cp1255_ci_as","sql_latin1_general_cp1256_ci_as", "sql_latin1_general_cp1257_ci_as", "sql_latin1_general_cp1258_ci_as", "chinese_prc_ci_as", "cyrillic_general_ci_as", "finnish_swedish_ci_as", "french_ci_as", "japanese_ci_as", "korean_wansung_ci_as", "latin1_general_ci_as", "modern_spanish_ci_as", "polish_ci_as", "thai_ci_as", "traditional_spanish_ci_as", "turkish_ci_as", "ukrainian_ci_as", "vietnamese_ci_as".</li>
        :type DBEngineConfig: str
        :param _SyncMode: <p>Primary-standby sync mode, supports: </p><li>Semi-sync: semi-synchronous</li><li>Async: asynchronous</li>Default value for the primary instance: Semi-syncDefault value for the read-only instance: Async
        :type SyncMode: str
        :param _NeedSupportIpv6: <p>Whether required to support Ipv6:</p><li>0: No</li><li>1: Yes</li>Default value: 0
        :type NeedSupportIpv6: int
        :param _DeletionProtection: <p>Whether to enable deletion protection for the instance: true-enable deletion protection; false-disable deletion protection.</p>
        :type DeletionProtection: bool
        :param _StorageType: <p>Instance storage type. Available values: PHYSICAL_LOCAL_SSD: LOCAL SSD hard disk of PHYSICAL machine; CLOUD_PREMIUM: high-performance CLOUD block storage; CLOUD_SSD: SSD CLOUD disk; CLOUD_HSSD: enhanced SSD CLOUD disk.</p>
        :type StorageType: str
        """
        self._Zone = None
        self._SpecCode = None
        self._Storage = None
        self._InstanceCount = None
        self._Period = None
        self._Charset = None
        self._AdminName = None
        self._AdminPassword = None
        self._DBMajorVersion = None
        self._DBVersion = None
        self._DBKernelVersion = None
        self._InstanceChargeType = None
        self._VpcId = None
        self._SubnetId = None
        self._DBNodeSet = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ProjectId = None
        self._ActivityId = None
        self._Name = None
        self._TagList = None
        self._SecurityGroupIds = None
        self._NeedSupportTDE = None
        self._KMSKeyId = None
        self._KMSRegion = None
        self._KMSClusterId = None
        self._DBEngine = None
        self._DBEngineConfig = None
        self._SyncMode = None
        self._NeedSupportIpv6 = None
        self._DeletionProtection = None
        self._StorageType = None

    @property
    def Zone(self):
        r"""<p>The primary availability zone of the instance, for example: ap-guangzhou-3. If needed to support multiple AZs, add primary and secondary AZ information in the DBNodeSet.N field.<br>AZ information can be obtained by calling the <a href="https://www.tencentcloud.com/document/api/409/16769?from_cn_redirect=1">DescribeZones</a> api and checking the Zone field in the returned value.</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecCode(self):
        r"""<p>Purchasable specification code. Obtain this parameter by calling the `SpecCode` field in the return value of <a href="https://www.tencentcloud.com/document/api/409/89019?from_cn_redirect=1">DescribeClasses</a>.</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Storage(self):
        r"""<p>Instance disk capacity size, unit: GB. The step length for parameter settings is 10.</p>
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceCount(self):
        r"""<p>Number of instances to purchase, value ranges from 1 to 10. Single transaction supports a maximum quantity of 10. If exceeding this quantity, multiple calls can be performed to purchase.</p>
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Period(self):
        r"""<p>Purchase duration, unit: month.</p><li>Prepaid: Supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.</li><li>Postpaid: Supports only `1`.</li>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Charset(self):
        r"""<p>Instance character set, which currently supports only:</p><li>UTF8</li><li>LATIN1</li>
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def AdminName(self):
        r"""<p>Username of the instance root account. Specific specifications are as follows:</p><li>The username must consist of 1-16 characters, which can only be letters, digits, or underscores.</li><li>Cannot be postgres.</li><li>Cannot begin with digits or pg_.</li><li>All rules are case-insensitive.</li>
        :rtype: str
        """
        return self._AdminName

    @AdminName.setter
    def AdminName(self, AdminName):
        self._AdminName = AdminName

    @property
    def AdminPassword(self):
        r"""<p>Password for the instance root account username, with a length of 8-32 characters. It is recommended to use a password of more than 12 characters and it cannot start with "/".<br>Must contain the following four character types:</p><li>Lowercase letter: [a-z]</li><li>Uppercase letter: [a-z]</li><li>Number: 0-9</li><li>Special character: ()`~!@#$%^&*-+=_|{}[]:;'<>,.?/</li>
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def DBMajorVersion(self):
        r"""<p>PostgreSQL major version number (this parameter is currently required). Version information can be obtained from <a href="https://www.tencentcloud.com/document/api/409/89018?from_cn_redirect=1">DescribeDBVersions</a>. Currently supports major versions 10, 11, 12, 13, 14, and 15. For details, see <a href="https://www.tencentcloud.com/document/product/409/67018?from_cn_redirect=1">kernel version overview</a>.<br>When this parameter is entered, an instance running the latest kernel version of the latest minor version will be created based on this major version number.</p>
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBVersion(self):
        r"""<p>PostgreSQL community major version + minor version number.<br>It's generally not recommended to pass in this parameter. If needed, only the latest minor version number under the current major version can be passed.</p>
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def DBKernelVersion(self):
        r"""<p>PostgreSQL kernel version number.<br>It's generally not recommended to pass in this parameter. If needed, only the latest kernel version number under the current major version can be passed.</p>
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def InstanceChargeType(self):
        r"""<p>Instance billing type. Currently supports:</p><li>PREPAID: Prepayment, i.e., yearly/monthly subscription</li><li>POSTPAID_BY_HOUR: Postpaid, i.e., pay-as-you-go</li>Default value: PREPAID
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def VpcId(self):
        r"""<p>VPC ID, such as vpc-xxxxxxxx (this parameter is currently required). A valid VPC ID can be obtained by logging in to the console to query or by calling the API <a href="https://www.tencentcloud.com/document/api/215/1372?from_cn_redirect=1">DescribeVpcEx</a> and acquiring the unVpcId field in the API return.</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>VPC subnet ID, such as subnet-xxxxxxxx (this parameter is currently required). Effective VPC subnet IDs can be queried by logging in to the console or by calling the API <a href="https://www.tencentcloud.com/document/api/215/15784?from_cn_redirect=1">DescribeSubnets</a> and acquiring the unSubnetId field in the API return.</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DBNodeSet(self):
        r"""<p>Instance node deployment information. When multi-availability zone deployment is supported, it requires specifying the AZ information for each node.<br>AZ information can be obtained from the Zone field in the returned value by calling the <a href="https://www.tencentcloud.com/document/api/409/16769?from_cn_redirect=1">DescribeZones</a> API.</p>
        :rtype: list of DBNode
        """
        return self._DBNodeSet

    @DBNodeSet.setter
    def DBNodeSet(self, DBNodeSet):
        self._DBNodeSet = DBNodeSet

    @property
    def AutoRenewFlag(self):
        r"""<p>Auto-renewal flag:</p><li>0: Manual renewal</li><li>1: Auto renewal</li>Default value: 0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        r"""<p>Whether to automatically use a voucher:</p><li>0: No</li><li>1: Yes</li>Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""<p>Voucher ID list. Currently only support specifying one voucher.</p>
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ProjectId(self):
        r"""<p>Project ID. The default value is 0, which means it belongs to the default project.</p>
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ActivityId(self):
        r"""<p>Activity ID.</p>
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def Name(self):
        r"""<p>Instance name only supports Chinese/English/number/"_"/"-" with length less than 60. If no instance name is specified, "unnamed" is displayed by default.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TagList(self):
        r"""<p>Tag information that should be bound to the instance is empty by default. You can get it by calling <a href="https://www.tencentcloud.com/document/api/651/35316?from_cn_redirect=1">DescribeTags</a> and checking the Tags field in the return value.</p>
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SecurityGroupIds(self):
        r"""<p>Security group to which an instance belongs. Obtain this parameter by calling the sgId field in the returned value of <a href="https://www.tencentcloud.com/document/api/215/15808?from_cn_redirect=1">DescribeSecurityGroups</a>. If not specified, the default security group is bound.</p>
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def NeedSupportTDE(self):
        r"""<p>Whether data transparent encryption is required:</p><li>0: No</li><li>1: Yes</li>Default value: 0. See [Overview of Data Transparent Encryption](https://www.tencentcloud.com/document/product/409/71748?from_cn_redirect=1).
        :rtype: int
        """
        return self._NeedSupportTDE

    @NeedSupportTDE.setter
    def NeedSupportTDE(self, NeedSupportTDE):
        self._NeedSupportTDE = NeedSupportTDE

    @property
    def KMSKeyId(self):
        r"""<p>The KeyId of the custom key. If you select custom key encryption, you need to input the KeyId of the custom key. KeyId is the unique identifier of CMK.<br>For related reference on KeyId creation and retrieval, see <a href="https://www.tencentcloud.com/document/product/409/71749?from_cn_redirect=1">Enable Transparent Data Encryption</a></p>
        :rtype: str
        """
        return self._KMSKeyId

    @KMSKeyId.setter
    def KMSKeyId(self, KMSKeyId):
        self._KMSKeyId = KMSKeyId

    @property
    def KMSRegion(self):
        r"""<p>For regions using the KMS service, KMSRegion is empty by default and the local region KMS is used. If the local region is not supported, select another KMS supported region.<br>For details about KMSRegion, see <a href="https://www.tencentcloud.com/document/product/409/71749?from_cn_redirect=1">enable transparent data encryption</a></p>
        :rtype: str
        """
        return self._KMSRegion

    @KMSRegion.setter
    def KMSRegion(self, KMSRegion):
        self._KMSRegion = KMSRegion

    @property
    def KMSClusterId(self):
        r"""<p>Designate the service cluster for KMS. If KMSClusterId is empty, use the KMS of the Default Cluster. To select the specified KMS cluster, require the input of KMSClusterId. For details about KMSClusterId, see enable transparent data encryption.</p>
        :rtype: str
        """
        return self._KMSClusterId

    @KMSClusterId.setter
    def KMSClusterId(self, KMSClusterId):
        self._KMSClusterId = KMSClusterId

    @property
    def DBEngine(self):
        r"""<p>Database engine, support:</p><li>`postgresql`: TencentDB for PostgreSQL</li><li>`mssql_compatible`: MSSQL compatible - TencentDB for PostgreSQL</li>Default value: postgresql
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def DBEngineConfig(self):
        r"""<p>Configuration information for the database engine. The configuration format is as follows:<br>{&quot;$key1&quot;:&quot;$value1&quot;, &quot;$key2&quot;:&quot;$value2&quot;}<br>Supported engines:<br>mssql_compatible engine:</p><li>migrationMode: Database schema, optional parameter. Valid values: single-db (single-database mode), multi-db (multi-database mode). Default is single-db.</li><li>defaultLocale: Sorting area rule, optional parameter, cannot be modified after initialization. Default is en_US. Valid values include: "af_ZA", "sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "hy_AM", "az_Cyrl_AZ", "az_Latn_AZ", "eu_ES", "be_BY", "bg_BG", "ca_ES", "zh_HK", "zh_MO", "zh_CN", "zh_SG", "zh_TW", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_BZ", "en_CA", "en_IE", "en_JM", "en_NZ", "en_PH", "en_ZA", "en_TT", "en_GB", "en_US", "en_ZW", "et_EE", "fo_FO", "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_MC", "fr_CH", "mk_MK", "ka_GE", "de_AT", "de_DE", "de_LI", "de_LU", "de_CH", "el_GR", "gu_IN", "he_IL", "hi_IN", "hu_HU", "is_IS", "id_ID", "it_IT", "it_CH", "ja_JP", "kn_IN", "kok_IN", "ko_KR", "ky_KG", "lv_LV", "lt_LT", "ms_BN", "ms_MY", "mr_IN", "mn_MN", "nb_NO", "nn_NO", "pl_PL", "pt_BR", "pt_PT", "pa_IN", "ro_RO", "ru_RU", "sa_IN", "sr_Cyrl_RS", "sr_Latn_RS", "sk_SK", "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY","es_PE", "es_PR", "es_ES", "es_TRADITIONAL", "es_UY", "es_VE", "sw_KE", "sv_FI", "sv_SE", "tt_RU", "te_IN", "th_TH", "tr_TR", "uk_UA", "ur_IN", "ur_PK", "uz_Cyrl_UZ", "uz_Latn_UZ", "vi_VN".</li><li>serverCollationName: Collation name, optional parameter, cannot be modified after initialization. Default is sql_latin1_general_cp1_ci_as. Valid values include: "bbf_unicode_general_ci_as", "bbf_unicode_cp1_ci_as", "bbf_unicode_CP1250_ci_as", "bbf_unicode_CP1251_ci_as", "bbf_unicode_cp1253_ci_as", "bbf_unicode_cp1254_ci_as", "bbf_unicode_cp1255_ci_as", "bbf_unicode_cp1256_ci_as", "bbf_unicode_cp1257_ci_as", "bbf_unicode_cp1258_ci_as", "bbf_unicode_cp874_ci_as", "sql_latin1_general_cp1250_ci_as", "sql_latin1_general_cp1251_ci_as", "sql_latin1_general_cp1_ci_as", "sql_latin1_general_cp1253_ci_as", "sql_latin1_general_cp1254_ci_as", "sql_latin1_general_cp1255_ci_as","sql_latin1_general_cp1256_ci_as", "sql_latin1_general_cp1257_ci_as", "sql_latin1_general_cp1258_ci_as", "chinese_prc_ci_as", "cyrillic_general_ci_as", "finnish_swedish_ci_as", "french_ci_as", "japanese_ci_as", "korean_wansung_ci_as", "latin1_general_ci_as", "modern_spanish_ci_as", "polish_ci_as", "thai_ci_as", "traditional_spanish_ci_as", "turkish_ci_as", "ukrainian_ci_as", "vietnamese_ci_as".</li>
        :rtype: str
        """
        return self._DBEngineConfig

    @DBEngineConfig.setter
    def DBEngineConfig(self, DBEngineConfig):
        self._DBEngineConfig = DBEngineConfig

    @property
    def SyncMode(self):
        r"""<p>Primary-standby sync mode, supports: </p><li>Semi-sync: semi-synchronous</li><li>Async: asynchronous</li>Default value for the primary instance: Semi-syncDefault value for the read-only instance: Async
        :rtype: str
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def NeedSupportIpv6(self):
        r"""<p>Whether required to support Ipv6:</p><li>0: No</li><li>1: Yes</li>Default value: 0
        :rtype: int
        """
        return self._NeedSupportIpv6

    @NeedSupportIpv6.setter
    def NeedSupportIpv6(self, NeedSupportIpv6):
        self._NeedSupportIpv6 = NeedSupportIpv6

    @property
    def DeletionProtection(self):
        r"""<p>Whether to enable deletion protection for the instance: true-enable deletion protection; false-disable deletion protection.</p>
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def StorageType(self):
        r"""<p>Instance storage type. Available values: PHYSICAL_LOCAL_SSD: LOCAL SSD hard disk of PHYSICAL machine; CLOUD_PREMIUM: high-performance CLOUD block storage; CLOUD_SSD: SSD CLOUD disk; CLOUD_HSSD: enhanced SSD CLOUD disk.</p>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SpecCode = params.get("SpecCode")
        self._Storage = params.get("Storage")
        self._InstanceCount = params.get("InstanceCount")
        self._Period = params.get("Period")
        self._Charset = params.get("Charset")
        self._AdminName = params.get("AdminName")
        self._AdminPassword = params.get("AdminPassword")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBVersion = params.get("DBVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("DBNodeSet") is not None:
            self._DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self._DBNodeSet.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._ProjectId = params.get("ProjectId")
        self._ActivityId = params.get("ActivityId")
        self._Name = params.get("Name")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._NeedSupportTDE = params.get("NeedSupportTDE")
        self._KMSKeyId = params.get("KMSKeyId")
        self._KMSRegion = params.get("KMSRegion")
        self._KMSClusterId = params.get("KMSClusterId")
        self._DBEngine = params.get("DBEngine")
        self._DBEngineConfig = params.get("DBEngineConfig")
        self._SyncMode = params.get("SyncMode")
        self._NeedSupportIpv6 = params.get("NeedSupportIpv6")
        self._DeletionProtection = params.get("DeletionProtection")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    r"""CreateInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: <p>Order number list. Each instance corresponds to an order number.</p>
        :type DealNames: list of str
        :param _BillId: <p>Frozen transaction ID.</p>
        :type BillId: str
        :param _DBInstanceIdSet: <p>ID set of successfully created instances. Return value is available only in pay scenarios.</p>
        :type DBInstanceIdSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealNames = None
        self._BillId = None
        self._DBInstanceIdSet = None
        self._RequestId = None

    @property
    def DealNames(self):
        r"""<p>Order number list. Each instance corresponds to an order number.</p>
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def BillId(self):
        r"""<p>Frozen transaction ID.</p>
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def DBInstanceIdSet(self):
        r"""<p>ID set of successfully created instances. Return value is available only in pay scenarios.</p>
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

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
        self._DealNames = params.get("DealNames")
        self._BillId = params.get("BillId")
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._RequestId = params.get("RequestId")


class CreateParameterTemplateRequest(AbstractModel):
    r"""CreateParameterTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateName: Template name, which can contain 1-60 letters, digits, and symbols (-_./()[]()+=:@).
        :type TemplateName: str
        :param _DBMajorVersion: The major database version number, such as 11, 12, 13.
        :type DBMajorVersion: str
        :param _DBEngine: Database engine, such as postgresql, mssql_compatible.
        :type DBEngine: str
        :param _TemplateDescription: Parameter template description, which can contain 1-60 letters, digits, and symbols (-_./()[]()+=:@).
        :type TemplateDescription: str
        """
        self._TemplateName = None
        self._DBMajorVersion = None
        self._DBEngine = None
        self._TemplateDescription = None

    @property
    def TemplateName(self):
        r"""Template name, which can contain 1-60 letters, digits, and symbols (-_./()[]()+=:@).
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def DBMajorVersion(self):
        r"""The major database version number, such as 11, 12, 13.
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBEngine(self):
        r"""Database engine, such as postgresql, mssql_compatible.
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def TemplateDescription(self):
        r"""Parameter template description, which can contain 1-60 letters, digits, and symbols (-_./()[]()+=:@).
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBEngine = params.get("DBEngine")
        self._TemplateDescription = params.get("TemplateDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParameterTemplateResponse(AbstractModel):
    r"""CreateParameterTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID, which uniquely identifies a parameter template.
        :type TemplateId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        r"""Parameter template ID, which uniquely identifies a parameter template.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

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
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateReadOnlyDBInstanceRequest(AbstractModel):
    r"""CreateReadOnlyDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Primary AZ of an instance, such as "ap-guangzhou-3".
The information of AZ can be obtained from the `Zone` field in the return value of the [DescribeZones](https://intl.cloud.tencent.com/document/api/409/16769?from_cn_redirect=1) API.
        :type Zone: str
        :param _MasterDBInstanceId: Primary instance ID of the read-only instance. obtain through the api [DescribeDBInstances](https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1).
        :type MasterDBInstanceId: str
        :param _SpecCode: Purchasable code, which can be obtained from the `SpecCode` field in the return value of the [DescribeClasses](https://intl.cloud.tencent.com/document/api/409/89019?from_cn_redirect=1) API.
        :type SpecCode: str
        :param _Storage: Instance disk capacity size in GB. specifies the step length for parameter settings as 10.
        :type Storage: int
        :param _InstanceCount: Number of instances to purchase. value range: [1-6]. maximum allowed number is 6.
        :type InstanceCount: int
        :param _Period: Purchase duration, in months.
<Li>Prepaid: supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.</li>.
<li>Pay-as-you-go: Only supports `1`.</li>
        :type Period: int
        :param _VpcId: VPC ID, in the format of vpc-xxxxxxxx (this parameter is currently required). A valid VpcId can be obtained by logging into the console; it can also be obtained from the unVpcId field in the return value of calling of the [DescribeVpcEx](https://intl.cloud.tencent.com/document/api/215/1372?from_cn_redirect=1) API.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID, in the format of subnet-xxxxxxxx (this parameter is currently required). A valid VPC subnet ID can be obtained by logging into the console; it can also be obtained from the unSubnetId field in the return value of calling of the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API.
        :type SubnetId: str
        :param _InstanceChargeType: Instance billing type, which currently supports:.
<Li>PREPAID: prepaid, i.e., yearly/monthly subscription.</li>.
<Li>POSTPAID_BY_HOUR: pay-as-you-go, i.e., pay by consumption.</li>.
Default value: PREPAID. if the primary instance is postpaid, the read-only instance must also be postpaid.
        :type InstanceChargeType: str
        :param _AutoVoucher: Specifies whether to automatically use a voucher.
<Li>0: no.</li>.
<Li>`1`: yes.</li>.
Default value: 0
        :type AutoVoucher: int
        :param _VoucherIds: Voucher ID list. Currently, you can specify only one voucher.
        :type VoucherIds: list of str
        :param _AutoRenewFlag: Specifies the auto-renewal flag.
<Li>`0`: manual renewal.</li>.
<Li>`1`: auto-renewal</li>.
Default value: 0
        :type AutoRenewFlag: int
        :param _ProjectId: Project ID. default value is 0, means it belongs to the default project.
        :type ProjectId: int
        :param _ActivityId: Special offer ID
        :type ActivityId: int
        :param _ReadOnlyGroupId: RO group ID
        :type ReadOnlyGroupId: str
        :param _TagList: The information of tags to be bound with the instance, which is left empty by default. This parameter can be obtained from the `Tags` field in the return value of the [DescribeTags](https://intl.cloud.tencent.com/document/api/651/35316?from_cn_redirect=1) API.
        :type TagList: :class:`tencentcloud.postgres.v20170312.models.Tag`
        :param _SecurityGroupIds: Security group of the instance, which can be obtained from the `sgld` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) API. If this parameter is not specified, the default security group will be bound.

        :type SecurityGroupIds: list of str
        :param _NeedSupportIpv6: Specifies whether to support Ipv6.
<Li>0: no.</li>.
<Li>`1`: yes.</li>.
Default value: 0
        :type NeedSupportIpv6: int
        :param _Name: Instance name. only chinese characters, letters, digits, underscores (_), and delimiters (-) are supported. the length must be less than 60 characters.
        :type Name: str
        :param _DBVersion: Specifies the kernel version number should be consistent with the primary instance and no longer needed to be specified.
        :type DBVersion: str
        :param _DedicatedClusterId: CDC ID.
        :type DedicatedClusterId: str
        :param _DeletionProtection: Specifies whether to enable deletion protection for the instance. valid values: true (enable deletion protection), false (disable deletion protection).
        :type DeletionProtection: bool
        """
        self._Zone = None
        self._MasterDBInstanceId = None
        self._SpecCode = None
        self._Storage = None
        self._InstanceCount = None
        self._Period = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceChargeType = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._AutoRenewFlag = None
        self._ProjectId = None
        self._ActivityId = None
        self._ReadOnlyGroupId = None
        self._TagList = None
        self._SecurityGroupIds = None
        self._NeedSupportIpv6 = None
        self._Name = None
        self._DBVersion = None
        self._DedicatedClusterId = None
        self._DeletionProtection = None

    @property
    def Zone(self):
        r"""Primary AZ of an instance, such as "ap-guangzhou-3".
The information of AZ can be obtained from the `Zone` field in the return value of the [DescribeZones](https://intl.cloud.tencent.com/document/api/409/16769?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def MasterDBInstanceId(self):
        r"""Primary instance ID of the read-only instance. obtain through the api [DescribeDBInstances](https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._MasterDBInstanceId

    @MasterDBInstanceId.setter
    def MasterDBInstanceId(self, MasterDBInstanceId):
        self._MasterDBInstanceId = MasterDBInstanceId

    @property
    def SpecCode(self):
        r"""Purchasable code, which can be obtained from the `SpecCode` field in the return value of the [DescribeClasses](https://intl.cloud.tencent.com/document/api/409/89019?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Storage(self):
        r"""Instance disk capacity size in GB. specifies the step length for parameter settings as 10.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceCount(self):
        r"""Number of instances to purchase. value range: [1-6]. maximum allowed number is 6.
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Period(self):
        r"""Purchase duration, in months.
<Li>Prepaid: supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.</li>.
<li>Pay-as-you-go: Only supports `1`.</li>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def VpcId(self):
        r"""VPC ID, in the format of vpc-xxxxxxxx (this parameter is currently required). A valid VpcId can be obtained by logging into the console; it can also be obtained from the unVpcId field in the return value of calling of the [DescribeVpcEx](https://intl.cloud.tencent.com/document/api/215/1372?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""VPC subnet ID, in the format of subnet-xxxxxxxx (this parameter is currently required). A valid VPC subnet ID can be obtained by logging into the console; it can also be obtained from the unSubnetId field in the return value of calling of the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceChargeType(self):
        r"""Instance billing type, which currently supports:.
<Li>PREPAID: prepaid, i.e., yearly/monthly subscription.</li>.
<Li>POSTPAID_BY_HOUR: pay-as-you-go, i.e., pay by consumption.</li>.
Default value: PREPAID. if the primary instance is postpaid, the read-only instance must also be postpaid.
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def AutoVoucher(self):
        r"""Specifies whether to automatically use a voucher.
<Li>0: no.</li>.
<Li>`1`: yes.</li>.
Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID list. Currently, you can specify only one voucher.
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def AutoRenewFlag(self):
        r"""Specifies the auto-renewal flag.
<Li>`0`: manual renewal.</li>.
<Li>`1`: auto-renewal</li>.
Default value: 0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ProjectId(self):
        r"""Project ID. default value is 0, means it belongs to the default project.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ActivityId(self):
        r"""Special offer ID
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ReadOnlyGroupId(self):
        r"""RO group ID
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def TagList(self):
        r"""The information of tags to be bound with the instance, which is left empty by default. This parameter can be obtained from the `Tags` field in the return value of the [DescribeTags](https://intl.cloud.tencent.com/document/api/651/35316?from_cn_redirect=1) API.
        :rtype: :class:`tencentcloud.postgres.v20170312.models.Tag`
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SecurityGroupIds(self):
        r"""Security group of the instance, which can be obtained from the `sgld` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) API. If this parameter is not specified, the default security group will be bound.

        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def NeedSupportIpv6(self):
        r"""Specifies whether to support Ipv6.
<Li>0: no.</li>.
<Li>`1`: yes.</li>.
Default value: 0
        :rtype: int
        """
        return self._NeedSupportIpv6

    @NeedSupportIpv6.setter
    def NeedSupportIpv6(self, NeedSupportIpv6):
        self._NeedSupportIpv6 = NeedSupportIpv6

    @property
    def Name(self):
        r"""Instance name. only chinese characters, letters, digits, underscores (_), and delimiters (-) are supported. the length must be less than 60 characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DBVersion(self):
        warnings.warn("parameter `DBVersion` is deprecated", DeprecationWarning) 

        r"""Specifies the kernel version number should be consistent with the primary instance and no longer needed to be specified.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        warnings.warn("parameter `DBVersion` is deprecated", DeprecationWarning) 

        self._DBVersion = DBVersion

    @property
    def DedicatedClusterId(self):
        r"""CDC ID.
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def DeletionProtection(self):
        r"""Specifies whether to enable deletion protection for the instance. valid values: true (enable deletion protection), false (disable deletion protection).
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._MasterDBInstanceId = params.get("MasterDBInstanceId")
        self._SpecCode = params.get("SpecCode")
        self._Storage = params.get("Storage")
        self._InstanceCount = params.get("InstanceCount")
        self._Period = params.get("Period")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ProjectId = params.get("ProjectId")
        self._ActivityId = params.get("ActivityId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        if params.get("TagList") is not None:
            self._TagList = Tag()
            self._TagList._deserialize(params.get("TagList"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._NeedSupportIpv6 = params.get("NeedSupportIpv6")
        self._Name = params.get("Name")
        self._DBVersion = params.get("DBVersion")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyDBInstanceResponse(AbstractModel):
    r"""CreateReadOnlyDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order number list. Each instance corresponds to an order number.
        :type DealNames: list of str
        :param _BillId: Bill ID of frozen fees
        :type BillId: str
        :param _DBInstanceIdSet: ID set of instances which have been created successfully. The parameter value will be returned only when the pay-as-you-go billing mode is used.
        :type DBInstanceIdSet: list of str
        :param _BillingParameters: BillingParameters specifies the parameters for product order placement. the output has a value only when billingparameters is provided.
        :type BillingParameters: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealNames = None
        self._BillId = None
        self._DBInstanceIdSet = None
        self._BillingParameters = None
        self._RequestId = None

    @property
    def DealNames(self):
        r"""Order number list. Each instance corresponds to an order number.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def BillId(self):
        r"""Bill ID of frozen fees
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def DBInstanceIdSet(self):
        r"""ID set of instances which have been created successfully. The parameter value will be returned only when the pay-as-you-go billing mode is used.
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def BillingParameters(self):
        r"""BillingParameters specifies the parameters for product order placement. the output has a value only when billingparameters is provided.
        :rtype: str
        """
        return self._BillingParameters

    @BillingParameters.setter
    def BillingParameters(self, BillingParameters):
        self._BillingParameters = BillingParameters

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
        self._DealNames = params.get("DealNames")
        self._BillId = params.get("BillId")
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._BillingParameters = params.get("BillingParameters")
        self._RequestId = params.get("RequestId")


class CreateReadOnlyGroupNetworkAccessRequest(AbstractModel):
    r"""CreateReadOnlyGroupNetworkAccess request structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: ROGroupId specifies the read-only group ID in the format of pgrogrp-4t9c6g7k. it can be obtained through the DescribeReadOnlyGroups api (https://www.tencentcloud.com/document/product/409/39725?lang=en).
        :type ReadOnlyGroupId: str
        :param _VpcId: Unified VPC ID.
        :type VpcId: str
        :param _SubnetId: Subnet ID.
        :type SubnetId: str
        :param _IsAssignVip: Whether to manually assign the VIP. Valid values: `true` (manually assign), `false` (automatically assign).
        :type IsAssignVip: bool
        :param _Vip: Target VIP address. when this parameter is not specified and IsAssignVip is true, the system automatically assigns a VIP by default.
        :type Vip: str
        """
        self._ReadOnlyGroupId = None
        self._VpcId = None
        self._SubnetId = None
        self._IsAssignVip = None
        self._Vip = None

    @property
    def ReadOnlyGroupId(self):
        r"""ROGroupId specifies the read-only group ID in the format of pgrogrp-4t9c6g7k. it can be obtained through the DescribeReadOnlyGroups api (https://www.tencentcloud.com/document/product/409/39725?lang=en).
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def VpcId(self):
        r"""Unified VPC ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def IsAssignVip(self):
        r"""Whether to manually assign the VIP. Valid values: `true` (manually assign), `false` (automatically assign).
        :rtype: bool
        """
        return self._IsAssignVip

    @IsAssignVip.setter
    def IsAssignVip(self, IsAssignVip):
        self._IsAssignVip = IsAssignVip

    @property
    def Vip(self):
        r"""Target VIP address. when this parameter is not specified and IsAssignVip is true, the system automatically assigns a VIP by default.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._IsAssignVip = params.get("IsAssignVip")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyGroupNetworkAccessResponse(AbstractModel):
    r"""CreateReadOnlyGroupNetworkAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID. FlowId is equivalent to TaskId.
        :type FlowId: int
        :param _TaskId: Task ID.
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Process ID. FlowId is equivalent to TaskId.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""Task ID.
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
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateReadOnlyGroupRequest(AbstractModel):
    r"""CreateReadOnlyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _MasterDBInstanceId: Primary instance ID
        :type MasterDBInstanceId: str
        :param _Name: RO group name
        :type Name: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _ReplayLagEliminate: Whether to remove a read-only replica from an RO group if the delay between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :type ReplayLagEliminate: int
        :param _ReplayLatencyEliminate: Whether to remove a read-only replica from an RO group if the sync log size difference between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :type ReplayLatencyEliminate: int
        :param _MaxReplayLag: Delay threshold in ms
        :type MaxReplayLag: int
        :param _MaxReplayLatency: Delayed log size threshold in MB
        :type MaxReplayLatency: int
        :param _MinDelayEliminateReserve: The minimum number of read-only replicas that must be retained in an RO group
        :type MinDelayEliminateReserve: int
        :param _SecurityGroupIds: Security group ID
        :type SecurityGroupIds: list of str
        """
        self._MasterDBInstanceId = None
        self._Name = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._ReplayLagEliminate = None
        self._ReplayLatencyEliminate = None
        self._MaxReplayLag = None
        self._MaxReplayLatency = None
        self._MinDelayEliminateReserve = None
        self._SecurityGroupIds = None

    @property
    def MasterDBInstanceId(self):
        r"""Primary instance ID
        :rtype: str
        """
        return self._MasterDBInstanceId

    @MasterDBInstanceId.setter
    def MasterDBInstanceId(self, MasterDBInstanceId):
        self._MasterDBInstanceId = MasterDBInstanceId

    @property
    def Name(self):
        r"""RO group name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ReplayLagEliminate(self):
        r"""Whether to remove a read-only replica from an RO group if the delay between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._ReplayLagEliminate

    @ReplayLagEliminate.setter
    def ReplayLagEliminate(self, ReplayLagEliminate):
        self._ReplayLagEliminate = ReplayLagEliminate

    @property
    def ReplayLatencyEliminate(self):
        r"""Whether to remove a read-only replica from an RO group if the sync log size difference between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._ReplayLatencyEliminate

    @ReplayLatencyEliminate.setter
    def ReplayLatencyEliminate(self, ReplayLatencyEliminate):
        self._ReplayLatencyEliminate = ReplayLatencyEliminate

    @property
    def MaxReplayLag(self):
        r"""Delay threshold in ms
        :rtype: int
        """
        return self._MaxReplayLag

    @MaxReplayLag.setter
    def MaxReplayLag(self, MaxReplayLag):
        self._MaxReplayLag = MaxReplayLag

    @property
    def MaxReplayLatency(self):
        r"""Delayed log size threshold in MB
        :rtype: int
        """
        return self._MaxReplayLatency

    @MaxReplayLatency.setter
    def MaxReplayLatency(self, MaxReplayLatency):
        self._MaxReplayLatency = MaxReplayLatency

    @property
    def MinDelayEliminateReserve(self):
        r"""The minimum number of read-only replicas that must be retained in an RO group
        :rtype: int
        """
        return self._MinDelayEliminateReserve

    @MinDelayEliminateReserve.setter
    def MinDelayEliminateReserve(self, MinDelayEliminateReserve):
        self._MinDelayEliminateReserve = MinDelayEliminateReserve

    @property
    def SecurityGroupIds(self):
        r"""Security group ID
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._MasterDBInstanceId = params.get("MasterDBInstanceId")
        self._Name = params.get("Name")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ReplayLagEliminate = params.get("ReplayLagEliminate")
        self._ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self._MaxReplayLag = params.get("MaxReplayLag")
        self._MaxReplayLatency = params.get("MaxReplayLatency")
        self._MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyGroupResponse(AbstractModel):
    r"""CreateReadOnlyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: RO group ID
        :type ReadOnlyGroupId: str
        :param _FlowId: Task ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReadOnlyGroupId = None
        self._FlowId = None
        self._RequestId = None

    @property
    def ReadOnlyGroupId(self):
        r"""RO group ID
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def FlowId(self):
        r"""Task ID
Note: this field may return `null`, indicating that no valid values can be obtained.
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
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateServerlessDBInstanceRequest(AbstractModel):
    r"""CreateServerlessDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone ID. Only ap-shanghai-2, ap-beijing-1, and ap-guangzhou-2 are supported during the beta test.
        :type Zone: str
        :param _DBInstanceName: Instance name. The value must be unique for the same account.
        :type DBInstanceName: str
        :param _DBVersion: Kernel version of a PostgreSQL instance. Currently, only 10.4 is supported.
        :type DBVersion: str
        :param _DBCharset: Database character set of a PostgreSQL instance. Currently, only UTF-8 is supported.
        :type DBCharset: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _VpcId: VPC ID.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID.
        :type SubnetId: str
        :param _TagList: Array of tags to be bound with the instance
        :type TagList: list of Tag
        """
        self._Zone = None
        self._DBInstanceName = None
        self._DBVersion = None
        self._DBCharset = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._TagList = None

    @property
    def Zone(self):
        r"""Availability zone ID. Only ap-shanghai-2, ap-beijing-1, and ap-guangzhou-2 are supported during the beta test.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DBInstanceName(self):
        r"""Instance name. The value must be unique for the same account.
        :rtype: str
        """
        return self._DBInstanceName

    @DBInstanceName.setter
    def DBInstanceName(self, DBInstanceName):
        self._DBInstanceName = DBInstanceName

    @property
    def DBVersion(self):
        r"""Kernel version of a PostgreSQL instance. Currently, only 10.4 is supported.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def DBCharset(self):
        r"""Database character set of a PostgreSQL instance. Currently, only UTF-8 is supported.
        :rtype: str
        """
        return self._DBCharset

    @DBCharset.setter
    def DBCharset(self, DBCharset):
        self._DBCharset = DBCharset

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
    def VpcId(self):
        r"""VPC ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""VPC subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def TagList(self):
        r"""Array of tags to be bound with the instance
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DBInstanceName = params.get("DBInstanceName")
        self._DBVersion = params.get("DBVersion")
        self._DBCharset = params.get("DBCharset")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerlessDBInstanceResponse(AbstractModel):
    r"""CreateServerlessDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID, such as "postgres-xxxxx". The value must be globally unique.
        :type DBInstanceId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DBInstanceId = None
        self._RequestId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID, such as "postgres-xxxxx". The value must be globally unique.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

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
        self._DBInstanceId = params.get("DBInstanceId")
        self._RequestId = params.get("RequestId")


class DBBackup(AbstractModel):
    r"""Database backup information

    """

    def __init__(self):
        r"""
        :param _Id: Unique backup file ID
        :type Id: int
        :param _StartTime: File generation start time
        :type StartTime: str
        :param _EndTime: File generation end time
        :type EndTime: str
        :param _Size: File size in KB
        :type Size: int
        :param _Strategy: Policy (0: instance backup, 1: multi-database backup)
        :type Strategy: int
        :param _Way: Type (0: scheduled)
        :type Way: int
        :param _Type: Backup mode (1: full)
        :type Type: int
        :param _Status: Status (1: creating, 2: success, 3: failure)
        :type Status: int
        :param _DbList: DB list
        :type DbList: list of str
        :param _InternalAddr: Download address on private network
        :type InternalAddr: str
        :param _ExternalAddr: Download address on public network
        :type ExternalAddr: str
        :param _SetId: Backup set ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SetId: str
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Strategy = None
        self._Way = None
        self._Type = None
        self._Status = None
        self._DbList = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._SetId = None

    @property
    def Id(self):
        r"""Unique backup file ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        r"""File generation start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""File generation end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        r"""File size in KB
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Strategy(self):
        r"""Policy (0: instance backup, 1: multi-database backup)
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Way(self):
        r"""Type (0: scheduled)
        :rtype: int
        """
        return self._Way

    @Way.setter
    def Way(self, Way):
        self._Way = Way

    @property
    def Type(self):
        r"""Backup mode (1: full)
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""Status (1: creating, 2: success, 3: failure)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DbList(self):
        r"""DB list
        :rtype: list of str
        """
        return self._DbList

    @DbList.setter
    def DbList(self, DbList):
        self._DbList = DbList

    @property
    def InternalAddr(self):
        r"""Download address on private network
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        r"""Download address on public network
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def SetId(self):
        r"""Backup set ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Strategy = params.get("Strategy")
        self._Way = params.get("Way")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._DbList = params.get("DbList")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._SetId = params.get("SetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    r"""Instance details

    """

    def __init__(self):
        r"""
        :param _Region: <p>Region of the instance, for example: ap-guangzhou, corresponds to the region field in RegionSet.</p>
        :type Region: str
        :param _Zone: <p>Availability zone to which the instance belongs, for example: ap-guangzhou-3, corresponds to the Zone field in ZoneSet.</p>
        :type Zone: str
        :param _VpcId: <p>VPC ID, such as vpc-e6w23k31. A valid VPC ID can be obtained by logging in to the console to query or by calling the API <a href="https://www.tencentcloud.com/document/api/215/15778?from_cn_redirect=1">DescribeVpcs</a> and acquiring the unVpcId field in API return.</p>
        :type VpcId: str
        :param _SubnetId: <p>VPC subnet ID, such as subnet-51lcif9y. An effective VPC subnet ID can be obtained by logging in to the console to query. You can also call API <a href="https://www.tencentcloud.com/document/api/215/15784?from_cn_redirect=1">DescribeSubnets</a> and get it from the unSubnetId field in API return.</p>
        :type SubnetId: str
        :param _DBInstanceId: <p>Instance ID.</p>
        :type DBInstanceId: str
        :param _DBInstanceName: <p>Instance name.</p>
        :type DBInstanceName: str
        :param _DBInstanceStatus: <p>Instance status, including: `applying` (applying), `init` (to be initialized), `initing` (initializing), `running` (running), `limited run` (restricted operation), `isolating` (isolating), `isolated` (isolated), `disisolating` (de-isolating), `recycling` (recycling), `recycled` (recycled), `job running` (task executing), `offline` (offline), `migrating` (migrating), `expanding` (scaling out), `waitSwitch` (waiting to switch), `switching` (switching), `readonly` (readonly), `restarting` (restarting), `network changing` (network modification in progress), `upgrading` (kernel version upgrading), `audit-switching` (audit status changing), `primary-switching` (primary-secondary switching), `offlining` (offline), `deployment changing` (modify AZ), `cloning` (recovering data), `parameter modifying` (parameter modification in progress), `log-switching` (log status change), `restoring` (recovering), and `expanding` (scaling out)</p>
        :type DBInstanceStatus: str
        :param _DBInstanceMemory: <p>Memory size allocated to the instance, measurement unit: GB</p>
        :type DBInstanceMemory: int
        :param _DBInstanceStorage: <p>Storage space size allocated to the instance, measurement unit: GB</p>
        :type DBInstanceStorage: int
        :param _DBInstanceCpu: <p>Number of CPUs allocated to the instance, unit: piece</p>
        :type DBInstanceCpu: int
        :param _DBInstanceClass: <p>Purchasable specification ID.</p>
        :type DBInstanceClass: str
        :param _DBMajorVersion: <p>PostgreSQL major version number. Version information can be obtained from <a href="https://www.tencentcloud.com/document/api/409/89018?from_cn_redirect=1">DescribeDBVersions</a>. Currently supports major versions 10, 11, 12, 13, 14, and 15.</p>
        :type DBMajorVersion: str
        :param _DBVersion: <p>PostgreSQL community major version + minor version number, such as 12.4. Version information can be obtained from <a href="https://www.tencentcloud.com/document/api/409/89018?from_cn_redirect=1">DescribeDBVersions</a>.</p>
        :type DBVersion: str
        :param _DBKernelVersion: <p>PostgreSQL Kernel Version, for example v12.7_r1.8. Version information can be obtained from <a href="https://www.tencentcloud.com/document/api/409/89018?from_cn_redirect=1">DescribeDBVersions</a>.</p>
        :type DBKernelVersion: str
        :param _DBInstanceType: <p>Instance types:</p><li>primary: Primary instance</li><li>readonly: Read-only instance</li><li>guard: Disaster recovery instance</li><li>temp: Temporary instance</li>
        :type DBInstanceType: str
        :param _DBInstanceVersion: <p>Instance version currently only supports standard (dual-server high-availability edition, one master and one slave).</p>
        :type DBInstanceVersion: str
        :param _DBCharset: <p>Instance character set, which currently supports only:</p><li>UTF8</li><li>LATIN1</li>
        :type DBCharset: str
        :param _CreateTime: <p>Instance creation time.</p>
        :type CreateTime: str
        :param _UpdateTime: <p>The time when the instance executed the last update.</p>
        :type UpdateTime: str
        :param _ExpireTime: <p>Instance expiration time.</p>
        :type ExpireTime: str
        :param _IsolatedTime: <p>Instance isolation time.</p>
        :type IsolatedTime: str
        :param _PayType: <p>Billing mode:</p><li>prepaid: Yearly/monthly subscription, prepayment</li><li>postpaid: Pay-as-you-go, postpaid</li>
        :type PayType: str
        :param _AutoRenew: <p>Auto-renewal or not:</p><li>0: Manual renewal</li><li>1: Auto renewal</li>Default value: 0
        :type AutoRenew: int
        :param _DBInstanceNetInfo: <p>Instance network connection information.</p>
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        :param _Type: <p>Machine type.</p>
        :type Type: str
        :param _AppId: <p>User's app id.</p>
        :type AppId: int
        :param _Uid: <p>Uid of the instance.</p>
        :type Uid: int
        :param _ProjectId: <p>Project ID.</p>
        :type ProjectId: int
        :param _TagList: <p>Tag information associated with the instance.</p>
        :type TagList: list of Tag
        :param _MasterDBInstanceId: <p>Primary instance information. Returned only when the instance is a read-only instance.</p>
        :type MasterDBInstanceId: str
        :param _ReadOnlyInstanceNum: <p>Number of read-only instances.</p>
        :type ReadOnlyInstanceNum: int
        :param _StatusInReadonlyGroup: <p>State of the read-only instance in the read-only group.</p>
        :type StatusInReadonlyGroup: str
        :param _OfflineTime: <p>Offline time.</p>
        :type OfflineTime: str
        :param _DBNodeSet: <p>Instance node information.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBNodeSet: list of DBNode
        :param _IsSupportTDE: <p>Whether the instance supports TDE data encryption:</p><li>0: Not supported</li><li>1: Supported</li>Default value: 0. For TDE data encryption, see [Overview of Data Transparent Encryption](https://www.tencentcloud.com/document/product/409/71748?from_cn_redirect=1).
        :type IsSupportTDE: int
        :param _DBEngine: <p>Database engine, support:</p><li>`postgresql`: TencentDB for PostgreSQL</li><li>`mssql_compatible`: MSSQL compatible - TencentDB for PostgreSQL</li>Default value: postgresql
        :type DBEngine: str
        :param _DBEngineConfig: <p>Configuration information for the database engine. The configuration format is as follows:<br>{&quot;$key1&quot;:&quot;$value1&quot;, &quot;$key2&quot;:&quot;$value2&quot;}<br>Supported engines:<br>mssql_compatible engine:</p><li>migrationMode: Database schema, optional parameter. Valid values: single-db (single-database mode), multi-db (multi-database mode). Default is single-db.</li><li>defaultLocale: Sorting area rule, optional parameter, cannot be modified after initialization. Default is en_US. Valid values include: "af_ZA", "sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "hy_AM", "az_Cyrl_AZ", "az_Latn_AZ", "eu_ES", "be_BY", "bg_BG", "ca_ES", "zh_HK", "zh_MO", "zh_CN", "zh_SG", "zh_TW", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_BZ", "en_CA", "en_IE", "en_JM", "en_NZ", "en_PH", "en_ZA", "en_TT", "en_GB", "en_US", "en_ZW", "et_EE", "fo_FO", "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_MC", "fr_CH", "mk_MK", "ka_GE", "de_AT", "de_DE", "de_LI", "de_LU", "de_CH", "el_GR", "gu_IN", "he_IL", "hi_IN", "hu_HU", "is_IS", "id_ID", "it_IT", "it_CH", "ja_JP", "kn_IN", "kok_IN", "ko_KR", "ky_KG", "lv_LV", "lt_LT", "ms_BN", "ms_MY", "mr_IN", "mn_MN", "nb_NO", "nn_NO", "pl_PL", "pt_BR", "pt_PT", "pa_IN", "ro_RO", "ru_RU", "sa_IN", "sr_Cyrl_RS", "sr_Latn_RS", "sk_SK", "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY","es_PE", "es_PR", "es_ES", "es_TRADITIONAL", "es_UY", "es_VE", "sw_KE", "sv_FI", "sv_SE", "tt_RU", "te_IN", "th_TH", "tr_TR", "uk_UA", "ur_IN", "ur_PK", "uz_Cyrl_UZ", "uz_Latn_UZ", "vi_VN".</li><li>serverCollationName: Collation name, optional parameter, cannot be modified after initialization. Default is sql_latin1_general_cp1_ci_as. Valid values include: "bbf_unicode_general_ci_as", "bbf_unicode_cp1_ci_as", "bbf_unicode_CP1250_ci_as", "bbf_unicode_CP1251_ci_as", "bbf_unicode_cp1253_ci_as", "bbf_unicode_cp1254_ci_as", "bbf_unicode_cp1255_ci_as", "bbf_unicode_cp1256_ci_as", "bbf_unicode_cp1257_ci_as", "bbf_unicode_cp1258_ci_as", "bbf_unicode_cp874_ci_as", "sql_latin1_general_cp1250_ci_as", "sql_latin1_general_cp1251_ci_as", "sql_latin1_general_cp1_ci_as", "sql_latin1_general_cp1253_ci_as", "sql_latin1_general_cp1254_ci_as", "sql_latin1_general_cp1255_ci_as","sql_latin1_general_cp1256_ci_as", "sql_latin1_general_cp1257_ci_as", "sql_latin1_general_cp1258_ci_as", "chinese_prc_ci_as", "cyrillic_general_ci_as", "finnish_swedish_ci_as", "french_ci_as", "japanese_ci_as", "korean_wansung_ci_as", "latin1_general_ci_as", "modern_spanish_ci_as", "polish_ci_as", "thai_ci_as", "traditional_spanish_ci_as", "turkish_ci_as", "ukrainian_ci_as", "vietnamese_ci_as".</li>
        :type DBEngineConfig: str
        :param _NetworkAccessList: <p>Instance network information list (deprecated)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetworkAccessList: list of NetworkAccess
        :param _SupportIpv6: <p>Whether the instance supports Ipv6:</p><li>0: No</li><li>1: Yes</li>Default value: 0
        :type SupportIpv6: int
        :param _ExpandedCpu: <p>Number of cpu cores that have been elastically scaled out for the instance</p>
        :type ExpandedCpu: int
        :param _DeletionProtection: <p>Whether to enable deletion protection for the instance, values as follows:</p><ul><li>true: enable deletion protection</li><li>false: disable deletion protection</li></ul>
        :type DeletionProtection: bool
        :param _DBInstanceStorageType: <p>Instance storage type. Available values: PHYSICAL_LOCAL_SSD: LOCAL SSD hard disk of PHYSICAL machine; CLOUD_PREMIUM: high-performance CLOUD block storage; CLOUD_SSD: SSD CLOUD disk; CLOUD_HSSD: enhanced SSD CLOUD disk.</p>
        :type DBInstanceStorageType: str
        """
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._DBInstanceId = None
        self._DBInstanceName = None
        self._DBInstanceStatus = None
        self._DBInstanceMemory = None
        self._DBInstanceStorage = None
        self._DBInstanceCpu = None
        self._DBInstanceClass = None
        self._DBMajorVersion = None
        self._DBVersion = None
        self._DBKernelVersion = None
        self._DBInstanceType = None
        self._DBInstanceVersion = None
        self._DBCharset = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ExpireTime = None
        self._IsolatedTime = None
        self._PayType = None
        self._AutoRenew = None
        self._DBInstanceNetInfo = None
        self._Type = None
        self._AppId = None
        self._Uid = None
        self._ProjectId = None
        self._TagList = None
        self._MasterDBInstanceId = None
        self._ReadOnlyInstanceNum = None
        self._StatusInReadonlyGroup = None
        self._OfflineTime = None
        self._DBNodeSet = None
        self._IsSupportTDE = None
        self._DBEngine = None
        self._DBEngineConfig = None
        self._NetworkAccessList = None
        self._SupportIpv6 = None
        self._ExpandedCpu = None
        self._DeletionProtection = None
        self._DBInstanceStorageType = None

    @property
    def Region(self):
        r"""<p>Region of the instance, for example: ap-guangzhou, corresponds to the region field in RegionSet.</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""<p>Availability zone to which the instance belongs, for example: ap-guangzhou-3, corresponds to the Zone field in ZoneSet.</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""<p>VPC ID, such as vpc-e6w23k31. A valid VPC ID can be obtained by logging in to the console to query or by calling the API <a href="https://www.tencentcloud.com/document/api/215/15778?from_cn_redirect=1">DescribeVpcs</a> and acquiring the unVpcId field in API return.</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>VPC subnet ID, such as subnet-51lcif9y. An effective VPC subnet ID can be obtained by logging in to the console to query. You can also call API <a href="https://www.tencentcloud.com/document/api/215/15784?from_cn_redirect=1">DescribeSubnets</a> and get it from the unSubnetId field in API return.</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DBInstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DBInstanceName(self):
        r"""<p>Instance name.</p>
        :rtype: str
        """
        return self._DBInstanceName

    @DBInstanceName.setter
    def DBInstanceName(self, DBInstanceName):
        self._DBInstanceName = DBInstanceName

    @property
    def DBInstanceStatus(self):
        r"""<p>Instance status, including: `applying` (applying), `init` (to be initialized), `initing` (initializing), `running` (running), `limited run` (restricted operation), `isolating` (isolating), `isolated` (isolated), `disisolating` (de-isolating), `recycling` (recycling), `recycled` (recycled), `job running` (task executing), `offline` (offline), `migrating` (migrating), `expanding` (scaling out), `waitSwitch` (waiting to switch), `switching` (switching), `readonly` (readonly), `restarting` (restarting), `network changing` (network modification in progress), `upgrading` (kernel version upgrading), `audit-switching` (audit status changing), `primary-switching` (primary-secondary switching), `offlining` (offline), `deployment changing` (modify AZ), `cloning` (recovering data), `parameter modifying` (parameter modification in progress), `log-switching` (log status change), `restoring` (recovering), and `expanding` (scaling out)</p>
        :rtype: str
        """
        return self._DBInstanceStatus

    @DBInstanceStatus.setter
    def DBInstanceStatus(self, DBInstanceStatus):
        self._DBInstanceStatus = DBInstanceStatus

    @property
    def DBInstanceMemory(self):
        r"""<p>Memory size allocated to the instance, measurement unit: GB</p>
        :rtype: int
        """
        return self._DBInstanceMemory

    @DBInstanceMemory.setter
    def DBInstanceMemory(self, DBInstanceMemory):
        self._DBInstanceMemory = DBInstanceMemory

    @property
    def DBInstanceStorage(self):
        r"""<p>Storage space size allocated to the instance, measurement unit: GB</p>
        :rtype: int
        """
        return self._DBInstanceStorage

    @DBInstanceStorage.setter
    def DBInstanceStorage(self, DBInstanceStorage):
        self._DBInstanceStorage = DBInstanceStorage

    @property
    def DBInstanceCpu(self):
        r"""<p>Number of CPUs allocated to the instance, unit: piece</p>
        :rtype: int
        """
        return self._DBInstanceCpu

    @DBInstanceCpu.setter
    def DBInstanceCpu(self, DBInstanceCpu):
        self._DBInstanceCpu = DBInstanceCpu

    @property
    def DBInstanceClass(self):
        r"""<p>Purchasable specification ID.</p>
        :rtype: str
        """
        return self._DBInstanceClass

    @DBInstanceClass.setter
    def DBInstanceClass(self, DBInstanceClass):
        self._DBInstanceClass = DBInstanceClass

    @property
    def DBMajorVersion(self):
        r"""<p>PostgreSQL major version number. Version information can be obtained from <a href="https://www.tencentcloud.com/document/api/409/89018?from_cn_redirect=1">DescribeDBVersions</a>. Currently supports major versions 10, 11, 12, 13, 14, and 15.</p>
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBVersion(self):
        r"""<p>PostgreSQL community major version + minor version number, such as 12.4. Version information can be obtained from <a href="https://www.tencentcloud.com/document/api/409/89018?from_cn_redirect=1">DescribeDBVersions</a>.</p>
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def DBKernelVersion(self):
        r"""<p>PostgreSQL Kernel Version, for example v12.7_r1.8. Version information can be obtained from <a href="https://www.tencentcloud.com/document/api/409/89018?from_cn_redirect=1">DescribeDBVersions</a>.</p>
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def DBInstanceType(self):
        r"""<p>Instance types:</p><li>primary: Primary instance</li><li>readonly: Read-only instance</li><li>guard: Disaster recovery instance</li><li>temp: Temporary instance</li>
        :rtype: str
        """
        return self._DBInstanceType

    @DBInstanceType.setter
    def DBInstanceType(self, DBInstanceType):
        self._DBInstanceType = DBInstanceType

    @property
    def DBInstanceVersion(self):
        r"""<p>Instance version currently only supports standard (dual-server high-availability edition, one master and one slave).</p>
        :rtype: str
        """
        return self._DBInstanceVersion

    @DBInstanceVersion.setter
    def DBInstanceVersion(self, DBInstanceVersion):
        self._DBInstanceVersion = DBInstanceVersion

    @property
    def DBCharset(self):
        r"""<p>Instance character set, which currently supports only:</p><li>UTF8</li><li>LATIN1</li>
        :rtype: str
        """
        return self._DBCharset

    @DBCharset.setter
    def DBCharset(self, DBCharset):
        self._DBCharset = DBCharset

    @property
    def CreateTime(self):
        r"""<p>Instance creation time.</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>The time when the instance executed the last update.</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ExpireTime(self):
        r"""<p>Instance expiration time.</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsolatedTime(self):
        r"""<p>Instance isolation time.</p>
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def PayType(self):
        r"""<p>Billing mode:</p><li>prepaid: Yearly/monthly subscription, prepayment</li><li>postpaid: Pay-as-you-go, postpaid</li>
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def AutoRenew(self):
        r"""<p>Auto-renewal or not:</p><li>0: Manual renewal</li><li>1: Auto renewal</li>Default value: 0
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def DBInstanceNetInfo(self):
        r"""<p>Instance network connection information.</p>
        :rtype: list of DBInstanceNetInfo
        """
        return self._DBInstanceNetInfo

    @DBInstanceNetInfo.setter
    def DBInstanceNetInfo(self, DBInstanceNetInfo):
        self._DBInstanceNetInfo = DBInstanceNetInfo

    @property
    def Type(self):
        r"""<p>Machine type.</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppId(self):
        r"""<p>User's app id.</p>
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uid(self):
        r"""<p>Uid of the instance.</p>
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def ProjectId(self):
        r"""<p>Project ID.</p>
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TagList(self):
        r"""<p>Tag information associated with the instance.</p>
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def MasterDBInstanceId(self):
        r"""<p>Primary instance information. Returned only when the instance is a read-only instance.</p>
        :rtype: str
        """
        return self._MasterDBInstanceId

    @MasterDBInstanceId.setter
    def MasterDBInstanceId(self, MasterDBInstanceId):
        self._MasterDBInstanceId = MasterDBInstanceId

    @property
    def ReadOnlyInstanceNum(self):
        r"""<p>Number of read-only instances.</p>
        :rtype: int
        """
        return self._ReadOnlyInstanceNum

    @ReadOnlyInstanceNum.setter
    def ReadOnlyInstanceNum(self, ReadOnlyInstanceNum):
        self._ReadOnlyInstanceNum = ReadOnlyInstanceNum

    @property
    def StatusInReadonlyGroup(self):
        r"""<p>State of the read-only instance in the read-only group.</p>
        :rtype: str
        """
        return self._StatusInReadonlyGroup

    @StatusInReadonlyGroup.setter
    def StatusInReadonlyGroup(self, StatusInReadonlyGroup):
        self._StatusInReadonlyGroup = StatusInReadonlyGroup

    @property
    def OfflineTime(self):
        r"""<p>Offline time.</p>
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def DBNodeSet(self):
        r"""<p>Instance node information.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DBNode
        """
        return self._DBNodeSet

    @DBNodeSet.setter
    def DBNodeSet(self, DBNodeSet):
        self._DBNodeSet = DBNodeSet

    @property
    def IsSupportTDE(self):
        r"""<p>Whether the instance supports TDE data encryption:</p><li>0: Not supported</li><li>1: Supported</li>Default value: 0. For TDE data encryption, see [Overview of Data Transparent Encryption](https://www.tencentcloud.com/document/product/409/71748?from_cn_redirect=1).
        :rtype: int
        """
        return self._IsSupportTDE

    @IsSupportTDE.setter
    def IsSupportTDE(self, IsSupportTDE):
        self._IsSupportTDE = IsSupportTDE

    @property
    def DBEngine(self):
        r"""<p>Database engine, support:</p><li>`postgresql`: TencentDB for PostgreSQL</li><li>`mssql_compatible`: MSSQL compatible - TencentDB for PostgreSQL</li>Default value: postgresql
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def DBEngineConfig(self):
        r"""<p>Configuration information for the database engine. The configuration format is as follows:<br>{&quot;$key1&quot;:&quot;$value1&quot;, &quot;$key2&quot;:&quot;$value2&quot;}<br>Supported engines:<br>mssql_compatible engine:</p><li>migrationMode: Database schema, optional parameter. Valid values: single-db (single-database mode), multi-db (multi-database mode). Default is single-db.</li><li>defaultLocale: Sorting area rule, optional parameter, cannot be modified after initialization. Default is en_US. Valid values include: "af_ZA", "sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "hy_AM", "az_Cyrl_AZ", "az_Latn_AZ", "eu_ES", "be_BY", "bg_BG", "ca_ES", "zh_HK", "zh_MO", "zh_CN", "zh_SG", "zh_TW", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_BZ", "en_CA", "en_IE", "en_JM", "en_NZ", "en_PH", "en_ZA", "en_TT", "en_GB", "en_US", "en_ZW", "et_EE", "fo_FO", "fa_IR", "fi_FI", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_MC", "fr_CH", "mk_MK", "ka_GE", "de_AT", "de_DE", "de_LI", "de_LU", "de_CH", "el_GR", "gu_IN", "he_IL", "hi_IN", "hu_HU", "is_IS", "id_ID", "it_IT", "it_CH", "ja_JP", "kn_IN", "kok_IN", "ko_KR", "ky_KG", "lv_LV", "lt_LT", "ms_BN", "ms_MY", "mr_IN", "mn_MN", "nb_NO", "nn_NO", "pl_PL", "pt_BR", "pt_PT", "pa_IN", "ro_RO", "ru_RU", "sa_IN", "sr_Cyrl_RS", "sr_Latn_RS", "sk_SK", "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY","es_PE", "es_PR", "es_ES", "es_TRADITIONAL", "es_UY", "es_VE", "sw_KE", "sv_FI", "sv_SE", "tt_RU", "te_IN", "th_TH", "tr_TR", "uk_UA", "ur_IN", "ur_PK", "uz_Cyrl_UZ", "uz_Latn_UZ", "vi_VN".</li><li>serverCollationName: Collation name, optional parameter, cannot be modified after initialization. Default is sql_latin1_general_cp1_ci_as. Valid values include: "bbf_unicode_general_ci_as", "bbf_unicode_cp1_ci_as", "bbf_unicode_CP1250_ci_as", "bbf_unicode_CP1251_ci_as", "bbf_unicode_cp1253_ci_as", "bbf_unicode_cp1254_ci_as", "bbf_unicode_cp1255_ci_as", "bbf_unicode_cp1256_ci_as", "bbf_unicode_cp1257_ci_as", "bbf_unicode_cp1258_ci_as", "bbf_unicode_cp874_ci_as", "sql_latin1_general_cp1250_ci_as", "sql_latin1_general_cp1251_ci_as", "sql_latin1_general_cp1_ci_as", "sql_latin1_general_cp1253_ci_as", "sql_latin1_general_cp1254_ci_as", "sql_latin1_general_cp1255_ci_as","sql_latin1_general_cp1256_ci_as", "sql_latin1_general_cp1257_ci_as", "sql_latin1_general_cp1258_ci_as", "chinese_prc_ci_as", "cyrillic_general_ci_as", "finnish_swedish_ci_as", "french_ci_as", "japanese_ci_as", "korean_wansung_ci_as", "latin1_general_ci_as", "modern_spanish_ci_as", "polish_ci_as", "thai_ci_as", "traditional_spanish_ci_as", "turkish_ci_as", "ukrainian_ci_as", "vietnamese_ci_as".</li>
        :rtype: str
        """
        return self._DBEngineConfig

    @DBEngineConfig.setter
    def DBEngineConfig(self, DBEngineConfig):
        self._DBEngineConfig = DBEngineConfig

    @property
    def NetworkAccessList(self):
        r"""<p>Instance network information list (deprecated)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of NetworkAccess
        """
        return self._NetworkAccessList

    @NetworkAccessList.setter
    def NetworkAccessList(self, NetworkAccessList):
        self._NetworkAccessList = NetworkAccessList

    @property
    def SupportIpv6(self):
        r"""<p>Whether the instance supports Ipv6:</p><li>0: No</li><li>1: Yes</li>Default value: 0
        :rtype: int
        """
        return self._SupportIpv6

    @SupportIpv6.setter
    def SupportIpv6(self, SupportIpv6):
        self._SupportIpv6 = SupportIpv6

    @property
    def ExpandedCpu(self):
        r"""<p>Number of cpu cores that have been elastically scaled out for the instance</p>
        :rtype: int
        """
        return self._ExpandedCpu

    @ExpandedCpu.setter
    def ExpandedCpu(self, ExpandedCpu):
        self._ExpandedCpu = ExpandedCpu

    @property
    def DeletionProtection(self):
        r"""<p>Whether to enable deletion protection for the instance, values as follows:</p><ul><li>true: enable deletion protection</li><li>false: disable deletion protection</li></ul>
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def DBInstanceStorageType(self):
        r"""<p>Instance storage type. Available values: PHYSICAL_LOCAL_SSD: LOCAL SSD hard disk of PHYSICAL machine; CLOUD_PREMIUM: high-performance CLOUD block storage; CLOUD_SSD: SSD CLOUD disk; CLOUD_HSSD: enhanced SSD CLOUD disk.</p>
        :rtype: str
        """
        return self._DBInstanceStorageType

    @DBInstanceStorageType.setter
    def DBInstanceStorageType(self, DBInstanceStorageType):
        self._DBInstanceStorageType = DBInstanceStorageType


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DBInstanceId = params.get("DBInstanceId")
        self._DBInstanceName = params.get("DBInstanceName")
        self._DBInstanceStatus = params.get("DBInstanceStatus")
        self._DBInstanceMemory = params.get("DBInstanceMemory")
        self._DBInstanceStorage = params.get("DBInstanceStorage")
        self._DBInstanceCpu = params.get("DBInstanceCpu")
        self._DBInstanceClass = params.get("DBInstanceClass")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBVersion = params.get("DBVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._DBInstanceType = params.get("DBInstanceType")
        self._DBInstanceVersion = params.get("DBInstanceVersion")
        self._DBCharset = params.get("DBCharset")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._IsolatedTime = params.get("IsolatedTime")
        self._PayType = params.get("PayType")
        self._AutoRenew = params.get("AutoRenew")
        if params.get("DBInstanceNetInfo") is not None:
            self._DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self._DBInstanceNetInfo.append(obj)
        self._Type = params.get("Type")
        self._AppId = params.get("AppId")
        self._Uid = params.get("Uid")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._MasterDBInstanceId = params.get("MasterDBInstanceId")
        self._ReadOnlyInstanceNum = params.get("ReadOnlyInstanceNum")
        self._StatusInReadonlyGroup = params.get("StatusInReadonlyGroup")
        self._OfflineTime = params.get("OfflineTime")
        if params.get("DBNodeSet") is not None:
            self._DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self._DBNodeSet.append(obj)
        self._IsSupportTDE = params.get("IsSupportTDE")
        self._DBEngine = params.get("DBEngine")
        self._DBEngineConfig = params.get("DBEngineConfig")
        if params.get("NetworkAccessList") is not None:
            self._NetworkAccessList = []
            for item in params.get("NetworkAccessList"):
                obj = NetworkAccess()
                obj._deserialize(item)
                self._NetworkAccessList.append(obj)
        self._SupportIpv6 = params.get("SupportIpv6")
        self._ExpandedCpu = params.get("ExpandedCpu")
        self._DeletionProtection = params.get("DeletionProtection")
        self._DBInstanceStorageType = params.get("DBInstanceStorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstanceNetInfo(AbstractModel):
    r"""Instance network connection information

    """

    def __init__(self):
        r"""
        :param _Address: DNS domain name
        :type Address: str
        :param _Ip: Ip
        :type Ip: str
        :param _Port: Connection port address
        :type Port: int
        :param _NetType: Network type. 1: inner (private network address), 2: public (public network address)
        :type NetType: str
        :param _Status: Network connection status. Valid values: `initing` (never enabled before), `opened` (enabled), `closed` (disabled), `opening` (enabling), `closing` (disabling)
        :type Status: str
        :param _VpcId: VPC ID. specifies the ID of the virtual private cloud.
        :type VpcId: str
        :param _SubnetId: Subnet ID.
        :type SubnetId: str
        :param _ProtocolType: Specifies the protocol type to connect to the database. currently supported: postgresql, mssql (mssql compatible syntax).
        :type ProtocolType: str
        """
        self._Address = None
        self._Ip = None
        self._Port = None
        self._NetType = None
        self._Status = None
        self._VpcId = None
        self._SubnetId = None
        self._ProtocolType = None

    @property
    def Address(self):
        r"""DNS domain name
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Ip(self):
        r"""Ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Connection port address
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NetType(self):
        r"""Network type. 1: inner (private network address), 2: public (public network address)
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Status(self):
        r"""Network connection status. Valid values: `initing` (never enabled before), `opened` (enabled), `closed` (disabled), `opening` (enabling), `closing` (disabling)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VpcId(self):
        r"""VPC ID. specifies the ID of the virtual private cloud.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProtocolType(self):
        r"""Specifies the protocol type to connect to the database. currently supported: postgresql, mssql (mssql compatible syntax).
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._NetType = params.get("NetType")
        self._Status = params.get("Status")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProtocolType = params.get("ProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBNode(AbstractModel):
    r"""Describes the instance node information, including the node type, availability zone where the node is located, and dedicated cluster where the node resides.

    """

    def __init__(self):
        r"""
        :param _Role: Node type. Valid values:
`Primary`;
`Standby`.
        :type Role: str
        :param _Zone: AZ where the node resides, such as ap-guangzhou-1.
        :type Zone: str
        :param _DedicatedClusterId: CDC ID.
        :type DedicatedClusterId: str
        """
        self._Role = None
        self._Zone = None
        self._DedicatedClusterId = None

    @property
    def Role(self):
        r"""Node type. Valid values:
`Primary`;
`Standby`.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Zone(self):
        r"""AZ where the node resides, such as ap-guangzhou-1.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DedicatedClusterId(self):
        r"""CDC ID.
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Zone = params.get("Zone")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    r"""Describes the database detailed information, including owner and character encoding.

    """

    def __init__(self):
        r"""
        :param _DatabaseName: Database name
        :type DatabaseName: str
        :param _DatabaseOwner: Specifies the database owner.
        :type DatabaseOwner: str
        :param _Encoding: Specifies the database character encoding.
        :type Encoding: str
        :param _Collate: Specifies the database sorting rule.
        :type Collate: str
        :param _Ctype: Specifies the character category of the database.
        :type Ctype: str
        :param _AllowConn: Specifies whether the database allows connections.
        :type AllowConn: bool
        :param _ConnLimit: Maximum number of connections for the database. -1 indicates unlimited.
        :type ConnLimit: int
        :param _Privileges: Specifies the database permission list.
        :type Privileges: str
        """
        self._DatabaseName = None
        self._DatabaseOwner = None
        self._Encoding = None
        self._Collate = None
        self._Ctype = None
        self._AllowConn = None
        self._ConnLimit = None
        self._Privileges = None

    @property
    def DatabaseName(self):
        r"""Database name
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatabaseOwner(self):
        r"""Specifies the database owner.
        :rtype: str
        """
        return self._DatabaseOwner

    @DatabaseOwner.setter
    def DatabaseOwner(self, DatabaseOwner):
        self._DatabaseOwner = DatabaseOwner

    @property
    def Encoding(self):
        r"""Specifies the database character encoding.
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Collate(self):
        r"""Specifies the database sorting rule.
        :rtype: str
        """
        return self._Collate

    @Collate.setter
    def Collate(self, Collate):
        self._Collate = Collate

    @property
    def Ctype(self):
        r"""Specifies the character category of the database.
        :rtype: str
        """
        return self._Ctype

    @Ctype.setter
    def Ctype(self, Ctype):
        self._Ctype = Ctype

    @property
    def AllowConn(self):
        r"""Specifies whether the database allows connections.
        :rtype: bool
        """
        return self._AllowConn

    @AllowConn.setter
    def AllowConn(self, AllowConn):
        self._AllowConn = AllowConn

    @property
    def ConnLimit(self):
        r"""Maximum number of connections for the database. -1 indicates unlimited.
        :rtype: int
        """
        return self._ConnLimit

    @ConnLimit.setter
    def ConnLimit(self, ConnLimit):
        self._ConnLimit = ConnLimit

    @property
    def Privileges(self):
        r"""Specifies the database permission list.
        :rtype: str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._DatabaseOwner = params.get("DatabaseOwner")
        self._Encoding = params.get("Encoding")
        self._Collate = params.get("Collate")
        self._Ctype = params.get("Ctype")
        self._AllowConn = params.get("AllowConn")
        self._ConnLimit = params.get("ConnLimit")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseObject(AbstractModel):
    r"""Describes the type of a certain object in the database, and the database, mode, and table of the object.

    """

    def __init__(self):
        r"""
        :param _ObjectType: Specifies the supported object types in the database: account, database, schema, sequence, procedure, type, function, table, view, matview, column.
        :type ObjectType: str
        :param _ObjectName: Specifies the database object name.
        :type ObjectName: str
        :param _DatabaseName: Describes the database object and the database name it belongs to. this parameter is required when the description object type is not database.
        :type DatabaseName: str
        :param _SchemaName: Specifies the schema name of the database object to describe. this parameter is required when the description object is not database or schema.
        :type SchemaName: str
        :param _TableName: Specifies the database object to describe and the table name it belongs to. this parameter is required when the object type is column.
        :type TableName: str
        """
        self._ObjectType = None
        self._ObjectName = None
        self._DatabaseName = None
        self._SchemaName = None
        self._TableName = None

    @property
    def ObjectType(self):
        r"""Specifies the supported object types in the database: account, database, schema, sequence, procedure, type, function, table, view, matview, column.
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def ObjectName(self):
        r"""Specifies the database object name.
        :rtype: str
        """
        return self._ObjectName

    @ObjectName.setter
    def ObjectName(self, ObjectName):
        self._ObjectName = ObjectName

    @property
    def DatabaseName(self):
        r"""Describes the database object and the database name it belongs to. this parameter is required when the description object type is not database.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SchemaName(self):
        r"""Specifies the schema name of the database object to describe. this parameter is required when the description object is not database or schema.
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TableName(self):
        r"""Specifies the database object to describe and the table name it belongs to. this parameter is required when the object type is column.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._ObjectType = params.get("ObjectType")
        self._ObjectName = params.get("ObjectName")
        self._DatabaseName = params.get("DatabaseName")
        self._SchemaName = params.get("SchemaName")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    r"""Specifies the permission list of the specified account for the database object.

    """

    def __init__(self):
        r"""
        :param _Object: The database object. when ObjectType is database, DatabaseName/SchemaName/TableName can be empty. when ObjectType is schema, SchemaName/TableName can be empty. when ObjectType is column, TableName cannot be empty. other cases can be empty.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Object: :class:`tencentcloud.postgres.v20170312.models.DatabaseObject`
        :param _PrivilegeSet: Specifies the permission list of the specified account for the database object.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivilegeSet: list of str
        """
        self._Object = None
        self._PrivilegeSet = None

    @property
    def Object(self):
        r"""The database object. when ObjectType is database, DatabaseName/SchemaName/TableName can be empty. when ObjectType is schema, SchemaName/TableName can be empty. when ObjectType is column, TableName cannot be empty. other cases can be empty.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DatabaseObject`
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def PrivilegeSet(self):
        r"""Specifies the permission list of the specified account for the database object.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._PrivilegeSet

    @PrivilegeSet.setter
    def PrivilegeSet(self, PrivilegeSet):
        self._PrivilegeSet = PrivilegeSet


    def _deserialize(self, params):
        if params.get("Object") is not None:
            self._Object = DatabaseObject()
            self._Object._deserialize(params.get("Object"))
        self._PrivilegeSet = params.get("PrivilegeSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedCluster(AbstractModel):
    r"""Exclusive cluster-related information, used for querying the user's exclusive cluster list.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: CDC ID.
        :type DedicatedClusterId: str
        :param _Name: Dedicated cluster name.
        :type Name: str
        :param _Zone: Specifies the AZ of the exclusive cluster.
        :type Zone: str
        :param _StandbyDedicatedClusterSet: Disaster recovery cluster.
        :type StandbyDedicatedClusterSet: list of str
        :param _InstanceCount: Specifies the instance count.
        :type InstanceCount: int
        :param _CpuTotal: Total number of cpus.
        :type CpuTotal: int
        :param _CpuAvailable: Specifies the available amount of Cpu.
        :type CpuAvailable: int
        :param _MemTotal: Total memory capacity in GB.
        :type MemTotal: int
        :param _MemAvailable: Available memory in GB.
        :type MemAvailable: int
        :param _DiskTotal: Total disk capacity (unit: GB).
        :type DiskTotal: int
        :param _DiskAvailable: Disk availability (unit: GB).
        :type DiskAvailable: int
        """
        self._DedicatedClusterId = None
        self._Name = None
        self._Zone = None
        self._StandbyDedicatedClusterSet = None
        self._InstanceCount = None
        self._CpuTotal = None
        self._CpuAvailable = None
        self._MemTotal = None
        self._MemAvailable = None
        self._DiskTotal = None
        self._DiskAvailable = None

    @property
    def DedicatedClusterId(self):
        r"""CDC ID.
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def Name(self):
        r"""Dedicated cluster name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Zone(self):
        r"""Specifies the AZ of the exclusive cluster.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def StandbyDedicatedClusterSet(self):
        r"""Disaster recovery cluster.
        :rtype: list of str
        """
        return self._StandbyDedicatedClusterSet

    @StandbyDedicatedClusterSet.setter
    def StandbyDedicatedClusterSet(self, StandbyDedicatedClusterSet):
        self._StandbyDedicatedClusterSet = StandbyDedicatedClusterSet

    @property
    def InstanceCount(self):
        r"""Specifies the instance count.
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def CpuTotal(self):
        r"""Total number of cpus.
        :rtype: int
        """
        return self._CpuTotal

    @CpuTotal.setter
    def CpuTotal(self, CpuTotal):
        self._CpuTotal = CpuTotal

    @property
    def CpuAvailable(self):
        r"""Specifies the available amount of Cpu.
        :rtype: int
        """
        return self._CpuAvailable

    @CpuAvailable.setter
    def CpuAvailable(self, CpuAvailable):
        self._CpuAvailable = CpuAvailable

    @property
    def MemTotal(self):
        r"""Total memory capacity in GB.
        :rtype: int
        """
        return self._MemTotal

    @MemTotal.setter
    def MemTotal(self, MemTotal):
        self._MemTotal = MemTotal

    @property
    def MemAvailable(self):
        r"""Available memory in GB.
        :rtype: int
        """
        return self._MemAvailable

    @MemAvailable.setter
    def MemAvailable(self, MemAvailable):
        self._MemAvailable = MemAvailable

    @property
    def DiskTotal(self):
        r"""Total disk capacity (unit: GB).
        :rtype: int
        """
        return self._DiskTotal

    @DiskTotal.setter
    def DiskTotal(self, DiskTotal):
        self._DiskTotal = DiskTotal

    @property
    def DiskAvailable(self):
        r"""Disk availability (unit: GB).
        :rtype: int
        """
        return self._DiskAvailable

    @DiskAvailable.setter
    def DiskAvailable(self, DiskAvailable):
        self._DiskAvailable = DiskAvailable


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._Name = params.get("Name")
        self._Zone = params.get("Zone")
        self._StandbyDedicatedClusterSet = params.get("StandbyDedicatedClusterSet")
        self._InstanceCount = params.get("InstanceCount")
        self._CpuTotal = params.get("CpuTotal")
        self._CpuAvailable = params.get("CpuAvailable")
        self._MemTotal = params.get("MemTotal")
        self._MemAvailable = params.get("MemAvailable")
        self._DiskTotal = params.get("DiskTotal")
        self._DiskAvailable = params.get("DiskAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    r"""DeleteAccount request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :type DBInstanceId: str
        :param _UserName: Account name to be deleted. obtain through the api [DescribeAccounts](https://www.tencentcloud.com/document/api/409/18109?from_cn_redirect=1).
        :type UserName: str
        """
        self._DBInstanceId = None
        self._UserName = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""Account name to be deleted. obtain through the api [DescribeAccounts](https://www.tencentcloud.com/document/api/409/18109?from_cn_redirect=1).
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    r"""DeleteAccount response structure.

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


class DeleteBackupPlanRequest(AbstractModel):
    r"""DeleteBackupPlan request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _PlanId: Backup plan ID. obtain through the api [DescribeBackupPlans](https://www.tencentcloud.com/document/product/409/45151?lang=en).
        :type PlanId: str
        """
        self._DBInstanceId = None
        self._PlanId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def PlanId(self):
        r"""Backup plan ID. obtain through the api [DescribeBackupPlans](https://www.tencentcloud.com/document/product/409/45151?lang=en).
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupPlanResponse(AbstractModel):
    r"""DeleteBackupPlan response structure.

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


class DeleteBaseBackupRequest(AbstractModel):
    r"""DeleteBaseBackup request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _BaseBackupId: Data backup ID. obtain through the api [DescribeBaseBackups](https://www.tencentcloud.com/document/product/409/54343?lang=en). automatic backup sets cannot be deleted within 7 days.
        :type BaseBackupId: str
        """
        self._DBInstanceId = None
        self._BaseBackupId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def BaseBackupId(self):
        r"""Data backup ID. obtain through the api [DescribeBaseBackups](https://www.tencentcloud.com/document/product/409/54343?lang=en). automatic backup sets cannot be deleted within 7 days.
        :rtype: str
        """
        return self._BaseBackupId

    @BaseBackupId.setter
    def BaseBackupId(self, BaseBackupId):
        self._BaseBackupId = BaseBackupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._BaseBackupId = params.get("BaseBackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBaseBackupResponse(AbstractModel):
    r"""DeleteBaseBackup response structure.

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


class DeleteDBInstanceNetworkAccessRequest(AbstractModel):
    r"""DeleteDBInstanceNetworkAccess request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of postgres-6bwgamo3.
        :type DBInstanceId: str
        :param _VpcId: Unified VPC ID. If you want to delete the classic network, set the parameter to `0`.
        :type VpcId: str
        :param _SubnetId: Subnet ID. If you want to delete the classic network, set the parameter to `0`.
        :type SubnetId: str
        :param _Vip: Target VIP.
        :type Vip: str
        """
        self._DBInstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-6bwgamo3.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def VpcId(self):
        r"""Unified VPC ID. If you want to delete the classic network, set the parameter to `0`.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID. If you want to delete the classic network, set the parameter to `0`.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        r"""Target VIP.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBInstanceNetworkAccessResponse(AbstractModel):
    r"""DeleteDBInstanceNetworkAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
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


class DeleteLogBackupRequest(AbstractModel):
    r"""DeleteLogBackup request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _LogBackupId: Log backup ID
        :type LogBackupId: str
        """
        self._DBInstanceId = None
        self._LogBackupId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def LogBackupId(self):
        r"""Log backup ID
        :rtype: str
        """
        return self._LogBackupId

    @LogBackupId.setter
    def LogBackupId(self, LogBackupId):
        self._LogBackupId = LogBackupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._LogBackupId = params.get("LogBackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogBackupResponse(AbstractModel):
    r"""DeleteLogBackup response structure.

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


class DeleteParameterTemplateRequest(AbstractModel):
    r"""DeleteParameterTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID, which uniquely identifies the parameter template to be operated.
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""Parameter template ID, which uniquely identifies the parameter template to be operated.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParameterTemplateResponse(AbstractModel):
    r"""DeleteParameterTemplate response structure.

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


class DeleteReadOnlyGroupNetworkAccessRequest(AbstractModel):
    r"""DeleteReadOnlyGroupNetworkAccess request structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: RO group ID in the format of pgro-4t9c6g7k.
        :type ReadOnlyGroupId: str
        :param _VpcId: Unified VPC ID. If you want to delete the classic network, set the parameter to `0`.
        :type VpcId: str
        :param _SubnetId: Subnet ID. If you want to delete the classic network, set the parameter to `0`.
        :type SubnetId: str
        :param _Vip: Target VIP.
        :type Vip: str
        """
        self._ReadOnlyGroupId = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None

    @property
    def ReadOnlyGroupId(self):
        r"""RO group ID in the format of pgro-4t9c6g7k.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def VpcId(self):
        r"""Unified VPC ID. If you want to delete the classic network, set the parameter to `0`.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID. If you want to delete the classic network, set the parameter to `0`.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        r"""Target VIP.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReadOnlyGroupNetworkAccessResponse(AbstractModel):
    r"""DeleteReadOnlyGroupNetworkAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
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


class DeleteReadOnlyGroupRequest(AbstractModel):
    r"""DeleteReadOnlyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: ID of the RO group to be deleted
        :type ReadOnlyGroupId: str
        """
        self._ReadOnlyGroupId = None

    @property
    def ReadOnlyGroupId(self):
        r"""ID of the RO group to be deleted
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReadOnlyGroupResponse(AbstractModel):
    r"""DeleteReadOnlyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task ID
Note: this field may return `null`, indicating that no valid values can be obtained.
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


class DeleteServerlessDBInstanceRequest(AbstractModel):
    r"""DeleteServerlessDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceName: Instance name. Either instance name or instance ID (or both) must be passed in. If both are passed in, the instance ID will prevail.
        :type DBInstanceName: str
        :param _DBInstanceId: Instance ID. Either instance name or instance ID (or both) must be passed in. If both are passed in, the instance ID will prevail.
        :type DBInstanceId: str
        """
        self._DBInstanceName = None
        self._DBInstanceId = None

    @property
    def DBInstanceName(self):
        r"""Instance name. Either instance name or instance ID (or both) must be passed in. If both are passed in, the instance ID will prevail.
        :rtype: str
        """
        return self._DBInstanceName

    @DBInstanceName.setter
    def DBInstanceName(self, DBInstanceName):
        self._DBInstanceName = DBInstanceName

    @property
    def DBInstanceId(self):
        r"""Instance ID. Either instance name or instance ID (or both) must be passed in. If both are passed in, the instance ID will prevail.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceName = params.get("DBInstanceName")
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServerlessDBInstanceResponse(AbstractModel):
    r"""DeleteServerlessDBInstance response structure.

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


class DescribeAccountPrivilegesRequest(AbstractModel):
    r"""DescribeAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _UserName: Describes the permissions owned by this account for a database object. the account name can be obtained through the [DescribeAccounts](https://www.tencentcloud.com/document/product/409/18109?lang=en) api.
        :type UserName: str
        :param _DatabaseObjectSet: Specifies the database object information to query.
        :type DatabaseObjectSet: list of DatabaseObject
        """
        self._DBInstanceId = None
        self._UserName = None
        self._DatabaseObjectSet = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""Describes the permissions owned by this account for a database object. the account name can be obtained through the [DescribeAccounts](https://www.tencentcloud.com/document/product/409/18109?lang=en) api.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DatabaseObjectSet(self):
        r"""Specifies the database object information to query.
        :rtype: list of DatabaseObject
        """
        return self._DatabaseObjectSet

    @DatabaseObjectSet.setter
    def DatabaseObjectSet(self, DatabaseObjectSet):
        self._DatabaseObjectSet = DatabaseObjectSet


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        if params.get("DatabaseObjectSet") is not None:
            self._DatabaseObjectSet = []
            for item in params.get("DatabaseObjectSet"):
                obj = DatabaseObject()
                obj._deserialize(item)
                self._DatabaseObjectSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    r"""DescribeAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _PrivilegeSet: Specifies that the user has CREATE, CONNECT, and TEMPORARY permissions on the database user_database.
        :type PrivilegeSet: list of DatabasePrivilege
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PrivilegeSet = None
        self._RequestId = None

    @property
    def PrivilegeSet(self):
        r"""Specifies that the user has CREATE, CONNECT, and TEMPORARY permissions on the database user_database.
        :rtype: list of DatabasePrivilege
        """
        return self._PrivilegeSet

    @PrivilegeSet.setter
    def PrivilegeSet(self, PrivilegeSet):
        self._PrivilegeSet = PrivilegeSet

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
        if params.get("PrivilegeSet") is not None:
            self._PrivilegeSet = []
            for item in params.get("PrivilegeSet"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self._PrivilegeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    r"""DescribeAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID, such as postgres-6fego161. can be obtained through the DescribeDBInstances api (https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _Limit: Pagination return. maximum return per page. default 20. value range 1-100.
        :type Limit: int
        :param _Offset: Data offset, which starts from 0.
        :type Offset: int
        :param _OrderBy: Return data is sorted by creation time or username. valid values: createTime, name, updateTime. createTime - sort by creation time; name - sort by username; updateTime - sort by update time.
Default value: createTime.
        :type OrderBy: str
        :param _OrderByType: Specifies whether the returned results are in ascending or descending order. valid values: desc or asc. desc - descending order; asc - ascending order.
Default value: desc.
        :type OrderByType: str
        """
        self._DBInstanceId = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def DBInstanceId(self):
        r"""Instance ID, such as postgres-6fego161. can be obtained through the DescribeDBInstances api (https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Limit(self):
        r"""Pagination return. maximum return per page. default 20. value range 1-100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, which starts from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Return data is sorted by creation time or username. valid values: createTime, name, updateTime. createTime - sort by creation time; name - sort by username; updateTime - sort by update time.
Default value: createTime.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Specifies whether the returned results are in ascending or descending order. valid values: desc or asc. desc - descending order; asc - ascending order.
Default value: desc.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    r"""DescribeAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of date entries returned for this API call.
        :type TotalCount: int
        :param _Details: Detailed account list information. when the CreateTime field is 0000-00-00 00:00:00, it means the corresponding account is created by direct connection database, not through the CreateAccount api.
        :type Details: list of AccountInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of date entries returned for this API call.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        r"""Detailed account list information. when the CreateTime field is 0000-00-00 00:00:00, it means the corresponding account is created by direct connection database, not through the CreateAccount api.
        :rtype: list of AccountInfo
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

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
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = AccountInfo()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAvailableRecoveryTimeRequest(AbstractModel):
    r"""DescribeAvailableRecoveryTime request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableRecoveryTimeResponse(AbstractModel):
    r"""DescribeAvailableRecoveryTime response structure.

    """

    def __init__(self):
        r"""
        :param _RecoveryBeginTime: The earliest restoration time (UTC+8).
        :type RecoveryBeginTime: str
        :param _RecoveryEndTime: The latest restoration time (UTC+8).
        :type RecoveryEndTime: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecoveryBeginTime = None
        self._RecoveryEndTime = None
        self._RequestId = None

    @property
    def RecoveryBeginTime(self):
        r"""The earliest restoration time (UTC+8).
        :rtype: str
        """
        return self._RecoveryBeginTime

    @RecoveryBeginTime.setter
    def RecoveryBeginTime(self, RecoveryBeginTime):
        self._RecoveryBeginTime = RecoveryBeginTime

    @property
    def RecoveryEndTime(self):
        r"""The latest restoration time (UTC+8).
        :rtype: str
        """
        return self._RecoveryEndTime

    @RecoveryEndTime.setter
    def RecoveryEndTime(self, RecoveryEndTime):
        self._RecoveryEndTime = RecoveryEndTime

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
        self._RecoveryBeginTime = params.get("RecoveryBeginTime")
        self._RecoveryEndTime = params.get("RecoveryEndTime")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    r"""DescribeBackupDownloadRestriction request structure.

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    r"""DescribeBackupDownloadRestriction response structure.

    """

    def __init__(self):
        r"""
        :param _RestrictionType: Type of the network restrictions for downloading a backup file. Valid values: `NONE` (backups can be downloaded over both private and public networks), `INTRANET` (backups can only be downloaded over the private network), `CUSTOMIZE` (backups can be downloaded over specified VPCs or at specified IPs).
        :type RestrictionType: str
        :param _VpcRestrictionEffect: Whether VPC is allowed. Valid values: `ALLOW` (allow), `DENY` (deny). 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type VpcRestrictionEffect: str
        :param _VpcIdSet: Whether it is allowed to download the VPC ID list of the backup files. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type VpcIdSet: list of str
        :param _IpRestrictionEffect: Whether IP is allowed. Valid values: `ALLOW` (allow), `DENY` (deny). 
Note: Note: This field may return null, indicating that no valid values can be obtained.
        :type IpRestrictionEffect: str
        :param _IpSet: Whether it is allowed to download the IP list of the backup files. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type IpSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RestrictionType = None
        self._VpcRestrictionEffect = None
        self._VpcIdSet = None
        self._IpRestrictionEffect = None
        self._IpSet = None
        self._RequestId = None

    @property
    def RestrictionType(self):
        r"""Type of the network restrictions for downloading a backup file. Valid values: `NONE` (backups can be downloaded over both private and public networks), `INTRANET` (backups can only be downloaded over the private network), `CUSTOMIZE` (backups can be downloaded over specified VPCs or at specified IPs).
        :rtype: str
        """
        return self._RestrictionType

    @RestrictionType.setter
    def RestrictionType(self, RestrictionType):
        self._RestrictionType = RestrictionType

    @property
    def VpcRestrictionEffect(self):
        r"""Whether VPC is allowed. Valid values: `ALLOW` (allow), `DENY` (deny). 
Note:  This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcRestrictionEffect

    @VpcRestrictionEffect.setter
    def VpcRestrictionEffect(self, VpcRestrictionEffect):
        self._VpcRestrictionEffect = VpcRestrictionEffect

    @property
    def VpcIdSet(self):
        r"""Whether it is allowed to download the VPC ID list of the backup files. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._VpcIdSet

    @VpcIdSet.setter
    def VpcIdSet(self, VpcIdSet):
        self._VpcIdSet = VpcIdSet

    @property
    def IpRestrictionEffect(self):
        r"""Whether IP is allowed. Valid values: `ALLOW` (allow), `DENY` (deny). 
Note: Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IpRestrictionEffect

    @IpRestrictionEffect.setter
    def IpRestrictionEffect(self, IpRestrictionEffect):
        self._IpRestrictionEffect = IpRestrictionEffect

    @property
    def IpSet(self):
        r"""Whether it is allowed to download the IP list of the backup files. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._IpSet

    @IpSet.setter
    def IpSet(self, IpSet):
        self._IpSet = IpSet

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
        self._RestrictionType = params.get("RestrictionType")
        self._VpcRestrictionEffect = params.get("VpcRestrictionEffect")
        self._VpcIdSet = params.get("VpcIdSet")
        self._IpRestrictionEffect = params.get("IpRestrictionEffect")
        self._IpSet = params.get("IpSet")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadURLRequest(AbstractModel):
    r"""DescribeBackupDownloadURL request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _BackupType: Backup type. Valid values: `LogBackup`, `BaseBackup`.
        :type BackupType: str
        :param _BackupId: Unique backup ID.
        :type BackupId: str
        :param _URLExpireTime: Validity time of the connection. value range: [0,36]. default value: 12 hours.
        :type URLExpireTime: int
        :param _BackupDownloadRestriction: Backup download restriction
        :type BackupDownloadRestriction: :class:`tencentcloud.postgres.v20170312.models.BackupDownloadRestriction`
        """
        self._DBInstanceId = None
        self._BackupType = None
        self._BackupId = None
        self._URLExpireTime = None
        self._BackupDownloadRestriction = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def BackupType(self):
        r"""Backup type. Valid values: `LogBackup`, `BaseBackup`.
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupId(self):
        r"""Unique backup ID.
        :rtype: str
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def URLExpireTime(self):
        r"""Validity time of the connection. value range: [0,36]. default value: 12 hours.
        :rtype: int
        """
        return self._URLExpireTime

    @URLExpireTime.setter
    def URLExpireTime(self, URLExpireTime):
        self._URLExpireTime = URLExpireTime

    @property
    def BackupDownloadRestriction(self):
        r"""Backup download restriction
        :rtype: :class:`tencentcloud.postgres.v20170312.models.BackupDownloadRestriction`
        """
        return self._BackupDownloadRestriction

    @BackupDownloadRestriction.setter
    def BackupDownloadRestriction(self, BackupDownloadRestriction):
        self._BackupDownloadRestriction = BackupDownloadRestriction


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._BackupType = params.get("BackupType")
        self._BackupId = params.get("BackupId")
        self._URLExpireTime = params.get("URLExpireTime")
        if params.get("BackupDownloadRestriction") is not None:
            self._BackupDownloadRestriction = BackupDownloadRestriction()
            self._BackupDownloadRestriction._deserialize(params.get("BackupDownloadRestriction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadURLResponse(AbstractModel):
    r"""DescribeBackupDownloadURL response structure.

    """

    def __init__(self):
        r"""
        :param _BackupDownloadURL: Backup download URL
        :type BackupDownloadURL: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupDownloadURL = None
        self._RequestId = None

    @property
    def BackupDownloadURL(self):
        r"""Backup download URL
        :rtype: str
        """
        return self._BackupDownloadURL

    @BackupDownloadURL.setter
    def BackupDownloadURL(self, BackupDownloadURL):
        self._BackupDownloadURL = BackupDownloadURL

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
        self._BackupDownloadURL = params.get("BackupDownloadURL")
        self._RequestId = params.get("RequestId")


class DescribeBackupOverviewRequest(AbstractModel):
    r"""DescribeBackupOverview request structure.

    """


class DescribeBackupOverviewResponse(AbstractModel):
    r"""DescribeBackupOverview response structure.

    """

    def __init__(self):
        r"""
        :param _TotalFreeSize: Total free space size in bytes
        :type TotalFreeSize: int
        :param _UsedFreeSize: Used free space size in bytes
        :type UsedFreeSize: int
        :param _UsedBillingSize: Used paid space size in bytes
        :type UsedBillingSize: int
        :param _LogBackupCount: Number of log backups
        :type LogBackupCount: int
        :param _LogBackupSize: Log backup size in bytes
        :type LogBackupSize: int
        :param _ManualBaseBackupCount: Number of manually created full backups
        :type ManualBaseBackupCount: int
        :param _ManualBaseBackupSize: Size of manually created full backups in bytes
        :type ManualBaseBackupSize: int
        :param _AutoBaseBackupCount: Number of automatically created full backups
        :type AutoBaseBackupCount: int
        :param _AutoBaseBackupSize: Size of automatically created full backups in bytes
        :type AutoBaseBackupSize: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalFreeSize = None
        self._UsedFreeSize = None
        self._UsedBillingSize = None
        self._LogBackupCount = None
        self._LogBackupSize = None
        self._ManualBaseBackupCount = None
        self._ManualBaseBackupSize = None
        self._AutoBaseBackupCount = None
        self._AutoBaseBackupSize = None
        self._RequestId = None

    @property
    def TotalFreeSize(self):
        r"""Total free space size in bytes
        :rtype: int
        """
        return self._TotalFreeSize

    @TotalFreeSize.setter
    def TotalFreeSize(self, TotalFreeSize):
        self._TotalFreeSize = TotalFreeSize

    @property
    def UsedFreeSize(self):
        r"""Used free space size in bytes
        :rtype: int
        """
        return self._UsedFreeSize

    @UsedFreeSize.setter
    def UsedFreeSize(self, UsedFreeSize):
        self._UsedFreeSize = UsedFreeSize

    @property
    def UsedBillingSize(self):
        r"""Used paid space size in bytes
        :rtype: int
        """
        return self._UsedBillingSize

    @UsedBillingSize.setter
    def UsedBillingSize(self, UsedBillingSize):
        self._UsedBillingSize = UsedBillingSize

    @property
    def LogBackupCount(self):
        r"""Number of log backups
        :rtype: int
        """
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def LogBackupSize(self):
        r"""Log backup size in bytes
        :rtype: int
        """
        return self._LogBackupSize

    @LogBackupSize.setter
    def LogBackupSize(self, LogBackupSize):
        self._LogBackupSize = LogBackupSize

    @property
    def ManualBaseBackupCount(self):
        r"""Number of manually created full backups
        :rtype: int
        """
        return self._ManualBaseBackupCount

    @ManualBaseBackupCount.setter
    def ManualBaseBackupCount(self, ManualBaseBackupCount):
        self._ManualBaseBackupCount = ManualBaseBackupCount

    @property
    def ManualBaseBackupSize(self):
        r"""Size of manually created full backups in bytes
        :rtype: int
        """
        return self._ManualBaseBackupSize

    @ManualBaseBackupSize.setter
    def ManualBaseBackupSize(self, ManualBaseBackupSize):
        self._ManualBaseBackupSize = ManualBaseBackupSize

    @property
    def AutoBaseBackupCount(self):
        r"""Number of automatically created full backups
        :rtype: int
        """
        return self._AutoBaseBackupCount

    @AutoBaseBackupCount.setter
    def AutoBaseBackupCount(self, AutoBaseBackupCount):
        self._AutoBaseBackupCount = AutoBaseBackupCount

    @property
    def AutoBaseBackupSize(self):
        r"""Size of automatically created full backups in bytes
        :rtype: int
        """
        return self._AutoBaseBackupSize

    @AutoBaseBackupSize.setter
    def AutoBaseBackupSize(self, AutoBaseBackupSize):
        self._AutoBaseBackupSize = AutoBaseBackupSize

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
        self._TotalFreeSize = params.get("TotalFreeSize")
        self._UsedFreeSize = params.get("UsedFreeSize")
        self._UsedBillingSize = params.get("UsedBillingSize")
        self._LogBackupCount = params.get("LogBackupCount")
        self._LogBackupSize = params.get("LogBackupSize")
        self._ManualBaseBackupCount = params.get("ManualBaseBackupCount")
        self._ManualBaseBackupSize = params.get("ManualBaseBackupSize")
        self._AutoBaseBackupCount = params.get("AutoBaseBackupCount")
        self._AutoBaseBackupSize = params.get("AutoBaseBackupSize")
        self._RequestId = params.get("RequestId")


class DescribeBackupPlansRequest(AbstractModel):
    r"""DescribeBackupPlans request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupPlansResponse(AbstractModel):
    r"""DescribeBackupPlans response structure.

    """

    def __init__(self):
        r"""
        :param _Plans: The set of instance backup plans
        :type Plans: list of BackupPlan
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Plans = None
        self._RequestId = None

    @property
    def Plans(self):
        r"""The set of instance backup plans
        :rtype: list of BackupPlan
        """
        return self._Plans

    @Plans.setter
    def Plans(self, Plans):
        self._Plans = Plans

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
        if params.get("Plans") is not None:
            self._Plans = []
            for item in params.get("Plans"):
                obj = BackupPlan()
                obj._deserialize(item)
                self._Plans.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupSummariesRequest(AbstractModel):
    r"""DescribeBackupSummaries request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The maximum number of results returned per page. Value range: 1-100. Default: `10`
        :type Limit: int
        :param _Offset: Data offset, which starts from 0.
        :type Offset: int
        :param _Filters: Filter instances using one or more criteria. Valid filter names:
db-instance-id: Filter by instance ID (in string format).
db-instance-name: Filter by instance name (in string format).
db-instance-ip: Filter by instance VPC IP (in string format).
        :type Filters: list of Filter
        :param _OrderBy: Sorting field. Valid values: `TotalBackupSize`, `LogBackupSize`, `ManualBaseBackupSize`, `AutoBaseBackupSize`.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: `asc` (ascending), `desc` (descending).
        :type OrderByType: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Limit(self):
        r"""The maximum number of results returned per page. Value range: 1-100. Default: `10`
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, which starts from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""Filter instances using one or more criteria. Valid filter names:
db-instance-id: Filter by instance ID (in string format).
db-instance-name: Filter by instance name (in string format).
db-instance-ip: Filter by instance VPC IP (in string format).
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""Sorting field. Valid values: `TotalBackupSize`, `LogBackupSize`, `ManualBaseBackupSize`, `AutoBaseBackupSize`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order. Valid values: `asc` (ascending), `desc` (descending).
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupSummariesResponse(AbstractModel):
    r"""DescribeBackupSummaries response structure.

    """

    def __init__(self):
        r"""
        :param _BackupSummarySet: Backup statistics list.
        :type BackupSummarySet: list of BackupSummary
        :param _TotalCount: Number of all queried backups.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupSummarySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BackupSummarySet(self):
        r"""Backup statistics list.
        :rtype: list of BackupSummary
        """
        return self._BackupSummarySet

    @BackupSummarySet.setter
    def BackupSummarySet(self, BackupSummarySet):
        self._BackupSummarySet = BackupSummarySet

    @property
    def TotalCount(self):
        r"""Number of all queried backups.
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
        if params.get("BackupSummarySet") is not None:
            self._BackupSummarySet = []
            for item in params.get("BackupSummarySet"):
                obj = BackupSummary()
                obj._deserialize(item)
                self._BackupSummarySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBaseBackupsRequest(AbstractModel):
    r"""DescribeBaseBackups request structure.

    """

    def __init__(self):
        r"""
        :param _MinFinishTime: Minimum end time of a backup in the format of `2018-01-01 00:00:00`. It is 7 days ago by default.
        :type MinFinishTime: str
        :param _MaxFinishTime: Maximum end time of a backup in the format of `2018-01-01 00:00:00`. It is the current time by default.
        :type MaxFinishTime: str
        :param _Filters: Query using one or more filter criteria. filter criteria currently supported include:.
db-instance-id: filter by instance id (string type).
db-instance-name: specifies the instance name to filter by, supports fuzzy matching (string type).
db-instance-ip: specifies the instance VPC ip for filtering (string type).
base-backup-id: filter by backup set id (in string format).
db-instance-status: filter by instance status (in string format). valid values refer to the DBInstanceStatus field in the DBInstance structure (https://www.tencentcloud.com/document/product/409/16778#dbinstance).
        :type Filters: list of Filter
        :param _Limit: The maximum number of results returned per page. Value range: 1-100. Default: `10`
        :type Limit: int
        :param _Offset: Data offset, which starts from 0.
        :type Offset: int
        :param _OrderBy: Specifies the sorting field, supports StartTime, FinishTime, and Size. default value: StartTime.
        :type OrderBy: str
        :param _OrderByType: Sorting method, including ascending: `asc` and descending: `desc`. the default value is `desc`.
        :type OrderByType: str
        """
        self._MinFinishTime = None
        self._MaxFinishTime = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def MinFinishTime(self):
        r"""Minimum end time of a backup in the format of `2018-01-01 00:00:00`. It is 7 days ago by default.
        :rtype: str
        """
        return self._MinFinishTime

    @MinFinishTime.setter
    def MinFinishTime(self, MinFinishTime):
        self._MinFinishTime = MinFinishTime

    @property
    def MaxFinishTime(self):
        r"""Maximum end time of a backup in the format of `2018-01-01 00:00:00`. It is the current time by default.
        :rtype: str
        """
        return self._MaxFinishTime

    @MaxFinishTime.setter
    def MaxFinishTime(self, MaxFinishTime):
        self._MaxFinishTime = MaxFinishTime

    @property
    def Filters(self):
        r"""Query using one or more filter criteria. filter criteria currently supported include:.
db-instance-id: filter by instance id (string type).
db-instance-name: specifies the instance name to filter by, supports fuzzy matching (string type).
db-instance-ip: specifies the instance VPC ip for filtering (string type).
base-backup-id: filter by backup set id (in string format).
db-instance-status: filter by instance status (in string format). valid values refer to the DBInstanceStatus field in the DBInstance structure (https://www.tencentcloud.com/document/product/409/16778#dbinstance).
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""The maximum number of results returned per page. Value range: 1-100. Default: `10`
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, which starts from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Specifies the sorting field, supports StartTime, FinishTime, and Size. default value: StartTime.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting method, including ascending: `asc` and descending: `desc`. the default value is `desc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._MinFinishTime = params.get("MinFinishTime")
        self._MaxFinishTime = params.get("MaxFinishTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaseBackupsResponse(AbstractModel):
    r"""DescribeBaseBackups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of queried data backups.
        :type TotalCount: int
        :param _BaseBackupSet: Detailed data backup information list.
        :type BaseBackupSet: list of BaseBackup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BaseBackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of queried data backups.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BaseBackupSet(self):
        r"""Detailed data backup information list.
        :rtype: list of BaseBackup
        """
        return self._BaseBackupSet

    @BaseBackupSet.setter
    def BaseBackupSet(self, BaseBackupSet):
        self._BaseBackupSet = BaseBackupSet

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
        if params.get("BaseBackupSet") is not None:
            self._BaseBackupSet = []
            for item in params.get("BaseBackupSet"):
                obj = BaseBackup()
                obj._deserialize(item)
                self._BaseBackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClassesRequest(AbstractModel):
    r"""DescribeClasses request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ ID, which can be obtained through the `DescribeZones` API.
        :type Zone: str
        :param _DBEngine: Database engines. Valid values:
1. `postgresql` (TencentDB for PostgreSQL)
2. `mssql_compatible` (MSSQL compatible-TencentDB for PostgreSQL)
        :type DBEngine: str
        :param _DBMajorVersion: Major version of a database, such as 12 or 13, which can be obtained through the `DescribeDBVersions` API.
        :type DBMajorVersion: str
        """
        self._Zone = None
        self._DBEngine = None
        self._DBMajorVersion = None

    @property
    def Zone(self):
        r"""AZ ID, which can be obtained through the `DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DBEngine(self):
        r"""Database engines. Valid values:
1. `postgresql` (TencentDB for PostgreSQL)
2. `mssql_compatible` (MSSQL compatible-TencentDB for PostgreSQL)
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def DBMajorVersion(self):
        r"""Major version of a database, such as 12 or 13, which can be obtained through the `DescribeDBVersions` API.
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DBEngine = params.get("DBEngine")
        self._DBMajorVersion = params.get("DBMajorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassesResponse(AbstractModel):
    r"""DescribeClasses response structure.

    """

    def __init__(self):
        r"""
        :param _ClassInfoSet: List of database specifications
        :type ClassInfoSet: list of ClassInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClassInfoSet = None
        self._RequestId = None

    @property
    def ClassInfoSet(self):
        r"""List of database specifications
        :rtype: list of ClassInfo
        """
        return self._ClassInfoSet

    @ClassInfoSet.setter
    def ClassInfoSet(self, ClassInfoSet):
        self._ClassInfoSet = ClassInfoSet

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
        if params.get("ClassInfoSet") is not None:
            self._ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = ClassInfo()
                obj._deserialize(item)
                self._ClassInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloneDBInstanceSpecRequest(AbstractModel):
    r"""DescribeCloneDBInstanceSpec request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _BackupSetId: Basic backup set ID. obtain through the api [DescribeBaseBackups](https://www.tencentcloud.com/document/product/409/54343?lang=en). this parameter and RecoveryTargetTime must be selected. if set simultaneously with RecoveryTargetTime, this parameter takes precedence.
        :type BackupSetId: str
        :param _RecoveryTargetTime: Restoration time (UTC+8). Either this parameter or `BackupSetId` must be passed in.
        :type RecoveryTargetTime: str
        """
        self._DBInstanceId = None
        self._BackupSetId = None
        self._RecoveryTargetTime = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def BackupSetId(self):
        r"""Basic backup set ID. obtain through the api [DescribeBaseBackups](https://www.tencentcloud.com/document/product/409/54343?lang=en). this parameter and RecoveryTargetTime must be selected. if set simultaneously with RecoveryTargetTime, this parameter takes precedence.
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def RecoveryTargetTime(self):
        r"""Restoration time (UTC+8). Either this parameter or `BackupSetId` must be passed in.
        :rtype: str
        """
        return self._RecoveryTargetTime

    @RecoveryTargetTime.setter
    def RecoveryTargetTime(self, RecoveryTargetTime):
        self._RecoveryTargetTime = RecoveryTargetTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._BackupSetId = params.get("BackupSetId")
        self._RecoveryTargetTime = params.get("RecoveryTargetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloneDBInstanceSpecResponse(AbstractModel):
    r"""DescribeCloneDBInstanceSpec response structure.

    """

    def __init__(self):
        r"""
        :param _MinSpecCode: Code of the minimum specification available for purchase.
        :type MinSpecCode: str
        :param _MinStorage: The minimum disk capacity in GB available for purchase.
        :type MinStorage: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MinSpecCode = None
        self._MinStorage = None
        self._RequestId = None

    @property
    def MinSpecCode(self):
        r"""Code of the minimum specification available for purchase.
        :rtype: str
        """
        return self._MinSpecCode

    @MinSpecCode.setter
    def MinSpecCode(self, MinSpecCode):
        self._MinSpecCode = MinSpecCode

    @property
    def MinStorage(self):
        r"""The minimum disk capacity in GB available for purchase.
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

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
        self._MinSpecCode = params.get("MinSpecCode")
        self._MinStorage = params.get("MinStorage")
        self._RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    r"""DescribeDBBackups request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of postgres-4wdeb0zv.
        :type DBInstanceId: str
        :param _Type: Backup mode (1: full). Currently, only full backup is supported. The value is 1.
        :type Type: int
        :param _StartTime: Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago
        :type StartTime: str
        :param _EndTime: Query end time in the format of 2018-06-10 17:06:38
        :type EndTime: str
        :param _Limit: Number of entries to be returned per page for backup list. Default value: 20. Minimum value: 1. Maximum value: 100. (If this parameter is left empty or 0, the default value will be used)
        :type Limit: int
        :param _Offset: Page number for data return in paged query. Pagination starts from 0. Default value: 0.
        :type Offset: int
        """
        self._DBInstanceId = None
        self._Type = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-4wdeb0zv.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Type(self):
        r"""Backup mode (1: full). Currently, only full backup is supported. The value is 1.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StartTime(self):
        r"""Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Query end time in the format of 2018-06-10 17:06:38
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""Number of entries to be returned per page for backup list. Default value: 20. Minimum value: 1. Maximum value: 100. (If this parameter is left empty or 0, the default value will be used)
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number for data return in paged query. Pagination starts from 0. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBBackupsResponse(AbstractModel):
    r"""DescribeDBBackups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of backup files in the returned backup list
        :type TotalCount: int
        :param _BackupList: Backup list
        :type BackupList: list of DBBackup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of backup files in the returned backup list
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupList(self):
        r"""Backup list
        :rtype: list of DBBackup
        """
        return self._BackupList

    @BackupList.setter
    def BackupList(self, BackupList):
        self._BackupList = BackupList

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
        if params.get("BackupList") is not None:
            self._BackupList = []
            for item in params.get("BackupList"):
                obj = DBBackup()
                obj._deserialize(item)
                self._BackupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBErrlogsRequest(AbstractModel):
    r"""DescribeDBErrlogs request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _StartTime: u200cu200cu200cQuery start time in the format of 2018-01-01 00:00:00. The log is retained for seven days by default, so the start time must fall within the retention period.	
        :type StartTime: str
        :param _EndTime: u200cu200cu200cu200cQuery end time in the format of 2018-01-01 00:00:00	
        :type EndTime: str
        :param _DatabaseName: Database name
        :type DatabaseName: str
        :param _SearchKeys: Keywords used for search
        :type SearchKeys: list of str
        :param _Limit: Number of results returned per page. Value range: 1-100. Default value: `50`.	
        :type Limit: int
        :param _Offset: Data offset, which starts from 0. Default value: `0`.	
        :type Offset: int
        """
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._DatabaseName = None
        self._SearchKeys = None
        self._Limit = None
        self._Offset = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""u200cu200cu200cQuery start time in the format of 2018-01-01 00:00:00. The log is retained for seven days by default, so the start time must fall within the retention period.	
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""u200cu200cu200cu200cQuery end time in the format of 2018-01-01 00:00:00	
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DatabaseName(self):
        r"""Database name
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SearchKeys(self):
        r"""Keywords used for search
        :rtype: list of str
        """
        return self._SearchKeys

    @SearchKeys.setter
    def SearchKeys(self, SearchKeys):
        self._SearchKeys = SearchKeys

    @property
    def Limit(self):
        r"""Number of results returned per page. Value range: 1-100. Default value: `50`.	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, which starts from 0. Default value: `0`.	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DatabaseName = params.get("DatabaseName")
        self._SearchKeys = params.get("SearchKeys")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBErrlogsResponse(AbstractModel):
    r"""DescribeDBErrlogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of logs returned in a single query. Maximum value: `10000`.
        :type TotalCount: int
        :param _Details: Detailed sets of error logs
        :type Details: list of ErrLogDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of logs returned in a single query. Maximum value: `10000`.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        r"""Detailed sets of error logs
        :rtype: list of ErrLogDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

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
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ErrLogDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceAttributeRequest(AbstractModel):
    r"""DescribeDBInstanceAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. can be obtained through the DescribeDBInstances api (https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1).
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. can be obtained through the DescribeDBInstances api (https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceAttributeResponse(AbstractModel):
    r"""DescribeDBInstanceAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _DBInstance: Instance details.
        :type DBInstance: :class:`tencentcloud.postgres.v20170312.models.DBInstance`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DBInstance = None
        self._RequestId = None

    @property
    def DBInstance(self):
        r"""Instance details.
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DBInstance`
        """
        return self._DBInstance

    @DBInstance.setter
    def DBInstance(self, DBInstance):
        self._DBInstance = DBInstance

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
        if params.get("DBInstance") is not None:
            self._DBInstance = DBInstance()
            self._DBInstance._deserialize(params.get("DBInstance"))
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceHAConfigRequest(AbstractModel):
    r"""DescribeDBInstanceHAConfig request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceHAConfigResponse(AbstractModel):
    r"""DescribeDBInstanceHAConfig response structure.

    """

    def __init__(self):
        r"""
        :param _SyncMode: Primary-standby sync mode. Valid values:
<li>`Semi-sync`
<li>`Async`
        :type SyncMode: str
        :param _MaxStandbyLatency: Maximum data lag for high-availability standby server. The standby node can be promoted to the primary node when its data lag and the delay time are both less than the value of `MaxStandbyLatency` and `MaxStandbyLag` respectively.
<li>Unit: byte
<li>Value range: 1073741824-322122547200
        :type MaxStandbyLatency: int
        :param _MaxStandbyLag: The maximum delay for high-availability standby server The standby node can be promoted to the primary node when its data lag and the delay time are both less than or equals to the value of `MaxStandbyLatency` and `MaxStandbyLag` respectively.
<li>Unit: s
<li>Value range: 5-10
        :type MaxStandbyLag: int
        :param _MaxSyncStandbyLatency: Maximum data sync lag for standby server. If data lag of the standby node and the delay time are both less than or equals to the values of `MaxSyncStandbyLatency` and `MaxSyncStandbyLag` respectively, the standby server adopts semi-sync replication; if not, it adopts async replication.
This value is only valid for the instance with `SyncMode` set to `Semi-sync`.
This field returns null for async instance
and semi-sync (non-downgradable to async) instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxSyncStandbyLatency: int
        :param _MaxSyncStandbyLag: Maximum sync delay time for standby server. If the delay time for standby server and the data lag are both less than or equals to the values of `MaxSyncStandbyLag` and `MaxSyncStandbyLatency` respectively, the standby server adopts sync replication mode; if not, it adopts async replication.
This value is only valid for the instance with `SyncMode` set to `Semi-sync`.
This field will not return for async instance
and semi-sync (non-downgradable to async) instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxSyncStandbyLag: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SyncMode = None
        self._MaxStandbyLatency = None
        self._MaxStandbyLag = None
        self._MaxSyncStandbyLatency = None
        self._MaxSyncStandbyLag = None
        self._RequestId = None

    @property
    def SyncMode(self):
        r"""Primary-standby sync mode. Valid values:
<li>`Semi-sync`
<li>`Async`
        :rtype: str
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def MaxStandbyLatency(self):
        r"""Maximum data lag for high-availability standby server. The standby node can be promoted to the primary node when its data lag and the delay time are both less than the value of `MaxStandbyLatency` and `MaxStandbyLag` respectively.
<li>Unit: byte
<li>Value range: 1073741824-322122547200
        :rtype: int
        """
        return self._MaxStandbyLatency

    @MaxStandbyLatency.setter
    def MaxStandbyLatency(self, MaxStandbyLatency):
        self._MaxStandbyLatency = MaxStandbyLatency

    @property
    def MaxStandbyLag(self):
        r"""The maximum delay for high-availability standby server The standby node can be promoted to the primary node when its data lag and the delay time are both less than or equals to the value of `MaxStandbyLatency` and `MaxStandbyLag` respectively.
<li>Unit: s
<li>Value range: 5-10
        :rtype: int
        """
        return self._MaxStandbyLag

    @MaxStandbyLag.setter
    def MaxStandbyLag(self, MaxStandbyLag):
        self._MaxStandbyLag = MaxStandbyLag

    @property
    def MaxSyncStandbyLatency(self):
        r"""Maximum data sync lag for standby server. If data lag of the standby node and the delay time are both less than or equals to the values of `MaxSyncStandbyLatency` and `MaxSyncStandbyLag` respectively, the standby server adopts semi-sync replication; if not, it adopts async replication.
This value is only valid for the instance with `SyncMode` set to `Semi-sync`.
This field returns null for async instance
and semi-sync (non-downgradable to async) instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxSyncStandbyLatency

    @MaxSyncStandbyLatency.setter
    def MaxSyncStandbyLatency(self, MaxSyncStandbyLatency):
        self._MaxSyncStandbyLatency = MaxSyncStandbyLatency

    @property
    def MaxSyncStandbyLag(self):
        r"""Maximum sync delay time for standby server. If the delay time for standby server and the data lag are both less than or equals to the values of `MaxSyncStandbyLag` and `MaxSyncStandbyLatency` respectively, the standby server adopts sync replication mode; if not, it adopts async replication.
This value is only valid for the instance with `SyncMode` set to `Semi-sync`.
This field will not return for async instance
and semi-sync (non-downgradable to async) instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxSyncStandbyLag

    @MaxSyncStandbyLag.setter
    def MaxSyncStandbyLag(self, MaxSyncStandbyLag):
        self._MaxSyncStandbyLag = MaxSyncStandbyLag

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
        self._SyncMode = params.get("SyncMode")
        self._MaxStandbyLatency = params.get("MaxStandbyLatency")
        self._MaxStandbyLag = params.get("MaxStandbyLag")
        self._MaxSyncStandbyLatency = params.get("MaxSyncStandbyLatency")
        self._MaxSyncStandbyLag = params.get("MaxSyncStandbyLag")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceParametersRequest(AbstractModel):
    r"""DescribeDBInstanceParameters request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _ParamName: Name of the parameter to be queried. If `ParamName` is left empty or not passed in, the list of all parameters will be returned.
        :type ParamName: str
        """
        self._DBInstanceId = None
        self._ParamName = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ParamName(self):
        r"""Name of the parameter to be queried. If `ParamName` is left empty or not passed in, the list of all parameters will be returned.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ParamName = params.get("ParamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceParametersResponse(AbstractModel):
    r"""DescribeDBInstanceParameters response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of the parameters in the returned list
        :type TotalCount: int
        :param _Detail: Details of the returned parameter list
        :type Detail: list of ParamInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Detail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of the parameters in the returned list
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Detail(self):
        r"""Details of the returned parameter list
        :rtype: list of ParamInfo
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceSSLConfigRequest(AbstractModel):
    r"""DescribeDBInstanceSSLConfig request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Specifies the instance ID, such as postgres-6bwgamo3. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Specifies the instance ID, such as postgres-6bwgamo3. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceSSLConfigResponse(AbstractModel):
    r"""DescribeDBInstanceSSLConfig response structure.

    """

    def __init__(self):
        r"""
        :param _SSLEnabled: true represents enabled. false represents not enabled.
        :type SSLEnabled: bool
        :param _CAUrl: Certificate download url for the cloud root certificate.
        :type CAUrl: str
        :param _ConnectAddress: Specifies the intranet or public network connection address in the server certificate.
        :type ConnectAddress: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SSLEnabled = None
        self._CAUrl = None
        self._ConnectAddress = None
        self._RequestId = None

    @property
    def SSLEnabled(self):
        r"""true represents enabled. false represents not enabled.
        :rtype: bool
        """
        return self._SSLEnabled

    @SSLEnabled.setter
    def SSLEnabled(self, SSLEnabled):
        self._SSLEnabled = SSLEnabled

    @property
    def CAUrl(self):
        r"""Certificate download url for the cloud root certificate.
        :rtype: str
        """
        return self._CAUrl

    @CAUrl.setter
    def CAUrl(self, CAUrl):
        self._CAUrl = CAUrl

    @property
    def ConnectAddress(self):
        r"""Specifies the intranet or public network connection address in the server certificate.
        :rtype: str
        """
        return self._ConnectAddress

    @ConnectAddress.setter
    def ConnectAddress(self, ConnectAddress):
        self._ConnectAddress = ConnectAddress

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
        self._SSLEnabled = params.get("SSLEnabled")
        self._CAUrl = params.get("CAUrl")
        self._ConnectAddress = params.get("ConnectAddress")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceSecurityGroupsRequest(AbstractModel):
    r"""DescribeDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en). specify either DBInstanceId or ReadOnlyGroupId. if both are provided, ReadOnlyGroupId is ignored.
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: ReadOnlyGroupId. specifies the read-only group ID, which can be obtained through the api [DescribeReadOnlyGroups](https://www.tencentcloud.com/document/product/409/39725?lang=en). valid values: DBInstanceId and ReadOnlyGroupId (at least one is required). if you need to query the associated security group of the read-only group, only ReadOnlyGroupId is required.
        :type ReadOnlyGroupId: str
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en). specify either DBInstanceId or ReadOnlyGroupId. if both are provided, ReadOnlyGroupId is ignored.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""ReadOnlyGroupId. specifies the read-only group ID, which can be obtained through the api [DescribeReadOnlyGroups](https://www.tencentcloud.com/document/product/409/39725?lang=en). valid values: DBInstanceId and ReadOnlyGroupId (at least one is required). if you need to query the associated security group of the read-only group, only ReadOnlyGroupId is required.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceSecurityGroupsResponse(AbstractModel):
    r"""DescribeDBInstanceSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupSet: Information of security groups in array
        :type SecurityGroupSet: list of SecurityGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityGroupSet = None
        self._RequestId = None

    @property
    def SecurityGroupSet(self):
        r"""Information of security groups in array
        :rtype: list of SecurityGroup
        """
        return self._SecurityGroupSet

    @SecurityGroupSet.setter
    def SecurityGroupSet(self, SecurityGroupSet):
        self._SecurityGroupSet = SecurityGroupSet

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
        if params.get("SecurityGroupSet") is not None:
            self._SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._SecurityGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    r"""DescribeDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Query using one or more filter criteria. Filter criteria currently supported include:
db-instance-id: filter by instance ID (in string format)
db-instance-name: filter by instance name (in string format)
db-project-id: filter by project ID (in string format)
db-pay-mode: filter by instance billing mode (in string format)
db-tag-key: filter by tag key (in string format)
db-private-ip: filter by instance VPC IP (in string format)
db-public-address: filter by instance public network address (in string format)
        :type Filters: list of Filter
        :param _Limit: The maximum number of results returned per page. Value range: 1-100. Default: `10`.
        :type Limit: int
        :param _Offset: Data offset, which starts from 0.
        :type Offset: int
        :param _OrderBy: Sorting metric, such as instance name or creation time. Valid values: DBInstanceId, CreateTime, Name, EndTime.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: `asc` (ascending), `desc` (descending)
        :type OrderByType: str
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Filters(self):
        r"""Query using one or more filter criteria. Filter criteria currently supported include:
db-instance-id: filter by instance ID (in string format)
db-instance-name: filter by instance name (in string format)
db-project-id: filter by project ID (in string format)
db-pay-mode: filter by instance billing mode (in string format)
db-tag-key: filter by tag key (in string format)
db-private-ip: filter by instance VPC IP (in string format)
db-public-address: filter by instance public network address (in string format)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""The maximum number of results returned per page. Value range: 1-100. Default: `10`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, which starts from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sorting metric, such as instance name or creation time. Valid values: DBInstanceId, CreateTime, Name, EndTime.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order. Valid values: `asc` (ascending), `desc` (descending)
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
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
        :param _TotalCount: Number of instances found.
        :type TotalCount: int
        :param _DBInstanceSet: Instance details set.
        :type DBInstanceSet: list of DBInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of instances found.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstanceSet(self):
        r"""Instance details set.
        :rtype: list of DBInstance
        """
        return self._DBInstanceSet

    @DBInstanceSet.setter
    def DBInstanceSet(self, DBInstanceSet):
        self._DBInstanceSet = DBInstanceSet

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
        if params.get("DBInstanceSet") is not None:
            self._DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = DBInstance()
                obj._deserialize(item)
                self._DBInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSlowlogsRequest(AbstractModel):
    r"""DescribeDBSlowlogs request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of postgres-lnp6j617
        :type DBInstanceId: str
        :param _StartTime: Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago
        :type StartTime: str
        :param _EndTime: Query end time in the format of 2018-06-10 17:06:38
        :type EndTime: str
        :param _DatabaseName: Database name
        :type DatabaseName: str
        :param _OrderBy: Metric for sorting. Valid values: `sum_calls` (total number of calls), `sum_cost_time` (total time consumed)
        :type OrderBy: str
        :param _OrderByType: Sorting order. desc: descending, asc: ascending
        :type OrderByType: str
        :param _Limit: Number of entries returned per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        :param _Offset: Page number for data return in paged query. Pagination starts from 0
        :type Offset: int
        """
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._DatabaseName = None
        self._OrderBy = None
        self._OrderByType = None
        self._Limit = None
        self._Offset = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-lnp6j617
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Query end time in the format of 2018-06-10 17:06:38
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DatabaseName(self):
        r"""Database name
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def OrderBy(self):
        r"""Metric for sorting. Valid values: `sum_calls` (total number of calls), `sum_cost_time` (total time consumed)
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order. desc: descending, asc: ascending
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Limit(self):
        r"""Number of entries returned per page. Value range: 1-100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number for data return in paged query. Pagination starts from 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DatabaseName = params.get("DatabaseName")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSlowlogsResponse(AbstractModel):
    r"""DescribeDBSlowlogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of date entries returned this time
        :type TotalCount: int
        :param _Detail: Slow query log details
        :type Detail: :class:`tencentcloud.postgres.v20170312.models.SlowlogDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Detail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of date entries returned this time
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Detail(self):
        r"""Slow query log details
        :rtype: :class:`tencentcloud.postgres.v20170312.models.SlowlogDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        if params.get("Detail") is not None:
            self._Detail = SlowlogDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeDBVersionsRequest(AbstractModel):
    r"""DescribeDBVersions request structure.

    """


class DescribeDBVersionsResponse(AbstractModel):
    r"""DescribeDBVersions response structure.

    """

    def __init__(self):
        r"""
        :param _VersionSet: List of database versions
        :type VersionSet: list of Version
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VersionSet = None
        self._RequestId = None

    @property
    def VersionSet(self):
        r"""List of database versions
        :rtype: list of Version
        """
        return self._VersionSet

    @VersionSet.setter
    def VersionSet(self, VersionSet):
        self._VersionSet = VersionSet

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
        if params.get("VersionSet") is not None:
            self._VersionSet = []
            for item in params.get("VersionSet"):
                obj = Version()
                obj._deserialize(item)
                self._VersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBXlogsRequest(AbstractModel):
    r"""DescribeDBXlogs request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of postgres-4wdeb0zv.
        :type DBInstanceId: str
        :param _StartTime: Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago
        :type StartTime: str
        :param _EndTime: Query end time in the format of 2018-06-10 17:06:38
        :type EndTime: str
        :param _Offset: Page number for data return in paged query. Pagination starts from 0
        :type Offset: int
        :param _Limit: Number of entries returned per page in paged query. Value range: 1-100.
        :type Limit: int
        """
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-4wdeb0zv.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Query end time in the format of 2018-06-10 17:06:38
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""Page number for data return in paged query. Pagination starts from 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries returned per page in paged query. Value range: 1-100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBXlogsResponse(AbstractModel):
    r"""DescribeDBXlogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of date entries returned this time.
        :type TotalCount: int
        :param _XlogList: Xlog list
        :type XlogList: list of Xlog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._XlogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of date entries returned this time.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def XlogList(self):
        r"""Xlog list
        :rtype: list of Xlog
        """
        return self._XlogList

    @XlogList.setter
    def XlogList(self, XlogList):
        self._XlogList = XlogList

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
        if params.get("XlogList") is not None:
            self._XlogList = []
            for item in params.get("XlogList"):
                obj = Xlog()
                obj._deserialize(item)
                self._XlogList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    r"""DescribeDatabaseObjects request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :type DBInstanceId: str
        :param _ObjectType: Specifies the object type for querying. supported objects: database, schema, sequence, procedure, type, function, table, view, matview, column.
        :type ObjectType: str
        :param _Limit: Number of items displayed at a time. default 20. value range 0-100.
        :type Limit: int
        :param _Offset: Data offset, starting from 0.		
        :type Offset: int
        :param _DatabaseName: Describes the database the query object belongs to. this parameter is required when the query object type is not database.
        :type DatabaseName: str
        :param _SchemaName: Specifies the mode belonging to the query object. this parameter is required when the query object type is not database or schema.
        :type SchemaName: str
        :param _TableName: Specifies the table belonging to the query object. this parameter is required when the query object type is column.
        :type TableName: str
        """
        self._DBInstanceId = None
        self._ObjectType = None
        self._Limit = None
        self._Offset = None
        self._DatabaseName = None
        self._SchemaName = None
        self._TableName = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ObjectType(self):
        r"""Specifies the object type for querying. supported objects: database, schema, sequence, procedure, type, function, table, view, matview, column.
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def Limit(self):
        r"""Number of items displayed at a time. default 20. value range 0-100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, starting from 0.		
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DatabaseName(self):
        r"""Describes the database the query object belongs to. this parameter is required when the query object type is not database.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SchemaName(self):
        r"""Specifies the mode belonging to the query object. this parameter is required when the query object type is not database or schema.
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TableName(self):
        r"""Specifies the table belonging to the query object. this parameter is required when the query object type is column.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ObjectType = params.get("ObjectType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DatabaseName = params.get("DatabaseName")
        self._SchemaName = params.get("SchemaName")
        self._TableName = params.get("TableName")
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
        :param _ObjectSet: Query object list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectSet: list of str
        :param _TotalCount: Specifies the total number of objects.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ObjectSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ObjectSet(self):
        r"""Query object list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ObjectSet

    @ObjectSet.setter
    def ObjectSet(self, ObjectSet):
        self._ObjectSet = ObjectSet

    @property
    def TotalCount(self):
        r"""Specifies the total number of objects.
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
        self._ObjectSet = params.get("ObjectSet")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    r"""DescribeDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the API [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?from_cn_redirect=1).
        :type DBInstanceId: str
        :param _Filters: Query using one or more filter criteria. Filter criteria currently supported include: database-name: filter by database name (in string format). Fuzzy matching is used to search for databases that meet the criteria.
        :type Filters: list of Filter
        :param _Offset: Data offset, which starts from 0.
        :type Offset: int
        :param _Limit: Number of items displayed at a time. the maximum value is recommended to be 100.
Default value: 20.
        :type Limit: int
        """
        self._DBInstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the API [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Filters(self):
        r"""Query using one or more filter criteria. Filter criteria currently supported include: database-name: filter by database name (in string format). Fuzzy matching is used to search for databases that meet the criteria.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""Data offset, which starts from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of items displayed at a time. the maximum value is recommended to be 100.
Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        :param _Items: Database information
        :type Items: list of str
        :param _TotalCount: Total number of databases
        :type TotalCount: int
        :param _Databases: Specifies the database details list.
        :type Databases: list of Database
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._Databases = None
        self._RequestId = None

    @property
    def Items(self):
        r"""Database information
        :rtype: list of str
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""Total number of databases
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Databases(self):
        r"""Specifies the database details list.
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

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
        self._Items = params.get("Items")
        self._TotalCount = params.get("TotalCount")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClustersRequest(AbstractModel):
    r"""DescribeDedicatedClusters request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Query using one or more filter criteria. filter criteria currently supported include:.
dedicated-cluster-id: filters by dedicated cluster id. string type.
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        r"""Query using one or more filter criteria. filter criteria currently supported include:.
dedicated-cluster-id: filters by dedicated cluster id. string type.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeDedicatedClustersResponse(AbstractModel):
    r"""DescribeDedicatedClusters response structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterSet: Exclusive cluster information.
        :type DedicatedClusterSet: list of DedicatedCluster
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DedicatedClusterSet = None
        self._RequestId = None

    @property
    def DedicatedClusterSet(self):
        r"""Exclusive cluster information.
        :rtype: list of DedicatedCluster
        """
        return self._DedicatedClusterSet

    @DedicatedClusterSet.setter
    def DedicatedClusterSet(self, DedicatedClusterSet):
        self._DedicatedClusterSet = DedicatedClusterSet

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
        if params.get("DedicatedClusterSet") is not None:
            self._DedicatedClusterSet = []
            for item in params.get("DedicatedClusterSet"):
                obj = DedicatedCluster()
                obj._deserialize(item)
                self._DedicatedClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDefaultParametersRequest(AbstractModel):
    r"""DescribeDefaultParameters request structure.

    """

    def __init__(self):
        r"""
        :param _DBMajorVersion: The major database version number, such as 11, 12, 13.
        :type DBMajorVersion: str
        :param _DBEngine: Database engine, such as postgresql, mssql_compatible.
        :type DBEngine: str
        """
        self._DBMajorVersion = None
        self._DBEngine = None

    @property
    def DBMajorVersion(self):
        r"""The major database version number, such as 11, 12, 13.
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBEngine(self):
        r"""Database engine, such as postgresql, mssql_compatible.
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine


    def _deserialize(self, params):
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBEngine = params.get("DBEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultParametersResponse(AbstractModel):
    r"""DescribeDefaultParameters response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of parameters
        :type TotalCount: int
        :param _ParamInfoSet: Parameter information
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParamInfoSet: list of ParamInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ParamInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of parameters
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ParamInfoSet(self):
        r"""Parameter information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ParamInfo
        """
        return self._ParamInfoSet

    @ParamInfoSet.setter
    def ParamInfoSet(self, ParamInfoSet):
        self._ParamInfoSet = ParamInfoSet

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
        if params.get("ParamInfoSet") is not None:
            self._ParamInfoSet = []
            for item in params.get("ParamInfoSet"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEncryptionKeysRequest(AbstractModel):
    r"""DescribeEncryptionKeys request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEncryptionKeysResponse(AbstractModel):
    r"""DescribeEncryptionKeys response structure.

    """

    def __init__(self):
        r"""
        :param _EncryptionKeys: Specifies the key information list of the instance.
        :type EncryptionKeys: list of EncryptionKey
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EncryptionKeys = None
        self._RequestId = None

    @property
    def EncryptionKeys(self):
        r"""Specifies the key information list of the instance.
        :rtype: list of EncryptionKey
        """
        return self._EncryptionKeys

    @EncryptionKeys.setter
    def EncryptionKeys(self, EncryptionKeys):
        self._EncryptionKeys = EncryptionKeys

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
        if params.get("EncryptionKeys") is not None:
            self._EncryptionKeys = []
            for item in params.get("EncryptionKeys"):
                obj = EncryptionKey()
                obj._deserialize(item)
                self._EncryptionKeys.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogBackupsRequest(AbstractModel):
    r"""DescribeLogBackups request structure.

    """

    def __init__(self):
        r"""
        :param _MinFinishTime: Minimum end time of a backup in the format of `2018-01-01 00:00:00`. It is 7 days ago by default.
        :type MinFinishTime: str
        :param _MaxFinishTime: Maximum end time of a backup in the format of `2018-01-01 00:00:00`. It is the current time by default.
        :type MaxFinishTime: str
        :param _Filters: Filter instances using one or more criteria. Valid filter names:
db-instance-id: Filter by instance ID (in string format).
db-instance-name: Filter by instance name (in string format).
db-instance-ip: Filter by instance VPC IP (in string format).
        :type Filters: list of Filter
        :param _Limit: The maximum number of results returned per page. Value range: 1-100. Default: `10`.
        :type Limit: int
        :param _Offset: Data offset, which starts from 0.
        :type Offset: int
        :param _OrderBy: Sorting field. Valid values: `StartTime`, `FinishTime`, `Size`.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: `asc` (ascending), `desc` (descending).
        :type OrderByType: str
        """
        self._MinFinishTime = None
        self._MaxFinishTime = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def MinFinishTime(self):
        r"""Minimum end time of a backup in the format of `2018-01-01 00:00:00`. It is 7 days ago by default.
        :rtype: str
        """
        return self._MinFinishTime

    @MinFinishTime.setter
    def MinFinishTime(self, MinFinishTime):
        self._MinFinishTime = MinFinishTime

    @property
    def MaxFinishTime(self):
        r"""Maximum end time of a backup in the format of `2018-01-01 00:00:00`. It is the current time by default.
        :rtype: str
        """
        return self._MaxFinishTime

    @MaxFinishTime.setter
    def MaxFinishTime(self, MaxFinishTime):
        self._MaxFinishTime = MaxFinishTime

    @property
    def Filters(self):
        r"""Filter instances using one or more criteria. Valid filter names:
db-instance-id: Filter by instance ID (in string format).
db-instance-name: Filter by instance name (in string format).
db-instance-ip: Filter by instance VPC IP (in string format).
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""The maximum number of results returned per page. Value range: 1-100. Default: `10`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, which starts from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sorting field. Valid values: `StartTime`, `FinishTime`, `Size`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order. Valid values: `asc` (ascending), `desc` (descending).
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._MinFinishTime = params.get("MinFinishTime")
        self._MaxFinishTime = params.get("MaxFinishTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogBackupsResponse(AbstractModel):
    r"""DescribeLogBackups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of queried log backups
        :type TotalCount: int
        :param _LogBackupSet: List of log backup details
        :type LogBackupSet: list of LogBackup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LogBackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of queried log backups
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LogBackupSet(self):
        r"""List of log backup details
        :rtype: list of LogBackup
        """
        return self._LogBackupSet

    @LogBackupSet.setter
    def LogBackupSet(self, LogBackupSet):
        self._LogBackupSet = LogBackupSet

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
        if params.get("LogBackupSet") is not None:
            self._LogBackupSet = []
            for item in params.get("LogBackupSet"):
                obj = LogBackup()
                obj._deserialize(item)
                self._LogBackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMaintainTimeWindowRequest(AbstractModel):
    r"""DescribeMaintainTimeWindow request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaintainTimeWindowResponse(AbstractModel):
    r"""DescribeMaintainTimeWindow response structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _MaintainStartTime: Maintenance start time. time zone is UTC+8.
        :type MaintainStartTime: str
        :param _MaintainDuration: Maintenance duration. unit: hr.
        :type MaintainDuration: int
        :param _MaintainWeekDays: Specifies the maintenance period.
        :type MaintainWeekDays: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DBInstanceId = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._MaintainWeekDays = None
        self._RequestId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def MaintainStartTime(self):
        r"""Maintenance start time. time zone is UTC+8.
        :rtype: str
        """
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        r"""Maintenance duration. unit: hr.
        :rtype: int
        """
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        r"""Specifies the maintenance period.
        :rtype: list of str
        """
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays

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
        self._DBInstanceId = params.get("DBInstanceId")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        self._RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    r"""DescribeOrders request structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order name set
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        r"""Order name set
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    r"""DescribeOrders response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of orders
        :type TotalCount: int
        :param _Deals: Order array
        :type Deals: list of PgDeal
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Deals = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of orders
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Deals(self):
        r"""Order array
        :rtype: list of PgDeal
        """
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

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
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = PgDeal()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeParameterTemplateAttributesRequest(AbstractModel):
    r"""DescribeParameterTemplateAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""Parameter template ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParameterTemplateAttributesResponse(AbstractModel):
    r"""DescribeParameterTemplateAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateId: str
        :param _TotalCount: Number of parameters contained in the parameter template
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ParamInfoSet: Parameter information contained in the parameter template
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParamInfoSet: list of ParamInfo
        :param _TemplateName: Parameter template name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateName: str
        :param _DBMajorVersion: Database version applicable to a parameter template
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBMajorVersion: str
        :param _DBEngine: Database engine applicable to a parameter template
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBEngine: str
        :param _TemplateDescription: Parameter template description
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateDescription: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._TotalCount = None
        self._ParamInfoSet = None
        self._TemplateName = None
        self._DBMajorVersion = None
        self._DBEngine = None
        self._TemplateDescription = None
        self._RequestId = None

    @property
    def TemplateId(self):
        r"""Parameter template ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TotalCount(self):
        r"""Number of parameters contained in the parameter template
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ParamInfoSet(self):
        r"""Parameter information contained in the parameter template
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ParamInfo
        """
        return self._ParamInfoSet

    @ParamInfoSet.setter
    def ParamInfoSet(self, ParamInfoSet):
        self._ParamInfoSet = ParamInfoSet

    @property
    def TemplateName(self):
        r"""Parameter template name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def DBMajorVersion(self):
        r"""Database version applicable to a parameter template
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBEngine(self):
        r"""Database engine applicable to a parameter template
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def TemplateDescription(self):
        r"""Parameter template description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

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
        self._TemplateId = params.get("TemplateId")
        self._TotalCount = params.get("TotalCount")
        if params.get("ParamInfoSet") is not None:
            self._ParamInfoSet = []
            for item in params.get("ParamInfoSet"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamInfoSet.append(obj)
        self._TemplateName = params.get("TemplateName")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBEngine = params.get("DBEngine")
        self._TemplateDescription = params.get("TemplateDescription")
        self._RequestId = params.get("RequestId")


class DescribeParameterTemplatesRequest(AbstractModel):
    r"""DescribeParameterTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter conditions. Valid values: `TemplateName`, `TemplateId`, `DBMajorVersion`, `DBEngine`.
        :type Filters: list of Filter
        :param _Limit: The maximum number of results returned per page. Value range: 0-100. Default: `20`.
        :type Limit: int
        :param _Offset: Data offset
        :type Offset: int
        :param _OrderBy: Sorting metric. Valid values: `CreateTime`, `TemplateName`, `DBMajorVersion`.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: `asc` (ascending order),`desc` (descending order).
        :type OrderByType: str
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Filters(self):
        r"""Filter conditions. Valid values: `TemplateName`, `TemplateId`, `DBMajorVersion`, `DBEngine`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""The maximum number of results returned per page. Value range: 0-100. Default: `20`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sorting metric. Valid values: `CreateTime`, `TemplateName`, `DBMajorVersion`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order. Valid values: `asc` (ascending order),`desc` (descending order).
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParameterTemplatesResponse(AbstractModel):
    r"""DescribeParameterTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of eligible parameter templates
        :type TotalCount: int
        :param _ParameterTemplateSet: Parameter template list
        :type ParameterTemplateSet: list of ParameterTemplate
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ParameterTemplateSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""The total number of eligible parameter templates
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ParameterTemplateSet(self):
        r"""Parameter template list
        :rtype: list of ParameterTemplate
        """
        return self._ParameterTemplateSet

    @ParameterTemplateSet.setter
    def ParameterTemplateSet(self, ParameterTemplateSet):
        self._ParameterTemplateSet = ParameterTemplateSet

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
        if params.get("ParameterTemplateSet") is not None:
            self._ParameterTemplateSet = []
            for item in params.get("ParameterTemplateSet"):
                obj = ParameterTemplate()
                obj._deserialize(item)
                self._ParameterTemplateSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeParamsEventRequest(AbstractModel):
    r"""DescribeParamsEvent request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamsEventResponse(AbstractModel):
    r"""DescribeParamsEvent response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of modified parameters
        :type TotalCount: int
        :param _EventItems: Details of parameter modification events
        :type EventItems: list of EventItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._EventItems = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of modified parameters
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EventItems(self):
        r"""Details of parameter modification events
        :rtype: list of EventItem
        """
        return self._EventItems

    @EventItems.setter
    def EventItems(self, EventItems):
        self._EventItems = EventItems

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
        if params.get("EventItems") is not None:
            self._EventItems = []
            for item in params.get("EventItems"):
                obj = EventItem()
                obj._deserialize(item)
                self._EventItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    r"""DescribeProductConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ name
        :type Zone: str
        :param _DBEngine: Database engines. Valid values:
1. `postgresql` (TencentDB for PostgreSQL)
2. `mssql_compatible` (MSSQL compatible-TencentDB for PostgreSQL)
Default value: `postgresql`
        :type DBEngine: str
        """
        self._Zone = None
        self._DBEngine = None

    @property
    def Zone(self):
        r"""AZ name
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DBEngine(self):
        r"""Database engines. Valid values:
1. `postgresql` (TencentDB for PostgreSQL)
2. `mssql_compatible` (MSSQL compatible-TencentDB for PostgreSQL)
Default value: `postgresql`
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DBEngine = params.get("DBEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductConfigResponse(AbstractModel):
    r"""DescribeProductConfig response structure.

    """

    def __init__(self):
        r"""
        :param _SpecInfoList: Purchasable specification list.
        :type SpecInfoList: list of SpecInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SpecInfoList = None
        self._RequestId = None

    @property
    def SpecInfoList(self):
        r"""Purchasable specification list.
        :rtype: list of SpecInfo
        """
        return self._SpecInfoList

    @SpecInfoList.setter
    def SpecInfoList(self, SpecInfoList):
        self._SpecInfoList = SpecInfoList

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
        if params.get("SpecInfoList") is not None:
            self._SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self._SpecInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupsRequest(AbstractModel):
    r"""DescribeReadOnlyGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter instances by using one or more filters. Valid values:  `db-master-instance-id` (filter by the primary instance ID in string), `read-only-group-id` (filter by the read-only group ID in string),
        :type Filters: list of Filter
        :param _PageSize: The number of results per page. Default value: 10.
        :type PageSize: int
        :param _PageNumber: Specify which page is displayed. Default value: 1 (the first page).
        :type PageNumber: int
        :param _OrderBy: Sorting criterion. Valid values: `ROGroupId`, `CreateTime`, `Name`.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: `desc`, `asc`.
        :type OrderByType: str
        """
        self._Filters = None
        self._PageSize = None
        self._PageNumber = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Filters(self):
        r"""Filter instances by using one or more filters. Valid values:  `db-master-instance-id` (filter by the primary instance ID in string), `read-only-group-id` (filter by the read-only group ID in string),
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def PageSize(self):
        r"""The number of results per page. Default value: 10.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""Specify which page is displayed. Default value: 1 (the first page).
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def OrderBy(self):
        r"""Sorting criterion. Valid values: `ROGroupId`, `CreateTime`, `Name`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order. Valid values: `desc`, `asc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupsResponse(AbstractModel):
    r"""DescribeReadOnlyGroups response structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupList: RO group list
        :type ReadOnlyGroupList: list of ReadOnlyGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReadOnlyGroupList = None
        self._RequestId = None

    @property
    def ReadOnlyGroupList(self):
        r"""RO group list
        :rtype: list of ReadOnlyGroup
        """
        return self._ReadOnlyGroupList

    @ReadOnlyGroupList.setter
    def ReadOnlyGroupList(self, ReadOnlyGroupList):
        self._ReadOnlyGroupList = ReadOnlyGroupList

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
        if params.get("ReadOnlyGroupList") is not None:
            self._ReadOnlyGroupList = []
            for item in params.get("ReadOnlyGroupList"):
                obj = ReadOnlyGroup()
                obj._deserialize(item)
                self._ReadOnlyGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    r"""DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    r"""DescribeRegions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of returned results.
        :type TotalCount: int
        :param _RegionSet: Region information set.
        :type RegionSet: list of RegionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of returned results.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        r"""Region information set.
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

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
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServerlessDBInstancesRequest(AbstractModel):
    r"""DescribeServerlessDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Query criteria. Query using one or more filter criteria. Filter criteria type (specified by the name field) currently supported include: 

- db-instance-id: filter by instance ID (in string format)
- db-instance-name: filter by instance name (in string format)
- db-tag-key: filter by instance tag (in string format)

The value field specifies the specific instance ID/instance name/instance tag-key to filter under this type of filter criteria.
        :type Filter: list of Filter
        :param _Limit: The number of queries
        :type Limit: int
        :param _Offset: The offset value
        :type Offset: int
        :param _OrderBy: Sorting metric. Currently, only "CreateTime" (instance creation time) is supported.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Ascending and descending are supported.
        :type OrderByType: str
        """
        self._Filter = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Filter(self):
        r"""Query criteria. Query using one or more filter criteria. Filter criteria type (specified by the name field) currently supported include: 

- db-instance-id: filter by instance ID (in string format)
- db-instance-name: filter by instance name (in string format)
- db-tag-key: filter by instance tag (in string format)

The value field specifies the specific instance ID/instance name/instance tag-key to filter under this type of filter criteria.
        :rtype: list of Filter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Limit(self):
        r"""The number of queries
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""The offset value
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sorting metric. Currently, only "CreateTime" (instance creation time) is supported.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order. Ascending and descending are supported.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessDBInstancesResponse(AbstractModel):
    r"""DescribeServerlessDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of query results
        :type TotalCount: int
        :param _DBInstanceSet: Query results
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBInstanceSet: list of ServerlessDBInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""The number of query results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstanceSet(self):
        r"""Query results
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of ServerlessDBInstance
        """
        return self._DBInstanceSet

    @DBInstanceSet.setter
    def DBInstanceSet(self, DBInstanceSet):
        self._DBInstanceSet = DBInstanceSet

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
        if params.get("DBInstanceSet") is not None:
            self._DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = ServerlessDBInstance()
                obj._deserialize(item)
                self._DBInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryAnalysisRequest(AbstractModel):
    r"""DescribeSlowQueryAnalysis request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID.
        :type DBInstanceId: str
        :param _StartTime: Query start time, in the format of 2018-01-01 00:00:00. The log is retained for seven days by default, so the start time must fall within the retention period.
        :type StartTime: str
        :param _EndTime: Query end time, in the format of 2018-01-01 00:00:00.
        :type EndTime: str
        :param _DatabaseName: Database name
        :type DatabaseName: str
        :param _OrderBy: Sorting field, with valid values `[CallNum, CostTime, AvgCostTime]`. The default value is `CallNum`.
        :type OrderBy: str
        :param _OrderByType: Sorting method, including ascending: `asc` and descending: `desc`. The default value is `desc`.
        :type OrderByType: str
        :param _Limit: Number of results returned per page, with a value range of 1-100. The default value is `50`.
        :type Limit: int
        :param _Offset: Data offset, which starts from 0. The default value is `0`.
        :type Offset: int
        """
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._DatabaseName = None
        self._OrderBy = None
        self._OrderByType = None
        self._Limit = None
        self._Offset = None

    @property
    def DBInstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""Query start time, in the format of 2018-01-01 00:00:00. The log is retained for seven days by default, so the start time must fall within the retention period.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Query end time, in the format of 2018-01-01 00:00:00.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DatabaseName(self):
        r"""Database name
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def OrderBy(self):
        r"""Sorting field, with valid values `[CallNum, CostTime, AvgCostTime]`. The default value is `CallNum`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting method, including ascending: `asc` and descending: `desc`. The default value is `desc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Limit(self):
        r"""Number of results returned per page, with a value range of 1-100. The default value is `50`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, which starts from 0. The default value is `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DatabaseName = params.get("DatabaseName")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryAnalysisResponse(AbstractModel):
    r"""DescribeSlowQueryAnalysis response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number found, with a maximum of 10,000 entries.
        :type TotalCount: int
        :param _Detail: Collection of detailed information on slow SQL statistical analysis found.
        :type Detail: :class:`tencentcloud.postgres.v20170312.models.Detail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Detail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number found, with a maximum of 10,000 entries.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Detail(self):
        r"""Collection of detailed information on slow SQL statistical analysis found.
        :rtype: :class:`tencentcloud.postgres.v20170312.models.Detail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        if params.get("Detail") is not None:
            self._Detail = Detail()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryListRequest(AbstractModel):
    r"""DescribeSlowQueryList request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID.
        :type DBInstanceId: str
        :param _StartTime: Query start time, in the format of 2018-01-01 00:00:00. The log is retained for seven days by default, so the start time must fall within the retention period.
        :type StartTime: str
        :param _EndTime: Query end time, in the format of 2018-01-01 00:00:00.
        :type EndTime: str
        :param _DatabaseName: Database name.
        :type DatabaseName: str
        :param _OrderByType: Sorting method, including ascending: `asc` and descending: `desc`. The default value is `desc`.	
        :type OrderByType: str
        :param _OrderBy: Sorting field, with a value range of `[SessionStartTime, Duration]`. The default value is `SessionStartTime`.
        :type OrderBy: str
        :param _Limit: Number of results returned per page, with a value range of 1-100. The default value is `50`.
        :type Limit: int
        :param _Offset: Data offset, which starts from 0. The default value is `0`.
        :type Offset: int
        """
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._DatabaseName = None
        self._OrderByType = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None

    @property
    def DBInstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""Query start time, in the format of 2018-01-01 00:00:00. The log is retained for seven days by default, so the start time must fall within the retention period.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Query end time, in the format of 2018-01-01 00:00:00.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
    def OrderByType(self):
        r"""Sorting method, including ascending: `asc` and descending: `desc`. The default value is `desc`.	
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def OrderBy(self):
        r"""Sorting field, with a value range of `[SessionStartTime, Duration]`. The default value is `SessionStartTime`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        r"""Number of results returned per page, with a value range of 1-100. The default value is `50`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, which starts from 0. The default value is `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DatabaseName = params.get("DatabaseName")
        self._OrderByType = params.get("OrderByType")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryListResponse(AbstractModel):
    r"""DescribeSlowQueryList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of slow logs found, with a maximum of 10,000 entries.	
        :type TotalCount: int
        :param _DurationAnalysis: Segmented analysis results of the time consumption of the slow logs found.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DurationAnalysis: list of DurationAnalysis
        :param _RawSlowQueryList: Collection of detailed information on slow logs found.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RawSlowQueryList: list of RawSlowQuery
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DurationAnalysis = None
        self._RawSlowQueryList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of slow logs found, with a maximum of 10,000 entries.	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DurationAnalysis(self):
        r"""Segmented analysis results of the time consumption of the slow logs found.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DurationAnalysis
        """
        return self._DurationAnalysis

    @DurationAnalysis.setter
    def DurationAnalysis(self, DurationAnalysis):
        self._DurationAnalysis = DurationAnalysis

    @property
    def RawSlowQueryList(self):
        r"""Collection of detailed information on slow logs found.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RawSlowQuery
        """
        return self._RawSlowQueryList

    @RawSlowQueryList.setter
    def RawSlowQueryList(self, RawSlowQueryList):
        self._RawSlowQueryList = RawSlowQueryList

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
        if params.get("DurationAnalysis") is not None:
            self._DurationAnalysis = []
            for item in params.get("DurationAnalysis"):
                obj = DurationAnalysis()
                obj._deserialize(item)
                self._DurationAnalysis.append(obj)
        if params.get("RawSlowQueryList") is not None:
            self._RawSlowQueryList = []
            for item in params.get("RawSlowQueryList"):
                obj = RawSlowQuery()
                obj._deserialize(item)
                self._RawSlowQueryList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    r"""DescribeTasks request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Query by task ID. the FlowId and TaskId returned in other cloud apis are equivalent.
        :type TaskId: int
        :param _DBInstanceId: Query by database instance ID.
        :type DBInstanceId: str
        :param _MinStartTime: Earliest start time of the task, such as 2024-08-23 00:00:00. default shows data within the last 180 days.
        :type MinStartTime: str
        :param _MaxStartTime: Latest start time of the task, such as 2024-08-23 00:00:00, defaults to the current time.
        :type MaxStartTime: str
        :param _Limit: Number of results displayed per page. value range 1-100. default 20.
        :type Limit: int
        :param _Offset: Data offset, starting from 0.
        :type Offset: int
        :param _OrderBy: Sorting field, supports StartTime and EndTime. defaults to StartTime.
        :type OrderBy: str
        :param _OrderByType: Specifies the sorting method, including ascending: `asc` and descending: `desc`. defaults to `desc`.
        :type OrderByType: str
        """
        self._TaskId = None
        self._DBInstanceId = None
        self._MinStartTime = None
        self._MaxStartTime = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def TaskId(self):
        r"""Query by task ID. the FlowId and TaskId returned in other cloud apis are equivalent.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DBInstanceId(self):
        r"""Query by database instance ID.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def MinStartTime(self):
        r"""Earliest start time of the task, such as 2024-08-23 00:00:00. default shows data within the last 180 days.
        :rtype: str
        """
        return self._MinStartTime

    @MinStartTime.setter
    def MinStartTime(self, MinStartTime):
        self._MinStartTime = MinStartTime

    @property
    def MaxStartTime(self):
        r"""Latest start time of the task, such as 2024-08-23 00:00:00, defaults to the current time.
        :rtype: str
        """
        return self._MaxStartTime

    @MaxStartTime.setter
    def MaxStartTime(self, MaxStartTime):
        self._MaxStartTime = MaxStartTime

    @property
    def Limit(self):
        r"""Number of results displayed per page. value range 1-100. default 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Data offset, starting from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sorting field, supports StartTime and EndTime. defaults to StartTime.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Specifies the sorting method, including ascending: `asc` and descending: `desc`. defaults to `desc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DBInstanceId = params.get("DBInstanceId")
        self._MinStartTime = params.get("MinStartTime")
        self._MaxStartTime = params.get("MaxStartTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    r"""DescribeTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of queried tasks.
        :type TotalCount: int
        :param _TaskSet: Task Information List
        :type TaskSet: list of TaskSet
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of queried tasks.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskSet(self):
        r"""Task Information List
        :rtype: list of TaskSet
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

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
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskSet()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    r"""DescribeZones request structure.

    """


class DescribeZonesResponse(AbstractModel):
    r"""DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of returned results.
        :type TotalCount: int
        :param _ZoneSet: AZ information set.
        :type ZoneSet: list of ZoneInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of returned results.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneSet(self):
        r"""AZ information set.
        :rtype: list of ZoneInfo
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

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
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyDBInstanceRequest(AbstractModel):
    r"""DestroyDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: The ID of the instance to be eliminated
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""The ID of the instance to be eliminated
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDBInstanceResponse(AbstractModel):
    r"""DestroyDBInstance response structure.

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


class Detail(AbstractModel):
    r"""Details returned by the `DescribeSlowQueryAnalysis` API

    """

    def __init__(self):
        r"""
        :param _TotalTime: The total execution time (in ms) of all slow query statements during the specified period of time
        :type TotalTime: float
        :param _TotalCallNum: The total number of all slow query statements during the specified period of time
        :type TotalCallNum: int
        :param _AnalysisItems: The statistical analysis list of slow queries
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AnalysisItems: list of AnalysisItems
        """
        self._TotalTime = None
        self._TotalCallNum = None
        self._AnalysisItems = None

    @property
    def TotalTime(self):
        r"""The total execution time (in ms) of all slow query statements during the specified period of time
        :rtype: float
        """
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def TotalCallNum(self):
        r"""The total number of all slow query statements during the specified period of time
        :rtype: int
        """
        return self._TotalCallNum

    @TotalCallNum.setter
    def TotalCallNum(self, TotalCallNum):
        self._TotalCallNum = TotalCallNum

    @property
    def AnalysisItems(self):
        r"""The statistical analysis list of slow queries
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of AnalysisItems
        """
        return self._AnalysisItems

    @AnalysisItems.setter
    def AnalysisItems(self, AnalysisItems):
        self._AnalysisItems = AnalysisItems


    def _deserialize(self, params):
        self._TotalTime = params.get("TotalTime")
        self._TotalCallNum = params.get("TotalCallNum")
        if params.get("AnalysisItems") is not None:
            self._AnalysisItems = []
            for item in params.get("AnalysisItems"):
                obj = AnalysisItems()
                obj._deserialize(item)
                self._AnalysisItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisIsolateDBInstancesRequest(AbstractModel):
    r"""DisIsolateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: Instance ID list. obtain through the api [DescribeDBInstances](https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1). supports de-isolating multiple instances simultaneously.
        :type DBInstanceIdSet: list of str
        :param _Period: Purchase duration, in months.
<Li>Prepaid: Yearly/monthly subscription, supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.</li>.
<Li>Postpaid: Pay-as-you-go, this parameter does not take effect.</li>.
        :type Period: int
        :param _AutoVoucher: Whether to use vouchers.
<li>true: use.</li>.
<li>false: non-use.</li>.
Default value: `false`.
        :type AutoVoucher: bool
        :param _VoucherIds: Voucher ID list
        :type VoucherIds: list of str
        """
        self._DBInstanceIdSet = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None

    @property
    def DBInstanceIdSet(self):
        r"""Instance ID list. obtain through the api [DescribeDBInstances](https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1). supports de-isolating multiple instances simultaneously.
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def Period(self):
        r"""Purchase duration, in months.
<Li>Prepaid: Yearly/monthly subscription, supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.</li>.
<Li>Postpaid: Pay-as-you-go, this parameter does not take effect.</li>.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        r"""Whether to use vouchers.
<li>true: use.</li>.
<li>false: non-use.</li>.
Default value: `false`.
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID list
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds


    def _deserialize(self, params):
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisIsolateDBInstancesResponse(AbstractModel):
    r"""DisIsolateDBInstances response structure.

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


class DurationAnalysis(AbstractModel):
    r"""Analyze the execution time of slow query statements by classifying them to different time ranges

    """

    def __init__(self):
        r"""
        :param _TimeSegment: Time range
        :type TimeSegment: str
        :param _Count: The number of slow query statements whose execution time falls within the time range
        :type Count: int
        """
        self._TimeSegment = None
        self._Count = None

    @property
    def TimeSegment(self):
        r"""Time range
        :rtype: str
        """
        return self._TimeSegment

    @TimeSegment.setter
    def TimeSegment(self, TimeSegment):
        self._TimeSegment = TimeSegment

    @property
    def Count(self):
        r"""The number of slow query statements whose execution time falls within the time range
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._TimeSegment = params.get("TimeSegment")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptionKey(AbstractModel):
    r"""KMS key information

    """

    def __init__(self):
        r"""
        :param _KeyId: Specifies the KeyId for KMS instance encryption.
        :type KeyId: str
        :param _KeyAlias: Alias name of the KMS instance encryption Key.
        :type KeyAlias: str
        :param _DEKCipherTextBlob: Specifies the ciphertext of the instance encryption key DEK.
        :type DEKCipherTextBlob: str
        :param _IsEnabled: Whether the key is enabled. valid values: 1 (enabled), 0 (disabled).
        :type IsEnabled: int
        :param _KeyRegion: Specifies the region of the KMS key.
        :type KeyRegion: str
        :param _CreateTime: Creation time of the DEK key.
        :type CreateTime: str
        :param _KMSClusterId: Specifies the Id of the KMS service cluster where the key resides. being empty indicates the key is in the default KMS cluster. a non-empty value indicates the key is in the specified KMS service cluster.
        :type KMSClusterId: str
        """
        self._KeyId = None
        self._KeyAlias = None
        self._DEKCipherTextBlob = None
        self._IsEnabled = None
        self._KeyRegion = None
        self._CreateTime = None
        self._KMSClusterId = None

    @property
    def KeyId(self):
        r"""Specifies the KeyId for KMS instance encryption.
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyAlias(self):
        r"""Alias name of the KMS instance encryption Key.
        :rtype: str
        """
        return self._KeyAlias

    @KeyAlias.setter
    def KeyAlias(self, KeyAlias):
        self._KeyAlias = KeyAlias

    @property
    def DEKCipherTextBlob(self):
        r"""Specifies the ciphertext of the instance encryption key DEK.
        :rtype: str
        """
        return self._DEKCipherTextBlob

    @DEKCipherTextBlob.setter
    def DEKCipherTextBlob(self, DEKCipherTextBlob):
        self._DEKCipherTextBlob = DEKCipherTextBlob

    @property
    def IsEnabled(self):
        r"""Whether the key is enabled. valid values: 1 (enabled), 0 (disabled).
        :rtype: int
        """
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def KeyRegion(self):
        r"""Specifies the region of the KMS key.
        :rtype: str
        """
        return self._KeyRegion

    @KeyRegion.setter
    def KeyRegion(self, KeyRegion):
        self._KeyRegion = KeyRegion

    @property
    def CreateTime(self):
        r"""Creation time of the DEK key.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def KMSClusterId(self):
        r"""Specifies the Id of the KMS service cluster where the key resides. being empty indicates the key is in the default KMS cluster. a non-empty value indicates the key is in the specified KMS service cluster.
        :rtype: str
        """
        return self._KMSClusterId

    @KMSClusterId.setter
    def KMSClusterId(self, KMSClusterId):
        self._KMSClusterId = KMSClusterId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyAlias = params.get("KeyAlias")
        self._DEKCipherTextBlob = params.get("DEKCipherTextBlob")
        self._IsEnabled = params.get("IsEnabled")
        self._KeyRegion = params.get("KeyRegion")
        self._CreateTime = params.get("CreateTime")
        self._KMSClusterId = params.get("KMSClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrLogDetail(AbstractModel):
    r"""Error log details

    """

    def __init__(self):
        r"""
        :param _UserName: Username
        :type UserName: str
        :param _Database: Database name
        :type Database: str
        :param _ErrTime: Error occurrence time
        :type ErrTime: str
        :param _ErrMsg: Error message
        :type ErrMsg: str
        """
        self._UserName = None
        self._Database = None
        self._ErrTime = None
        self._ErrMsg = None

    @property
    def UserName(self):
        r"""Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        r"""Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def ErrTime(self):
        r"""Error occurrence time
        :rtype: str
        """
        return self._ErrTime

    @ErrTime.setter
    def ErrTime(self, ErrTime):
        self._ErrTime = ErrTime

    @property
    def ErrMsg(self):
        r"""Error message
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Database = params.get("Database")
        self._ErrTime = params.get("ErrTime")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    r"""Parameter modification event information

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name.
        :type ParamName: str
        :param _OldValue: Original parameter value.
        :type OldValue: str
        :param _NewValue: This modification specifies the expected parameter value.
        :type NewValue: str
        :param _ModifyTime: Specifies the start time for backend parameter modification.
        :type ModifyTime: str
        :param _EffectiveTime: Specifies the start of effective time for the backend parameter.
        :type EffectiveTime: str
        :param _State: Modification status. valid values: in progress, success, paused.
        :type State: str
        :param _Operator: Operator (normal: user sub UIN).
        :type Operator: str
        :param _EventLog: Time log.
        :type EventLog: str
        """
        self._ParamName = None
        self._OldValue = None
        self._NewValue = None
        self._ModifyTime = None
        self._EffectiveTime = None
        self._State = None
        self._Operator = None
        self._EventLog = None

    @property
    def ParamName(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def OldValue(self):
        r"""Original parameter value.
        :rtype: str
        """
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        r"""This modification specifies the expected parameter value.
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def ModifyTime(self):
        r"""Specifies the start time for backend parameter modification.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def EffectiveTime(self):
        r"""Specifies the start of effective time for the backend parameter.
        :rtype: str
        """
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def State(self):
        r"""Modification status. valid values: in progress, success, paused.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Operator(self):
        r"""Operator (normal: user sub UIN).
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def EventLog(self):
        r"""Time log.
        :rtype: str
        """
        return self._EventLog

    @EventLog.setter
    def EventLog(self, EventLog):
        self._EventLog = EventLog


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        self._ModifyTime = params.get("ModifyTime")
        self._EffectiveTime = params.get("EffectiveTime")
        self._State = params.get("State")
        self._Operator = params.get("Operator")
        self._EventLog = params.get("EventLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventItem(AbstractModel):
    r"""Modification details of one parameter

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name.
        :type ParamName: str
        :param _EventCount: Number of modified events.
        :type EventCount: int
        :param _EventDetail: Last modification time.
        :type EventDetail: list of EventInfo
        """
        self._ParamName = None
        self._EventCount = None
        self._EventDetail = None

    @property
    def ParamName(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def EventCount(self):
        r"""Number of modified events.
        :rtype: int
        """
        return self._EventCount

    @EventCount.setter
    def EventCount(self, EventCount):
        self._EventCount = EventCount

    @property
    def EventDetail(self):
        r"""Last modification time.
        :rtype: list of EventInfo
        """
        return self._EventDetail

    @EventDetail.setter
    def EventDetail(self, EventDetail):
        self._EventDetail = EventDetail


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._EventCount = params.get("EventCount")
        if params.get("EventDetail") is not None:
            self._EventDetail = []
            for item in params.get("EventDetail"):
                obj = EventInfo()
                obj._deserialize(item)
                self._EventDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""Key-value pair filter for conditional filtering queries, such as filter ID and name
    * If more than one filter exists, the logical relationship between these filters is `AND`.
    * If multiple values exist in one filter, the logical relationship between these values is `OR`.

    """

    def __init__(self):
        r"""
        :param _Name: Filter name.
        :type Name: str
        :param _Values: One or more filter values.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""Filter name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""One or more filter values.
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
        


class InitDBInstancesRequest(AbstractModel):
    r"""InitDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: Instance ID set.
        :type DBInstanceIdSet: list of str
        :param _AdminName: Instance admin account username.
        :type AdminName: str
        :param _AdminPassword: Password corresponding to instance root account username.
        :type AdminPassword: str
        :param _Charset: Instance character set. Valid values: UTF8, LATIN1.
        :type Charset: str
        """
        self._DBInstanceIdSet = None
        self._AdminName = None
        self._AdminPassword = None
        self._Charset = None

    @property
    def DBInstanceIdSet(self):
        r"""Instance ID set.
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def AdminName(self):
        r"""Instance admin account username.
        :rtype: str
        """
        return self._AdminName

    @AdminName.setter
    def AdminName(self, AdminName):
        self._AdminName = AdminName

    @property
    def AdminPassword(self):
        r"""Password corresponding to instance root account username.
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Charset(self):
        r"""Instance character set. Valid values: UTF8, LATIN1.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset


    def _deserialize(self, params):
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._AdminName = params.get("AdminName")
        self._AdminPassword = params.get("AdminPassword")
        self._Charset = params.get("Charset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesResponse(AbstractModel):
    r"""InitDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: Instance ID set.
        :type DBInstanceIdSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DBInstanceIdSet = None
        self._RequestId = None

    @property
    def DBInstanceIdSet(self):
        r"""Instance ID set.
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

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
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._RequestId = params.get("RequestId")


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    r"""InquiryPriceCreateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: <p>Availability zone name. The value of this parameter can be obtained from the returned Zone field of the <a href="https://www.tencentcloud.com/document/product/409/16769?from_cn_redirect=1">DescribeZones</a> API.</p>
        :type Zone: str
        :param _SpecCode: <p>Specification ID. The value of this parameter can be obtained from the returned SpecCode field of the <a href="https://www.tencentcloud.com/document/product/409/89019?from_cn_redirect=1">DescribeClasses</a> API.</p>
        :type SpecCode: str
        :param _Storage: <p>Storage capacity, in GB. The value for this parameter must be set in increments of 10.</p>
        :type Storage: int
        :param _InstanceCount: <p>Instance quantity. The maximum allowed quantity is no more than 100. If you need to create more instances at a time, please contact customer service.</p>
        :type InstanceCount: int
        :param _Period: <p>Purchased duration, in months. Only 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36 are supported.</p>
        :type Period: int
        :param _Pid: <p>[Deprecated and no longer effective] Billing ID. The value of this parameter can be obtained from the returned Pid field of the DescribeProductConfig API.</p>
        :type Pid: int
        :param _InstanceChargeType: <p>Instance billing type. Valid values: PREPAID (prepaid, also known as yearly/monthly subscription) and POSTPAID (pay-as-you-go).<br>Default value: PREPAID.</p>
        :type InstanceChargeType: str
        :param _InstanceType: <p>Instance type. The default value is primary. Valid values:<br>primary (dual-server high availability (one primary and one standby)).<br>readonly (read-only instance).</p>
        :type InstanceType: str
        :param _DBEngine: <p>Database engine. The default value is postgresql. Valid values:<br>postgresql (TencentDB for PostgreSQL).<br>mssql_compatible (MSSQL compatible - TencentDB for PostgreSQL).</p>
        :type DBEngine: str
        :param _StorageType: <p>Instance storage type. Valid values: PHYSICAL_LOCAL_SSD: local SSD of physical machine. CLOUD_PREMIUM: Premium Disk. CLOUD_SSD: Cloud SSD. CLOUD_HSSD: Enhanced SSD.</p>
        :type StorageType: str
        """
        self._Zone = None
        self._SpecCode = None
        self._Storage = None
        self._InstanceCount = None
        self._Period = None
        self._Pid = None
        self._InstanceChargeType = None
        self._InstanceType = None
        self._DBEngine = None
        self._StorageType = None

    @property
    def Zone(self):
        r"""<p>Availability zone name. The value of this parameter can be obtained from the returned Zone field of the <a href="https://www.tencentcloud.com/document/product/409/16769?from_cn_redirect=1">DescribeZones</a> API.</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecCode(self):
        r"""<p>Specification ID. The value of this parameter can be obtained from the returned SpecCode field of the <a href="https://www.tencentcloud.com/document/product/409/89019?from_cn_redirect=1">DescribeClasses</a> API.</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Storage(self):
        r"""<p>Storage capacity, in GB. The value for this parameter must be set in increments of 10.</p>
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceCount(self):
        r"""<p>Instance quantity. The maximum allowed quantity is no more than 100. If you need to create more instances at a time, please contact customer service.</p>
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Period(self):
        r"""<p>Purchased duration, in months. Only 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36 are supported.</p>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Pid(self):
        r"""<p>[Deprecated and no longer effective] Billing ID. The value of this parameter can be obtained from the returned Pid field of the DescribeProductConfig API.</p>
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def InstanceChargeType(self):
        r"""<p>Instance billing type. Valid values: PREPAID (prepaid, also known as yearly/monthly subscription) and POSTPAID (pay-as-you-go).<br>Default value: PREPAID.</p>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceType(self):
        r"""<p>Instance type. The default value is primary. Valid values:<br>primary (dual-server high availability (one primary and one standby)).<br>readonly (read-only instance).</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DBEngine(self):
        r"""<p>Database engine. The default value is postgresql. Valid values:<br>postgresql (TencentDB for PostgreSQL).<br>mssql_compatible (MSSQL compatible - TencentDB for PostgreSQL).</p>
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def StorageType(self):
        r"""<p>Instance storage type. Valid values: PHYSICAL_LOCAL_SSD: local SSD of physical machine. CLOUD_PREMIUM: Premium Disk. CLOUD_SSD: Cloud SSD. CLOUD_HSSD: Enhanced SSD.</p>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SpecCode = params.get("SpecCode")
        self._Storage = params.get("Storage")
        self._InstanceCount = params.get("InstanceCount")
        self._Period = params.get("Period")
        self._Pid = params.get("Pid")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._InstanceType = params.get("InstanceType")
        self._DBEngine = params.get("DBEngine")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    r"""InquiryPriceCreateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: <p>List price, in cents.</p>
        :type OriginalPrice: int
        :param _Price: <p>Actual payment amount after discount, in cents.</p>
        :type Price: int
        :param _Currency: Currency, such as USD.
        :type Currency: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._Currency = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        r"""<p>List price, in cents.</p>
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        r"""<p>Actual payment amount after discount, in cents.</p>
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Currency(self):
        r"""Currency, such as USD.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

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
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewDBInstanceRequest(AbstractModel):
    r"""InquiryPriceRenewDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _Period: Renewal duration in months. Maximum value: 48
        :type Period: int
        """
        self._DBInstanceId = None
        self._Period = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Period(self):
        r"""Renewal duration in months. Maximum value: 48
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewDBInstanceResponse(AbstractModel):
    r"""InquiryPriceRenewDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: Published price in cents. For example, 24650 indicates 246.5 USD.
        :type OriginalPrice: int
        :param _Price: Discounted total amount. For example, 24650 indicates 246.5 USD.
        :type Price: int
        :param _Currency: Currency, such as USD.
        :type Currency: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._Currency = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        r"""Published price in cents. For example, 24650 indicates 246.5 USD.
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        r"""Discounted total amount. For example, 24650 indicates 246.5 USD.
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Currency(self):
        r"""Currency, such as USD.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

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
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    r"""InquiryPriceUpgradeDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Storage: Instance disk size in GB
        :type Storage: int
        :param _Memory: Instance memory size in GB
        :type Memory: int
        :param _DBInstanceId: Instance ID in the format of postgres-hez4fh0v
        :type DBInstanceId: str
        :param _InstanceChargeType: Instance billing type. Valid value: `POSTPAID_BY_HOUR` (pay-as-you-go hourly)
        :type InstanceChargeType: str
        :param _Cpu: Instance CPU size, unit: Core
        :type Cpu: int
        """
        self._Storage = None
        self._Memory = None
        self._DBInstanceId = None
        self._InstanceChargeType = None
        self._Cpu = None

    @property
    def Storage(self):
        r"""Instance disk size in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Memory(self):
        r"""Instance memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-hez4fh0v
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def InstanceChargeType(self):
        r"""Instance billing type. Valid value: `POSTPAID_BY_HOUR` (pay-as-you-go hourly)
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Cpu(self):
        r"""Instance CPU size, unit: Core
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._Storage = params.get("Storage")
        self._Memory = params.get("Memory")
        self._DBInstanceId = params.get("DBInstanceId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    r"""InquiryPriceUpgradeDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: Total cost before discount.
        :type OriginalPrice: int
        :param _Price: Discounted total amount
        :type Price: int
        :param _Currency: Currency, such as USD.
        :type Currency: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._Currency = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        r"""Total cost before discount.
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        r"""Discounted total amount
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Currency(self):
        r"""Currency, such as USD.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

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
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class IsolateDBInstancesRequest(AbstractModel):
    r"""IsolateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: List of instance IDs. Note that currently you cannot isolate multiple instances at the same time. Only one instance ID can be passed in here.
        :type DBInstanceIdSet: list of str
        """
        self._DBInstanceIdSet = None

    @property
    def DBInstanceIdSet(self):
        r"""List of instance IDs. Note that currently you cannot isolate multiple instances at the same time. Only one instance ID can be passed in here.
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet


    def _deserialize(self, params):
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstancesResponse(AbstractModel):
    r"""IsolateDBInstances response structure.

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


class LockAccountRequest(AbstractModel):
    r"""LockAccount request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID.		
        :type DBInstanceId: str
        :param _UserName: Account name.
        :type UserName: str
        """
        self._DBInstanceId = None
        self._UserName = None

    @property
    def DBInstanceId(self):
        r"""Instance ID.		
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""Account name.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockAccountResponse(AbstractModel):
    r"""LockAccount response structure.

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


class LogBackup(AbstractModel):
    r"""Log backup information of a database

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _Id: Unique ID of a backup file
        :type Id: str
        :param _Name: Backup file name
        :type Name: str
        :param _BackupMethod: Backup method, including physical and logical.
        :type BackupMethod: str
        :param _BackupMode: Backup mode, including automatic and manual.
        :type BackupMode: str
        :param _State: Backup task status
        :type State: str
        :param _Size: Backup set size in bytes
        :type Size: int
        :param _StartTime: Backup start time
        :type StartTime: str
        :param _FinishTime: Backup end time
        :type FinishTime: str
        :param _ExpireTime: Backup expiration time
        :type ExpireTime: str
        """
        self._DBInstanceId = None
        self._Id = None
        self._Name = None
        self._BackupMethod = None
        self._BackupMode = None
        self._State = None
        self._Size = None
        self._StartTime = None
        self._FinishTime = None
        self._ExpireTime = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Id(self):
        r"""Unique ID of a backup file
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Backup file name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BackupMethod(self):
        r"""Backup method, including physical and logical.
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupMode(self):
        r"""Backup mode, including automatic and manual.
        :rtype: str
        """
        return self._BackupMode

    @BackupMode.setter
    def BackupMode(self, BackupMode):
        self._BackupMode = BackupMode

    @property
    def State(self):
        r"""Backup task status
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Size(self):
        r"""Backup set size in bytes
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def StartTime(self):
        r"""Backup start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        r"""Backup end time
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def ExpireTime(self):
        r"""Backup expiration time
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupMode = params.get("BackupMode")
        self._State = params.get("State")
        self._Size = params.get("Size")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesRequest(AbstractModel):
    r"""ModifyAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :type DBInstanceId: str
        :param _UserName: Modify the permission of this account for a database object. obtain through the [DescribeAccounts](https://www.tencentcloud.com/document/api/409/18109?from_cn_redirect=1) api.
        :type UserName: str
        :param _ModifyPrivilegeSet: Permission information to modify. supports batch modification. the maximum number of modifications per batch is 50.
        :type ModifyPrivilegeSet: list of ModifyPrivilege
        """
        self._DBInstanceId = None
        self._UserName = None
        self._ModifyPrivilegeSet = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""Modify the permission of this account for a database object. obtain through the [DescribeAccounts](https://www.tencentcloud.com/document/api/409/18109?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ModifyPrivilegeSet(self):
        r"""Permission information to modify. supports batch modification. the maximum number of modifications per batch is 50.
        :rtype: list of ModifyPrivilege
        """
        return self._ModifyPrivilegeSet

    @ModifyPrivilegeSet.setter
    def ModifyPrivilegeSet(self, ModifyPrivilegeSet):
        self._ModifyPrivilegeSet = ModifyPrivilegeSet


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        if params.get("ModifyPrivilegeSet") is not None:
            self._ModifyPrivilegeSet = []
            for item in params.get("ModifyPrivilegeSet"):
                obj = ModifyPrivilege()
                obj._deserialize(item)
                self._ModifyPrivilegeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    r"""ModifyAccountPrivileges response structure.

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


class ModifyAccountRemarkRequest(AbstractModel):
    r"""ModifyAccountRemark request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of postgres-4wdeb0zv
        :type DBInstanceId: str
        :param _UserName: Instance username
        :type UserName: str
        :param _Remark: New remarks corresponding to user `UserName`
        :type Remark: str
        """
        self._DBInstanceId = None
        self._UserName = None
        self._Remark = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-4wdeb0zv
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""Instance username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Remark(self):
        r"""New remarks corresponding to user `UserName`
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountRemarkResponse(AbstractModel):
    r"""ModifyAccountRemark response structure.

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


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    r"""ModifyBackupDownloadRestriction request structure.

    """

    def __init__(self):
        r"""
        :param _RestrictionType: Type of the network restrictions for downloading a backup file. Valid values: `NONE` (backups can be downloaded over both private and public networks), `INTRANET` (backups can only be downloaded over the private network), `CUSTOMIZE` (backups can be downloaded over specified VPCs or at specified IPs).
        :type RestrictionType: str
        :param _VpcRestrictionEffect: Whether VPC is allowed. Valid values: `ALLOW` (allow), `DENY` (deny).
        :type VpcRestrictionEffect: str
        :param _VpcIdSet: Whether it is allowed to download the VPC ID list of the backup files.
        :type VpcIdSet: list of str
        :param _IpRestrictionEffect: Whether IP is allowed. Valid values: `ALLOW` (allow), `DENY` (deny).
        :type IpRestrictionEffect: str
        :param _IpSet: Whether it is allowed to download the IP list of the backup files.
        :type IpSet: list of str
        """
        self._RestrictionType = None
        self._VpcRestrictionEffect = None
        self._VpcIdSet = None
        self._IpRestrictionEffect = None
        self._IpSet = None

    @property
    def RestrictionType(self):
        r"""Type of the network restrictions for downloading a backup file. Valid values: `NONE` (backups can be downloaded over both private and public networks), `INTRANET` (backups can only be downloaded over the private network), `CUSTOMIZE` (backups can be downloaded over specified VPCs or at specified IPs).
        :rtype: str
        """
        return self._RestrictionType

    @RestrictionType.setter
    def RestrictionType(self, RestrictionType):
        self._RestrictionType = RestrictionType

    @property
    def VpcRestrictionEffect(self):
        r"""Whether VPC is allowed. Valid values: `ALLOW` (allow), `DENY` (deny).
        :rtype: str
        """
        return self._VpcRestrictionEffect

    @VpcRestrictionEffect.setter
    def VpcRestrictionEffect(self, VpcRestrictionEffect):
        self._VpcRestrictionEffect = VpcRestrictionEffect

    @property
    def VpcIdSet(self):
        r"""Whether it is allowed to download the VPC ID list of the backup files.
        :rtype: list of str
        """
        return self._VpcIdSet

    @VpcIdSet.setter
    def VpcIdSet(self, VpcIdSet):
        self._VpcIdSet = VpcIdSet

    @property
    def IpRestrictionEffect(self):
        r"""Whether IP is allowed. Valid values: `ALLOW` (allow), `DENY` (deny).
        :rtype: str
        """
        return self._IpRestrictionEffect

    @IpRestrictionEffect.setter
    def IpRestrictionEffect(self, IpRestrictionEffect):
        self._IpRestrictionEffect = IpRestrictionEffect

    @property
    def IpSet(self):
        r"""Whether it is allowed to download the IP list of the backup files.
        :rtype: list of str
        """
        return self._IpSet

    @IpSet.setter
    def IpSet(self, IpSet):
        self._IpSet = IpSet


    def _deserialize(self, params):
        self._RestrictionType = params.get("RestrictionType")
        self._VpcRestrictionEffect = params.get("VpcRestrictionEffect")
        self._VpcIdSet = params.get("VpcIdSet")
        self._IpRestrictionEffect = params.get("IpRestrictionEffect")
        self._IpSet = params.get("IpSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadRestrictionResponse(AbstractModel):
    r"""ModifyBackupDownloadRestriction response structure.

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


class ModifyBackupPlanRequest(AbstractModel):
    r"""ModifyBackupPlan request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _MinBackupStartTime: The earliest time to start a backup
        :type MinBackupStartTime: str
        :param _MaxBackupStartTime: The latest time to start a backup
        :type MaxBackupStartTime: str
        :param _BaseBackupRetentionPeriod: Backup retention period in days. Value range: 7-1830
        :type BaseBackupRetentionPeriod: int
        :param _BackupPeriod: Backup cycle, which means on which days each week the instance will be backed up. The parameter value should be the lowercase names of the days of the week.
        :type BackupPeriod: list of str
        :param _LogBackupRetentionPeriod: Instance log backup retention duration, with a value range of 7-1830 and a unit of day
        :type LogBackupRetentionPeriod: int
        """
        self._DBInstanceId = None
        self._MinBackupStartTime = None
        self._MaxBackupStartTime = None
        self._BaseBackupRetentionPeriod = None
        self._BackupPeriod = None
        self._LogBackupRetentionPeriod = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def MinBackupStartTime(self):
        r"""The earliest time to start a backup
        :rtype: str
        """
        return self._MinBackupStartTime

    @MinBackupStartTime.setter
    def MinBackupStartTime(self, MinBackupStartTime):
        self._MinBackupStartTime = MinBackupStartTime

    @property
    def MaxBackupStartTime(self):
        r"""The latest time to start a backup
        :rtype: str
        """
        return self._MaxBackupStartTime

    @MaxBackupStartTime.setter
    def MaxBackupStartTime(self, MaxBackupStartTime):
        self._MaxBackupStartTime = MaxBackupStartTime

    @property
    def BaseBackupRetentionPeriod(self):
        r"""Backup retention period in days. Value range: 7-1830
        :rtype: int
        """
        return self._BaseBackupRetentionPeriod

    @BaseBackupRetentionPeriod.setter
    def BaseBackupRetentionPeriod(self, BaseBackupRetentionPeriod):
        self._BaseBackupRetentionPeriod = BaseBackupRetentionPeriod

    @property
    def BackupPeriod(self):
        r"""Backup cycle, which means on which days each week the instance will be backed up. The parameter value should be the lowercase names of the days of the week.
        :rtype: list of str
        """
        return self._BackupPeriod

    @BackupPeriod.setter
    def BackupPeriod(self, BackupPeriod):
        self._BackupPeriod = BackupPeriod

    @property
    def LogBackupRetentionPeriod(self):
        r"""Instance log backup retention duration, with a value range of 7-1830 and a unit of day
        :rtype: int
        """
        return self._LogBackupRetentionPeriod

    @LogBackupRetentionPeriod.setter
    def LogBackupRetentionPeriod(self, LogBackupRetentionPeriod):
        self._LogBackupRetentionPeriod = LogBackupRetentionPeriod


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._MinBackupStartTime = params.get("MinBackupStartTime")
        self._MaxBackupStartTime = params.get("MaxBackupStartTime")
        self._BaseBackupRetentionPeriod = params.get("BaseBackupRetentionPeriod")
        self._BackupPeriod = params.get("BackupPeriod")
        self._LogBackupRetentionPeriod = params.get("LogBackupRetentionPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupPlanResponse(AbstractModel):
    r"""ModifyBackupPlan response structure.

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


class ModifyBaseBackupExpireTimeRequest(AbstractModel):
    r"""ModifyBaseBackupExpireTime request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _BaseBackupId: Data backup ID. obtain through the api [DescribeBaseBackups](https://www.tencentcloud.com/document/product/409/54343?lang=en).
        :type BaseBackupId: str
        :param _NewExpireTime: New expiration time
        :type NewExpireTime: str
        """
        self._DBInstanceId = None
        self._BaseBackupId = None
        self._NewExpireTime = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def BaseBackupId(self):
        r"""Data backup ID. obtain through the api [DescribeBaseBackups](https://www.tencentcloud.com/document/product/409/54343?lang=en).
        :rtype: str
        """
        return self._BaseBackupId

    @BaseBackupId.setter
    def BaseBackupId(self, BaseBackupId):
        self._BaseBackupId = BaseBackupId

    @property
    def NewExpireTime(self):
        r"""New expiration time
        :rtype: str
        """
        return self._NewExpireTime

    @NewExpireTime.setter
    def NewExpireTime(self, NewExpireTime):
        self._NewExpireTime = NewExpireTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._BaseBackupId = params.get("BaseBackupId")
        self._NewExpireTime = params.get("NewExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBaseBackupExpireTimeResponse(AbstractModel):
    r"""ModifyBaseBackupExpireTime response structure.

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


class ModifyDBInstanceChargeTypeRequest(AbstractModel):
    r"""ModifyDBInstanceChargeType request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Specifies the instance ID, such as postgres-6fego161. obtain through the api [DescribeDBInstances](https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1).
        :type DBInstanceId: str
        :param _InstanceChargeType: Instance billing type, which currently supports:.
<Li>PREPAID: prepaid, i.e., yearly/monthly subscription</li>.
<Li>POSTPAID_BY_HOUR: pay-as-you-go, i.e., pay by consumption.</li>.
Default value: PREPAID
        :type InstanceChargeType: str
        :param _Period: Purchase duration, in months.
<Li>Prepaid: supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.</li>.
<li>Pay-as-you-go: Only supports `1`.</li>
        :type Period: int
        :param _AutoRenewFlag: Specifies the auto-renewal flag.
<Li>`0`: manual renewal.</li>.
<Li>`1`: auto-renewal</li>.
Default value: 0
        :type AutoRenewFlag: int
        :param _AutoVoucher: Specifies whether to automatically use a voucher.
<Li>0: no.</li>.
<Li>`1`: yes.</li>.
Default value: 0
        :type AutoVoucher: int
        """
        self._DBInstanceId = None
        self._InstanceChargeType = None
        self._Period = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None

    @property
    def DBInstanceId(self):
        r"""Specifies the instance ID, such as postgres-6fego161. obtain through the api [DescribeDBInstances](https://www.tencentcloud.comom/document/api/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def InstanceChargeType(self):
        r"""Instance billing type, which currently supports:.
<Li>PREPAID: prepaid, i.e., yearly/monthly subscription</li>.
<Li>POSTPAID_BY_HOUR: pay-as-you-go, i.e., pay by consumption.</li>.
Default value: PREPAID
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Period(self):
        r"""Purchase duration, in months.
<Li>Prepaid: supports `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, and `36`.</li>.
<li>Pay-as-you-go: Only supports `1`.</li>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoRenewFlag(self):
        r"""Specifies the auto-renewal flag.
<Li>`0`: manual renewal.</li>.
<Li>`1`: auto-renewal</li>.
Default value: 0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        r"""Specifies whether to automatically use a voucher.
<Li>0: no.</li>.
<Li>`1`: yes.</li>.
Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Period = params.get("Period")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceChargeTypeResponse(AbstractModel):
    r"""ModifyDBInstanceChargeType response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order name
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceDeploymentRequest(AbstractModel):
    r"""ModifyDBInstanceDeployment request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID.
        :type DBInstanceId: str
        :param _DBNodeSet: Deployment information of the instance node, which will display the information of each AZ when the instance node is deployed across multiple AZs.
The information of AZ can be obtained from the `Zone` field in the returned value of the [DescribeZones](https://intl.cloud.tencent.com/document/api/409/16769?from_cn_redirect=1) API.
        :type DBNodeSet: list of DBNode
        :param _SwitchTag: Switch time after instance configurations are modified.
<li>0: Switch immediately</li>
<li>1: Switch at specified time</li>
<li>2: Switch during maintenance time window</li>
Default value: 0
        :type SwitchTag: int
        :param _SwitchStartTime: Switch start time in the format of `HH:MM:SS`, such as 01:00:00. When `SwitchTag` is 0 or 2, this parameter becomes invalid.
        :type SwitchStartTime: str
        :param _SwitchEndTime: Switch end time in the format of `HH:MM:SS`, such as 01:30:00. When `SwitchTag` is 0 or 2, this parameter becomes invalid.
        :type SwitchEndTime: str
        """
        self._DBInstanceId = None
        self._DBNodeSet = None
        self._SwitchTag = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None

    @property
    def DBInstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DBNodeSet(self):
        r"""Deployment information of the instance node, which will display the information of each AZ when the instance node is deployed across multiple AZs.
The information of AZ can be obtained from the `Zone` field in the returned value of the [DescribeZones](https://intl.cloud.tencent.com/document/api/409/16769?from_cn_redirect=1) API.
        :rtype: list of DBNode
        """
        return self._DBNodeSet

    @DBNodeSet.setter
    def DBNodeSet(self, DBNodeSet):
        self._DBNodeSet = DBNodeSet

    @property
    def SwitchTag(self):
        r"""Switch time after instance configurations are modified.
<li>0: Switch immediately</li>
<li>1: Switch at specified time</li>
<li>2: Switch during maintenance time window</li>
Default value: 0
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchStartTime(self):
        r"""Switch start time in the format of `HH:MM:SS`, such as 01:00:00. When `SwitchTag` is 0 or 2, this parameter becomes invalid.
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        r"""Switch end time in the format of `HH:MM:SS`, such as 01:30:00. When `SwitchTag` is 0 or 2, this parameter becomes invalid.
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        if params.get("DBNodeSet") is not None:
            self._DBNodeSet = []
            for item in params.get("DBNodeSet"):
                obj = DBNode()
                obj._deserialize(item)
                self._DBNodeSet.append(obj)
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceDeploymentResponse(AbstractModel):
    r"""ModifyDBInstanceDeployment response structure.

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


class ModifyDBInstanceHAConfigRequest(AbstractModel):
    r"""ModifyDBInstanceHAConfig request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _SyncMode: Primary-standby sync mode. Valid values:
<li>`Semi-sync`
<li>`Async`

        :type SyncMode: str
        :param _MaxStandbyLatency: Maximum data lag for high-availability standby server. The standby node can be promoted to the primary node when its data lag and the delay time are both less than the value of `MaxStandbyLatency` and `MaxStandbyLag` respectively.
<li>Unit: byte
<li>Value range: 1073741824-322122547200
        :type MaxStandbyLatency: int
        :param _MaxStandbyLag: The maximum delay for high-availability standby server The standby node can be promoted to the primary node when its data lag and the delay time are both less or equals to the value of `MaxStandbyLatency` and `MaxStandbyLag` respectively.
<li>Unit: s
<li>Value range: 5-10
        :type MaxStandbyLag: int
        :param _MaxSyncStandbyLatency: Maximum data sync lag for standby server. If data lag of the standby node and the delay ime are both less than or equals to the values of `MaxSyncStandbyLatency` and `MaxSyncStandbyLag`, the standby server adopts semi-sync replication; if not, it adopts async replication.
This value is only valid for the instance with `SyncMode` set to `Semi-sync`.
When the semi-sync replication mode of the instance is not allowed to downgrade to async replication, `MaxSyncStandbyLatency` and `MaxSyncStandbyLag` are not required.
When the semi-sync instance is allowed to downgrade to async replication, `MaxSyncStandbyLatency` is required and `MaxSyncStandbyLag` must be left empty for PostgreSQL 9; `MaxSyncStandbyLatency` and MaxSyncStandbyLag` are required for PostgreSQL 10 and later.
        :type MaxSyncStandbyLatency: int
        :param _MaxSyncStandbyLag: Maximum delay for sync standby server. If the delay time for standby server and the data lag are both less than or equals to the value of `MaxSyncStandbyLag` and `MaxSyncStandbyLatency` respectively, the standby server adopts sync replication mode; if not, it adopts async replication.
This value is only valid for the instance with `SyncMode` set to `Semi-sync`.
When the semi-sync replication mode of the instance is not allowed to downgrade to async replication, `MaxSyncStandbyLatency` and `MaxSyncStandbyLag` are not required.
When the semi-sync instance is allowed to downgrade to async replication, `MaxSyncStandbyLatency` is required and `MaxSyncStandbyLag` must be left empty for PostgreSQL 9; `MaxSyncStandbyLatency` and MaxSyncStandbyLag` are required for PostgreSQL 10 and later.
        :type MaxSyncStandbyLag: int
        """
        self._DBInstanceId = None
        self._SyncMode = None
        self._MaxStandbyLatency = None
        self._MaxStandbyLag = None
        self._MaxSyncStandbyLatency = None
        self._MaxSyncStandbyLag = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def SyncMode(self):
        r"""Primary-standby sync mode. Valid values:
<li>`Semi-sync`
<li>`Async`

        :rtype: str
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def MaxStandbyLatency(self):
        r"""Maximum data lag for high-availability standby server. The standby node can be promoted to the primary node when its data lag and the delay time are both less than the value of `MaxStandbyLatency` and `MaxStandbyLag` respectively.
<li>Unit: byte
<li>Value range: 1073741824-322122547200
        :rtype: int
        """
        return self._MaxStandbyLatency

    @MaxStandbyLatency.setter
    def MaxStandbyLatency(self, MaxStandbyLatency):
        self._MaxStandbyLatency = MaxStandbyLatency

    @property
    def MaxStandbyLag(self):
        r"""The maximum delay for high-availability standby server The standby node can be promoted to the primary node when its data lag and the delay time are both less or equals to the value of `MaxStandbyLatency` and `MaxStandbyLag` respectively.
<li>Unit: s
<li>Value range: 5-10
        :rtype: int
        """
        return self._MaxStandbyLag

    @MaxStandbyLag.setter
    def MaxStandbyLag(self, MaxStandbyLag):
        self._MaxStandbyLag = MaxStandbyLag

    @property
    def MaxSyncStandbyLatency(self):
        r"""Maximum data sync lag for standby server. If data lag of the standby node and the delay ime are both less than or equals to the values of `MaxSyncStandbyLatency` and `MaxSyncStandbyLag`, the standby server adopts semi-sync replication; if not, it adopts async replication.
This value is only valid for the instance with `SyncMode` set to `Semi-sync`.
When the semi-sync replication mode of the instance is not allowed to downgrade to async replication, `MaxSyncStandbyLatency` and `MaxSyncStandbyLag` are not required.
When the semi-sync instance is allowed to downgrade to async replication, `MaxSyncStandbyLatency` is required and `MaxSyncStandbyLag` must be left empty for PostgreSQL 9; `MaxSyncStandbyLatency` and MaxSyncStandbyLag` are required for PostgreSQL 10 and later.
        :rtype: int
        """
        return self._MaxSyncStandbyLatency

    @MaxSyncStandbyLatency.setter
    def MaxSyncStandbyLatency(self, MaxSyncStandbyLatency):
        self._MaxSyncStandbyLatency = MaxSyncStandbyLatency

    @property
    def MaxSyncStandbyLag(self):
        r"""Maximum delay for sync standby server. If the delay time for standby server and the data lag are both less than or equals to the value of `MaxSyncStandbyLag` and `MaxSyncStandbyLatency` respectively, the standby server adopts sync replication mode; if not, it adopts async replication.
This value is only valid for the instance with `SyncMode` set to `Semi-sync`.
When the semi-sync replication mode of the instance is not allowed to downgrade to async replication, `MaxSyncStandbyLatency` and `MaxSyncStandbyLag` are not required.
When the semi-sync instance is allowed to downgrade to async replication, `MaxSyncStandbyLatency` is required and `MaxSyncStandbyLag` must be left empty for PostgreSQL 9; `MaxSyncStandbyLatency` and MaxSyncStandbyLag` are required for PostgreSQL 10 and later.
        :rtype: int
        """
        return self._MaxSyncStandbyLag

    @MaxSyncStandbyLag.setter
    def MaxSyncStandbyLag(self, MaxSyncStandbyLag):
        self._MaxSyncStandbyLag = MaxSyncStandbyLag


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._SyncMode = params.get("SyncMode")
        self._MaxStandbyLatency = params.get("MaxStandbyLatency")
        self._MaxStandbyLag = params.get("MaxStandbyLag")
        self._MaxSyncStandbyLatency = params.get("MaxSyncStandbyLatency")
        self._MaxSyncStandbyLag = params.get("MaxSyncStandbyLag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceHAConfigResponse(AbstractModel):
    r"""ModifyDBInstanceHAConfig response structure.

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


class ModifyDBInstanceNameRequest(AbstractModel):
    r"""ModifyDBInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Database instance ID in the format of postgres-6fego161
        :type DBInstanceId: str
        :param _InstanceName: Instance name, which can contain up to 60 letters, digits, hyphens, and symbols (_-). If this parameter is not specified, "Unnamed" will be displayed by default.

        :type InstanceName: str
        """
        self._DBInstanceId = None
        self._InstanceName = None

    @property
    def DBInstanceId(self):
        r"""Database instance ID in the format of postgres-6fego161
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def InstanceName(self):
        r"""Instance name, which can contain up to 60 letters, digits, hyphens, and symbols (_-). If this parameter is not specified, "Unnamed" will be displayed by default.

        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    r"""ModifyDBInstanceName response structure.

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


class ModifyDBInstanceParametersRequest(AbstractModel):
    r"""ModifyDBInstanceParameters request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _ParamList: Parameters to be modified and expected values.
        :type ParamList: list of ParamEntry
        """
        self._DBInstanceId = None
        self._ParamList = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ParamList(self):
        r"""Parameters to be modified and expected values.
        :rtype: list of ParamEntry
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamEntry()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceParametersResponse(AbstractModel):
    r"""ModifyDBInstanceParameters response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID.
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


class ModifyDBInstanceReadOnlyGroupRequest(AbstractModel):
    r"""ModifyDBInstanceReadOnlyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: ID of the RO group to which the read-only replica belongs
        :type ReadOnlyGroupId: str
        :param _NewReadOnlyGroupId: ID of the new RO group into which the read-only replica will move
        :type NewReadOnlyGroupId: str
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None
        self._NewReadOnlyGroupId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""ID of the RO group to which the read-only replica belongs
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def NewReadOnlyGroupId(self):
        r"""ID of the new RO group into which the read-only replica will move
        :rtype: str
        """
        return self._NewReadOnlyGroupId

    @NewReadOnlyGroupId.setter
    def NewReadOnlyGroupId(self, NewReadOnlyGroupId):
        self._NewReadOnlyGroupId = NewReadOnlyGroupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._NewReadOnlyGroupId = params.get("NewReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceReadOnlyGroupResponse(AbstractModel):
    r"""ModifyDBInstanceReadOnlyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task ID
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


class ModifyDBInstanceSSLConfigRequest(AbstractModel):
    r"""ModifyDBInstanceSSLConfig request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _SSLEnabled: Turn on or off SSL. true - turn on; false - turn off.
        :type SSLEnabled: bool
        :param _ConnectAddress: The unique connection address protected by an SSL certificate. for a primary instance, it can be set to private and public IP addresses. for a read-only instance, it can be set to the instance IP or read-only group IP. this parameter is required when enabling SSL or modifying the SSL-protected connection address. it will be ignored when disabling SSL.
        :type ConnectAddress: str
        """
        self._DBInstanceId = None
        self._SSLEnabled = None
        self._ConnectAddress = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def SSLEnabled(self):
        r"""Turn on or off SSL. true - turn on; false - turn off.
        :rtype: bool
        """
        return self._SSLEnabled

    @SSLEnabled.setter
    def SSLEnabled(self, SSLEnabled):
        self._SSLEnabled = SSLEnabled

    @property
    def ConnectAddress(self):
        r"""The unique connection address protected by an SSL certificate. for a primary instance, it can be set to private and public IP addresses. for a read-only instance, it can be set to the instance IP or read-only group IP. this parameter is required when enabling SSL or modifying the SSL-protected connection address. it will be ignored when disabling SSL.
        :rtype: str
        """
        return self._ConnectAddress

    @ConnectAddress.setter
    def ConnectAddress(self, ConnectAddress):
        self._ConnectAddress = ConnectAddress


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._SSLEnabled = params.get("SSLEnabled")
        self._ConnectAddress = params.get("ConnectAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSSLConfigResponse(AbstractModel):
    r"""ModifyDBInstanceSSLConfig response structure.

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


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    r"""ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIdSet: The list of security groups to be associated with the instance or RO groups.
Information of security groups can be obtained from the `sgld` field in the returned value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) API.

        :type SecurityGroupIdSet: list of str
        :param _DBInstanceId: Instance ID. Either this parameter or `ReadOnlyGroupId` must be passed in. If both parameters are passed in, `ReadOnlyGroupId` will be ignored.
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: RO group ID. Either this parameter or `DBInstanceId` must be passed in. To modify  the security groups associated with the RO groups, only pass in `ReadOnlyGroupId`.
        :type ReadOnlyGroupId: str
        """
        self._SecurityGroupIdSet = None
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def SecurityGroupIdSet(self):
        r"""The list of security groups to be associated with the instance or RO groups.
Information of security groups can be obtained from the `sgld` field in the returned value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) API.

        :rtype: list of str
        """
        return self._SecurityGroupIdSet

    @SecurityGroupIdSet.setter
    def SecurityGroupIdSet(self, SecurityGroupIdSet):
        self._SecurityGroupIdSet = SecurityGroupIdSet

    @property
    def DBInstanceId(self):
        r"""Instance ID. Either this parameter or `ReadOnlyGroupId` must be passed in. If both parameters are passed in, `ReadOnlyGroupId` will be ignored.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""RO group ID. Either this parameter or `DBInstanceId` must be passed in. To modify  the security groups associated with the RO groups, only pass in `ReadOnlyGroupId`.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._SecurityGroupIdSet = params.get("SecurityGroupIdSet")
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
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


class ModifyDBInstanceSpecRequest(AbstractModel):
    r"""ModifyDBInstanceSpec request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of postgres-6bwgamo3.
        :type DBInstanceId: str
        :param _Memory: Instance memory size in GiB after modification.
        :type Memory: int
        :param _Storage: Instance disk size in GiB after modification.
        :type Storage: int
        :param _AutoVoucher: Whether to automatically use coupons:
<li>`0`: no</li>
<li>`1`: yes</li>
Default value: 0
        :type AutoVoucher: int
        :param _VoucherIds: Voucher ID list. Currently, you can specify only one voucher.
        :type VoucherIds: list of str
        :param _ActivityId: Campaign ID.
        :type ActivityId: int
        :param _SwitchTag: Switch time after instance configurations are modified.
<li>0: Switch immediately</li>
<li>1: Switch at specified time</li>
<li>2: Switch during maintenance time window</li>
Default value: 0
        :type SwitchTag: int
        :param _SwitchStartTime: Switch start time in the format of `HH:MM:SS`, such as 01:00:00. When `SwitchTag` is 0 or 2, this parameter becomes invalid.
        :type SwitchStartTime: str
        :param _SwitchEndTime: Switch end time in the format of `HH:MM:SS`, such as 01:30:00. When `SwitchTag` is 0 or 2, this parameter becomes invalid.
        :type SwitchEndTime: str
        :param _Cpu: Instance CPU size in Cores after modification.
        :type Cpu: int
        """
        self._DBInstanceId = None
        self._Memory = None
        self._Storage = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ActivityId = None
        self._SwitchTag = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None
        self._Cpu = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-6bwgamo3.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Memory(self):
        r"""Instance memory size in GiB after modification.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Instance disk size in GiB after modification.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use coupons:
<li>`0`: no</li>
<li>`1`: yes</li>
Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID list. Currently, you can specify only one voucher.
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ActivityId(self):
        r"""Campaign ID.
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def SwitchTag(self):
        r"""Switch time after instance configurations are modified.
<li>0: Switch immediately</li>
<li>1: Switch at specified time</li>
<li>2: Switch during maintenance time window</li>
Default value: 0
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchStartTime(self):
        r"""Switch start time in the format of `HH:MM:SS`, such as 01:00:00. When `SwitchTag` is 0 or 2, this parameter becomes invalid.
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        r"""Switch end time in the format of `HH:MM:SS`, such as 01:30:00. When `SwitchTag` is 0 or 2, this parameter becomes invalid.
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime

    @property
    def Cpu(self):
        r"""Instance CPU size in Cores after modification.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._ActivityId = params.get("ActivityId")
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSpecResponse(AbstractModel):
    r"""ModifyDBInstanceSpec response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order ID.
        :type DealName: str
        :param _BillId: Bill ID of frozen fees.
        :type BillId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._BillId = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order ID.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def BillId(self):
        r"""Bill ID of frozen fees.
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

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
        self._DealName = params.get("DealName")
        self._BillId = params.get("BillId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    r"""ModifyDBInstancesProject request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: List of instance IDs. Note that currently you cannot manipulate multiple instances at the same time. Only one instance ID can be passed in here.
        :type DBInstanceIdSet: list of str
        :param _ProjectId: ID of the new project
        :type ProjectId: str
        """
        self._DBInstanceIdSet = None
        self._ProjectId = None

    @property
    def DBInstanceIdSet(self):
        r"""List of instance IDs. Note that currently you cannot manipulate multiple instances at the same time. Only one instance ID can be passed in here.
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def ProjectId(self):
        r"""ID of the new project
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    r"""ModifyDBInstancesProject response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of successfully transferred instances
        :type Count: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        r"""Number of successfully transferred instances
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

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
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class ModifyDatabaseOwnerRequest(AbstractModel):
    r"""ModifyDatabaseOwner request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :type DBInstanceId: str
        :param _DatabaseName: Database name. obtain through the api [DescribeDatabases](https://www.tencentcloud.com/document/api/409/43353?from_cn_redirect=1).
        :type DatabaseName: str
        :param _DatabaseOwner: New owner of the database. obtain through the api [DescribeAccounts](https://www.tencentcloud.com/document/api/409/18109?from_cn_redirect=1).
        :type DatabaseOwner: str
        """
        self._DBInstanceId = None
        self._DatabaseName = None
        self._DatabaseOwner = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/api/409/16773?from_cn_redirect=1).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DatabaseName(self):
        r"""Database name. obtain through the api [DescribeDatabases](https://www.tencentcloud.com/document/api/409/43353?from_cn_redirect=1).
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatabaseOwner(self):
        r"""New owner of the database. obtain through the api [DescribeAccounts](https://www.tencentcloud.com/document/api/409/18109?from_cn_redirect=1).
        :rtype: str
        """
        return self._DatabaseOwner

    @DatabaseOwner.setter
    def DatabaseOwner(self, DatabaseOwner):
        self._DatabaseOwner = DatabaseOwner


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._DatabaseName = params.get("DatabaseName")
        self._DatabaseOwner = params.get("DatabaseOwner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseOwnerResponse(AbstractModel):
    r"""ModifyDatabaseOwner response structure.

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


class ModifyMaintainTimeWindowRequest(AbstractModel):
    r"""ModifyMaintainTimeWindow request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _MaintainStartTime: Maintenance start time. time zone is UTC+8.
        :type MaintainStartTime: str
        :param _MaintainDuration: Maintenance duration. unit: hr. value range: [1,4].
        :type MaintainDuration: int
        :param _MaintainWeekDays: Specifies the maintenance period.
        :type MaintainWeekDays: list of str
        """
        self._DBInstanceId = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._MaintainWeekDays = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def MaintainStartTime(self):
        r"""Maintenance start time. time zone is UTC+8.
        :rtype: str
        """
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        r"""Maintenance duration. unit: hr. value range: [1,4].
        :rtype: int
        """
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        r"""Specifies the maintenance period.
        :rtype: list of str
        """
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintainTimeWindowResponse(AbstractModel):
    r"""ModifyMaintainTimeWindow response structure.

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


class ModifyParameterTemplateRequest(AbstractModel):
    r"""ModifyParameterTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Specifies the parameter template ID, which uniquely identifies the parameter template and cannot be modified. it can be obtained through the api [DescribeParameterTemplates](https://www.tencentcloud.com/document/product/409/52651?lang=en).
        :type TemplateId: str
        :param _TemplateName: Parameter template name, which can contain 1-60 letters, digits, and symbols (-_./()[]()+=:@). If this field is empty, the original parameter template name will be used.
        :type TemplateName: str
        :param _TemplateDescription: Parameter template description, which can contain 1-60 letters, digits, and symbols (-_./()[]()+=:@). If this parameter is not passed in, the original parameter template description will be used.
        :type TemplateDescription: str
        :param _ModifyParamEntrySet: The set of parameters to be modified or added. A parameter cannot be put to `ModifyParamEntrySet` and `DeleteParamSet` at the same time, that is, it cannot be modified/added and deleted at the same time.
        :type ModifyParamEntrySet: list of ParamEntry
        :param _DeleteParamSet: The set of parameters to be deleted in the template. A parameter cannot be put to `ModifyParamEntrySet` and `DeleteParamSet` at the same time, that is, it cannot be modified/added and deleted at the same time.
        :type DeleteParamSet: list of str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateDescription = None
        self._ModifyParamEntrySet = None
        self._DeleteParamSet = None

    @property
    def TemplateId(self):
        r"""Specifies the parameter template ID, which uniquely identifies the parameter template and cannot be modified. it can be obtained through the api [DescribeParameterTemplates](https://www.tencentcloud.com/document/product/409/52651?lang=en).
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""Parameter template name, which can contain 1-60 letters, digits, and symbols (-_./()[]()+=:@). If this field is empty, the original parameter template name will be used.
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        r"""Parameter template description, which can contain 1-60 letters, digits, and symbols (-_./()[]()+=:@). If this parameter is not passed in, the original parameter template description will be used.
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def ModifyParamEntrySet(self):
        r"""The set of parameters to be modified or added. A parameter cannot be put to `ModifyParamEntrySet` and `DeleteParamSet` at the same time, that is, it cannot be modified/added and deleted at the same time.
        :rtype: list of ParamEntry
        """
        return self._ModifyParamEntrySet

    @ModifyParamEntrySet.setter
    def ModifyParamEntrySet(self, ModifyParamEntrySet):
        self._ModifyParamEntrySet = ModifyParamEntrySet

    @property
    def DeleteParamSet(self):
        r"""The set of parameters to be deleted in the template. A parameter cannot be put to `ModifyParamEntrySet` and `DeleteParamSet` at the same time, that is, it cannot be modified/added and deleted at the same time.
        :rtype: list of str
        """
        return self._DeleteParamSet

    @DeleteParamSet.setter
    def DeleteParamSet(self, DeleteParamSet):
        self._DeleteParamSet = DeleteParamSet


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateDescription = params.get("TemplateDescription")
        if params.get("ModifyParamEntrySet") is not None:
            self._ModifyParamEntrySet = []
            for item in params.get("ModifyParamEntrySet"):
                obj = ParamEntry()
                obj._deserialize(item)
                self._ModifyParamEntrySet.append(obj)
        self._DeleteParamSet = params.get("DeleteParamSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParameterTemplateResponse(AbstractModel):
    r"""ModifyParameterTemplate response structure.

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


class ModifyPrivilege(AbstractModel):
    r"""Specifies the permissions for modifying a database object, including the data structure of the database object description, the list of permissions required for modification, and the modification type.

    """

    def __init__(self):
        r"""
        :param _DatabasePrivilege: Specifies the database object and permission list to be modified.
        :type DatabasePrivilege: :class:`tencentcloud.postgres.v20170312.models.DatabasePrivilege`
        :param _ModifyType: Modifies via grantObject, revokeObject, or alterRole. grantObject represents authorization, revokeObject represents withdraw, alterRole represents modify account type.
        :type ModifyType: str
        :param _IsCascade: This parameter is required only when ModifyType is revokeObject. when set to true, the permission will be revoked with cascading effect. default false.
        :type IsCascade: bool
        """
        self._DatabasePrivilege = None
        self._ModifyType = None
        self._IsCascade = None

    @property
    def DatabasePrivilege(self):
        r"""Specifies the database object and permission list to be modified.
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DatabasePrivilege`
        """
        return self._DatabasePrivilege

    @DatabasePrivilege.setter
    def DatabasePrivilege(self, DatabasePrivilege):
        self._DatabasePrivilege = DatabasePrivilege

    @property
    def ModifyType(self):
        r"""Modifies via grantObject, revokeObject, or alterRole. grantObject represents authorization, revokeObject represents withdraw, alterRole represents modify account type.
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def IsCascade(self):
        r"""This parameter is required only when ModifyType is revokeObject. when set to true, the permission will be revoked with cascading effect. default false.
        :rtype: bool
        """
        return self._IsCascade

    @IsCascade.setter
    def IsCascade(self, IsCascade):
        self._IsCascade = IsCascade


    def _deserialize(self, params):
        if params.get("DatabasePrivilege") is not None:
            self._DatabasePrivilege = DatabasePrivilege()
            self._DatabasePrivilege._deserialize(params.get("DatabasePrivilege"))
        self._ModifyType = params.get("ModifyType")
        self._IsCascade = params.get("IsCascade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyDBInstanceWeightRequest(AbstractModel):
    r"""ModifyReadOnlyDBInstanceWeight request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: ReadOnlyGroupId. specifies the read-only group ID, which can be obtained through the api [DescribeReadOnlyGroups](https://www.tencentcloud.com/document/product/409/39725?lang=en).
        :type ReadOnlyGroupId: str
        :param _Weight: Specifies the traffic weight of the read-only instance in the read-only group. valid values: 1-50.
        :type Weight: int
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None
        self._Weight = None

    @property
    def DBInstanceId(self):
        r"""Instance ID. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""ReadOnlyGroupId. specifies the read-only group ID, which can be obtained through the api [DescribeReadOnlyGroups](https://www.tencentcloud.com/document/product/409/39725?lang=en).
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def Weight(self):
        r"""Specifies the traffic weight of the read-only instance in the read-only group. valid values: 1-50.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyDBInstanceWeightResponse(AbstractModel):
    r"""ModifyReadOnlyDBInstanceWeight response structure.

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


class ModifyReadOnlyGroupConfigRequest(AbstractModel):
    r"""ModifyReadOnlyGroupConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: RO group ID
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: RO group name
        :type ReadOnlyGroupName: str
        :param _ReplayLagEliminate: Whether to remove a read-only replica from an RO group if the delay between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :type ReplayLagEliminate: int
        :param _ReplayLatencyEliminate: Whether to remove a read-only replica from an RO group if the sync log size difference between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :type ReplayLatencyEliminate: int
        :param _MaxReplayLatency: Delayed log size threshold in MB
        :type MaxReplayLatency: int
        :param _MaxReplayLag: Delay threshold in ms
        :type MaxReplayLag: int
        :param _Rebalance: Whether to enable automatic load balancing. Valid values: `0` (disable), `1` (enable).
        :type Rebalance: int
        :param _MinDelayEliminateReserve: The minimum number of read-only replicas that must be retained in an RO group
        :type MinDelayEliminateReserve: int
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._ReplayLagEliminate = None
        self._ReplayLatencyEliminate = None
        self._MaxReplayLatency = None
        self._MaxReplayLag = None
        self._Rebalance = None
        self._MinDelayEliminateReserve = None

    @property
    def ReadOnlyGroupId(self):
        r"""RO group ID
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""RO group name
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ReplayLagEliminate(self):
        r"""Whether to remove a read-only replica from an RO group if the delay between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._ReplayLagEliminate

    @ReplayLagEliminate.setter
    def ReplayLagEliminate(self, ReplayLagEliminate):
        self._ReplayLagEliminate = ReplayLagEliminate

    @property
    def ReplayLatencyEliminate(self):
        r"""Whether to remove a read-only replica from an RO group if the sync log size difference between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._ReplayLatencyEliminate

    @ReplayLatencyEliminate.setter
    def ReplayLatencyEliminate(self, ReplayLatencyEliminate):
        self._ReplayLatencyEliminate = ReplayLatencyEliminate

    @property
    def MaxReplayLatency(self):
        r"""Delayed log size threshold in MB
        :rtype: int
        """
        return self._MaxReplayLatency

    @MaxReplayLatency.setter
    def MaxReplayLatency(self, MaxReplayLatency):
        self._MaxReplayLatency = MaxReplayLatency

    @property
    def MaxReplayLag(self):
        r"""Delay threshold in ms
        :rtype: int
        """
        return self._MaxReplayLag

    @MaxReplayLag.setter
    def MaxReplayLag(self, MaxReplayLag):
        self._MaxReplayLag = MaxReplayLag

    @property
    def Rebalance(self):
        r"""Whether to enable automatic load balancing. Valid values: `0` (disable), `1` (enable).
        :rtype: int
        """
        return self._Rebalance

    @Rebalance.setter
    def Rebalance(self, Rebalance):
        self._Rebalance = Rebalance

    @property
    def MinDelayEliminateReserve(self):
        r"""The minimum number of read-only replicas that must be retained in an RO group
        :rtype: int
        """
        return self._MinDelayEliminateReserve

    @MinDelayEliminateReserve.setter
    def MinDelayEliminateReserve(self, MinDelayEliminateReserve):
        self._MinDelayEliminateReserve = MinDelayEliminateReserve


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._ReplayLagEliminate = params.get("ReplayLagEliminate")
        self._ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self._MaxReplayLatency = params.get("MaxReplayLatency")
        self._MaxReplayLag = params.get("MaxReplayLag")
        self._Rebalance = params.get("Rebalance")
        self._MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyGroupConfigResponse(AbstractModel):
    r"""ModifyReadOnlyGroupConfig response structure.

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


class ModifySwitchTimePeriodRequest(AbstractModel):
    r"""ModifySwitchTimePeriod request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: The ID of the instance waiting for a switch
        :type DBInstanceId: str
        :param _SwitchTag: Valid value: `0` (switch immediately)
        :type SwitchTag: int
        """
        self._DBInstanceId = None
        self._SwitchTag = None

    @property
    def DBInstanceId(self):
        r"""The ID of the instance waiting for a switch
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def SwitchTag(self):
        r"""Valid value: `0` (switch immediately)
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._SwitchTag = params.get("SwitchTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySwitchTimePeriodResponse(AbstractModel):
    r"""ModifySwitchTimePeriod response structure.

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


class NetworkAccess(AbstractModel):
    r"""Network information. (This parameter structure has been deprecated. Please use `DBInstanceNetInfo` to query network information.)

    """

    def __init__(self):
        r"""
        :param _ResourceId: Network resource id, instance id, or RO group id.
        :type ResourceId: str
        :param _ResourceType: Resource type. valid values: 1 (instance), 2 (RO group).
        :type ResourceType: int
        :param _VpcId: VPC ID. specifies the ID of the virtual private cloud.
        :type VpcId: str
        :param _Vip: IPv4 Address
        :type Vip: str
        :param _Vip6: IPv6 Address
        :type Vip6: str
        :param _Vport: Specifies the access port.
        :type Vport: int
        :param _SubnetId: Subnet ID.
        :type SubnetId: str
        :param _VpcStatus: Network status. valid values: 1-applying, 2-active, 3-deleting, 4-deleted.
        :type VpcStatus: int
        """
        self._ResourceId = None
        self._ResourceType = None
        self._VpcId = None
        self._Vip = None
        self._Vip6 = None
        self._Vport = None
        self._SubnetId = None
        self._VpcStatus = None

    @property
    def ResourceId(self):
        r"""Network resource id, instance id, or RO group id.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""Resource type. valid values: 1 (instance), 2 (RO group).
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def VpcId(self):
        r"""VPC ID. specifies the ID of the virtual private cloud.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Vip(self):
        r"""IPv4 Address
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vip6(self):
        r"""IPv6 Address
        :rtype: str
        """
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def Vport(self):
        r"""Specifies the access port.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def SubnetId(self):
        r"""Subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcStatus(self):
        r"""Network status. valid values: 1-applying, 2-active, 3-deleting, 4-deleted.
        :rtype: int
        """
        return self._VpcStatus

    @VpcStatus.setter
    def VpcStatus(self, VpcStatus):
        self._VpcStatus = VpcStatus


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._VpcId = params.get("VpcId")
        self._Vip = params.get("Vip")
        self._Vip6 = params.get("Vip6")
        self._Vport = params.get("Vport")
        self._SubnetId = params.get("SubnetId")
        self._VpcStatus = params.get("VpcStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalQueryItem(AbstractModel):
    r"""Information of one SlowQuery

    """

    def __init__(self):
        r"""
        :param _UserName: Username
        :type UserName: str
        :param _Calls: Number of calls
        :type Calls: int
        :param _CallsGrids: Granularity
        :type CallsGrids: list of int
        :param _CostTime: Total time consumed
        :type CostTime: float
        :param _Rows: Number of affected rows
        :type Rows: int
        :param _MinCostTime: Minimum time consumed
        :type MinCostTime: float
        :param _MaxCostTime: Maximum time consumed
        :type MaxCostTime: float
        :param _FirstTime: Time of the earliest slow SQL statement
        :type FirstTime: str
        :param _LastTime: Time of the latest slow SQL statement
        :type LastTime: str
        :param _SharedReadBlks: Shared memory blocks for reads
        :type SharedReadBlks: int
        :param _SharedWriteBlks: Shared memory blocks for writes
        :type SharedWriteBlks: int
        :param _ReadCostTime: Total IO read time
        :type ReadCostTime: int
        :param _WriteCostTime: Total IO write time
        :type WriteCostTime: int
        :param _DatabaseName: Database name
        :type DatabaseName: str
        :param _NormalQuery: Slow SQL statement after desensitization
        :type NormalQuery: str
        """
        self._UserName = None
        self._Calls = None
        self._CallsGrids = None
        self._CostTime = None
        self._Rows = None
        self._MinCostTime = None
        self._MaxCostTime = None
        self._FirstTime = None
        self._LastTime = None
        self._SharedReadBlks = None
        self._SharedWriteBlks = None
        self._ReadCostTime = None
        self._WriteCostTime = None
        self._DatabaseName = None
        self._NormalQuery = None

    @property
    def UserName(self):
        r"""Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Calls(self):
        r"""Number of calls
        :rtype: int
        """
        return self._Calls

    @Calls.setter
    def Calls(self, Calls):
        self._Calls = Calls

    @property
    def CallsGrids(self):
        r"""Granularity
        :rtype: list of int
        """
        return self._CallsGrids

    @CallsGrids.setter
    def CallsGrids(self, CallsGrids):
        self._CallsGrids = CallsGrids

    @property
    def CostTime(self):
        r"""Total time consumed
        :rtype: float
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def Rows(self):
        r"""Number of affected rows
        :rtype: int
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def MinCostTime(self):
        r"""Minimum time consumed
        :rtype: float
        """
        return self._MinCostTime

    @MinCostTime.setter
    def MinCostTime(self, MinCostTime):
        self._MinCostTime = MinCostTime

    @property
    def MaxCostTime(self):
        r"""Maximum time consumed
        :rtype: float
        """
        return self._MaxCostTime

    @MaxCostTime.setter
    def MaxCostTime(self, MaxCostTime):
        self._MaxCostTime = MaxCostTime

    @property
    def FirstTime(self):
        r"""Time of the earliest slow SQL statement
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def LastTime(self):
        r"""Time of the latest slow SQL statement
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def SharedReadBlks(self):
        r"""Shared memory blocks for reads
        :rtype: int
        """
        return self._SharedReadBlks

    @SharedReadBlks.setter
    def SharedReadBlks(self, SharedReadBlks):
        self._SharedReadBlks = SharedReadBlks

    @property
    def SharedWriteBlks(self):
        r"""Shared memory blocks for writes
        :rtype: int
        """
        return self._SharedWriteBlks

    @SharedWriteBlks.setter
    def SharedWriteBlks(self, SharedWriteBlks):
        self._SharedWriteBlks = SharedWriteBlks

    @property
    def ReadCostTime(self):
        r"""Total IO read time
        :rtype: int
        """
        return self._ReadCostTime

    @ReadCostTime.setter
    def ReadCostTime(self, ReadCostTime):
        self._ReadCostTime = ReadCostTime

    @property
    def WriteCostTime(self):
        r"""Total IO write time
        :rtype: int
        """
        return self._WriteCostTime

    @WriteCostTime.setter
    def WriteCostTime(self, WriteCostTime):
        self._WriteCostTime = WriteCostTime

    @property
    def DatabaseName(self):
        r"""Database name
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def NormalQuery(self):
        r"""Slow SQL statement after desensitization
        :rtype: str
        """
        return self._NormalQuery

    @NormalQuery.setter
    def NormalQuery(self, NormalQuery):
        self._NormalQuery = NormalQuery


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Calls = params.get("Calls")
        self._CallsGrids = params.get("CallsGrids")
        self._CostTime = params.get("CostTime")
        self._Rows = params.get("Rows")
        self._MinCostTime = params.get("MinCostTime")
        self._MaxCostTime = params.get("MaxCostTime")
        self._FirstTime = params.get("FirstTime")
        self._LastTime = params.get("LastTime")
        self._SharedReadBlks = params.get("SharedReadBlks")
        self._SharedWriteBlks = params.get("SharedWriteBlks")
        self._ReadCostTime = params.get("ReadCostTime")
        self._WriteCostTime = params.get("WriteCostTime")
        self._DatabaseName = params.get("DatabaseName")
        self._NormalQuery = params.get("NormalQuery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessRequest(AbstractModel):
    r"""OpenDBExtranetAccess request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Specifies the instance ID, such as postgres-hez4fh0v. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :type DBInstanceId: str
        :param _IsIpv6: Specifies whether to enable public network Ipv6. valid values: 1 (yes), 0 (no).
Default value: 0
        :type IsIpv6: int
        """
        self._DBInstanceId = None
        self._IsIpv6 = None

    @property
    def DBInstanceId(self):
        r"""Specifies the instance ID, such as postgres-hez4fh0v. obtain through the api [DescribeDBInstances](https://www.tencentcloud.com/document/product/409/16773?lang=en).
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def IsIpv6(self):
        r"""Specifies whether to enable public network Ipv6. valid values: 1 (yes), 0 (no).
Default value: 0
        :rtype: int
        """
        return self._IsIpv6

    @IsIpv6.setter
    def IsIpv6(self, IsIpv6):
        self._IsIpv6 = IsIpv6


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._IsIpv6 = params.get("IsIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessResponse(AbstractModel):
    r"""OpenDBExtranetAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID. FlowId is equivalent to TaskId.
        :type FlowId: int
        :param _TaskId: Task ID.
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Process ID. FlowId is equivalent to TaskId.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        r"""Task ID.
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
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class OpenServerlessDBExtranetAccessRequest(AbstractModel):
    r"""OpenServerlessDBExtranetAccess request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Unique ID of an instance
        :type DBInstanceId: str
        :param _DBInstanceName: Instance name
        :type DBInstanceName: str
        """
        self._DBInstanceId = None
        self._DBInstanceName = None

    @property
    def DBInstanceId(self):
        r"""Unique ID of an instance
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DBInstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._DBInstanceName

    @DBInstanceName.setter
    def DBInstanceName(self, DBInstanceName):
        self._DBInstanceName = DBInstanceName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._DBInstanceName = params.get("DBInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenServerlessDBExtranetAccessResponse(AbstractModel):
    r"""OpenServerlessDBExtranetAccess response structure.

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


class ParamEntry(AbstractModel):
    r"""Parameters to be modified in batches

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name
        :type Name: str
        :param _ExpectedValue: The new value to which the parameter will be modified. When this parameter is used as an input parameter, its value must be a string, such as `0.1` (decimal), `1000` (integer), and `replica` (enum).
        :type ExpectedValue: str
        """
        self._Name = None
        self._ExpectedValue = None

    @property
    def Name(self):
        r"""Parameter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ExpectedValue(self):
        r"""The new value to which the parameter will be modified. When this parameter is used as an input parameter, its value must be a string, such as `0.1` (decimal), `1000` (integer), and `replica` (enum).
        :rtype: str
        """
        return self._ExpectedValue

    @ExpectedValue.setter
    def ExpectedValue(self, ExpectedValue):
        self._ExpectedValue = ExpectedValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ExpectedValue = params.get("ExpectedValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    r"""Parameter details

    """

    def __init__(self):
        r"""
        :param _ID: Parameter ID
        :type ID: int
        :param _Name: Parameter name.
        :type Name: str
        :param _ParamValueType: Parameter value type: integer, real, bool, enum, mutil_enum.
When the parameter type is integer or real (floating-point), the value range is determined based on the Max and Min of the return value. 
When the parameter type is boolean, the valid values are true or false. 
When the parameter type is enum (enumeration type) or mutil_enum (multi-enum type), the valid values are determined by EnumValue in the return value.
        :type ParamValueType: str
        :param _Unit: Parameter value unit. returns null if the parameter has no units.
        :type Unit: str
        :param _DefaultValue: Default parameter value. returns in string form.
        :type DefaultValue: str
        :param _CurrentValue: Specifies the current value in string form.
        :type CurrentValue: str
        :param _Max: Specifies the numerical type (integer, real) parameter and its lower bound.
        :type Max: float
        :param _EnumValue: Value range of the enum parameter
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EnumValue: list of str
        :param _Min: Numerical type (integer, real) parameter specifies the upper bound.
        :type Min: float
        :param _ParamDescriptionCH: Chinese description.
        :type ParamDescriptionCH: str
        :param _ParamDescriptionEN: Specifies the english description of the parameter.
        :type ParamDescriptionEN: str
        :param _NeedReboot: Specifies whether a restart is required for parameter modification (true indicates required, false indicates not required).
        :type NeedReboot: bool
        :param _ClassificationCN: Parameter chinese category.
        :type ClassificationCN: str
        :param _ClassificationEN: Parameter english category.
        :type ClassificationEN: str
        :param _SpecRelated: Specifies whether it is related to the specification (true for related, false for unrelated).
        :type SpecRelated: bool
        :param _Advanced: Indicates whether it is a key parameter (true means it is a key parameter, modification requires special attention and may affect instance performance).
        :type Advanced: bool
        :param _LastModifyTime: Specifies the last modified time.
        :type LastModifyTime: str
        :param _StandbyRelated: Parameter primary-secondary constraints. `0`: no constraint between primary and standby. `1`: standby parameter value > primary machine parameter value. `2`: primary parameter value must be greater than that of the standby machine.
        :type StandbyRelated: int
        :param _VersionRelationSet: Parameter version association information, containing detailed parameter information for the respective kernel version
Note: This field may return null, indicating that no valid values can be obtained.
        :type VersionRelationSet: list of ParamVersionRelation
        :param _SpecRelationSet: Parameter specification association information, containing detailed parameter information for the respective specification
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecRelationSet: list of ParamSpecRelation
        """
        self._ID = None
        self._Name = None
        self._ParamValueType = None
        self._Unit = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Max = None
        self._EnumValue = None
        self._Min = None
        self._ParamDescriptionCH = None
        self._ParamDescriptionEN = None
        self._NeedReboot = None
        self._ClassificationCN = None
        self._ClassificationEN = None
        self._SpecRelated = None
        self._Advanced = None
        self._LastModifyTime = None
        self._StandbyRelated = None
        self._VersionRelationSet = None
        self._SpecRelationSet = None

    @property
    def ID(self):
        r"""Parameter ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamValueType(self):
        r"""Parameter value type: integer, real, bool, enum, mutil_enum.
When the parameter type is integer or real (floating-point), the value range is determined based on the Max and Min of the return value. 
When the parameter type is boolean, the valid values are true or false. 
When the parameter type is enum (enumeration type) or mutil_enum (multi-enum type), the valid values are determined by EnumValue in the return value.
        :rtype: str
        """
        return self._ParamValueType

    @ParamValueType.setter
    def ParamValueType(self, ParamValueType):
        self._ParamValueType = ParamValueType

    @property
    def Unit(self):
        r"""Parameter value unit. returns null if the parameter has no units.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def DefaultValue(self):
        r"""Default parameter value. returns in string form.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        r"""Specifies the current value in string form.
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Max(self):
        r"""Specifies the numerical type (integer, real) parameter and its lower bound.
        :rtype: float
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def EnumValue(self):
        r"""Value range of the enum parameter
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Min(self):
        r"""Numerical type (integer, real) parameter specifies the upper bound.
        :rtype: float
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ParamDescriptionCH(self):
        r"""Chinese description.
        :rtype: str
        """
        return self._ParamDescriptionCH

    @ParamDescriptionCH.setter
    def ParamDescriptionCH(self, ParamDescriptionCH):
        self._ParamDescriptionCH = ParamDescriptionCH

    @property
    def ParamDescriptionEN(self):
        r"""Specifies the english description of the parameter.
        :rtype: str
        """
        return self._ParamDescriptionEN

    @ParamDescriptionEN.setter
    def ParamDescriptionEN(self, ParamDescriptionEN):
        self._ParamDescriptionEN = ParamDescriptionEN

    @property
    def NeedReboot(self):
        r"""Specifies whether a restart is required for parameter modification (true indicates required, false indicates not required).
        :rtype: bool
        """
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def ClassificationCN(self):
        r"""Parameter chinese category.
        :rtype: str
        """
        return self._ClassificationCN

    @ClassificationCN.setter
    def ClassificationCN(self, ClassificationCN):
        self._ClassificationCN = ClassificationCN

    @property
    def ClassificationEN(self):
        r"""Parameter english category.
        :rtype: str
        """
        return self._ClassificationEN

    @ClassificationEN.setter
    def ClassificationEN(self, ClassificationEN):
        self._ClassificationEN = ClassificationEN

    @property
    def SpecRelated(self):
        r"""Specifies whether it is related to the specification (true for related, false for unrelated).
        :rtype: bool
        """
        return self._SpecRelated

    @SpecRelated.setter
    def SpecRelated(self, SpecRelated):
        self._SpecRelated = SpecRelated

    @property
    def Advanced(self):
        r"""Indicates whether it is a key parameter (true means it is a key parameter, modification requires special attention and may affect instance performance).
        :rtype: bool
        """
        return self._Advanced

    @Advanced.setter
    def Advanced(self, Advanced):
        self._Advanced = Advanced

    @property
    def LastModifyTime(self):
        r"""Specifies the last modified time.
        :rtype: str
        """
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def StandbyRelated(self):
        r"""Parameter primary-secondary constraints. `0`: no constraint between primary and standby. `1`: standby parameter value > primary machine parameter value. `2`: primary parameter value must be greater than that of the standby machine.
        :rtype: int
        """
        return self._StandbyRelated

    @StandbyRelated.setter
    def StandbyRelated(self, StandbyRelated):
        self._StandbyRelated = StandbyRelated

    @property
    def VersionRelationSet(self):
        r"""Parameter version association information, containing detailed parameter information for the respective kernel version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ParamVersionRelation
        """
        return self._VersionRelationSet

    @VersionRelationSet.setter
    def VersionRelationSet(self, VersionRelationSet):
        self._VersionRelationSet = VersionRelationSet

    @property
    def SpecRelationSet(self):
        r"""Parameter specification association information, containing detailed parameter information for the respective specification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ParamSpecRelation
        """
        return self._SpecRelationSet

    @SpecRelationSet.setter
    def SpecRelationSet(self, SpecRelationSet):
        self._SpecRelationSet = SpecRelationSet


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._ParamValueType = params.get("ParamValueType")
        self._Unit = params.get("Unit")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Max = params.get("Max")
        self._EnumValue = params.get("EnumValue")
        self._Min = params.get("Min")
        self._ParamDescriptionCH = params.get("ParamDescriptionCH")
        self._ParamDescriptionEN = params.get("ParamDescriptionEN")
        self._NeedReboot = params.get("NeedReboot")
        self._ClassificationCN = params.get("ClassificationCN")
        self._ClassificationEN = params.get("ClassificationEN")
        self._SpecRelated = params.get("SpecRelated")
        self._Advanced = params.get("Advanced")
        self._LastModifyTime = params.get("LastModifyTime")
        self._StandbyRelated = params.get("StandbyRelated")
        if params.get("VersionRelationSet") is not None:
            self._VersionRelationSet = []
            for item in params.get("VersionRelationSet"):
                obj = ParamVersionRelation()
                obj._deserialize(item)
                self._VersionRelationSet.append(obj)
        if params.get("SpecRelationSet") is not None:
            self._SpecRelationSet = []
            for item in params.get("SpecRelationSet"):
                obj = ParamSpecRelation()
                obj._deserialize(item)
                self._SpecRelationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamSpecRelation(AbstractModel):
    r"""Parameter information for each specification

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name.
        :type Name: str
        :param _Memory: Parameter information belonging to specification.
        :type Memory: str
        :param _Value: Default value of the parameter for this specification.
        :type Value: str
        :param _Unit: Parameter value unit. returns null if the parameter has no units.
        :type Unit: str
        :param _Max: Numerical type (integer, real) parameter specifies the upper bound.
        :type Max: float
        :param _Min: Specifies the numerical type (integer, real) parameter and its lower bound.
        :type Min: float
        :param _EnumValue: Value range of the enum parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnumValue: list of str
        """
        self._Name = None
        self._Memory = None
        self._Value = None
        self._Unit = None
        self._Max = None
        self._Min = None
        self._EnumValue = None

    @property
    def Name(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Memory(self):
        r"""Parameter information belonging to specification.
        :rtype: str
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Value(self):
        r"""Default value of the parameter for this specification.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Unit(self):
        r"""Parameter value unit. returns null if the parameter has no units.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Max(self):
        r"""Numerical type (integer, real) parameter specifies the upper bound.
        :rtype: float
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        r"""Specifies the numerical type (integer, real) parameter and its lower bound.
        :rtype: float
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        r"""Value range of the enum parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Memory = params.get("Memory")
        self._Value = params.get("Value")
        self._Unit = params.get("Unit")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamVersionRelation(AbstractModel):
    r"""Parameter information for each version

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name.
        :type Name: str
        :param _DBKernelVersion: Parameter information belonging to kernel version.
        :type DBKernelVersion: str
        :param _Value: Default value of the parameter for this version and specification.
        :type Value: str
        :param _Unit: Parameter value unit. returns null if the parameter has no units.
        :type Unit: str
        :param _Max: Numerical type (integer, real) parameter specifies the upper bound.
        :type Max: float
        :param _Min: Specifies the numerical type (integer, real) parameter and its lower bound.
        :type Min: float
        :param _EnumValue: Value range of the enum parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnumValue: list of str
        """
        self._Name = None
        self._DBKernelVersion = None
        self._Value = None
        self._Unit = None
        self._Max = None
        self._Min = None
        self._EnumValue = None

    @property
    def Name(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DBKernelVersion(self):
        r"""Parameter information belonging to kernel version.
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def Value(self):
        r"""Default value of the parameter for this version and specification.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Unit(self):
        r"""Parameter value unit. returns null if the parameter has no units.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Max(self):
        r"""Numerical type (integer, real) parameter specifies the upper bound.
        :rtype: float
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        r"""Specifies the numerical type (integer, real) parameter and its lower bound.
        :rtype: float
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        r"""Value range of the enum parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._Value = params.get("Value")
        self._Unit = params.get("Unit")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterTemplate(AbstractModel):
    r"""Basic information of a parameter template

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID
        :type TemplateId: str
        :param _TemplateName: Parameter template name
        :type TemplateName: str
        :param _DBMajorVersion: Database version applicable to a parameter template
        :type DBMajorVersion: str
        :param _DBEngine: Database engine applicable to a parameter template
        :type DBEngine: str
        :param _TemplateDescription: Parameter template description
        :type TemplateDescription: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._DBMajorVersion = None
        self._DBEngine = None
        self._TemplateDescription = None

    @property
    def TemplateId(self):
        r"""Parameter template ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""Parameter template name
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def DBMajorVersion(self):
        r"""Database version applicable to a parameter template
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBEngine(self):
        r"""Database engine applicable to a parameter template
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def TemplateDescription(self):
        r"""Parameter template description
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBEngine = params.get("DBEngine")
        self._TemplateDescription = params.get("TemplateDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PgDeal(AbstractModel):
    r"""Order details

    """

    def __init__(self):
        r"""
        :param _DealName: Order name
        :type DealName: str
        :param _OwnerUin: User
        :type OwnerUin: str
        :param _Count: Number of instances involved in order
        :type Count: int
        :param _PayMode: Billing mode. 0: pay-as-you-go
        :type PayMode: int
        :param _FlowId: Async task flow ID
        :type FlowId: int
        :param _DBInstanceIdSet: Instance ID array
        :type DBInstanceIdSet: list of str
        """
        self._DealName = None
        self._OwnerUin = None
        self._Count = None
        self._PayMode = None
        self._FlowId = None
        self._DBInstanceIdSet = None

    @property
    def DealName(self):
        r"""Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def OwnerUin(self):
        r"""User
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Count(self):
        r"""Number of instances involved in order
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def PayMode(self):
        r"""Billing mode. 0: pay-as-you-go
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def FlowId(self):
        r"""Async task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DBInstanceIdSet(self):
        r"""Instance ID array
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._OwnerUin = params.get("OwnerUin")
        self._Count = params.get("Count")
        self._PayMode = params.get("PayMode")
        self._FlowId = params.get("FlowId")
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyRule(AbstractModel):
    r"""Rule information for security group

    """

    def __init__(self):
        r"""
        :param _Action: Policy, Valid values: `ACCEPT`, `DROP`.
        :type Action: str
        :param _CidrIp: Source or destination IP or IP range, such as 172.16.0.0/12.
        :type CidrIp: str
        :param _PortRange: Port
        :type PortRange: str
        :param _IpProtocol: Network protocol. UDP and TCP are supported.
        :type IpProtocol: str
        :param _Description: The rule description
        :type Description: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Description = None

    @property
    def Action(self):
        r"""Policy, Valid values: `ACCEPT`, `DROP`.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        r"""Source or destination IP or IP range, such as 172.16.0.0/12.
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        r"""Port
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        r"""Network protocol. UDP and TCP are supported.
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Description(self):
        r"""The rule description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawSlowQuery(AbstractModel):
    r"""The list of slow query details returned by the `DescribeSlowQueryList` API

    """

    def __init__(self):
        r"""
        :param _RawQuery: Slow query statement
        :type RawQuery: str
        :param _DatabaseName: The database queried by the slow query statement
        :type DatabaseName: str
        :param _Duration: The execution time of the slow query statement
        :type Duration: float
        :param _ClientAddr: The client that executes the slow query statement
        :type ClientAddr: str
        :param _UserName: The name of the user who executes the slow query statement
        :type UserName: str
        :param _SessionStartTime: The time when the slow query statement starts to execute
        :type SessionStartTime: str
        """
        self._RawQuery = None
        self._DatabaseName = None
        self._Duration = None
        self._ClientAddr = None
        self._UserName = None
        self._SessionStartTime = None

    @property
    def RawQuery(self):
        r"""Slow query statement
        :rtype: str
        """
        return self._RawQuery

    @RawQuery.setter
    def RawQuery(self, RawQuery):
        self._RawQuery = RawQuery

    @property
    def DatabaseName(self):
        r"""The database queried by the slow query statement
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Duration(self):
        r"""The execution time of the slow query statement
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ClientAddr(self):
        r"""The client that executes the slow query statement
        :rtype: str
        """
        return self._ClientAddr

    @ClientAddr.setter
    def ClientAddr(self, ClientAddr):
        self._ClientAddr = ClientAddr

    @property
    def UserName(self):
        r"""The name of the user who executes the slow query statement
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def SessionStartTime(self):
        r"""The time when the slow query statement starts to execute
        :rtype: str
        """
        return self._SessionStartTime

    @SessionStartTime.setter
    def SessionStartTime(self, SessionStartTime):
        self._SessionStartTime = SessionStartTime


    def _deserialize(self, params):
        self._RawQuery = params.get("RawQuery")
        self._DatabaseName = params.get("DatabaseName")
        self._Duration = params.get("Duration")
        self._ClientAddr = params.get("ClientAddr")
        self._UserName = params.get("UserName")
        self._SessionStartTime = params.get("SessionStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyGroup(AbstractModel):
    r"""RO group information

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: RO group identifier
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: RO group name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReadOnlyGroupName: str
        :param _ProjectId: Project ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _MasterDBInstanceId: Primary instance ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MasterDBInstanceId: str
        :param _MinDelayEliminateReserve: The minimum number of read-only replicas that must be retained in an RO group
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MinDelayEliminateReserve: int
        :param _MaxReplayLatency: Delayed log size threshold
        :type MaxReplayLatency: int
        :param _ReplayLatencyEliminate: Whether to remove a read-only replica from an RO group if the sync log size difference between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :type ReplayLatencyEliminate: int
        :param _MaxReplayLag: Delay threshold
        :type MaxReplayLag: float
        :param _ReplayLagEliminate: Whether to remove a read-only replica from an RO group if the delay between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :type ReplayLagEliminate: int
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _Region: Region ID
        :type Region: str
        :param _Zone: Availability zone ID
        :type Zone: str
        :param _Status: Status
        :type Status: str
        :param _ReadOnlyDBInstanceList: Instance details
        :type ReadOnlyDBInstanceList: list of DBInstance
        :param _Rebalance: Whether to enable automatic load balancing
        :type Rebalance: int
        :param _DBInstanceNetInfo: Network information
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        :param _NetworkAccessList: Network access list of the RO group (this field has been deprecated)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type NetworkAccessList: list of NetworkAccess
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._ProjectId = None
        self._MasterDBInstanceId = None
        self._MinDelayEliminateReserve = None
        self._MaxReplayLatency = None
        self._ReplayLatencyEliminate = None
        self._MaxReplayLag = None
        self._ReplayLagEliminate = None
        self._VpcId = None
        self._SubnetId = None
        self._Region = None
        self._Zone = None
        self._Status = None
        self._ReadOnlyDBInstanceList = None
        self._Rebalance = None
        self._DBInstanceNetInfo = None
        self._NetworkAccessList = None

    @property
    def ReadOnlyGroupId(self):
        r"""RO group identifier
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""RO group name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ProjectId(self):
        r"""Project ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def MasterDBInstanceId(self):
        r"""Primary instance ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MasterDBInstanceId

    @MasterDBInstanceId.setter
    def MasterDBInstanceId(self, MasterDBInstanceId):
        self._MasterDBInstanceId = MasterDBInstanceId

    @property
    def MinDelayEliminateReserve(self):
        r"""The minimum number of read-only replicas that must be retained in an RO group
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MinDelayEliminateReserve

    @MinDelayEliminateReserve.setter
    def MinDelayEliminateReserve(self, MinDelayEliminateReserve):
        self._MinDelayEliminateReserve = MinDelayEliminateReserve

    @property
    def MaxReplayLatency(self):
        r"""Delayed log size threshold
        :rtype: int
        """
        return self._MaxReplayLatency

    @MaxReplayLatency.setter
    def MaxReplayLatency(self, MaxReplayLatency):
        self._MaxReplayLatency = MaxReplayLatency

    @property
    def ReplayLatencyEliminate(self):
        r"""Whether to remove a read-only replica from an RO group if the sync log size difference between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._ReplayLatencyEliminate

    @ReplayLatencyEliminate.setter
    def ReplayLatencyEliminate(self, ReplayLatencyEliminate):
        self._ReplayLatencyEliminate = ReplayLatencyEliminate

    @property
    def MaxReplayLag(self):
        r"""Delay threshold
        :rtype: float
        """
        return self._MaxReplayLag

    @MaxReplayLag.setter
    def MaxReplayLag(self, MaxReplayLag):
        self._MaxReplayLag = MaxReplayLag

    @property
    def ReplayLagEliminate(self):
        r"""Whether to remove a read-only replica from an RO group if the delay between the read-only replica and the primary instance exceeds the threshold. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._ReplayLagEliminate

    @ReplayLagEliminate.setter
    def ReplayLagEliminate(self, ReplayLagEliminate):
        self._ReplayLagEliminate = ReplayLagEliminate

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Region(self):
        r"""Region ID
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""Availability zone ID
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        r"""Status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReadOnlyDBInstanceList(self):
        r"""Instance details
        :rtype: list of DBInstance
        """
        return self._ReadOnlyDBInstanceList

    @ReadOnlyDBInstanceList.setter
    def ReadOnlyDBInstanceList(self, ReadOnlyDBInstanceList):
        self._ReadOnlyDBInstanceList = ReadOnlyDBInstanceList

    @property
    def Rebalance(self):
        r"""Whether to enable automatic load balancing
        :rtype: int
        """
        return self._Rebalance

    @Rebalance.setter
    def Rebalance(self, Rebalance):
        self._Rebalance = Rebalance

    @property
    def DBInstanceNetInfo(self):
        r"""Network information
        :rtype: list of DBInstanceNetInfo
        """
        return self._DBInstanceNetInfo

    @DBInstanceNetInfo.setter
    def DBInstanceNetInfo(self, DBInstanceNetInfo):
        self._DBInstanceNetInfo = DBInstanceNetInfo

    @property
    def NetworkAccessList(self):
        r"""Network access list of the RO group (this field has been deprecated)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of NetworkAccess
        """
        return self._NetworkAccessList

    @NetworkAccessList.setter
    def NetworkAccessList(self, NetworkAccessList):
        self._NetworkAccessList = NetworkAccessList


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._ProjectId = params.get("ProjectId")
        self._MasterDBInstanceId = params.get("MasterDBInstanceId")
        self._MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        self._MaxReplayLatency = params.get("MaxReplayLatency")
        self._ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self._MaxReplayLag = params.get("MaxReplayLag")
        self._ReplayLagEliminate = params.get("ReplayLagEliminate")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        if params.get("ReadOnlyDBInstanceList") is not None:
            self._ReadOnlyDBInstanceList = []
            for item in params.get("ReadOnlyDBInstanceList"):
                obj = DBInstance()
                obj._deserialize(item)
                self._ReadOnlyDBInstanceList.append(obj)
        self._Rebalance = params.get("Rebalance")
        if params.get("DBInstanceNetInfo") is not None:
            self._DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self._DBInstanceNetInfo.append(obj)
        if params.get("NetworkAccessList") is not None:
            self._NetworkAccessList = []
            for item in params.get("NetworkAccessList"):
                obj = NetworkAccess()
                obj._deserialize(item)
                self._NetworkAccessList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebalanceReadOnlyGroupRequest(AbstractModel):
    r"""RebalanceReadOnlyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: RO group ID
        :type ReadOnlyGroupId: str
        """
        self._ReadOnlyGroupId = None

    @property
    def ReadOnlyGroupId(self):
        r"""RO group ID
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebalanceReadOnlyGroupResponse(AbstractModel):
    r"""RebalanceReadOnlyGroup response structure.

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


class RegionInfo(AbstractModel):
    r"""Region information such as number and status

    """

    def __init__(self):
        r"""
        :param _Region: Region abbreviation
        :type Region: str
        :param _RegionName: Region name
        :type RegionName: str
        :param _RegionId: Region number
        :type RegionId: int
        :param _RegionState: Availability status. UNAVAILABLE: unavailable, AVAILABLE: available
        :type RegionState: str
        :param _SupportInternational: Whether the resource can be purchased in this region. Valid values: `0` (no), `1` (yes).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SupportInternational: int
        """
        self._Region = None
        self._RegionName = None
        self._RegionId = None
        self._RegionState = None
        self._SupportInternational = None

    @property
    def Region(self):
        r"""Region abbreviation
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        r"""Region name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        r"""Region number
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionState(self):
        r"""Availability status. UNAVAILABLE: unavailable, AVAILABLE: available
        :rtype: str
        """
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState

    @property
    def SupportInternational(self):
        r"""Whether the resource can be purchased in this region. Valid values: `0` (no), `1` (yes).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SupportInternational

    @SupportInternational.setter
    def SupportInternational(self, SupportInternational):
        self._SupportInternational = SupportInternational


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._RegionState = params.get("RegionState")
        self._SupportInternational = params.get("SupportInternational")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDBInstanceFromReadOnlyGroupRequest(AbstractModel):
    r"""RemoveDBInstanceFromReadOnlyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _ReadOnlyGroupId: RO group ID
        :type ReadOnlyGroupId: str
        """
        self._DBInstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""RO group ID
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDBInstanceFromReadOnlyGroupResponse(AbstractModel):
    r"""RemoveDBInstanceFromReadOnlyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task ID
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


class RenewInstanceRequest(AbstractModel):
    r"""RenewInstance request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of `postgres-6fego161`
        :type DBInstanceId: str
        :param _Period: Renewal duration in months
        :type Period: int
        :param _AutoVoucher: Whether to automatically use vouchers. 1: yes, 0: no. Default value: 0
        :type AutoVoucher: int
        :param _VoucherIds: Voucher ID list (only one voucher can be specified currently)
        :type VoucherIds: list of str
        """
        self._DBInstanceId = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of `postgres-6fego161`
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Period(self):
        r"""Renewal duration in months
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use vouchers. 1: yes, 0: no. Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID list (only one voucher can be specified currently)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    r"""RenewInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order name
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    r"""ResetAccountPassword request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of postgres-4wdeb0zv
        :type DBInstanceId: str
        :param _UserName: Instance account name
        :type UserName: str
        :param _Password: New password corresponding to `UserName` account
        :type Password: str
        """
        self._DBInstanceId = None
        self._UserName = None
        self._Password = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-4wdeb0zv
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""Instance account name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""New password corresponding to `UserName` account
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    r"""ResetAccountPassword response structure.

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


class RestartDBInstanceRequest(AbstractModel):
    r"""RestartDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID in the format of postgres-6r233v55
        :type DBInstanceId: str
        """
        self._DBInstanceId = None

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-6r233v55
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstanceResponse(AbstractModel):
    r"""RestartDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Async flow ID
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


class RestoreDBInstanceObjectsRequest(AbstractModel):
    r"""RestoreDBInstanceObjects request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID.
        :type DBInstanceId: str
        :param _RestoreObjects: List of objects to be restored. If the object to be restored is named test, the restored name will be `test_bak_${LinuxTime}`. `${LinuxTime}` cannot be specified and is set by the system based on the Linux time at task initiation.
        :type RestoreObjects: list of str
        :param _BackupSetId: Backup set used for recovery. Either `BackupSetId` or `RestoreTargetTime` must be provided, and only one can be passed.
        :type BackupSetId: str
        :param _RestoreTargetTime: Recovery target time, Beijing Time (UTC+8). Either `BackupSetId` or `RestoreTargetTime` must be provided, and only one can be passed.
        :type RestoreTargetTime: str
        """
        self._DBInstanceId = None
        self._RestoreObjects = None
        self._BackupSetId = None
        self._RestoreTargetTime = None

    @property
    def DBInstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def RestoreObjects(self):
        r"""List of objects to be restored. If the object to be restored is named test, the restored name will be `test_bak_${LinuxTime}`. `${LinuxTime}` cannot be specified and is set by the system based on the Linux time at task initiation.
        :rtype: list of str
        """
        return self._RestoreObjects

    @RestoreObjects.setter
    def RestoreObjects(self, RestoreObjects):
        self._RestoreObjects = RestoreObjects

    @property
    def BackupSetId(self):
        r"""Backup set used for recovery. Either `BackupSetId` or `RestoreTargetTime` must be provided, and only one can be passed.
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def RestoreTargetTime(self):
        r"""Recovery target time, Beijing Time (UTC+8). Either `BackupSetId` or `RestoreTargetTime` must be provided, and only one can be passed.
        :rtype: str
        """
        return self._RestoreTargetTime

    @RestoreTargetTime.setter
    def RestoreTargetTime(self, RestoreTargetTime):
        self._RestoreTargetTime = RestoreTargetTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._RestoreObjects = params.get("RestoreObjects")
        self._BackupSetId = params.get("BackupSetId")
        self._RestoreTargetTime = params.get("RestoreTargetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreDBInstanceObjectsResponse(AbstractModel):
    r"""RestoreDBInstanceObjects response structure.

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


class SecurityGroup(AbstractModel):
    r"""Security group information

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Inbound: Inbound rule
        :type Inbound: list of PolicyRule
        :param _Outbound: Outbound rule
        :type Outbound: list of PolicyRule
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param _SecurityGroupDescription: Security group remarks
        :type SecurityGroupDescription: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._Inbound = None
        self._Outbound = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupDescription = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def Inbound(self):
        r"""Inbound rule
        :rtype: list of PolicyRule
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        r"""Outbound rule
        :rtype: list of PolicyRule
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def SecurityGroupId(self):
        r"""Security group ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        r"""Security group name
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupDescription(self):
        r"""Security group remarks
        :rtype: str
        """
        return self._SecurityGroupDescription

    @SecurityGroupDescription.setter
    def SecurityGroupDescription(self, SecurityGroupDescription):
        self._SecurityGroupDescription = SecurityGroupDescription


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self._Outbound.append(obj)
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupDescription = params.get("SecurityGroupDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessDBAccount(AbstractModel):
    r"""PostgreSQL for Serverless instance account description

    """

    def __init__(self):
        r"""
        :param _DBUser: Username
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBUser: str
        :param _DBPassword: Password
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBPassword: str
        :param _DBConnLimit: The maximum number of connections
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBConnLimit: int
        """
        self._DBUser = None
        self._DBPassword = None
        self._DBConnLimit = None

    @property
    def DBUser(self):
        r"""Username
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBUser

    @DBUser.setter
    def DBUser(self, DBUser):
        self._DBUser = DBUser

    @property
    def DBPassword(self):
        r"""Password
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBPassword

    @DBPassword.setter
    def DBPassword(self, DBPassword):
        self._DBPassword = DBPassword

    @property
    def DBConnLimit(self):
        r"""The maximum number of connections
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DBConnLimit

    @DBConnLimit.setter
    def DBConnLimit(self, DBConnLimit):
        self._DBConnLimit = DBConnLimit


    def _deserialize(self, params):
        self._DBUser = params.get("DBUser")
        self._DBPassword = params.get("DBPassword")
        self._DBConnLimit = params.get("DBConnLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessDBInstance(AbstractModel):
    r"""PostgreSQL for Serverless instance description

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID, which is the unique identifier
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBInstanceId: str
        :param _DBInstanceName: Instance name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBInstanceName: str
        :param _DBInstanceStatus: Instance status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBInstanceStatus: str
        :param _Region: Region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zone: Availability zone
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Zone: str
        :param _ProjectId: Project ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _VpcId: VPC ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _DBCharset: Character set
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBCharset: str
        :param _DBVersion: Database version
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBVersion: str
        :param _CreateTime: Creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _DBInstanceNetInfo: Instance network information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBInstanceNetInfo: list of ServerlessDBInstanceNetInfo
        :param _DBAccountSet: Instance account information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBAccountSet: list of ServerlessDBAccount
        :param _DBDatabaseList: Information of the databases in an instance
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBDatabaseList: list of str
        :param _TagList: The array of tags bound to an instance
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagList: list of Tag
        :param _DBKernelVersion: Database kernel version
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBKernelVersion: str
        :param _DBMajorVersion: Database major version number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DBMajorVersion: str
        """
        self._DBInstanceId = None
        self._DBInstanceName = None
        self._DBInstanceStatus = None
        self._Region = None
        self._Zone = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._DBCharset = None
        self._DBVersion = None
        self._CreateTime = None
        self._DBInstanceNetInfo = None
        self._DBAccountSet = None
        self._DBDatabaseList = None
        self._TagList = None
        self._DBKernelVersion = None
        self._DBMajorVersion = None

    @property
    def DBInstanceId(self):
        r"""Instance ID, which is the unique identifier
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def DBInstanceName(self):
        r"""Instance name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBInstanceName

    @DBInstanceName.setter
    def DBInstanceName(self, DBInstanceName):
        self._DBInstanceName = DBInstanceName

    @property
    def DBInstanceStatus(self):
        r"""Instance status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBInstanceStatus

    @DBInstanceStatus.setter
    def DBInstanceStatus(self, DBInstanceStatus):
        self._DBInstanceStatus = DBInstanceStatus

    @property
    def Region(self):
        r"""Region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""Availability zone
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        r"""Project ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        r"""VPC ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DBCharset(self):
        r"""Character set
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBCharset

    @DBCharset.setter
    def DBCharset(self, DBCharset):
        self._DBCharset = DBCharset

    @property
    def DBVersion(self):
        r"""Database version
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def CreateTime(self):
        r"""Creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DBInstanceNetInfo(self):
        r"""Instance network information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of ServerlessDBInstanceNetInfo
        """
        return self._DBInstanceNetInfo

    @DBInstanceNetInfo.setter
    def DBInstanceNetInfo(self, DBInstanceNetInfo):
        self._DBInstanceNetInfo = DBInstanceNetInfo

    @property
    def DBAccountSet(self):
        r"""Instance account information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of ServerlessDBAccount
        """
        return self._DBAccountSet

    @DBAccountSet.setter
    def DBAccountSet(self, DBAccountSet):
        self._DBAccountSet = DBAccountSet

    @property
    def DBDatabaseList(self):
        r"""Information of the databases in an instance
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DBDatabaseList

    @DBDatabaseList.setter
    def DBDatabaseList(self, DBDatabaseList):
        self._DBDatabaseList = DBDatabaseList

    @property
    def TagList(self):
        r"""The array of tags bound to an instance
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def DBKernelVersion(self):
        r"""Database kernel version
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def DBMajorVersion(self):
        r"""Database major version number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._DBInstanceName = params.get("DBInstanceName")
        self._DBInstanceStatus = params.get("DBInstanceStatus")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DBCharset = params.get("DBCharset")
        self._DBVersion = params.get("DBVersion")
        self._CreateTime = params.get("CreateTime")
        if params.get("DBInstanceNetInfo") is not None:
            self._DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = ServerlessDBInstanceNetInfo()
                obj._deserialize(item)
                self._DBInstanceNetInfo.append(obj)
        if params.get("DBAccountSet") is not None:
            self._DBAccountSet = []
            for item in params.get("DBAccountSet"):
                obj = ServerlessDBAccount()
                obj._deserialize(item)
                self._DBAccountSet.append(obj)
        self._DBDatabaseList = params.get("DBDatabaseList")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._DBMajorVersion = params.get("DBMajorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessDBInstanceNetInfo(AbstractModel):
    r"""PostgreSQL for Serverless instance network description

    """

    def __init__(self):
        r"""
        :param _Address: Address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Address: str
        :param _Ip: IP address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ip: str
        :param _Port: Port number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Port: int
        :param _Status: Status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Status: str
        :param _NetType: Network type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type NetType: str
        """
        self._Address = None
        self._Ip = None
        self._Port = None
        self._Status = None
        self._NetType = None

    @property
    def Address(self):
        r"""Address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Ip(self):
        r"""IP address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Port number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        r"""Status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NetType(self):
        r"""Network type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        self._NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewFlagRequest(AbstractModel):
    r"""SetAutoRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceIdSet: List of instance IDs. Note that currently you cannot manipulate multiple instances at the same time. Only one instance ID can be passed in here.
        :type DBInstanceIdSet: list of str
        :param _AutoRenewFlag: Renewal flag. 0: normal renewal, 1: auto-renewal, 2: no renewal upon expiration
        :type AutoRenewFlag: int
        """
        self._DBInstanceIdSet = None
        self._AutoRenewFlag = None

    @property
    def DBInstanceIdSet(self):
        r"""List of instance IDs. Note that currently you cannot manipulate multiple instances at the same time. Only one instance ID can be passed in here.
        :rtype: list of str
        """
        return self._DBInstanceIdSet

    @DBInstanceIdSet.setter
    def DBInstanceIdSet(self, DBInstanceIdSet):
        self._DBInstanceIdSet = DBInstanceIdSet

    @property
    def AutoRenewFlag(self):
        r"""Renewal flag. 0: normal renewal, 1: auto-renewal, 2: no renewal upon expiration
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._DBInstanceIdSet = params.get("DBInstanceIdSet")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewFlagResponse(AbstractModel):
    r"""SetAutoRenewFlag response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of successfully set instances
        :type Count: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        r"""Number of successfully set instances
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

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
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class SlowlogDetail(AbstractModel):
    r"""Slow query details

    """

    def __init__(self):
        r"""
        :param _TotalTime: Total time consumed
        :type TotalTime: float
        :param _TotalCalls: Total number of calls
        :type TotalCalls: int
        :param _NormalQueries: List of slow SQL statements after desensitization
        :type NormalQueries: list of NormalQueryItem
        """
        self._TotalTime = None
        self._TotalCalls = None
        self._NormalQueries = None

    @property
    def TotalTime(self):
        r"""Total time consumed
        :rtype: float
        """
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def TotalCalls(self):
        r"""Total number of calls
        :rtype: int
        """
        return self._TotalCalls

    @TotalCalls.setter
    def TotalCalls(self, TotalCalls):
        self._TotalCalls = TotalCalls

    @property
    def NormalQueries(self):
        r"""List of slow SQL statements after desensitization
        :rtype: list of NormalQueryItem
        """
        return self._NormalQueries

    @NormalQueries.setter
    def NormalQueries(self, NormalQueries):
        self._NormalQueries = NormalQueries


    def _deserialize(self, params):
        self._TotalTime = params.get("TotalTime")
        self._TotalCalls = params.get("TotalCalls")
        if params.get("NormalQueries") is not None:
            self._NormalQueries = []
            for item in params.get("NormalQueries"):
                obj = NormalQueryItem()
                obj._deserialize(item)
                self._NormalQueries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecInfo(AbstractModel):
    r"""Purchasable specification details in an AZ in a region.

    """

    def __init__(self):
        r"""
        :param _Region: Region abbreviation, which corresponds to the `Region` field of `RegionSet`
        :type Region: str
        :param _Zone: AZ abbreviate, which corresponds to the `Zone` field of `ZoneSet`
        :type Zone: str
        :param _SpecItemInfoList: Specification details list
        :type SpecItemInfoList: list of SpecItemInfo
        :param _SupportKMSRegions: Regions where KMS is supported
Note: This field may return `null`, indicating that no valid value was found.
        :type SupportKMSRegions: list of str
        """
        self._Region = None
        self._Zone = None
        self._SpecItemInfoList = None
        self._SupportKMSRegions = None

    @property
    def Region(self):
        r"""Region abbreviation, which corresponds to the `Region` field of `RegionSet`
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""AZ abbreviate, which corresponds to the `Zone` field of `ZoneSet`
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecItemInfoList(self):
        r"""Specification details list
        :rtype: list of SpecItemInfo
        """
        return self._SpecItemInfoList

    @SpecItemInfoList.setter
    def SpecItemInfoList(self, SpecItemInfoList):
        self._SpecItemInfoList = SpecItemInfoList

    @property
    def SupportKMSRegions(self):
        r"""Regions where KMS is supported
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of str
        """
        return self._SupportKMSRegions

    @SupportKMSRegions.setter
    def SupportKMSRegions(self, SupportKMSRegions):
        self._SupportKMSRegions = SupportKMSRegions


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        if params.get("SpecItemInfoList") is not None:
            self._SpecItemInfoList = []
            for item in params.get("SpecItemInfoList"):
                obj = SpecItemInfo()
                obj._deserialize(item)
                self._SpecItemInfoList.append(obj)
        self._SupportKMSRegions = params.get("SupportKMSRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecItemInfo(AbstractModel):
    r"""Specification description

    """

    def __init__(self):
        r"""
        :param _SpecCode: Specification ID
        :type SpecCode: str
        :param _Version: PostgerSQL version number
        :type Version: str
        :param _VersionName: Full version name corresponding to kernel number
        :type VersionName: str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Memory: Memory size in MB
        :type Memory: int
        :param _MaxStorage: Maximum storage capacity in GB supported by this specification
        :type MaxStorage: int
        :param _MinStorage: Minimum storage capacity in GB supported by this specification
        :type MinStorage: int
        :param _Qps: Estimated QPS for this specification
        :type Qps: int
        :param _Pid: (Disused)
        :type Pid: int
        :param _Type: Machine type
        :type Type: str
        :param _MajorVersion: PostgreSQL major version number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MajorVersion: str
        :param _KernelVersion: PostgreSQL kernel version number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type KernelVersion: str
        :param _IsSupportTDE: Whether TDE data encryption is supported. Valid values: 0 (no), 1 (yes)
Note: This field may return `null`, indicating that no valid value was found.
        :type IsSupportTDE: int
        """
        self._SpecCode = None
        self._Version = None
        self._VersionName = None
        self._Cpu = None
        self._Memory = None
        self._MaxStorage = None
        self._MinStorage = None
        self._Qps = None
        self._Pid = None
        self._Type = None
        self._MajorVersion = None
        self._KernelVersion = None
        self._IsSupportTDE = None

    @property
    def SpecCode(self):
        r"""Specification ID
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Version(self):
        r"""PostgerSQL version number
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def VersionName(self):
        r"""Full version name corresponding to kernel number
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Cpu(self):
        r"""Number of CPU cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""Memory size in MB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def MaxStorage(self):
        r"""Maximum storage capacity in GB supported by this specification
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def MinStorage(self):
        r"""Minimum storage capacity in GB supported by this specification
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def Qps(self):
        r"""Estimated QPS for this specification
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Pid(self):
        r"""(Disused)
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Type(self):
        r"""Machine type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MajorVersion(self):
        r"""PostgreSQL major version number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MajorVersion

    @MajorVersion.setter
    def MajorVersion(self, MajorVersion):
        self._MajorVersion = MajorVersion

    @property
    def KernelVersion(self):
        r"""PostgreSQL kernel version number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KernelVersion

    @KernelVersion.setter
    def KernelVersion(self, KernelVersion):
        self._KernelVersion = KernelVersion

    @property
    def IsSupportTDE(self):
        r"""Whether TDE data encryption is supported. Valid values: 0 (no), 1 (yes)
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._IsSupportTDE

    @IsSupportTDE.setter
    def IsSupportTDE(self, IsSupportTDE):
        self._IsSupportTDE = IsSupportTDE


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._Version = params.get("Version")
        self._VersionName = params.get("VersionName")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._MaxStorage = params.get("MaxStorage")
        self._MinStorage = params.get("MinStorage")
        self._Qps = params.get("Qps")
        self._Pid = params.get("Pid")
        self._Type = params.get("Type")
        self._MajorVersion = params.get("MajorVersion")
        self._KernelVersion = params.get("KernelVersion")
        self._IsSupportTDE = params.get("IsSupportTDE")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstancePrimaryRequest(AbstractModel):
    r"""SwitchDBInstancePrimary request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _Force: Whether to perform forced switch. As long as the standby node can be accessed, the switch will be performed regardless of the primary-standby sync delay. You can switch immediately only when `SwitchTag` is `0.
<li>Default: `false`.
        :type Force: bool
        :param _SwitchTag: Switch time for the specified instance after configuration modification.
<li>`0`: Switch now. 
<li>`1`: Switch at the specified time.
<li>`2`: Switch in the maintenance time.
<li>Default value: `0`. 
        :type SwitchTag: int
        :param _SwitchStartTime: The earliest time to start a switch in the format of "HH:MM:SS", such as "01:00:00". This parameter is invalid when `SwitchTag` is `0` or `2`.
        :type SwitchStartTime: str
        :param _SwitchEndTime: The latest time to start a switch in the format of "HH:MM:SS", such as "01:30:00". This parameter is invalid when `SwitchTag` is `0` or `2`. The difference between `SwitchStartTime` and `SwitchEndTime` cannot be less than 30 minutes.
        :type SwitchEndTime: str
        """
        self._DBInstanceId = None
        self._Force = None
        self._SwitchTag = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def Force(self):
        r"""Whether to perform forced switch. As long as the standby node can be accessed, the switch will be performed regardless of the primary-standby sync delay. You can switch immediately only when `SwitchTag` is `0.
<li>Default: `false`.
        :rtype: bool
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def SwitchTag(self):
        r"""Switch time for the specified instance after configuration modification.
<li>`0`: Switch now. 
<li>`1`: Switch at the specified time.
<li>`2`: Switch in the maintenance time.
<li>Default value: `0`. 
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchStartTime(self):
        r"""The earliest time to start a switch in the format of "HH:MM:SS", such as "01:00:00". This parameter is invalid when `SwitchTag` is `0` or `2`.
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        r"""The latest time to start a switch in the format of "HH:MM:SS", such as "01:30:00". This parameter is invalid when `SwitchTag` is `0` or `2`. The difference between `SwitchStartTime` and `SwitchEndTime` cannot be less than 30 minutes.
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._Force = params.get("Force")
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstancePrimaryResponse(AbstractModel):
    r"""SwitchDBInstancePrimary response structure.

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


class Tag(AbstractModel):
    r"""The information of tags associated with instances, including `TagKey` and `TagValue`

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
        


class TaskDetail(AbstractModel):
    r"""Task details.

    """

    def __init__(self):
        r"""
        :param _CurrentStep: Current task step name.
        :type CurrentStep: str
        :param _AllSteps: Describes the step description of the current task you own.
        :type AllSteps: str
        :param _Input: Input of the task.
        :type Input: str
        :param _Output: Output parameter of the task.
        :type Output: str
        :param _SwitchTag: Specifies the switch time after instance configurations are modified. default value: 0.
This task does not require switching.
Switch immediately.
2: switch at specified time.
3: switch during maintenance time window.
        :type SwitchTag: int
        :param _SwitchTime: Specifies the switch time.
        :type SwitchTime: str
        :param _Message: Note of the task.
        :type Message: str
        """
        self._CurrentStep = None
        self._AllSteps = None
        self._Input = None
        self._Output = None
        self._SwitchTag = None
        self._SwitchTime = None
        self._Message = None

    @property
    def CurrentStep(self):
        r"""Current task step name.
        :rtype: str
        """
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def AllSteps(self):
        r"""Describes the step description of the current task you own.
        :rtype: str
        """
        return self._AllSteps

    @AllSteps.setter
    def AllSteps(self, AllSteps):
        self._AllSteps = AllSteps

    @property
    def Input(self):
        r"""Input of the task.
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        r"""Output parameter of the task.
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def SwitchTag(self):
        r"""Specifies the switch time after instance configurations are modified. default value: 0.
This task does not require switching.
Switch immediately.
2: switch at specified time.
3: switch during maintenance time window.
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchTime(self):
        r"""Specifies the switch time.
        :rtype: str
        """
        return self._SwitchTime

    @SwitchTime.setter
    def SwitchTime(self, SwitchTime):
        self._SwitchTime = SwitchTime

    @property
    def Message(self):
        r"""Note of the task.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._CurrentStep = params.get("CurrentStep")
        self._AllSteps = params.get("AllSteps")
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchTime = params.get("SwitchTime")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSet(AbstractModel):
    r"""Task list information

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: int
        :param _TaskType: Specifies the task type.
        :type TaskType: str
        :param _DBInstanceId: Specifies the instance ID of the task instance.
        :type DBInstanceId: str
        :param _StartTime: Start time of the task.
        :type StartTime: str
        :param _EndTime: Task end time.
        :type EndTime: str
        :param _Status: Specifies the task Running status, including Running, Success, WaitSwitch, Fail, Pause.
        :type Status: str
        :param _Progress: Indicates the progress of task execution, with a value range of 0-100.
        :type Progress: int
        :param _TaskDetail: Specifies the task details.
        :type TaskDetail: :class:`tencentcloud.postgres.v20170312.models.TaskDetail`
        """
        self._TaskId = None
        self._TaskType = None
        self._DBInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Progress = None
        self._TaskDetail = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        r"""Specifies the task type.
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def DBInstanceId(self):
        r"""Specifies the instance ID of the task instance.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def StartTime(self):
        r"""Start time of the task.
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
    def Status(self):
        r"""Specifies the task Running status, including Running, Success, WaitSwitch, Fail, Pause.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        r"""Indicates the progress of task execution, with a value range of 0-100.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskDetail(self):
        r"""Specifies the task details.
        :rtype: :class:`tencentcloud.postgres.v20170312.models.TaskDetail`
        """
        return self._TaskDetail

    @TaskDetail.setter
    def TaskDetail(self, TaskDetail):
        self._TaskDetail = TaskDetail


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._DBInstanceId = params.get("DBInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        if params.get("TaskDetail") is not None:
            self._TaskDetail = TaskDetail()
            self._TaskDetail._deserialize(params.get("TaskDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlockAccountRequest(AbstractModel):
    r"""UnlockAccount request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID.		
        :type DBInstanceId: str
        :param _UserName: Account name.
        :type UserName: str
        """
        self._DBInstanceId = None
        self._UserName = None

    @property
    def DBInstanceId(self):
        r"""Instance ID.		
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def UserName(self):
        r"""Account name.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlockAccountResponse(AbstractModel):
    r"""UnlockAccount response structure.

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


class UpgradeDBInstanceKernelVersionRequest(AbstractModel):
    r"""UpgradeDBInstanceKernelVersion request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param _TargetDBKernelVersion: Target kernel version, which can be obtained in the `AvailableUpgradeTarget` field in the returned value of the [DescribeDBVersions](https://intl.cloud.tencent.com/document/api/409/89018?from_cn_redirect=1) API.

        :type TargetDBKernelVersion: str
        :param _SwitchTag: Switch time after the kernel version upgrade for the specified instance. Valid values:
<li>`0`: Switch now.
<li>`1`: Switch at the specified time.
<li>`2`: Switch in the maintenance time.
Default value: `0`. 
        :type SwitchTag: int
        :param _SwitchStartTime: Switch start time in the format of `HH:MM:SS`, such as 01:00:00. When `SwitchTag` is `0` or `2`, this parameter is invalid.
        :type SwitchStartTime: str
        :param _SwitchEndTime: Switch end time in the format of `HH:MM:SS`, such as 01:30:00. When `SwitchTag` is `0` or `2`, this parameter is invalid. The difference between `SwitchStartTime` and `SwitchEndTime` cannot be less than 30 minutes.
        :type SwitchEndTime: str
        :param _DryRun: Whether to perform a pre-check on the current operation of upgrading the instance kernel version. Valid values:
u200c<li>u200c`true`: Performs a pre-check without upgrading the kernel version. Check items include request parameters, kernel version compatibility, and instance parameters.
u200cu200c<li>`false`: Sends a normal request and upgrades the kernel version directly after the check is passed.
Default value: `false`.
        :type DryRun: bool
        """
        self._DBInstanceId = None
        self._TargetDBKernelVersion = None
        self._SwitchTag = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None
        self._DryRun = None

    @property
    def DBInstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def TargetDBKernelVersion(self):
        r"""Target kernel version, which can be obtained in the `AvailableUpgradeTarget` field in the returned value of the [DescribeDBVersions](https://intl.cloud.tencent.com/document/api/409/89018?from_cn_redirect=1) API.

        :rtype: str
        """
        return self._TargetDBKernelVersion

    @TargetDBKernelVersion.setter
    def TargetDBKernelVersion(self, TargetDBKernelVersion):
        self._TargetDBKernelVersion = TargetDBKernelVersion

    @property
    def SwitchTag(self):
        r"""Switch time after the kernel version upgrade for the specified instance. Valid values:
<li>`0`: Switch now.
<li>`1`: Switch at the specified time.
<li>`2`: Switch in the maintenance time.
Default value: `0`. 
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchStartTime(self):
        r"""Switch start time in the format of `HH:MM:SS`, such as 01:00:00. When `SwitchTag` is `0` or `2`, this parameter is invalid.
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        r"""Switch end time in the format of `HH:MM:SS`, such as 01:30:00. When `SwitchTag` is `0` or `2`, this parameter is invalid. The difference between `SwitchStartTime` and `SwitchEndTime` cannot be less than 30 minutes.
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime

    @property
    def DryRun(self):
        r"""Whether to perform a pre-check on the current operation of upgrading the instance kernel version. Valid values:
u200c<li>u200c`true`: Performs a pre-check without upgrading the kernel version. Check items include request parameters, kernel version compatibility, and instance parameters.
u200cu200c<li>`false`: Sends a normal request and upgrades the kernel version directly after the check is passed.
Default value: `false`.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._TargetDBKernelVersion = params.get("TargetDBKernelVersion")
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceKernelVersionResponse(AbstractModel):
    r"""UpgradeDBInstanceKernelVersion response structure.

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


class UpgradeDBInstanceMajorVersionRequest(AbstractModel):
    r"""UpgradeDBInstanceMajorVersion request structure.

    """

    def __init__(self):
        r"""
        :param _DBInstanceId: Instance ID.
        :type DBInstanceId: str
        :param _TargetDBKernelVersion: Target kernel version number, where upgradeable target kernel version numbers can be acquired through API DescribeDBVersions.
        :type TargetDBKernelVersion: str
        :param _UpgradeCheck: Whether it is verification mode: if UpgradeCheck is True, it means only kernel version compatibility check will be conducted, without actual upgrade operations, and there will be no affect on the original instance. The check results can be viewed through the upgrade logs.
        :type UpgradeCheck: bool
        :param _BackupBeforeUpgrade: Pre-upgrade backup option: True means a full backup is required before upgrade, and False means a full backup is not required before upgrade. If there is an existing backup set that can restore the instance to its pre-upgrade state, False can be selected; otherwise, True should be specified. This parameter is invalid when UpgradeCheck is True.
        :type BackupBeforeUpgrade: bool
        :param _StatisticsRefreshOption: Statistics collection option, which is used to run ANALYZE on the primary instance to update system statistics after the upgrade. Valid values include:
0: No statistics collection required;
1: Collect statistics before instance recovery write;
3: Collect statistics after instance recovery write.
This parameter is invalid when UpgradeCheck is True.
        :type StatisticsRefreshOption: int
        :param _ExtensionUpgradeOption: Plugin upgrade option. pg_upgrade does not upgrade any plugins, and "ALTER EXTENSION UPDATE" needs to be executed on the database where the plugins were created after the upgrade. When initiating a major version upgrade of an instance, you can specify whether the upgrade task automatically upgrades the plugin version before/after the instance recovery write. Valid values include:
0: No automatic plugin upgrade required;
1: Upgrade plugins before recovery write;
2: Upgrade plugins after recovery write.
This parameter is invalid when UpgradeCheck is True.
        :type ExtensionUpgradeOption: int
        :param _UpgradeTimeOption: Upgrade time option. During the upgrade process, there will be a period when the instance is read-only, and there will be a second-level flash disconnection. When initiating an upgrade, you need to choose the time window for this impact. Valid values include:
0: Execute automatically, no specific time window required;
1: Specify the time window for this upgrade task, which is set via UpgradeTimeBegin and UpgradeTimeEnd parameters;
2: Execute during the instance operation and maintenance time window.
This parameter is invalid when UpgradeCheck is True.
        :type UpgradeTimeOption: int
        :param _UpgradeTimeBegin: Upgrade window start time, and the time format is HH:MM:SS, for example: 01:00:00. This parameter is valid when UpgradeTimeOption is set to `1`.
This parameter is invalid when UpgradeCheck is True.
        :type UpgradeTimeBegin: str
        :param _UpgradeTimeEnd: Upgrade window end time, and the time format is HH:MM:SS, for example: 2:00:00 AM. This parameter is valid when UpgradeTimeOption is set to `1`.
This parameter is invalid when UpgradeCheck is True.
        :type UpgradeTimeEnd: str
        """
        self._DBInstanceId = None
        self._TargetDBKernelVersion = None
        self._UpgradeCheck = None
        self._BackupBeforeUpgrade = None
        self._StatisticsRefreshOption = None
        self._ExtensionUpgradeOption = None
        self._UpgradeTimeOption = None
        self._UpgradeTimeBegin = None
        self._UpgradeTimeEnd = None

    @property
    def DBInstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def TargetDBKernelVersion(self):
        r"""Target kernel version number, where upgradeable target kernel version numbers can be acquired through API DescribeDBVersions.
        :rtype: str
        """
        return self._TargetDBKernelVersion

    @TargetDBKernelVersion.setter
    def TargetDBKernelVersion(self, TargetDBKernelVersion):
        self._TargetDBKernelVersion = TargetDBKernelVersion

    @property
    def UpgradeCheck(self):
        r"""Whether it is verification mode: if UpgradeCheck is True, it means only kernel version compatibility check will be conducted, without actual upgrade operations, and there will be no affect on the original instance. The check results can be viewed through the upgrade logs.
        :rtype: bool
        """
        return self._UpgradeCheck

    @UpgradeCheck.setter
    def UpgradeCheck(self, UpgradeCheck):
        self._UpgradeCheck = UpgradeCheck

    @property
    def BackupBeforeUpgrade(self):
        r"""Pre-upgrade backup option: True means a full backup is required before upgrade, and False means a full backup is not required before upgrade. If there is an existing backup set that can restore the instance to its pre-upgrade state, False can be selected; otherwise, True should be specified. This parameter is invalid when UpgradeCheck is True.
        :rtype: bool
        """
        return self._BackupBeforeUpgrade

    @BackupBeforeUpgrade.setter
    def BackupBeforeUpgrade(self, BackupBeforeUpgrade):
        self._BackupBeforeUpgrade = BackupBeforeUpgrade

    @property
    def StatisticsRefreshOption(self):
        r"""Statistics collection option, which is used to run ANALYZE on the primary instance to update system statistics after the upgrade. Valid values include:
0: No statistics collection required;
1: Collect statistics before instance recovery write;
3: Collect statistics after instance recovery write.
This parameter is invalid when UpgradeCheck is True.
        :rtype: int
        """
        return self._StatisticsRefreshOption

    @StatisticsRefreshOption.setter
    def StatisticsRefreshOption(self, StatisticsRefreshOption):
        self._StatisticsRefreshOption = StatisticsRefreshOption

    @property
    def ExtensionUpgradeOption(self):
        r"""Plugin upgrade option. pg_upgrade does not upgrade any plugins, and "ALTER EXTENSION UPDATE" needs to be executed on the database where the plugins were created after the upgrade. When initiating a major version upgrade of an instance, you can specify whether the upgrade task automatically upgrades the plugin version before/after the instance recovery write. Valid values include:
0: No automatic plugin upgrade required;
1: Upgrade plugins before recovery write;
2: Upgrade plugins after recovery write.
This parameter is invalid when UpgradeCheck is True.
        :rtype: int
        """
        return self._ExtensionUpgradeOption

    @ExtensionUpgradeOption.setter
    def ExtensionUpgradeOption(self, ExtensionUpgradeOption):
        self._ExtensionUpgradeOption = ExtensionUpgradeOption

    @property
    def UpgradeTimeOption(self):
        r"""Upgrade time option. During the upgrade process, there will be a period when the instance is read-only, and there will be a second-level flash disconnection. When initiating an upgrade, you need to choose the time window for this impact. Valid values include:
0: Execute automatically, no specific time window required;
1: Specify the time window for this upgrade task, which is set via UpgradeTimeBegin and UpgradeTimeEnd parameters;
2: Execute during the instance operation and maintenance time window.
This parameter is invalid when UpgradeCheck is True.
        :rtype: int
        """
        return self._UpgradeTimeOption

    @UpgradeTimeOption.setter
    def UpgradeTimeOption(self, UpgradeTimeOption):
        self._UpgradeTimeOption = UpgradeTimeOption

    @property
    def UpgradeTimeBegin(self):
        r"""Upgrade window start time, and the time format is HH:MM:SS, for example: 01:00:00. This parameter is valid when UpgradeTimeOption is set to `1`.
This parameter is invalid when UpgradeCheck is True.
        :rtype: str
        """
        return self._UpgradeTimeBegin

    @UpgradeTimeBegin.setter
    def UpgradeTimeBegin(self, UpgradeTimeBegin):
        self._UpgradeTimeBegin = UpgradeTimeBegin

    @property
    def UpgradeTimeEnd(self):
        r"""Upgrade window end time, and the time format is HH:MM:SS, for example: 2:00:00 AM. This parameter is valid when UpgradeTimeOption is set to `1`.
This parameter is invalid when UpgradeCheck is True.
        :rtype: str
        """
        return self._UpgradeTimeEnd

    @UpgradeTimeEnd.setter
    def UpgradeTimeEnd(self, UpgradeTimeEnd):
        self._UpgradeTimeEnd = UpgradeTimeEnd


    def _deserialize(self, params):
        self._DBInstanceId = params.get("DBInstanceId")
        self._TargetDBKernelVersion = params.get("TargetDBKernelVersion")
        self._UpgradeCheck = params.get("UpgradeCheck")
        self._BackupBeforeUpgrade = params.get("BackupBeforeUpgrade")
        self._StatisticsRefreshOption = params.get("StatisticsRefreshOption")
        self._ExtensionUpgradeOption = params.get("ExtensionUpgradeOption")
        self._UpgradeTimeOption = params.get("UpgradeTimeOption")
        self._UpgradeTimeBegin = params.get("UpgradeTimeBegin")
        self._UpgradeTimeEnd = params.get("UpgradeTimeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceMajorVersionResponse(AbstractModel):
    r"""UpgradeDBInstanceMajorVersion response structure.

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


class UpgradeDBInstanceRequest(AbstractModel):
    r"""UpgradeDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Memory: Instance memory size in GB after upgrade
        :type Memory: int
        :param _Storage: Instance disk size in GB after upgrade
        :type Storage: int
        :param _DBInstanceId: Instance ID in the format of postgres-lnp6j617
        :type DBInstanceId: str
        :param _AutoVoucher: Whether to automatically use vouchers. 1: yes, 0: no. Default value: no
        :type AutoVoucher: int
        :param _VoucherIds: Voucher ID list (only one voucher can be specified currently)
        :type VoucherIds: list of str
        :param _ActivityId: Activity ID
        :type ActivityId: int
        :param _SwitchTag: Switch time after instance configurations are modified. Valid values: `0` (switch immediately), `1` (switch at specified time). Default value: `0`
        :type SwitchTag: int
        :param _SwitchStartTime: The earliest time to start a switch
        :type SwitchStartTime: str
        :param _SwitchEndTime: The latest time to start a switch
        :type SwitchEndTime: str
        """
        self._Memory = None
        self._Storage = None
        self._DBInstanceId = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ActivityId = None
        self._SwitchTag = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None

    @property
    def Memory(self):
        r"""Instance memory size in GB after upgrade
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Instance disk size in GB after upgrade
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def DBInstanceId(self):
        r"""Instance ID in the format of postgres-lnp6j617
        :rtype: str
        """
        return self._DBInstanceId

    @DBInstanceId.setter
    def DBInstanceId(self, DBInstanceId):
        self._DBInstanceId = DBInstanceId

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use vouchers. 1: yes, 0: no. Default value: no
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID list (only one voucher can be specified currently)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ActivityId(self):
        r"""Activity ID
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def SwitchTag(self):
        r"""Switch time after instance configurations are modified. Valid values: `0` (switch immediately), `1` (switch at specified time). Default value: `0`
        :rtype: int
        """
        return self._SwitchTag

    @SwitchTag.setter
    def SwitchTag(self, SwitchTag):
        self._SwitchTag = SwitchTag

    @property
    def SwitchStartTime(self):
        r"""The earliest time to start a switch
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        r"""The latest time to start a switch
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._DBInstanceId = params.get("DBInstanceId")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._ActivityId = params.get("ActivityId")
        self._SwitchTag = params.get("SwitchTag")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceResponse(AbstractModel):
    r"""UpgradeDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Transaction name.
        :type DealName: str
        :param _BillId: Bill ID of frozen fees
        :type BillId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._BillId = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Transaction name.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def BillId(self):
        r"""Bill ID of frozen fees
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

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
        self._DealName = params.get("DealName")
        self._BillId = params.get("BillId")
        self._RequestId = params.get("RequestId")


class Version(AbstractModel):
    r"""Database version information

    """

    def __init__(self):
        r"""
        :param _DBEngine: Database engines. Valid values:
1. `postgresql` (TencentDB for PostgreSQL)
2. `mssql_compatible` (MSSQL compatible-TencentDB for PostgreSQL)
        :type DBEngine: str
        :param _DBVersion: Database version, such as 12.4.
        :type DBVersion: str
        :param _DBMajorVersion: Database major version, such as 12.
        :type DBMajorVersion: str
        :param _DBKernelVersion: Database kernel version, such as v12.4_r1.3.
        :type DBKernelVersion: str
        :param _SupportedFeatureNames: List of features supported by the database kernel, such as:
TDE: Supports data encryption.
        :type SupportedFeatureNames: list of str
        :param _Status: Database version status. Valid values:
`AVAILABLE`.
`DEPRECATED`.
        :type Status: str
        :param _AvailableUpgradeTarget: List of versions to which this database version (`DBKernelVersion`) can be upgraded, including minor and major version numbers available for upgrade (complete kernel version format example: v15.1_v1.6).
        :type AvailableUpgradeTarget: list of str
        """
        self._DBEngine = None
        self._DBVersion = None
        self._DBMajorVersion = None
        self._DBKernelVersion = None
        self._SupportedFeatureNames = None
        self._Status = None
        self._AvailableUpgradeTarget = None

    @property
    def DBEngine(self):
        r"""Database engines. Valid values:
1. `postgresql` (TencentDB for PostgreSQL)
2. `mssql_compatible` (MSSQL compatible-TencentDB for PostgreSQL)
        :rtype: str
        """
        return self._DBEngine

    @DBEngine.setter
    def DBEngine(self, DBEngine):
        self._DBEngine = DBEngine

    @property
    def DBVersion(self):
        r"""Database version, such as 12.4.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def DBMajorVersion(self):
        r"""Database major version, such as 12.
        :rtype: str
        """
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBKernelVersion(self):
        r"""Database kernel version, such as v12.4_r1.3.
        :rtype: str
        """
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def SupportedFeatureNames(self):
        r"""List of features supported by the database kernel, such as:
TDE: Supports data encryption.
        :rtype: list of str
        """
        return self._SupportedFeatureNames

    @SupportedFeatureNames.setter
    def SupportedFeatureNames(self, SupportedFeatureNames):
        self._SupportedFeatureNames = SupportedFeatureNames

    @property
    def Status(self):
        r"""Database version status. Valid values:
`AVAILABLE`.
`DEPRECATED`.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AvailableUpgradeTarget(self):
        r"""List of versions to which this database version (`DBKernelVersion`) can be upgraded, including minor and major version numbers available for upgrade (complete kernel version format example: v15.1_v1.6).
        :rtype: list of str
        """
        return self._AvailableUpgradeTarget

    @AvailableUpgradeTarget.setter
    def AvailableUpgradeTarget(self, AvailableUpgradeTarget):
        self._AvailableUpgradeTarget = AvailableUpgradeTarget


    def _deserialize(self, params):
        self._DBEngine = params.get("DBEngine")
        self._DBVersion = params.get("DBVersion")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._SupportedFeatureNames = params.get("SupportedFeatureNames")
        self._Status = params.get("Status")
        self._AvailableUpgradeTarget = params.get("AvailableUpgradeTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Xlog(AbstractModel):
    r"""Database Xlog information

    """

    def __init__(self):
        r"""
        :param _Id: Unique backup file ID
        :type Id: int
        :param _StartTime: File generation start time
        :type StartTime: str
        :param _EndTime: File generation end time
        :type EndTime: str
        :param _InternalAddr: Download address on private network
        :type InternalAddr: str
        :param _ExternalAddr: Download address on public network
        :type ExternalAddr: str
        :param _Size: Backup file size
        :type Size: int
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._Size = None

    @property
    def Id(self):
        r"""Unique backup file ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        r"""File generation start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""File generation end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InternalAddr(self):
        r"""Download address on private network
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        r"""Download address on public network
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Size(self):
        r"""Backup file size
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    r"""AZ information such as number and status

    """

    def __init__(self):
        r"""
        :param _Zone: AZ abbreviation
        :type Zone: str
        :param _ZoneName: AZ name
        :type ZoneName: str
        :param _ZoneId: AZ number
        :type ZoneId: int
        :param _ZoneState: Availability status. Valid values:
`UNAVAILABLE`.
`AVAILABLE`.
`SELLOUT`.
`SUPPORTMODIFYONLY` (supports configuration adjustment).
        :type ZoneState: str
        :param _ZoneSupportIpv6: Whether the AZ supports IPv6 address access
        :type ZoneSupportIpv6: int
        :param _StandbyZoneSet: AZs that can be used as standby when this AZ is primary
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StandbyZoneSet: list of str
        """
        self._Zone = None
        self._ZoneName = None
        self._ZoneId = None
        self._ZoneState = None
        self._ZoneSupportIpv6 = None
        self._StandbyZoneSet = None

    @property
    def Zone(self):
        r"""AZ abbreviation
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        r"""AZ name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        r"""AZ number
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneState(self):
        r"""Availability status. Valid values:
`UNAVAILABLE`.
`AVAILABLE`.
`SELLOUT`.
`SUPPORTMODIFYONLY` (supports configuration adjustment).
        :rtype: str
        """
        return self._ZoneState

    @ZoneState.setter
    def ZoneState(self, ZoneState):
        self._ZoneState = ZoneState

    @property
    def ZoneSupportIpv6(self):
        r"""Whether the AZ supports IPv6 address access
        :rtype: int
        """
        return self._ZoneSupportIpv6

    @ZoneSupportIpv6.setter
    def ZoneSupportIpv6(self, ZoneSupportIpv6):
        self._ZoneSupportIpv6 = ZoneSupportIpv6

    @property
    def StandbyZoneSet(self):
        r"""AZs that can be used as standby when this AZ is primary
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._StandbyZoneSet

    @StandbyZoneSet.setter
    def StandbyZoneSet(self, StandbyZoneSet):
        self._StandbyZoneSet = StandbyZoneSet


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneState = params.get("ZoneState")
        self._ZoneSupportIpv6 = params.get("ZoneSupportIpv6")
        self._StandbyZoneSet = params.get("StandbyZoneSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        