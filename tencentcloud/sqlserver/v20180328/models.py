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


class AccountCreateInfo(AbstractModel):
    """Account creation information

    """

    def __init__(self):
        r"""
        :param _UserName: Instance username
        :type UserName: str
        :param _Password: Instance password
        :type Password: str
        :param _DBPrivileges: List of database permissions
        :type DBPrivileges: list of DBPrivilege
        :param _Remark: Account remarks
        :type Remark: str
        :param _IsAdmin: Whether it is an admin account. Valid values: true (it is an admin account when the instance is a single-node type and AccountType is L0; when the instance is a two-node type and AccountType is L1), false (it is a standard account when AccountType is L3)
        :type IsAdmin: bool
        :param _Authentication: Valid values: `win-windows authentication`, `sql-sqlserver authentication`. Default value: `sql-sqlserver authentication`
        :type Authentication: str
        :param _AccountType: Account type, which is an extension field of `IsAdmin`. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account, default)
        :type AccountType: str
        :param _IsCam: Whether CAM authentication is enabled
        :type IsCam: bool
        """
        self._UserName = None
        self._Password = None
        self._DBPrivileges = None
        self._Remark = None
        self._IsAdmin = None
        self._Authentication = None
        self._AccountType = None
        self._IsCam = None

    @property
    def UserName(self):
        """Instance username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Instance password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DBPrivileges(self):
        """List of database permissions
        :rtype: list of DBPrivilege
        """
        return self._DBPrivileges

    @DBPrivileges.setter
    def DBPrivileges(self, DBPrivileges):
        self._DBPrivileges = DBPrivileges

    @property
    def Remark(self):
        """Account remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def IsAdmin(self):
        """Whether it is an admin account. Valid values: true (it is an admin account when the instance is a single-node type and AccountType is L0; when the instance is a two-node type and AccountType is L1), false (it is a standard account when AccountType is L3)
        :rtype: bool
        """
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def Authentication(self):
        """Valid values: `win-windows authentication`, `sql-sqlserver authentication`. Default value: `sql-sqlserver authentication`
        :rtype: str
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def AccountType(self):
        """Account type, which is an extension field of `IsAdmin`. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account, default)
        :rtype: str
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def IsCam(self):
        """Whether CAM authentication is enabled
        :rtype: bool
        """
        return self._IsCam

    @IsCam.setter
    def IsCam(self, IsCam):
        self._IsCam = IsCam


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        if params.get("DBPrivileges") is not None:
            self._DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self._DBPrivileges.append(obj)
        self._Remark = params.get("Remark")
        self._IsAdmin = params.get("IsAdmin")
        self._Authentication = params.get("Authentication")
        self._AccountType = params.get("AccountType")
        self._IsCam = params.get("IsCam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountDetail(AbstractModel):
    """Account information details

    """

    def __init__(self):
        r"""
        :param _Name: Account name
        :type Name: str
        :param _Remark: Account remarks
        :type Remark: str
        :param _CreateTime: Account creation time
        :type CreateTime: str
        :param _Status: Account status. 1: creating, 2: normal, 3: modifying, 4: resetting password, -1: deleting
        :type Status: int
        :param _UpdateTime: Account update time
        :type UpdateTime: str
        :param _PassTime: Password update time
        :type PassTime: str
        :param _InternalStatus: Internal account status, which should be `enable` normally
        :type InternalStatus: str
        :param _Dbs: Information of read and write permissions of this account on relevant databases
        :type Dbs: list of DBPrivilege
        :param _IsAdmin: Whether it is an admin account
        :type IsAdmin: bool
        :param _IsCam: Whether it is a CAM managed account
        :type IsCam: bool
        :param _Authentication: Valid values: `win-windows authentication`, `sql-sqlserver authentication`.
        :type Authentication: str
        :param _Host: The host required for `win-windows authentication` account
        :type Host: str
        :param _AccountType: Account type. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account).
        :type AccountType: str
        """
        self._Name = None
        self._Remark = None
        self._CreateTime = None
        self._Status = None
        self._UpdateTime = None
        self._PassTime = None
        self._InternalStatus = None
        self._Dbs = None
        self._IsAdmin = None
        self._IsCam = None
        self._Authentication = None
        self._Host = None
        self._AccountType = None

    @property
    def Name(self):
        """Account name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """Account remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """Account creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        """Account status. 1: creating, 2: normal, 3: modifying, 4: resetting password, -1: deleting
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        """Account update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PassTime(self):
        """Password update time
        :rtype: str
        """
        return self._PassTime

    @PassTime.setter
    def PassTime(self, PassTime):
        self._PassTime = PassTime

    @property
    def InternalStatus(self):
        """Internal account status, which should be `enable` normally
        :rtype: str
        """
        return self._InternalStatus

    @InternalStatus.setter
    def InternalStatus(self, InternalStatus):
        self._InternalStatus = InternalStatus

    @property
    def Dbs(self):
        """Information of read and write permissions of this account on relevant databases
        :rtype: list of DBPrivilege
        """
        return self._Dbs

    @Dbs.setter
    def Dbs(self, Dbs):
        self._Dbs = Dbs

    @property
    def IsAdmin(self):
        """Whether it is an admin account
        :rtype: bool
        """
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def IsCam(self):
        """Whether it is a CAM managed account
        :rtype: bool
        """
        return self._IsCam

    @IsCam.setter
    def IsCam(self, IsCam):
        self._IsCam = IsCam

    @property
    def Authentication(self):
        """Valid values: `win-windows authentication`, `sql-sqlserver authentication`.
        :rtype: str
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Host(self):
        """The host required for `win-windows authentication` account
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def AccountType(self):
        """Account type. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account).
        :rtype: str
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._UpdateTime = params.get("UpdateTime")
        self._PassTime = params.get("PassTime")
        self._InternalStatus = params.get("InternalStatus")
        if params.get("Dbs") is not None:
            self._Dbs = []
            for item in params.get("Dbs"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self._Dbs.append(obj)
        self._IsAdmin = params.get("IsAdmin")
        self._IsCam = params.get("IsCam")
        self._Authentication = params.get("Authentication")
        self._Host = params.get("Host")
        self._AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountPassword(AbstractModel):
    """Instance account password information

    """

    def __init__(self):
        r"""
        :param _UserName: Username
        :type UserName: str
        :param _Password: Password
        :type Password: str
        """
        self._UserName = None
        self._Password = None

    @property
    def UserName(self):
        """Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountPrivilege(AbstractModel):
    """Database account permission information, which is set when the database is created

    """

    def __init__(self):
        r"""
        :param _UserName: Database username
        :type UserName: str
        :param _Privilege: Database permission. Valid values: `ReadWrite` (read-write), `ReadOnly` (read-only), `Delete` (delete the database permissions of this account), `DBOwner` (owner).
        :type Privilege: str
        :param _AccountType: Account name. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account).
        :type AccountType: str
        """
        self._UserName = None
        self._Privilege = None
        self._AccountType = None

    @property
    def UserName(self):
        """Database username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Privilege(self):
        """Database permission. Valid values: `ReadWrite` (read-write), `ReadOnly` (read-only), `Delete` (delete the database permissions of this account), `DBOwner` (owner).
        :rtype: str
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def AccountType(self):
        """Account name. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account).
        :rtype: str
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Privilege = params.get("Privilege")
        self._AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountPrivilegeModifyInfo(AbstractModel):
    """Database account permission change information

    """

    def __init__(self):
        r"""
        :param _UserName: Database username
        :type UserName: str
        :param _DBPrivileges: Account permission change information
        :type DBPrivileges: list of DBPrivilegeModifyInfo
        :param _IsAdmin: Whether it is an instance admin account. Valid values: `true` (Yes. When the instance is single-node and `AccountType` is `L0`, it's an admin account; when the instance is two-node and `AccountType` is `L1`, it's a privileged account), `false` (No. It's a standard account and `AccountType` is `L3`).
        :type IsAdmin: bool
        :param _AccountType: Account type, which is an extension field of `IsAdmin`. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account, default)
        :type AccountType: str
        """
        self._UserName = None
        self._DBPrivileges = None
        self._IsAdmin = None
        self._AccountType = None

    @property
    def UserName(self):
        """Database username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DBPrivileges(self):
        """Account permission change information
        :rtype: list of DBPrivilegeModifyInfo
        """
        return self._DBPrivileges

    @DBPrivileges.setter
    def DBPrivileges(self, DBPrivileges):
        self._DBPrivileges = DBPrivileges

    @property
    def IsAdmin(self):
        """Whether it is an instance admin account. Valid values: `true` (Yes. When the instance is single-node and `AccountType` is `L0`, it's an admin account; when the instance is two-node and `AccountType` is `L1`, it's a privileged account), `false` (No. It's a standard account and `AccountType` is `L3`).
        :rtype: bool
        """
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def AccountType(self):
        """Account type, which is an extension field of `IsAdmin`. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account, default)
        :rtype: str
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        if params.get("DBPrivileges") is not None:
            self._DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilegeModifyInfo()
                obj._deserialize(item)
                self._DBPrivileges.append(obj)
        self._IsAdmin = params.get("IsAdmin")
        self._AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountRemark(AbstractModel):
    """Account remarks

    """

    def __init__(self):
        r"""
        :param _UserName: Account name
        :type UserName: str
        :param _Remark: New remarks of account
        :type Remark: str
        """
        self._UserName = None
        self._Remark = None

    @property
    def UserName(self):
        """Account name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Remark(self):
        """New remarks of account
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Backup(AbstractModel):
    """Backup file details

    """

    def __init__(self):
        r"""
        :param _FileName: File name. The name of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :type FileName: str
        :param _Size: File size in KB. The size of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :type Size: int
        :param _StartTime: Backup start time
        :type StartTime: str
        :param _EndTime: Backup end time
        :type EndTime: str
        :param _InternalAddr: Private network download address. The download address of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :type InternalAddr: str
        :param _ExternalAddr: Public network download address. The download address of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :type ExternalAddr: str
        :param _Id: Unique ID of a backup file, which is used by the `RestoreInstance` API. The unique ID of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :type Id: int
        :param _Status: Backup file status (0: creating, 1: succeeded, 2: failed)
        :type Status: int
        :param _DBs: List of databases for multi-database backup
        :type DBs: list of str
        :param _Strategy: Backup policy (0: instance backup, 1: multi-database backup)
        :type Strategy: int
        :param _BackupWay: Backup Mode. Valid values: `0` (scheduled backup); `1` (manual backup); `2` (archive backup).
        :type BackupWay: int
        :param _BackupName: Backup task name (customizable)
        :type BackupName: str
        :param _GroupId: Group ID of unarchived backup files, which can be used as a request parameter in the `DescribeBackupFiles` API to get details of unarchived backup files in the specified group. This parameter is invalid for archived backup files.
        :type GroupId: str
        :param _BackupFormat: Backup file format. Valid values:`pkg` (archive file), `single` (unarchived files).
        :type BackupFormat: str
        :param _Region: The code of current region where the instance resides
        :type Region: str
        :param _CrossBackupAddr: The download address of cross-region backup in target region
        :type CrossBackupAddr: list of CrossBackupAddr
        :param _CrossBackupStatus: The target region and status of cross-region backup
        :type CrossBackupStatus: list of CrossRegionStatus
        """
        self._FileName = None
        self._Size = None
        self._StartTime = None
        self._EndTime = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._Id = None
        self._Status = None
        self._DBs = None
        self._Strategy = None
        self._BackupWay = None
        self._BackupName = None
        self._GroupId = None
        self._BackupFormat = None
        self._Region = None
        self._CrossBackupAddr = None
        self._CrossBackupStatus = None

    @property
    def FileName(self):
        """File name. The name of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        """File size in KB. The size of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def StartTime(self):
        """Backup start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Backup end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InternalAddr(self):
        """Private network download address. The download address of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        """Public network download address. The download address of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Id(self):
        """Unique ID of a backup file, which is used by the `RestoreInstance` API. The unique ID of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """Backup file status (0: creating, 1: succeeded, 2: failed)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DBs(self):
        """List of databases for multi-database backup
        :rtype: list of str
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def Strategy(self):
        """Backup policy (0: instance backup, 1: multi-database backup)
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def BackupWay(self):
        """Backup Mode. Valid values: `0` (scheduled backup); `1` (manual backup); `2` (archive backup).
        :rtype: int
        """
        return self._BackupWay

    @BackupWay.setter
    def BackupWay(self, BackupWay):
        self._BackupWay = BackupWay

    @property
    def BackupName(self):
        """Backup task name (customizable)
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def GroupId(self):
        """Group ID of unarchived backup files, which can be used as a request parameter in the `DescribeBackupFiles` API to get details of unarchived backup files in the specified group. This parameter is invalid for archived backup files.
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def BackupFormat(self):
        """Backup file format. Valid values:`pkg` (archive file), `single` (unarchived files).
        :rtype: str
        """
        return self._BackupFormat

    @BackupFormat.setter
    def BackupFormat(self, BackupFormat):
        self._BackupFormat = BackupFormat

    @property
    def Region(self):
        """The code of current region where the instance resides
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CrossBackupAddr(self):
        """The download address of cross-region backup in target region
        :rtype: list of CrossBackupAddr
        """
        return self._CrossBackupAddr

    @CrossBackupAddr.setter
    def CrossBackupAddr(self, CrossBackupAddr):
        self._CrossBackupAddr = CrossBackupAddr

    @property
    def CrossBackupStatus(self):
        """The target region and status of cross-region backup
        :rtype: list of CrossRegionStatus
        """
        return self._CrossBackupStatus

    @CrossBackupStatus.setter
    def CrossBackupStatus(self, CrossBackupStatus):
        self._CrossBackupStatus = CrossBackupStatus


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._Size = params.get("Size")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._DBs = params.get("DBs")
        self._Strategy = params.get("Strategy")
        self._BackupWay = params.get("BackupWay")
        self._BackupName = params.get("BackupName")
        self._GroupId = params.get("GroupId")
        self._BackupFormat = params.get("BackupFormat")
        self._Region = params.get("Region")
        if params.get("CrossBackupAddr") is not None:
            self._CrossBackupAddr = []
            for item in params.get("CrossBackupAddr"):
                obj = CrossBackupAddr()
                obj._deserialize(item)
                self._CrossBackupAddr.append(obj)
        if params.get("CrossBackupStatus") is not None:
            self._CrossBackupStatus = []
            for item in params.get("CrossBackupStatus"):
                obj = CrossRegionStatus()
                obj._deserialize(item)
                self._CrossBackupStatus.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFile(AbstractModel):
    """If the backup files are unarchived, each database corresponds to one backup file.

    """

    def __init__(self):
        r"""
        :param _Id: Unique ID of a backup file
        :type Id: int
        :param _FileName: Backup file name
        :type FileName: str
        :param _Size: File size in KB
        :type Size: int
        :param _DBs: Name of the database corresponding to the backup file
        :type DBs: list of str
        :param _DownloadLink: Download address
        :type DownloadLink: str
        :param _Region: The code of the region where current instance resides
        :type Region: str
        :param _CrossBackupAddr: The target region and download address of cross-region backup
        :type CrossBackupAddr: list of CrossBackupAddr
        """
        self._Id = None
        self._FileName = None
        self._Size = None
        self._DBs = None
        self._DownloadLink = None
        self._Region = None
        self._CrossBackupAddr = None

    @property
    def Id(self):
        """Unique ID of a backup file
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FileName(self):
        """Backup file name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        """File size in KB
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def DBs(self):
        """Name of the database corresponding to the backup file
        :rtype: list of str
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def DownloadLink(self):
        """Download address
        :rtype: str
        """
        return self._DownloadLink

    @DownloadLink.setter
    def DownloadLink(self, DownloadLink):
        self._DownloadLink = DownloadLink

    @property
    def Region(self):
        """The code of the region where current instance resides
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CrossBackupAddr(self):
        """The target region and download address of cross-region backup
        :rtype: list of CrossBackupAddr
        """
        return self._CrossBackupAddr

    @CrossBackupAddr.setter
    def CrossBackupAddr(self, CrossBackupAddr):
        self._CrossBackupAddr = CrossBackupAddr


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._FileName = params.get("FileName")
        self._Size = params.get("Size")
        self._DBs = params.get("DBs")
        self._DownloadLink = params.get("DownloadLink")
        self._Region = params.get("Region")
        if params.get("CrossBackupAddr") is not None:
            self._CrossBackupAddr = []
            for item in params.get("CrossBackupAddr"):
                obj = CrossBackupAddr()
                obj._deserialize(item)
                self._CrossBackupAddr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessIntelligenceFile(AbstractModel):
    """Business intelligence service file type

    """

    def __init__(self):
        r"""
        :param _FileName: File name
        :type FileName: str
        :param _FileType: File type
        :type FileType: str
        :param _FileURL: File COS_URL
        :type FileURL: str
        :param _FilePath: The file path on the server
        :type FilePath: str
        :param _FileSize: File size in bytes
        :type FileSize: int
        :param _FileMd5: File MD5 value
        :type FileMd5: str
        :param _Status: File deployment status. Valid values: `1`(Initialize to be deployed), `2` (Deploying), `3` (Deployment successful), `4` (Deployment failed).
        :type Status: int
        :param _Remark: Remarks
        :type Remark: str
        :param _CreateTime: File creation time
        :type CreateTime: str
        :param _StartTime: Start time of file deployment
        :type StartTime: str
        :param _EndTime: End time of file deployment
        :type EndTime: str
        :param _Message: Returned error message
        :type Message: str
        :param _InstanceId: Business intelligence instance ID
        :type InstanceId: str
        :param _Action: Operation information
        :type Action: :class:`tencentcloud.sqlserver.v20180328.models.FileAction`
        """
        self._FileName = None
        self._FileType = None
        self._FileURL = None
        self._FilePath = None
        self._FileSize = None
        self._FileMd5 = None
        self._Status = None
        self._Remark = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Message = None
        self._InstanceId = None
        self._Action = None

    @property
    def FileName(self):
        """File name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        """File type
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileURL(self):
        """File COS_URL
        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def FilePath(self):
        """The file path on the server
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileSize(self):
        """File size in bytes
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileMd5(self):
        """File MD5 value
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def Status(self):
        """File deployment status. Valid values: `1`(Initialize to be deployed), `2` (Deploying), `3` (Deployment successful), `4` (Deployment failed).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        """Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """File creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """Start time of file deployment
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of file deployment
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Message(self):
        """Returned error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceId(self):
        """Business intelligence instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Action(self):
        """Operation information
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.FileAction`
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._FileURL = params.get("FileURL")
        self._FilePath = params.get("FilePath")
        self._FileSize = params.get("FileSize")
        self._FileMd5 = params.get("FileMd5")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Message = params.get("Message")
        self._InstanceId = params.get("InstanceId")
        if params.get("Action") is not None:
            self._Action = FileAction()
            self._Action._deserialize(params.get("Action"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBRequest(AbstractModel):
    """CloneDB request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        :param _RenameRestore: Clone and rename the databases specified in `ReNameRestoreDatabase`. Please note that the clones must be renamed.
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self._InstanceId = None
        self._RenameRestore = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-j8kv137v
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RenameRestore(self):
        """Clone and rename the databases specified in `ReNameRestoreDatabase`. Please note that the clones must be renamed.
        :rtype: list of RenameRestoreDatabase
        """
        return self._RenameRestore

    @RenameRestore.setter
    def RenameRestore(self, RenameRestore):
        self._RenameRestore = RenameRestore


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("RenameRestore") is not None:
            self._RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBResponse(AbstractModel):
    """CloneDB response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task request ID, which can be used in the `DescribeFlowStatus` API to query the execution result of an async task
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task request ID, which can be used in the `DescribeFlowStatus` API to query the execution result of an async task
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloseInterCommunicationRequest(AbstractModel):
    """CloseInterCommunication request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: IDs of instances with interconnection disabled
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        """IDs of instances with interconnection disabled
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseInterCommunicationResponse(AbstractModel):
    """CloseInterCommunication response structure.

    """

    def __init__(self):
        r"""
        :param _InterInstanceFlowSet: IDs of instance and async task
        :type InterInstanceFlowSet: list of InterInstanceFlow
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InterInstanceFlowSet = None
        self._RequestId = None

    @property
    def InterInstanceFlowSet(self):
        """IDs of instance and async task
        :rtype: list of InterInstanceFlow
        """
        return self._InterInstanceFlowSet

    @InterInstanceFlowSet.setter
    def InterInstanceFlowSet(self, InterInstanceFlowSet):
        self._InterInstanceFlowSet = InterInstanceFlowSet

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
        if params.get("InterInstanceFlowSet") is not None:
            self._InterInstanceFlowSet = []
            for item in params.get("InterInstanceFlowSet"):
                obj = InterInstanceFlow()
                obj._deserialize(item)
                self._InterInstanceFlowSet.append(obj)
        self._RequestId = params.get("RequestId")


class CosUploadBackupFile(AbstractModel):
    """Querying the size of uploaded backup files.

    """

    def __init__(self):
        r"""
        :param _FileName: Backup name
        :type FileName: str
        :param _Size: Backup size
        :type Size: int
        """
        self._FileName = None
        self._Size = None

    @property
    def FileName(self):
        """Backup name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        """Backup size
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param _Accounts: Database instance account information
        :type Accounts: list of AccountCreateInfo
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        """Database instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        """Database instance account information
        :rtype: list of AccountCreateInfo
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountCreateInfo()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateBackupMigrationRequest(AbstractModel):
    """CreateBackupMigration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _RecoveryType: Migration task restoration type. FULL: full backup restoration, FULL_LOG: full backup and transaction log restoration, FULL_DIFF: full backup and differential backup restoration
        :type RecoveryType: str
        :param _UploadType: Backup upload type. COS_URL: the backup is stored in user's Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application's Cloud Object Storage and needs to be uploaded by the user.
        :type UploadType: str
        :param _MigrationName: Task name
        :type MigrationName: str
        :param _BackupFiles: If the UploadType is COS_URL, fill in the URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :type BackupFiles: list of str
        """
        self._InstanceId = None
        self._RecoveryType = None
        self._UploadType = None
        self._MigrationName = None
        self._BackupFiles = None

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RecoveryType(self):
        """Migration task restoration type. FULL: full backup restoration, FULL_LOG: full backup and transaction log restoration, FULL_DIFF: full backup and differential backup restoration
        :rtype: str
        """
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        """Backup upload type. COS_URL: the backup is stored in user's Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application's Cloud Object Storage and needs to be uploaded by the user.
        :rtype: str
        """
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def MigrationName(self):
        """Task name
        :rtype: str
        """
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def BackupFiles(self):
        """If the UploadType is COS_URL, fill in the URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :rtype: list of str
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RecoveryType = params.get("RecoveryType")
        self._UploadType = params.get("UploadType")
        self._MigrationName = params.get("MigrationName")
        self._BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupMigrationResponse(AbstractModel):
    """CreateBackupMigration response structure.

    """

    def __init__(self):
        r"""
        :param _BackupMigrationId: Backup import task ID
        :type BackupMigrationId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupMigrationId = None
        self._RequestId = None

    @property
    def BackupMigrationId(self):
        """Backup import task ID
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

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
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        r"""
        :param _Strategy: Backup policy (0: instance backup, 1: multi-database backup)
        :type Strategy: int
        :param _DBNames: List of names of databases to be backed up (required only for multi-database backup)
        :type DBNames: list of str
        :param _InstanceId: (Required) Instance ID in the format of mssql-i1z41iwd
        :type InstanceId: str
        :param _BackupName: Backup name. If this parameter is left empty, a backup name in the format of "[Instance ID]_[Backup start timestamp]" will be automatically generated.
        :type BackupName: str
        :param _StorageStrategy: Backup storage policy. 0: Follow the custom backup retention policy; 1: Follow the instance lifecycle until the instance is eliminated. Default value: 0.
        :type StorageStrategy: int
        """
        self._Strategy = None
        self._DBNames = None
        self._InstanceId = None
        self._BackupName = None
        self._StorageStrategy = None

    @property
    def Strategy(self):
        """Backup policy (0: instance backup, 1: multi-database backup)
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def DBNames(self):
        """List of names of databases to be backed up (required only for multi-database backup)
        :rtype: list of str
        """
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def InstanceId(self):
        """(Required) Instance ID in the format of mssql-i1z41iwd
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        """Backup name. If this parameter is left empty, a backup name in the format of "[Instance ID]_[Backup start timestamp]" will be automatically generated.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def StorageStrategy(self):
        """Backup storage policy. 0: Follow the custom backup retention policy; 1: Follow the instance lifecycle until the instance is eliminated. Default value: 0.
        :rtype: int
        """
        return self._StorageStrategy

    @StorageStrategy.setter
    def StorageStrategy(self, StorageStrategy):
        self._StorageStrategy = StorageStrategy


    def _deserialize(self, params):
        self._Strategy = params.get("Strategy")
        self._DBNames = params.get("DBNames")
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        self._StorageStrategy = params.get("StorageStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The async job ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """The async job ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateBasicDBInstancesRequest(AbstractModel):
    """CreateBasicDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: 
        :type Zone: str
        :param _Cpu: 
        :type Cpu: int
        :param _Memory: 
        :type Memory: int
        :param _Storage: 
        :type Storage: int
        :param _SubnetId: 
        :type SubnetId: str
        :param _VpcId: 
        :type VpcId: str
        :param _MachineType: 
        :type MachineType: str
        :param _InstanceChargeType: 
        :type InstanceChargeType: str
        :param _ProjectId: 
        :type ProjectId: int
        :param _GoodsNum: 
        :type GoodsNum: int
        :param _DBVersion: 
        :type DBVersion: str
        :param _Period: 
        :type Period: int
        :param _SecurityGroupList: 
        :type SecurityGroupList: list of str
        :param _AutoRenewFlag: 
        :type AutoRenewFlag: int
        :param _AutoVoucher: 
        :type AutoVoucher: int
        :param _VoucherIds: 
        :type VoucherIds: list of str
        :param _Weekly: 
        :type Weekly: list of int
        :param _StartTime: 
        :type StartTime: str
        :param _Span: 
        :type Span: int
        :param _ResourceTags: 
        :type ResourceTags: list of ResourceTag
        :param _Collation: 
        :type Collation: str
        :param _TimeZone: 
        :type TimeZone: str
        """
        self._Zone = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._SubnetId = None
        self._VpcId = None
        self._MachineType = None
        self._InstanceChargeType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._DBVersion = None
        self._Period = None
        self._SecurityGroupList = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def Zone(self):
        """
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Cpu(self):
        """
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def SubnetId(self):
        """
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        """
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def MachineType(self):
        """
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def InstanceChargeType(self):
        """
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def ProjectId(self):
        """
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        """
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def DBVersion(self):
        """
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def Period(self):
        """
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        """
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoRenewFlag(self):
        """
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        """
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def Weekly(self):
        """
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        """
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        """
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def ResourceTags(self):
        """
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        """
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        """
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._MachineType = params.get("MachineType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._DBVersion = params.get("DBVersion")
        self._Period = params.get("Period")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDBInstancesResponse(AbstractModel):
    """CreateBasicDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: 
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        """
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateBusinessDBInstancesRequest(AbstractModel):
    """CreateBusinessDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :type Zone: str
        :param _Memory: Instance memory size in GB
        :type Memory: int
        :param _Storage: Instance disk size in GB
        :type Storage: int
        :param _Cpu: The number of CPU cores of the instance you want to purchase.
        :type Cpu: int
        :param _MachineType: The host type of purchased instance. Valid values: `CLOUD_PREMIUM` (virtual machine with premium cloud disk), `CLOUD_SSD` (virtual machine with SSD).
        :type MachineType: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _GoodsNum: Number of instances purchased this time. Default value: `1`.
        :type GoodsNum: int
        :param _SubnetId: VPC subnet ID in the format of subnet-bdoe83fa. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :type SubnetId: str
        :param _VpcId: VPC ID in the format of vpc-dsp338hz. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :type VpcId: str
        :param _DBVersion: - Supported versions of business intelligence server. Valid values: `201603` (SQL Server 2016 Integration Services), `201703` (SQL Server 2017 Integration Services), `201903` (SQL Server 2019 Integration Services). Default value: `201903`. As the purchasable versions are region-specific, you can use the `DescribeProductConfig` API to query the information of purchasable versions in each region.
        :type DBVersion: str
        :param _SecurityGroupList: Security group list, which contains security group IDs in the format of sg-xxx.
        :type SecurityGroupList: list of str
        :param _Weekly: Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: `1` (Monday), `2` (Tuesday), `3` (Wednesday), `4` (Thursday), `5` (Friday), `6` (Saturday), `7` (Sunday).
        :type Weekly: list of int
        :param _StartTime: Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :type StartTime: str
        :param _Span: Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :type Span: int
        :param _ResourceTags: Tags associated with the instances to be created
        :type ResourceTags: list of ResourceTag
        """
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None
        self._MachineType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._DBVersion = None
        self._SecurityGroupList = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._ResourceTags = None

    @property
    def Zone(self):
        """Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        """Instance memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Instance disk size in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        """The number of CPU cores of the instance you want to purchase.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def MachineType(self):
        """The host type of purchased instance. Valid values: `CLOUD_PREMIUM` (virtual machine with premium cloud disk), `CLOUD_SSD` (virtual machine with SSD).
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        """Number of instances purchased this time. Default value: `1`.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        """VPC subnet ID in the format of subnet-bdoe83fa. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        """VPC ID in the format of vpc-dsp338hz. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DBVersion(self):
        """- Supported versions of business intelligence server. Valid values: `201603` (SQL Server 2016 Integration Services), `201703` (SQL Server 2017 Integration Services), `201903` (SQL Server 2019 Integration Services). Default value: `201903`. As the purchasable versions are region-specific, you can use the `DescribeProductConfig` API to query the information of purchasable versions in each region.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def SecurityGroupList(self):
        """Security group list, which contains security group IDs in the format of sg-xxx.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def Weekly(self):
        """Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: `1` (Monday), `2` (Tuesday), `3` (Wednesday), `4` (Thursday), `5` (Friday), `6` (Saturday), `7` (Sunday).
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        """Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        """Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def ResourceTags(self):
        """Tags associated with the instances to be created
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        self._MachineType = params.get("MachineType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._DBVersion = params.get("DBVersion")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBusinessDBInstancesResponse(AbstractModel):
    """CreateBusinessDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order name
        :type DealName: str
        :param _FlowId: Process ID Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _InstanceIdSet: IDs of instances Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIdSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._FlowId = None
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def DealName(self):
        """Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def FlowId(self):
        """Process ID Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceIdSet(self):
        """IDs of instances Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

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
        self._DealName = params.get("DealName")
        self._FlowId = params.get("FlowId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class CreateBusinessIntelligenceFileRequest(AbstractModel):
    """CreateBusinessIntelligenceFile request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _FileURL: 
        :type FileURL: str
        :param _FileType: File type. Valid values: `FLAT` (flat file as data source), `SSIS` (.ispac SSIS package file)
        :type FileType: str
        :param _Remark: Remarks
        :type Remark: str
        """
        self._InstanceId = None
        self._FileURL = None
        self._FileType = None
        self._Remark = None

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
    def FileURL(self):
        """
        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def FileType(self):
        """File type. Valid values: `FLAT` (flat file as data source), `SSIS` (.ispac SSIS package file)
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Remark(self):
        """Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileURL = params.get("FileURL")
        self._FileType = params.get("FileType")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBusinessIntelligenceFileResponse(AbstractModel):
    """CreateBusinessIntelligenceFile response structure.

    """

    def __init__(self):
        r"""
        :param _FileTaskId: File name
        :type FileTaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileTaskId = None
        self._RequestId = None

    @property
    def FileTaskId(self):
        """File name
        :rtype: str
        """
        return self._FileTaskId

    @FileTaskId.setter
    def FileTaskId(self, FileTaskId):
        self._FileTaskId = FileTaskId

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
        self._FileTaskId = params.get("FileTaskId")
        self._RequestId = params.get("RequestId")


class CreateCloudDBInstancesRequest(AbstractModel):
    """CreateCloudDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Instance AZ, such as `ap-guangzhou-1` (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :type Zone: str
        :param _Memory: Instance memory size in GB
        :type Memory: int
        :param _Storage: Instance disk size in GB
        :type Storage: int
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _MachineType: The host type of the purchased instance. Valid values: `CLOUD_HSSD` (virtual machine with enhanced SSD), `CLOUD_TSSD` (virtual machine with ulTra SSD), `CLOUD_BSSD` (virtual machine with balanced SSD).
        :type MachineType: str
        :param _InstanceChargeType: Billing mode. Valid values: `PREPAID` (monthly subscription), `POSTPAID` (pay-as-you-go).
        :type InstanceChargeType: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _GoodsNum: Number of instances purchased this time. Default value: `1`.  Maximum value: `10`.
        :type GoodsNum: int
        :param _SubnetId: VPC subnet ID in the format of `subnet-bdoe83fa`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :type SubnetId: str
        :param _VpcId: VPC ID in the format of `vpc-dsp338hz`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :type VpcId: str
        :param _Period: The purchase period of an instance. Default value: `1` (one month).  Maximum value: `48`.
        :type Period: int
        :param _AutoVoucher: Whether to automatically use voucher. Valid values: `0` (no, default), `1` (yes).
        :type AutoVoucher: int
        :param _VoucherIds: Array of voucher IDs (currently, only one voucher can be used per order)
        :type VoucherIds: list of str
        :param _DBVersion: SQL Server version. Valid values:  `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard).  Default value: `2008R2`.  The available version varies by region, and you can pull the version information through the `DescribeProductConfig` API.
        :type DBVersion: str
        :param _AutoRenewFlag: Auto-renewal flag, which takes effect only when purchasing a monthly subscribed instance.  Valid values:  `0` (auto-renewal disabled), `1` (auto-renewal enabled). Default value: `0`.
        :type AutoRenewFlag: int
        :param _SecurityGroupList: Security group list, which contains security group IDs in the format of `sg-xxx`.
        :type SecurityGroupList: list of str
        :param _Weekly: Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: `1` (Monday), `2` (Tuesday), `3` (Wednesday), `4` (Thursday), `5` (Friday), `6` (Saturday), `7` (Sunday).
        :type Weekly: list of int
        :param _StartTime: Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :type StartTime: str
        :param _Span: Configuration of the maintenance window, which specifies the maintenance duration in hours. Hour
        :type Span: int
        :param _MultiZones: Whether to deploy across AZs. Default value: `false`.
        :type MultiZones: bool
        :param _ResourceTags: Tags associated with the instances to be created
        :type ResourceTags: list of ResourceTag
        :param _Collation: Collation of system character sets. Default value:  `Chinese_PRC_CI_AS`.
        :type Collation: str
        :param _TimeZone: System time zone. Default value:  `China Standard Time`.
        :type TimeZone: str
        """
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None
        self._MachineType = None
        self._InstanceChargeType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._DBVersion = None
        self._AutoRenewFlag = None
        self._SecurityGroupList = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._MultiZones = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def Zone(self):
        """Instance AZ, such as `ap-guangzhou-1` (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        """Instance memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Instance disk size in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def MachineType(self):
        """The host type of the purchased instance. Valid values: `CLOUD_HSSD` (virtual machine with enhanced SSD), `CLOUD_TSSD` (virtual machine with ulTra SSD), `CLOUD_BSSD` (virtual machine with balanced SSD).
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def InstanceChargeType(self):
        """Billing mode. Valid values: `PREPAID` (monthly subscription), `POSTPAID` (pay-as-you-go).
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        """Number of instances purchased this time. Default value: `1`.  Maximum value: `10`.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        """VPC subnet ID in the format of `subnet-bdoe83fa`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        """VPC ID in the format of `vpc-dsp338hz`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        """The purchase period of an instance. Default value: `1` (one month).  Maximum value: `48`.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        """Whether to automatically use voucher. Valid values: `0` (no, default), `1` (yes).
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """Array of voucher IDs (currently, only one voucher can be used per order)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def DBVersion(self):
        """SQL Server version. Valid values:  `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard).  Default value: `2008R2`.  The available version varies by region, and you can pull the version information through the `DescribeProductConfig` API.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def AutoRenewFlag(self):
        """Auto-renewal flag, which takes effect only when purchasing a monthly subscribed instance.  Valid values:  `0` (auto-renewal disabled), `1` (auto-renewal enabled). Default value: `0`.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SecurityGroupList(self):
        """Security group list, which contains security group IDs in the format of `sg-xxx`.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def Weekly(self):
        """Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: `1` (Monday), `2` (Tuesday), `3` (Wednesday), `4` (Thursday), `5` (Friday), `6` (Saturday), `7` (Sunday).
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        """Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        """Configuration of the maintenance window, which specifies the maintenance duration in hours. Hour
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def MultiZones(self):
        """Whether to deploy across AZs. Default value: `false`.
        :rtype: bool
        """
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def ResourceTags(self):
        """Tags associated with the instances to be created
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        """Collation of system character sets. Default value:  `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        """System time zone. Default value:  `China Standard Time`.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        self._MachineType = params.get("MachineType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._DBVersion = params.get("DBVersion")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        self._MultiZones = params.get("MultiZones")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudDBInstancesResponse(AbstractModel):
    """CreateCloudDBInstances response structure.

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
        """Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateCloudReadOnlyDBInstancesRequest(AbstractModel):
    """CreateCloudReadOnlyDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of  `mssql-3l3fgqn7`.
        :type InstanceId: str
        :param _Zone: Instance AZ, such as `ap-guangzhou-1` (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :type Zone: str
        :param _ReadOnlyGroupType: Read-only group types. Valid values: `1` (each read-only replica is placed in one auto-created read-only group), `2` (all read-only replicas are placed in one auto-created read-only group), `3` (all read-only replicas are placed in one existing read-only group).
        :type ReadOnlyGroupType: int
        :param _Memory: Instance memory size in GB
        :type Memory: int
        :param _Storage: Instance disk size in GB
        :type Storage: int
        :param _Cpu: Number of instance cores
        :type Cpu: int
        :param _MachineType: The host type of purchased instance. Valid values: `CLOUD_HSSD` (virtual machine with enhanced SSD), `CLOUD_TSSD` (virtual machine with ulTra SSD), `CLOUD_BSSD` (virtual machine with balanced SSD).
        :type MachineType: str
        :param _ReadOnlyGroupForcedUpgrade: Valid values: `0` (not upgrade the primary instance by default), `1` (upgrade the primary instance to complete the RO deployment).  You need to pass in `1` for this parameter and upgrade the primary instance to cluster edition.
        :type ReadOnlyGroupForcedUpgrade: int
        :param _ReadOnlyGroupId: Existing read-only group ID, which is required when `ReadOnlyGroupType` is `3`.
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: New read-only group ID, which is required when `ReadOnlyGroupType` is `2`.
        :type ReadOnlyGroupName: str
        :param _ReadOnlyGroupIsOfflineDelay: Whether delayed read-only instance removal is enabled in a new read-only group, which is required when `ReadOnlyGroupType` is `2`. Valid values: `1` (enabled), `0` (disabled).  The read-only replica will be automatically removed when the delay between it and the primary instance exceeds the threshold.
        :type ReadOnlyGroupIsOfflineDelay: int
        :param _ReadOnlyGroupMaxDelayTime: The delay threshold for a new read-only group, which is required when `ReadOnlyGroupType` is `2` and `ReadOnlyGroupIsOfflineDelay` is `1`.
        :type ReadOnlyGroupMaxDelayTime: int
        :param _ReadOnlyGroupMinInGroup: Minimum number of reserved read-only replicas when the delayed removal is enabled for the new read-only group, which is required when `ReadOnlyGroupType` is `2` and `ReadOnlyGroupIsOfflineDelay` is `1`.
        :type ReadOnlyGroupMinInGroup: int
        :param _InstanceChargeType: Billing mode. Valid values: `PREPAID` (monthly subscription), `POSTPAID` (pay-as-you-go).
        :type InstanceChargeType: str
        :param _GoodsNum: Number of read-only instances to be purchased this time. Default value: `2`.
        :type GoodsNum: int
        :param _SubnetId: VPC subnet ID in the format of `subnet-bdoe83fa`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :type SubnetId: str
        :param _VpcId: VPC ID in the format of `vpc-dsp338hz`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :type VpcId: str
        :param _Period: The purchase period of an instance. Default value: `1` (one month).  Maximum value: `48`.
        :type Period: int
        :param _SecurityGroupList: Security group list, which contains security group IDs in the format of `sg-xxx`.
        :type SecurityGroupList: list of str
        :param _AutoVoucher: Whether to automatically use voucher. Valid values: `0` (no, default), `1` (yes).
        :type AutoVoucher: int
        :param _VoucherIds: Array of voucher IDs (currently, only one voucher can be used per order)
        :type VoucherIds: list of str
        :param _ResourceTags: Tags associated with the instances to be created
        :type ResourceTags: list of ResourceTag
        :param _Collation: Collation of system character sets. Default value:  Chinese_PRC_CI_AS
        :type Collation: str
        :param _TimeZone: System time zone. Default value:  `China Standard Time`
        :type TimeZone: str
        """
        self._InstanceId = None
        self._Zone = None
        self._ReadOnlyGroupType = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None
        self._MachineType = None
        self._ReadOnlyGroupForcedUpgrade = None
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._ReadOnlyGroupIsOfflineDelay = None
        self._ReadOnlyGroupMaxDelayTime = None
        self._ReadOnlyGroupMinInGroup = None
        self._InstanceChargeType = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._SecurityGroupList = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def InstanceId(self):
        """Instance ID in the format of  `mssql-3l3fgqn7`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        """Instance AZ, such as `ap-guangzhou-1` (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ReadOnlyGroupType(self):
        """Read-only group types. Valid values: `1` (each read-only replica is placed in one auto-created read-only group), `2` (all read-only replicas are placed in one auto-created read-only group), `3` (all read-only replicas are placed in one existing read-only group).
        :rtype: int
        """
        return self._ReadOnlyGroupType

    @ReadOnlyGroupType.setter
    def ReadOnlyGroupType(self, ReadOnlyGroupType):
        self._ReadOnlyGroupType = ReadOnlyGroupType

    @property
    def Memory(self):
        """Instance memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Instance disk size in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        """Number of instance cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def MachineType(self):
        """The host type of purchased instance. Valid values: `CLOUD_HSSD` (virtual machine with enhanced SSD), `CLOUD_TSSD` (virtual machine with ulTra SSD), `CLOUD_BSSD` (virtual machine with balanced SSD).
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def ReadOnlyGroupForcedUpgrade(self):
        """Valid values: `0` (not upgrade the primary instance by default), `1` (upgrade the primary instance to complete the RO deployment).  You need to pass in `1` for this parameter and upgrade the primary instance to cluster edition.
        :rtype: int
        """
        return self._ReadOnlyGroupForcedUpgrade

    @ReadOnlyGroupForcedUpgrade.setter
    def ReadOnlyGroupForcedUpgrade(self, ReadOnlyGroupForcedUpgrade):
        self._ReadOnlyGroupForcedUpgrade = ReadOnlyGroupForcedUpgrade

    @property
    def ReadOnlyGroupId(self):
        """Existing read-only group ID, which is required when `ReadOnlyGroupType` is `3`.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        """New read-only group ID, which is required when `ReadOnlyGroupType` is `2`.
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ReadOnlyGroupIsOfflineDelay(self):
        """Whether delayed read-only instance removal is enabled in a new read-only group, which is required when `ReadOnlyGroupType` is `2`. Valid values: `1` (enabled), `0` (disabled).  The read-only replica will be automatically removed when the delay between it and the primary instance exceeds the threshold.
        :rtype: int
        """
        return self._ReadOnlyGroupIsOfflineDelay

    @ReadOnlyGroupIsOfflineDelay.setter
    def ReadOnlyGroupIsOfflineDelay(self, ReadOnlyGroupIsOfflineDelay):
        self._ReadOnlyGroupIsOfflineDelay = ReadOnlyGroupIsOfflineDelay

    @property
    def ReadOnlyGroupMaxDelayTime(self):
        """The delay threshold for a new read-only group, which is required when `ReadOnlyGroupType` is `2` and `ReadOnlyGroupIsOfflineDelay` is `1`.
        :rtype: int
        """
        return self._ReadOnlyGroupMaxDelayTime

    @ReadOnlyGroupMaxDelayTime.setter
    def ReadOnlyGroupMaxDelayTime(self, ReadOnlyGroupMaxDelayTime):
        self._ReadOnlyGroupMaxDelayTime = ReadOnlyGroupMaxDelayTime

    @property
    def ReadOnlyGroupMinInGroup(self):
        """Minimum number of reserved read-only replicas when the delayed removal is enabled for the new read-only group, which is required when `ReadOnlyGroupType` is `2` and `ReadOnlyGroupIsOfflineDelay` is `1`.
        :rtype: int
        """
        return self._ReadOnlyGroupMinInGroup

    @ReadOnlyGroupMinInGroup.setter
    def ReadOnlyGroupMinInGroup(self, ReadOnlyGroupMinInGroup):
        self._ReadOnlyGroupMinInGroup = ReadOnlyGroupMinInGroup

    @property
    def InstanceChargeType(self):
        """Billing mode. Valid values: `PREPAID` (monthly subscription), `POSTPAID` (pay-as-you-go).
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def GoodsNum(self):
        """Number of read-only instances to be purchased this time. Default value: `2`.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        """VPC subnet ID in the format of `subnet-bdoe83fa`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        """VPC ID in the format of `vpc-dsp338hz`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        """The purchase period of an instance. Default value: `1` (one month).  Maximum value: `48`.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        """Security group list, which contains security group IDs in the format of `sg-xxx`.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoVoucher(self):
        """Whether to automatically use voucher. Valid values: `0` (no, default), `1` (yes).
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """Array of voucher IDs (currently, only one voucher can be used per order)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ResourceTags(self):
        """Tags associated with the instances to be created
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        """Collation of system character sets. Default value:  Chinese_PRC_CI_AS
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        """System time zone. Default value:  `China Standard Time`
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._ReadOnlyGroupType = params.get("ReadOnlyGroupType")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        self._MachineType = params.get("MachineType")
        self._ReadOnlyGroupForcedUpgrade = params.get("ReadOnlyGroupForcedUpgrade")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._ReadOnlyGroupIsOfflineDelay = params.get("ReadOnlyGroupIsOfflineDelay")
        self._ReadOnlyGroupMaxDelayTime = params.get("ReadOnlyGroupMaxDelayTime")
        self._ReadOnlyGroupMinInGroup = params.get("ReadOnlyGroupMinInGroup")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudReadOnlyDBInstancesResponse(AbstractModel):
    """CreateCloudReadOnlyDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order name in array
        :type DealNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealNames = None
        self._RequestId = None

    @property
    def DealNames(self):
        """Order name in array
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

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
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    """CreateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API
        :type Zone: str
        :param _Memory: Instance memory size in GB
        :type Memory: int
        :param _Storage: Instance storage capacity in GB
        :type Storage: int
        :param _InstanceChargeType: Billing mode. Valid value: POSTPAID (pay-as-you-go).
        :type InstanceChargeType: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _GoodsNum: Number of instances purchased this time. Default value: 1. Maximum value: 10
        :type GoodsNum: int
        :param _SubnetId: VPC subnet ID in the format of subnet-bdoe83fa. `SubnetId` and `VpcId` should be set or ignored simultaneously
        :type SubnetId: str
        :param _VpcId: VPC ID in the format of vpc-dsp338hz. `SubnetId` and `VpcId` should be set or ignored simultaneously
        :type VpcId: str
        :param _Period: Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48
        :type Period: int
        :param _AutoVoucher: Whether to automatically use voucher. 0: no, 1: yes. Default value: no
        :type AutoVoucher: int
        :param _VoucherIds: Array of voucher IDs (currently, only one voucher can be used per order)
        :type VoucherIds: list of str
        :param _DBVersion: SQL Server version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The available version varies by region, and you can pull the version information by calling the `DescribeProductConfig` API.
        :type DBVersion: str
        :param _AutoRenewFlag: Auto-renewal flag. 0: normal renewal, 1: auto-renewal. Default value: 1.
        :type AutoRenewFlag: int
        :param _SecurityGroupList: Security group list, which contains security group IDs in the format of sg-xxx.
        :type SecurityGroupList: list of str
        :param _Weekly: Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: 1 (Monday), 2 (Tuesday), 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday).
        :type Weekly: list of int
        :param _StartTime: Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :type StartTime: str
        :param _Span: Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :type Span: int
        :param _HAType: The type of purchased high-availability instance. Valid values: DUAL (dual-server high availability), CLUSTER (cluster). Default value: DUAL.
        :type HAType: str
        :param _MultiZones: Whether to deploy across availability zones. Default value: false.
        :type MultiZones: bool
        :param _ResourceTags: Tags associated with the instances to be created
        :type ResourceTags: list of ResourceTag
        :param _Collation: Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :type Collation: str
        :param _TimeZone: System time zone. Default value: `China Standard Time`.
        :type TimeZone: str
        """
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._InstanceChargeType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._DBVersion = None
        self._AutoRenewFlag = None
        self._SecurityGroupList = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._HAType = None
        self._MultiZones = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def Zone(self):
        """Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        """Instance memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Instance storage capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceChargeType(self):
        """Billing mode. Valid value: POSTPAID (pay-as-you-go).
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GoodsNum(self):
        """Number of instances purchased this time. Default value: 1. Maximum value: 10
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        """VPC subnet ID in the format of subnet-bdoe83fa. `SubnetId` and `VpcId` should be set or ignored simultaneously
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        """VPC ID in the format of vpc-dsp338hz. `SubnetId` and `VpcId` should be set or ignored simultaneously
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        """Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        """Whether to automatically use voucher. 0: no, 1: yes. Default value: no
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """Array of voucher IDs (currently, only one voucher can be used per order)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def DBVersion(self):
        """SQL Server version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The available version varies by region, and you can pull the version information by calling the `DescribeProductConfig` API.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def AutoRenewFlag(self):
        """Auto-renewal flag. 0: normal renewal, 1: auto-renewal. Default value: 1.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SecurityGroupList(self):
        """Security group list, which contains security group IDs in the format of sg-xxx.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def Weekly(self):
        """Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: 1 (Monday), 2 (Tuesday), 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday).
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        """Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        """Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def HAType(self):
        """The type of purchased high-availability instance. Valid values: DUAL (dual-server high availability), CLUSTER (cluster). Default value: DUAL.
        :rtype: str
        """
        return self._HAType

    @HAType.setter
    def HAType(self, HAType):
        self._HAType = HAType

    @property
    def MultiZones(self):
        """Whether to deploy across availability zones. Default value: false.
        :rtype: bool
        """
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def ResourceTags(self):
        """Tags associated with the instances to be created
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        """Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        """System time zone. Default value: `China Standard Time`.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._DBVersion = params.get("DBVersion")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        self._HAType = params.get("HAType")
        self._MultiZones = params.get("MultiZones")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order name
        :type DealName: str
        :param _DealNames: Order name array
        :type DealNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._DealNames = None
        self._RequestId = None

    @property
    def DealName(self):
        """Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def DealNames(self):
        """Order name array
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

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
        self._DealName = params.get("DealName")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CreateDBRequest(AbstractModel):
    """CreateDB request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DBs: Database creation information
        :type DBs: list of DBCreateInfo
        """
        self._InstanceId = None
        self._DBs = None

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
    def DBs(self):
        """Database creation information
        :rtype: list of DBCreateInfo
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DBs") is not None:
            self._DBs = []
            for item in params.get("DBs"):
                obj = DBCreateInfo()
                obj._deserialize(item)
                self._DBs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBResponse(AbstractModel):
    """CreateDB response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateIncrementalMigrationRequest(AbstractModel):
    """CreateIncrementalMigration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration.
        :type BackupMigrationId: str
        :param _BackupFiles: Incremental backup file. If the UploadType of a full backup file is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :type BackupFiles: list of str
        :param _IsRecovery: Whether restoration is required. No: not required. Yes: required. Not required by default.
        :type IsRecovery: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._BackupFiles = None
        self._IsRecovery = None

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API CreateBackupMigration.
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def BackupFiles(self):
        """Incremental backup file. If the UploadType of a full backup file is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :rtype: list of str
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def IsRecovery(self):
        """Whether restoration is required. No: not required. Yes: required. Not required by default.
        :rtype: str
        """
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._BackupFiles = params.get("BackupFiles")
        self._IsRecovery = params.get("IsRecovery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIncrementalMigrationResponse(AbstractModel):
    """CreateIncrementalMigration response structure.

    """

    def __init__(self):
        r"""
        :param _IncrementalMigrationId: ID of an incremental backup import task
        :type IncrementalMigrationId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IncrementalMigrationId = None
        self._RequestId = None

    @property
    def IncrementalMigrationId(self):
        """ID of an incremental backup import task
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId

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
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        self._RequestId = params.get("RequestId")


class CreateMigrationRequest(AbstractModel):
    """CreateMigration request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateName: Migration task name
        :type MigrateName: str
        :param _MigrateType: Migration type (1: structure migration, 2: data migration, 3: incremental sync)
        :type MigrateType: int
        :param _SourceType: Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :type SourceType: int
        :param _Source: Migration source
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param _Target: Migration target
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param _MigrateDBSet: Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5)
        :type MigrateDBSet: list of MigrateDB
        :param _RenameRestore: Restore and rename the databases listed in `ReNameRestoreDatabase`. If this parameter is left empty, all restored databases will be renamed in the default format. This parameter takes effect only when `SourceType=5`.
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self._MigrateName = None
        self._MigrateType = None
        self._SourceType = None
        self._Source = None
        self._Target = None
        self._MigrateDBSet = None
        self._RenameRestore = None

    @property
    def MigrateName(self):
        """Migration task name
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def MigrateType(self):
        """Migration type (1: structure migration, 2: data migration, 3: incremental sync)
        :rtype: int
        """
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def SourceType(self):
        """Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Source(self):
        """Migration source
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        """Migration target
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def MigrateDBSet(self):
        """Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5)
        :rtype: list of MigrateDB
        """
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet

    @property
    def RenameRestore(self):
        """Restore and rename the databases listed in `ReNameRestoreDatabase`. If this parameter is left empty, all restored databases will be renamed in the default format. This parameter takes effect only when `SourceType=5`.
        :rtype: list of RenameRestoreDatabase
        """
        return self._RenameRestore

    @RenameRestore.setter
    def RenameRestore(self, RenameRestore):
        self._RenameRestore = RenameRestore


    def _deserialize(self, params):
        self._MigrateName = params.get("MigrateName")
        self._MigrateType = params.get("MigrateType")
        self._SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self._Source = MigrateSource()
            self._Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self._Target = MigrateTarget()
            self._Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self._MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self._MigrateDBSet.append(obj)
        if params.get("RenameRestore") is not None:
            self._RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationResponse(AbstractModel):
    """CreateMigration response structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MigrateId = None
        self._RequestId = None

    @property
    def MigrateId(self):
        """Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

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
        self._MigrateId = params.get("MigrateId")
        self._RequestId = params.get("RequestId")


class CreateReadOnlyDBInstancesRequest(AbstractModel):
    """CreateReadOnlyDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: 
        :type InstanceId: str
        :param _Zone: 
        :type Zone: str
        :param _ReadOnlyGroupType: 
        :type ReadOnlyGroupType: int
        :param _Memory: 
        :type Memory: int
        :param _Storage: 
        :type Storage: int
        :param _ReadOnlyGroupForcedUpgrade: 
        :type ReadOnlyGroupForcedUpgrade: int
        :param _ReadOnlyGroupId: 
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: 
        :type ReadOnlyGroupName: str
        :param _ReadOnlyGroupIsOfflineDelay: 
        :type ReadOnlyGroupIsOfflineDelay: int
        :param _ReadOnlyGroupMaxDelayTime: 
        :type ReadOnlyGroupMaxDelayTime: int
        :param _ReadOnlyGroupMinInGroup: 
        :type ReadOnlyGroupMinInGroup: int
        :param _InstanceChargeType: 
        :type InstanceChargeType: str
        :param _GoodsNum: 
        :type GoodsNum: int
        :param _SubnetId: 
        :type SubnetId: str
        :param _VpcId: 
        :type VpcId: str
        :param _Period: 
        :type Period: int
        :param _SecurityGroupList: 
        :type SecurityGroupList: list of str
        :param _AutoVoucher: 
        :type AutoVoucher: int
        :param _VoucherIds: 
        :type VoucherIds: list of str
        :param _ResourceTags: 
        :type ResourceTags: list of ResourceTag
        :param _Collation: 
        :type Collation: str
        :param _TimeZone: 
        :type TimeZone: str
        """
        self._InstanceId = None
        self._Zone = None
        self._ReadOnlyGroupType = None
        self._Memory = None
        self._Storage = None
        self._ReadOnlyGroupForcedUpgrade = None
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._ReadOnlyGroupIsOfflineDelay = None
        self._ReadOnlyGroupMaxDelayTime = None
        self._ReadOnlyGroupMinInGroup = None
        self._InstanceChargeType = None
        self._GoodsNum = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._SecurityGroupList = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._ResourceTags = None
        self._Collation = None
        self._TimeZone = None

    @property
    def InstanceId(self):
        """
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        """
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ReadOnlyGroupType(self):
        """
        :rtype: int
        """
        return self._ReadOnlyGroupType

    @ReadOnlyGroupType.setter
    def ReadOnlyGroupType(self, ReadOnlyGroupType):
        self._ReadOnlyGroupType = ReadOnlyGroupType

    @property
    def Memory(self):
        """
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ReadOnlyGroupForcedUpgrade(self):
        """
        :rtype: int
        """
        return self._ReadOnlyGroupForcedUpgrade

    @ReadOnlyGroupForcedUpgrade.setter
    def ReadOnlyGroupForcedUpgrade(self, ReadOnlyGroupForcedUpgrade):
        self._ReadOnlyGroupForcedUpgrade = ReadOnlyGroupForcedUpgrade

    @property
    def ReadOnlyGroupId(self):
        """
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        """
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ReadOnlyGroupIsOfflineDelay(self):
        """
        :rtype: int
        """
        return self._ReadOnlyGroupIsOfflineDelay

    @ReadOnlyGroupIsOfflineDelay.setter
    def ReadOnlyGroupIsOfflineDelay(self, ReadOnlyGroupIsOfflineDelay):
        self._ReadOnlyGroupIsOfflineDelay = ReadOnlyGroupIsOfflineDelay

    @property
    def ReadOnlyGroupMaxDelayTime(self):
        """
        :rtype: int
        """
        return self._ReadOnlyGroupMaxDelayTime

    @ReadOnlyGroupMaxDelayTime.setter
    def ReadOnlyGroupMaxDelayTime(self, ReadOnlyGroupMaxDelayTime):
        self._ReadOnlyGroupMaxDelayTime = ReadOnlyGroupMaxDelayTime

    @property
    def ReadOnlyGroupMinInGroup(self):
        """
        :rtype: int
        """
        return self._ReadOnlyGroupMinInGroup

    @ReadOnlyGroupMinInGroup.setter
    def ReadOnlyGroupMinInGroup(self, ReadOnlyGroupMinInGroup):
        self._ReadOnlyGroupMinInGroup = ReadOnlyGroupMinInGroup

    @property
    def InstanceChargeType(self):
        """
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def GoodsNum(self):
        """
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        """
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        """
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        """
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        """
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoVoucher(self):
        """
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ResourceTags(self):
        """
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        """
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        """
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._ReadOnlyGroupType = params.get("ReadOnlyGroupType")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._ReadOnlyGroupForcedUpgrade = params.get("ReadOnlyGroupForcedUpgrade")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._ReadOnlyGroupIsOfflineDelay = params.get("ReadOnlyGroupIsOfflineDelay")
        self._ReadOnlyGroupMaxDelayTime = params.get("ReadOnlyGroupMaxDelayTime")
        self._ReadOnlyGroupMinInGroup = params.get("ReadOnlyGroupMinInGroup")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._GoodsNum = params.get("GoodsNum")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyDBInstancesResponse(AbstractModel):
    """CreateReadOnlyDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: 
        :type DealNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealNames = None
        self._RequestId = None

    @property
    def DealNames(self):
        """
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

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
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CrossBackupAddr(AbstractModel):
    """All Download addresses of cross-region backup

    """

    def __init__(self):
        r"""
        :param _CrossRegion: The target region of cross-region backup
        :type CrossRegion: str
        :param _CrossInternalAddr: The address used to download the cross-region backup over a private network
        :type CrossInternalAddr: str
        :param _CrossExternalAddr: The address used to download the cross-region backup over a public network
        :type CrossExternalAddr: str
        """
        self._CrossRegion = None
        self._CrossInternalAddr = None
        self._CrossExternalAddr = None

    @property
    def CrossRegion(self):
        """The target region of cross-region backup
        :rtype: str
        """
        return self._CrossRegion

    @CrossRegion.setter
    def CrossRegion(self, CrossRegion):
        self._CrossRegion = CrossRegion

    @property
    def CrossInternalAddr(self):
        """The address used to download the cross-region backup over a private network
        :rtype: str
        """
        return self._CrossInternalAddr

    @CrossInternalAddr.setter
    def CrossInternalAddr(self, CrossInternalAddr):
        self._CrossInternalAddr = CrossInternalAddr

    @property
    def CrossExternalAddr(self):
        """The address used to download the cross-region backup over a public network
        :rtype: str
        """
        return self._CrossExternalAddr

    @CrossExternalAddr.setter
    def CrossExternalAddr(self, CrossExternalAddr):
        self._CrossExternalAddr = CrossExternalAddr


    def _deserialize(self, params):
        self._CrossRegion = params.get("CrossRegion")
        self._CrossInternalAddr = params.get("CrossInternalAddr")
        self._CrossExternalAddr = params.get("CrossExternalAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CrossRegionStatus(AbstractModel):
    """The target region and status of cross-region backup

    """

    def __init__(self):
        r"""
        :param _CrossRegion: The target region of cross-region backup
        :type CrossRegion: str
        :param _CrossStatus: Synchronization status of cross-region backup. Valid values: `0` (creating), `1` (succeeded), `2`: (failed), `4` (syncing)
        :type CrossStatus: int
        """
        self._CrossRegion = None
        self._CrossStatus = None

    @property
    def CrossRegion(self):
        """The target region of cross-region backup
        :rtype: str
        """
        return self._CrossRegion

    @CrossRegion.setter
    def CrossRegion(self, CrossRegion):
        self._CrossRegion = CrossRegion

    @property
    def CrossStatus(self):
        """Synchronization status of cross-region backup. Valid values: `0` (creating), `1` (succeeded), `2`: (failed), `4` (syncing)
        :rtype: int
        """
        return self._CrossStatus

    @CrossStatus.setter
    def CrossStatus(self, CrossStatus):
        self._CrossStatus = CrossStatus


    def _deserialize(self, params):
        self._CrossRegion = params.get("CrossRegion")
        self._CrossStatus = params.get("CrossStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBCreateInfo(AbstractModel):
    """Database creation information

    """

    def __init__(self):
        r"""
        :param _DBName: Database name
        :type DBName: str
        :param _Charset: Character set, which can be queried by the `DescribeDBCharsets` API. Default value: `Chinese_PRC_CI_AS`.
        :type Charset: str
        :param _Accounts: Database account permission information
        :type Accounts: list of AccountPrivilege
        :param _Remark: Remarks
        :type Remark: str
        """
        self._DBName = None
        self._Charset = None
        self._Accounts = None
        self._Remark = None

    @property
    def DBName(self):
        """Database name
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Charset(self):
        """Character set, which can be queried by the `DescribeDBCharsets` API. Default value: `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def Accounts(self):
        """Database account permission information
        :rtype: list of AccountPrivilege
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def Remark(self):
        """Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._Charset = params.get("Charset")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBDetail(AbstractModel):
    """Database information

    """

    def __init__(self):
        r"""
        :param _Name: Database name
        :type Name: str
        :param _Charset: Character set
        :type Charset: str
        :param _Remark: Remarks
        :type Remark: str
        :param _CreateTime: Database creation time
        :type CreateTime: str
        :param _Status: Database status. 1: creating, 2: running, 3: modifying, -1: dropping
        :type Status: int
        :param _Accounts: Database account permission information
        :type Accounts: list of AccountPrivilege
        :param _InternalStatus: Internal status. ONLINE: running
        :type InternalStatus: str
        :param _Encryption: TDE status. Valid values: `enable` (enabled), `disable` (disabled).
        :type Encryption: str
        """
        self._Name = None
        self._Charset = None
        self._Remark = None
        self._CreateTime = None
        self._Status = None
        self._Accounts = None
        self._InternalStatus = None
        self._Encryption = None

    @property
    def Name(self):
        """Database name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Charset(self):
        """Character set
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def Remark(self):
        """Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """Database creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        """Database status. 1: creating, 2: running, 3: modifying, -1: dropping
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Accounts(self):
        """Database account permission information
        :rtype: list of AccountPrivilege
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def InternalStatus(self):
        """Internal status. ONLINE: running
        :rtype: str
        """
        return self._InternalStatus

    @InternalStatus.setter
    def InternalStatus(self, InternalStatus):
        self._InternalStatus = InternalStatus

    @property
    def Encryption(self):
        """TDE status. Valid values: `enable` (enabled), `disable` (disabled).
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Charset = params.get("Charset")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._InternalStatus = params.get("InternalStatus")
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    """Instance details

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Name: Instance name
        :type Name: str
        :param _ProjectId: Project ID of instance
        :type ProjectId: int
        :param _RegionId: Instance region ID
        :type RegionId: int
        :param _ZoneId: Instance AZ ID
        :type ZoneId: int
        :param _VpcId: Instance VPC ID, which will be 0 if the basic network is used
        :type VpcId: int
        :param _SubnetId: Instance VPC subnet ID, which will be 0 if the basic network is used
        :type SubnetId: int
        :param _Status: Instance status. Valid values: <li>1: creating</li> <li>2: running</li> <li>3: instance operations restricted (due to the ongoing primary-replica switch)</li> <li>4: isolated</li> <li>5: repossessing</li> <li>6: repossessed</li> <li>7: running tasks (such as backup and rollback tasks)</li> <li>8: eliminated</li> <li>9: expanding capacity</li> <li>10: migrating</li> <li>11: read-only</li> <li>12: restarting</li>  <li>13: modifying configuration and waiting for switch</li> <li>14: implementing pub/sub</li> <li>15: modifying pub/sub configuration</li> <li>16: modifying configuration and switching</li> <li>17: creating read-only instances</li>
        :type Status: int
        :param _Vip: Instance access IP
        :type Vip: str
        :param _Vport: Instance access port
        :type Vport: int
        :param _CreateTime: Instance creation time
        :type CreateTime: str
        :param _UpdateTime: Instance update time
        :type UpdateTime: str
        :param _StartTime: Instance billing start time
        :type StartTime: str
        :param _EndTime: Instance billing end time
        :type EndTime: str
        :param _IsolateTime: Instance isolation time
        :type IsolateTime: str
        :param _Memory: Instance memory size in GB
        :type Memory: int
        :param _UsedStorage: Used storage capacity of instance in GB
        :type UsedStorage: int
        :param _Storage: Instance storage capacity in GB
        :type Storage: int
        :param _VersionName: Instance version
        :type VersionName: str
        :param _RenewFlag: Instance renewal flag
        :type RenewFlag: int
        :param _Model: High-availability instance type. Valid values: 1 (dual-server high-availability), 2 (standalone), 3 (multi-AZ), 4 (multi-AZ cluster), 5 (cluster), 9 (private consumption)
        :type Model: int
        :param _Region: Instance region name, such as ap-guangzhou
        :type Region: str
        :param _Zone: Instance AZ name, such as ap-guangzhou-1
        :type Zone: str
        :param _BackupTime: Backup time point
        :type BackupTime: str
        :param _PayMode: Instance billing mode. 0: pay-as-you-go
        :type PayMode: int
        :param _Uid: Instance UID
        :type Uid: str
        :param _Cpu: Number of CPU cores of instance
        :type Cpu: int
        :param _Version: Instance version code
        :type Version: str
        :param _Type: Instance type. Valid values: `TS85` (physical machine, local SSD), `Z3` (early version of physical machine, local SSD), `CLOUD_BASIC` (virtual machine, HDD cloud disk), `CLOUD_PREMIUM` (virtual machine, premium cloud disk), `CLOUD_SSD` (virtual machine, SSD), `CLOUD_HSSD` (virtual machine, enhanced SSD), `CLOUD_TSSD` (virtual machine, ulTra SSD), `CLOUD_BSSD` virtual machine, balanced SSD).
        :type Type: str
        :param _Pid: Billing ID
        :type Pid: int
        :param _UniqVpcId: Unique string-type ID of instance VPC in the format of `vpc-xxx`, which is an empty string if the basic network is used
        :type UniqVpcId: str
        :param _UniqSubnetId: Unique string-type ID of instance subnet in the format of `subnet-xxx`, which is an empty string if the basic network is used
        :type UniqSubnetId: str
        :param _IsolateOperator: Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolateOperator: str
        :param _SubFlag: Note: This field may return null, indicating that no valid values can be obtained.
        :type SubFlag: str
        :param _ROFlag: Note: This field may return null, indicating that no valid values can be obtained.
        :type ROFlag: str
        :param _HAFlag: Note: This field may return null, indicating that no valid values can be obtained.
        :type HAFlag: str
        :param _ResourceTags: Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceTags: list of ResourceTag
        :param _BackupModel: Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupModel: str
        :param _InstanceNote: Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceNote: str
        :param _BackupCycle: Backup cycle
        :type BackupCycle: list of int
        :param _BackupCycleType: Backup cycle type. Valid values: `daily`, `weekly`, `monthly`.
        :type BackupCycleType: str
        :param _BackupSaveDays: Data (log) backup retention period
        :type BackupSaveDays: int
        :param _InstanceType: Instance type. Valid values: `HA` (high-availability), `RO` (read-only), `SI` (basic edition), `BI` (business intelligence service).
        :type InstanceType: str
        :param _CrossRegions: The target region of cross-region backup. If this parameter left empty, it indicates that cross-region backup is disabled.
        :type CrossRegions: list of str
        :param _CrossBackupEnabled: Cross-region backup status. Valid values: `enable` (enabled), `disable` (disabed)
        :type CrossBackupEnabled: str
        :param _CrossBackupSaveDays: The retention period of cross-region backup. Default value: 7 days
        :type CrossBackupSaveDays: int
        :param _DnsPodDomain: Domain name of the public network address
        :type DnsPodDomain: str
        :param _TgwWanVPort: Port number of the public network
        :type TgwWanVPort: int
        :param _Collation: Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :type Collation: str
        :param _TimeZone: System time zone. Default value: `China Standard Time`.
        :type TimeZone: str
        :param _IsDrZone: Whether the instance is deployed across AZs
        :type IsDrZone: bool
        :param _SlaveZones: Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaveZones: :class:`tencentcloud.sqlserver.v20180328.models.SlaveZones`
        :param _Architecture: Note: This field may return null, indicating that no valid values can be obtained.
        :type Architecture: str
        :param _Style: Note: This field may return null, indicating that no valid values can be obtained.
        :type Style: str
        """
        self._InstanceId = None
        self._Name = None
        self._ProjectId = None
        self._RegionId = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._Vip = None
        self._Vport = None
        self._CreateTime = None
        self._UpdateTime = None
        self._StartTime = None
        self._EndTime = None
        self._IsolateTime = None
        self._Memory = None
        self._UsedStorage = None
        self._Storage = None
        self._VersionName = None
        self._RenewFlag = None
        self._Model = None
        self._Region = None
        self._Zone = None
        self._BackupTime = None
        self._PayMode = None
        self._Uid = None
        self._Cpu = None
        self._Version = None
        self._Type = None
        self._Pid = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._IsolateOperator = None
        self._SubFlag = None
        self._ROFlag = None
        self._HAFlag = None
        self._ResourceTags = None
        self._BackupModel = None
        self._InstanceNote = None
        self._BackupCycle = None
        self._BackupCycleType = None
        self._BackupSaveDays = None
        self._InstanceType = None
        self._CrossRegions = None
        self._CrossBackupEnabled = None
        self._CrossBackupSaveDays = None
        self._DnsPodDomain = None
        self._TgwWanVPort = None
        self._Collation = None
        self._TimeZone = None
        self._IsDrZone = None
        self._SlaveZones = None
        self._Architecture = None
        self._Style = None

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
    def Name(self):
        """Instance name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProjectId(self):
        """Project ID of instance
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        """Instance region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        """Instance AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        """Instance VPC ID, which will be 0 if the basic network is used
        :rtype: int
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Instance VPC subnet ID, which will be 0 if the basic network is used
        :rtype: int
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        """Instance status. Valid values: <li>1: creating</li> <li>2: running</li> <li>3: instance operations restricted (due to the ongoing primary-replica switch)</li> <li>4: isolated</li> <li>5: repossessing</li> <li>6: repossessed</li> <li>7: running tasks (such as backup and rollback tasks)</li> <li>8: eliminated</li> <li>9: expanding capacity</li> <li>10: migrating</li> <li>11: read-only</li> <li>12: restarting</li>  <li>13: modifying configuration and waiting for switch</li> <li>14: implementing pub/sub</li> <li>15: modifying pub/sub configuration</li> <li>16: modifying configuration and switching</li> <li>17: creating read-only instances</li>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        """Instance access IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Instance access port
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CreateTime(self):
        """Instance creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Instance update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        """Instance billing start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Instance billing end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IsolateTime(self):
        """Instance isolation time
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def Memory(self):
        """Instance memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def UsedStorage(self):
        """Used storage capacity of instance in GB
        :rtype: int
        """
        return self._UsedStorage

    @UsedStorage.setter
    def UsedStorage(self, UsedStorage):
        self._UsedStorage = UsedStorage

    @property
    def Storage(self):
        """Instance storage capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def VersionName(self):
        """Instance version
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def RenewFlag(self):
        """Instance renewal flag
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Model(self):
        """High-availability instance type. Valid values: 1 (dual-server high-availability), 2 (standalone), 3 (multi-AZ), 4 (multi-AZ cluster), 5 (cluster), 9 (private consumption)
        :rtype: int
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Region(self):
        """Instance region name, such as ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """Instance AZ name, such as ap-guangzhou-1
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def BackupTime(self):
        """Backup time point
        :rtype: str
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def PayMode(self):
        """Instance billing mode. 0: pay-as-you-go
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Uid(self):
        """Instance UID
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Cpu(self):
        """Number of CPU cores of instance
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Version(self):
        """Instance version code
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Type(self):
        """Instance type. Valid values: `TS85` (physical machine, local SSD), `Z3` (early version of physical machine, local SSD), `CLOUD_BASIC` (virtual machine, HDD cloud disk), `CLOUD_PREMIUM` (virtual machine, premium cloud disk), `CLOUD_SSD` (virtual machine, SSD), `CLOUD_HSSD` (virtual machine, enhanced SSD), `CLOUD_TSSD` (virtual machine, ulTra SSD), `CLOUD_BSSD` virtual machine, balanced SSD).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Pid(self):
        """Billing ID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def UniqVpcId(self):
        """Unique string-type ID of instance VPC in the format of `vpc-xxx`, which is an empty string if the basic network is used
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        """Unique string-type ID of instance subnet in the format of `subnet-xxx`, which is an empty string if the basic network is used
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def IsolateOperator(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolateOperator

    @IsolateOperator.setter
    def IsolateOperator(self, IsolateOperator):
        self._IsolateOperator = IsolateOperator

    @property
    def SubFlag(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubFlag

    @SubFlag.setter
    def SubFlag(self, SubFlag):
        self._SubFlag = SubFlag

    @property
    def ROFlag(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ROFlag

    @ROFlag.setter
    def ROFlag(self, ROFlag):
        self._ROFlag = ROFlag

    @property
    def HAFlag(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HAFlag

    @HAFlag.setter
    def HAFlag(self, HAFlag):
        self._HAFlag = HAFlag

    @property
    def ResourceTags(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def BackupModel(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupModel

    @BackupModel.setter
    def BackupModel(self, BackupModel):
        self._BackupModel = BackupModel

    @property
    def InstanceNote(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceNote

    @InstanceNote.setter
    def InstanceNote(self, InstanceNote):
        self._InstanceNote = InstanceNote

    @property
    def BackupCycle(self):
        """Backup cycle
        :rtype: list of int
        """
        return self._BackupCycle

    @BackupCycle.setter
    def BackupCycle(self, BackupCycle):
        self._BackupCycle = BackupCycle

    @property
    def BackupCycleType(self):
        """Backup cycle type. Valid values: `daily`, `weekly`, `monthly`.
        :rtype: str
        """
        return self._BackupCycleType

    @BackupCycleType.setter
    def BackupCycleType(self, BackupCycleType):
        self._BackupCycleType = BackupCycleType

    @property
    def BackupSaveDays(self):
        """Data (log) backup retention period
        :rtype: int
        """
        return self._BackupSaveDays

    @BackupSaveDays.setter
    def BackupSaveDays(self, BackupSaveDays):
        self._BackupSaveDays = BackupSaveDays

    @property
    def InstanceType(self):
        """Instance type. Valid values: `HA` (high-availability), `RO` (read-only), `SI` (basic edition), `BI` (business intelligence service).
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def CrossRegions(self):
        """The target region of cross-region backup. If this parameter left empty, it indicates that cross-region backup is disabled.
        :rtype: list of str
        """
        return self._CrossRegions

    @CrossRegions.setter
    def CrossRegions(self, CrossRegions):
        self._CrossRegions = CrossRegions

    @property
    def CrossBackupEnabled(self):
        """Cross-region backup status. Valid values: `enable` (enabled), `disable` (disabed)
        :rtype: str
        """
        return self._CrossBackupEnabled

    @CrossBackupEnabled.setter
    def CrossBackupEnabled(self, CrossBackupEnabled):
        self._CrossBackupEnabled = CrossBackupEnabled

    @property
    def CrossBackupSaveDays(self):
        """The retention period of cross-region backup. Default value: 7 days
        :rtype: int
        """
        return self._CrossBackupSaveDays

    @CrossBackupSaveDays.setter
    def CrossBackupSaveDays(self, CrossBackupSaveDays):
        self._CrossBackupSaveDays = CrossBackupSaveDays

    @property
    def DnsPodDomain(self):
        """Domain name of the public network address
        :rtype: str
        """
        return self._DnsPodDomain

    @DnsPodDomain.setter
    def DnsPodDomain(self, DnsPodDomain):
        self._DnsPodDomain = DnsPodDomain

    @property
    def TgwWanVPort(self):
        """Port number of the public network
        :rtype: int
        """
        return self._TgwWanVPort

    @TgwWanVPort.setter
    def TgwWanVPort(self, TgwWanVPort):
        self._TgwWanVPort = TgwWanVPort

    @property
    def Collation(self):
        """Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        """System time zone. Default value: `China Standard Time`.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def IsDrZone(self):
        """Whether the instance is deployed across AZs
        :rtype: bool
        """
        return self._IsDrZone

    @IsDrZone.setter
    def IsDrZone(self, IsDrZone):
        self._IsDrZone = IsDrZone

    @property
    def SlaveZones(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.SlaveZones`
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def Architecture(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def Style(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IsolateTime = params.get("IsolateTime")
        self._Memory = params.get("Memory")
        self._UsedStorage = params.get("UsedStorage")
        self._Storage = params.get("Storage")
        self._VersionName = params.get("VersionName")
        self._RenewFlag = params.get("RenewFlag")
        self._Model = params.get("Model")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._BackupTime = params.get("BackupTime")
        self._PayMode = params.get("PayMode")
        self._Uid = params.get("Uid")
        self._Cpu = params.get("Cpu")
        self._Version = params.get("Version")
        self._Type = params.get("Type")
        self._Pid = params.get("Pid")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._IsolateOperator = params.get("IsolateOperator")
        self._SubFlag = params.get("SubFlag")
        self._ROFlag = params.get("ROFlag")
        self._HAFlag = params.get("HAFlag")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._BackupModel = params.get("BackupModel")
        self._InstanceNote = params.get("InstanceNote")
        self._BackupCycle = params.get("BackupCycle")
        self._BackupCycleType = params.get("BackupCycleType")
        self._BackupSaveDays = params.get("BackupSaveDays")
        self._InstanceType = params.get("InstanceType")
        self._CrossRegions = params.get("CrossRegions")
        self._CrossBackupEnabled = params.get("CrossBackupEnabled")
        self._CrossBackupSaveDays = params.get("CrossBackupSaveDays")
        self._DnsPodDomain = params.get("DnsPodDomain")
        self._TgwWanVPort = params.get("TgwWanVPort")
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        self._IsDrZone = params.get("IsDrZone")
        if params.get("SlaveZones") is not None:
            self._SlaveZones = SlaveZones()
            self._SlaveZones._deserialize(params.get("SlaveZones"))
        self._Architecture = params.get("Architecture")
        self._Style = params.get("Style")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBPrivilege(AbstractModel):
    """Database permission information of account

    """

    def __init__(self):
        r"""
        :param _DBName: Database name
        :type DBName: str
        :param _Privilege: Database permissions. Valid values: `ReadWrite` (read-write), `ReadOnly` (read-only), `DBOwner` (owner)
        :type Privilege: str
        """
        self._DBName = None
        self._Privilege = None

    @property
    def DBName(self):
        """Database name
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Privilege(self):
        """Database permissions. Valid values: `ReadWrite` (read-write), `ReadOnly` (read-only), `DBOwner` (owner)
        :rtype: str
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBPrivilegeModifyInfo(AbstractModel):
    """Database permission change information

    """

    def __init__(self):
        r"""
        :param _DBName: Database name
        :type DBName: str
        :param _Privilege: Permission modification information. Valid values: `ReadWrite` (read-write), `ReadOnly` (read-only), `Delete` (delete the account's permission to this database), `DBOwner` (owner).
        :type Privilege: str
        """
        self._DBName = None
        self._Privilege = None

    @property
    def DBName(self):
        """Database name
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Privilege(self):
        """Permission modification information. Valid values: `ReadWrite` (read-write), `ReadOnly` (read-only), `Delete` (delete the account's permission to this database), `DBOwner` (owner).
        :rtype: str
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBRemark(AbstractModel):
    """Database remarks

    """

    def __init__(self):
        r"""
        :param _Name: Database name
        :type Name: str
        :param _Remark: Remarks
        :type Remark: str
        """
        self._Name = None
        self._Remark = None

    @property
    def Name(self):
        """Database name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBRenameRes(AbstractModel):
    """Database renaming response parameter

    """

    def __init__(self):
        r"""
        :param _NewName: Name of the new database
        :type NewName: str
        :param _OldName: Name of the old database
        :type OldName: str
        """
        self._NewName = None
        self._OldName = None

    @property
    def NewName(self):
        """Name of the new database
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName

    @property
    def OldName(self):
        """Name of the old database
        :rtype: str
        """
        return self._OldName

    @OldName.setter
    def OldName(self, OldName):
        self._OldName = OldName


    def _deserialize(self, params):
        self._NewName = params.get("NewName")
        self._OldName = params.get("OldName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBTDEEncrypt(AbstractModel):
    """This example shows you how to enable or disable TDE of a database.

    """

    def __init__(self):
        r"""
        :param _DBName: 
        :type DBName: str
        :param _Encryption: TDE status. Valid values: `enable` (enabled), `disable` (disabled).
        :type Encryption: str
        """
        self._DBName = None
        self._Encryption = None

    @property
    def DBName(self):
        """
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Encryption(self):
        """TDE status. Valid values: `enable` (enabled), `disable` (disabled).
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbNormalDetail(AbstractModel):
    """Database configurations

    """

    def __init__(self):
        r"""
        :param _IsSubscribed: Whether it is subscribed. Valid values: `0` (no), `1` (yes)
        :type IsSubscribed: str
        :param _CollationName: Database collation
        :type CollationName: str
        :param _IsAutoCleanupOn: Whether the cleanup task is enabled to automatically remove old change tracking information when CT is enabled. Valid values: `0` (no), `1` (yes)
        :type IsAutoCleanupOn: str
        :param _IsBrokerEnabled: Whether SQL Server Service Broker is enabled. Valid values: `0` (no), `1` (yes)
        :type IsBrokerEnabled: str
        :param _IsCdcEnabled: Whether CDC is enabled. Valid values: `0` (disabled), `1` (enabled)
        :type IsCdcEnabled: str
        :param _IsDbChainingOn: Whether CT is enabled. Valid values: `0` (disabled), `1` (enabled)
        :type IsDbChainingOn: str
        :param _IsEncrypted: Whether it is encrypted. Valid values: `0` (no), `1` (yes)
        :type IsEncrypted: str
        :param _IsFulltextEnabled: Whether full-text indexes are enabled. Valid values: `0` (no), `1` (yes)
        :type IsFulltextEnabled: str
        :param _IsMirroring: Whether it is a mirror database. Valid values: `0` (no), `1` (yes)
        :type IsMirroring: str
        :param _IsPublished: Whether it is published. Valid values: `0` (no), `1` (yes)
        :type IsPublished: str
        :param _IsReadCommittedSnapshotOn: Whether snapshots are enabled. Valid values: `0` (no), `1` (yes)
        :type IsReadCommittedSnapshotOn: str
        :param _IsTrustworthyOn: Whether it is trustworthy. Valid values: `0` (no), `1` (yes)
        :type IsTrustworthyOn: str
        :param _MirroringState: Mirroring state
        :type MirroringState: str
        :param _Name: Database name
        :type Name: str
        :param _RecoveryModelDesc: Recovery model
        :type RecoveryModelDesc: str
        :param _RetentionPeriod: Retention period (in days) of change tracking information
        :type RetentionPeriod: str
        :param _StateDesc: Database status
        :type StateDesc: str
        :param _UserAccessDesc: User type
        :type UserAccessDesc: str
        :param _CreateTime: Database creation time
        :type CreateTime: str
        """
        self._IsSubscribed = None
        self._CollationName = None
        self._IsAutoCleanupOn = None
        self._IsBrokerEnabled = None
        self._IsCdcEnabled = None
        self._IsDbChainingOn = None
        self._IsEncrypted = None
        self._IsFulltextEnabled = None
        self._IsMirroring = None
        self._IsPublished = None
        self._IsReadCommittedSnapshotOn = None
        self._IsTrustworthyOn = None
        self._MirroringState = None
        self._Name = None
        self._RecoveryModelDesc = None
        self._RetentionPeriod = None
        self._StateDesc = None
        self._UserAccessDesc = None
        self._CreateTime = None

    @property
    def IsSubscribed(self):
        """Whether it is subscribed. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsSubscribed

    @IsSubscribed.setter
    def IsSubscribed(self, IsSubscribed):
        self._IsSubscribed = IsSubscribed

    @property
    def CollationName(self):
        """Database collation
        :rtype: str
        """
        return self._CollationName

    @CollationName.setter
    def CollationName(self, CollationName):
        self._CollationName = CollationName

    @property
    def IsAutoCleanupOn(self):
        """Whether the cleanup task is enabled to automatically remove old change tracking information when CT is enabled. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsAutoCleanupOn

    @IsAutoCleanupOn.setter
    def IsAutoCleanupOn(self, IsAutoCleanupOn):
        self._IsAutoCleanupOn = IsAutoCleanupOn

    @property
    def IsBrokerEnabled(self):
        """Whether SQL Server Service Broker is enabled. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsBrokerEnabled

    @IsBrokerEnabled.setter
    def IsBrokerEnabled(self, IsBrokerEnabled):
        self._IsBrokerEnabled = IsBrokerEnabled

    @property
    def IsCdcEnabled(self):
        """Whether CDC is enabled. Valid values: `0` (disabled), `1` (enabled)
        :rtype: str
        """
        return self._IsCdcEnabled

    @IsCdcEnabled.setter
    def IsCdcEnabled(self, IsCdcEnabled):
        self._IsCdcEnabled = IsCdcEnabled

    @property
    def IsDbChainingOn(self):
        """Whether CT is enabled. Valid values: `0` (disabled), `1` (enabled)
        :rtype: str
        """
        return self._IsDbChainingOn

    @IsDbChainingOn.setter
    def IsDbChainingOn(self, IsDbChainingOn):
        self._IsDbChainingOn = IsDbChainingOn

    @property
    def IsEncrypted(self):
        """Whether it is encrypted. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsEncrypted

    @IsEncrypted.setter
    def IsEncrypted(self, IsEncrypted):
        self._IsEncrypted = IsEncrypted

    @property
    def IsFulltextEnabled(self):
        warnings.warn("parameter `IsFulltextEnabled` is deprecated", DeprecationWarning) 

        """Whether full-text indexes are enabled. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsFulltextEnabled

    @IsFulltextEnabled.setter
    def IsFulltextEnabled(self, IsFulltextEnabled):
        warnings.warn("parameter `IsFulltextEnabled` is deprecated", DeprecationWarning) 

        self._IsFulltextEnabled = IsFulltextEnabled

    @property
    def IsMirroring(self):
        """Whether it is a mirror database. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsMirroring

    @IsMirroring.setter
    def IsMirroring(self, IsMirroring):
        self._IsMirroring = IsMirroring

    @property
    def IsPublished(self):
        """Whether it is published. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsPublished

    @IsPublished.setter
    def IsPublished(self, IsPublished):
        self._IsPublished = IsPublished

    @property
    def IsReadCommittedSnapshotOn(self):
        """Whether snapshots are enabled. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsReadCommittedSnapshotOn

    @IsReadCommittedSnapshotOn.setter
    def IsReadCommittedSnapshotOn(self, IsReadCommittedSnapshotOn):
        self._IsReadCommittedSnapshotOn = IsReadCommittedSnapshotOn

    @property
    def IsTrustworthyOn(self):
        """Whether it is trustworthy. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsTrustworthyOn

    @IsTrustworthyOn.setter
    def IsTrustworthyOn(self, IsTrustworthyOn):
        self._IsTrustworthyOn = IsTrustworthyOn

    @property
    def MirroringState(self):
        """Mirroring state
        :rtype: str
        """
        return self._MirroringState

    @MirroringState.setter
    def MirroringState(self, MirroringState):
        self._MirroringState = MirroringState

    @property
    def Name(self):
        """Database name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RecoveryModelDesc(self):
        """Recovery model
        :rtype: str
        """
        return self._RecoveryModelDesc

    @RecoveryModelDesc.setter
    def RecoveryModelDesc(self, RecoveryModelDesc):
        self._RecoveryModelDesc = RecoveryModelDesc

    @property
    def RetentionPeriod(self):
        """Retention period (in days) of change tracking information
        :rtype: str
        """
        return self._RetentionPeriod

    @RetentionPeriod.setter
    def RetentionPeriod(self, RetentionPeriod):
        self._RetentionPeriod = RetentionPeriod

    @property
    def StateDesc(self):
        """Database status
        :rtype: str
        """
        return self._StateDesc

    @StateDesc.setter
    def StateDesc(self, StateDesc):
        self._StateDesc = StateDesc

    @property
    def UserAccessDesc(self):
        """User type
        :rtype: str
        """
        return self._UserAccessDesc

    @UserAccessDesc.setter
    def UserAccessDesc(self, UserAccessDesc):
        self._UserAccessDesc = UserAccessDesc

    @property
    def CreateTime(self):
        """Database creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._IsSubscribed = params.get("IsSubscribed")
        self._CollationName = params.get("CollationName")
        self._IsAutoCleanupOn = params.get("IsAutoCleanupOn")
        self._IsBrokerEnabled = params.get("IsBrokerEnabled")
        self._IsCdcEnabled = params.get("IsCdcEnabled")
        self._IsDbChainingOn = params.get("IsDbChainingOn")
        self._IsEncrypted = params.get("IsEncrypted")
        self._IsFulltextEnabled = params.get("IsFulltextEnabled")
        self._IsMirroring = params.get("IsMirroring")
        self._IsPublished = params.get("IsPublished")
        self._IsReadCommittedSnapshotOn = params.get("IsReadCommittedSnapshotOn")
        self._IsTrustworthyOn = params.get("IsTrustworthyOn")
        self._MirroringState = params.get("MirroringState")
        self._Name = params.get("Name")
        self._RecoveryModelDesc = params.get("RecoveryModelDesc")
        self._RetentionPeriod = params.get("RetentionPeriod")
        self._StateDesc = params.get("StateDesc")
        self._UserAccessDesc = params.get("UserAccessDesc")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbRollbackTimeInfo(AbstractModel):
    """Information of time range available for database rollback

    """

    def __init__(self):
        r"""
        :param _DBName: Database name
        :type DBName: str
        :param _StartTime: Start time of time range available for rollback
        :type StartTime: str
        :param _EndTime: End time of time range available for rollback
        :type EndTime: str
        """
        self._DBName = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DBName(self):
        """Database name
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def StartTime(self):
        """Start time of time range available for rollback
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of time range available for rollback
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DealInfo(AbstractModel):
    """Order information

    """

    def __init__(self):
        r"""
        :param _DealName: Order name
        :type DealName: str
        :param _Count: Number of items
        :type Count: int
        :param _FlowId: ID of associated flow, which can be used to query the flow execution status
        :type FlowId: int
        :param _InstanceIdSet: This field is required only for an order that creates an instance, indicating the ID of the instance created by the order
        :type InstanceIdSet: list of str
        :param _OwnerUin: Account
        :type OwnerUin: str
        :param _InstanceChargeType: Instance billing type
        :type InstanceChargeType: str
        """
        self._DealName = None
        self._Count = None
        self._FlowId = None
        self._InstanceIdSet = None
        self._OwnerUin = None
        self._InstanceChargeType = None

    @property
    def DealName(self):
        """Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def Count(self):
        """Number of items
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def FlowId(self):
        """ID of associated flow, which can be used to query the flow execution status
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceIdSet(self):
        """This field is required only for an order that creates an instance, indicating the ID of the instance created by the order
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def OwnerUin(self):
        """Account
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def InstanceChargeType(self):
        """Instance billing type
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._Count = params.get("Count")
        self._FlowId = params.get("FlowId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._OwnerUin = params.get("OwnerUin")
        self._InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DealInstance(AbstractModel):
    """List of the resource IDs corresponding to order number

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: list of str
        :param _DealName: Order ID
        :type DealName: str
        """
        self._InstanceId = None
        self._DealName = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: list of str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealName(self):
        """Order ID
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param _UserNames: Array of instance usernames
        :type UserNames: list of str
        """
        self._InstanceId = None
        self._UserNames = None

    @property
    def InstanceId(self):
        """Database instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserNames(self):
        """Array of instance usernames
        :rtype: list of str
        """
        return self._UserNames

    @UserNames.setter
    def UserNames(self, UserNames):
        self._UserNames = UserNames


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserNames = params.get("UserNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DeleteBackupMigrationRequest(AbstractModel):
    """DeleteBackupMigration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Target instance ID, which is returned through the API DescribeBackupMigration.
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the API DescribeBackupMigration.
        :type BackupMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None

    @property
    def InstanceId(self):
        """Target instance ID, which is returned through the API DescribeBackupMigration.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API DescribeBackupMigration.
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupMigrationResponse(AbstractModel):
    """DeleteBackupMigration response structure.

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


class DeleteBusinessIntelligenceFileRequest(AbstractModel):
    """DeleteBusinessIntelligenceFile request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _FileNameSet: File name set
        :type FileNameSet: list of str
        """
        self._InstanceId = None
        self._FileNameSet = None

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
    def FileNameSet(self):
        """File name set
        :rtype: list of str
        """
        return self._FileNameSet

    @FileNameSet.setter
    def FileNameSet(self, FileNameSet):
        self._FileNameSet = FileNameSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileNameSet = params.get("FileNameSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBusinessIntelligenceFileResponse(AbstractModel):
    """DeleteBusinessIntelligenceFile response structure.

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


class DeleteDBRequest(AbstractModel):
    """DeleteDB request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-rljoi3bf
        :type InstanceId: str
        :param _Names: Array of database names
        :type Names: list of str
        """
        self._InstanceId = None
        self._Names = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-rljoi3bf
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Names(self):
        """Array of database names
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBResponse(AbstractModel):
    """DeleteDB response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DeleteIncrementalMigrationRequest(AbstractModel):
    """DeleteIncrementalMigration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Target instance ID.
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the `CreateBackupMigration` API
        :type BackupMigrationId: str
        :param _IncrementalMigrationId: Incremental backup import task ID, which is returned through the `CreateIncrementalMigration` API
        :type IncrementalMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._IncrementalMigrationId = None

    @property
    def InstanceId(self):
        """Target instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the `CreateBackupMigration` API
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        """Incremental backup import task ID, which is returned through the `CreateIncrementalMigration` API
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIncrementalMigrationResponse(AbstractModel):
    """DeleteIncrementalMigration response structure.

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


class DeleteMigrationRequest(AbstractModel):
    """DeleteMigration request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        """Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMigrationResponse(AbstractModel):
    """DeleteMigration response structure.

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


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Limit: Number of results per page. Value range: 1-100. Default value: 20
        :type Limit: int
        :param _Offset: Page number. Default value: 0
        :type Offset: int
        :param _Name: Account ID
        :type Name: str
        :param _OrderBy: Sorting by `createTime`, `updateTime`, or `passTime`. Default value: `createTime` (desc).
        :type OrderBy: str
        :param _OrderByType: Sorting rule. Valid values: `desc` (descending order), `asc` (ascending order). Default value: `desc`.
        :type OrderByType: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._Name = None
        self._OrderBy = None
        self._OrderByType = None

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
    def Limit(self):
        """Number of results per page. Value range: 1-100. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Name(self):
        """Account ID
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OrderBy(self):
        """Sorting by `createTime`, `updateTime`, or `passTime`. Default value: `createTime` (desc).
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting rule. Valid values: `desc` (descending order), `asc` (ascending order). Default value: `desc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Name = params.get("Name")
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
    """DescribeAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Accounts: Account information list
        :type Accounts: list of AccountDetail
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Accounts = None
        self._TotalCount = None
        self._RequestId = None

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
    def Accounts(self):
        """Account information list
        :rtype: list of AccountDetail
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def TotalCount(self):
        """Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountDetail()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBackupCommandRequest(AbstractModel):
    """DescribeBackupCommand request structure.

    """

    def __init__(self):
        r"""
        :param _BackupFileType: Backup file type. Full: full backup. FULL_LOG: full backup which needs log increments. FULL_DIFF: full backup which needs differential increments. LOG: log backup. DIFF: differential backup.
        :type BackupFileType: str
        :param _DataBaseName: Database name
        :type DataBaseName: str
        :param _IsRecovery: Whether restoration is required. No: not required. Yes: required.
        :type IsRecovery: str
        :param _LocalPath: Storage path of backup files. If this parameter is left empty, the default storage path will be D:\\.
        :type LocalPath: str
        """
        self._BackupFileType = None
        self._DataBaseName = None
        self._IsRecovery = None
        self._LocalPath = None

    @property
    def BackupFileType(self):
        """Backup file type. Full: full backup. FULL_LOG: full backup which needs log increments. FULL_DIFF: full backup which needs differential increments. LOG: log backup. DIFF: differential backup.
        :rtype: str
        """
        return self._BackupFileType

    @BackupFileType.setter
    def BackupFileType(self, BackupFileType):
        self._BackupFileType = BackupFileType

    @property
    def DataBaseName(self):
        """Database name
        :rtype: str
        """
        return self._DataBaseName

    @DataBaseName.setter
    def DataBaseName(self, DataBaseName):
        self._DataBaseName = DataBaseName

    @property
    def IsRecovery(self):
        """Whether restoration is required. No: not required. Yes: required.
        :rtype: str
        """
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery

    @property
    def LocalPath(self):
        """Storage path of backup files. If this parameter is left empty, the default storage path will be D:\\.
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath


    def _deserialize(self, params):
        self._BackupFileType = params.get("BackupFileType")
        self._DataBaseName = params.get("DataBaseName")
        self._IsRecovery = params.get("IsRecovery")
        self._LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupCommandResponse(AbstractModel):
    """DescribeBackupCommand response structure.

    """

    def __init__(self):
        r"""
        :param _Command: Create a backup command
        :type Command: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Command = None
        self._RequestId = None

    @property
    def Command(self):
        """Create a backup command
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

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
        self._Command = params.get("Command")
        self._RequestId = params.get("RequestId")


class DescribeBackupFilesRequest(AbstractModel):
    """DescribeBackupFiles request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param _GroupId: Group ID of unarchived backup files, which can be obtained by the `DescribeBackups` API (Querying archived backup record is not supported).
        :type GroupId: str
        :param _Limit: Number of entries to be returned per page. Value range: 1-100. Default value: `20`
        :type Limit: int
        :param _Offset: Page number. Default value: `0`
        :type Offset: int
        :param _DatabaseName: Filter backups by database name. If the parameter is left empty, this filter criterion will not take effect.
        :type DatabaseName: str
        :param _OrderBy: List items sorting by backup size. Valid values: `desc`(descending order), `asc` (ascending order). Default value: `desc`.
        :type OrderBy: str
        """
        self._InstanceId = None
        self._GroupId = None
        self._Limit = None
        self._Offset = None
        self._DatabaseName = None
        self._OrderBy = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupId(self):
        """Group ID of unarchived backup files, which can be obtained by the `DescribeBackups` API (Querying archived backup record is not supported).
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Limit(self):
        """Number of entries to be returned per page. Value range: 1-100. Default value: `20`
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: `0`
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DatabaseName(self):
        """Filter backups by database name. If the parameter is left empty, this filter criterion will not take effect.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def OrderBy(self):
        """List items sorting by backup size. Valid values: `desc`(descending order), `asc` (ascending order). Default value: `desc`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupId = params.get("GroupId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DatabaseName = params.get("DatabaseName")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupFilesResponse(AbstractModel):
    """DescribeBackupFiles response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of backups
        :type TotalCount: int
        :param _BackupFiles: List of backup file details
        :type BackupFiles: list of BackupFile
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupFiles = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of backups
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupFiles(self):
        """List of backup file details
        :rtype: list of BackupFile
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

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
        if params.get("BackupFiles") is not None:
            self._BackupFiles = []
            for item in params.get("BackupFiles"):
                obj = BackupFile()
                obj._deserialize(item)
                self._BackupFiles.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupMigrationRequest(AbstractModel):
    """DescribeBackupMigration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration.
        :type BackupMigrationId: str
        :param _MigrationName: Import task name
        :type MigrationName: str
        :param _BackupFileName: Backup file name
        :type BackupFileName: str
        :param _StatusSet: Status set of import tasks
        :type StatusSet: list of int
        :param _RecoveryType: Import task restoration type: FULL,FULL_LOG,FULL_DIFF
        :type RecoveryType: str
        :param _UploadType: COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :type UploadType: str
        :param _Limit: The maximum number of results returned per page. Default value: `100`.
        :type Limit: int
        :param _Offset: Page number. Default value: `0`.
        :type Offset: int
        :param _OrderBy: Sort by field. Valid values: `name`, `createTime`, `startTime`, `endTime`. By default, the results returned are sorted by `createTime` in the ascending order.
        :type OrderBy: str
        :param _OrderByType: Sorting order which is valid only when `OrderBy` is specified. Valid values: `asc` (ascending), `desc` (descending). Default value: `asc`.
        :type OrderByType: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._MigrationName = None
        self._BackupFileName = None
        self._StatusSet = None
        self._RecoveryType = None
        self._UploadType = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API CreateBackupMigration.
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def MigrationName(self):
        """Import task name
        :rtype: str
        """
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def BackupFileName(self):
        """Backup file name
        :rtype: str
        """
        return self._BackupFileName

    @BackupFileName.setter
    def BackupFileName(self, BackupFileName):
        self._BackupFileName = BackupFileName

    @property
    def StatusSet(self):
        """Status set of import tasks
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def RecoveryType(self):
        """Import task restoration type: FULL,FULL_LOG,FULL_DIFF
        :rtype: str
        """
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        """COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :rtype: str
        """
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def Limit(self):
        """The maximum number of results returned per page. Default value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """Sort by field. Valid values: `name`, `createTime`, `startTime`, `endTime`. By default, the results returned are sorted by `createTime` in the ascending order.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order which is valid only when `OrderBy` is specified. Valid values: `asc` (ascending), `desc` (descending). Default value: `asc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._MigrationName = params.get("MigrationName")
        self._BackupFileName = params.get("BackupFileName")
        self._StatusSet = params.get("StatusSet")
        self._RecoveryType = params.get("RecoveryType")
        self._UploadType = params.get("UploadType")
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
        


class DescribeBackupMigrationResponse(AbstractModel):
    """DescribeBackupMigration response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of tasks
        :type TotalCount: int
        :param _BackupMigrationSet: Migration task set
        :type BackupMigrationSet: list of Migration
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupMigrationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of tasks
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupMigrationSet(self):
        """Migration task set
        :rtype: list of Migration
        """
        return self._BackupMigrationSet

    @BackupMigrationSet.setter
    def BackupMigrationSet(self, BackupMigrationSet):
        self._BackupMigrationSet = BackupMigrationSet

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
        if params.get("BackupMigrationSet") is not None:
            self._BackupMigrationSet = []
            for item in params.get("BackupMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self._BackupMigrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupUploadSizeRequest(AbstractModel):
    """DescribeBackupUploadSize request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param _IncrementalMigrationId: Incremental import task ID
        :type IncrementalMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._IncrementalMigrationId = None

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        """Incremental import task ID
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupUploadSizeResponse(AbstractModel):
    """DescribeBackupUploadSize response structure.

    """

    def __init__(self):
        r"""
        :param _CosUploadBackupFileSet: Information of uploaded backups
        :type CosUploadBackupFileSet: list of CosUploadBackupFile
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CosUploadBackupFileSet = None
        self._RequestId = None

    @property
    def CosUploadBackupFileSet(self):
        """Information of uploaded backups
        :rtype: list of CosUploadBackupFile
        """
        return self._CosUploadBackupFileSet

    @CosUploadBackupFileSet.setter
    def CosUploadBackupFileSet(self, CosUploadBackupFileSet):
        self._CosUploadBackupFileSet = CosUploadBackupFileSet

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
        if params.get("CosUploadBackupFileSet") is not None:
            self._CosUploadBackupFileSet = []
            for item in params.get("CosUploadBackupFileSet"):
                obj = CosUploadBackupFile()
                obj._deserialize(item)
                self._CosUploadBackupFileSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start name (yyyy-MM-dd HH:mm:ss)
        :type StartTime: str
        :param _EndTime: End time (yyyy-MM-dd HH:mm:ss)
        :type EndTime: str
        :param _InstanceId: Instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param _Limit: Number of results per page. Value range: 1-100. Default value: 20
        :type Limit: int
        :param _Offset: Page number. Default value: 0
        :type Offset: int
        :param _BackupName: Filter by backup name. If this parameter is left empty, backup name will not be used in filtering.
        :type BackupName: str
        :param _Strategy: Filter by backup policy. Valid values: 0 (instance backup), 1 (multi-database backup). If this parameter is left empty, backup policy will not be used in filtering.
        :type Strategy: int
        :param _BackupWay: Filter by backup mode. Valid values: `0` (scheduled backup); `1` (manual backup); `2` (archive backup). Default value: `2`.
        :type BackupWay: int
        :param _BackupId: Filter by backup ID. If this parameter is left empty, backup ID will not be used in filtering.
        :type BackupId: int
        :param _DatabaseName: Filter backups by the database name. If the parameter is left empty, this filter criteria will not take effect.
        :type DatabaseName: str
        :param _Group: Whether to group backup files by backup task. Valid value: `0` (no), `1` (yes). Default value: `0`. This parameter is valid only for unarchived backup files.
        :type Group: int
        :param _Type: Backup type. Valid values: `1` (data backup), `2` (log backup). Default value: `1`.
        :type Type: int
        :param _BackupFormat: Filter by backup file format. Valid values: `pkg` (archive file), `single` (Unarchived files).
        :type BackupFormat: str
        """
        self._StartTime = None
        self._EndTime = None
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._BackupName = None
        self._Strategy = None
        self._BackupWay = None
        self._BackupId = None
        self._DatabaseName = None
        self._Group = None
        self._Type = None
        self._BackupFormat = None

    @property
    def StartTime(self):
        """Start name (yyyy-MM-dd HH:mm:ss)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time (yyyy-MM-dd HH:mm:ss)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """Number of results per page. Value range: 1-100. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BackupName(self):
        """Filter by backup name. If this parameter is left empty, backup name will not be used in filtering.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def Strategy(self):
        """Filter by backup policy. Valid values: 0 (instance backup), 1 (multi-database backup). If this parameter is left empty, backup policy will not be used in filtering.
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def BackupWay(self):
        """Filter by backup mode. Valid values: `0` (scheduled backup); `1` (manual backup); `2` (archive backup). Default value: `2`.
        :rtype: int
        """
        return self._BackupWay

    @BackupWay.setter
    def BackupWay(self, BackupWay):
        self._BackupWay = BackupWay

    @property
    def BackupId(self):
        """Filter by backup ID. If this parameter is left empty, backup ID will not be used in filtering.
        :rtype: int
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def DatabaseName(self):
        """Filter backups by the database name. If the parameter is left empty, this filter criteria will not take effect.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Group(self):
        """Whether to group backup files by backup task. Valid value: `0` (no), `1` (yes). Default value: `0`. This parameter is valid only for unarchived backup files.
        :rtype: int
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Type(self):
        """Backup type. Valid values: `1` (data backup), `2` (log backup). Default value: `1`.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BackupFormat(self):
        """Filter by backup file format. Valid values: `pkg` (archive file), `single` (Unarchived files).
        :rtype: str
        """
        return self._BackupFormat

    @BackupFormat.setter
    def BackupFormat(self, BackupFormat):
        self._BackupFormat = BackupFormat


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BackupName = params.get("BackupName")
        self._Strategy = params.get("Strategy")
        self._BackupWay = params.get("BackupWay")
        self._BackupId = params.get("BackupId")
        self._DatabaseName = params.get("DatabaseName")
        self._Group = params.get("Group")
        self._Type = params.get("Type")
        self._BackupFormat = params.get("BackupFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of backups
        :type TotalCount: int
        :param _Backups: Backup list details
        :type Backups: list of Backup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Backups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of backups
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Backups(self):
        """Backup list details
        :rtype: list of Backup
        """
        return self._Backups

    @Backups.setter
    def Backups(self, Backups):
        self._Backups = Backups

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
        if params.get("Backups") is not None:
            self._Backups = []
            for item in params.get("Backups"):
                obj = Backup()
                obj._deserialize(item)
                self._Backups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBusinessIntelligenceFileRequest(AbstractModel):
    """DescribeBusinessIntelligenceFile request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _FileName: File name
        :type FileName: str
        :param _StatusSet: Migration task status set. Valid values: `1` (Initialize to be deployed), `2` (Deploying), `3` (Deployment successful), `4` (Deployment failed)
        :type StatusSet: list of int
        :param _FileType: File type. Valid values: `FLAT` (flat files), `SSIS` (project file for business intelligence service).
        :type FileType: str
        :param _Limit: The maximum number of results returned per page. Value range: 1-100.
        :type Limit: int
        :param _Offset: Page number. Default value: `0`.
        :type Offset: int
        :param _OrderBy: Sorting field. Valid values: `file_name`, `create_time`, `start_time`.
        :type OrderBy: str
        :param _OrderByType: Sorting order: Valid values: `desc`, `asc`.
        :type OrderByType: str
        """
        self._InstanceId = None
        self._FileName = None
        self._StatusSet = None
        self._FileType = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

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
    def FileName(self):
        """File name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def StatusSet(self):
        """Migration task status set. Valid values: `1` (Initialize to be deployed), `2` (Deploying), `3` (Deployment successful), `4` (Deployment failed)
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def FileType(self):
        """File type. Valid values: `FLAT` (flat files), `SSIS` (project file for business intelligence service).
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Limit(self):
        """The maximum number of results returned per page. Value range: 1-100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """Sorting field. Valid values: `file_name`, `create_time`, `start_time`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order: Valid values: `desc`, `asc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileName = params.get("FileName")
        self._StatusSet = params.get("StatusSet")
        self._FileType = params.get("FileType")
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
        


class DescribeBusinessIntelligenceFileResponse(AbstractModel):
    """DescribeBusinessIntelligenceFile response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of file deployment tasks
        :type TotalCount: int
        :param _BackupMigrationSet: File deployment task set
        :type BackupMigrationSet: list of BusinessIntelligenceFile
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupMigrationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of file deployment tasks
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupMigrationSet(self):
        """File deployment task set
        :rtype: list of BusinessIntelligenceFile
        """
        return self._BackupMigrationSet

    @BackupMigrationSet.setter
    def BackupMigrationSet(self, BackupMigrationSet):
        self._BackupMigrationSet = BackupMigrationSet

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
        if params.get("BackupMigrationSet") is not None:
            self._BackupMigrationSet = []
            for item in params.get("BackupMigrationSet"):
                obj = BusinessIntelligenceFile()
                obj._deserialize(item)
                self._BackupMigrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBCharsetsRequest(AbstractModel):
    """DescribeDBCharsets request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-j8kv137v
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
        


class DescribeDBCharsetsResponse(AbstractModel):
    """DescribeDBCharsets response structure.

    """

    def __init__(self):
        r"""
        :param _DatabaseCharsets: Database character set list
        :type DatabaseCharsets: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DatabaseCharsets = None
        self._RequestId = None

    @property
    def DatabaseCharsets(self):
        """Database character set list
        :rtype: list of str
        """
        return self._DatabaseCharsets

    @DatabaseCharsets.setter
    def DatabaseCharsets(self, DatabaseCharsets):
        self._DatabaseCharsets = DatabaseCharsets

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
        self._DatabaseCharsets = params.get("DatabaseCharsets")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceInterRequest(AbstractModel):
    """DescribeDBInstanceInter request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The maximum number of results returned per page. Value range: 1-100.
        :type Limit: int
        :param _InstanceId: Filter by instance ID
        :type InstanceId: str
        :param _Status: Filter by status. Valid values: `1` (Enabling interworking IP), `2` (Enabled interworking IP), `3` (Adding to interworking group), `4` (Added to interworking group), `5` (Reclaiming interworking IP), `6` (Reclaimed interworking IP), `7` (Removing from interworking group), `8` (Removed from interworking group).
        :type Status: int
        :param _VersionSet: The list of instance version numbers
        :type VersionSet: list of str
        :param _Zone: Instance AZ ID in the format of ap-guangzhou-2
        :type Zone: str
        :param _Offset: Page number. Default value: `0`.
        :type Offset: int
        """
        self._Limit = None
        self._InstanceId = None
        self._Status = None
        self._VersionSet = None
        self._Zone = None
        self._Offset = None

    @property
    def Limit(self):
        """The maximum number of results returned per page. Value range: 1-100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        """Filter by instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        """Filter by status. Valid values: `1` (Enabling interworking IP), `2` (Enabled interworking IP), `3` (Adding to interworking group), `4` (Added to interworking group), `5` (Reclaiming interworking IP), `6` (Reclaimed interworking IP), `7` (Removing from interworking group), `8` (Removed from interworking group).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VersionSet(self):
        """The list of instance version numbers
        :rtype: list of str
        """
        return self._VersionSet

    @VersionSet.setter
    def VersionSet(self, VersionSet):
        self._VersionSet = VersionSet

    @property
    def Zone(self):
        """Instance AZ ID in the format of ap-guangzhou-2
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Offset(self):
        """Page number. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        self._VersionSet = params.get("VersionSet")
        self._Zone = params.get("Zone")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceInterResponse(AbstractModel):
    """DescribeDBInstanceInter response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of records returned
        :type TotalCount: int
        :param _InterInstanceSet: Details of instance in the interworking group
        :type InterInstanceSet: list of InterInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InterInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of records returned
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InterInstanceSet(self):
        """Details of instance in the interworking group
        :rtype: list of InterInstance
        """
        return self._InterInstanceSet

    @InterInstanceSet.setter
    def InterInstanceSet(self, InterInstanceSet):
        self._InterInstanceSet = InterInstanceSet

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
        if params.get("InterInstanceSet") is not None:
            self._InterInstanceSet = []
            for item in params.get("InterInstanceSet"):
                obj = InterInstance()
                obj._deserialize(item)
                self._InterInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesAttributeRequest(AbstractModel):
    """DescribeDBInstancesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID
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
        


class DescribeDBInstancesAttributeResponse(AbstractModel):
    """DescribeDBInstancesAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _RegularBackupEnable: Archive backup status. Valid values: `enable` (enabled), `disable` (disabled)
        :type RegularBackupEnable: str
        :param _RegularBackupSaveDays: Archive backup retention period: [90-3650] days
        :type RegularBackupSaveDays: int
        :param _RegularBackupStrategy: Archive backup policy. Valid values: `years` (yearly); `quarters (quarterly); `months` (monthly).
        :type RegularBackupStrategy: str
        :param _RegularBackupCounts: The number of retained archive backups
        :type RegularBackupCounts: int
        :param _RegularBackupStartTime: Archive backup start date in YYYY-MM-DD format, which is the current time by default.
        :type RegularBackupStartTime: str
        :param _BlockedThreshold: Block process threshold in milliseconds
        :type BlockedThreshold: int
        :param _EventSaveDays: Retention period for the files of slow SQL, blocking, deadlock, and extended events.
        :type EventSaveDays: int
        :param _TDEConfig: TDE configuration
        :type TDEConfig: :class:`tencentcloud.sqlserver.v20180328.models.TDEConfigAttribute`
        :param _SSLConfig: 
        :type SSLConfig: :class:`tencentcloud.sqlserver.v20180328.models.SSLConfig`
        :param _DrReadableInfo: 
        :type DrReadableInfo: :class:`tencentcloud.sqlserver.v20180328.models.DrReadableInfo`
        :param _OldVipList: 
        :type OldVipList: list of OldVip
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._RegularBackupEnable = None
        self._RegularBackupSaveDays = None
        self._RegularBackupStrategy = None
        self._RegularBackupCounts = None
        self._RegularBackupStartTime = None
        self._BlockedThreshold = None
        self._EventSaveDays = None
        self._TDEConfig = None
        self._SSLConfig = None
        self._DrReadableInfo = None
        self._OldVipList = None
        self._RequestId = None

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
    def RegularBackupEnable(self):
        """Archive backup status. Valid values: `enable` (enabled), `disable` (disabled)
        :rtype: str
        """
        return self._RegularBackupEnable

    @RegularBackupEnable.setter
    def RegularBackupEnable(self, RegularBackupEnable):
        self._RegularBackupEnable = RegularBackupEnable

    @property
    def RegularBackupSaveDays(self):
        """Archive backup retention period: [90-3650] days
        :rtype: int
        """
        return self._RegularBackupSaveDays

    @RegularBackupSaveDays.setter
    def RegularBackupSaveDays(self, RegularBackupSaveDays):
        self._RegularBackupSaveDays = RegularBackupSaveDays

    @property
    def RegularBackupStrategy(self):
        """Archive backup policy. Valid values: `years` (yearly); `quarters (quarterly); `months` (monthly).
        :rtype: str
        """
        return self._RegularBackupStrategy

    @RegularBackupStrategy.setter
    def RegularBackupStrategy(self, RegularBackupStrategy):
        self._RegularBackupStrategy = RegularBackupStrategy

    @property
    def RegularBackupCounts(self):
        """The number of retained archive backups
        :rtype: int
        """
        return self._RegularBackupCounts

    @RegularBackupCounts.setter
    def RegularBackupCounts(self, RegularBackupCounts):
        self._RegularBackupCounts = RegularBackupCounts

    @property
    def RegularBackupStartTime(self):
        """Archive backup start date in YYYY-MM-DD format, which is the current time by default.
        :rtype: str
        """
        return self._RegularBackupStartTime

    @RegularBackupStartTime.setter
    def RegularBackupStartTime(self, RegularBackupStartTime):
        self._RegularBackupStartTime = RegularBackupStartTime

    @property
    def BlockedThreshold(self):
        """Block process threshold in milliseconds
        :rtype: int
        """
        return self._BlockedThreshold

    @BlockedThreshold.setter
    def BlockedThreshold(self, BlockedThreshold):
        self._BlockedThreshold = BlockedThreshold

    @property
    def EventSaveDays(self):
        """Retention period for the files of slow SQL, blocking, deadlock, and extended events.
        :rtype: int
        """
        return self._EventSaveDays

    @EventSaveDays.setter
    def EventSaveDays(self, EventSaveDays):
        self._EventSaveDays = EventSaveDays

    @property
    def TDEConfig(self):
        """TDE configuration
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.TDEConfigAttribute`
        """
        return self._TDEConfig

    @TDEConfig.setter
    def TDEConfig(self, TDEConfig):
        self._TDEConfig = TDEConfig

    @property
    def SSLConfig(self):
        """
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.SSLConfig`
        """
        return self._SSLConfig

    @SSLConfig.setter
    def SSLConfig(self, SSLConfig):
        self._SSLConfig = SSLConfig

    @property
    def DrReadableInfo(self):
        """
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DrReadableInfo`
        """
        return self._DrReadableInfo

    @DrReadableInfo.setter
    def DrReadableInfo(self, DrReadableInfo):
        self._DrReadableInfo = DrReadableInfo

    @property
    def OldVipList(self):
        """
        :rtype: list of OldVip
        """
        return self._OldVipList

    @OldVipList.setter
    def OldVipList(self, OldVipList):
        self._OldVipList = OldVipList

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
        self._InstanceId = params.get("InstanceId")
        self._RegularBackupEnable = params.get("RegularBackupEnable")
        self._RegularBackupSaveDays = params.get("RegularBackupSaveDays")
        self._RegularBackupStrategy = params.get("RegularBackupStrategy")
        self._RegularBackupCounts = params.get("RegularBackupCounts")
        self._RegularBackupStartTime = params.get("RegularBackupStartTime")
        self._BlockedThreshold = params.get("BlockedThreshold")
        self._EventSaveDays = params.get("EventSaveDays")
        if params.get("TDEConfig") is not None:
            self._TDEConfig = TDEConfigAttribute()
            self._TDEConfig._deserialize(params.get("TDEConfig"))
        if params.get("SSLConfig") is not None:
            self._SSLConfig = SSLConfig()
            self._SSLConfig._deserialize(params.get("SSLConfig"))
        if params.get("DrReadableInfo") is not None:
            self._DrReadableInfo = DrReadableInfo()
            self._DrReadableInfo._deserialize(params.get("DrReadableInfo"))
        if params.get("OldVipList") is not None:
            self._OldVipList = []
            for item in params.get("OldVipList"):
                obj = OldVip()
                obj._deserialize(item)
                self._OldVipList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Status: Instance status. Valid values:
<li>1: applying</li>
<li>2: running</li>
<li>3: running restrictedly (primary/secondary switching)</li>
<li>4: isolated</li>
<li>5: repossessing</li>
<li>6: repossessed</li>
<li>7: executing task (e.g., backing up or rolling back instance)</li>
<li>8: deactivated</li>
<li>9: scaling out instance</li>
<li>10: migrating instance</li>
<li>11: read-only</li>
<li>12: restarting</li>
        :type Status: int
        :param _Offset: Page number. Default value: 0
        :type Offset: int
        :param _Limit: Number of results per page. Value range: 1-100. Default value: 100
        :type Limit: int
        :param _InstanceIdSet: One or more instance IDs in the format of mssql-si2823jyl
        :type InstanceIdSet: list of str
        :param _PayMode: Retrieves billing type. 0: pay-as-you-go
        :type PayMode: int
        :param _VpcId: Unique string-type ID of instance VPC in the format of `vpc-xxx`. If an empty string ("") is passed in, filtering will be made by basic network.
        :type VpcId: str
        :param _SubnetId: Unique string-type ID of instance subnet in the format of `subnet-xxx`. If an empty string ("") is passed in, filtering will be made by basic network.
        :type SubnetId: str
        :param _VipSet: The list of instance private IPs, such as 172.1.0.12
        :type VipSet: list of str
        :param _InstanceNameSet: The list of instance names used for fuzzy match
        :type InstanceNameSet: list of str
        :param _VersionSet: The list of instance version numbers, such as 2008R2, 2012SP3
        :type VersionSet: list of str
        :param _Zone: Instance availability zone, such as ap-guangzhou-2
        :type Zone: str
        :param _TagKeys: The list of instance tags
        :type TagKeys: list of str
        :param _SearchKey: Keyword used for fuzzy match, including instance ID, instance name, and instance private IP
        :type SearchKey: str
        :param _UidSet: Unique Uid of an instance
        :type UidSet: list of str
        :param _InstanceType: Instance type. Valid values: `HA` (high-availability), `RO` (read-only), `SI` (basic edition), `BI` (business intelligence service).
        :type InstanceType: str
        :param _PaginationType: 
        :type PaginationType: str
        """
        self._ProjectId = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._InstanceIdSet = None
        self._PayMode = None
        self._VpcId = None
        self._SubnetId = None
        self._VipSet = None
        self._InstanceNameSet = None
        self._VersionSet = None
        self._Zone = None
        self._TagKeys = None
        self._SearchKey = None
        self._UidSet = None
        self._InstanceType = None
        self._PaginationType = None

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        """Instance status. Valid values:
<li>1: applying</li>
<li>2: running</li>
<li>3: running restrictedly (primary/secondary switching)</li>
<li>4: isolated</li>
<li>5: repossessing</li>
<li>6: repossessed</li>
<li>7: executing task (e.g., backing up or rolling back instance)</li>
<li>8: deactivated</li>
<li>9: scaling out instance</li>
<li>10: migrating instance</li>
<li>11: read-only</li>
<li>12: restarting</li>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        """Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results per page. Value range: 1-100. Default value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceIdSet(self):
        """One or more instance IDs in the format of mssql-si2823jyl
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def PayMode(self):
        """Retrieves billing type. 0: pay-as-you-go
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def VpcId(self):
        """Unique string-type ID of instance VPC in the format of `vpc-xxx`. If an empty string ("") is passed in, filtering will be made by basic network.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Unique string-type ID of instance subnet in the format of `subnet-xxx`. If an empty string ("") is passed in, filtering will be made by basic network.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VipSet(self):
        """The list of instance private IPs, such as 172.1.0.12
        :rtype: list of str
        """
        return self._VipSet

    @VipSet.setter
    def VipSet(self, VipSet):
        self._VipSet = VipSet

    @property
    def InstanceNameSet(self):
        """The list of instance names used for fuzzy match
        :rtype: list of str
        """
        return self._InstanceNameSet

    @InstanceNameSet.setter
    def InstanceNameSet(self, InstanceNameSet):
        self._InstanceNameSet = InstanceNameSet

    @property
    def VersionSet(self):
        """The list of instance version numbers, such as 2008R2, 2012SP3
        :rtype: list of str
        """
        return self._VersionSet

    @VersionSet.setter
    def VersionSet(self, VersionSet):
        self._VersionSet = VersionSet

    @property
    def Zone(self):
        """Instance availability zone, such as ap-guangzhou-2
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def TagKeys(self):
        """The list of instance tags
        :rtype: list of str
        """
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def SearchKey(self):
        """Keyword used for fuzzy match, including instance ID, instance name, and instance private IP
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def UidSet(self):
        """Unique Uid of an instance
        :rtype: list of str
        """
        return self._UidSet

    @UidSet.setter
    def UidSet(self, UidSet):
        self._UidSet = UidSet

    @property
    def InstanceType(self):
        """Instance type. Valid values: `HA` (high-availability), `RO` (read-only), `SI` (basic edition), `BI` (business intelligence service).
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PaginationType(self):
        """
        :rtype: str
        """
        return self._PaginationType

    @PaginationType.setter
    def PaginationType(self, PaginationType):
        self._PaginationType = PaginationType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._PayMode = params.get("PayMode")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VipSet = params.get("VipSet")
        self._InstanceNameSet = params.get("InstanceNameSet")
        self._VersionSet = params.get("VersionSet")
        self._Zone = params.get("Zone")
        self._TagKeys = params.get("TagKeys")
        self._SearchKey = params.get("SearchKey")
        self._UidSet = params.get("UidSet")
        self._InstanceType = params.get("InstanceType")
        self._PaginationType = params.get("PaginationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of eligible instances. If the results are returned in multiple pages, this value will be the number of all eligible instances but not the number of instances returned according to the current values of `Limit` and `Offset`
        :type TotalCount: int
        :param _DBInstances: Instance list
        :type DBInstances: list of DBInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBInstances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of eligible instances. If the results are returned in multiple pages, this value will be the number of all eligible instances but not the number of instances returned according to the current values of `Limit` and `Offset`
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstances(self):
        """Instance list
        :rtype: list of DBInstance
        """
        return self._DBInstances

    @DBInstances.setter
    def DBInstances(self, DBInstances):
        self._DBInstances = DBInstances

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
        if params.get("DBInstances") is not None:
            self._DBInstances = []
            for item in params.get("DBInstances"):
                obj = DBInstance()
                obj._deserialize(item)
                self._DBInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBsNormalRequest(AbstractModel):
    """DescribeDBsNormal request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-7vfv3rk3
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-7vfv3rk3
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
        


class DescribeDBsNormalResponse(AbstractModel):
    """DescribeDBsNormal response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of databases of the instance
        :type TotalCount: int
        :param _DBList: Detailed database configurations, such as whether CDC or CT is enabled for the database
        :type DBList: list of DbNormalDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of databases of the instance
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBList(self):
        """Detailed database configurations, such as whether CDC or CT is enabled for the database
        :rtype: list of DbNormalDetail
        """
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

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
        if params.get("DBList") is not None:
            self._DBList = []
            for item in params.get("DBList"):
                obj = DbNormalDetail()
                obj._deserialize(item)
                self._DBList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBsRequest(AbstractModel):
    """DescribeDBs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: Instance ID
        :type InstanceIdSet: list of str
        :param _Limit: Number of results per page. Value range: 1-100. Default value: 20
        :type Limit: int
        :param _Offset: Page number. Default value: 0
        :type Offset: int
        :param _Name: Database name
        :type Name: str
        :param _OrderByType: Sorting rule. Valid values: `desc` (descending order), `asc` (ascending order). Default value: `desc`.
        :type OrderByType: str
        :param _Encryption: TDE status. Valid values: `enable` (enabled), `disable` (disabled).
        :type Encryption: str
        """
        self._InstanceIdSet = None
        self._Limit = None
        self._Offset = None
        self._Name = None
        self._OrderByType = None
        self._Encryption = None

    @property
    def InstanceIdSet(self):
        """Instance ID
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def Limit(self):
        """Number of results per page. Value range: 1-100. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Name(self):
        """Database name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OrderByType(self):
        """Sorting rule. Valid values: `desc` (descending order), `asc` (ascending order). Default value: `desc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Encryption(self):
        """TDE status. Valid values: `enable` (enabled), `disable` (disabled).
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Name = params.get("Name")
        self._OrderByType = params.get("OrderByType")
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBsResponse(AbstractModel):
    """DescribeDBs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of databases
        :type TotalCount: int
        :param _DBInstances: List of instance databases
        :type DBInstances: list of InstanceDBDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBInstances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of databases
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstances(self):
        """List of instance databases
        :rtype: list of InstanceDBDetail
        """
        return self._DBInstances

    @DBInstances.setter
    def DBInstances(self, DBInstances):
        self._DBInstances = DBInstances

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
        if params.get("DBInstances") is not None:
            self._DBInstances = []
            for item in params.get("DBInstances"):
                obj = InstanceDBDetail()
                obj._deserialize(item)
                self._DBInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowStatusRequest(AbstractModel):
    """DescribeFlowStatus request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        """Flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowStatusResponse(AbstractModel):
    """DescribeFlowStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Flow status. 0: succeeded, 1: failed, 2: running
        :type Status: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Flow status. 0: succeeded, 1: failed, 2: running
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._RequestId = params.get("RequestId")


class DescribeIncrementalMigrationRequest(AbstractModel):
    """DescribeIncrementalMigration request structure.

    """

    def __init__(self):
        r"""
        :param _BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _BackupFileName: Backup file name
        :type BackupFileName: str
        :param _StatusSet: Status set of import tasks
        :type StatusSet: list of int
        :param _Limit: The maximum number of results returned per page. Default value: `100`.
        :type Limit: int
        :param _Offset: Page number. Default value: `0`.
        :type Offset: int
        :param _OrderBy: Sort by field. Valid values: `name`, `createTime`, `startTime`, `endTime`. By default, the results returned are sorted by `createTime` in the ascending order.
        :type OrderBy: str
        :param _OrderByType: Sorting order which is valid only when `OrderBy` is specified. Valid values: `asc` (ascending), `desc` (descending). Default value: `asc`.
        :type OrderByType: str
        :param _IncrementalMigrationId: Incremental backup import task ID, which is returned through the `CreateIncrementalMigration` API.
        :type IncrementalMigrationId: str
        """
        self._BackupMigrationId = None
        self._InstanceId = None
        self._BackupFileName = None
        self._StatusSet = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._IncrementalMigrationId = None

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupFileName(self):
        """Backup file name
        :rtype: str
        """
        return self._BackupFileName

    @BackupFileName.setter
    def BackupFileName(self, BackupFileName):
        self._BackupFileName = BackupFileName

    @property
    def StatusSet(self):
        """Status set of import tasks
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def Limit(self):
        """The maximum number of results returned per page. Default value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """Sort by field. Valid values: `name`, `createTime`, `startTime`, `endTime`. By default, the results returned are sorted by `createTime` in the ascending order.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order which is valid only when `OrderBy` is specified. Valid values: `asc` (ascending), `desc` (descending). Default value: `asc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def IncrementalMigrationId(self):
        """Incremental backup import task ID, which is returned through the `CreateIncrementalMigration` API.
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId


    def _deserialize(self, params):
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._InstanceId = params.get("InstanceId")
        self._BackupFileName = params.get("BackupFileName")
        self._StatusSet = params.get("StatusSet")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIncrementalMigrationResponse(AbstractModel):
    """DescribeIncrementalMigration response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of import tasks
        :type TotalCount: int
        :param _IncrementalMigrationSet: Incremental import task set
        :type IncrementalMigrationSet: list of Migration
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._IncrementalMigrationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of import tasks
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IncrementalMigrationSet(self):
        """Incremental import task set
        :rtype: list of Migration
        """
        return self._IncrementalMigrationSet

    @IncrementalMigrationSet.setter
    def IncrementalMigrationSet(self, IncrementalMigrationSet):
        self._IncrementalMigrationSet = IncrementalMigrationSet

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
        if params.get("IncrementalMigrationSet") is not None:
            self._IncrementalMigrationSet = []
            for item in params.get("IncrementalMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self._IncrementalMigrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceByOrdersRequest(AbstractModel):
    """DescribeInstanceByOrders request structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order ID set
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        """Order ID set
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
        


class DescribeInstanceByOrdersResponse(AbstractModel):
    """DescribeInstanceByOrders response structure.

    """

    def __init__(self):
        r"""
        :param _DealInstance: 
        :type DealInstance: list of DealInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealInstance = None
        self._RequestId = None

    @property
    def DealInstance(self):
        """
        :rtype: list of DealInstance
        """
        return self._DealInstance

    @DealInstance.setter
    def DealInstance(self, DealInstance):
        self._DealInstance = DealInstance

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
        if params.get("DealInstance") is not None:
            self._DealInstance = []
            for item in params.get("DealInstance"):
                obj = DealInstance()
                obj._deserialize(item)
                self._DealInstance.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-dj5i29c5n. It is the same as the instance ID displayed in the TencentDB console and the response parameter `InstanceId` of the `DescribeDBInstances` API.
        :type InstanceId: str
        :param _Offset: Page number. Default value: `0`.
        :type Offset: int
        :param _Limit: The maximum number of results returned per page. Maximum value: `100`. Default value: `20`.
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-dj5i29c5n. It is the same as the instance ID displayed in the TencentDB console and the response parameter `InstanceId` of the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """Page number. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """The maximum number of results returned per page. Maximum value: `100`. Default value: `20`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible records
        :type TotalCount: int
        :param _Items: Parameter modification records
        :type Items: list of ParamRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Parameter modification records
        :rtype: list of ParamRecord
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
                obj = ParamRecord()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-dj5i29c5n. It is the same as the instance ID displayed in the TencentDB console and the response parameter `InstanceId` of the `DescribeDBInstances` API.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-dj5i29c5n. It is the same as the instance ID displayed in the TencentDB console and the response parameter `InstanceId` of the `DescribeDBInstances` API.
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
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instance parameters
        :type TotalCount: int
        :param _Items: Parameter details
        :type Items: list of ParameterDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of instance parameters
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Parameter details
        :rtype: list of ParameterDetail
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
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMaintenanceSpanRequest(AbstractModel):
    """DescribeMaintenanceSpan request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. For example, mssql-k8voqdlz.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID. For example, mssql-k8voqdlz.
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
        


class DescribeMaintenanceSpanResponse(AbstractModel):
    """DescribeMaintenanceSpan response structure.

    """

    def __init__(self):
        r"""
        :param _Weekly: Specifies the days in each week allowed for maintenance. For example, [1,2,3,4,5,6,7] indicates that all days from Monday to Sunday are allowed for maintenance.
        :type Weekly: list of int
        :param _StartTime: Maintenance start time each day. For example, 10:24 indicates that the maintenance window starts at 10:24.
        :type StartTime: str
        :param _Span: Maintenance duration each day, in hours. For example, 1 indicates that the duration is 1 hour after maintenance starts.
        :type Span: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._RequestId = None

    @property
    def Weekly(self):
        """Specifies the days in each week allowed for maintenance. For example, [1,2,3,4,5,6,7] indicates that all days from Monday to Sunday are allowed for maintenance.
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        """Maintenance start time each day. For example, 10:24 indicates that the maintenance window starts at 10:24.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        """Maintenance duration each day, in hours. For example, 1 indicates that the duration is 1 hour after maintenance starts.
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

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
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        self._RequestId = params.get("RequestId")


class DescribeMigrationDetailRequest(AbstractModel):
    """DescribeMigrationDetail request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        """Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
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
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        :param _MigrateName: Migration task name
        :type MigrateName: str
        :param _AppId: User ID of migration task
        :type AppId: int
        :param _Region: Migration task region
        :type Region: str
        :param _SourceType: Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :type SourceType: int
        :param _CreateTime: Migration task creation time
        :type CreateTime: str
        :param _StartTime: Migration task start time
        :type StartTime: str
        :param _EndTime: Migration task end time
        :type EndTime: str
        :param _Status: Migration task status (1: initializing, 4: migrating, 5: migration failed, 6: migration succeeded)
        :type Status: int
        :param _Progress: Migration task progress
        :type Progress: int
        :param _MigrateType: Migration type (1: structure migration, 2: data migration, 3: incremental sync)
        :type MigrateType: int
        :param _Source: Migration source
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param _Target: Migration target
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param _MigrateDBSet: Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5)
        :type MigrateDBSet: list of MigrateDB
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MigrateId = None
        self._MigrateName = None
        self._AppId = None
        self._Region = None
        self._SourceType = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Progress = None
        self._MigrateType = None
        self._Source = None
        self._Target = None
        self._MigrateDBSet = None
        self._RequestId = None

    @property
    def MigrateId(self):
        """Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def MigrateName(self):
        """Migration task name
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def AppId(self):
        """User ID of migration task
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        """Migration task region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SourceType(self):
        """Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def CreateTime(self):
        """Migration task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """Migration task start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Migration task end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """Migration task status (1: initializing, 4: migrating, 5: migration failed, 6: migration succeeded)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        """Migration task progress
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def MigrateType(self):
        """Migration type (1: structure migration, 2: data migration, 3: incremental sync)
        :rtype: int
        """
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def Source(self):
        """Migration source
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        """Migration target
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def MigrateDBSet(self):
        """Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5)
        :rtype: list of MigrateDB
        """
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet

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
        self._MigrateId = params.get("MigrateId")
        self._MigrateName = params.get("MigrateName")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._SourceType = params.get("SourceType")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._MigrateType = params.get("MigrateType")
        if params.get("Source") is not None:
            self._Source = MigrateSource()
            self._Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self._Target = MigrateTarget()
            self._Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self._MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self._MigrateDBSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigrationsRequest(AbstractModel):
    """DescribeMigrations request structure.

    """

    def __init__(self):
        r"""
        :param _StatusSet: Status set. As long as a migration task is in a status therein, it will be listed
        :type StatusSet: list of int
        :param _MigrateName: Migration task name (fuzzy match)
        :type MigrateName: str
        :param _Limit: Number of results per page. Value range: 1-100. Default value: 100
        :type Limit: int
        :param _Offset: Page number. Default value: 0
        :type Offset: int
        :param _OrderBy: The query results are sorted by keyword. Valid values: name, createTime, startTime, endTime, status
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: desc, asc
        :type OrderByType: str
        """
        self._StatusSet = None
        self._MigrateName = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def StatusSet(self):
        """Status set. As long as a migration task is in a status therein, it will be listed
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def MigrateName(self):
        """Migration task name (fuzzy match)
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def Limit(self):
        """Number of results per page. Value range: 1-100. Default value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """The query results are sorted by keyword. Valid values: name, createTime, startTime, endTime, status
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values: desc, asc
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._StatusSet = params.get("StatusSet")
        self._MigrateName = params.get("MigrateName")
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
        


class DescribeMigrationsResponse(AbstractModel):
    """DescribeMigrations response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results
        :type TotalCount: int
        :param _MigrateTaskSet: List of query results
        :type MigrateTaskSet: list of MigrateTask
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._MigrateTaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of query results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MigrateTaskSet(self):
        """List of query results
        :rtype: list of MigrateTask
        """
        return self._MigrateTaskSet

    @MigrateTaskSet.setter
    def MigrateTaskSet(self, MigrateTaskSet):
        self._MigrateTaskSet = MigrateTaskSet

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
        if params.get("MigrateTaskSet") is not None:
            self._MigrateTaskSet = []
            for item in params.get("MigrateTaskSet"):
                obj = MigrateTask()
                obj._deserialize(item)
                self._MigrateTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders request structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order array. The order name will be returned upon shipping, which can be used to call the `DescribeOrders` API to query shipment status
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        """Order array. The order name will be returned upon shipping, which can be used to call the `DescribeOrders` API to query shipment status
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
    """DescribeOrders response structure.

    """

    def __init__(self):
        r"""
        :param _Deals: Order information array
        :type Deals: list of DealInfo
        :param _TotalCount: Number of orders returned
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Deals = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Deals(self):
        """Order information array
        :rtype: list of DealInfo
        """
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

    @property
    def TotalCount(self):
        """Number of orders returned
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = DealInfo()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ ID in the format of ap-guangzhou-1
        :type Zone: str
        :param _InstanceType: Type of purchased instance. Valid values: HA - local disk high availability (including dual-machine high availability, AlwaysOn Cluster), RO - local disk read-only replica, SI - cloud disk edition single node, BI - business intelligence service, cvmHA - cloud disk edition high availability, cvmRO - cloud disk edition read-only replica
        :type InstanceType: str
        """
        self._Zone = None
        self._InstanceType = None

    @property
    def Zone(self):
        """AZ ID in the format of ap-guangzhou-1
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        """Type of purchased instance. Valid values: HA - local disk high availability (including dual-machine high availability, AlwaysOn Cluster), RO - local disk read-only replica, SI - cloud disk edition single node, BI - business intelligence service, cvmHA - cloud disk edition high availability, cvmRO - cloud disk edition read-only replica
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductConfigResponse(AbstractModel):
    """DescribeProductConfig response structure.

    """

    def __init__(self):
        r"""
        :param _SpecInfoList: Specification information array
        :type SpecInfoList: list of SpecInfo
        :param _TotalCount: Number of date entries returned
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SpecInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SpecInfoList(self):
        """Specification information array
        :rtype: list of SpecInfo
        """
        return self._SpecInfoList

    @SpecInfoList.setter
    def SpecInfoList(self, SpecInfoList):
        self._SpecInfoList = SpecInfoList

    @property
    def TotalCount(self):
        """Number of date entries returned
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("SpecInfoList") is not None:
            self._SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self._SpecInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of regions returned
        :type TotalCount: int
        :param _RegionSet: Region information array
        :type RegionSet: list of RegionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of regions returned
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        """Region information array
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

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
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRestoreTimeRangeRequest(AbstractModel):
    """DescribeRestoreTimeRange request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: 
        :type InstanceId: str
        :param _TargetInstanceId: 
        :type TargetInstanceId: str
        """
        self._InstanceId = None
        self._TargetInstanceId = None

    @property
    def InstanceId(self):
        """
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TargetInstanceId(self):
        """
        :rtype: str
        """
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TargetInstanceId = params.get("TargetInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTimeRangeResponse(AbstractModel):
    """DescribeRestoreTimeRange response structure.

    """

    def __init__(self):
        r"""
        :param _MinTime: 
        :type MinTime: str
        :param _MaxTime: 
        :type MaxTime: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MinTime = None
        self._MaxTime = None
        self._RequestId = None

    @property
    def MinTime(self):
        """
        :rtype: str
        """
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        """
        :rtype: str
        """
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

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
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._RequestId = params.get("RequestId")


class DescribeRollbackTimeRequest(AbstractModel):
    """DescribeRollbackTime request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DBs: List of databases to be queried
        :type DBs: list of str
        """
        self._InstanceId = None
        self._DBs = None

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
    def DBs(self):
        """List of databases to be queried
        :rtype: list of str
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DBs = params.get("DBs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeResponse(AbstractModel):
    """DescribeRollbackTime response structure.

    """

    def __init__(self):
        r"""
        :param _Details: Information of time range available for database rollback
        :type Details: list of DbRollbackTimeInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Details = None
        self._RequestId = None

    @property
    def Details(self):
        """Information of time range available for database rollback
        :rtype: list of DbRollbackTimeInfo
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

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
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = DbRollbackTimeInfo()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowlogsRequest(AbstractModel):
    """DescribeSlowlogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-k8voqdlz
        :type InstanceId: str
        :param _StartTime: Start time in the format of `yyyy-MM-dd HH:mm:ss`
        :type StartTime: str
        :param _EndTime: End time in the format of `yyyy-MM-dd HH:mm:ss`
        :type EndTime: str
        :param _Limit: Number of results per page. Value range: 1-100. Default value: 20
        :type Limit: int
        :param _Offset: Page number. Default value: 0
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-k8voqdlz
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Start time in the format of `yyyy-MM-dd HH:mm:ss`
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time in the format of `yyyy-MM-dd HH:mm:ss`
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """Number of results per page. Value range: 1-100. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: 0
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
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowlogsResponse(AbstractModel):
    """DescribeSlowlogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of queries
        :type TotalCount: int
        :param _Slowlogs: Information list of slow query logs
        :type Slowlogs: list of SlowlogInfo
        :param _SlowLogs: 
        :type SlowLogs: list of SlowLog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Slowlogs = None
        self._SlowLogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of queries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Slowlogs(self):
        warnings.warn("parameter `Slowlogs` is deprecated", DeprecationWarning) 

        """Information list of slow query logs
        :rtype: list of SlowlogInfo
        """
        return self._Slowlogs

    @Slowlogs.setter
    def Slowlogs(self, Slowlogs):
        warnings.warn("parameter `Slowlogs` is deprecated", DeprecationWarning) 

        self._Slowlogs = Slowlogs

    @property
    def SlowLogs(self):
        """
        :rtype: list of SlowLog
        """
        return self._SlowLogs

    @SlowLogs.setter
    def SlowLogs(self, SlowLogs):
        self._SlowLogs = SlowLogs

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
        if params.get("Slowlogs") is not None:
            self._Slowlogs = []
            for item in params.get("Slowlogs"):
                obj = SlowlogInfo()
                obj._deserialize(item)
                self._Slowlogs.append(obj)
        if params.get("SlowLogs") is not None:
            self._SlowLogs = []
            for item in params.get("SlowLogs"):
                obj = SlowLog()
                obj._deserialize(item)
                self._SlowLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUploadBackupInfoRequest(AbstractModel):
    """DescribeUploadBackupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadBackupInfoResponse(AbstractModel):
    """DescribeUploadBackupInfo response structure.

    """

    def __init__(self):
        r"""
        :param _BucketName: Bucket name
        :type BucketName: str
        :param _Region: Bucket location information
        :type Region: str
        :param _Path: Storage path
        :type Path: str
        :param _TmpSecretId: Temporary key ID
        :type TmpSecretId: str
        :param _TmpSecretKey: Temporary key (Key)
        :type TmpSecretKey: str
        :param _XCosSecurityToken: Temporary key (Token)
        :type XCosSecurityToken: str
        :param _StartTime: Temporary key start time
        :type StartTime: str
        :param _ExpiredTime: Temporary key expiration time
        :type ExpiredTime: str
        :param _CosSecurityToken: 
        :type CosSecurityToken: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BucketName = None
        self._Region = None
        self._Path = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._XCosSecurityToken = None
        self._StartTime = None
        self._ExpiredTime = None
        self._CosSecurityToken = None
        self._RequestId = None

    @property
    def BucketName(self):
        """Bucket name
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def Region(self):
        """Bucket location information
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Path(self):
        """Storage path
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def TmpSecretId(self):
        """Temporary key ID
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """Temporary key (Key)
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def XCosSecurityToken(self):
        warnings.warn("parameter `XCosSecurityToken` is deprecated", DeprecationWarning) 

        """Temporary key (Token)
        :rtype: str
        """
        return self._XCosSecurityToken

    @XCosSecurityToken.setter
    def XCosSecurityToken(self, XCosSecurityToken):
        warnings.warn("parameter `XCosSecurityToken` is deprecated", DeprecationWarning) 

        self._XCosSecurityToken = XCosSecurityToken

    @property
    def StartTime(self):
        """Temporary key start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        """Temporary key expiration time
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CosSecurityToken(self):
        """
        :rtype: str
        """
        return self._CosSecurityToken

    @CosSecurityToken.setter
    def CosSecurityToken(self, CosSecurityToken):
        self._CosSecurityToken = CosSecurityToken

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
        self._BucketName = params.get("BucketName")
        self._Region = params.get("Region")
        self._Path = params.get("Path")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._XCosSecurityToken = params.get("XCosSecurityToken")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._CosSecurityToken = params.get("CosSecurityToken")
        self._RequestId = params.get("RequestId")


class DescribeXEventsRequest(AbstractModel):
    """DescribeXEvents request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _EventType: Event type. Valid values: `slow` (Slow SQL event), `blocked` (blocking event),  deadlock` (deadlock event).
        :type EventType: str
        :param _StartTime: Generation start time of an extended file in the format of yyyy-MM-dd HH:mm:ss.
        :type StartTime: str
        :param _EndTime: Generation end time of an extended file in the format of yyyy-MM-dd HH:mm:ss.
        :type EndTime: str
        :param _Offset: Page number. Default value: `0`
        :type Offset: int
        :param _Limit: Number of entries to be returned per page. Value range: 1-100. Default value: `20`
        :type Limit: int
        """
        self._InstanceId = None
        self._EventType = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

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
    def EventType(self):
        """Event type. Valid values: `slow` (Slow SQL event), `blocked` (blocking event),  deadlock` (deadlock event).
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def StartTime(self):
        """Generation start time of an extended file in the format of yyyy-MM-dd HH:mm:ss.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Generation end time of an extended file in the format of yyyy-MM-dd HH:mm:ss.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """Page number. Default value: `0`
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of entries to be returned per page. Value range: 1-100. Default value: `20`
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EventType = params.get("EventType")
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
        


class DescribeXEventsResponse(AbstractModel):
    """DescribeXEvents response structure.

    """

    def __init__(self):
        r"""
        :param _Events: List of extended events
        :type Events: list of Events
        :param _TotalCount: Total number of extended events
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Events = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Events(self):
        """List of extended events
        :rtype: list of Events
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        """Total number of extended events
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = Events()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of AZs returned
        :type TotalCount: int
        :param _ZoneSet: Array of AZs
        :type ZoneSet: list of ZoneInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of AZs returned
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneSet(self):
        """Array of AZs
        :rtype: list of ZoneInfo
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

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
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DrReadableInfo(AbstractModel):
    """Replica server read-only information

    """

    def __init__(self):
        r"""
        :param _SlaveStatus: Replica server status. Valid values: enable - running; disable - unavailable
Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaveStatus: str
        :param _ReadableStatus: Replica server readable status. Valid values: enable - enabled; disable - disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReadableStatus: str
        :param _Vip: Replica server read-only VIP
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vip: str
        :param _VPort: Replica server read-only port
Note: This field may return null, indicating that no valid values can be obtained.
        :type VPort: int
        :param _UniqVpcId: Replica server VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param _UniqSubnetId: Replica server VPC subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqSubnetId: str
        """
        self._SlaveStatus = None
        self._ReadableStatus = None
        self._Vip = None
        self._VPort = None
        self._UniqVpcId = None
        self._UniqSubnetId = None

    @property
    def SlaveStatus(self):
        """Replica server status. Valid values: enable - running; disable - unavailable
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SlaveStatus

    @SlaveStatus.setter
    def SlaveStatus(self, SlaveStatus):
        self._SlaveStatus = SlaveStatus

    @property
    def ReadableStatus(self):
        """Replica server readable status. Valid values: enable - enabled; disable - disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReadableStatus

    @ReadableStatus.setter
    def ReadableStatus(self, ReadableStatus):
        self._ReadableStatus = ReadableStatus

    @property
    def Vip(self):
        """Replica server read-only VIP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        """Replica server read-only port
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def UniqVpcId(self):
        """Replica server VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        """Replica server VPC subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId


    def _deserialize(self, params):
        self._SlaveStatus = params.get("SlaveStatus")
        self._ReadableStatus = params.get("ReadableStatus")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventConfig(AbstractModel):
    """Threshold setting for an extended event

    """

    def __init__(self):
        r"""
        :param _EventType: Event type. Valid values: `slow` (set threshold for slow SQL ), `blocked` (set threshold for the blocking and deadlock).
        :type EventType: str
        :param _Threshold: Threshold in milliseconds. Valid values: `0`(disable), `non-zero` (enable)
        :type Threshold: int
        """
        self._EventType = None
        self._Threshold = None

    @property
    def EventType(self):
        """Event type. Valid values: `slow` (set threshold for slow SQL ), `blocked` (set threshold for the blocking and deadlock).
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Threshold(self):
        """Threshold in milliseconds. Valid values: `0`(disable), `non-zero` (enable)
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._EventType = params.get("EventType")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Events(AbstractModel):
    """Details of an extended event

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: int
        :param _FileName: File name of an extended event
        :type FileName: str
        :param _Size: File size of an extended event
        :type Size: int
        :param _EventType: Event type. Valid values: `slow` (Slow SQL event), `blocked` (blocking event),  `deadlock` (deadlock event).
        :type EventType: str
        :param _Status: Event record status. Valid values: `1` (succeeded), `2` (failed).
        :type Status: int
        :param _StartTime: Generation start time of an extended file
        :type StartTime: str
        :param _EndTime: Generation end time of an extended file
        :type EndTime: str
        :param _InternalAddr: Download address on the private network
        :type InternalAddr: str
        :param _ExternalAddr: Download address on the public network
        :type ExternalAddr: str
        """
        self._Id = None
        self._FileName = None
        self._Size = None
        self._EventType = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._InternalAddr = None
        self._ExternalAddr = None

    @property
    def Id(self):
        """ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FileName(self):
        """File name of an extended event
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        """File size of an extended event
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventType(self):
        """Event type. Valid values: `slow` (Slow SQL event), `blocked` (blocking event),  `deadlock` (deadlock event).
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Status(self):
        """Event record status. Valid values: `1` (succeeded), `2` (failed).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        """Generation start time of an extended file
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Generation end time of an extended file
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InternalAddr(self):
        """Download address on the private network
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        """Download address on the public network
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._FileName = params.get("FileName")
        self._Size = params.get("Size")
        self._EventType = params.get("EventType")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileAction(AbstractModel):
    """Information of allowed operation

    """

    def __init__(self):
        r"""
        :param _AllAction: Allowed operations. Valid values: `view` (view list), `remark` (modify remark), `deploy` (deploy files), `delete` (delete files).
        :type AllAction: list of str
        :param _AllowedAction: Operation allowed in the current status. If the subset of `AllAction` is empty, no operations will be allowed.
        :type AllowedAction: list of str
        """
        self._AllAction = None
        self._AllowedAction = None

    @property
    def AllAction(self):
        """Allowed operations. Valid values: `view` (view list), `remark` (modify remark), `deploy` (deploy files), `delete` (delete files).
        :rtype: list of str
        """
        return self._AllAction

    @AllAction.setter
    def AllAction(self, AllAction):
        self._AllAction = AllAction

    @property
    def AllowedAction(self):
        """Operation allowed in the current status. If the subset of `AllAction` is empty, no operations will be allowed.
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
        


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ ID, which can be obtained through the `Zone` field in the returned value of the `DescribeZones` API
        :type Zone: str
        :param _Memory: Memory size in GB
        :type Memory: int
        :param _Storage: Instance capacity in GB
        :type Storage: int
        :param _InstanceChargeType: Billing type. Valid value: POSTPAID.
        :type InstanceChargeType: str
        :param _Period: Length of purchase in months. Value range: 1-48. Default value: 1
        :type Period: int
        :param _GoodsNum: Number of instances purchased at a time. Value range: 1-100. Default value: 1
        :type GoodsNum: int
        :param _DBVersion: SQL version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), `201402` (SQL Server 2014 Standard)`, `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The purchasable version varies by region. It can be queried by the `DescribeProductConfig` API.
        :type DBVersion: str
        :param _Cpu: The number of CPU cores of the instance you want to purchase.
        :type Cpu: int
        :param _InstanceType: The type of instance to be purchased. Valid values: `HA` (high-availability edition, including dual-server high-availability and AlwaysOn cluster edition), `RO` (read-only replica edition), `SI` (single-node edition), `cvmHA` (dual-server high-availability edition for CVM), `cvmRO` (read-only edition for CVM).
        :type InstanceType: str
        :param _MachineType: The host type of the instance to be purchased. Valid values: `PM` (physical machine), `CLOUD_PREMIUM` (virtual machine with premium cloud disk), `CLOUD_SSD` (virtual machine with SSD), 
`CLOUD_HSSD` (virtual machine with enhanced SSD), `CLOUD_TSSD` (virtual machine with ulTra SSD), `CLOUD_BSSD` (virtual machine with balanced SSD).
        :type MachineType: str
        """
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._InstanceChargeType = None
        self._Period = None
        self._GoodsNum = None
        self._DBVersion = None
        self._Cpu = None
        self._InstanceType = None
        self._MachineType = None

    @property
    def Zone(self):
        """AZ ID, which can be obtained through the `Zone` field in the returned value of the `DescribeZones` API
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        """Memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Instance capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceChargeType(self):
        """Billing type. Valid value: POSTPAID.
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Period(self):
        """Length of purchase in months. Value range: 1-48. Default value: 1
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def GoodsNum(self):
        """Number of instances purchased at a time. Value range: 1-100. Default value: 1
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def DBVersion(self):
        """SQL version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), `201402` (SQL Server 2014 Standard)`, `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The purchasable version varies by region. It can be queried by the `DescribeProductConfig` API.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def Cpu(self):
        """The number of CPU cores of the instance you want to purchase.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def InstanceType(self):
        """The type of instance to be purchased. Valid values: `HA` (high-availability edition, including dual-server high-availability and AlwaysOn cluster edition), `RO` (read-only replica edition), `SI` (single-node edition), `cvmHA` (dual-server high-availability edition for CVM), `cvmRO` (read-only edition for CVM).
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MachineType(self):
        """The host type of the instance to be purchased. Valid values: `PM` (physical machine), `CLOUD_PREMIUM` (virtual machine with premium cloud disk), `CLOUD_SSD` (virtual machine with SSD), 
`CLOUD_HSSD` (virtual machine with enhanced SSD), `CLOUD_TSSD` (virtual machine with ulTra SSD), `CLOUD_BSSD` (virtual machine with balanced SSD).
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Period = params.get("Period")
        self._GoodsNum = params.get("GoodsNum")
        self._DBVersion = params.get("DBVersion")
        self._Cpu = params.get("Cpu")
        self._InstanceType = params.get("InstanceType")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: Price before discount. This value divided by 100 indicates the price; for example, 10010 means 100.10 USD
        :type OriginalPrice: int
        :param _Price: The actual price to be paid. This value divided by 100 indicates the price; for example, 10010 means 100.10 USD
        :type Price: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        """Price before discount. This value divided by 100 indicates the price; for example, 10010 means 100.10 USD
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        """The actual price to be paid. This value divided by 100 indicates the price; for example, 10010 means 100.10 USD
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

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
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param _Memory: Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size
        :type Memory: int
        :param _Storage: Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity
        :type Storage: int
        :param _Cpu: The number of CUP cores after the instance is upgraded, which cannot be smaller than that of the current cores.
        :type Cpu: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        """Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        """The number of CUP cores after the instance is upgraded, which cannot be smaller than that of the current cores.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: Price before discount. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD
        :type OriginalPrice: int
        :param _Price: The actual price to be paid. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD
        :type Price: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        """Price before discount. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        """The actual price to be paid. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

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
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InstanceDBDetail(AbstractModel):
    """Instance database information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DBDetails: Database information list
        :type DBDetails: list of DBDetail
        """
        self._InstanceId = None
        self._DBDetails = None

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
    def DBDetails(self):
        """Database information list
        :rtype: list of DBDetail
        """
        return self._DBDetails

    @DBDetails.setter
    def DBDetails(self, DBDetails):
        self._DBDetails = DBDetails


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DBDetails") is not None:
            self._DBDetails = []
            for item in params.get("DBDetails"):
                obj = DBDetail()
                obj._deserialize(item)
                self._DBDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InterInstance(AbstractModel):
    """Details of instances in the interwoking group

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InterVip: Instance interworking IP, which can be accessed after the instance is added to the interworking group.
        :type InterVip: str
        :param _InterPort: Instance interworking port, which can be accessed after the instance is added to the interworking group.
        :type InterPort: int
        :param _Status: Instance interworking status. Valid values: `1` (Enabling interworking IP), `2` (Enabled interworking IP), `3` (Adding to interworking group), `4` (Added to interworking group), `5` (Reclaiming interworking IP), `6`(Reclaimed interworking IP), `7` (Removing from interworking group), `8` (Removed from interworking group).
        :type Status: int
        :param _Region: Instance region, such as ap-guangzhou.
        :type Region: str
        :param _Zone: Instance AZ name, such as ap-guangzhou-1.
        :type Zone: str
        :param _Version: Instance version code
        :type Version: str
        :param _VersionName: Instance version
        :type VersionName: str
        :param _Name: Instance name
        :type Name: str
        :param _Vip: Instance access IP
        :type Vip: str
        :param _Vport: Instance access port
        :type Vport: int
        """
        self._InstanceId = None
        self._InterVip = None
        self._InterPort = None
        self._Status = None
        self._Region = None
        self._Zone = None
        self._Version = None
        self._VersionName = None
        self._Name = None
        self._Vip = None
        self._Vport = None

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
    def InterVip(self):
        """Instance interworking IP, which can be accessed after the instance is added to the interworking group.
        :rtype: str
        """
        return self._InterVip

    @InterVip.setter
    def InterVip(self, InterVip):
        self._InterVip = InterVip

    @property
    def InterPort(self):
        """Instance interworking port, which can be accessed after the instance is added to the interworking group.
        :rtype: int
        """
        return self._InterPort

    @InterPort.setter
    def InterPort(self, InterPort):
        self._InterPort = InterPort

    @property
    def Status(self):
        """Instance interworking status. Valid values: `1` (Enabling interworking IP), `2` (Enabled interworking IP), `3` (Adding to interworking group), `4` (Added to interworking group), `5` (Reclaiming interworking IP), `6`(Reclaimed interworking IP), `7` (Removing from interworking group), `8` (Removed from interworking group).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        """Instance region, such as ap-guangzhou.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """Instance AZ name, such as ap-guangzhou-1.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Version(self):
        """Instance version code
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def VersionName(self):
        """Instance version
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Name(self):
        """Instance name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Vip(self):
        """Instance access IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Instance access port
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InterVip = params.get("InterVip")
        self._InterPort = params.get("InterPort")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Version = params.get("Version")
        self._VersionName = params.get("VersionName")
        self._Name = params.get("Name")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InterInstanceFlow(AbstractModel):
    """Instance status after enabling or disabling the interworking group

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, such as mssql-sdf32n1d.
        :type InstanceId: str
        :param _FlowId: Instance task ID for enabling or disabling the interworking group. When `FlowId` is less than 0, the interworking group will be enabled or disabled successfully; otherwise, the operation failed.
        :type FlowId: int
        """
        self._InstanceId = None
        self._FlowId = None

    @property
    def InstanceId(self):
        """Instance ID, such as mssql-sdf32n1d.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        """Instance task ID for enabling or disabling the interworking group. When `FlowId` is less than 0, the interworking group will be enabled or disabled successfully; otherwise, the operation failed.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDB(AbstractModel):
    """List of databases to be migrated

    """

    def __init__(self):
        r"""
        :param _DBName: Name of migrated database
        :type DBName: str
        """
        self._DBName = None

    @property
    def DBName(self):
        """Name of migrated database
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDetail(AbstractModel):
    """Migration progress details

    """

    def __init__(self):
        r"""
        :param _StepName: Name of current step
        :type StepName: str
        :param _Progress: Progress of current step in %
        :type Progress: int
        """
        self._StepName = None
        self._Progress = None

    @property
    def StepName(self):
        """Name of current step
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def Progress(self):
        """Progress of current step in %
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress


    def _deserialize(self, params):
        self._StepName = params.get("StepName")
        self._Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateSource(AbstractModel):
    """Source type of migration task

    """

    def __init__(self):
        r"""
        :param _InstanceId: Source instance ID in the format of `mssql-si2823jyl`, which is used when `MigrateType` is 1 (TencentDB for SQL Server)
        :type InstanceId: str
        :param _CvmId: ID of source CVM instance, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type CvmId: str
        :param _VpcId: VPC ID of source CVM instance in the format of vpc-6ys9ont9, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type VpcId: str
        :param _SubnetId: VPC subnet ID of source CVM instance in the format of subnet-h9extioi, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type SubnetId: str
        :param _UserName: Username, which is used when `MigrateType` is 1 or 2
        :type UserName: str
        :param _Password: Password, which is used when `MigrateType` is 1 or 2
        :type Password: str
        :param _Ip: Private IP of source CVM database, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type Ip: str
        :param _Port: Port number of source CVM database, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type Port: int
        :param _Url: Source backup address for offline migration, which is used when `MigrateType` is 4 or 5
        :type Url: list of str
        :param _UrlPassword: Source backup password for offline migration, which is used when `MigrateType` is 4 or 5
        :type UrlPassword: str
        """
        self._InstanceId = None
        self._CvmId = None
        self._VpcId = None
        self._SubnetId = None
        self._UserName = None
        self._Password = None
        self._Ip = None
        self._Port = None
        self._Url = None
        self._UrlPassword = None

    @property
    def InstanceId(self):
        """Source instance ID in the format of `mssql-si2823jyl`, which is used when `MigrateType` is 1 (TencentDB for SQL Server)
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmId(self):
        """ID of source CVM instance, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: str
        """
        return self._CvmId

    @CvmId.setter
    def CvmId(self, CvmId):
        self._CvmId = CvmId

    @property
    def VpcId(self):
        """VPC ID of source CVM instance in the format of vpc-6ys9ont9, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """VPC subnet ID of source CVM instance in the format of subnet-h9extioi, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def UserName(self):
        """Username, which is used when `MigrateType` is 1 or 2
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Password, which is used when `MigrateType` is 1 or 2
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Ip(self):
        """Private IP of source CVM database, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """Port number of source CVM database, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Url(self):
        """Source backup address for offline migration, which is used when `MigrateType` is 4 or 5
        :rtype: list of str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def UrlPassword(self):
        """Source backup password for offline migration, which is used when `MigrateType` is 4 or 5
        :rtype: str
        """
        return self._UrlPassword

    @UrlPassword.setter
    def UrlPassword(self, UrlPassword):
        self._UrlPassword = UrlPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CvmId = params.get("CvmId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Url = params.get("Url")
        self._UrlPassword = params.get("UrlPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateTarget(AbstractModel):
    """Target type of migration task

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of target instance in the format of mssql-si2823jyl
        :type InstanceId: str
        :param _UserName: Username of migration target instance
        :type UserName: str
        :param _Password: Password of migration target instance
        :type Password: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Password = None

    @property
    def InstanceId(self):
        """ID of target instance in the format of mssql-si2823jyl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Username of migration target instance
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Password of migration target instance
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateTask(AbstractModel):
    """Migration task type

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        :param _MigrateName: Migration task name
        :type MigrateName: str
        :param _AppId: User ID of migration task
        :type AppId: int
        :param _Region: Migration task region
        :type Region: str
        :param _SourceType: Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :type SourceType: int
        :param _CreateTime: Migration task creation time
        :type CreateTime: str
        :param _StartTime: Migration task start time
        :type StartTime: str
        :param _EndTime: Migration task end time
        :type EndTime: str
        :param _Status: Migration task status (1: initializing, 4: migrating, 5: migration failed, 6: migration succeeded, 7: suspended, 8: deleted, 9: suspending, 10: completing, 11: suspension failed, 12: completion failed)
        :type Status: int
        :param _Message: Information
        :type Message: str
        :param _CheckFlag: Whether migration task has been checked (0: not checked, 1: check succeeded, 2: check failed, 3: checking)
        :type CheckFlag: int
        :param _Progress: Migration task progress in %
        :type Progress: int
        :param _MigrateDetail: Migration task progress details
        :type MigrateDetail: :class:`tencentcloud.sqlserver.v20180328.models.MigrateDetail`
        """
        self._MigrateId = None
        self._MigrateName = None
        self._AppId = None
        self._Region = None
        self._SourceType = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Message = None
        self._CheckFlag = None
        self._Progress = None
        self._MigrateDetail = None

    @property
    def MigrateId(self):
        """Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def MigrateName(self):
        """Migration task name
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def AppId(self):
        """User ID of migration task
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        """Migration task region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SourceType(self):
        """Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def CreateTime(self):
        """Migration task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """Migration task start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Migration task end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """Migration task status (1: initializing, 4: migrating, 5: migration failed, 6: migration succeeded, 7: suspended, 8: deleted, 9: suspending, 10: completing, 11: suspension failed, 12: completion failed)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        """Information
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def CheckFlag(self):
        """Whether migration task has been checked (0: not checked, 1: check succeeded, 2: check failed, 3: checking)
        :rtype: int
        """
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

    @property
    def Progress(self):
        """Migration task progress in %
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def MigrateDetail(self):
        """Migration task progress details
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateDetail`
        """
        return self._MigrateDetail

    @MigrateDetail.setter
    def MigrateDetail(self, MigrateDetail):
        self._MigrateDetail = MigrateDetail


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        self._MigrateName = params.get("MigrateName")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._SourceType = params.get("SourceType")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._CheckFlag = params.get("CheckFlag")
        self._Progress = params.get("Progress")
        if params.get("MigrateDetail") is not None:
            self._MigrateDetail = MigrateDetail()
            self._MigrateDetail._deserialize(params.get("MigrateDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Migration(AbstractModel):
    """Cold backup migration import

    """

    def __init__(self):
        r"""
        :param _MigrationId: Backup import task ID or incremental import task ID
        :type MigrationId: str
        :param _MigrationName: Backup import task name. For an incremental import task, this field will be left empty.
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :type MigrationName: str
        :param _AppId: Application ID
        :type AppId: int
        :param _Region: Region
        :type Region: str
        :param _InstanceId: ID of migrated target instance
        :type InstanceId: str
        :param _RecoveryType: Migration task restoration type
        :type RecoveryType: str
        :param _UploadType: Backup user upload type. COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :type UploadType: str
        :param _BackupFiles: Backup file list, which is determined by UploadType. If the upload type is COS_URL, URL will be saved. If the upload type is COS_UPLOAD, the backup name will be saved.
        :type BackupFiles: list of str
        :param _Status: Migration task status. Valid values: `2` (Creation completed), `7` (Importing full backups), `8` (Waiting for incremental backups), `9` (Import success), `10` (Import failure), `12` (Importing incremental backups).
        :type Status: int
        :param _CreateTime: Migration task creation time
        :type CreateTime: str
        :param _StartTime: Migration task start time
        :type StartTime: str
        :param _EndTime: Migration task end time
        :type EndTime: str
        :param _Message: More information
        :type Message: str
        :param _Detail: Migration detail
        :type Detail: :class:`tencentcloud.sqlserver.v20180328.models.MigrationDetail`
        :param _Action: Operation allowed in the current status
        :type Action: :class:`tencentcloud.sqlserver.v20180328.models.MigrationAction`
        :param _IsRecovery: Whether this is the final restoration. For a full import task, this field will be left empty.
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :type IsRecovery: str
        :param _DBRename: Name set of renamed databases
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBRename: list of DBRenameRes
        """
        self._MigrationId = None
        self._MigrationName = None
        self._AppId = None
        self._Region = None
        self._InstanceId = None
        self._RecoveryType = None
        self._UploadType = None
        self._BackupFiles = None
        self._Status = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Message = None
        self._Detail = None
        self._Action = None
        self._IsRecovery = None
        self._DBRename = None

    @property
    def MigrationId(self):
        """Backup import task ID or incremental import task ID
        :rtype: str
        """
        return self._MigrationId

    @MigrationId.setter
    def MigrationId(self, MigrationId):
        self._MigrationId = MigrationId

    @property
    def MigrationName(self):
        """Backup import task name. For an incremental import task, this field will be left empty.
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def AppId(self):
        """Application ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        """ID of migrated target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RecoveryType(self):
        """Migration task restoration type
        :rtype: str
        """
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        """Backup user upload type. COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :rtype: str
        """
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def BackupFiles(self):
        """Backup file list, which is determined by UploadType. If the upload type is COS_URL, URL will be saved. If the upload type is COS_UPLOAD, the backup name will be saved.
        :rtype: list of str
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def Status(self):
        """Migration task status. Valid values: `2` (Creation completed), `7` (Importing full backups), `8` (Waiting for incremental backups), `9` (Import success), `10` (Import failure), `12` (Importing incremental backups).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """Migration task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """Migration task start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Migration task end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Message(self):
        """More information
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Detail(self):
        """Migration detail
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrationDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Action(self):
        """Operation allowed in the current status
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrationAction`
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def IsRecovery(self):
        """Whether this is the final restoration. For a full import task, this field will be left empty.
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery

    @property
    def DBRename(self):
        """Name set of renamed databases
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DBRenameRes
        """
        return self._DBRename

    @DBRename.setter
    def DBRename(self, DBRename):
        self._DBRename = DBRename


    def _deserialize(self, params):
        self._MigrationId = params.get("MigrationId")
        self._MigrationName = params.get("MigrationName")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        self._RecoveryType = params.get("RecoveryType")
        self._UploadType = params.get("UploadType")
        self._BackupFiles = params.get("BackupFiles")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Message = params.get("Message")
        if params.get("Detail") is not None:
            self._Detail = MigrationDetail()
            self._Detail._deserialize(params.get("Detail"))
        if params.get("Action") is not None:
            self._Action = MigrationAction()
            self._Action._deserialize(params.get("Action"))
        self._IsRecovery = params.get("IsRecovery")
        if params.get("DBRename") is not None:
            self._DBRename = []
            for item in params.get("DBRename"):
                obj = DBRenameRes()
                obj._deserialize(item)
                self._DBRename.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationAction(AbstractModel):
    """Operation allowed by a cold backup import task

    """

    def __init__(self):
        r"""
        :param _AllAction: All the allowed operations. Values include: view (viewing a task), modify (modifying a task), start (starting a task), incremental (creating an incremental task), delete (deleting a task), and upload (obtaining the upload permission).
        :type AllAction: list of str
        :param _AllowedAction: Operation allowed in the current status. If the subset of AllAction is left empty, no operations will be allowed.
        :type AllowedAction: list of str
        """
        self._AllAction = None
        self._AllowedAction = None

    @property
    def AllAction(self):
        """All the allowed operations. Values include: view (viewing a task), modify (modifying a task), start (starting a task), incremental (creating an incremental task), delete (deleting a task), and upload (obtaining the upload permission).
        :rtype: list of str
        """
        return self._AllAction

    @AllAction.setter
    def AllAction(self, AllAction):
        self._AllAction = AllAction

    @property
    def AllowedAction(self):
        """Operation allowed in the current status. If the subset of AllAction is left empty, no operations will be allowed.
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
        


class MigrationDetail(AbstractModel):
    """Details of a cold backup import task

    """

    def __init__(self):
        r"""
        :param _StepAll: Total number of steps
        :type StepAll: int
        :param _StepNow: Current step
        :type StepNow: int
        :param _Progress: Overall progress. For example, “30” means 30%.
        :type Progress: int
        :param _StepInfo: Step information. ‘null’ means the migration has not started
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :type StepInfo: list of MigrationStep
        """
        self._StepAll = None
        self._StepNow = None
        self._Progress = None
        self._StepInfo = None

    @property
    def StepAll(self):
        """Total number of steps
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """Current step
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Progress(self):
        """Overall progress. For example, “30” means 30%.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepInfo(self):
        """Step information. ‘null’ means the migration has not started
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :rtype: list of MigrationStep
        """
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo


    def _deserialize(self, params):
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._Progress = params.get("Progress")
        if params.get("StepInfo") is not None:
            self._StepInfo = []
            for item in params.get("StepInfo"):
                obj = MigrationStep()
                obj._deserialize(item)
                self._StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationStep(AbstractModel):
    """Migration steps of a cold backup import task

    """

    def __init__(self):
        r"""
        :param _StepNo: Step sequence
        :type StepNo: int
        :param _StepName: Step name
        :type StepName: str
        :param _StepId: Step ID in English
        :type StepId: str
        :param _Status: Step status: 0 (default value), 1 (succeeded), 2 (failed), 3 (in progress), 4 (not started)
        :type Status: int
        """
        self._StepNo = None
        self._StepName = None
        self._StepId = None
        self._Status = None

    @property
    def StepNo(self):
        """Step sequence
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        """Step name
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        """Step ID in English
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        """Step status: 0 (default value), 1 (succeeded), 2 (failed), 3 (in progress), 4 (not started)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegeRequest(AbstractModel):
    """ModifyAccountPrivilege request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param _Accounts: Account permission change information
        :type Accounts: list of AccountPrivilegeModifyInfo
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        """Database instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        """Account permission change information
        :rtype: list of AccountPrivilegeModifyInfo
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilegeModifyInfo()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegeResponse(AbstractModel):
    """ModifyAccountPrivilege response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyAccountRemarkRequest(AbstractModel):
    """ModifyAccountRemark request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        :param _Accounts: Information of account for which to modify remarks
        :type Accounts: list of AccountRemark
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-j8kv137v
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        """Information of account for which to modify remarks
        :rtype: list of AccountRemark
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountRemark()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountRemarkResponse(AbstractModel):
    """ModifyAccountRemark response structure.

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


class ModifyBackupMigrationRequest(AbstractModel):
    """ModifyBackupMigration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param _MigrationName: Task name
        :type MigrationName: str
        :param _RecoveryType: Migration task restoration type: FULL,FULL_LOG,FULL_DIFF
        :type RecoveryType: str
        :param _UploadType: COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :type UploadType: str
        :param _BackupFiles: If the UploadType is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :type BackupFiles: list of str
        :param _DBRename: Name set of databases to be renamed
        :type DBRename: list of RenameRestoreDatabase
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._MigrationName = None
        self._RecoveryType = None
        self._UploadType = None
        self._BackupFiles = None
        self._DBRename = None

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def MigrationName(self):
        """Task name
        :rtype: str
        """
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def RecoveryType(self):
        """Migration task restoration type: FULL,FULL_LOG,FULL_DIFF
        :rtype: str
        """
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        """COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :rtype: str
        """
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def BackupFiles(self):
        """If the UploadType is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :rtype: list of str
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def DBRename(self):
        """Name set of databases to be renamed
        :rtype: list of RenameRestoreDatabase
        """
        return self._DBRename

    @DBRename.setter
    def DBRename(self, DBRename):
        self._DBRename = DBRename


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._MigrationName = params.get("MigrationName")
        self._RecoveryType = params.get("RecoveryType")
        self._UploadType = params.get("UploadType")
        self._BackupFiles = params.get("BackupFiles")
        if params.get("DBRename") is not None:
            self._DBRename = []
            for item in params.get("DBRename"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._DBRename.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupMigrationResponse(AbstractModel):
    """ModifyBackupMigration response structure.

    """

    def __init__(self):
        r"""
        :param _BackupMigrationId: Backup import task ID
        :type BackupMigrationId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupMigrationId = None
        self._RequestId = None

    @property
    def BackupMigrationId(self):
        """Backup import task ID
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

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
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._RequestId = params.get("RequestId")


class ModifyBackupStrategyRequest(AbstractModel):
    """ModifyBackupStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _BackupType: Backup type. Valid values: `weekly` (when length(BackupDay) <=7 && length(BackupDay) >=2), `daily` (when length(BackupDay)=1). Default value: `daily`.
        :type BackupType: str
        :param _BackupTime: Backup time. Value range: an integer from 0 to 23.
        :type BackupTime: int
        :param _BackupDay: Backup interval in days when the `BackupType` is `daily`. Valid value: 1.
        :type BackupDay: int
        :param _BackupModel: Backup mode. Valid values: `master_pkg` (archive the backup files of the primary node), `master_no_pkg` (do not archive the backup files of the primary node), `slave_pkg` (archive the backup files of the replica node), `slave_no_pkg` (do not archive the backup files of the replica node). Backup files of the replica node are supported only when Always On disaster recovery is enabled.
        :type BackupModel: str
        :param _BackupCycle: The days of the week on which backup will be performed when “BackupType” is `weekly`. If data backup retention period is less than 7 days, the values will be 1-7, indicating that backup will be performed everyday by default; if data backup retention period is greater than or equal to 7 days, the values will be at least any two days, indicating that backup will be performed at least twice in a week by default.
        :type BackupCycle: list of int non-negative
        :param _BackupSaveDays: Data (log) backup retention period. Value range: 3-1830 days, default value: 7 days.
        :type BackupSaveDays: int
        :param _RegularBackupEnable: Archive backup status. Valid values: `enable` (enabled); `disable` (disabled). Default value: `disable`.
        :type RegularBackupEnable: str
        :param _RegularBackupSaveDays: Archive backup retention days. Value range: 90–3650 days. Default value: 365 days.
        :type RegularBackupSaveDays: int
        :param _RegularBackupStrategy: Archive backup policy. Valid values: `years` (yearly); `quarters (quarterly); `months` (monthly); Default value: `months`.
        :type RegularBackupStrategy: str
        :param _RegularBackupCounts: The number of retained archive backups. Default value: `1`.
        :type RegularBackupCounts: int
        :param _RegularBackupStartTime: Archive backup start date in YYYY-MM-DD format, which is the current time by default.
        :type RegularBackupStartTime: str
        """
        self._InstanceId = None
        self._BackupType = None
        self._BackupTime = None
        self._BackupDay = None
        self._BackupModel = None
        self._BackupCycle = None
        self._BackupSaveDays = None
        self._RegularBackupEnable = None
        self._RegularBackupSaveDays = None
        self._RegularBackupStrategy = None
        self._RegularBackupCounts = None
        self._RegularBackupStartTime = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupType(self):
        """Backup type. Valid values: `weekly` (when length(BackupDay) <=7 && length(BackupDay) >=2), `daily` (when length(BackupDay)=1). Default value: `daily`.
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupTime(self):
        """Backup time. Value range: an integer from 0 to 23.
        :rtype: int
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def BackupDay(self):
        """Backup interval in days when the `BackupType` is `daily`. Valid value: 1.
        :rtype: int
        """
        return self._BackupDay

    @BackupDay.setter
    def BackupDay(self, BackupDay):
        self._BackupDay = BackupDay

    @property
    def BackupModel(self):
        """Backup mode. Valid values: `master_pkg` (archive the backup files of the primary node), `master_no_pkg` (do not archive the backup files of the primary node), `slave_pkg` (archive the backup files of the replica node), `slave_no_pkg` (do not archive the backup files of the replica node). Backup files of the replica node are supported only when Always On disaster recovery is enabled.
        :rtype: str
        """
        return self._BackupModel

    @BackupModel.setter
    def BackupModel(self, BackupModel):
        self._BackupModel = BackupModel

    @property
    def BackupCycle(self):
        """The days of the week on which backup will be performed when “BackupType” is `weekly`. If data backup retention period is less than 7 days, the values will be 1-7, indicating that backup will be performed everyday by default; if data backup retention period is greater than or equal to 7 days, the values will be at least any two days, indicating that backup will be performed at least twice in a week by default.
        :rtype: list of int non-negative
        """
        return self._BackupCycle

    @BackupCycle.setter
    def BackupCycle(self, BackupCycle):
        self._BackupCycle = BackupCycle

    @property
    def BackupSaveDays(self):
        """Data (log) backup retention period. Value range: 3-1830 days, default value: 7 days.
        :rtype: int
        """
        return self._BackupSaveDays

    @BackupSaveDays.setter
    def BackupSaveDays(self, BackupSaveDays):
        self._BackupSaveDays = BackupSaveDays

    @property
    def RegularBackupEnable(self):
        """Archive backup status. Valid values: `enable` (enabled); `disable` (disabled). Default value: `disable`.
        :rtype: str
        """
        return self._RegularBackupEnable

    @RegularBackupEnable.setter
    def RegularBackupEnable(self, RegularBackupEnable):
        self._RegularBackupEnable = RegularBackupEnable

    @property
    def RegularBackupSaveDays(self):
        """Archive backup retention days. Value range: 90–3650 days. Default value: 365 days.
        :rtype: int
        """
        return self._RegularBackupSaveDays

    @RegularBackupSaveDays.setter
    def RegularBackupSaveDays(self, RegularBackupSaveDays):
        self._RegularBackupSaveDays = RegularBackupSaveDays

    @property
    def RegularBackupStrategy(self):
        """Archive backup policy. Valid values: `years` (yearly); `quarters (quarterly); `months` (monthly); Default value: `months`.
        :rtype: str
        """
        return self._RegularBackupStrategy

    @RegularBackupStrategy.setter
    def RegularBackupStrategy(self, RegularBackupStrategy):
        self._RegularBackupStrategy = RegularBackupStrategy

    @property
    def RegularBackupCounts(self):
        """The number of retained archive backups. Default value: `1`.
        :rtype: int
        """
        return self._RegularBackupCounts

    @RegularBackupCounts.setter
    def RegularBackupCounts(self, RegularBackupCounts):
        self._RegularBackupCounts = RegularBackupCounts

    @property
    def RegularBackupStartTime(self):
        """Archive backup start date in YYYY-MM-DD format, which is the current time by default.
        :rtype: str
        """
        return self._RegularBackupStartTime

    @RegularBackupStartTime.setter
    def RegularBackupStartTime(self, RegularBackupStartTime):
        self._RegularBackupStartTime = RegularBackupStartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupType = params.get("BackupType")
        self._BackupTime = params.get("BackupTime")
        self._BackupDay = params.get("BackupDay")
        self._BackupModel = params.get("BackupModel")
        self._BackupCycle = params.get("BackupCycle")
        self._BackupSaveDays = params.get("BackupSaveDays")
        self._RegularBackupEnable = params.get("RegularBackupEnable")
        self._RegularBackupSaveDays = params.get("RegularBackupSaveDays")
        self._RegularBackupStrategy = params.get("RegularBackupStrategy")
        self._RegularBackupCounts = params.get("RegularBackupCounts")
        self._RegularBackupStartTime = params.get("RegularBackupStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupStrategyResponse(AbstractModel):
    """ModifyBackupStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Errno: Returned error code.
        :type Errno: int
        :param _Msg: Returned error message.
        :type Msg: str
        :param _Code: 
        :type Code: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Errno = None
        self._Msg = None
        self._Code = None
        self._RequestId = None

    @property
    def Errno(self):
        warnings.warn("parameter `Errno` is deprecated", DeprecationWarning) 

        """Returned error code.
        :rtype: int
        """
        return self._Errno

    @Errno.setter
    def Errno(self, Errno):
        warnings.warn("parameter `Errno` is deprecated", DeprecationWarning) 

        self._Errno = Errno

    @property
    def Msg(self):
        """Returned error message.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Code(self):
        """
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

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
        self._Errno = params.get("Errno")
        self._Msg = params.get("Msg")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class ModifyDBEncryptAttributesRequest(AbstractModel):
    """ModifyDBEncryptAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DBTDEEncrypt: A parameter used to enable or disable TDE of the database
        :type DBTDEEncrypt: list of DBTDEEncrypt
        """
        self._InstanceId = None
        self._DBTDEEncrypt = None

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
    def DBTDEEncrypt(self):
        """A parameter used to enable or disable TDE of the database
        :rtype: list of DBTDEEncrypt
        """
        return self._DBTDEEncrypt

    @DBTDEEncrypt.setter
    def DBTDEEncrypt(self, DBTDEEncrypt):
        self._DBTDEEncrypt = DBTDEEncrypt


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DBTDEEncrypt") is not None:
            self._DBTDEEncrypt = []
            for item in params.get("DBTDEEncrypt"):
                obj = DBTDEEncrypt()
                obj._deserialize(item)
                self._DBTDEEncrypt.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBEncryptAttributesResponse(AbstractModel):
    """ModifyDBEncryptAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param _InstanceName: New name of database instance
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        """Database instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """New name of database instance
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
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName response structure.

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


class ModifyDBInstanceNetworkRequest(AbstractModel):
    """ModifyDBInstanceNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _NewVpcId: ID of the new VPC
        :type NewVpcId: str
        :param _NewSubnetId: ID of the new subnet
        :type NewSubnetId: str
        :param _OldIpRetainTime: Retention period (in hours) of the original VIP. Value range: `0-168`. Default value: `0`, indicating the original VIP is released immediately.
        :type OldIpRetainTime: int
        :param _Vip: New VIP
        :type Vip: str
        :param _DRNetwork: 
        :type DRNetwork: int
        """
        self._InstanceId = None
        self._NewVpcId = None
        self._NewSubnetId = None
        self._OldIpRetainTime = None
        self._Vip = None
        self._DRNetwork = None

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
    def NewVpcId(self):
        """ID of the new VPC
        :rtype: str
        """
        return self._NewVpcId

    @NewVpcId.setter
    def NewVpcId(self, NewVpcId):
        self._NewVpcId = NewVpcId

    @property
    def NewSubnetId(self):
        """ID of the new subnet
        :rtype: str
        """
        return self._NewSubnetId

    @NewSubnetId.setter
    def NewSubnetId(self, NewSubnetId):
        self._NewSubnetId = NewSubnetId

    @property
    def OldIpRetainTime(self):
        """Retention period (in hours) of the original VIP. Value range: `0-168`. Default value: `0`, indicating the original VIP is released immediately.
        :rtype: int
        """
        return self._OldIpRetainTime

    @OldIpRetainTime.setter
    def OldIpRetainTime(self, OldIpRetainTime):
        self._OldIpRetainTime = OldIpRetainTime

    @property
    def Vip(self):
        """New VIP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def DRNetwork(self):
        """
        :rtype: int
        """
        return self._DRNetwork

    @DRNetwork.setter
    def DRNetwork(self, DRNetwork):
        self._DRNetwork = DRNetwork


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NewVpcId = params.get("NewVpcId")
        self._NewSubnetId = params.get("NewSubnetId")
        self._OldIpRetainTime = params.get("OldIpRetainTime")
        self._Vip = params.get("Vip")
        self._DRNetwork = params.get("DRNetwork")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNetworkResponse(AbstractModel):
    """ModifyDBInstanceNetwork response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: ID of the instance network changing task. You can use the [DescribeFlowStatus](https://intl.cloud.tencent.com/document/product/238/19967?from_cn_redirect=1) API to query the task status.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """ID of the instance network changing task. You can use the [DescribeFlowStatus](https://intl.cloud.tencent.com/document/product/238/19967?from_cn_redirect=1) API to query the task status.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: Array of instance IDs in the format of mssql-j8kv137v
        :type InstanceIdSet: list of str
        :param _ProjectId: Project ID. If this parameter is 0, the default project will be used
        :type ProjectId: int
        """
        self._InstanceIdSet = None
        self._ProjectId = None

    @property
    def InstanceIdSet(self):
        """Array of instance IDs in the format of mssql-j8kv137v
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def ProjectId(self):
        """Project ID. If this parameter is 0, the default project will be used
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of successfully modified instances
        :type Count: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        """Number of successfully modified instances
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

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
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class ModifyDBNameRequest(AbstractModel):
    """ModifyDBName request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _OldDBName: Old database name
        :type OldDBName: str
        :param _NewDBName: New name of database
        :type NewDBName: str
        """
        self._InstanceId = None
        self._OldDBName = None
        self._NewDBName = None

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
    def OldDBName(self):
        """Old database name
        :rtype: str
        """
        return self._OldDBName

    @OldDBName.setter
    def OldDBName(self, OldDBName):
        self._OldDBName = OldDBName

    @property
    def NewDBName(self):
        """New name of database
        :rtype: str
        """
        return self._NewDBName

    @NewDBName.setter
    def NewDBName(self, NewDBName):
        self._NewDBName = NewDBName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldDBName = params.get("OldDBName")
        self._NewDBName = params.get("NewDBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBNameResponse(AbstractModel):
    """ModifyDBName response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBRemarkRequest(AbstractModel):
    """ModifyDBRemark request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-rljoi3bf
        :type InstanceId: str
        :param _DBRemarks: Array of database names and remarks, where each element contains a database name and the corresponding remarks
        :type DBRemarks: list of DBRemark
        """
        self._InstanceId = None
        self._DBRemarks = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-rljoi3bf
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBRemarks(self):
        """Array of database names and remarks, where each element contains a database name and the corresponding remarks
        :rtype: list of DBRemark
        """
        return self._DBRemarks

    @DBRemarks.setter
    def DBRemarks(self, DBRemarks):
        self._DBRemarks = DBRemarks


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DBRemarks") is not None:
            self._DBRemarks = []
            for item in params.get("DBRemarks"):
                obj = DBRemark()
                obj._deserialize(item)
                self._DBRemarks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBRemarkResponse(AbstractModel):
    """ModifyDBRemark response structure.

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


class ModifyDReadableRequest(AbstractModel):
    """ModifyDReadable request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Type: Operation type. Valid values: enable - enabling the read-only mode of the replica server; disable - disabling the read-only mode of the replica server
        :type Type: str
        :param _VpcId: Replica server network ID, which will be consistent with the primary instance by default if left blank
        :type VpcId: str
        :param _SubnetId: Replica server subnet ID, which will be consistent with the primary instance by default if left blank
        :type SubnetId: str
        :param _Vip: Specified replica server read-only VIP, which will be assigned automatically if left blank
        :type Vip: str
        """
        self._InstanceId = None
        self._Type = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None

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
    def Type(self):
        """Operation type. Valid values: enable - enabling the read-only mode of the replica server; disable - disabling the read-only mode of the replica server
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VpcId(self):
        """Replica server network ID, which will be consistent with the primary instance by default if left blank
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Replica server subnet ID, which will be consistent with the primary instance by default if left blank
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        """Specified replica server read-only VIP, which will be assigned automatically if left blank
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
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
        


class ModifyDReadableResponse(AbstractModel):
    """ModifyDReadable response structure.

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
        """Task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDatabaseCDCRequest(AbstractModel):
    """ModifyDatabaseCDC request structure.

    """

    def __init__(self):
        r"""
        :param _DBNames: Array of database names
        :type DBNames: list of str
        :param _ModifyType: Enable or disable CDC. Valid values: `enable`, `disable`
        :type ModifyType: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._DBNames = None
        self._ModifyType = None
        self._InstanceId = None

    @property
    def DBNames(self):
        """Array of database names
        :rtype: list of str
        """
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def ModifyType(self):
        """Enable or disable CDC. Valid values: `enable`, `disable`
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DBNames = params.get("DBNames")
        self._ModifyType = params.get("ModifyType")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseCDCResponse(AbstractModel):
    """ModifyDatabaseCDC response structure.

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
        """Task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDatabaseCTRequest(AbstractModel):
    """ModifyDatabaseCT request structure.

    """

    def __init__(self):
        r"""
        :param _DBNames: Array of database names
        :type DBNames: list of str
        :param _ModifyType: Enable or disable CT. Valid values: `enable`, `disable`
        :type ModifyType: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ChangeRetentionDay: Retention period (in days) of change tracking information when CT is enabled. Value range: 3-30. Default value: `3`
        :type ChangeRetentionDay: int
        """
        self._DBNames = None
        self._ModifyType = None
        self._InstanceId = None
        self._ChangeRetentionDay = None

    @property
    def DBNames(self):
        """Array of database names
        :rtype: list of str
        """
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def ModifyType(self):
        """Enable or disable CT. Valid values: `enable`, `disable`
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

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
    def ChangeRetentionDay(self):
        """Retention period (in days) of change tracking information when CT is enabled. Value range: 3-30. Default value: `3`
        :rtype: int
        """
        return self._ChangeRetentionDay

    @ChangeRetentionDay.setter
    def ChangeRetentionDay(self, ChangeRetentionDay):
        self._ChangeRetentionDay = ChangeRetentionDay


    def _deserialize(self, params):
        self._DBNames = params.get("DBNames")
        self._ModifyType = params.get("ModifyType")
        self._InstanceId = params.get("InstanceId")
        self._ChangeRetentionDay = params.get("ChangeRetentionDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseCTResponse(AbstractModel):
    """ModifyDatabaseCT response structure.

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
        """Task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDatabaseMdfRequest(AbstractModel):
    """ModifyDatabaseMdf request structure.

    """

    def __init__(self):
        r"""
        :param _DBNames: Array of database names
        :type DBNames: list of str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._DBNames = None
        self._InstanceId = None

    @property
    def DBNames(self):
        """Array of database names
        :rtype: list of str
        """
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DBNames = params.get("DBNames")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseMdfResponse(AbstractModel):
    """ModifyDatabaseMdf response structure.

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
        """Task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyIncrementalMigrationRequest(AbstractModel):
    """ModifyIncrementalMigration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param _IncrementalMigrationId: Incremental backup import task ID, which is returned through the `CreateIncrementalMigration` API.
        :type IncrementalMigrationId: str
        :param _IsRecovery: Whether to restore backups. Valid values: `NO`, `YES`. If this parameter is not specified, current settings will be applied.
        :type IsRecovery: str
        :param _BackupFiles: If the UploadType is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :type BackupFiles: list of str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._IncrementalMigrationId = None
        self._IsRecovery = None
        self._BackupFiles = None

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        """Incremental backup import task ID, which is returned through the `CreateIncrementalMigration` API.
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId

    @property
    def IsRecovery(self):
        """Whether to restore backups. Valid values: `NO`, `YES`. If this parameter is not specified, current settings will be applied.
        :rtype: str
        """
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery

    @property
    def BackupFiles(self):
        """If the UploadType is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :rtype: list of str
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        self._IsRecovery = params.get("IsRecovery")
        self._BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIncrementalMigrationResponse(AbstractModel):
    """ModifyIncrementalMigration response structure.

    """

    def __init__(self):
        r"""
        :param _IncrementalMigrationId: ID of an incremental backup import task
        :type IncrementalMigrationId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IncrementalMigrationId = None
        self._RequestId = None

    @property
    def IncrementalMigrationId(self):
        """ID of an incremental backup import task
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId

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
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceEncryptAttributesRequest(AbstractModel):
    """ModifyInstanceEncryptAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _CertificateAttribution: Certificate ownership. Valid values: `self` (certificate of this account), `others` (certificate of the other account). Default value: `self`.
        :type CertificateAttribution: str
        :param _QuoteUin: ID of the other referenced root account, which is required when `CertificateAttribution` is `others`.
        :type QuoteUin: str
        """
        self._InstanceId = None
        self._CertificateAttribution = None
        self._QuoteUin = None

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
    def CertificateAttribution(self):
        """Certificate ownership. Valid values: `self` (certificate of this account), `others` (certificate of the other account). Default value: `self`.
        :rtype: str
        """
        return self._CertificateAttribution

    @CertificateAttribution.setter
    def CertificateAttribution(self, CertificateAttribution):
        self._CertificateAttribution = CertificateAttribution

    @property
    def QuoteUin(self):
        """ID of the other referenced root account, which is required when `CertificateAttribution` is `others`.
        :rtype: str
        """
        return self._QuoteUin

    @QuoteUin.setter
    def QuoteUin(self, QuoteUin):
        self._QuoteUin = QuoteUin


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CertificateAttribution = params.get("CertificateAttribution")
        self._QuoteUin = params.get("QuoteUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceEncryptAttributesResponse(AbstractModel):
    """ModifyInstanceEncryptAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list.
        :type InstanceIds: list of str
        :param _ParamList: List of modified parameters. Each list element has two fields: `Name` and `CurrentValue`. Set `Name` to the parameter name and `CurrentValue` to the new value after modification. <b>Note</b>: if the instance needs to be <b>restarted</b> for the modified parameter to take effect, it will be <b>restarted</b> immediately or during the maintenance time. Before you modify a parameter, you can use the `DescribeInstanceParams` API to query whether the instance needs to be restarted.
        :type ParamList: list of Parameter
        :param _WaitSwitch: When to execute the parameter modification task. Valid values: `0` (execute immediately), `1` (execute during maintenance time). Default value: `0`.
        :type WaitSwitch: int
        """
        self._InstanceIds = None
        self._ParamList = None
        self._WaitSwitch = None

    @property
    def InstanceIds(self):
        """Instance ID list.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamList(self):
        """List of modified parameters. Each list element has two fields: `Name` and `CurrentValue`. Set `Name` to the parameter name and `CurrentValue` to the new value after modification. <b>Note</b>: if the instance needs to be <b>restarted</b> for the modified parameter to take effect, it will be <b>restarted</b> immediately or during the maintenance time. Before you modify a parameter, you can use the `DescribeInstanceParams` API to query whether the instance needs to be restarted.
        :rtype: list of Parameter
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def WaitSwitch(self):
        """When to execute the parameter modification task. Valid values: `0` (execute immediately), `1` (execute during maintenance time). Default value: `0`.
        :rtype: int
        """
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam response structure.

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


class ModifyMigrationRequest(AbstractModel):
    """ModifyMigration request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        :param _MigrateName: New name of migration task. If this parameter is left empty, no modification will be made
        :type MigrateName: str
        :param _MigrateType: New migration type (1: structure migration, 2: data migration, 3: incremental sync). If this parameter is left empty, no modification will be made
        :type MigrateType: int
        :param _SourceType: Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode). If this parameter is left empty, no modification will be made
        :type SourceType: int
        :param _Source: Migration source. If this parameter is left empty, no modification will be made
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param _Target: Migration target. If this parameter is left empty, no modification will be made
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param _MigrateDBSet: Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5). If it left empty, no modification will be made
        :type MigrateDBSet: list of MigrateDB
        """
        self._MigrateId = None
        self._MigrateName = None
        self._MigrateType = None
        self._SourceType = None
        self._Source = None
        self._Target = None
        self._MigrateDBSet = None

    @property
    def MigrateId(self):
        """Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def MigrateName(self):
        """New name of migration task. If this parameter is left empty, no modification will be made
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def MigrateType(self):
        """New migration type (1: structure migration, 2: data migration, 3: incremental sync). If this parameter is left empty, no modification will be made
        :rtype: int
        """
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def SourceType(self):
        """Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode). If this parameter is left empty, no modification will be made
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Source(self):
        """Migration source. If this parameter is left empty, no modification will be made
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        """Migration target. If this parameter is left empty, no modification will be made
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def MigrateDBSet(self):
        """Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5). If it left empty, no modification will be made
        :rtype: list of MigrateDB
        """
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        self._MigrateName = params.get("MigrateName")
        self._MigrateType = params.get("MigrateType")
        self._SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self._Source = MigrateSource()
            self._Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self._Target = MigrateTarget()
            self._Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self._MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self._MigrateDBSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationResponse(AbstractModel):
    """ModifyMigration response structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MigrateId = None
        self._RequestId = None

    @property
    def MigrateId(self):
        """Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

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
        self._MigrateId = params.get("MigrateId")
        self._RequestId = params.get("RequestId")


class OldVip(AbstractModel):
    """This API is used to return the number of unrecovered IP addresses for the instance.

    """

    def __init__(self):
        r"""
        :param _Vip: Unrecovered old IP addresses
        :type Vip: str
        :param _RecycleTime: IP recovery time
        :type RecycleTime: str
        :param _OldIpRetainTime: Old IP retention time (hours)
Note: This field may return null, indicating that no valid values can be obtained.
        :type OldIpRetainTime: int
        """
        self._Vip = None
        self._RecycleTime = None
        self._OldIpRetainTime = None

    @property
    def Vip(self):
        """Unrecovered old IP addresses
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def RecycleTime(self):
        """IP recovery time
        :rtype: str
        """
        return self._RecycleTime

    @RecycleTime.setter
    def RecycleTime(self, RecycleTime):
        self._RecycleTime = RecycleTime

    @property
    def OldIpRetainTime(self):
        """Old IP retention time (hours)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OldIpRetainTime

    @OldIpRetainTime.setter
    def OldIpRetainTime(self, OldIpRetainTime):
        self._OldIpRetainTime = OldIpRetainTime


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._RecycleTime = params.get("RecycleTime")
        self._OldIpRetainTime = params.get("OldIpRetainTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenInterCommunicationRequest(AbstractModel):
    """OpenInterCommunication request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: IDs of instances with interwoking group enabled
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        """IDs of instances with interwoking group enabled
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenInterCommunicationResponse(AbstractModel):
    """OpenInterCommunication response structure.

    """

    def __init__(self):
        r"""
        :param _InterInstanceFlowSet: IDs of instance and async task
        :type InterInstanceFlowSet: list of InterInstanceFlow
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InterInstanceFlowSet = None
        self._RequestId = None

    @property
    def InterInstanceFlowSet(self):
        """IDs of instance and async task
        :rtype: list of InterInstanceFlow
        """
        return self._InterInstanceFlowSet

    @InterInstanceFlowSet.setter
    def InterInstanceFlowSet(self, InterInstanceFlowSet):
        self._InterInstanceFlowSet = InterInstanceFlowSet

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
        if params.get("InterInstanceFlowSet") is not None:
            self._InterInstanceFlowSet = []
            for item in params.get("InterInstanceFlowSet"):
                obj = InterInstanceFlow()
                obj._deserialize(item)
                self._InterInstanceFlowSet.append(obj)
        self._RequestId = params.get("RequestId")


class ParamRecord(AbstractModel):
    """Instance parameter modification record

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _OldValue: Parameter value before modification
        :type OldValue: str
        :param _NewValue: Parameter value after modification
        :type NewValue: str
        :param _Status: Parameter modification status. Valid values: `1` (initializing and waiting for modification), `2` (modification succeed), `3` (modification failed), `4` (modifying)
        :type Status: int
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._ParamName = None
        self._OldValue = None
        self._NewValue = None
        self._Status = None
        self._ModifyTime = None

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
    def ParamName(self):
        """Parameter name
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def OldValue(self):
        """Parameter value before modification
        :rtype: str
        """
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        """Parameter value after modification
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def Status(self):
        """Parameter modification status. Valid values: `1` (initializing and waiting for modification), `2` (modification succeed), `3` (modification failed), `4` (modifying)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        """Modification time
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ParamName = params.get("ParamName")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        self._Status = params.get("Status")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Parameter(AbstractModel):
    """Database instance parameter

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name
        :type Name: str
        :param _CurrentValue: Parameter value
        :type CurrentValue: str
        """
        self._Name = None
        self._CurrentValue = None

    @property
    def Name(self):
        """Parameter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CurrentValue(self):
        """Parameter value
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CurrentValue = params.get("CurrentValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterDetail(AbstractModel):
    """Instance parameter details

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name
        :type Name: str
        :param _ParamType: Data type of the parameter. Valid values: `integer`, `enum`
        :type ParamType: str
        :param _Default: Default value of the parameter
        :type Default: str
        :param _Description: Parameter description
        :type Description: str
        :param _CurrentValue: Current value of the parameter
        :type CurrentValue: str
        :param _NeedReboot: Whether the database needs to be restarted for the modified parameter to take effect. Valid values: `0` (no),`1` (yes)
        :type NeedReboot: int
        :param _Max: Maximum value of the parameter
        :type Max: int
        :param _Min: Minimum value of the parameter
        :type Min: int
        :param _EnumValue: Enumerated values of the parameter
        :type EnumValue: list of str
        :param _Status: Parameter status. Valid values: `0` (normal), `1` (modifying)
        :type Status: int
        """
        self._Name = None
        self._ParamType = None
        self._Default = None
        self._Description = None
        self._CurrentValue = None
        self._NeedReboot = None
        self._Max = None
        self._Min = None
        self._EnumValue = None
        self._Status = None

    @property
    def Name(self):
        """Parameter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamType(self):
        """Data type of the parameter. Valid values: `integer`, `enum`
        :rtype: str
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Default(self):
        """Default value of the parameter
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        """Parameter description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        """Current value of the parameter
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        """Whether the database needs to be restarted for the modified parameter to take effect. Valid values: `0` (no),`1` (yes)
        :rtype: int
        """
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        """Maximum value of the parameter
        :rtype: int
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        """Minimum value of the parameter
        :rtype: int
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        """Enumerated values of the parameter
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
        """Parameter status. Valid values: `0` (normal), `1` (modifying)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ParamType = params.get("ParamType")
        self._Default = params.get("Default")
        self._Description = params.get("Description")
        self._CurrentValue = params.get("CurrentValue")
        self._NeedReboot = params.get("NeedReboot")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecycleDBInstanceRequest(AbstractModel):
    """RecycleDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID
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
        


class RecycleDBInstanceResponse(AbstractModel):
    """RecycleDBInstance response structure.

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
        """Task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param _Region: Region ID in the format of ap-guangzhou
        :type Region: str
        :param _RegionName: Region name
        :type RegionName: str
        :param _RegionId: Numeric ID of region
        :type RegionId: int
        :param _RegionState: Current purchasability of this region. UNAVAILABLE: not purchasable, AVAILABLE: purchasable
        :type RegionState: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionId = None
        self._RegionState = None

    @property
    def Region(self):
        """Region ID in the format of ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        """Region name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        """Numeric ID of region
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionState(self):
        """Current purchasability of this region. UNAVAILABLE: not purchasable, AVAILABLE: purchasable
        :rtype: str
        """
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameRestoreDatabase(AbstractModel):
    """It is used to specify and rename the database to be restored through the `RestoreInstance`, `RollbackInstance`, `CreateMigration`, `CloneDB` or `ModifyBackupMigration` APIs.

    """

    def __init__(self):
        r"""
        :param _OldName: Database name. If the `OldName` database does not exist, a failure will be returned.
It can be left empty in offline migration tasks.
        :type OldName: str
        :param _NewName: New database name. In offline migration, `OldName` will be used if `NewName` is left empty (`OldName` and `NewName` cannot be both empty). In database cloning, `OldName` and `NewName` must be both specified and cannot have the same value.
        :type NewName: str
        """
        self._OldName = None
        self._NewName = None

    @property
    def OldName(self):
        """Database name. If the `OldName` database does not exist, a failure will be returned.
It can be left empty in offline migration tasks.
        :rtype: str
        """
        return self._OldName

    @OldName.setter
    def OldName(self, OldName):
        self._OldName = OldName

    @property
    def NewName(self):
        """New database name. In offline migration, `OldName` will be used if `NewName` is left empty (`OldName` and `NewName` cannot be both empty). In database cloning, `OldName` and `NewName` must be both specified and cannot have the same value.
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName


    def _deserialize(self, params):
        self._OldName = params.get("OldName")
        self._NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param _Accounts: Updated account password information array
        :type Accounts: list of AccountPassword
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        """Database instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        """Updated account password information array
        :rtype: list of AccountPassword
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPassword()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: ID of asynchronous task flow for account password modification
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """ID of asynchronous task flow for account password modification
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """The information of tags associated with instances

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
        


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Database instance ID in the format of mssql-njj2mtpl
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
        


class RestartDBInstanceResponse(AbstractModel):
    """RestartDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        :param _BackupId: Backup file ID, which can be obtained through the `Id` field in the returned value of the `DescribeBackups` API
        :type BackupId: int
        :param _TargetInstanceId: ID of the target instance to which the backup is restored. The target instance should be under the same `APPID`. If this parameter is left empty, ID of the source instance will be used.
        :type TargetInstanceId: str
        :param _RenameRestore: Restore the databases listed in `ReNameRestoreDatabase` and rename them after restoration. If this parameter is left empty, all databases will be restored and renamed in the default format.
        :type RenameRestore: list of RenameRestoreDatabase
        :param _Type: Rollback type. Valid values: `0` (overwriting), `1` (renaming).
        :type Type: int
        :param _DBList: Database to be overwritten, which is required when overwriting a rollback database.
        :type DBList: list of str
        :param _GroupId: Group ID of unarchived backup files grouped by backup task
        :type GroupId: str
        """
        self._InstanceId = None
        self._BackupId = None
        self._TargetInstanceId = None
        self._RenameRestore = None
        self._Type = None
        self._DBList = None
        self._GroupId = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-j8kv137v
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        """Backup file ID, which can be obtained through the `Id` field in the returned value of the `DescribeBackups` API
        :rtype: int
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def TargetInstanceId(self):
        """ID of the target instance to which the backup is restored. The target instance should be under the same `APPID`. If this parameter is left empty, ID of the source instance will be used.
        :rtype: str
        """
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def RenameRestore(self):
        """Restore the databases listed in `ReNameRestoreDatabase` and rename them after restoration. If this parameter is left empty, all databases will be restored and renamed in the default format.
        :rtype: list of RenameRestoreDatabase
        """
        return self._RenameRestore

    @RenameRestore.setter
    def RenameRestore(self, RenameRestore):
        self._RenameRestore = RenameRestore

    @property
    def Type(self):
        """Rollback type. Valid values: `0` (overwriting), `1` (renaming).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DBList(self):
        """Database to be overwritten, which is required when overwriting a rollback database.
        :rtype: list of str
        """
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

    @property
    def GroupId(self):
        """Group ID of unarchived backup files grouped by backup task
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        self._TargetInstanceId = params.get("TargetInstanceId")
        if params.get("RenameRestore") is not None:
            self._RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._RenameRestore.append(obj)
        self._Type = params.get("Type")
        self._DBList = params.get("DBList")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async flow task ID, which can be used to call the `DescribeFlowStatus` API to get the task execution status
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async flow task ID, which can be used to call the `DescribeFlowStatus` API to get the task execution status
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RollbackInstanceRequest(AbstractModel):
    """RollbackInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Type: Rollback type. 0: the database rolled back overwrites the original database; 1: the database rolled back is renamed and does not overwrite the original database
        :type Type: int
        :param _Time: Target time point for rollback
        :type Time: str
        :param _DBs: Database to be rolled back
        :type DBs: list of str
        :param _TargetInstanceId: ID of the target instance to which the backup is restored. The target instance should be under the same `APPID`. If this parameter is left empty, ID of the source instance will be used.
        :type TargetInstanceId: str
        :param _RenameRestore: Rename the databases listed in `ReNameRestoreDatabase`. This parameter takes effect only when `Type = 1` which indicates that backup rollback supports renaming databases. If it is left empty, databases will be renamed in the default format and the `DBs` parameter specifies the databases to be restored.
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self._InstanceId = None
        self._Type = None
        self._Time = None
        self._DBs = None
        self._TargetInstanceId = None
        self._RenameRestore = None

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
    def Type(self):
        """Rollback type. 0: the database rolled back overwrites the original database; 1: the database rolled back is renamed and does not overwrite the original database
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        """Target time point for rollback
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def DBs(self):
        """Database to be rolled back
        :rtype: list of str
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def TargetInstanceId(self):
        """ID of the target instance to which the backup is restored. The target instance should be under the same `APPID`. If this parameter is left empty, ID of the source instance will be used.
        :rtype: str
        """
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def RenameRestore(self):
        """Rename the databases listed in `ReNameRestoreDatabase`. This parameter takes effect only when `Type = 1` which indicates that backup rollback supports renaming databases. If it is left empty, databases will be renamed in the default format and the `DBs` parameter specifies the databases to be restored.
        :rtype: list of RenameRestoreDatabase
        """
        return self._RenameRestore

    @RenameRestore.setter
    def RenameRestore(self, RenameRestore):
        self._RenameRestore = RenameRestore


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._Time = params.get("Time")
        self._DBs = params.get("DBs")
        self._TargetInstanceId = params.get("TargetInstanceId")
        if params.get("RenameRestore") is not None:
            self._RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self._RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstanceResponse(AbstractModel):
    """RollbackInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The async job ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """The async job ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RunMigrationRequest(AbstractModel):
    """RunMigration request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        """Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMigrationResponse(AbstractModel):
    """RunMigration response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: After the migration task starts, the flow ID will be returned
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """After the migration task starts, the flow ID will be returned
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SSLConfig(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Encryption: 
        :type Encryption: str
        :param _SSLValidityPeriod: 
        :type SSLValidityPeriod: str
        :param _SSLValidity: 
        :type SSLValidity: int
        """
        self._Encryption = None
        self._SSLValidityPeriod = None
        self._SSLValidity = None

    @property
    def Encryption(self):
        """
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def SSLValidityPeriod(self):
        """
        :rtype: str
        """
        return self._SSLValidityPeriod

    @SSLValidityPeriod.setter
    def SSLValidityPeriod(self, SSLValidityPeriod):
        self._SSLValidityPeriod = SSLValidityPeriod

    @property
    def SSLValidity(self):
        """
        :rtype: int
        """
        return self._SSLValidity

    @SSLValidity.setter
    def SSLValidity(self, SSLValidity):
        self._SSLValidity = SSLValidity


    def _deserialize(self, params):
        self._Encryption = params.get("Encryption")
        self._SSLValidityPeriod = params.get("SSLValidityPeriod")
        self._SSLValidity = params.get("SSLValidity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveZones(AbstractModel):
    """Replica AZ information

    """

    def __init__(self):
        r"""
        :param _SlaveZone: Replica AZ region code
        :type SlaveZone: str
        :param _SlaveZoneName: Replica AZ
        :type SlaveZoneName: str
        """
        self._SlaveZone = None
        self._SlaveZoneName = None

    @property
    def SlaveZone(self):
        """Replica AZ region code
        :rtype: str
        """
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def SlaveZoneName(self):
        """Replica AZ
        :rtype: str
        """
        return self._SlaveZoneName

    @SlaveZoneName.setter
    def SlaveZoneName(self, SlaveZoneName):
        self._SlaveZoneName = SlaveZoneName


    def _deserialize(self, params):
        self._SlaveZone = params.get("SlaveZone")
        self._SlaveZoneName = params.get("SlaveZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLog(AbstractModel):
    """Slow query log file information

    """

    def __init__(self):
        r"""
        :param _Id: Unique ID of slow query log file
        :type Id: int
        :param _StartTime: File generation start time
        :type StartTime: str
        :param _EndTime: File generation end time
        :type EndTime: str
        :param _Size: File size in KB
        :type Size: int
        :param _Count: Number of logs in file
        :type Count: int
        :param _InternalAddr: Download address for private network
        :type InternalAddr: str
        :param _ExternalAddr: Download address for public network
        :type ExternalAddr: str
        :param _Status: Status (1: success, 2: failure)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Count = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._Status = None

    @property
    def Id(self):
        """Unique ID of slow query log file
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        """File generation start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """File generation end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        """File size in KB
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Count(self):
        """Number of logs in file
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def InternalAddr(self):
        """Download address for private network
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        """Download address for public network
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Status(self):
        """Status (1: success, 2: failure)
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Count = params.get("Count")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowlogInfo(AbstractModel):
    """Slow query log file information

    """

    def __init__(self):
        r"""
        :param _Id: Unique ID of slow query log file
        :type Id: int
        :param _StartTime: File generation start time
        :type StartTime: str
        :param _EndTime: File generation end time
        :type EndTime: str
        :param _Size: File size in KB
        :type Size: int
        :param _Count: Number of logs in file
        :type Count: int
        :param _InternalAddr: Download address for private network
        :type InternalAddr: str
        :param _ExternalAddr: Download address for public network
        :type ExternalAddr: str
        :param _Status: Status (1: success, 2: failure)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Count = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._Status = None

    @property
    def Id(self):
        """Unique ID of slow query log file
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        """File generation start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """File generation end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        """File size in KB
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Count(self):
        """Number of logs in file
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def InternalAddr(self):
        """Download address for private network
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        """Download address for public network
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Status(self):
        """Status (1: success, 2: failure)
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Count = params.get("Count")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecInfo(AbstractModel):
    """Information of purchasable specification for an instance

    """

    def __init__(self):
        r"""
        :param _SpecId: Instance specification ID. The `SpecId` returned by `DescribeZones` together with the purchasable specification information returned by `DescribeProductConfig` can be used to find out what specifications can be purchased in a specified AZ
        :type SpecId: int
        :param _MachineType: Model ID
        :type MachineType: str
        :param _MachineTypeName: Model name
        :type MachineTypeName: str
        :param _Version: Database version information. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise)
        :type Version: str
        :param _VersionName: Version name corresponding to the `Version` field
        :type VersionName: str
        :param _Memory: Memory size in GB
        :type Memory: int
        :param _CPU: Number of CPU cores
        :type CPU: int
        :param _MinStorage: Minimum disk size under this specification in GB
        :type MinStorage: int
        :param _MaxStorage: Maximum disk size under this specification in GB
        :type MaxStorage: int
        :param _QPS: QPS of this specification
        :type QPS: int
        :param _SuitInfo: Description of this specification
        :type SuitInfo: str
        :param _Pid: Pid of this specification
        :type Pid: int
        :param _PostPid: Pay-as-you-go Pid list corresponding to this specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type PostPid: list of int
        :param _PayModeStatus: Billing mode under this specification. POST: pay-as-you-go
        :type PayModeStatus: str
        :param _InstanceType: Instance type. Valid values: HA (High-Availability Edition, including dual-server high availability and AlwaysOn cluster), RO (read-only replica), SI (Basic Edition)
        :type InstanceType: str
        :param _MultiZonesStatus: Whether multi-AZ deployment is supported. Valid values: MultiZones (only multi-AZ deployment is supported), SameZones (only single-AZ deployment is supported), ALL (both deployments are supported)
        :type MultiZonesStatus: str
        """
        self._SpecId = None
        self._MachineType = None
        self._MachineTypeName = None
        self._Version = None
        self._VersionName = None
        self._Memory = None
        self._CPU = None
        self._MinStorage = None
        self._MaxStorage = None
        self._QPS = None
        self._SuitInfo = None
        self._Pid = None
        self._PostPid = None
        self._PayModeStatus = None
        self._InstanceType = None
        self._MultiZonesStatus = None

    @property
    def SpecId(self):
        """Instance specification ID. The `SpecId` returned by `DescribeZones` together with the purchasable specification information returned by `DescribeProductConfig` can be used to find out what specifications can be purchased in a specified AZ
        :rtype: int
        """
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def MachineType(self):
        """Model ID
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineTypeName(self):
        """Model name
        :rtype: str
        """
        return self._MachineTypeName

    @MachineTypeName.setter
    def MachineTypeName(self, MachineTypeName):
        self._MachineTypeName = MachineTypeName

    @property
    def Version(self):
        """Database version information. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise)
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def VersionName(self):
        """Version name corresponding to the `Version` field
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Memory(self):
        """Memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def CPU(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def MinStorage(self):
        """Minimum disk size under this specification in GB
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def MaxStorage(self):
        """Maximum disk size under this specification in GB
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def QPS(self):
        """QPS of this specification
        :rtype: int
        """
        return self._QPS

    @QPS.setter
    def QPS(self, QPS):
        self._QPS = QPS

    @property
    def SuitInfo(self):
        """Description of this specification
        :rtype: str
        """
        return self._SuitInfo

    @SuitInfo.setter
    def SuitInfo(self, SuitInfo):
        self._SuitInfo = SuitInfo

    @property
    def Pid(self):
        """Pid of this specification
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def PostPid(self):
        """Pay-as-you-go Pid list corresponding to this specification
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._PostPid

    @PostPid.setter
    def PostPid(self, PostPid):
        self._PostPid = PostPid

    @property
    def PayModeStatus(self):
        """Billing mode under this specification. POST: pay-as-you-go
        :rtype: str
        """
        return self._PayModeStatus

    @PayModeStatus.setter
    def PayModeStatus(self, PayModeStatus):
        self._PayModeStatus = PayModeStatus

    @property
    def InstanceType(self):
        """Instance type. Valid values: HA (High-Availability Edition, including dual-server high availability and AlwaysOn cluster), RO (read-only replica), SI (Basic Edition)
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MultiZonesStatus(self):
        """Whether multi-AZ deployment is supported. Valid values: MultiZones (only multi-AZ deployment is supported), SameZones (only single-AZ deployment is supported), ALL (both deployments are supported)
        :rtype: str
        """
        return self._MultiZonesStatus

    @MultiZonesStatus.setter
    def MultiZonesStatus(self, MultiZonesStatus):
        self._MultiZonesStatus = MultiZonesStatus


    def _deserialize(self, params):
        self._SpecId = params.get("SpecId")
        self._MachineType = params.get("MachineType")
        self._MachineTypeName = params.get("MachineTypeName")
        self._Version = params.get("Version")
        self._VersionName = params.get("VersionName")
        self._Memory = params.get("Memory")
        self._CPU = params.get("CPU")
        self._MinStorage = params.get("MinStorage")
        self._MaxStorage = params.get("MaxStorage")
        self._QPS = params.get("QPS")
        self._SuitInfo = params.get("SuitInfo")
        self._Pid = params.get("Pid")
        self._PostPid = params.get("PostPid")
        self._PayModeStatus = params.get("PayModeStatus")
        self._InstanceType = params.get("InstanceType")
        self._MultiZonesStatus = params.get("MultiZonesStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBackupMigrationRequest(AbstractModel):
    """StartBackupMigration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBackupMigrationResponse(AbstractModel):
    """StartBackupMigration response structure.

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
        """Task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class StartIncrementalMigrationRequest(AbstractModel):
    """StartIncrementalMigration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of imported target instance
        :type InstanceId: str
        :param _BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param _IncrementalMigrationId: ID of an incremental backup import task
        :type IncrementalMigrationId: str
        """
        self._InstanceId = None
        self._BackupMigrationId = None
        self._IncrementalMigrationId = None

    @property
    def InstanceId(self):
        """ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        """Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        """ID of an incremental backup import task
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartIncrementalMigrationResponse(AbstractModel):
    """StartIncrementalMigration response structure.

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
        """Task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class StartInstanceXEventRequest(AbstractModel):
    """StartInstanceXEvent request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _EventConfig: Whether to start or stop an extended event
        :type EventConfig: list of EventConfig
        """
        self._InstanceId = None
        self._EventConfig = None

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
    def EventConfig(self):
        """Whether to start or stop an extended event
        :rtype: list of EventConfig
        """
        return self._EventConfig

    @EventConfig.setter
    def EventConfig(self, EventConfig):
        self._EventConfig = EventConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("EventConfig") is not None:
            self._EventConfig = []
            for item in params.get("EventConfig"):
                obj = EventConfig()
                obj._deserialize(item)
                self._EventConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstanceXEventResponse(AbstractModel):
    """StartInstanceXEvent response structure.

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


class TDEConfigAttribute(AbstractModel):
    """TDE configuration

    """

    def __init__(self):
        r"""
        :param _Encryption: TDE status. Valid values: `enable` (enabled), `disable` (disabled).
        :type Encryption: str
        :param _CertificateAttribution: Certificate ownership. Valid values: `self` (certificate of the this account), `others` (certificate of the other account), `none` (no certificate).
        :type CertificateAttribution: str
        :param _QuoteUin: Note: This field may return null, indicating that no valid values can be obtained.
        :type QuoteUin: str
        """
        self._Encryption = None
        self._CertificateAttribution = None
        self._QuoteUin = None

    @property
    def Encryption(self):
        """TDE status. Valid values: `enable` (enabled), `disable` (disabled).
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def CertificateAttribution(self):
        """Certificate ownership. Valid values: `self` (certificate of the this account), `others` (certificate of the other account), `none` (no certificate).
        :rtype: str
        """
        return self._CertificateAttribution

    @CertificateAttribution.setter
    def CertificateAttribution(self, CertificateAttribution):
        self._CertificateAttribution = CertificateAttribution

    @property
    def QuoteUin(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._QuoteUin

    @QuoteUin.setter
    def QuoteUin(self, QuoteUin):
        self._QuoteUin = QuoteUin


    def _deserialize(self, params):
        self._Encryption = params.get("Encryption")
        self._CertificateAttribution = params.get("CertificateAttribution")
        self._QuoteUin = params.get("QuoteUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDBInstanceRequest(AbstractModel):
    """TerminateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of instance IDs manually terminated in the format of [mssql-3l3fgqn7], which are the same as the instance IDs displayed on the TencentDB Console page
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        """List of instance IDs manually terminated in the format of [mssql-3l3fgqn7], which are the same as the instance IDs displayed on the TencentDB Console page
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance response structure.

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


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        :param _Memory: Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size
        :type Memory: int
        :param _Storage: Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity
        :type Storage: int
        :param _AutoVoucher: Whether to automatically use vouchers. 0: no, 1: yes. Default value: 0
        :type AutoVoucher: int
        :param _VoucherIds: Voucher ID (currently, only one voucher can be used per order)
        :type VoucherIds: list of str
        :param _Cpu: The number of CUP cores after the instance is upgraded.
        :type Cpu: int
        :param _DBVersion: Upgrade the SQL Server version. Supported versions include SQL Server 2008 Enterprise (`2008R2`), SQL Server 2012 Enterprise (`2012SP3`), etc. As the purchasable versions are region-specific, you can use the `DescribeProductConfig` API to query the information of purchasable versions in each region. Downgrading is unsupported. If this parameter is left empty, the SQL Server version will not be changed.
        :type DBVersion: str
        :param _HAType: Upgrade the high availability architecture from image-based disaster recovery to Always On cluster disaster recovery. This parameter is valid only for instances which support Always On high availability and run SQL Server 2017 or later. Neither downgrading to image-based disaster recovery nor upgrading from cluster disaster recovery to Always On disaster recovery is supported. If this parameter is left empty, the high availability architecture will not be changed.
        :type HAType: str
        :param _MultiZones: Change the instance deployment scheme. Valid values: `SameZones` (change to single-AZ deployment, which does not support cross-AZ disaster recovery), `MultiZones` (change to multi-AZ deployment, which supports cross-AZ disaster recovery).
        :type MultiZones: str
        :param _WaitSwitch: The time when configuration adjustment task is performed. Valid values: `0` (execute immediately), `1` (execute during maintenance time). Default value: `1`.
        :type WaitSwitch: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Storage = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._Cpu = None
        self._DBVersion = None
        self._HAType = None
        self._MultiZones = None
        self._WaitSwitch = None

    @property
    def InstanceId(self):
        """Instance ID in the format of mssql-j8kv137v
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        """Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def AutoVoucher(self):
        """Whether to automatically use vouchers. 0: no, 1: yes. Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """Voucher ID (currently, only one voucher can be used per order)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def Cpu(self):
        """The number of CUP cores after the instance is upgraded.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DBVersion(self):
        """Upgrade the SQL Server version. Supported versions include SQL Server 2008 Enterprise (`2008R2`), SQL Server 2012 Enterprise (`2012SP3`), etc. As the purchasable versions are region-specific, you can use the `DescribeProductConfig` API to query the information of purchasable versions in each region. Downgrading is unsupported. If this parameter is left empty, the SQL Server version will not be changed.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def HAType(self):
        """Upgrade the high availability architecture from image-based disaster recovery to Always On cluster disaster recovery. This parameter is valid only for instances which support Always On high availability and run SQL Server 2017 or later. Neither downgrading to image-based disaster recovery nor upgrading from cluster disaster recovery to Always On disaster recovery is supported. If this parameter is left empty, the high availability architecture will not be changed.
        :rtype: str
        """
        return self._HAType

    @HAType.setter
    def HAType(self, HAType):
        self._HAType = HAType

    @property
    def MultiZones(self):
        """Change the instance deployment scheme. Valid values: `SameZones` (change to single-AZ deployment, which does not support cross-AZ disaster recovery), `MultiZones` (change to multi-AZ deployment, which supports cross-AZ disaster recovery).
        :rtype: str
        """
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def WaitSwitch(self):
        """The time when configuration adjustment task is performed. Valid values: `0` (execute immediately), `1` (execute during maintenance time). Default value: `1`.
        :rtype: int
        """
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._Cpu = params.get("Cpu")
        self._DBVersion = params.get("DBVersion")
        self._HAType = params.get("HAType")
        self._MultiZones = params.get("MultiZones")
        self._WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance response structure.

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
        """Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ZoneInfo(AbstractModel):
    """AZ information

    """

    def __init__(self):
        r"""
        :param _Zone: AZ ID in the format of ap-guangzhou-1 (i.e., Guangzhou Zone 1)
        :type Zone: str
        :param _ZoneName: AZ name
        :type ZoneName: str
        :param _ZoneId: Numeric ID of AZ
        :type ZoneId: int
        :param _SpecId: ID of specification purchasable in this AZ, which, together with the returned value of the `DescribeProductConfig` API, can be used to find out the specifications currently purchasable in the AZ
        :type SpecId: int
        :param _Version: Information of database versions purchasable under the current AZ and specification. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise)
        :type Version: str
        """
        self._Zone = None
        self._ZoneName = None
        self._ZoneId = None
        self._SpecId = None
        self._Version = None

    @property
    def Zone(self):
        """AZ ID in the format of ap-guangzhou-1 (i.e., Guangzhou Zone 1)
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        """AZ name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        """Numeric ID of AZ
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SpecId(self):
        """ID of specification purchasable in this AZ, which, together with the returned value of the `DescribeProductConfig` API, can be used to find out the specifications currently purchasable in the AZ
        :rtype: int
        """
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def Version(self):
        """Information of database versions purchasable under the current AZ and specification. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise)
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._SpecId = params.get("SpecId")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        