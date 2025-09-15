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


class AccountCreateInfo(AbstractModel):
    r"""Account creation information

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
        :param _IsCam: Whether CAM authentication is enabled.
        :type IsCam: bool
        :param _EncryptedVersion: Encryption key version number. 0: disable encryption.
        :type EncryptedVersion: int
        """
        self._UserName = None
        self._Password = None
        self._DBPrivileges = None
        self._Remark = None
        self._IsAdmin = None
        self._Authentication = None
        self._AccountType = None
        self._IsCam = None
        self._EncryptedVersion = None

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
    def Password(self):
        r"""Instance password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DBPrivileges(self):
        r"""List of database permissions
        :rtype: list of DBPrivilege
        """
        return self._DBPrivileges

    @DBPrivileges.setter
    def DBPrivileges(self, DBPrivileges):
        self._DBPrivileges = DBPrivileges

    @property
    def Remark(self):
        r"""Account remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def IsAdmin(self):
        r"""Whether it is an admin account. Valid values: true (it is an admin account when the instance is a single-node type and AccountType is L0; when the instance is a two-node type and AccountType is L1), false (it is a standard account when AccountType is L3)
        :rtype: bool
        """
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def Authentication(self):
        r"""Valid values: `win-windows authentication`, `sql-sqlserver authentication`. Default value: `sql-sqlserver authentication`
        :rtype: str
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def AccountType(self):
        r"""Account type, which is an extension field of `IsAdmin`. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account, default)
        :rtype: str
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def IsCam(self):
        r"""Whether CAM authentication is enabled.
        :rtype: bool
        """
        return self._IsCam

    @IsCam.setter
    def IsCam(self, IsCam):
        self._IsCam = IsCam

    @property
    def EncryptedVersion(self):
        r"""Encryption key version number. 0: disable encryption.
        :rtype: int
        """
        return self._EncryptedVersion

    @EncryptedVersion.setter
    def EncryptedVersion(self, EncryptedVersion):
        self._EncryptedVersion = EncryptedVersion


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
        self._EncryptedVersion = params.get("EncryptedVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountDetail(AbstractModel):
    r"""Account information details

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
        r"""Account name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""Account remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        r"""Account creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        r"""Account status. 1: creating, 2: normal, 3: modifying, 4: resetting password, -1: deleting
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        r"""Account update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PassTime(self):
        r"""Password update time
        :rtype: str
        """
        return self._PassTime

    @PassTime.setter
    def PassTime(self, PassTime):
        self._PassTime = PassTime

    @property
    def InternalStatus(self):
        r"""Internal account status, which should be `enable` normally
        :rtype: str
        """
        return self._InternalStatus

    @InternalStatus.setter
    def InternalStatus(self, InternalStatus):
        self._InternalStatus = InternalStatus

    @property
    def Dbs(self):
        r"""Information of read and write permissions of this account on relevant databases
        :rtype: list of DBPrivilege
        """
        return self._Dbs

    @Dbs.setter
    def Dbs(self, Dbs):
        self._Dbs = Dbs

    @property
    def IsAdmin(self):
        r"""Whether it is an admin account
        :rtype: bool
        """
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def IsCam(self):
        r"""Whether it is a CAM managed account
        :rtype: bool
        """
        return self._IsCam

    @IsCam.setter
    def IsCam(self, IsCam):
        self._IsCam = IsCam

    @property
    def Authentication(self):
        r"""Valid values: `win-windows authentication`, `sql-sqlserver authentication`.
        :rtype: str
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Host(self):
        r"""The host required for `win-windows authentication` account
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def AccountType(self):
        r"""Account type. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account).
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
    r"""Instance account password information

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
        r"""Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""Password
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
    r"""Database account permission information, which is set when the database is created

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
        r"""Database username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Privilege(self):
        r"""Database permission. Valid values: `ReadWrite` (read-write), `ReadOnly` (read-only), `Delete` (delete the database permissions of this account), `DBOwner` (owner).
        :rtype: str
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def AccountType(self):
        r"""Account name. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account).
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
    r"""Database account permission change information

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
        r"""Database username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DBPrivileges(self):
        r"""Account permission change information
        :rtype: list of DBPrivilegeModifyInfo
        """
        return self._DBPrivileges

    @DBPrivileges.setter
    def DBPrivileges(self, DBPrivileges):
        self._DBPrivileges = DBPrivileges

    @property
    def IsAdmin(self):
        r"""Whether it is an instance admin account. Valid values: `true` (Yes. When the instance is single-node and `AccountType` is `L0`, it's an admin account; when the instance is two-node and `AccountType` is `L1`, it's a privileged account), `false` (No. It's a standard account and `AccountType` is `L3`).
        :rtype: bool
        """
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def AccountType(self):
        r"""Account type, which is an extension field of `IsAdmin`. Valid values: `L0` (admin account, only for basic edition), `L1` (privileged account), `L2` (designated account), `L3` (standard account, default)
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
    r"""Account remarks

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
        r"""Account name
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Remark(self):
        r"""New remarks of account
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
        


class AssociateSecurityGroupsRequest(AbstractModel):
    r"""AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group ID.
        :type SecurityGroupId: str
        :param _InstanceIdSet: Instance ID list, which is an array of one or more instance IDs. Multiple instances should be in the same region, AZ, and project.
        :type InstanceIdSet: list of str
        """
        self._SecurityGroupId = None
        self._InstanceIdSet = None

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
    def InstanceIdSet(self):
        r"""Instance ID list, which is an array of one or more instance IDs. Multiple instances should be in the same region, AZ, and project.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    r"""AssociateSecurityGroups response structure.

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


class Backup(AbstractModel):
    r"""Backup file details

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
        r"""File name. The name of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        r"""File size in KB. The size of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
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
    def EndTime(self):
        r"""Backup end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InternalAddr(self):
        r"""Private network download address. The download address of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        r"""Public network download address. The download address of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Id(self):
        r"""Unique ID of a backup file, which is used by the `RestoreInstance` API. The unique ID of an unarchived backup file is returned by the `DescribeBackupFiles` API instead of this parameter.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        r"""Backup file status (0: creating, 1: succeeded, 2: failed)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DBs(self):
        r"""List of databases for multi-database backup
        :rtype: list of str
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def Strategy(self):
        r"""Backup policy (0: instance backup, 1: multi-database backup)
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def BackupWay(self):
        r"""Backup Mode. Valid values: `0` (scheduled backup); `1` (manual backup); `2` (archive backup).
        :rtype: int
        """
        return self._BackupWay

    @BackupWay.setter
    def BackupWay(self, BackupWay):
        self._BackupWay = BackupWay

    @property
    def BackupName(self):
        r"""Backup task name (customizable)
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def GroupId(self):
        r"""Group ID of unarchived backup files, which can be used as a request parameter in the `DescribeBackupFiles` API to get details of unarchived backup files in the specified group. This parameter is invalid for archived backup files.
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def BackupFormat(self):
        r"""Backup file format. Valid values:`pkg` (archive file), `single` (unarchived files).
        :rtype: str
        """
        return self._BackupFormat

    @BackupFormat.setter
    def BackupFormat(self, BackupFormat):
        self._BackupFormat = BackupFormat

    @property
    def Region(self):
        r"""The code of current region where the instance resides
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CrossBackupAddr(self):
        r"""The download address of cross-region backup in target region
        :rtype: list of CrossBackupAddr
        """
        return self._CrossBackupAddr

    @CrossBackupAddr.setter
    def CrossBackupAddr(self, CrossBackupAddr):
        self._CrossBackupAddr = CrossBackupAddr

    @property
    def CrossBackupStatus(self):
        r"""The target region and status of cross-region backup
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
    r"""If the backup files are unarchived, each database corresponds to one backup file.

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
        r"""Unique ID of a backup file
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FileName(self):
        r"""Backup file name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

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
    def DBs(self):
        r"""Name of the database corresponding to the backup file
        :rtype: list of str
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def DownloadLink(self):
        r"""Download address
        :rtype: str
        """
        return self._DownloadLink

    @DownloadLink.setter
    def DownloadLink(self, DownloadLink):
        self._DownloadLink = DownloadLink

    @property
    def Region(self):
        r"""The code of the region where current instance resides
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CrossBackupAddr(self):
        r"""The target region and download address of cross-region backup
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
        


class BalanceReadOnlyGroupRequest(AbstractModel):
    r"""BalanceReadOnlyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Primary instance ID, in the format of mssql-3l3fgqn7.
        :type InstanceId: str
        :param _ReadOnlyGroupId: Read-only group ID, in the format of mssqlrg-dj5i29c5n.
        :type ReadOnlyGroupId: str
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def InstanceId(self):
        r"""Primary instance ID, in the format of mssql-3l3fgqn7.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""Read-only group ID, in the format of mssqlrg-dj5i29c5n.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceReadOnlyGroupResponse(AbstractModel):
    r"""BalanceReadOnlyGroup response structure.

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


class BusinessIntelligenceFile(AbstractModel):
    r"""Business intelligence service file type

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
        r"""File name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""File type
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileURL(self):
        r"""File COS_URL
        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def FilePath(self):
        r"""The file path on the server
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileSize(self):
        r"""File size in bytes
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileMd5(self):
        r"""File MD5 value
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def Status(self):
        r"""File deployment status. Valid values: `1`(Initialize to be deployed), `2` (Deploying), `3` (Deployment successful), `4` (Deployment failed).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        r"""File creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        r"""Start time of file deployment
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time of file deployment
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Message(self):
        r"""Returned error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceId(self):
        r"""Business intelligence instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Action(self):
        r"""Operation information
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
        


class CheckItem(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _CheckName: 
        :type CheckName: str
        :param _CurrentValue: 
        :type CurrentValue: str
        :param _Passed: 
        :type Passed: int
        :param _IsAffect: 
        :type IsAffect: int
        :param _Msg: 
        :type Msg: str
        :param _MsgCode: 
        :type MsgCode: int
        """
        self._CheckName = None
        self._CurrentValue = None
        self._Passed = None
        self._IsAffect = None
        self._Msg = None
        self._MsgCode = None

    @property
    def CheckName(self):
        r"""
        :rtype: str
        """
        return self._CheckName

    @CheckName.setter
    def CheckName(self, CheckName):
        self._CheckName = CheckName

    @property
    def CurrentValue(self):
        r"""
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Passed(self):
        r"""
        :rtype: int
        """
        return self._Passed

    @Passed.setter
    def Passed(self, Passed):
        self._Passed = Passed

    @property
    def IsAffect(self):
        r"""
        :rtype: int
        """
        return self._IsAffect

    @IsAffect.setter
    def IsAffect(self, IsAffect):
        self._IsAffect = IsAffect

    @property
    def Msg(self):
        r"""
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def MsgCode(self):
        r"""
        :rtype: int
        """
        return self._MsgCode

    @MsgCode.setter
    def MsgCode(self, MsgCode):
        self._MsgCode = MsgCode


    def _deserialize(self, params):
        self._CheckName = params.get("CheckName")
        self._CurrentValue = params.get("CurrentValue")
        self._Passed = params.get("Passed")
        self._IsAffect = params.get("IsAffect")
        self._Msg = params.get("Msg")
        self._MsgCode = params.get("MsgCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneDBRequest(AbstractModel):
    r"""CloneDB request structure.

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
        r"""Instance ID in the format of mssql-j8kv137v
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RenameRestore(self):
        r"""Clone and rename the databases specified in `ReNameRestoreDatabase`. Please note that the clones must be renamed.
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
    r"""CloneDB response structure.

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
        r"""Async task request ID, which can be used in the `DescribeFlowStatus` API to query the execution result of an async task
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


class CloseInterCommunicationRequest(AbstractModel):
    r"""CloseInterCommunication request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: IDs of instances with interconnection disabled
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        r"""IDs of instances with interconnection disabled
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
    r"""CloseInterCommunication response structure.

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
        r"""IDs of instance and async task
        :rtype: list of InterInstanceFlow
        """
        return self._InterInstanceFlowSet

    @InterInstanceFlowSet.setter
    def InterInstanceFlowSet(self, InterInstanceFlowSet):
        self._InterInstanceFlowSet = InterInstanceFlowSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CompleteExpansionRequest(AbstractModel):
    r"""CompleteExpansion request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-j8kv137v.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-j8kv137v.
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
        


class CompleteExpansionResponse(AbstractModel):
    r"""CompleteExpansion response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID, which can be used to query the status of the immediate switch upgrade task through the API DescribeFlowStatus.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Process ID, which can be used to query the status of the immediate switch upgrade task through the API DescribeFlowStatus.
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


class CompleteMigrationRequest(AbstractModel):
    r"""CompleteMigration request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID.
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        r"""Migration task ID.
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
        


class CompleteMigrationResponse(AbstractModel):
    r"""CompleteMigration response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID returned after the migration process is initiated.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Process ID returned after the migration process is initiated.
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


class CosUploadBackupFile(AbstractModel):
    r"""Querying the size of uploaded backup files.

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
        r"""Backup name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        r"""Backup size
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
    r"""CreateAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID in the format of mssql-njj2mtpl.
        :type InstanceId: str
        :param _Accounts: Database instance account information.
        :type Accounts: list of AccountCreateInfo
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        r"""Database instance ID in the format of mssql-njj2mtpl.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        r"""Database instance account information.
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
    r"""CreateAccount response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task flow ID.
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


class CreateBackupMigrationRequest(AbstractModel):
    r"""CreateBackupMigration request structure.

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
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RecoveryType(self):
        r"""Migration task restoration type. FULL: full backup restoration, FULL_LOG: full backup and transaction log restoration, FULL_DIFF: full backup and differential backup restoration
        :rtype: str
        """
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        r"""Backup upload type. COS_URL: the backup is stored in user's Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application's Cloud Object Storage and needs to be uploaded by the user.
        :rtype: str
        """
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def MigrationName(self):
        r"""Task name
        :rtype: str
        """
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def BackupFiles(self):
        r"""If the UploadType is COS_URL, fill in the URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
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
    r"""CreateBackupMigration response structure.

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
        r"""Backup import task ID
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""CreateBackup request structure.

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
        r"""Backup policy (0: instance backup, 1: multi-database backup)
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def DBNames(self):
        r"""List of names of databases to be backed up (required only for multi-database backup)
        :rtype: list of str
        """
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def InstanceId(self):
        r"""(Required) Instance ID in the format of mssql-i1z41iwd
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        r"""Backup name. If this parameter is left empty, a backup name in the format of "[Instance ID]_[Backup start timestamp]" will be automatically generated.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def StorageStrategy(self):
        r"""Backup storage policy. 0: Follow the custom backup retention policy; 1: Follow the instance lifecycle until the instance is eliminated. Default value: 0.
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
    r"""CreateBackup response structure.

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
        r"""The async job ID
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


class CreateBasicDBInstancesRequest(AbstractModel):
    r"""CreateBasicDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API.
        :type Zone: str
        :param _Cpu: Number of CPU cores.
        :type Cpu: int
        :param _Memory: Instance memory size in GB.
        :type Memory: int
        :param _Storage: Instance storage capacity in GB.
        :type Storage: int
        :param _SubnetId: VPC subnet ID in the format of subnet-bdoe83fa.
        :type SubnetId: str
        :param _VpcId: VPC ID in the format of vpc-dsp338hz.
        :type VpcId: str
        :param _MachineType: Host type of purchased instances. CLOUD_PREMIUM: Premium Disk for virtual machines; CLOUD_SSD: Cloud SSD for virtual machines; CLOUD_HSSD: Enhanced SSD for virtual machines; CLOUD_BSSD: Balanced SSD for virtual machines.
        :type MachineType: str
        :param _InstanceChargeType: Billing mode. Valid value: POSTPAID (pay-as-you-go).
        :type InstanceChargeType: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _GoodsNum: Number of instances purchased this time. Default value: 1. Maximum value: 10.
        :type GoodsNum: int
        :param _DBVersion: SQL Server version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The available version varies by region, and you can pull the version information by calling the `DescribeProductConfig` API.
        :type DBVersion: str
        :param _Period: Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48.
        :type Period: int
        :param _SecurityGroupList: Security group list, which contains security group IDs in the format of sg-xxx.
        :type SecurityGroupList: list of str
        :param _AutoRenewFlag: Auto-renewal flag. 0: normal renewal, 1: auto-renewal. Default value: 1.
        :type AutoRenewFlag: int
        :param _AutoVoucher: Whether to automatically use voucher. 0: no, 1: yes. Default value: no.
        :type AutoVoucher: int
        :param _VoucherIds: Array of voucher IDs (currently, only one voucher can be used per order).
        :type VoucherIds: list of str
        :param _Weekly: Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: 1 (Monday), 2 (Tuesday), 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday).
        :type Weekly: list of int
        :param _StartTime: Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :type StartTime: str
        :param _Span: Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :type Span: int
        :param _ResourceTags: Tags associated with the instances to be created.
        :type ResourceTags: list of ResourceTag
        :param _Collation: Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :type Collation: str
        :param _TimeZone: System time zone. Default value: `China Standard Time`.
        :type TimeZone: str
        :param _DiskEncryptFlag: Disk encryption identifier, 0-unencrypted, 1-encrypted.
        :type DiskEncryptFlag: int
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
        self._DiskEncryptFlag = None

    @property
    def Zone(self):
        r"""Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Cpu(self):
        r"""Number of CPU cores.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""Instance memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Instance storage capacity in GB.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def SubnetId(self):
        r"""VPC subnet ID in the format of subnet-bdoe83fa.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        r"""VPC ID in the format of vpc-dsp338hz.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def MachineType(self):
        r"""Host type of purchased instances. CLOUD_PREMIUM: Premium Disk for virtual machines; CLOUD_SSD: Cloud SSD for virtual machines; CLOUD_HSSD: Enhanced SSD for virtual machines; CLOUD_BSSD: Balanced SSD for virtual machines.
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def InstanceChargeType(self):
        r"""Billing mode. Valid value: POSTPAID (pay-as-you-go).
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

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
    def GoodsNum(self):
        r"""Number of instances purchased this time. Default value: 1. Maximum value: 10.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def DBVersion(self):
        r"""SQL Server version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The available version varies by region, and you can pull the version information by calling the `DescribeProductConfig` API.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def Period(self):
        r"""Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        r"""Security group list, which contains security group IDs in the format of sg-xxx.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoRenewFlag(self):
        r"""Auto-renewal flag. 0: normal renewal, 1: auto-renewal. Default value: 1.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use voucher. 0: no, 1: yes. Default value: no.
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Array of voucher IDs (currently, only one voucher can be used per order).
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def Weekly(self):
        r"""Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: 1 (Monday), 2 (Tuesday), 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday).
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        r"""Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        r"""Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def ResourceTags(self):
        r"""Tags associated with the instances to be created.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        r"""Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        r"""System time zone. Default value: `China Standard Time`.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def DiskEncryptFlag(self):
        r"""Disk encryption identifier, 0-unencrypted, 1-encrypted.
        :rtype: int
        """
        return self._DiskEncryptFlag

    @DiskEncryptFlag.setter
    def DiskEncryptFlag(self, DiskEncryptFlag):
        self._DiskEncryptFlag = DiskEncryptFlag


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
        self._DiskEncryptFlag = params.get("DiskEncryptFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDBInstancesResponse(AbstractModel):
    r"""CreateBasicDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order name.
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order name.
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


class CreateBusinessDBInstancesRequest(AbstractModel):
    r"""CreateBusinessDBInstances request structure.

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
        r"""Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def Storage(self):
        r"""Instance disk size in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        r"""The number of CPU cores of the instance you want to purchase.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def MachineType(self):
        r"""The host type of purchased instance. Valid values: `CLOUD_PREMIUM` (virtual machine with premium cloud disk), `CLOUD_SSD` (virtual machine with SSD).
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

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
    def GoodsNum(self):
        r"""Number of instances purchased this time. Default value: `1`.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        r"""VPC subnet ID in the format of subnet-bdoe83fa. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        r"""VPC ID in the format of vpc-dsp338hz. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DBVersion(self):
        r"""- Supported versions of business intelligence server. Valid values: `201603` (SQL Server 2016 Integration Services), `201703` (SQL Server 2017 Integration Services), `201903` (SQL Server 2019 Integration Services). Default value: `201903`. As the purchasable versions are region-specific, you can use the `DescribeProductConfig` API to query the information of purchasable versions in each region.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def SecurityGroupList(self):
        r"""Security group list, which contains security group IDs in the format of sg-xxx.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def Weekly(self):
        r"""Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: `1` (Monday), `2` (Tuesday), `3` (Wednesday), `4` (Thursday), `5` (Friday), `6` (Saturday), `7` (Sunday).
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        r"""Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        r"""Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def ResourceTags(self):
        r"""Tags associated with the instances to be created
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
    r"""CreateBusinessDBInstances response structure.

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
        r"""Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def FlowId(self):
        r"""Process ID Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceIdSet(self):
        r"""IDs of instances Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
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
        self._FlowId = params.get("FlowId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class CreateBusinessIntelligenceFileRequest(AbstractModel):
    r"""CreateBusinessIntelligenceFile request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileURL(self):
        r"""
        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def FileType(self):
        r"""File type. Valid values: `FLAT` (flat file as data source), `SSIS` (.ispac SSIS package file)
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Remark(self):
        r"""Remarks
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
    r"""CreateBusinessIntelligenceFile response structure.

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
        r"""File name
        :rtype: str
        """
        return self._FileTaskId

    @FileTaskId.setter
    def FileTaskId(self, FileTaskId):
        self._FileTaskId = FileTaskId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""CreateCloudDBInstances request structure.

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
        r"""Instance AZ, such as `ap-guangzhou-1` (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def Storage(self):
        r"""Instance disk size in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

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
    def MachineType(self):
        r"""The host type of the purchased instance. Valid values: `CLOUD_HSSD` (virtual machine with enhanced SSD), `CLOUD_TSSD` (virtual machine with ulTra SSD), `CLOUD_BSSD` (virtual machine with balanced SSD).
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def InstanceChargeType(self):
        r"""Billing mode. Valid values: `PREPAID` (monthly subscription), `POSTPAID` (pay-as-you-go).
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

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
    def GoodsNum(self):
        r"""Number of instances purchased this time. Default value: `1`.  Maximum value: `10`.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        r"""VPC subnet ID in the format of `subnet-bdoe83fa`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        r"""VPC ID in the format of `vpc-dsp338hz`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        r"""The purchase period of an instance. Default value: `1` (one month).  Maximum value: `48`.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use voucher. Valid values: `0` (no, default), `1` (yes).
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Array of voucher IDs (currently, only one voucher can be used per order)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def DBVersion(self):
        r"""SQL Server version. Valid values:  `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard).  Default value: `2008R2`.  The available version varies by region, and you can pull the version information through the `DescribeProductConfig` API.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def AutoRenewFlag(self):
        r"""Auto-renewal flag, which takes effect only when purchasing a monthly subscribed instance.  Valid values:  `0` (auto-renewal disabled), `1` (auto-renewal enabled). Default value: `0`.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SecurityGroupList(self):
        r"""Security group list, which contains security group IDs in the format of `sg-xxx`.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def Weekly(self):
        r"""Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: `1` (Monday), `2` (Tuesday), `3` (Wednesday), `4` (Thursday), `5` (Friday), `6` (Saturday), `7` (Sunday).
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        r"""Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        r"""Configuration of the maintenance window, which specifies the maintenance duration in hours. Hour
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def MultiZones(self):
        r"""Whether to deploy across AZs. Default value: `false`.
        :rtype: bool
        """
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def ResourceTags(self):
        r"""Tags associated with the instances to be created
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        r"""Collation of system character sets. Default value:  `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        r"""System time zone. Default value:  `China Standard Time`.
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
    r"""CreateCloudDBInstances response structure.

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


class CreateCloudReadOnlyDBInstancesRequest(AbstractModel):
    r"""CreateCloudReadOnlyDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of  `mssql-3l3fgqn7`.
        :type InstanceId: str
        :param _Zone: Instance AZ, such as `ap-guangzhou-1` (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :type Zone: str
        :param _ReadOnlyGroupType: Read-only group types. Valid values: `1` (each read-only replica is placed in one auto-created read-only group), `2` (all read-only replicas are placed in one auto-created read-only group), `3` (all read-only replicas are placed in one existing read-only group).
        :type ReadOnlyGroupType: int
        :param _Memory: Instance memory size in GB.
        :type Memory: int
        :param _Storage: Instance disk size in GB.
        :type Storage: int
        :param _Cpu: Number of instance cores.
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
        :param _VoucherIds: Array of voucher IDs (currently, only one voucher can be used per order).
        :type VoucherIds: list of str
        :param _ResourceTags: Tags associated with the instances to be created.
        :type ResourceTags: list of ResourceTag
        :param _Collation: Collation of system character sets. Default value:  Chinese_PRC_CI_AS.
        :type Collation: str
        :param _TimeZone: System time zone. Default value:  `China Standard Time`.
        :type TimeZone: str
        :param _DiskEncryptFlag: Disk encryption identification, 0 - no encryption, 1 - encryption.
        :type DiskEncryptFlag: int
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
        self._DiskEncryptFlag = None

    @property
    def InstanceId(self):
        r"""Instance ID in the format of  `mssql-3l3fgqn7`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        r"""Instance AZ, such as `ap-guangzhou-1` (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ReadOnlyGroupType(self):
        r"""Read-only group types. Valid values: `1` (each read-only replica is placed in one auto-created read-only group), `2` (all read-only replicas are placed in one auto-created read-only group), `3` (all read-only replicas are placed in one existing read-only group).
        :rtype: int
        """
        return self._ReadOnlyGroupType

    @ReadOnlyGroupType.setter
    def ReadOnlyGroupType(self, ReadOnlyGroupType):
        self._ReadOnlyGroupType = ReadOnlyGroupType

    @property
    def Memory(self):
        r"""Instance memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Instance disk size in GB.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        r"""Number of instance cores.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def MachineType(self):
        r"""The host type of purchased instance. Valid values: `CLOUD_HSSD` (virtual machine with enhanced SSD), `CLOUD_TSSD` (virtual machine with ulTra SSD), `CLOUD_BSSD` (virtual machine with balanced SSD).
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def ReadOnlyGroupForcedUpgrade(self):
        r"""Valid values: `0` (not upgrade the primary instance by default), `1` (upgrade the primary instance to complete the RO deployment).  You need to pass in `1` for this parameter and upgrade the primary instance to cluster edition.
        :rtype: int
        """
        return self._ReadOnlyGroupForcedUpgrade

    @ReadOnlyGroupForcedUpgrade.setter
    def ReadOnlyGroupForcedUpgrade(self, ReadOnlyGroupForcedUpgrade):
        self._ReadOnlyGroupForcedUpgrade = ReadOnlyGroupForcedUpgrade

    @property
    def ReadOnlyGroupId(self):
        r"""Existing read-only group ID, which is required when `ReadOnlyGroupType` is `3`.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""New read-only group ID, which is required when `ReadOnlyGroupType` is `2`.
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ReadOnlyGroupIsOfflineDelay(self):
        r"""Whether delayed read-only instance removal is enabled in a new read-only group, which is required when `ReadOnlyGroupType` is `2`. Valid values: `1` (enabled), `0` (disabled).  The read-only replica will be automatically removed when the delay between it and the primary instance exceeds the threshold.
        :rtype: int
        """
        return self._ReadOnlyGroupIsOfflineDelay

    @ReadOnlyGroupIsOfflineDelay.setter
    def ReadOnlyGroupIsOfflineDelay(self, ReadOnlyGroupIsOfflineDelay):
        self._ReadOnlyGroupIsOfflineDelay = ReadOnlyGroupIsOfflineDelay

    @property
    def ReadOnlyGroupMaxDelayTime(self):
        r"""The delay threshold for a new read-only group, which is required when `ReadOnlyGroupType` is `2` and `ReadOnlyGroupIsOfflineDelay` is `1`.
        :rtype: int
        """
        return self._ReadOnlyGroupMaxDelayTime

    @ReadOnlyGroupMaxDelayTime.setter
    def ReadOnlyGroupMaxDelayTime(self, ReadOnlyGroupMaxDelayTime):
        self._ReadOnlyGroupMaxDelayTime = ReadOnlyGroupMaxDelayTime

    @property
    def ReadOnlyGroupMinInGroup(self):
        r"""Minimum number of reserved read-only replicas when the delayed removal is enabled for the new read-only group, which is required when `ReadOnlyGroupType` is `2` and `ReadOnlyGroupIsOfflineDelay` is `1`.
        :rtype: int
        """
        return self._ReadOnlyGroupMinInGroup

    @ReadOnlyGroupMinInGroup.setter
    def ReadOnlyGroupMinInGroup(self, ReadOnlyGroupMinInGroup):
        self._ReadOnlyGroupMinInGroup = ReadOnlyGroupMinInGroup

    @property
    def InstanceChargeType(self):
        r"""Billing mode. Valid values: `PREPAID` (monthly subscription), `POSTPAID` (pay-as-you-go).
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def GoodsNum(self):
        r"""Number of read-only instances to be purchased this time. Default value: `2`.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        r"""VPC subnet ID in the format of `subnet-bdoe83fa`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        r"""VPC ID in the format of `vpc-dsp338hz`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        r"""The purchase period of an instance. Default value: `1` (one month).  Maximum value: `48`.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        r"""Security group list, which contains security group IDs in the format of `sg-xxx`.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use voucher. Valid values: `0` (no, default), `1` (yes).
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Array of voucher IDs (currently, only one voucher can be used per order).
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ResourceTags(self):
        r"""Tags associated with the instances to be created.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        r"""Collation of system character sets. Default value:  Chinese_PRC_CI_AS.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        r"""System time zone. Default value:  `China Standard Time`.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def DiskEncryptFlag(self):
        r"""Disk encryption identification, 0 - no encryption, 1 - encryption.
        :rtype: int
        """
        return self._DiskEncryptFlag

    @DiskEncryptFlag.setter
    def DiskEncryptFlag(self, DiskEncryptFlag):
        self._DiskEncryptFlag = DiskEncryptFlag


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
        self._DiskEncryptFlag = params.get("DiskEncryptFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudReadOnlyDBInstancesResponse(AbstractModel):
    r"""CreateCloudReadOnlyDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order name in array.
        :type DealNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealNames = None
        self._RequestId = None

    @property
    def DealNames(self):
        r"""Order name in array.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
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
        self._RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    r"""CreateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API.
        :type Zone: str
        :param _Memory: Instance memory size in GB.
        :type Memory: int
        :param _Storage: Instance storage capacity in GB.
        :type Storage: int
        :param _InstanceChargeType: Billing mode. Valid value: POSTPAID (pay-as-you-go).
        :type InstanceChargeType: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _GoodsNum: Number of instances purchased this time. Default value: 1. Maximum value: 10.
        :type GoodsNum: int
        :param _SubnetId: VPC subnet ID in the format of subnet-bdoe83fa. `SubnetId` and `VpcId` should be set or ignored simultaneously.
        :type SubnetId: str
        :param _VpcId: VPC ID in the format of vpc-dsp338hz. `SubnetId` and `VpcId` should be set or ignored simultaneously.
        :type VpcId: str
        :param _Period: Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48.
        :type Period: int
        :param _AutoVoucher: Whether to automatically use voucher. 0: no, 1: yes. Default value: no.
        :type AutoVoucher: int
        :param _VoucherIds: Array of voucher IDs (currently, only one voucher can be used per order).
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
        :param _ResourceTags: Tags associated with the instances to be created.
        :type ResourceTags: list of ResourceTag
        :param _Collation: Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :type Collation: str
        :param _TimeZone: System time zone. Default value: `China Standard Time`.
        :type TimeZone: str
        :param _MultiNodes: Whether it is a multi-node architecture instance. Default value: `false`.If MultiNodes = true, the value of the MultiZones parameter must be true.
        :type MultiNodes: bool
        :param _DrZones: The zone in which the standby node is available. Default is empty. When MultiNodes = true, the availability zones of the primary and standby nodes cannot all be the same. The minimum number of availability zones for the standby nodes is 2, and the maximum is 5.
        :type DrZones: list of str
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
        self._MultiNodes = None
        self._DrZones = None

    @property
    def Zone(self):
        r"""Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        r"""Instance memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Instance storage capacity in GB.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceChargeType(self):
        r"""Billing mode. Valid value: POSTPAID (pay-as-you-go).
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

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
    def GoodsNum(self):
        r"""Number of instances purchased this time. Default value: 1. Maximum value: 10.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        r"""VPC subnet ID in the format of subnet-bdoe83fa. `SubnetId` and `VpcId` should be set or ignored simultaneously.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        r"""VPC ID in the format of vpc-dsp338hz. `SubnetId` and `VpcId` should be set or ignored simultaneously.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        r"""Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use voucher. 0: no, 1: yes. Default value: no.
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Array of voucher IDs (currently, only one voucher can be used per order).
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def DBVersion(self):
        r"""SQL Server version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The available version varies by region, and you can pull the version information by calling the `DescribeProductConfig` API.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def AutoRenewFlag(self):
        r"""Auto-renewal flag. 0: normal renewal, 1: auto-renewal. Default value: 1.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SecurityGroupList(self):
        r"""Security group list, which contains security group IDs in the format of sg-xxx.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def Weekly(self):
        r"""Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: 1 (Monday), 2 (Tuesday), 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday).
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        r"""Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        r"""Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def HAType(self):
        r"""The type of purchased high-availability instance. Valid values: DUAL (dual-server high availability), CLUSTER (cluster). Default value: DUAL.
        :rtype: str
        """
        return self._HAType

    @HAType.setter
    def HAType(self, HAType):
        self._HAType = HAType

    @property
    def MultiZones(self):
        r"""Whether to deploy across availability zones. Default value: false.
        :rtype: bool
        """
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def ResourceTags(self):
        r"""Tags associated with the instances to be created.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        r"""Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        r"""System time zone. Default value: `China Standard Time`.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def MultiNodes(self):
        r"""Whether it is a multi-node architecture instance. Default value: `false`.If MultiNodes = true, the value of the MultiZones parameter must be true.
        :rtype: bool
        """
        return self._MultiNodes

    @MultiNodes.setter
    def MultiNodes(self, MultiNodes):
        self._MultiNodes = MultiNodes

    @property
    def DrZones(self):
        r"""The zone in which the standby node is available. Default is empty. When MultiNodes = true, the availability zones of the primary and standby nodes cannot all be the same. The minimum number of availability zones for the standby nodes is 2, and the maximum is 5.
        :rtype: list of str
        """
        return self._DrZones

    @DrZones.setter
    def DrZones(self, DrZones):
        self._DrZones = DrZones


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
        self._MultiNodes = params.get("MultiNodes")
        self._DrZones = params.get("DrZones")
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
        :param _DealName: Order name.
        :type DealName: str
        :param _DealNames: Order name array.
        :type DealNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._DealNames = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order name.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def DealNames(self):
        r"""Order name array.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
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
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CreateDBRequest(AbstractModel):
    r"""CreateDB request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBs(self):
        r"""Database creation information
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
    r"""CreateDB response structure.

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
        r"""Task flow ID
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


class CreateIncrementalMigrationRequest(AbstractModel):
    r"""CreateIncrementalMigration request structure.

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
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the API CreateBackupMigration.
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def BackupFiles(self):
        r"""Incremental backup file. If the UploadType of a full backup file is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :rtype: list of str
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def IsRecovery(self):
        r"""Whether restoration is required. No: not required. Yes: required. Not required by default.
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
    r"""CreateIncrementalMigration response structure.

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
        r"""ID of an incremental backup import task
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""CreateMigration request structure.

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
        r"""Migration task name
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def MigrateType(self):
        r"""Migration type (1: structure migration, 2: data migration, 3: incremental sync)
        :rtype: int
        """
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def SourceType(self):
        r"""Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Source(self):
        r"""Migration source
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""Migration target
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def MigrateDBSet(self):
        r"""Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5)
        :rtype: list of MigrateDB
        """
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet

    @property
    def RenameRestore(self):
        r"""Restore and rename the databases listed in `ReNameRestoreDatabase`. If this parameter is left empty, all restored databases will be renamed in the default format. This parameter takes effect only when `SourceType=5`.
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
    r"""CreateMigration response structure.

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
        r"""Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        self._RequestId = params.get("RequestId")


class CreatePublishSubscribeRequest(AbstractModel):
    r"""CreatePublishSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _PublishInstanceId: Publishing instance ID. For example, mssql-j8kv137v.
        :type PublishInstanceId: str
        :param _SubscribeInstanceId: Subscription instance ID. For example, mssql-j8kv137v.
        :type SubscribeInstanceId: str
        :param _DatabaseTupleSet: Publish/subscribe relationship collection of the database.
        :type DatabaseTupleSet: list of DatabaseTuple
        :param _PublishSubscribeName: Publish/subscribe name. The default value is default_name.
        :type PublishSubscribeName: str
        """
        self._PublishInstanceId = None
        self._SubscribeInstanceId = None
        self._DatabaseTupleSet = None
        self._PublishSubscribeName = None

    @property
    def PublishInstanceId(self):
        r"""Publishing instance ID. For example, mssql-j8kv137v.
        :rtype: str
        """
        return self._PublishInstanceId

    @PublishInstanceId.setter
    def PublishInstanceId(self, PublishInstanceId):
        self._PublishInstanceId = PublishInstanceId

    @property
    def SubscribeInstanceId(self):
        r"""Subscription instance ID. For example, mssql-j8kv137v.
        :rtype: str
        """
        return self._SubscribeInstanceId

    @SubscribeInstanceId.setter
    def SubscribeInstanceId(self, SubscribeInstanceId):
        self._SubscribeInstanceId = SubscribeInstanceId

    @property
    def DatabaseTupleSet(self):
        r"""Publish/subscribe relationship collection of the database.
        :rtype: list of DatabaseTuple
        """
        return self._DatabaseTupleSet

    @DatabaseTupleSet.setter
    def DatabaseTupleSet(self, DatabaseTupleSet):
        self._DatabaseTupleSet = DatabaseTupleSet

    @property
    def PublishSubscribeName(self):
        r"""Publish/subscribe name. The default value is default_name.
        :rtype: str
        """
        return self._PublishSubscribeName

    @PublishSubscribeName.setter
    def PublishSubscribeName(self, PublishSubscribeName):
        self._PublishSubscribeName = PublishSubscribeName


    def _deserialize(self, params):
        self._PublishInstanceId = params.get("PublishInstanceId")
        self._SubscribeInstanceId = params.get("SubscribeInstanceId")
        if params.get("DatabaseTupleSet") is not None:
            self._DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = DatabaseTuple()
                obj._deserialize(item)
                self._DatabaseTupleSet.append(obj)
        self._PublishSubscribeName = params.get("PublishSubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePublishSubscribeResponse(AbstractModel):
    r"""CreatePublishSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID. The DescribeFlowStatus API can be used to query the status of the immediate switch upgrade task.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Process ID. The DescribeFlowStatus API can be used to query the status of the immediate switch upgrade task.
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


class CreateReadOnlyDBInstancesRequest(AbstractModel):
    r"""CreateReadOnlyDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of  `mssql-3l3fgqn7`.
        :type InstanceId: str
        :param _Zone: Instance AZ, such as `ap-guangzhou-1` (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :type Zone: str
        :param _ReadOnlyGroupType: Read-only group types. Valid values: `1` (each read-only replica is placed in one auto-created read-only group), `2` (all read-only replicas are placed in one auto-created read-only group), `3` (all read-only replicas are placed in one existing read-only group).
        :type ReadOnlyGroupType: int
        :param _Memory: Instance memory size in GB.
        :type Memory: int
        :param _Storage: Instance disk size in GB.
        :type Storage: int
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
        :param _VoucherIds: Array of voucher IDs (currently, only one voucher can be used per order).
        :type VoucherIds: list of str
        :param _ResourceTags: Tags associated with the instances to be created.
        :type ResourceTags: list of ResourceTag
        :param _Collation: Collation of system character sets. Default value:  Chinese_PRC_CI_AS.
        :type Collation: str
        :param _TimeZone: System time zone. Default value:  `China Standard Time`.
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
        r"""Instance ID in the format of  `mssql-3l3fgqn7`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        r"""Instance AZ, such as `ap-guangzhou-1` (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the`DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ReadOnlyGroupType(self):
        r"""Read-only group types. Valid values: `1` (each read-only replica is placed in one auto-created read-only group), `2` (all read-only replicas are placed in one auto-created read-only group), `3` (all read-only replicas are placed in one existing read-only group).
        :rtype: int
        """
        return self._ReadOnlyGroupType

    @ReadOnlyGroupType.setter
    def ReadOnlyGroupType(self, ReadOnlyGroupType):
        self._ReadOnlyGroupType = ReadOnlyGroupType

    @property
    def Memory(self):
        r"""Instance memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Instance disk size in GB.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ReadOnlyGroupForcedUpgrade(self):
        r"""Valid values: `0` (not upgrade the primary instance by default), `1` (upgrade the primary instance to complete the RO deployment).  You need to pass in `1` for this parameter and upgrade the primary instance to cluster edition.
        :rtype: int
        """
        return self._ReadOnlyGroupForcedUpgrade

    @ReadOnlyGroupForcedUpgrade.setter
    def ReadOnlyGroupForcedUpgrade(self, ReadOnlyGroupForcedUpgrade):
        self._ReadOnlyGroupForcedUpgrade = ReadOnlyGroupForcedUpgrade

    @property
    def ReadOnlyGroupId(self):
        r"""Existing read-only group ID, which is required when `ReadOnlyGroupType` is `3`.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""New read-only group ID, which is required when `ReadOnlyGroupType` is `2`.
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def ReadOnlyGroupIsOfflineDelay(self):
        r"""Whether delayed read-only instance removal is enabled in a new read-only group, which is required when `ReadOnlyGroupType` is `2`. Valid values: `1` (enabled), `0` (disabled).  The read-only replica will be automatically removed when the delay between it and the primary instance exceeds the threshold.
        :rtype: int
        """
        return self._ReadOnlyGroupIsOfflineDelay

    @ReadOnlyGroupIsOfflineDelay.setter
    def ReadOnlyGroupIsOfflineDelay(self, ReadOnlyGroupIsOfflineDelay):
        self._ReadOnlyGroupIsOfflineDelay = ReadOnlyGroupIsOfflineDelay

    @property
    def ReadOnlyGroupMaxDelayTime(self):
        r"""The delay threshold for a new read-only group, which is required when `ReadOnlyGroupType` is `2` and `ReadOnlyGroupIsOfflineDelay` is `1`.
        :rtype: int
        """
        return self._ReadOnlyGroupMaxDelayTime

    @ReadOnlyGroupMaxDelayTime.setter
    def ReadOnlyGroupMaxDelayTime(self, ReadOnlyGroupMaxDelayTime):
        self._ReadOnlyGroupMaxDelayTime = ReadOnlyGroupMaxDelayTime

    @property
    def ReadOnlyGroupMinInGroup(self):
        r"""Minimum number of reserved read-only replicas when the delayed removal is enabled for the new read-only group, which is required when `ReadOnlyGroupType` is `2` and `ReadOnlyGroupIsOfflineDelay` is `1`.
        :rtype: int
        """
        return self._ReadOnlyGroupMinInGroup

    @ReadOnlyGroupMinInGroup.setter
    def ReadOnlyGroupMinInGroup(self, ReadOnlyGroupMinInGroup):
        self._ReadOnlyGroupMinInGroup = ReadOnlyGroupMinInGroup

    @property
    def InstanceChargeType(self):
        r"""Billing mode. Valid values: `PREPAID` (monthly subscription), `POSTPAID` (pay-as-you-go).
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def GoodsNum(self):
        r"""Number of read-only instances to be purchased this time. Default value: `2`.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SubnetId(self):
        r"""VPC subnet ID in the format of `subnet-bdoe83fa`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        r"""VPC ID in the format of `vpc-dsp338hz`. Both `SubnetId` and `VpcId` need to be set or unset at the same time.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        r"""The purchase period of an instance. Default value: `1` (one month).  Maximum value: `48`.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        r"""Security group list, which contains security group IDs in the format of `sg-xxx`.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use voucher. Valid values: `0` (no, default), `1` (yes).
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Array of voucher IDs (currently, only one voucher can be used per order).
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def ResourceTags(self):
        r"""Tags associated with the instances to be created.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Collation(self):
        r"""Collation of system character sets. Default value:  Chinese_PRC_CI_AS.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        r"""System time zone. Default value:  `China Standard Time`.
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
    r"""CreateReadOnlyDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order name in array.
        :type DealNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealNames = None
        self._RequestId = None

    @property
    def DealNames(self):
        r"""Order name in array.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
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
        self._RequestId = params.get("RequestId")


class CrossBackupAddr(AbstractModel):
    r"""All Download addresses of cross-region backup

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
        r"""The target region of cross-region backup
        :rtype: str
        """
        return self._CrossRegion

    @CrossRegion.setter
    def CrossRegion(self, CrossRegion):
        self._CrossRegion = CrossRegion

    @property
    def CrossInternalAddr(self):
        r"""The address used to download the cross-region backup over a private network
        :rtype: str
        """
        return self._CrossInternalAddr

    @CrossInternalAddr.setter
    def CrossInternalAddr(self, CrossInternalAddr):
        self._CrossInternalAddr = CrossInternalAddr

    @property
    def CrossExternalAddr(self):
        r"""The address used to download the cross-region backup over a public network
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
    r"""The target region and status of cross-region backup

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
        r"""The target region of cross-region backup
        :rtype: str
        """
        return self._CrossRegion

    @CrossRegion.setter
    def CrossRegion(self, CrossRegion):
        self._CrossRegion = CrossRegion

    @property
    def CrossStatus(self):
        r"""Synchronization status of cross-region backup. Valid values: `0` (creating), `1` (succeeded), `2`: (failed), `4` (syncing)
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
        


class CrossSummaryDetailRes(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Status: 
        :type Status: int
        :param _Region: 
        :type Region: str
        :param _InstanceId: 
        :type InstanceId: str
        :param _Name: 
        :type Name: str
        :param _CrossBackupEnabled: 
        :type CrossBackupEnabled: str
        :param _CrossRegions: 
        :type CrossRegions: list of str
        :param _LastBackupStartTime: 
        :type LastBackupStartTime: str
        :param _CrossBackupSaveDays: 
        :type CrossBackupSaveDays: int
        :param _DataBackupSpace: 
        :type DataBackupSpace: int
        :param _DataBackupCount: 
        :type DataBackupCount: int
        :param _LogBackupSpace: 
        :type LogBackupSpace: int
        :param _LogBackupCount: 
        :type LogBackupCount: int
        :param _ActualUsedSpace: 
        :type ActualUsedSpace: int
        :param _ActualUsedCount: 
        :type ActualUsedCount: int
        """
        self._Status = None
        self._Region = None
        self._InstanceId = None
        self._Name = None
        self._CrossBackupEnabled = None
        self._CrossRegions = None
        self._LastBackupStartTime = None
        self._CrossBackupSaveDays = None
        self._DataBackupSpace = None
        self._DataBackupCount = None
        self._LogBackupSpace = None
        self._LogBackupCount = None
        self._ActualUsedSpace = None
        self._ActualUsedCount = None

    @property
    def Status(self):
        r"""
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        r"""
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CrossBackupEnabled(self):
        r"""
        :rtype: str
        """
        return self._CrossBackupEnabled

    @CrossBackupEnabled.setter
    def CrossBackupEnabled(self, CrossBackupEnabled):
        self._CrossBackupEnabled = CrossBackupEnabled

    @property
    def CrossRegions(self):
        r"""
        :rtype: list of str
        """
        return self._CrossRegions

    @CrossRegions.setter
    def CrossRegions(self, CrossRegions):
        self._CrossRegions = CrossRegions

    @property
    def LastBackupStartTime(self):
        r"""
        :rtype: str
        """
        return self._LastBackupStartTime

    @LastBackupStartTime.setter
    def LastBackupStartTime(self, LastBackupStartTime):
        self._LastBackupStartTime = LastBackupStartTime

    @property
    def CrossBackupSaveDays(self):
        r"""
        :rtype: int
        """
        return self._CrossBackupSaveDays

    @CrossBackupSaveDays.setter
    def CrossBackupSaveDays(self, CrossBackupSaveDays):
        self._CrossBackupSaveDays = CrossBackupSaveDays

    @property
    def DataBackupSpace(self):
        r"""
        :rtype: int
        """
        return self._DataBackupSpace

    @DataBackupSpace.setter
    def DataBackupSpace(self, DataBackupSpace):
        self._DataBackupSpace = DataBackupSpace

    @property
    def DataBackupCount(self):
        r"""
        :rtype: int
        """
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def LogBackupSpace(self):
        r"""
        :rtype: int
        """
        return self._LogBackupSpace

    @LogBackupSpace.setter
    def LogBackupSpace(self, LogBackupSpace):
        self._LogBackupSpace = LogBackupSpace

    @property
    def LogBackupCount(self):
        r"""
        :rtype: int
        """
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def ActualUsedSpace(self):
        r"""
        :rtype: int
        """
        return self._ActualUsedSpace

    @ActualUsedSpace.setter
    def ActualUsedSpace(self, ActualUsedSpace):
        self._ActualUsedSpace = ActualUsedSpace

    @property
    def ActualUsedCount(self):
        r"""
        :rtype: int
        """
        return self._ActualUsedCount

    @ActualUsedCount.setter
    def ActualUsedCount(self, ActualUsedCount):
        self._ActualUsedCount = ActualUsedCount


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._CrossBackupEnabled = params.get("CrossBackupEnabled")
        self._CrossRegions = params.get("CrossRegions")
        self._LastBackupStartTime = params.get("LastBackupStartTime")
        self._CrossBackupSaveDays = params.get("CrossBackupSaveDays")
        self._DataBackupSpace = params.get("DataBackupSpace")
        self._DataBackupCount = params.get("DataBackupCount")
        self._LogBackupSpace = params.get("LogBackupSpace")
        self._LogBackupCount = params.get("LogBackupCount")
        self._ActualUsedSpace = params.get("ActualUsedSpace")
        self._ActualUsedCount = params.get("ActualUsedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CutXEventsRequest(AbstractModel):
    r"""CutXEvents request structure.

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
        


class CutXEventsResponse(AbstractModel):
    r"""CutXEvents response structure.

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


class DBCreateInfo(AbstractModel):
    r"""Database creation information

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
        r"""Database name
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Charset(self):
        r"""Character set, which can be queried by the `DescribeDBCharsets` API. Default value: `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def Accounts(self):
        r"""Database account permission information
        :rtype: list of AccountPrivilege
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def Remark(self):
        r"""Remarks
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
    r"""Database information

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
        r"""Database name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Charset(self):
        r"""Character set
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        r"""Database creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        r"""Database status. 1: creating, 2: running, 3: modifying, -1: dropping
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Accounts(self):
        r"""Database account permission information
        :rtype: list of AccountPrivilege
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def InternalStatus(self):
        r"""Internal status. ONLINE: running
        :rtype: str
        """
        return self._InternalStatus

    @InternalStatus.setter
    def InternalStatus(self, InternalStatus):
        self._InternalStatus = InternalStatus

    @property
    def Encryption(self):
        r"""TDE status. Valid values: `enable` (enabled), `disable` (disabled).
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
    r"""Instance details

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
        :param _Model: Instance disaster recovery type. 1: dual-server high availability; 2: single-node; 3: cross-AZ; 4: cross-AZ cluster; 5: cluster; 6: multi-node cluster; 7: multi-node cross-AZ cluster.
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
        :param _IsolateOperator: Instance isolation operation.
        :type IsolateOperator: str
        :param _SubFlag: Publishing/Subscription flag. SUB: subscription instance; PUB: publishing instance. If this parameter is left blank, the instance is an ordinary instance that does not involve publishing or subscription.
        :type SubFlag: str
        :param _ROFlag: Read-only flag. RO: read-only instance; MASTER: primary instance bound to a read-only instance. If this parameter is left blank, the instance is not a read-only instance and is not in any read-only group.
        :type ROFlag: str
        :param _HAFlag: Disaster recovery type. MIRROR: image; ALWAYSON: Always On; SINGLE: single instance.
        :type HAFlag: str
        :param _ResourceTags: Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceTags: list of ResourceTag
        :param _BackupModel: Backup mode. master_pkg: backup on the primary node (default value); master_no_pkg: no backup on the primary node; slave_pkg: backup on secondary nodes (valid for Always On clusters); slave_no_pkg: no backup on secondary nodes (valid for Always On clusters). This parameter is invalid for read-only instances.
        :type BackupModel: str
        :param _InstanceNote: Instance backup information.
        :type InstanceNote: str
        :param _BackupCycle: Backup cycle
        :type BackupCycle: list of int
        :param _BackupCycleType: Backup cycle type. Valid values: `daily`, `weekly`, `monthly`.
        :type BackupCycleType: str
        :param _BackupSaveDays: Data (log) backup retention period
        :type BackupSaveDays: int
        :param _InstanceType: Instance type. HA: high-availability instance; RO: read-only instance; SI: basic edition instance; BI: business intelligence service instance; cvmHA: high-availability instance with cloud disk; cvmRO: read-only instance with cloud disk; MultiHA: multi-node instance; cvmMultiHA: multi-node instance with cloud disk.

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
        :param _SlaveZones: Secondary AZ information on the two-node instance.
        :type SlaveZones: :class:`tencentcloud.sqlserver.v20180328.models.SlaveZones`
        :param _Architecture: Architecture flag. SINGLE: single-node; DOUBLE: two-node.
        :type Architecture: str
        :param _Style: Type flag. EXCLUSIVE: exclusive; SHARED: shared.
        :type Style: str
        :param _MultiSlaveZones: 
        :type MultiSlaveZones: list of SlaveZones
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
        self._MultiSlaveZones = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""Instance name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProjectId(self):
        r"""Project ID of instance
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        r"""Instance region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""Instance AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        r"""Instance VPC ID, which will be 0 if the basic network is used
        :rtype: int
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Instance VPC subnet ID, which will be 0 if the basic network is used
        :rtype: int
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        r"""Instance status. Valid values: <li>1: creating</li> <li>2: running</li> <li>3: instance operations restricted (due to the ongoing primary-replica switch)</li> <li>4: isolated</li> <li>5: repossessing</li> <li>6: repossessed</li> <li>7: running tasks (such as backup and rollback tasks)</li> <li>8: eliminated</li> <li>9: expanding capacity</li> <li>10: migrating</li> <li>11: read-only</li> <li>12: restarting</li>  <li>13: modifying configuration and waiting for switch</li> <li>14: implementing pub/sub</li> <li>15: modifying pub/sub configuration</li> <li>16: modifying configuration and switching</li> <li>17: creating read-only instances</li>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        r"""Instance access IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Instance access port
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CreateTime(self):
        r"""Instance creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Instance update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        r"""Instance billing start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Instance billing end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IsolateTime(self):
        r"""Instance isolation time
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

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
    def UsedStorage(self):
        r"""Used storage capacity of instance in GB
        :rtype: int
        """
        return self._UsedStorage

    @UsedStorage.setter
    def UsedStorage(self, UsedStorage):
        self._UsedStorage = UsedStorage

    @property
    def Storage(self):
        r"""Instance storage capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def VersionName(self):
        r"""Instance version
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def RenewFlag(self):
        r"""Instance renewal flag
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Model(self):
        r"""Instance disaster recovery type. 1: dual-server high availability; 2: single-node; 3: cross-AZ; 4: cross-AZ cluster; 5: cluster; 6: multi-node cluster; 7: multi-node cross-AZ cluster.
        :rtype: int
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Region(self):
        r"""Instance region name, such as ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""Instance AZ name, such as ap-guangzhou-1
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def BackupTime(self):
        r"""Backup time point
        :rtype: str
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def PayMode(self):
        r"""Instance billing mode. 0: pay-as-you-go
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Uid(self):
        r"""Instance UID
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Cpu(self):
        r"""Number of CPU cores of instance
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Version(self):
        r"""Instance version code
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Type(self):
        r"""Instance type. Valid values: `TS85` (physical machine, local SSD), `Z3` (early version of physical machine, local SSD), `CLOUD_BASIC` (virtual machine, HDD cloud disk), `CLOUD_PREMIUM` (virtual machine, premium cloud disk), `CLOUD_SSD` (virtual machine, SSD), `CLOUD_HSSD` (virtual machine, enhanced SSD), `CLOUD_TSSD` (virtual machine, ulTra SSD), `CLOUD_BSSD` virtual machine, balanced SSD).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Pid(self):
        r"""Billing ID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def UniqVpcId(self):
        r"""Unique string-type ID of instance VPC in the format of `vpc-xxx`, which is an empty string if the basic network is used
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        r"""Unique string-type ID of instance subnet in the format of `subnet-xxx`, which is an empty string if the basic network is used
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def IsolateOperator(self):
        r"""Instance isolation operation.
        :rtype: str
        """
        return self._IsolateOperator

    @IsolateOperator.setter
    def IsolateOperator(self, IsolateOperator):
        self._IsolateOperator = IsolateOperator

    @property
    def SubFlag(self):
        r"""Publishing/Subscription flag. SUB: subscription instance; PUB: publishing instance. If this parameter is left blank, the instance is an ordinary instance that does not involve publishing or subscription.
        :rtype: str
        """
        return self._SubFlag

    @SubFlag.setter
    def SubFlag(self, SubFlag):
        self._SubFlag = SubFlag

    @property
    def ROFlag(self):
        r"""Read-only flag. RO: read-only instance; MASTER: primary instance bound to a read-only instance. If this parameter is left blank, the instance is not a read-only instance and is not in any read-only group.
        :rtype: str
        """
        return self._ROFlag

    @ROFlag.setter
    def ROFlag(self, ROFlag):
        self._ROFlag = ROFlag

    @property
    def HAFlag(self):
        r"""Disaster recovery type. MIRROR: image; ALWAYSON: Always On; SINGLE: single instance.
        :rtype: str
        """
        return self._HAFlag

    @HAFlag.setter
    def HAFlag(self, HAFlag):
        self._HAFlag = HAFlag

    @property
    def ResourceTags(self):
        r"""Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def BackupModel(self):
        r"""Backup mode. master_pkg: backup on the primary node (default value); master_no_pkg: no backup on the primary node; slave_pkg: backup on secondary nodes (valid for Always On clusters); slave_no_pkg: no backup on secondary nodes (valid for Always On clusters). This parameter is invalid for read-only instances.
        :rtype: str
        """
        return self._BackupModel

    @BackupModel.setter
    def BackupModel(self, BackupModel):
        self._BackupModel = BackupModel

    @property
    def InstanceNote(self):
        r"""Instance backup information.
        :rtype: str
        """
        return self._InstanceNote

    @InstanceNote.setter
    def InstanceNote(self, InstanceNote):
        self._InstanceNote = InstanceNote

    @property
    def BackupCycle(self):
        r"""Backup cycle
        :rtype: list of int
        """
        return self._BackupCycle

    @BackupCycle.setter
    def BackupCycle(self, BackupCycle):
        self._BackupCycle = BackupCycle

    @property
    def BackupCycleType(self):
        r"""Backup cycle type. Valid values: `daily`, `weekly`, `monthly`.
        :rtype: str
        """
        return self._BackupCycleType

    @BackupCycleType.setter
    def BackupCycleType(self, BackupCycleType):
        self._BackupCycleType = BackupCycleType

    @property
    def BackupSaveDays(self):
        r"""Data (log) backup retention period
        :rtype: int
        """
        return self._BackupSaveDays

    @BackupSaveDays.setter
    def BackupSaveDays(self, BackupSaveDays):
        self._BackupSaveDays = BackupSaveDays

    @property
    def InstanceType(self):
        r"""Instance type. HA: high-availability instance; RO: read-only instance; SI: basic edition instance; BI: business intelligence service instance; cvmHA: high-availability instance with cloud disk; cvmRO: read-only instance with cloud disk; MultiHA: multi-node instance; cvmMultiHA: multi-node instance with cloud disk.

        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def CrossRegions(self):
        r"""The target region of cross-region backup. If this parameter left empty, it indicates that cross-region backup is disabled.
        :rtype: list of str
        """
        return self._CrossRegions

    @CrossRegions.setter
    def CrossRegions(self, CrossRegions):
        self._CrossRegions = CrossRegions

    @property
    def CrossBackupEnabled(self):
        r"""Cross-region backup status. Valid values: `enable` (enabled), `disable` (disabed)
        :rtype: str
        """
        return self._CrossBackupEnabled

    @CrossBackupEnabled.setter
    def CrossBackupEnabled(self, CrossBackupEnabled):
        self._CrossBackupEnabled = CrossBackupEnabled

    @property
    def CrossBackupSaveDays(self):
        r"""The retention period of cross-region backup. Default value: 7 days
        :rtype: int
        """
        return self._CrossBackupSaveDays

    @CrossBackupSaveDays.setter
    def CrossBackupSaveDays(self, CrossBackupSaveDays):
        self._CrossBackupSaveDays = CrossBackupSaveDays

    @property
    def DnsPodDomain(self):
        r"""Domain name of the public network address
        :rtype: str
        """
        return self._DnsPodDomain

    @DnsPodDomain.setter
    def DnsPodDomain(self, DnsPodDomain):
        self._DnsPodDomain = DnsPodDomain

    @property
    def TgwWanVPort(self):
        r"""Port number of the public network
        :rtype: int
        """
        return self._TgwWanVPort

    @TgwWanVPort.setter
    def TgwWanVPort(self, TgwWanVPort):
        self._TgwWanVPort = TgwWanVPort

    @property
    def Collation(self):
        r"""Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        r"""System time zone. Default value: `China Standard Time`.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def IsDrZone(self):
        r"""Whether the instance is deployed across AZs
        :rtype: bool
        """
        return self._IsDrZone

    @IsDrZone.setter
    def IsDrZone(self, IsDrZone):
        self._IsDrZone = IsDrZone

    @property
    def SlaveZones(self):
        r"""Secondary AZ information on the two-node instance.
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.SlaveZones`
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def Architecture(self):
        r"""Architecture flag. SINGLE: single-node; DOUBLE: two-node.
        :rtype: str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def Style(self):
        r"""Type flag. EXCLUSIVE: exclusive; SHARED: shared.
        :rtype: str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def MultiSlaveZones(self):
        r"""
        :rtype: list of SlaveZones
        """
        return self._MultiSlaveZones

    @MultiSlaveZones.setter
    def MultiSlaveZones(self, MultiSlaveZones):
        self._MultiSlaveZones = MultiSlaveZones


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
        if params.get("MultiSlaveZones") is not None:
            self._MultiSlaveZones = []
            for item in params.get("MultiSlaveZones"):
                obj = SlaveZones()
                obj._deserialize(item)
                self._MultiSlaveZones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBPrivilege(AbstractModel):
    r"""Database permission information of account

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
        r"""Database name
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Privilege(self):
        r"""Database permissions. Valid values: `ReadWrite` (read-write), `ReadOnly` (read-only), `DBOwner` (owner)
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
    r"""Database permission change information

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
        r"""Database name
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Privilege(self):
        r"""Permission modification information. Valid values: `ReadWrite` (read-write), `ReadOnly` (read-only), `Delete` (delete the account's permission to this database), `DBOwner` (owner).
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
    r"""Database remarks

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
        r"""Database name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""Remarks
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
    r"""Database renaming response parameter

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
        r"""Name of the new database
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName

    @property
    def OldName(self):
        r"""Name of the old database
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
    r"""This example shows you how to enable or disable TDE of a database.

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
        r"""
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Encryption(self):
        r"""TDE status. Valid values: `enable` (enabled), `disable` (disabled).
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
        


class DataBasePrivilegeModifyInfo(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _DataBaseName: 
        :type DataBaseName: str
        :param _AccountPrivileges: 
        :type AccountPrivileges: list of AccountPrivilege
        """
        self._DataBaseName = None
        self._AccountPrivileges = None

    @property
    def DataBaseName(self):
        r"""
        :rtype: str
        """
        return self._DataBaseName

    @DataBaseName.setter
    def DataBaseName(self, DataBaseName):
        self._DataBaseName = DataBaseName

    @property
    def AccountPrivileges(self):
        r"""
        :rtype: list of AccountPrivilege
        """
        return self._AccountPrivileges

    @AccountPrivileges.setter
    def AccountPrivileges(self, AccountPrivileges):
        self._AccountPrivileges = AccountPrivileges


    def _deserialize(self, params):
        self._DataBaseName = params.get("DataBaseName")
        if params.get("AccountPrivileges") is not None:
            self._AccountPrivileges = []
            for item in params.get("AccountPrivileges"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self._AccountPrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTuple(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _PublishDatabase: 
        :type PublishDatabase: str
        :param _SubscribeDatabase: 
        :type SubscribeDatabase: str
        """
        self._PublishDatabase = None
        self._SubscribeDatabase = None

    @property
    def PublishDatabase(self):
        r"""
        :rtype: str
        """
        return self._PublishDatabase

    @PublishDatabase.setter
    def PublishDatabase(self, PublishDatabase):
        self._PublishDatabase = PublishDatabase

    @property
    def SubscribeDatabase(self):
        r"""
        :rtype: str
        """
        return self._SubscribeDatabase

    @SubscribeDatabase.setter
    def SubscribeDatabase(self, SubscribeDatabase):
        self._SubscribeDatabase = SubscribeDatabase


    def _deserialize(self, params):
        self._PublishDatabase = params.get("PublishDatabase")
        self._SubscribeDatabase = params.get("SubscribeDatabase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTupleStatus(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _PublishDatabase: 
        :type PublishDatabase: str
        :param _SubscribeDatabase: 
        :type SubscribeDatabase: str
        :param _LastSyncTime: 
        :type LastSyncTime: str
        :param _Status: 
        :type Status: str
        """
        self._PublishDatabase = None
        self._SubscribeDatabase = None
        self._LastSyncTime = None
        self._Status = None

    @property
    def PublishDatabase(self):
        r"""
        :rtype: str
        """
        return self._PublishDatabase

    @PublishDatabase.setter
    def PublishDatabase(self, PublishDatabase):
        self._PublishDatabase = PublishDatabase

    @property
    def SubscribeDatabase(self):
        r"""
        :rtype: str
        """
        return self._SubscribeDatabase

    @SubscribeDatabase.setter
    def SubscribeDatabase(self, SubscribeDatabase):
        self._SubscribeDatabase = SubscribeDatabase

    @property
    def LastSyncTime(self):
        r"""
        :rtype: str
        """
        return self._LastSyncTime

    @LastSyncTime.setter
    def LastSyncTime(self, LastSyncTime):
        self._LastSyncTime = LastSyncTime

    @property
    def Status(self):
        r"""
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PublishDatabase = params.get("PublishDatabase")
        self._SubscribeDatabase = params.get("SubscribeDatabase")
        self._LastSyncTime = params.get("LastSyncTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbNormalDetail(AbstractModel):
    r"""Database configurations

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
        r"""Whether it is subscribed. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsSubscribed

    @IsSubscribed.setter
    def IsSubscribed(self, IsSubscribed):
        self._IsSubscribed = IsSubscribed

    @property
    def CollationName(self):
        r"""Database collation
        :rtype: str
        """
        return self._CollationName

    @CollationName.setter
    def CollationName(self, CollationName):
        self._CollationName = CollationName

    @property
    def IsAutoCleanupOn(self):
        r"""Whether the cleanup task is enabled to automatically remove old change tracking information when CT is enabled. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsAutoCleanupOn

    @IsAutoCleanupOn.setter
    def IsAutoCleanupOn(self, IsAutoCleanupOn):
        self._IsAutoCleanupOn = IsAutoCleanupOn

    @property
    def IsBrokerEnabled(self):
        r"""Whether SQL Server Service Broker is enabled. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsBrokerEnabled

    @IsBrokerEnabled.setter
    def IsBrokerEnabled(self, IsBrokerEnabled):
        self._IsBrokerEnabled = IsBrokerEnabled

    @property
    def IsCdcEnabled(self):
        r"""Whether CDC is enabled. Valid values: `0` (disabled), `1` (enabled)
        :rtype: str
        """
        return self._IsCdcEnabled

    @IsCdcEnabled.setter
    def IsCdcEnabled(self, IsCdcEnabled):
        self._IsCdcEnabled = IsCdcEnabled

    @property
    def IsDbChainingOn(self):
        r"""Whether CT is enabled. Valid values: `0` (disabled), `1` (enabled)
        :rtype: str
        """
        return self._IsDbChainingOn

    @IsDbChainingOn.setter
    def IsDbChainingOn(self, IsDbChainingOn):
        self._IsDbChainingOn = IsDbChainingOn

    @property
    def IsEncrypted(self):
        r"""Whether it is encrypted. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsEncrypted

    @IsEncrypted.setter
    def IsEncrypted(self, IsEncrypted):
        self._IsEncrypted = IsEncrypted

    @property
    def IsFulltextEnabled(self):
        warnings.warn("parameter `IsFulltextEnabled` is deprecated", DeprecationWarning) 

        r"""Whether full-text indexes are enabled. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsFulltextEnabled

    @IsFulltextEnabled.setter
    def IsFulltextEnabled(self, IsFulltextEnabled):
        warnings.warn("parameter `IsFulltextEnabled` is deprecated", DeprecationWarning) 

        self._IsFulltextEnabled = IsFulltextEnabled

    @property
    def IsMirroring(self):
        r"""Whether it is a mirror database. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsMirroring

    @IsMirroring.setter
    def IsMirroring(self, IsMirroring):
        self._IsMirroring = IsMirroring

    @property
    def IsPublished(self):
        r"""Whether it is published. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsPublished

    @IsPublished.setter
    def IsPublished(self, IsPublished):
        self._IsPublished = IsPublished

    @property
    def IsReadCommittedSnapshotOn(self):
        r"""Whether snapshots are enabled. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsReadCommittedSnapshotOn

    @IsReadCommittedSnapshotOn.setter
    def IsReadCommittedSnapshotOn(self, IsReadCommittedSnapshotOn):
        self._IsReadCommittedSnapshotOn = IsReadCommittedSnapshotOn

    @property
    def IsTrustworthyOn(self):
        r"""Whether it is trustworthy. Valid values: `0` (no), `1` (yes)
        :rtype: str
        """
        return self._IsTrustworthyOn

    @IsTrustworthyOn.setter
    def IsTrustworthyOn(self, IsTrustworthyOn):
        self._IsTrustworthyOn = IsTrustworthyOn

    @property
    def MirroringState(self):
        r"""Mirroring state
        :rtype: str
        """
        return self._MirroringState

    @MirroringState.setter
    def MirroringState(self, MirroringState):
        self._MirroringState = MirroringState

    @property
    def Name(self):
        r"""Database name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RecoveryModelDesc(self):
        r"""Recovery model
        :rtype: str
        """
        return self._RecoveryModelDesc

    @RecoveryModelDesc.setter
    def RecoveryModelDesc(self, RecoveryModelDesc):
        self._RecoveryModelDesc = RecoveryModelDesc

    @property
    def RetentionPeriod(self):
        r"""Retention period (in days) of change tracking information
        :rtype: str
        """
        return self._RetentionPeriod

    @RetentionPeriod.setter
    def RetentionPeriod(self, RetentionPeriod):
        self._RetentionPeriod = RetentionPeriod

    @property
    def StateDesc(self):
        r"""Database status
        :rtype: str
        """
        return self._StateDesc

    @StateDesc.setter
    def StateDesc(self, StateDesc):
        self._StateDesc = StateDesc

    @property
    def UserAccessDesc(self):
        r"""User type
        :rtype: str
        """
        return self._UserAccessDesc

    @UserAccessDesc.setter
    def UserAccessDesc(self, UserAccessDesc):
        self._UserAccessDesc = UserAccessDesc

    @property
    def CreateTime(self):
        r"""Database creation time
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
    r"""Information of time range available for database rollback

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
        r"""Database name
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def StartTime(self):
        r"""Start time of time range available for rollback
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time of time range available for rollback
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
    r"""Order information

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
        r"""Order name
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def Count(self):
        r"""Number of items
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def FlowId(self):
        r"""ID of associated flow, which can be used to query the flow execution status
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceIdSet(self):
        r"""This field is required only for an order that creates an instance, indicating the ID of the instance created by the order
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def OwnerUin(self):
        r"""Account
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def InstanceChargeType(self):
        r"""Instance billing type
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
    r"""List of the resource IDs corresponding to order number

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
        r"""Instance ID
        :rtype: list of str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealName(self):
        r"""Order ID
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
    r"""DeleteAccount request structure.

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
        r"""Database instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserNames(self):
        r"""Array of instance usernames
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
    r"""DeleteAccount response structure.

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
        r"""Task flow ID
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


class DeleteBackupMigrationRequest(AbstractModel):
    r"""DeleteBackupMigration request structure.

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
        r"""Target instance ID, which is returned through the API DescribeBackupMigration.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the API DescribeBackupMigration.
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
    r"""DeleteBackupMigration response structure.

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


class DeleteBusinessIntelligenceFileRequest(AbstractModel):
    r"""DeleteBusinessIntelligenceFile request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileNameSet(self):
        r"""File name set
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
    r"""DeleteBusinessIntelligenceFile response structure.

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


class DeleteDBInstanceRequest(AbstractModel):
    r"""DeleteDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-3l3fgqn7 or mssqlro-3l3fgqn7.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-3l3fgqn7 or mssqlro-3l3fgqn7.
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
        


class DeleteDBInstanceResponse(AbstractModel):
    r"""DeleteDBInstance response structure.

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


class DeleteDBRequest(AbstractModel):
    r"""DeleteDB request structure.

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
        r"""Instance ID in the format of mssql-rljoi3bf
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Names(self):
        r"""Array of database names
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
    r"""DeleteDB response structure.

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
        r"""Task flow ID
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


class DeleteIncrementalMigrationRequest(AbstractModel):
    r"""DeleteIncrementalMigration request structure.

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
        r"""Target instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the `CreateBackupMigration` API
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        r"""Incremental backup import task ID, which is returned through the `CreateIncrementalMigration` API
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
    r"""DeleteIncrementalMigration response structure.

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


class DeleteMigrationRequest(AbstractModel):
    r"""DeleteMigration request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        r"""Migration task ID
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
    r"""DeleteMigration response structure.

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


class DeletePublishSubscribeRequest(AbstractModel):
    r"""DeletePublishSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _PublishSubscribeId: Publish/subscribe ID, which can be obtained through the DescribePublishSubscribe API.
        :type PublishSubscribeId: int
        :param _DatabaseTupleSet: Publish/subscribe relationship collection of the database to be deleted.
        :type DatabaseTupleSet: list of DatabaseTuple
        """
        self._PublishSubscribeId = None
        self._DatabaseTupleSet = None

    @property
    def PublishSubscribeId(self):
        r"""Publish/subscribe ID, which can be obtained through the DescribePublishSubscribe API.
        :rtype: int
        """
        return self._PublishSubscribeId

    @PublishSubscribeId.setter
    def PublishSubscribeId(self, PublishSubscribeId):
        self._PublishSubscribeId = PublishSubscribeId

    @property
    def DatabaseTupleSet(self):
        r"""Publish/subscribe relationship collection of the database to be deleted.
        :rtype: list of DatabaseTuple
        """
        return self._DatabaseTupleSet

    @DatabaseTupleSet.setter
    def DatabaseTupleSet(self, DatabaseTupleSet):
        self._DatabaseTupleSet = DatabaseTupleSet


    def _deserialize(self, params):
        self._PublishSubscribeId = params.get("PublishSubscribeId")
        if params.get("DatabaseTupleSet") is not None:
            self._DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = DatabaseTuple()
                obj._deserialize(item)
                self._DatabaseTupleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePublishSubscribeResponse(AbstractModel):
    r"""DeletePublishSubscribe response structure.

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


class DescribeAccountPrivilegeByDBRequest(AbstractModel):
    r"""DescribeAccountPrivilegeByDB request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-njj2mtpl7.
        :type InstanceId: str
        :param _DBName: Database name.
        :type DBName: str
        :param _AccountName: Database account name.
        :type AccountName: str
        :param _Limit: The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 20.
        :type Limit: int
        :param _Offset: Page number in pagination mode. The default value is 0.
        :type Offset: int
        """
        self._InstanceId = None
        self._DBName = None
        self._AccountName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-njj2mtpl7.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBName(self):
        r"""Database name.
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def AccountName(self):
        r"""Database account name.
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Limit(self):
        r"""The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number in pagination mode. The default value is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DBName = params.get("DBName")
        self._AccountName = params.get("AccountName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegeByDBResponse(AbstractModel):
    r"""DescribeAccountPrivilegeByDB response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of accounts.
        :type TotalCount: int
        :param _Accounts: Account permission list.
        :type Accounts: list of AccountPrivilege
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Accounts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of accounts.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Accounts(self):
        r"""Account permission list.
        :rtype: list of AccountPrivilege
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
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
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    r"""DescribeAccounts request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""Number of results per page. Value range: 1-100. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Name(self):
        r"""Account ID
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OrderBy(self):
        r"""Sorting by `createTime`, `updateTime`, or `passTime`. Default value: `createTime` (desc).
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting rule. Valid values: `desc` (descending order), `asc` (ascending order). Default value: `desc`.
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
    r"""DescribeAccounts response structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        r"""Account information list
        :rtype: list of AccountDetail
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def TotalCount(self):
        r"""Total number
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
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountDetail()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBackupByFlowIdRequest(AbstractModel):
    r"""DescribeBackupByFlowId request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-3l3fgqn7.
        :type InstanceId: str
        :param _FlowId: Backup creation process ID, which can be obtained through the [CreateBackup](https://cloud.tencent.com/document/product/238/19946) API.
        :type FlowId: str
        """
        self._InstanceId = None
        self._FlowId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-3l3fgqn7.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        r"""Backup creation process ID, which can be obtained through the [CreateBackup](https://cloud.tencent.com/document/product/238/19946) API.
        :rtype: str
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
        


class DescribeBackupByFlowIdResponse(AbstractModel):
    r"""DescribeBackupByFlowId response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Unique identifier of the backup file. This field is used by the RestoreInstance API. For a single-database backup file, only the unique identifier of the backup file for the first record is returned. Through the DescribeBackupFiles API, IDs of all backup files that are available for rollback can be obtained for single-database backup files.
        :type Id: int
        :param _FileName: File name. For a single-database backup file, only the file name of the first record is returned. Through the DescribeBackupFiles API, file names of all records can be obtained for single-database backup files.
        :type FileName: str
        :param _BackupName: Backup task name, which can be customized.
        :type BackupName: str
        :param _StartTime: Backup start time.
        :type StartTime: str
        :param _EndTime: Backup end time.
        :type EndTime: str
        :param _Size: File size, in KB. For a single-database backup file, only the file size of the first record is returned. Through the DescribeBackupFiles API, file sizes of all records can be obtained for single-database backup files.
        :type Size: int
        :param _Strategy: Backup policy: 0 - instance backup; 1 - multi-database backup. When the instance status is 0 - creating, the default value of this field is 0, which has no practical significance.
        :type Strategy: int
        :param _Status: Backup file status. 0 - creating; 1 - successful; 2-failed.
        :type Status: int
        :param _BackupWay: Backup method. 0 - scheduled backup; 1 - manual temporary backup. When the instance status is 0 - creating, the default value of this field is 0, which has no practical significance.
        :type BackupWay: int
        :param _DBs: Database list. For a single-database backup file, only the database name included in the first record is returned. Through the DescribeBackupFiles API, the database names of all records can be obtained for single-database backup files.
        :type DBs: list of str
        :param _InternalAddr: Private network download address. For a single-database backup file, only the private network download address of the first record is returned. Through the DescribeBackupFiles API, download addresses of all records can be obtained for single-database backup files.
        :type InternalAddr: str
        :param _ExternalAddr: Public network download address. For a single-database backup file, only the public network download address of the first record is returned. Through the DescribeBackupFiles API, download addresses of all records can be obtained for single-database backup files.
        :type ExternalAddr: str
        :param _GroupId: Aggregation ID. This value is not returned for packaging backup files. Call the DescribeBackupFiles API with this value to obtain detailed information about single-database backup files.
        :type GroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._FileName = None
        self._BackupName = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Strategy = None
        self._Status = None
        self._BackupWay = None
        self._DBs = None
        self._InternalAddr = None
        self._ExternalAddr = None
        self._GroupId = None
        self._RequestId = None

    @property
    def Id(self):
        r"""Unique identifier of the backup file. This field is used by the RestoreInstance API. For a single-database backup file, only the unique identifier of the backup file for the first record is returned. Through the DescribeBackupFiles API, IDs of all backup files that are available for rollback can be obtained for single-database backup files.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FileName(self):
        r"""File name. For a single-database backup file, only the file name of the first record is returned. Through the DescribeBackupFiles API, file names of all records can be obtained for single-database backup files.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def BackupName(self):
        r"""Backup task name, which can be customized.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def StartTime(self):
        r"""Backup start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Backup end time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        r"""File size, in KB. For a single-database backup file, only the file size of the first record is returned. Through the DescribeBackupFiles API, file sizes of all records can be obtained for single-database backup files.
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Strategy(self):
        r"""Backup policy: 0 - instance backup; 1 - multi-database backup. When the instance status is 0 - creating, the default value of this field is 0, which has no practical significance.
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Status(self):
        r"""Backup file status. 0 - creating; 1 - successful; 2-failed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BackupWay(self):
        r"""Backup method. 0 - scheduled backup; 1 - manual temporary backup. When the instance status is 0 - creating, the default value of this field is 0, which has no practical significance.
        :rtype: int
        """
        return self._BackupWay

    @BackupWay.setter
    def BackupWay(self, BackupWay):
        self._BackupWay = BackupWay

    @property
    def DBs(self):
        r"""Database list. For a single-database backup file, only the database name included in the first record is returned. Through the DescribeBackupFiles API, the database names of all records can be obtained for single-database backup files.
        :rtype: list of str
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def InternalAddr(self):
        r"""Private network download address. For a single-database backup file, only the private network download address of the first record is returned. Through the DescribeBackupFiles API, download addresses of all records can be obtained for single-database backup files.
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        r"""Public network download address. For a single-database backup file, only the public network download address of the first record is returned. Through the DescribeBackupFiles API, download addresses of all records can be obtained for single-database backup files.
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def GroupId(self):
        r"""Aggregation ID. This value is not returned for packaging backup files. Call the DescribeBackupFiles API with this value to obtain detailed information about single-database backup files.
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._FileName = params.get("FileName")
        self._BackupName = params.get("BackupName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Strategy = params.get("Strategy")
        self._Status = params.get("Status")
        self._BackupWay = params.get("BackupWay")
        self._DBs = params.get("DBs")
        self._InternalAddr = params.get("InternalAddr")
        self._ExternalAddr = params.get("ExternalAddr")
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class DescribeBackupCommandRequest(AbstractModel):
    r"""DescribeBackupCommand request structure.

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
        r"""Backup file type. Full: full backup. FULL_LOG: full backup which needs log increments. FULL_DIFF: full backup which needs differential increments. LOG: log backup. DIFF: differential backup.
        :rtype: str
        """
        return self._BackupFileType

    @BackupFileType.setter
    def BackupFileType(self, BackupFileType):
        self._BackupFileType = BackupFileType

    @property
    def DataBaseName(self):
        r"""Database name
        :rtype: str
        """
        return self._DataBaseName

    @DataBaseName.setter
    def DataBaseName(self, DataBaseName):
        self._DataBaseName = DataBaseName

    @property
    def IsRecovery(self):
        r"""Whether restoration is required. No: not required. Yes: required.
        :rtype: str
        """
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery

    @property
    def LocalPath(self):
        r"""Storage path of backup files. If this parameter is left empty, the default storage path will be D:\\.
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
    r"""DescribeBackupCommand response structure.

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
        r"""Create a backup command
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeBackupFiles request structure.

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
        :param _OrderByType: Sorting field. Size - sort by backup size; DBs - sort by database name. The default value is size.
        :type OrderByType: str
        """
        self._InstanceId = None
        self._GroupId = None
        self._Limit = None
        self._Offset = None
        self._DatabaseName = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        r"""Instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupId(self):
        r"""Group ID of unarchived backup files, which can be obtained by the `DescribeBackups` API (Querying archived backup record is not supported).
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Limit(self):
        r"""Number of entries to be returned per page. Value range: 1-100. Default value: `20`
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number. Default value: `0`
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DatabaseName(self):
        r"""Filter backups by database name. If the parameter is left empty, this filter criterion will not take effect.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def OrderBy(self):
        r"""List items sorting by backup size. Valid values: `desc`(descending order), `asc` (ascending order). Default value: `desc`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting field. Size - sort by backup size; DBs - sort by database name. The default value is size.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupId = params.get("GroupId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DatabaseName = params.get("DatabaseName")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupFilesResponse(AbstractModel):
    r"""DescribeBackupFiles response structure.

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
        r"""Total number of backups
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupFiles(self):
        r"""List of backup file details
        :rtype: list of BackupFile
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
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
        if params.get("BackupFiles") is not None:
            self._BackupFiles = []
            for item in params.get("BackupFiles"):
                obj = BackupFile()
                obj._deserialize(item)
                self._BackupFiles.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupMigrationRequest(AbstractModel):
    r"""DescribeBackupMigration request structure.

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
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the API CreateBackupMigration.
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def MigrationName(self):
        r"""Import task name
        :rtype: str
        """
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def BackupFileName(self):
        r"""Backup file name
        :rtype: str
        """
        return self._BackupFileName

    @BackupFileName.setter
    def BackupFileName(self, BackupFileName):
        self._BackupFileName = BackupFileName

    @property
    def StatusSet(self):
        r"""Status set of import tasks
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def RecoveryType(self):
        r"""Import task restoration type: FULL,FULL_LOG,FULL_DIFF
        :rtype: str
        """
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        r"""COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :rtype: str
        """
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def Limit(self):
        r"""The maximum number of results returned per page. Default value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sort by field. Valid values: `name`, `createTime`, `startTime`, `endTime`. By default, the results returned are sorted by `createTime` in the ascending order.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order which is valid only when `OrderBy` is specified. Valid values: `asc` (ascending), `desc` (descending). Default value: `asc`.
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
    r"""DescribeBackupMigration response structure.

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
        r"""Total number of tasks
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupMigrationSet(self):
        r"""Migration task set
        :rtype: list of Migration
        """
        return self._BackupMigrationSet

    @BackupMigrationSet.setter
    def BackupMigrationSet(self, BackupMigrationSet):
        self._BackupMigrationSet = BackupMigrationSet

    @property
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
        if params.get("BackupMigrationSet") is not None:
            self._BackupMigrationSet = []
            for item in params.get("BackupMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self._BackupMigrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupMonitorRequest(AbstractModel):
    r"""DescribeBackupMonitor request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Sets the start time for querying backup space usage details.
        :type StartTime: str
        :param _EndTime: End time of backup space usage.
        :type EndTime: str
        :param _Type: Backup trend query type. local - local backup; cross - cross-region backup.
        :type Type: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Type = None

    @property
    def StartTime(self):
        r"""Sets the start time for querying backup space usage details.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time of backup space usage.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""Backup trend query type. local - local backup; cross - cross-region backup.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
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
        


class DescribeBackupMonitorResponse(AbstractModel):
    r"""DescribeBackupMonitor response structure.

    """

    def __init__(self):
        r"""
        :param _TimeStamp: Backup trend chart timeline.
        :type TimeStamp: list of str
        :param _FreeSpace: Free backup space.
        :type FreeSpace: list of float
        :param _ActualUsedSpace: Actual total backup space.
        :type ActualUsedSpace: list of float
        :param _LogBackupSpace: Backup space for logs.
        :type LogBackupSpace: list of float
        :param _DataBackupSpace: Backup space for data.
        :type DataBackupSpace: list of float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TimeStamp = None
        self._FreeSpace = None
        self._ActualUsedSpace = None
        self._LogBackupSpace = None
        self._DataBackupSpace = None
        self._RequestId = None

    @property
    def TimeStamp(self):
        r"""Backup trend chart timeline.
        :rtype: list of str
        """
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp

    @property
    def FreeSpace(self):
        r"""Free backup space.
        :rtype: list of float
        """
        return self._FreeSpace

    @FreeSpace.setter
    def FreeSpace(self, FreeSpace):
        self._FreeSpace = FreeSpace

    @property
    def ActualUsedSpace(self):
        r"""Actual total backup space.
        :rtype: list of float
        """
        return self._ActualUsedSpace

    @ActualUsedSpace.setter
    def ActualUsedSpace(self, ActualUsedSpace):
        self._ActualUsedSpace = ActualUsedSpace

    @property
    def LogBackupSpace(self):
        r"""Backup space for logs.
        :rtype: list of float
        """
        return self._LogBackupSpace

    @LogBackupSpace.setter
    def LogBackupSpace(self, LogBackupSpace):
        self._LogBackupSpace = LogBackupSpace

    @property
    def DataBackupSpace(self):
        r"""Backup space for data.
        :rtype: list of float
        """
        return self._DataBackupSpace

    @DataBackupSpace.setter
    def DataBackupSpace(self, DataBackupSpace):
        self._DataBackupSpace = DataBackupSpace

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TimeStamp = params.get("TimeStamp")
        self._FreeSpace = params.get("FreeSpace")
        self._ActualUsedSpace = params.get("ActualUsedSpace")
        self._LogBackupSpace = params.get("LogBackupSpace")
        self._DataBackupSpace = params.get("DataBackupSpace")
        self._RequestId = params.get("RequestId")


class DescribeBackupStatisticalRequest(AbstractModel):
    r"""DescribeBackupStatistical request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 100.
        :type Limit: int
        :param _Offset: Page number in pagination mode. The default value is 0.
        :type Offset: int
        :param _InstanceIdSet: One or more instance IDs. The instance ID is in the format of mssql-si2823jyl.
        :type InstanceIdSet: list of str
        :param _InstanceNameSet: Instance name list. Fuzzy query is supported.
        :type InstanceNameSet: list of str
        :param _OrderBy: Sorting field. The default value is default, which indicates sorting by backup space in descending order. default - sort by backup space; data - sort by data backup; log - sort by log backup; auto - sort by automatic backup; manual - sort by manual backup.
        :type OrderBy: str
        :param _OrderByType: The default value is desc. [desc - descending order; asc - ascending order].
        :type OrderByType: str
        """
        self._Limit = None
        self._Offset = None
        self._InstanceIdSet = None
        self._InstanceNameSet = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Limit(self):
        r"""The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number in pagination mode. The default value is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceIdSet(self):
        r"""One or more instance IDs. The instance ID is in the format of mssql-si2823jyl.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def InstanceNameSet(self):
        r"""Instance name list. Fuzzy query is supported.
        :rtype: list of str
        """
        return self._InstanceNameSet

    @InstanceNameSet.setter
    def InstanceNameSet(self, InstanceNameSet):
        self._InstanceNameSet = InstanceNameSet

    @property
    def OrderBy(self):
        r"""Sorting field. The default value is default, which indicates sorting by backup space in descending order. default - sort by backup space; data - sort by data backup; log - sort by log backup; auto - sort by automatic backup; manual - sort by manual backup.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""The default value is desc. [desc - descending order; asc - ascending order].
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._InstanceNameSet = params.get("InstanceNameSet")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupStatisticalResponse(AbstractModel):
    r"""DescribeBackupStatistical response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances meeting conditions. When results are returned in pagination mode, this value refers to the total number of instances that meet conditions, rather than the number of instances returned based on the specified Limit and Offset values.
        :type TotalCount: int
        :param _Items: Instance list.
        :type Items: list of SummaryDetailRes
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of instances meeting conditions. When results are returned in pagination mode, this value refers to the total number of instances that meet conditions, rather than the number of instances returned based on the specified Limit and Offset values.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""Instance list.
        :rtype: list of SummaryDetailRes
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
                obj = SummaryDetailRes()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupSummaryRequest(AbstractModel):
    r"""DescribeBackupSummary request structure.

    """


class DescribeBackupSummaryResponse(AbstractModel):
    r"""DescribeBackupSummary response structure.

    """

    def __init__(self):
        r"""
        :param _FreeSpace: Actual free total space, in KB.
        :type FreeSpace: int
        :param _ActualUsedSpace: Actual used space of backups, in KB.
        :type ActualUsedSpace: int
        :param _BackupFilesTotal: Total number of backup files.
        :type BackupFilesTotal: int
        :param _BillingSpace: Charged space of the space occupied by backups, in KB.
        :type BillingSpace: int
        :param _DataBackupSpace: Data backup usage space, in KB.
        :type DataBackupSpace: int
        :param _DataBackupCount: Total number of data backup files.
        :type DataBackupCount: int
        :param _ManualBackupSpace: Storage space used by manual backups in data backup, in KB.
        :type ManualBackupSpace: int
        :param _ManualBackupCount: Total number of files for manual backups in data backup.
        :type ManualBackupCount: int
        :param _AutoBackupSpace: Storage space used by automatic backups in data backup, in KB.
        :type AutoBackupSpace: int
        :param _AutoBackupCount: Total number of files for automatic backups in data backup.
        :type AutoBackupCount: int
        :param _LogBackupSpace: Backup usage space for logs, in KB.
        :type LogBackupSpace: int
        :param _LogBackupCount: Total number of log backup files.
        :type LogBackupCount: int
        :param _EstimatedAmount: Estimated fees, in USD/hour.
        :type EstimatedAmount: float
        :param _LocalBackupFilesTotal: Total number of local backup files.
        :type LocalBackupFilesTotal: int
        :param _CrossBackupFilesTotal: Total number of cross-region backup files.
        :type CrossBackupFilesTotal: int
        :param _CrossBillingSpace: Charged space of the space occupied by cross-region backups, in KB.
        :type CrossBillingSpace: int
        :param _CrossAutoBackupSpace: Space used by cross-region automatic data backups, in KB.
        :type CrossAutoBackupSpace: int
        :param _CrossAutoBackupCount: Total number of files for cross-region automatic data backups.
        :type CrossAutoBackupCount: int
        :param _LocalLogBackupSpace: Space used by local log backups, in KB.
        :type LocalLogBackupSpace: int
        :param _LocalLogBackupCount: Total number of files for local log backups.
        :type LocalLogBackupCount: int
        :param _CrossLogBackupSpace: Space used by cross-region log backups, in KB.
        :type CrossLogBackupSpace: int
        :param _CrossLogBackupCount: Total number of files for cross-region log backups.
        :type CrossLogBackupCount: int
        :param _CrossEstimatedAmount: Estimated fees for cross-region backups, in USD/hour.
        :type CrossEstimatedAmount: float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FreeSpace = None
        self._ActualUsedSpace = None
        self._BackupFilesTotal = None
        self._BillingSpace = None
        self._DataBackupSpace = None
        self._DataBackupCount = None
        self._ManualBackupSpace = None
        self._ManualBackupCount = None
        self._AutoBackupSpace = None
        self._AutoBackupCount = None
        self._LogBackupSpace = None
        self._LogBackupCount = None
        self._EstimatedAmount = None
        self._LocalBackupFilesTotal = None
        self._CrossBackupFilesTotal = None
        self._CrossBillingSpace = None
        self._CrossAutoBackupSpace = None
        self._CrossAutoBackupCount = None
        self._LocalLogBackupSpace = None
        self._LocalLogBackupCount = None
        self._CrossLogBackupSpace = None
        self._CrossLogBackupCount = None
        self._CrossEstimatedAmount = None
        self._RequestId = None

    @property
    def FreeSpace(self):
        r"""Actual free total space, in KB.
        :rtype: int
        """
        return self._FreeSpace

    @FreeSpace.setter
    def FreeSpace(self, FreeSpace):
        self._FreeSpace = FreeSpace

    @property
    def ActualUsedSpace(self):
        r"""Actual used space of backups, in KB.
        :rtype: int
        """
        return self._ActualUsedSpace

    @ActualUsedSpace.setter
    def ActualUsedSpace(self, ActualUsedSpace):
        self._ActualUsedSpace = ActualUsedSpace

    @property
    def BackupFilesTotal(self):
        r"""Total number of backup files.
        :rtype: int
        """
        return self._BackupFilesTotal

    @BackupFilesTotal.setter
    def BackupFilesTotal(self, BackupFilesTotal):
        self._BackupFilesTotal = BackupFilesTotal

    @property
    def BillingSpace(self):
        r"""Charged space of the space occupied by backups, in KB.
        :rtype: int
        """
        return self._BillingSpace

    @BillingSpace.setter
    def BillingSpace(self, BillingSpace):
        self._BillingSpace = BillingSpace

    @property
    def DataBackupSpace(self):
        r"""Data backup usage space, in KB.
        :rtype: int
        """
        return self._DataBackupSpace

    @DataBackupSpace.setter
    def DataBackupSpace(self, DataBackupSpace):
        self._DataBackupSpace = DataBackupSpace

    @property
    def DataBackupCount(self):
        r"""Total number of data backup files.
        :rtype: int
        """
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def ManualBackupSpace(self):
        r"""Storage space used by manual backups in data backup, in KB.
        :rtype: int
        """
        return self._ManualBackupSpace

    @ManualBackupSpace.setter
    def ManualBackupSpace(self, ManualBackupSpace):
        self._ManualBackupSpace = ManualBackupSpace

    @property
    def ManualBackupCount(self):
        r"""Total number of files for manual backups in data backup.
        :rtype: int
        """
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def AutoBackupSpace(self):
        r"""Storage space used by automatic backups in data backup, in KB.
        :rtype: int
        """
        return self._AutoBackupSpace

    @AutoBackupSpace.setter
    def AutoBackupSpace(self, AutoBackupSpace):
        self._AutoBackupSpace = AutoBackupSpace

    @property
    def AutoBackupCount(self):
        r"""Total number of files for automatic backups in data backup.
        :rtype: int
        """
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def LogBackupSpace(self):
        r"""Backup usage space for logs, in KB.
        :rtype: int
        """
        return self._LogBackupSpace

    @LogBackupSpace.setter
    def LogBackupSpace(self, LogBackupSpace):
        self._LogBackupSpace = LogBackupSpace

    @property
    def LogBackupCount(self):
        r"""Total number of log backup files.
        :rtype: int
        """
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def EstimatedAmount(self):
        r"""Estimated fees, in USD/hour.
        :rtype: float
        """
        return self._EstimatedAmount

    @EstimatedAmount.setter
    def EstimatedAmount(self, EstimatedAmount):
        self._EstimatedAmount = EstimatedAmount

    @property
    def LocalBackupFilesTotal(self):
        r"""Total number of local backup files.
        :rtype: int
        """
        return self._LocalBackupFilesTotal

    @LocalBackupFilesTotal.setter
    def LocalBackupFilesTotal(self, LocalBackupFilesTotal):
        self._LocalBackupFilesTotal = LocalBackupFilesTotal

    @property
    def CrossBackupFilesTotal(self):
        r"""Total number of cross-region backup files.
        :rtype: int
        """
        return self._CrossBackupFilesTotal

    @CrossBackupFilesTotal.setter
    def CrossBackupFilesTotal(self, CrossBackupFilesTotal):
        self._CrossBackupFilesTotal = CrossBackupFilesTotal

    @property
    def CrossBillingSpace(self):
        r"""Charged space of the space occupied by cross-region backups, in KB.
        :rtype: int
        """
        return self._CrossBillingSpace

    @CrossBillingSpace.setter
    def CrossBillingSpace(self, CrossBillingSpace):
        self._CrossBillingSpace = CrossBillingSpace

    @property
    def CrossAutoBackupSpace(self):
        r"""Space used by cross-region automatic data backups, in KB.
        :rtype: int
        """
        return self._CrossAutoBackupSpace

    @CrossAutoBackupSpace.setter
    def CrossAutoBackupSpace(self, CrossAutoBackupSpace):
        self._CrossAutoBackupSpace = CrossAutoBackupSpace

    @property
    def CrossAutoBackupCount(self):
        r"""Total number of files for cross-region automatic data backups.
        :rtype: int
        """
        return self._CrossAutoBackupCount

    @CrossAutoBackupCount.setter
    def CrossAutoBackupCount(self, CrossAutoBackupCount):
        self._CrossAutoBackupCount = CrossAutoBackupCount

    @property
    def LocalLogBackupSpace(self):
        r"""Space used by local log backups, in KB.
        :rtype: int
        """
        return self._LocalLogBackupSpace

    @LocalLogBackupSpace.setter
    def LocalLogBackupSpace(self, LocalLogBackupSpace):
        self._LocalLogBackupSpace = LocalLogBackupSpace

    @property
    def LocalLogBackupCount(self):
        r"""Total number of files for local log backups.
        :rtype: int
        """
        return self._LocalLogBackupCount

    @LocalLogBackupCount.setter
    def LocalLogBackupCount(self, LocalLogBackupCount):
        self._LocalLogBackupCount = LocalLogBackupCount

    @property
    def CrossLogBackupSpace(self):
        r"""Space used by cross-region log backups, in KB.
        :rtype: int
        """
        return self._CrossLogBackupSpace

    @CrossLogBackupSpace.setter
    def CrossLogBackupSpace(self, CrossLogBackupSpace):
        self._CrossLogBackupSpace = CrossLogBackupSpace

    @property
    def CrossLogBackupCount(self):
        r"""Total number of files for cross-region log backups.
        :rtype: int
        """
        return self._CrossLogBackupCount

    @CrossLogBackupCount.setter
    def CrossLogBackupCount(self, CrossLogBackupCount):
        self._CrossLogBackupCount = CrossLogBackupCount

    @property
    def CrossEstimatedAmount(self):
        r"""Estimated fees for cross-region backups, in USD/hour.
        :rtype: float
        """
        return self._CrossEstimatedAmount

    @CrossEstimatedAmount.setter
    def CrossEstimatedAmount(self, CrossEstimatedAmount):
        self._CrossEstimatedAmount = CrossEstimatedAmount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FreeSpace = params.get("FreeSpace")
        self._ActualUsedSpace = params.get("ActualUsedSpace")
        self._BackupFilesTotal = params.get("BackupFilesTotal")
        self._BillingSpace = params.get("BillingSpace")
        self._DataBackupSpace = params.get("DataBackupSpace")
        self._DataBackupCount = params.get("DataBackupCount")
        self._ManualBackupSpace = params.get("ManualBackupSpace")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._AutoBackupSpace = params.get("AutoBackupSpace")
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._LogBackupSpace = params.get("LogBackupSpace")
        self._LogBackupCount = params.get("LogBackupCount")
        self._EstimatedAmount = params.get("EstimatedAmount")
        self._LocalBackupFilesTotal = params.get("LocalBackupFilesTotal")
        self._CrossBackupFilesTotal = params.get("CrossBackupFilesTotal")
        self._CrossBillingSpace = params.get("CrossBillingSpace")
        self._CrossAutoBackupSpace = params.get("CrossAutoBackupSpace")
        self._CrossAutoBackupCount = params.get("CrossAutoBackupCount")
        self._LocalLogBackupSpace = params.get("LocalLogBackupSpace")
        self._LocalLogBackupCount = params.get("LocalLogBackupCount")
        self._CrossLogBackupSpace = params.get("CrossLogBackupSpace")
        self._CrossLogBackupCount = params.get("CrossLogBackupCount")
        self._CrossEstimatedAmount = params.get("CrossEstimatedAmount")
        self._RequestId = params.get("RequestId")


class DescribeBackupUploadSizeRequest(AbstractModel):
    r"""DescribeBackupUploadSize request structure.

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
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        r"""Incremental import task ID
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
    r"""DescribeBackupUploadSize response structure.

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
        r"""Information of uploaded backups
        :rtype: list of CosUploadBackupFile
        """
        return self._CosUploadBackupFileSet

    @CosUploadBackupFileSet.setter
    def CosUploadBackupFileSet(self, CosUploadBackupFileSet):
        self._CosUploadBackupFileSet = CosUploadBackupFileSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeBackups request structure.

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
        :param _StorageStrategy: Backup storage policy. 0 - follow the custom backup retention policy; 1 - follow the instance lifecycle until the instance is eliminated. The default value is 0.
        :type StorageStrategy: int
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
        self._StorageStrategy = None

    @property
    def StartTime(self):
        r"""Start name (yyyy-MM-dd HH:mm:ss)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time (yyyy-MM-dd HH:mm:ss)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceId(self):
        r"""Instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""Number of results per page. Value range: 1-100. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BackupName(self):
        r"""Filter by backup name. If this parameter is left empty, backup name will not be used in filtering.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def Strategy(self):
        r"""Filter by backup policy. Valid values: 0 (instance backup), 1 (multi-database backup). If this parameter is left empty, backup policy will not be used in filtering.
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def BackupWay(self):
        r"""Filter by backup mode. Valid values: `0` (scheduled backup); `1` (manual backup); `2` (archive backup). Default value: `2`.
        :rtype: int
        """
        return self._BackupWay

    @BackupWay.setter
    def BackupWay(self, BackupWay):
        self._BackupWay = BackupWay

    @property
    def BackupId(self):
        r"""Filter by backup ID. If this parameter is left empty, backup ID will not be used in filtering.
        :rtype: int
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def DatabaseName(self):
        r"""Filter backups by the database name. If the parameter is left empty, this filter criteria will not take effect.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Group(self):
        r"""Whether to group backup files by backup task. Valid value: `0` (no), `1` (yes). Default value: `0`. This parameter is valid only for unarchived backup files.
        :rtype: int
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Type(self):
        r"""Backup type. Valid values: `1` (data backup), `2` (log backup). Default value: `1`.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BackupFormat(self):
        r"""Filter by backup file format. Valid values: `pkg` (archive file), `single` (Unarchived files).
        :rtype: str
        """
        return self._BackupFormat

    @BackupFormat.setter
    def BackupFormat(self, BackupFormat):
        self._BackupFormat = BackupFormat

    @property
    def StorageStrategy(self):
        r"""Backup storage policy. 0 - follow the custom backup retention policy; 1 - follow the instance lifecycle until the instance is eliminated. The default value is 0.
        :rtype: int
        """
        return self._StorageStrategy

    @StorageStrategy.setter
    def StorageStrategy(self, StorageStrategy):
        self._StorageStrategy = StorageStrategy


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
        self._StorageStrategy = params.get("StorageStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupsResponse(AbstractModel):
    r"""DescribeBackups response structure.

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
        r"""Total number of backups
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Backups(self):
        r"""Backup list details
        :rtype: list of Backup
        """
        return self._Backups

    @Backups.setter
    def Backups(self, Backups):
        self._Backups = Backups

    @property
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
        if params.get("Backups") is not None:
            self._Backups = []
            for item in params.get("Backups"):
                obj = Backup()
                obj._deserialize(item)
                self._Backups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBusinessIntelligenceFileRequest(AbstractModel):
    r"""DescribeBusinessIntelligenceFile request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileName(self):
        r"""File name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def StatusSet(self):
        r"""Migration task status set. Valid values: `1` (Initialize to be deployed), `2` (Deploying), `3` (Deployment successful), `4` (Deployment failed)
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def FileType(self):
        r"""File type. Valid values: `FLAT` (flat files), `SSIS` (project file for business intelligence service).
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Limit(self):
        r"""The maximum number of results returned per page. Value range: 1-100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sorting field. Valid values: `file_name`, `create_time`, `start_time`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order: Valid values: `desc`, `asc`.
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
    r"""DescribeBusinessIntelligenceFile response structure.

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
        r"""Total number of file deployment tasks
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupMigrationSet(self):
        r"""File deployment task set
        :rtype: list of BusinessIntelligenceFile
        """
        return self._BackupMigrationSet

    @BackupMigrationSet.setter
    def BackupMigrationSet(self, BackupMigrationSet):
        self._BackupMigrationSet = BackupMigrationSet

    @property
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
        if params.get("BackupMigrationSet") is not None:
            self._BackupMigrationSet = []
            for item in params.get("BackupMigrationSet"):
                obj = BusinessIntelligenceFile()
                obj._deserialize(item)
                self._BackupMigrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCollationTimeZoneRequest(AbstractModel):
    r"""DescribeCollationTimeZone request structure.

    """

    def __init__(self):
        r"""
        :param _MachineType: Host type of the purchased instance. PM: physical server; CLOUD_PREMIUM: CVM with Premium Cloud Disk;
CLOUD_SSD: CVM with Cloud SSD; CLOUD_HSSD: CVM with Enhanced SSD; CLOUD_TSSD: CVM with Tremendous SSD; CLOUD_BSSD: CVM with Balanced SSD; CLOUD_BASIC: CVM with cloud disk. PM is set as the default value.
        :type MachineType: str
        :param _DBVersion: Version number of the purchased instance.
        :type DBVersion: str
        """
        self._MachineType = None
        self._DBVersion = None

    @property
    def MachineType(self):
        r"""Host type of the purchased instance. PM: physical server; CLOUD_PREMIUM: CVM with Premium Cloud Disk;
CLOUD_SSD: CVM with Cloud SSD; CLOUD_HSSD: CVM with Enhanced SSD; CLOUD_TSSD: CVM with Tremendous SSD; CLOUD_BSSD: CVM with Balanced SSD; CLOUD_BASIC: CVM with cloud disk. PM is set as the default value.
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def DBVersion(self):
        r"""Version number of the purchased instance.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._DBVersion = params.get("DBVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCollationTimeZoneResponse(AbstractModel):
    r"""DescribeCollationTimeZone response structure.

    """

    def __init__(self):
        r"""
        :param _Collation: System character set collation list.
        :type Collation: list of str
        :param _TimeZone: System time zone list.
        :type TimeZone: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Collation = None
        self._TimeZone = None
        self._RequestId = None

    @property
    def Collation(self):
        r"""System character set collation list.
        :rtype: list of str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def TimeZone(self):
        r"""System time zone list.
        :rtype: list of str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Collation = params.get("Collation")
        self._TimeZone = params.get("TimeZone")
        self._RequestId = params.get("RequestId")


class DescribeCrossBackupStatisticalRequest(AbstractModel):
    r"""DescribeCrossBackupStatistical request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination number.

        :type Offset: int
        :param _Limit: Pagination size.

        :type Limit: int
        :param _InstanceIdSet: Instance ID list.

        :type InstanceIdSet: list of str
        :param _InstanceNameSet: Instance name list.
        :type InstanceNameSet: list of str
        :param _CrossBackupStatus: Cross-region backup status. enable: enabled; disable: disabled.
        :type CrossBackupStatus: str
        :param _CrossRegion: Target region for cross-region backups.
        :type CrossRegion: str
        :param _OrderBy: Sorting field. The default value is default, which indicates sorting by backup space in descending order. data - sort by data backup; log - sort by log backup.
        :type OrderBy: str
        :param _OrderByType: Collation rule (desc - descending order; asc - ascending order). The default value is desc.
        :type OrderByType: str
        """
        self._Offset = None
        self._Limit = None
        self._InstanceIdSet = None
        self._InstanceNameSet = None
        self._CrossBackupStatus = None
        self._CrossRegion = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def Offset(self):
        r"""Pagination number.

        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination size.

        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceIdSet(self):
        r"""Instance ID list.

        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def InstanceNameSet(self):
        r"""Instance name list.
        :rtype: list of str
        """
        return self._InstanceNameSet

    @InstanceNameSet.setter
    def InstanceNameSet(self, InstanceNameSet):
        self._InstanceNameSet = InstanceNameSet

    @property
    def CrossBackupStatus(self):
        r"""Cross-region backup status. enable: enabled; disable: disabled.
        :rtype: str
        """
        return self._CrossBackupStatus

    @CrossBackupStatus.setter
    def CrossBackupStatus(self, CrossBackupStatus):
        self._CrossBackupStatus = CrossBackupStatus

    @property
    def CrossRegion(self):
        r"""Target region for cross-region backups.
        :rtype: str
        """
        return self._CrossRegion

    @CrossRegion.setter
    def CrossRegion(self, CrossRegion):
        self._CrossRegion = CrossRegion

    @property
    def OrderBy(self):
        r"""Sorting field. The default value is default, which indicates sorting by backup space in descending order. data - sort by data backup; log - sort by log backup.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Collation rule (desc - descending order; asc - ascending order). The default value is desc.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._InstanceNameSet = params.get("InstanceNameSet")
        self._CrossBackupStatus = params.get("CrossBackupStatus")
        self._CrossRegion = params.get("CrossRegion")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCrossBackupStatisticalResponse(AbstractModel):
    r"""DescribeCrossBackupStatistical response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Real-time statistics on the total number of cross-region backup overview data entries.
        :type TotalCount: int
        :param _Items: Real-time statistics list of cross-region backups.
        :type Items: list of CrossSummaryDetailRes
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Real-time statistics on the total number of cross-region backup overview data entries.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""Real-time statistics list of cross-region backups.
        :rtype: list of CrossSummaryDetailRes
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
                obj = CrossSummaryDetailRes()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCrossRegionZoneRequest(AbstractModel):
    r"""DescribeCrossRegionZone request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-3l3fgqn7.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-3l3fgqn7.
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
        


class DescribeCrossRegionZoneResponse(AbstractModel):
    r"""DescribeCrossRegionZone response structure.

    """

    def __init__(self):
        r"""
        :param _Region: String ID of the region where the secondary node is located, in the format of ap-guangzhou.
        :type Region: str
        :param _Zone: String ID of the AZ where the secondary node is located, in the format of ap-guangzhou-1.
        :type Zone: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Region = None
        self._Zone = None
        self._RequestId = None

    @property
    def Region(self):
        r"""String ID of the region where the secondary node is located, in the format of ap-guangzhou.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""String ID of the AZ where the secondary node is located, in the format of ap-guangzhou-1.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._RequestId = params.get("RequestId")


class DescribeCrossRegionsRequest(AbstractModel):
    r"""DescribeCrossRegions request structure.

    """


class DescribeCrossRegionsResponse(AbstractModel):
    r"""DescribeCrossRegions response structure.

    """

    def __init__(self):
        r"""
        :param _Regions: Collection of target regions that support cross-region backups.
        :type Regions: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Regions = None
        self._RequestId = None

    @property
    def Regions(self):
        r"""Collection of target regions that support cross-region backups.
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Regions = params.get("Regions")
        self._RequestId = params.get("RequestId")


class DescribeDBCharsetsRequest(AbstractModel):
    r"""DescribeDBCharsets request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID in the format of mssql-j8kv137v
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
    r"""DescribeDBCharsets response structure.

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
        r"""Database character set list
        :rtype: list of str
        """
        return self._DatabaseCharsets

    @DatabaseCharsets.setter
    def DatabaseCharsets(self, DatabaseCharsets):
        self._DatabaseCharsets = DatabaseCharsets

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeDBInstanceInter request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The maximum number of results returned per page. Value range: 1-100.
        :type Limit: int
        :param _InstanceId: Filter by instance ID.
        :type InstanceId: str
        :param _Status: Filter by status. Valid values: `1` (Enabling interworking IP), `2` (Enabled interworking IP), `3` (Adding to interworking group), `4` (Added to interworking group), `5` (Reclaiming interworking IP), `6` (Reclaimed interworking IP), `7` (Removing from interworking group), `8` (Removed from interworking group).
        :type Status: int
        :param _VersionSet: The list of instance version numbers.
        :type VersionSet: list of str
        :param _Zone: Instance AZ ID in the format of ap-guangzhou-3.
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
        r"""The maximum number of results returned per page. Value range: 1-100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        r"""Filter by instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        r"""Filter by status. Valid values: `1` (Enabling interworking IP), `2` (Enabled interworking IP), `3` (Adding to interworking group), `4` (Added to interworking group), `5` (Reclaiming interworking IP), `6` (Reclaimed interworking IP), `7` (Removing from interworking group), `8` (Removed from interworking group).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VersionSet(self):
        r"""The list of instance version numbers.
        :rtype: list of str
        """
        return self._VersionSet

    @VersionSet.setter
    def VersionSet(self, VersionSet):
        self._VersionSet = VersionSet

    @property
    def Zone(self):
        r"""Instance AZ ID in the format of ap-guangzhou-3.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Offset(self):
        r"""Page number. Default value: `0`.
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
    r"""DescribeDBInstanceInter response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of records returned.
        :type TotalCount: int
        :param _InterInstanceSet: Details of instance in the interworking group.
        :type InterInstanceSet: list of InterInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InterInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of records returned.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InterInstanceSet(self):
        r"""Details of instance in the interworking group.
        :rtype: list of InterInstance
        """
        return self._InterInstanceSet

    @InterInstanceSet.setter
    def InterInstanceSet(self, InterInstanceSet):
        self._InterInstanceSet = InterInstanceSet

    @property
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
        if params.get("InterInstanceSet") is not None:
            self._InterInstanceSet = []
            for item in params.get("InterInstanceSet"):
                obj = InterInstance()
                obj._deserialize(item)
                self._InterInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesAttributeRequest(AbstractModel):
    r"""DescribeDBInstancesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID
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
    r"""DescribeDBInstancesAttribute response structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RegularBackupEnable(self):
        r"""Archive backup status. Valid values: `enable` (enabled), `disable` (disabled)
        :rtype: str
        """
        return self._RegularBackupEnable

    @RegularBackupEnable.setter
    def RegularBackupEnable(self, RegularBackupEnable):
        self._RegularBackupEnable = RegularBackupEnable

    @property
    def RegularBackupSaveDays(self):
        r"""Archive backup retention period: [90-3650] days
        :rtype: int
        """
        return self._RegularBackupSaveDays

    @RegularBackupSaveDays.setter
    def RegularBackupSaveDays(self, RegularBackupSaveDays):
        self._RegularBackupSaveDays = RegularBackupSaveDays

    @property
    def RegularBackupStrategy(self):
        r"""Archive backup policy. Valid values: `years` (yearly); `quarters (quarterly); `months` (monthly).
        :rtype: str
        """
        return self._RegularBackupStrategy

    @RegularBackupStrategy.setter
    def RegularBackupStrategy(self, RegularBackupStrategy):
        self._RegularBackupStrategy = RegularBackupStrategy

    @property
    def RegularBackupCounts(self):
        r"""The number of retained archive backups
        :rtype: int
        """
        return self._RegularBackupCounts

    @RegularBackupCounts.setter
    def RegularBackupCounts(self, RegularBackupCounts):
        self._RegularBackupCounts = RegularBackupCounts

    @property
    def RegularBackupStartTime(self):
        r"""Archive backup start date in YYYY-MM-DD format, which is the current time by default.
        :rtype: str
        """
        return self._RegularBackupStartTime

    @RegularBackupStartTime.setter
    def RegularBackupStartTime(self, RegularBackupStartTime):
        self._RegularBackupStartTime = RegularBackupStartTime

    @property
    def BlockedThreshold(self):
        r"""Block process threshold in milliseconds
        :rtype: int
        """
        return self._BlockedThreshold

    @BlockedThreshold.setter
    def BlockedThreshold(self, BlockedThreshold):
        self._BlockedThreshold = BlockedThreshold

    @property
    def EventSaveDays(self):
        r"""Retention period for the files of slow SQL, blocking, deadlock, and extended events.
        :rtype: int
        """
        return self._EventSaveDays

    @EventSaveDays.setter
    def EventSaveDays(self, EventSaveDays):
        self._EventSaveDays = EventSaveDays

    @property
    def TDEConfig(self):
        r"""TDE configuration
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.TDEConfigAttribute`
        """
        return self._TDEConfig

    @TDEConfig.setter
    def TDEConfig(self, TDEConfig):
        self._TDEConfig = TDEConfig

    @property
    def SSLConfig(self):
        r"""
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.SSLConfig`
        """
        return self._SSLConfig

    @SSLConfig.setter
    def SSLConfig(self, SSLConfig):
        self._SSLConfig = SSLConfig

    @property
    def DrReadableInfo(self):
        r"""
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DrReadableInfo`
        """
        return self._DrReadableInfo

    @DrReadableInfo.setter
    def DrReadableInfo(self, DrReadableInfo):
        self._DrReadableInfo = DrReadableInfo

    @property
    def OldVipList(self):
        r"""
        :rtype: list of OldVip
        """
        return self._OldVipList

    @OldVipList.setter
    def OldVipList(self, OldVipList):
        self._OldVipList = OldVipList

    @property
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
    r"""DescribeDBInstances request structure.

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
        :param _Zone: Instance availability zone, such as ap-guangzhou-3
        :type Zone: str
        :param _TagKeys: The list of instance tags
        :type TagKeys: list of str
        :param _SearchKey: Keyword used for fuzzy match, including instance ID, instance name, and instance private IP
        :type SearchKey: str
        :param _UidSet: Unique Uid of an instance
        :type UidSet: list of str
        :param _InstanceType: Instance type. HA: high-availability instance; RO: read-only instance; SI: basic edition instance; BI: business intelligence service instance; cvmHA: dual-server high-availability instance with cloud disk; cvmRO: read-only instance with cloud disk; MultiHA: multi-node instance; cvmMultiHA: multi-node instance with cloud disk.
        :type InstanceType: str
        :param _PaginationType: Pagination query method. offset - pagination query by offset; pageNumber - pagination query by number of pages. The default value is pageNumber.
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
        r"""Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        r"""Instance status. Valid values:
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
        r"""Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results per page. Value range: 1-100. Default value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceIdSet(self):
        r"""One or more instance IDs in the format of mssql-si2823jyl
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def PayMode(self):
        r"""Retrieves billing type. 0: pay-as-you-go
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def VpcId(self):
        r"""Unique string-type ID of instance VPC in the format of `vpc-xxx`. If an empty string ("") is passed in, filtering will be made by basic network.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Unique string-type ID of instance subnet in the format of `subnet-xxx`. If an empty string ("") is passed in, filtering will be made by basic network.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VipSet(self):
        r"""The list of instance private IPs, such as 172.1.0.12
        :rtype: list of str
        """
        return self._VipSet

    @VipSet.setter
    def VipSet(self, VipSet):
        self._VipSet = VipSet

    @property
    def InstanceNameSet(self):
        r"""The list of instance names used for fuzzy match
        :rtype: list of str
        """
        return self._InstanceNameSet

    @InstanceNameSet.setter
    def InstanceNameSet(self, InstanceNameSet):
        self._InstanceNameSet = InstanceNameSet

    @property
    def VersionSet(self):
        r"""The list of instance version numbers, such as 2008R2, 2012SP3
        :rtype: list of str
        """
        return self._VersionSet

    @VersionSet.setter
    def VersionSet(self, VersionSet):
        self._VersionSet = VersionSet

    @property
    def Zone(self):
        r"""Instance availability zone, such as ap-guangzhou-3
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def TagKeys(self):
        r"""The list of instance tags
        :rtype: list of str
        """
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def SearchKey(self):
        r"""Keyword used for fuzzy match, including instance ID, instance name, and instance private IP
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def UidSet(self):
        r"""Unique Uid of an instance
        :rtype: list of str
        """
        return self._UidSet

    @UidSet.setter
    def UidSet(self, UidSet):
        self._UidSet = UidSet

    @property
    def InstanceType(self):
        r"""Instance type. HA: high-availability instance; RO: read-only instance; SI: basic edition instance; BI: business intelligence service instance; cvmHA: dual-server high-availability instance with cloud disk; cvmRO: read-only instance with cloud disk; MultiHA: multi-node instance; cvmMultiHA: multi-node instance with cloud disk.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PaginationType(self):
        r"""Pagination query method. offset - pagination query by offset; pageNumber - pagination query by number of pages. The default value is pageNumber.
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
    r"""DescribeDBInstances response structure.

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
        r"""Total number of eligible instances. If the results are returned in multiple pages, this value will be the number of all eligible instances but not the number of instances returned according to the current values of `Limit` and `Offset`
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstances(self):
        r"""Instance list
        :rtype: list of DBInstance
        """
        return self._DBInstances

    @DBInstances.setter
    def DBInstances(self, DBInstances):
        self._DBInstances = DBInstances

    @property
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
        if params.get("DBInstances") is not None:
            self._DBInstances = []
            for item in params.get("DBInstances"):
                obj = DBInstance()
                obj._deserialize(item)
                self._DBInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBPrivilegeByAccountRequest(AbstractModel):
    r"""DescribeDBPrivilegeByAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-njj2mtpl.
        :type InstanceId: str
        :param _AccountName: Account name.
        :type AccountName: str
        :param _DBName: Database name associated with the account.
        :type DBName: str
        :param _Limit: The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 20.
        :type Limit: int
        :param _Offset: Page number in pagination mode. The default value is 0.
        :type Offset: int
        """
        self._InstanceId = None
        self._AccountName = None
        self._DBName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-njj2mtpl.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        r"""Account name.
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def DBName(self):
        r"""Database name associated with the account.
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Limit(self):
        r"""The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number in pagination mode. The default value is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._DBName = params.get("DBName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPrivilegeByAccountResponse(AbstractModel):
    r"""DescribeDBPrivilegeByAccount response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of databases.
        :type TotalCount: int
        :param _DBList: Database permission list.
        :type DBList: list of DBPrivilege
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of databases.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBList(self):
        r"""Database permission list.
        :rtype: list of DBPrivilege
        """
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

    @property
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
        if params.get("DBList") is not None:
            self._DBList = []
            for item in params.get("DBList"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self._DBList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBRestoreTimeRequest(AbstractModel):
    r"""DescribeDBRestoreTime request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Original instance ID.
        :type InstanceId: str
        :param _TargetInstanceId: ID of the target instance for rollback. If this parameter is left unspecified, roll back to the original instance by default.
        :type TargetInstanceId: str
        :param _Time: Queries databases that can be rolled back by time point, with the time format of YYYY-MM-DD HH:MM:SS. Either BackupId or Time should be specified, as they cannot be empty simultaneously.
        :type Time: str
        :param _BackupId: Queries databases that can be rolled back by backup set ID, which can be obtained through the DescribeBackups API. Either BackupId or Time should be specified, as they cannot be empty simultaneously.
        :type BackupId: int
        :param _DBName: Database name.
        :type DBName: str
        """
        self._InstanceId = None
        self._TargetInstanceId = None
        self._Time = None
        self._BackupId = None
        self._DBName = None

    @property
    def InstanceId(self):
        r"""Original instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TargetInstanceId(self):
        r"""ID of the target instance for rollback. If this parameter is left unspecified, roll back to the original instance by default.
        :rtype: str
        """
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def Time(self):
        r"""Queries databases that can be rolled back by time point, with the time format of YYYY-MM-DD HH:MM:SS. Either BackupId or Time should be specified, as they cannot be empty simultaneously.
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def BackupId(self):
        r"""Queries databases that can be rolled back by backup set ID, which can be obtained through the DescribeBackups API. Either BackupId or Time should be specified, as they cannot be empty simultaneously.
        :rtype: int
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def DBName(self):
        r"""Database name.
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TargetInstanceId = params.get("TargetInstanceId")
        self._Time = params.get("Time")
        self._BackupId = params.get("BackupId")
        self._DBName = params.get("DBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBRestoreTimeResponse(AbstractModel):
    r"""DescribeDBRestoreTime response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of databases that can be rolled back.
        :type TotalCount: int
        :param _Details: List of databases that can be rolled back.
        :type Details: list of DBRenameRes
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of databases that can be rolled back.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        r"""List of databases that can be rolled back.
        :rtype: list of DBRenameRes
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
                obj = DBRenameRes()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    r"""DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-c1nl9rpv or mssqlro-c1nl9rpv, which is the same as that displayed on the cloud database console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-c1nl9rpv or mssqlro-c1nl9rpv, which is the same as that displayed on the cloud database console page.
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
        :param _SecurityGroupSet: Security group details.
        :type SecurityGroupSet: list of SecurityGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityGroupSet = None
        self._RequestId = None

    @property
    def SecurityGroupSet(self):
        r"""Security group details.
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


class DescribeDBsNormalRequest(AbstractModel):
    r"""DescribeDBsNormal request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-7vfv3rk3
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID in the format of mssql-7vfv3rk3
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
    r"""DescribeDBsNormal response structure.

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
        r"""Total number of databases of the instance
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBList(self):
        r"""Detailed database configurations, such as whether CDC or CT is enabled for the database
        :rtype: list of DbNormalDetail
        """
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

    @property
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
        if params.get("DBList") is not None:
            self._DBList = []
            for item in params.get("DBList"):
                obj = DbNormalDetail()
                obj._deserialize(item)
                self._DBList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBsRequest(AbstractModel):
    r"""DescribeDBs request structure.

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
        r"""Instance ID
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def Limit(self):
        r"""Number of results per page. Value range: 1-100. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Name(self):
        r"""Database name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OrderByType(self):
        r"""Sorting rule. Valid values: `desc` (descending order), `asc` (ascending order). Default value: `desc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Encryption(self):
        r"""TDE status. Valid values: `enable` (enabled), `disable` (disabled).
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
    r"""DescribeDBs response structure.

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
        r"""Number of databases
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstances(self):
        r"""List of instance databases
        :rtype: list of InstanceDBDetail
        """
        return self._DBInstances

    @DBInstances.setter
    def DBInstances(self, DBInstances):
        self._DBInstances = DBInstances

    @property
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
        if params.get("DBInstances") is not None:
            self._DBInstances = []
            for item in params.get("DBInstances"):
                obj = InstanceDBDetail()
                obj._deserialize(item)
                self._DBInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseNamesRequest(AbstractModel):
    r"""DescribeDatabaseNames request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-rljoi3bf.
        :type InstanceId: str
        :param _AccountName: Account name.
        :type AccountName: str
        """
        self._InstanceId = None
        self._AccountName = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-rljoi3bf.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        r"""Account name.
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseNamesResponse(AbstractModel):
    r"""DescribeDatabaseNames response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of databases associated with the account.
        :type TotalCount: int
        :param _DatabaseNameSet: Database name set.
        :type DatabaseNameSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DatabaseNameSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of databases associated with the account.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DatabaseNameSet(self):
        r"""Database name set.
        :rtype: list of str
        """
        return self._DatabaseNameSet

    @DatabaseNameSet.setter
    def DatabaseNameSet(self, DatabaseNameSet):
        self._DatabaseNameSet = DatabaseNameSet

    @property
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
        self._DatabaseNameSet = params.get("DatabaseNameSet")
        self._RequestId = params.get("RequestId")


class DescribeDatabasesNormalRequest(AbstractModel):
    r"""DescribeDatabasesNormal request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-7vfv3rk3.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-7vfv3rk3.
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
        


class DescribeDatabasesNormalResponse(AbstractModel):
    r"""DescribeDatabasesNormal response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Indicates the total number of databases under the current instance.
        :type TotalCount: int
        :param _DBList: Returns detailed configuration information of the databases, such as whether CDC and CT are enabled for the databases.
        :type DBList: list of DbNormalDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Indicates the total number of databases under the current instance.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBList(self):
        r"""Returns detailed configuration information of the databases, such as whether CDC and CT are enabled for the databases.
        :rtype: list of DbNormalDetail
        """
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

    @property
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
        if params.get("DBList") is not None:
            self._DBList = []
            for item in params.get("DBList"):
                obj = DbNormalDetail()
                obj._deserialize(item)
                self._DBList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    r"""DescribeDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: Instance ID
        :type InstanceIdSet: list of str
        :param _Limit: The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 20.
        :type Limit: int
        :param _Offset: Page number in pagination mode. The default value is 0.
        :type Offset: int
        :param _Name: Database name.
        :type Name: str
        :param _OrderByType: Collation rule (desc - descending order; asc - ascending order). The default value is desc.
        :type OrderByType: str
        :param _Encryption: Whether TDE encryption is enabled. enable - encrypted; disable - unencrypted.
        :type Encryption: str
        :param _OrderBy: Sorting field. (Name - sort by name; CreateTime - sort by creation time). The default value is CreateTime.
        :type OrderBy: str
        """
        self._InstanceIdSet = None
        self._Limit = None
        self._Offset = None
        self._Name = None
        self._OrderByType = None
        self._Encryption = None
        self._OrderBy = None

    @property
    def InstanceIdSet(self):
        r"""Instance ID
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def Limit(self):
        r"""The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number in pagination mode. The default value is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Name(self):
        r"""Database name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OrderByType(self):
        r"""Collation rule (desc - descending order; asc - ascending order). The default value is desc.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Encryption(self):
        r"""Whether TDE encryption is enabled. enable - encrypted; disable - unencrypted.
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def OrderBy(self):
        r"""Sorting field. (Name - sort by name; CreateTime - sort by creation time). The default value is CreateTime.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Name = params.get("Name")
        self._OrderByType = params.get("OrderByType")
        self._Encryption = params.get("Encryption")
        self._OrderBy = params.get("OrderBy")
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
        :param _TotalCount: Number of databases.
        :type TotalCount: int
        :param _DBInstances: Instance database list.
        :type DBInstances: list of InstanceDBDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DBInstances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of databases.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DBInstances(self):
        r"""Instance database list.
        :rtype: list of InstanceDBDetail
        """
        return self._DBInstances

    @DBInstances.setter
    def DBInstances(self, DBInstances):
        self._DBInstances = DBInstances

    @property
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
        if params.get("DBInstances") is not None:
            self._DBInstances = []
            for item in params.get("DBInstances"):
                obj = InstanceDBDetail()
                obj._deserialize(item)
                self._DBInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowStatusRequest(AbstractModel):
    r"""DescribeFlowStatus request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        r"""Flow ID
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
    r"""DescribeFlowStatus response structure.

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
        r"""Flow status. 0: succeeded, 1: failed, 2: running
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeHASwitchLogRequest(AbstractModel):
    r"""DescribeHASwitchLog request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time (yyyy-MM-dd HH:mm:ss).
        :type StartTime: str
        :param _EndTime: End time (yyyy-MM-dd HH:mm:ss).
        :type EndTime: str
        :param _SwitchType: Switch mode. 0 - system automatic switch; 1 - manual switch. Check all switch modes by default if the parameter is left unspecified.
        :type SwitchType: int
        :param _Limit: Pagination size.
        :type Limit: int
        :param _Offset: Pagination number.
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SwitchType = None
        self._Limit = None
        self._Offset = None

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
        r"""Start time (yyyy-MM-dd HH:mm:ss).
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time (yyyy-MM-dd HH:mm:ss).
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SwitchType(self):
        r"""Switch mode. 0 - system automatic switch; 1 - manual switch. Check all switch modes by default if the parameter is left unspecified.
        :rtype: int
        """
        return self._SwitchType

    @SwitchType.setter
    def SwitchType(self, SwitchType):
        self._SwitchType = SwitchType

    @property
    def Limit(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination number.
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
        self._SwitchType = params.get("SwitchType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHASwitchLogResponse(AbstractModel):
    r"""DescribeHASwitchLog response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of logs.
        :type TotalCount: int
        :param _SwitchLog: Primary-secondary switch logs.
        :type SwitchLog: list of SwitchLog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SwitchLog = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of logs.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SwitchLog(self):
        r"""Primary-secondary switch logs.
        :rtype: list of SwitchLog
        """
        return self._SwitchLog

    @SwitchLog.setter
    def SwitchLog(self, SwitchLog):
        self._SwitchLog = SwitchLog

    @property
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
        if params.get("SwitchLog") is not None:
            self._SwitchLog = []
            for item in params.get("SwitchLog"):
                obj = SwitchLog()
                obj._deserialize(item)
                self._SwitchLog.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIncrementalMigrationRequest(AbstractModel):
    r"""DescribeIncrementalMigration request structure.

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
        r"""Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def InstanceId(self):
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupFileName(self):
        r"""Backup file name
        :rtype: str
        """
        return self._BackupFileName

    @BackupFileName.setter
    def BackupFileName(self, BackupFileName):
        self._BackupFileName = BackupFileName

    @property
    def StatusSet(self):
        r"""Status set of import tasks
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def Limit(self):
        r"""The maximum number of results returned per page. Default value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sort by field. Valid values: `name`, `createTime`, `startTime`, `endTime`. By default, the results returned are sorted by `createTime` in the ascending order.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order which is valid only when `OrderBy` is specified. Valid values: `asc` (ascending), `desc` (descending). Default value: `asc`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def IncrementalMigrationId(self):
        r"""Incremental backup import task ID, which is returned through the `CreateIncrementalMigration` API.
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
    r"""DescribeIncrementalMigration response structure.

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
        r"""Total number of import tasks
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IncrementalMigrationSet(self):
        r"""Incremental import task set
        :rtype: list of Migration
        """
        return self._IncrementalMigrationSet

    @IncrementalMigrationSet.setter
    def IncrementalMigrationSet(self, IncrementalMigrationSet):
        self._IncrementalMigrationSet = IncrementalMigrationSet

    @property
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
        if params.get("IncrementalMigrationSet") is not None:
            self._IncrementalMigrationSet = []
            for item in params.get("IncrementalMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self._IncrementalMigrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceByOrdersRequest(AbstractModel):
    r"""DescribeInstanceByOrders request structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order ID set
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        r"""Order ID set
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
    r"""DescribeInstanceByOrders response structure.

    """

    def __init__(self):
        r"""
        :param _DealInstance: Resource ID set.
        :type DealInstance: list of DealInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealInstance = None
        self._RequestId = None

    @property
    def DealInstance(self):
        r"""Resource ID set.
        :rtype: list of DealInstance
        """
        return self._DealInstance

    @DealInstance.setter
    def DealInstance(self, DealInstance):
        self._DealInstance = DealInstance

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeInstanceParamRecords request structure.

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
        r"""Instance ID in the format of mssql-dj5i29c5n. It is the same as the instance ID displayed in the TencentDB console and the response parameter `InstanceId` of the `DescribeDBInstances` API.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""Page number. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""The maximum number of results returned per page. Maximum value: `100`. Default value: `20`.
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
    r"""DescribeInstanceParamRecords response structure.

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
        r"""Number of eligible records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""Parameter modification records
        :rtype: list of ParamRecord
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
                obj = ParamRecord()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    r"""DescribeInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-dj5i29c5n. It is the same as the instance ID displayed in the TencentDB console and the response parameter `InstanceId` of the `DescribeDBInstances` API.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID in the format of mssql-dj5i29c5n. It is the same as the instance ID displayed in the TencentDB console and the response parameter `InstanceId` of the `DescribeDBInstances` API.
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
    r"""DescribeInstanceParams response structure.

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
        r"""Total number of instance parameters
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""Parameter details
        :rtype: list of ParameterDetail
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
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTasksRequest(AbstractModel):
    r"""DescribeInstanceTasks request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID, in the format of mssql-njj2mtpl.
        :type InstanceId: str
        :param _Limit: Pagination size.
        :type Limit: int
        :param _Status: Asynchronous task status. 1 - running; 2 - running successful; 3 - running failed.
        :type Status: int
        :param _Offset: Pagination offset.
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Status = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""Database instance ID, in the format of mssql-njj2mtpl.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        r"""Asynchronous task status. 1 - running; 2 - running successful; 3 - running failed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        r"""Pagination offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTasksResponse(AbstractModel):
    r"""DescribeInstanceTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of asynchronous tasks.
        :type TotalCount: int
        :param _InstanceTaskSet: Asynchronous task information array.
        :type InstanceTaskSet: list of InstanceTask
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceTaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of asynchronous tasks.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceTaskSet(self):
        r"""Asynchronous task information array.
        :rtype: list of InstanceTask
        """
        return self._InstanceTaskSet

    @InstanceTaskSet.setter
    def InstanceTaskSet(self, InstanceTaskSet):
        self._InstanceTaskSet = InstanceTaskSet

    @property
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
        if params.get("InstanceTaskSet") is not None:
            self._InstanceTaskSet = []
            for item in params.get("InstanceTaskSet"):
                obj = InstanceTask()
                obj._deserialize(item)
                self._InstanceTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTradeParameterRequest(AbstractModel):
    r"""DescribeInstanceTradeParameter request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API.
        :type Zone: str
        :param _Cpu: Number of CPU cores.
        :type Cpu: int
        :param _Memory: Instance memory size in GB.
        :type Memory: int
        :param _Storage: Instance storage capacity in GB.
        :type Storage: int
        :param _InstanceType: Type of purchased instances. HA: high-availability edition (including dual-server high-availability edition and Always On cluster edition); RO: read-only replica edition; SI: single-node edition; BI: business intelligence edition; cvmHA: new high-availability edition; cvmRO: new read-only replica edition; MultiHA: multi-node edition; cvmMultiHA: multi-node cloud disk edition.
        :type InstanceType: str
        :param _MachineType: Host disk type of purchased instances. CLOUD_HSSD - Enhanced SSD for CVMs, CLOUD_TSSD - Tremendous SSD for CVMs, CLOUD_BSSD - Balanced SSD for CVMs. 
        :type MachineType: str
        :param _InstanceChargeType: Billing mode. Valid value: POSTPAID (pay-as-you-go).
        :type InstanceChargeType: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _GoodsNum: Number of instances purchased this time. Default value: 1. Maximum value: 10.
        :type GoodsNum: int
        :param _DBVersion: SQL Server version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The available version varies by region, and you can pull the version information by calling the `DescribeProductConfig` API.
        :type DBVersion: str
        :param _SubnetId: VPC subnet ID in the format of subnet-bdoe83fa. `SubnetId` and `VpcId` should be set or ignored simultaneously.
        :type SubnetId: str
        :param _VpcId: VPC ID in the format of vpc-dsp338hz. `SubnetId` and `VpcId` should be set or ignored simultaneously.
        :type VpcId: str
        :param _Period: Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48.
        :type Period: int
        :param _SecurityGroupList: Security group list, which contains security group IDs in the format of sg-xxx.
        :type SecurityGroupList: list of str
        :param _AutoRenewFlag: Auto-renewal flag. 0: normal renewal, 1: auto-renewal. Default value: 1.
        :type AutoRenewFlag: int
        :param _Weekly: Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: 1 (Monday), 2 (Tuesday), 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday).
        :type Weekly: list of int
        :param _StartTime: Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :type StartTime: str
        :param _Span: Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :type Span: int
        :param _MultiZones: Whether to deploy across availability zones. Default value: false.
        :type MultiZones: bool
        :param _ResourceTags: Tags associated with the instances to be created.
        :type ResourceTags: list of ResourceTag
        :param _TimeZone: System time zone. Default value: `China Standard Time`.
        :type TimeZone: str
        :param _Collation: Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :type Collation: str
        :param _MultiNodes: Whether it is a multi-node architecture instance. Default value: `false`.
        :type MultiNodes: bool
        :param _DrZones: The zone in which the standby node is available. Default is empty. If it is a multi-node architecture, it must be transmitted. When MultiNodes = true, the availability zones of the primary and standby nodes cannot all be the same. The minimum number of availability zones for the standby nodes is 2, and the maximum is 5.
        :type DrZones: list of str
        """
        self._Zone = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._InstanceType = None
        self._MachineType = None
        self._InstanceChargeType = None
        self._ProjectId = None
        self._GoodsNum = None
        self._DBVersion = None
        self._SubnetId = None
        self._VpcId = None
        self._Period = None
        self._SecurityGroupList = None
        self._AutoRenewFlag = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None
        self._MultiZones = None
        self._ResourceTags = None
        self._TimeZone = None
        self._Collation = None
        self._MultiNodes = None
        self._DrZones = None

    @property
    def Zone(self):
        r"""Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Cpu(self):
        r"""Number of CPU cores.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""Instance memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Instance storage capacity in GB.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceType(self):
        r"""Type of purchased instances. HA: high-availability edition (including dual-server high-availability edition and Always On cluster edition); RO: read-only replica edition; SI: single-node edition; BI: business intelligence edition; cvmHA: new high-availability edition; cvmRO: new read-only replica edition; MultiHA: multi-node edition; cvmMultiHA: multi-node cloud disk edition.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MachineType(self):
        r"""Host disk type of purchased instances. CLOUD_HSSD - Enhanced SSD for CVMs, CLOUD_TSSD - Tremendous SSD for CVMs, CLOUD_BSSD - Balanced SSD for CVMs. 
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def InstanceChargeType(self):
        r"""Billing mode. Valid value: POSTPAID (pay-as-you-go).
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

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
    def GoodsNum(self):
        r"""Number of instances purchased this time. Default value: 1. Maximum value: 10.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def DBVersion(self):
        r"""SQL Server version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), 201402 (SQL Server 2014 Standard), `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The available version varies by region, and you can pull the version information by calling the `DescribeProductConfig` API.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def SubnetId(self):
        r"""VPC subnet ID in the format of subnet-bdoe83fa. `SubnetId` and `VpcId` should be set or ignored simultaneously.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        r"""VPC ID in the format of vpc-dsp338hz. `SubnetId` and `VpcId` should be set or ignored simultaneously.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Period(self):
        r"""Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupList(self):
        r"""Security group list, which contains security group IDs in the format of sg-xxx.
        :rtype: list of str
        """
        return self._SecurityGroupList

    @SecurityGroupList.setter
    def SecurityGroupList(self, SecurityGroupList):
        self._SecurityGroupList = SecurityGroupList

    @property
    def AutoRenewFlag(self):
        r"""Auto-renewal flag. 0: normal renewal, 1: auto-renewal. Default value: 1.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Weekly(self):
        r"""Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: 1 (Monday), 2 (Tuesday), 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday).
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        r"""Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        r"""Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def MultiZones(self):
        r"""Whether to deploy across availability zones. Default value: false.
        :rtype: bool
        """
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def ResourceTags(self):
        r"""Tags associated with the instances to be created.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def TimeZone(self):
        r"""System time zone. Default value: `China Standard Time`.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def Collation(self):
        r"""Collation of system character sets. Default value: `Chinese_PRC_CI_AS`.
        :rtype: str
        """
        return self._Collation

    @Collation.setter
    def Collation(self, Collation):
        self._Collation = Collation

    @property
    def MultiNodes(self):
        r"""Whether it is a multi-node architecture instance. Default value: `false`.
        :rtype: bool
        """
        return self._MultiNodes

    @MultiNodes.setter
    def MultiNodes(self, MultiNodes):
        self._MultiNodes = MultiNodes

    @property
    def DrZones(self):
        r"""The zone in which the standby node is available. Default is empty. If it is a multi-node architecture, it must be transmitted. When MultiNodes = true, the availability zones of the primary and standby nodes cannot all be the same. The minimum number of availability zones for the standby nodes is 2, and the maximum is 5.
        :rtype: list of str
        """
        return self._DrZones

    @DrZones.setter
    def DrZones(self, DrZones):
        self._DrZones = DrZones


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceType = params.get("InstanceType")
        self._MachineType = params.get("MachineType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ProjectId = params.get("ProjectId")
        self._GoodsNum = params.get("GoodsNum")
        self._DBVersion = params.get("DBVersion")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Period = params.get("Period")
        self._SecurityGroupList = params.get("SecurityGroupList")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
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
        self._TimeZone = params.get("TimeZone")
        self._Collation = params.get("Collation")
        self._MultiNodes = params.get("MultiNodes")
        self._DrZones = params.get("DrZones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTradeParameterResponse(AbstractModel):
    r"""DescribeInstanceTradeParameter response structure.

    """

    def __init__(self):
        r"""
        :param _Parameter: Billing parameter.
        :type Parameter: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Parameter = None
        self._RequestId = None

    @property
    def Parameter(self):
        r"""Billing parameter.
        :rtype: str
        """
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Parameter = params.get("Parameter")
        self._RequestId = params.get("RequestId")


class DescribeMaintenanceSpanRequest(AbstractModel):
    r"""DescribeMaintenanceSpan request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. For example, mssql-k8voqdlz.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID. For example, mssql-k8voqdlz.
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
    r"""DescribeMaintenanceSpan response structure.

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
        r"""Specifies the days in each week allowed for maintenance. For example, [1,2,3,4,5,6,7] indicates that all days from Monday to Sunday are allowed for maintenance.
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        r"""Maintenance start time each day. For example, 10:24 indicates that the maintenance window starts at 10:24.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        r"""Maintenance duration each day, in hours. For example, 1 indicates that the duration is 1 hour after maintenance starts.
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DescribeMigrationDatabasesRequest(AbstractModel):
    r"""DescribeMigrationDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Migration source instance ID, in the format of mssql-si2823jyl.
        :type InstanceId: str
        :param _UserName: Username of the migration source instance.
        :type UserName: str
        :param _Password: Password of the migration source instance.
        :type Password: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Password = None

    @property
    def InstanceId(self):
        r"""Migration source instance ID, in the format of mssql-si2823jyl.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        r"""Username of the migration source instance.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""Password of the migration source instance.
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
        


class DescribeMigrationDatabasesResponse(AbstractModel):
    r"""DescribeMigrationDatabases response structure.

    """

    def __init__(self):
        r"""
        :param _Amount: Number of databases.
        :type Amount: int
        :param _MigrateDBSet: Database name array.
        :type MigrateDBSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Amount = None
        self._MigrateDBSet = None
        self._RequestId = None

    @property
    def Amount(self):
        r"""Number of databases.
        :rtype: int
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def MigrateDBSet(self):
        r"""Database name array.
        :rtype: list of str
        """
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Amount = params.get("Amount")
        self._MigrateDBSet = params.get("MigrateDBSet")
        self._RequestId = params.get("RequestId")


class DescribeMigrationDetailRequest(AbstractModel):
    r"""DescribeMigrationDetail request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        r"""Migration task ID
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
    r"""DescribeMigrationDetail response structure.

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
        r"""Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def MigrateName(self):
        r"""Migration task name
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def AppId(self):
        r"""User ID of migration task
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        r"""Migration task region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SourceType(self):
        r"""Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def CreateTime(self):
        r"""Migration task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        r"""Migration task start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Migration task end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""Migration task status (1: initializing, 4: migrating, 5: migration failed, 6: migration succeeded)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        r"""Migration task progress
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def MigrateType(self):
        r"""Migration type (1: structure migration, 2: data migration, 3: incremental sync)
        :rtype: int
        """
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def Source(self):
        r"""Migration source
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""Migration target
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def MigrateDBSet(self):
        r"""Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5)
        :rtype: list of MigrateDB
        """
        return self._MigrateDBSet

    @MigrateDBSet.setter
    def MigrateDBSet(self, MigrateDBSet):
        self._MigrateDBSet = MigrateDBSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeMigrations request structure.

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
        r"""Status set. As long as a migration task is in a status therein, it will be listed
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def MigrateName(self):
        r"""Migration task name (fuzzy match)
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def Limit(self):
        r"""Number of results per page. Value range: 1-100. Default value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""The query results are sorted by keyword. Valid values: name, createTime, startTime, endTime, status
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting order. Valid values: desc, asc
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
    r"""DescribeMigrations response structure.

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
        r"""Total number of query results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MigrateTaskSet(self):
        r"""List of query results
        :rtype: list of MigrateTask
        """
        return self._MigrateTaskSet

    @MigrateTaskSet.setter
    def MigrateTaskSet(self, MigrateTaskSet):
        self._MigrateTaskSet = MigrateTaskSet

    @property
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
        if params.get("MigrateTaskSet") is not None:
            self._MigrateTaskSet = []
            for item in params.get("MigrateTaskSet"):
                obj = MigrateTask()
                obj._deserialize(item)
                self._MigrateTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    r"""DescribeOrders request structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Order array. The order name will be returned upon shipping, which can be used to call the `DescribeOrders` API to query shipment status
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        r"""Order array. The order name will be returned upon shipping, which can be used to call the `DescribeOrders` API to query shipment status
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
        r"""Order information array
        :rtype: list of DealInfo
        """
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

    @property
    def TotalCount(self):
        r"""Number of orders returned
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
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = DealInfo()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    r"""DescribeProductConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ ID in the format of ap-guangzhou-1.
        :type Zone: str
        :param _InstanceType: Type of purchased instance. Valid values: HA - local disk high availability (including dual-machine high availability, AlwaysOn Cluster), RO - local disk read-only replica, SI - cloud disk edition single node, BI - business intelligence service, cvmHA - cloud disk edition high availability, cvmRO - cloud disk edition read-only replica.
        :type InstanceType: str
        """
        self._Zone = None
        self._InstanceType = None

    @property
    def Zone(self):
        r"""AZ ID in the format of ap-guangzhou-1.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        r"""Type of purchased instance. Valid values: HA - local disk high availability (including dual-machine high availability, AlwaysOn Cluster), RO - local disk read-only replica, SI - cloud disk edition single node, BI - business intelligence service, cvmHA - cloud disk edition high availability, cvmRO - cloud disk edition read-only replica.
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
    r"""DescribeProductConfig response structure.

    """

    def __init__(self):
        r"""
        :param _SpecInfoList: Specification information array.
        :type SpecInfoList: list of SpecInfo
        :param _TotalCount: Number of date entries returned.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SpecInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SpecInfoList(self):
        r"""Specification information array.
        :rtype: list of SpecInfo
        """
        return self._SpecInfoList

    @SpecInfoList.setter
    def SpecInfoList(self, SpecInfoList):
        self._SpecInfoList = SpecInfoList

    @property
    def TotalCount(self):
        r"""Number of date entries returned.
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
        if params.get("SpecInfoList") is not None:
            self._SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self._SpecInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    r"""DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID, which can be viewed under project management in the console.
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        r"""Project ID, which can be viewed under project management in the console.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    r"""DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupSet: Security group details.
        :type SecurityGroupSet: list of SecurityGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityGroupSet = None
        self._RequestId = None

    @property
    def SecurityGroupSet(self):
        r"""Security group details.
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


class DescribePublishSubscribeRequest(AbstractModel):
    r"""DescribePublishSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. For example, mssql-j8kv137v.
        :type InstanceId: str
        :param _PubOrSubInstanceId: Publish/subscribe instance ID, which is related to whether InstanceId is a publishing instance or a subscription instance. When the value of InstanceId is a publishing instance, filtering by subscription instance ID is performed for this field. When the value of InstanceId is a subscription instance, filtering by publishing instance ID is performed for this field.
        :type PubOrSubInstanceId: str
        :param _PubOrSubInstanceIp: Private address of the publish/subscribe instance, which is related to whether InstanceId is a publishing instance or a subscription instance. When the value of InstanceId is a publishing instance, filtering by private IP address of the subscription instance is performed for this field. When the value of InstanceId is a subscription instance, filtering by private IP address of the publishing instance is performed for this field.
        :type PubOrSubInstanceIp: str
        :param _PublishSubscribeId: Publish/subscribe ID, which is used for filtering.
        :type PublishSubscribeId: int
        :param _PublishSubscribeName: Publish/subscribe name, which is used for filtering.
        :type PublishSubscribeName: str
        :param _PublishDBName: Publishing database name, which is used for filtering.
        :type PublishDBName: str
        :param _SubscribeDBName: Subscription database name, which is used for filtering.
        :type SubscribeDBName: str
        :param _Offset: Pagination number.
        :type Offset: int
        :param _Limit: Pagination size.
        :type Limit: int
        """
        self._InstanceId = None
        self._PubOrSubInstanceId = None
        self._PubOrSubInstanceIp = None
        self._PublishSubscribeId = None
        self._PublishSubscribeName = None
        self._PublishDBName = None
        self._SubscribeDBName = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""Instance ID. For example, mssql-j8kv137v.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PubOrSubInstanceId(self):
        r"""Publish/subscribe instance ID, which is related to whether InstanceId is a publishing instance or a subscription instance. When the value of InstanceId is a publishing instance, filtering by subscription instance ID is performed for this field. When the value of InstanceId is a subscription instance, filtering by publishing instance ID is performed for this field.
        :rtype: str
        """
        return self._PubOrSubInstanceId

    @PubOrSubInstanceId.setter
    def PubOrSubInstanceId(self, PubOrSubInstanceId):
        self._PubOrSubInstanceId = PubOrSubInstanceId

    @property
    def PubOrSubInstanceIp(self):
        r"""Private address of the publish/subscribe instance, which is related to whether InstanceId is a publishing instance or a subscription instance. When the value of InstanceId is a publishing instance, filtering by private IP address of the subscription instance is performed for this field. When the value of InstanceId is a subscription instance, filtering by private IP address of the publishing instance is performed for this field.
        :rtype: str
        """
        return self._PubOrSubInstanceIp

    @PubOrSubInstanceIp.setter
    def PubOrSubInstanceIp(self, PubOrSubInstanceIp):
        self._PubOrSubInstanceIp = PubOrSubInstanceIp

    @property
    def PublishSubscribeId(self):
        r"""Publish/subscribe ID, which is used for filtering.
        :rtype: int
        """
        return self._PublishSubscribeId

    @PublishSubscribeId.setter
    def PublishSubscribeId(self, PublishSubscribeId):
        self._PublishSubscribeId = PublishSubscribeId

    @property
    def PublishSubscribeName(self):
        r"""Publish/subscribe name, which is used for filtering.
        :rtype: str
        """
        return self._PublishSubscribeName

    @PublishSubscribeName.setter
    def PublishSubscribeName(self, PublishSubscribeName):
        self._PublishSubscribeName = PublishSubscribeName

    @property
    def PublishDBName(self):
        r"""Publishing database name, which is used for filtering.
        :rtype: str
        """
        return self._PublishDBName

    @PublishDBName.setter
    def PublishDBName(self, PublishDBName):
        self._PublishDBName = PublishDBName

    @property
    def SubscribeDBName(self):
        r"""Subscription database name, which is used for filtering.
        :rtype: str
        """
        return self._SubscribeDBName

    @SubscribeDBName.setter
    def SubscribeDBName(self, SubscribeDBName):
        self._SubscribeDBName = SubscribeDBName

    @property
    def Offset(self):
        r"""Pagination number.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PubOrSubInstanceId = params.get("PubOrSubInstanceId")
        self._PubOrSubInstanceIp = params.get("PubOrSubInstanceIp")
        self._PublishSubscribeId = params.get("PublishSubscribeId")
        self._PublishSubscribeName = params.get("PublishSubscribeName")
        self._PublishDBName = params.get("PublishDBName")
        self._SubscribeDBName = params.get("SubscribeDBName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublishSubscribeResponse(AbstractModel):
    r"""DescribePublishSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number.
        :type TotalCount: int
        :param _PublishSubscribeSet: Publish/subscribe list.
        :type PublishSubscribeSet: list of PublishSubscribe
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._PublishSubscribeSet = None
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
    def PublishSubscribeSet(self):
        r"""Publish/subscribe list.
        :rtype: list of PublishSubscribe
        """
        return self._PublishSubscribeSet

    @PublishSubscribeSet.setter
    def PublishSubscribeSet(self, PublishSubscribeSet):
        self._PublishSubscribeSet = PublishSubscribeSet

    @property
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
        if params.get("PublishSubscribeSet") is not None:
            self._PublishSubscribeSet = []
            for item in params.get("PublishSubscribeSet"):
                obj = PublishSubscribe()
                obj._deserialize(item)
                self._PublishSubscribeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupAutoWeightRequest(AbstractModel):
    r"""DescribeReadOnlyGroupAutoWeight request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Primary instance ID, in the format of mssql-3l3fgqn7.
        :type InstanceId: str
        :param _ReadOnlyGroupId: Read-only group ID, in the format of mssqlro-3l3fgqn7.
        :type ReadOnlyGroupId: str
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def InstanceId(self):
        r"""Primary instance ID, in the format of mssql-3l3fgqn7.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""Read-only group ID, in the format of mssqlro-3l3fgqn7.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupAutoWeightResponse(AbstractModel):
    r"""DescribeReadOnlyGroupAutoWeight response structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: Read-only group ID, in the format of mssqlro-3l3fgqn7.

        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: Read-only group name.
        :type ReadOnlyGroupName: str
        :param _RegionId: Region ID of the read-only group, which is the same as that of the primary instance.
        :type RegionId: str
        :param _ZoneId: AZ of the read-only group, which is the same as that of the primary instance.
        :type ZoneId: str
        :param _IsOfflineDelay: Whether to enable the delayed read-only instance removal feature. 1 - enabled; 0 - disabled.
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: Timeout threshold used after the delayed read-only instance removal feature is enabled, in seconds.
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: Minimum number of retained read-only replicas in the read-only group, after the delayed read-only instance removal feature is enabled.
        :type MinReadOnlyInGroup: int
        :param _Vip: Read-only group VIP.
        :type Vip: str
        :param _Vport: Read-only group VPort.
        :type Vport: int
        :param _VpcId: VPC ID of the read-only group.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID of the read-only group.
        :type SubnetId: str
        :param _ReadOnlyInstanceSet: Read-only instance replica collection.
        :type ReadOnlyInstanceSet: list of ReadOnlyInstance
        :param _Status: Read-only group status: 1 - running after successful application; 5 - applying.
        :type Status: int
        :param _MasterInstanceId: Primary instance ID. For example, mssql-sgeshe3th.
        :type MasterInstanceId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._RegionId = None
        self._ZoneId = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._ReadOnlyInstanceSet = None
        self._Status = None
        self._MasterInstanceId = None
        self._RequestId = None

    @property
    def ReadOnlyGroupId(self):
        r"""Read-only group ID, in the format of mssqlro-3l3fgqn7.

        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""Read-only group name.
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def RegionId(self):
        r"""Region ID of the read-only group, which is the same as that of the primary instance.
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""AZ of the read-only group, which is the same as that of the primary instance.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsOfflineDelay(self):
        r"""Whether to enable the delayed read-only instance removal feature. 1 - enabled; 0 - disabled.
        :rtype: int
        """
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        r"""Timeout threshold used after the delayed read-only instance removal feature is enabled, in seconds.
        :rtype: int
        """
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        r"""Minimum number of retained read-only replicas in the read-only group, after the delayed read-only instance removal feature is enabled.
        :rtype: int
        """
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def Vip(self):
        r"""Read-only group VIP.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Read-only group VPort.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        r"""VPC ID of the read-only group.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""VPC subnet ID of the read-only group.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ReadOnlyInstanceSet(self):
        r"""Read-only instance replica collection.
        :rtype: list of ReadOnlyInstance
        """
        return self._ReadOnlyInstanceSet

    @ReadOnlyInstanceSet.setter
    def ReadOnlyInstanceSet(self, ReadOnlyInstanceSet):
        self._ReadOnlyInstanceSet = ReadOnlyInstanceSet

    @property
    def Status(self):
        r"""Read-only group status: 1 - running after successful application; 5 - applying.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MasterInstanceId(self):
        r"""Primary instance ID. For example, mssql-sgeshe3th.
        :rtype: str
        """
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
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
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("ReadOnlyInstanceSet") is not None:
            self._ReadOnlyInstanceSet = []
            for item in params.get("ReadOnlyInstanceSet"):
                obj = ReadOnlyInstance()
                obj._deserialize(item)
                self._ReadOnlyInstanceSet.append(obj)
        self._Status = params.get("Status")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupByReadOnlyInstanceRequest(AbstractModel):
    r"""DescribeReadOnlyGroupByReadOnlyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssqlro-3l3fgqn7.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssqlro-3l3fgqn7.
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
        


class DescribeReadOnlyGroupByReadOnlyInstanceResponse(AbstractModel):
    r"""DescribeReadOnlyGroupByReadOnlyInstance response structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: Read only group ID.
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: Read-only group name.
        :type ReadOnlyGroupName: str
        :param _RegionId: Region ID of the read-only group.
        :type RegionId: str
        :param _ZoneId: AZ ID of the read-only group.
        :type ZoneId: str
        :param _IsOfflineDelay: Whether to enable startup timeout elimination, 0 - disable removal, 1 - enable removal.
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: Timeout threshold used after the delayed read-only instance removal feature is enabled, in seconds.
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: Minimum number of retained read-only replicas in the read-only group, after the delayed read-only instance removal feature is enabled.
        :type MinReadOnlyInGroup: int
        :param _Vip: Read-only group VIP.
        :type Vip: str
        :param _Vport: Read-only group VPort.
        :type Vport: int
        :param _VpcId: VPC ID of the read-only group.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID of the read-only group.
        :type SubnetId: str
        :param _MasterInstanceId: Primary instance ID. For example, mssql-sgeshe3th.
        :type MasterInstanceId: str
        :param _MasterRegionId: Region ID of the primary instance.
        :type MasterRegionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._RegionId = None
        self._ZoneId = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._MasterInstanceId = None
        self._MasterRegionId = None
        self._RequestId = None

    @property
    def ReadOnlyGroupId(self):
        r"""Read only group ID.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""Read-only group name.
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def RegionId(self):
        r"""Region ID of the read-only group.
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""AZ ID of the read-only group.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsOfflineDelay(self):
        r"""Whether to enable startup timeout elimination, 0 - disable removal, 1 - enable removal.
        :rtype: int
        """
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        r"""Timeout threshold used after the delayed read-only instance removal feature is enabled, in seconds.
        :rtype: int
        """
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        r"""Minimum number of retained read-only replicas in the read-only group, after the delayed read-only instance removal feature is enabled.
        :rtype: int
        """
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def Vip(self):
        r"""Read-only group VIP.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Read-only group VPort.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        r"""VPC ID of the read-only group.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""VPC subnet ID of the read-only group.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def MasterInstanceId(self):
        r"""Primary instance ID. For example, mssql-sgeshe3th.
        :rtype: str
        """
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def MasterRegionId(self):
        r"""Region ID of the primary instance.
        :rtype: str
        """
        return self._MasterRegionId

    @MasterRegionId.setter
    def MasterRegionId(self, MasterRegionId):
        self._MasterRegionId = MasterRegionId

    @property
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
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._MasterRegionId = params.get("MasterRegionId")
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupDetailsRequest(AbstractModel):
    r"""DescribeReadOnlyGroupDetails request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Primary instance ID, in the format of mssql-3l3fgqn7.
        :type InstanceId: str
        :param _ReadOnlyGroupId: Read-only group ID, in the format of mssqlrg-3l3fgqn7.
        :type ReadOnlyGroupId: str
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def InstanceId(self):
        r"""Primary instance ID, in the format of mssql-3l3fgqn7.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""Read-only group ID, in the format of mssqlrg-3l3fgqn7.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupDetailsResponse(AbstractModel):
    r"""DescribeReadOnlyGroupDetails response structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: Read-only group ID.
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: Read-only group name.
        :type ReadOnlyGroupName: str
        :param _RegionId: Region ID of the read-only group, which is the same as that of the primary instance.
        :type RegionId: str
        :param _ZoneId: AZ ID of the read-only group, which is the same as that of the primary instance.
        :type ZoneId: str
        :param _IsOfflineDelay: Whether to enable startup timeout elimination, 0 - disable removal, 1 - enable removal.
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: Timeout threshold used after the delayed read-only instance removal feature is enabled.
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: Minimum number of retained read-only replicas in the read-only group, after the delayed read-only instance removal feature is enabled.
        :type MinReadOnlyInGroup: int
        :param _Vip: Read-only group VIP.
        :type Vip: str
        :param _Vport: Read-only group VPort.
        :type Vport: int
        :param _VpcId: VPC ID of the read-only group.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID of the read-only group.
        :type SubnetId: str
        :param _ReadOnlyInstanceSet: Read-only instance replica collection.
        :type ReadOnlyInstanceSet: list of ReadOnlyInstance
        :param _Status: Read-only group status: 1 - running after successful application; 5 - applying.
        :type Status: int
        :param _MasterInstanceId: Primary instance ID. For example, mssql-sgeshe3th.
        :type MasterInstanceId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._RegionId = None
        self._ZoneId = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._ReadOnlyInstanceSet = None
        self._Status = None
        self._MasterInstanceId = None
        self._RequestId = None

    @property
    def ReadOnlyGroupId(self):
        r"""Read-only group ID.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""Read-only group name.
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def RegionId(self):
        r"""Region ID of the read-only group, which is the same as that of the primary instance.
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""AZ ID of the read-only group, which is the same as that of the primary instance.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsOfflineDelay(self):
        r"""Whether to enable startup timeout elimination, 0 - disable removal, 1 - enable removal.
        :rtype: int
        """
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        r"""Timeout threshold used after the delayed read-only instance removal feature is enabled.
        :rtype: int
        """
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        r"""Minimum number of retained read-only replicas in the read-only group, after the delayed read-only instance removal feature is enabled.
        :rtype: int
        """
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def Vip(self):
        r"""Read-only group VIP.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Read-only group VPort.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        r"""VPC ID of the read-only group.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""VPC subnet ID of the read-only group.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ReadOnlyInstanceSet(self):
        r"""Read-only instance replica collection.
        :rtype: list of ReadOnlyInstance
        """
        return self._ReadOnlyInstanceSet

    @ReadOnlyInstanceSet.setter
    def ReadOnlyInstanceSet(self, ReadOnlyInstanceSet):
        self._ReadOnlyInstanceSet = ReadOnlyInstanceSet

    @property
    def Status(self):
        r"""Read-only group status: 1 - running after successful application; 5 - applying.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MasterInstanceId(self):
        r"""Primary instance ID. For example, mssql-sgeshe3th.
        :rtype: str
        """
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
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
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("ReadOnlyInstanceSet") is not None:
            self._ReadOnlyInstanceSet = []
            for item in params.get("ReadOnlyInstanceSet"):
                obj = ReadOnlyInstance()
                obj._deserialize(item)
                self._ReadOnlyInstanceSet.append(obj)
        self._Status = params.get("Status")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._RequestId = params.get("RequestId")


class DescribeReadOnlyGroupListRequest(AbstractModel):
    r"""DescribeReadOnlyGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Primary instance ID, in the format of mssql-3l3fgqn7.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Primary instance ID, in the format of mssql-3l3fgqn7.
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
        


class DescribeReadOnlyGroupListResponse(AbstractModel):
    r"""DescribeReadOnlyGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupSet: Read-only group list.
        :type ReadOnlyGroupSet: list of ReadOnlyGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReadOnlyGroupSet = None
        self._RequestId = None

    @property
    def ReadOnlyGroupSet(self):
        r"""Read-only group list.
        :rtype: list of ReadOnlyGroup
        """
        return self._ReadOnlyGroupSet

    @ReadOnlyGroupSet.setter
    def ReadOnlyGroupSet(self, ReadOnlyGroupSet):
        self._ReadOnlyGroupSet = ReadOnlyGroupSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReadOnlyGroupSet") is not None:
            self._ReadOnlyGroupSet = []
            for item in params.get("ReadOnlyGroupSet"):
                obj = ReadOnlyGroup()
                obj._deserialize(item)
                self._ReadOnlyGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    r"""DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    r"""DescribeRegions response structure.

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
        r"""Total number of regions returned
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        r"""Region information array
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


class DescribeRegularBackupPlanRequest(AbstractModel):
    r"""DescribeRegularBackupPlan request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _RegularBackupSaveDays: Scheduled backup retention days, in the range of [90 - 3650]. The default value is 365.
        :type RegularBackupSaveDays: int
        :param _RegularBackupStrategy: Scheduled backup policy. years - annually; quarters - quarterly; months - monthly. The default value is months.
        :type RegularBackupStrategy: str
        :param _RegularBackupCounts: Number of retained scheduled backups. The default value is 1.
        :type RegularBackupCounts: int
        :param _RegularBackupStartTime: Scheduled backup start date, in the format of YYYY-MM-DD. The current date is used by default.
        :type RegularBackupStartTime: str
        :param _BackupCycle: Regular backup cycle.
        :type BackupCycle: list of int non-negative
        """
        self._InstanceId = None
        self._RegularBackupSaveDays = None
        self._RegularBackupStrategy = None
        self._RegularBackupCounts = None
        self._RegularBackupStartTime = None
        self._BackupCycle = None

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
    def RegularBackupSaveDays(self):
        r"""Scheduled backup retention days, in the range of [90 - 3650]. The default value is 365.
        :rtype: int
        """
        return self._RegularBackupSaveDays

    @RegularBackupSaveDays.setter
    def RegularBackupSaveDays(self, RegularBackupSaveDays):
        self._RegularBackupSaveDays = RegularBackupSaveDays

    @property
    def RegularBackupStrategy(self):
        r"""Scheduled backup policy. years - annually; quarters - quarterly; months - monthly. The default value is months.
        :rtype: str
        """
        return self._RegularBackupStrategy

    @RegularBackupStrategy.setter
    def RegularBackupStrategy(self, RegularBackupStrategy):
        self._RegularBackupStrategy = RegularBackupStrategy

    @property
    def RegularBackupCounts(self):
        r"""Number of retained scheduled backups. The default value is 1.
        :rtype: int
        """
        return self._RegularBackupCounts

    @RegularBackupCounts.setter
    def RegularBackupCounts(self, RegularBackupCounts):
        self._RegularBackupCounts = RegularBackupCounts

    @property
    def RegularBackupStartTime(self):
        r"""Scheduled backup start date, in the format of YYYY-MM-DD. The current date is used by default.
        :rtype: str
        """
        return self._RegularBackupStartTime

    @RegularBackupStartTime.setter
    def RegularBackupStartTime(self, RegularBackupStartTime):
        self._RegularBackupStartTime = RegularBackupStartTime

    @property
    def BackupCycle(self):
        r"""Regular backup cycle.
        :rtype: list of int non-negative
        """
        return self._BackupCycle

    @BackupCycle.setter
    def BackupCycle(self, BackupCycle):
        self._BackupCycle = BackupCycle


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RegularBackupSaveDays = params.get("RegularBackupSaveDays")
        self._RegularBackupStrategy = params.get("RegularBackupStrategy")
        self._RegularBackupCounts = params.get("RegularBackupCounts")
        self._RegularBackupStartTime = params.get("RegularBackupStartTime")
        self._BackupCycle = params.get("BackupCycle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegularBackupPlanResponse(AbstractModel):
    r"""DescribeRegularBackupPlan response structure.

    """

    def __init__(self):
        r"""
        :param _SaveModePeriod: Regular backup plan.
        :type SaveModePeriod: list of str
        :param _SaveModeRegular: Scheduled backup plan.
        :type SaveModeRegular: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SaveModePeriod = None
        self._SaveModeRegular = None
        self._RequestId = None

    @property
    def SaveModePeriod(self):
        r"""Regular backup plan.
        :rtype: list of str
        """
        return self._SaveModePeriod

    @SaveModePeriod.setter
    def SaveModePeriod(self, SaveModePeriod):
        self._SaveModePeriod = SaveModePeriod

    @property
    def SaveModeRegular(self):
        r"""Scheduled backup plan.
        :rtype: list of str
        """
        return self._SaveModeRegular

    @SaveModeRegular.setter
    def SaveModeRegular(self, SaveModeRegular):
        self._SaveModeRegular = SaveModeRegular

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SaveModePeriod = params.get("SaveModePeriod")
        self._SaveModeRegular = params.get("SaveModeRegular")
        self._RequestId = params.get("RequestId")


class DescribeRestoreTaskRequest(AbstractModel):
    r"""DescribeRestoreTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Source Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _RestoreType: Rollback method. 0 - roll back by time point; 1 - roll back by backup set.
        :type RestoreType: int
        :param _TargetRegion: Region where the target instance is located for rollback.
        :type TargetRegion: str
        :param _TargetType: Type of the target instance for rollback. 0 - current instance; 1 - existing instance; 2 - new instance.
        :type TargetType: int
        :param _Status: Rollback status, 0: initialized; 1: running; 2: successful; 3: failed.
        :type Status: int
        :param _Offset: The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 20.
        :type Offset: int
        :param _Limit: Page number in pagination mode. The default value is 0.
        :type Limit: int
        :param _OrderBy: Sorting field. restoreTime - rollback time; startTime-task start time; endTime-task end time. By default, the results are sorted in descending order by task start time.
        :type OrderBy: str
        :param _OrderByType: Sorting rule. desc - descending order; asc - ascending order. The default value is desc.
        :type OrderByType: str
        :param _FlowId: Asynchronous rollback task ID.
        :type FlowId: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._RestoreType = None
        self._TargetRegion = None
        self._TargetType = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderByType = None
        self._FlowId = None

    @property
    def InstanceId(self):
        r"""Source Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def RestoreType(self):
        r"""Rollback method. 0 - roll back by time point; 1 - roll back by backup set.
        :rtype: int
        """
        return self._RestoreType

    @RestoreType.setter
    def RestoreType(self, RestoreType):
        self._RestoreType = RestoreType

    @property
    def TargetRegion(self):
        r"""Region where the target instance is located for rollback.
        :rtype: str
        """
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def TargetType(self):
        r"""Type of the target instance for rollback. 0 - current instance; 1 - existing instance; 2 - new instance.
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Status(self):
        r"""Rollback status, 0: initialized; 1: running; 2: successful; 3: failed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        r"""The number of returned entries per page in pagination mode. Value range: 1-100. The default value is 20.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Page number in pagination mode. The default value is 0.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        r"""Sorting field. restoreTime - rollback time; startTime-task start time; endTime-task end time. By default, the results are sorted in descending order by task start time.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting rule. desc - descending order; asc - ascending order. The default value is desc.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def FlowId(self):
        r"""Asynchronous rollback task ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RestoreType = params.get("RestoreType")
        self._TargetRegion = params.get("TargetRegion")
        self._TargetType = params.get("TargetType")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTaskResponse(AbstractModel):
    r"""DescribeRestoreTask response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of rollback tasks.
        :type TotalCount: int
        :param _Tasks: Rollback task record list.
        :type Tasks: list of RestoreTask
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of rollback tasks.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        r"""Rollback task record list.
        :rtype: list of RestoreTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRestoreTimeRangeRequest(AbstractModel):
    r"""DescribeRestoreTimeRange request structure.

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
        r"""
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TargetInstanceId(self):
        r"""
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
    r"""DescribeRestoreTimeRange response structure.

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
        r"""
        :rtype: str
        """
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        r"""
        :rtype: str
        """
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeRollbackTime request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBs(self):
        r"""List of databases to be queried
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
    r"""DescribeRollbackTime response structure.

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
        r"""Information of time range available for database rollback
        :rtype: list of DbRollbackTimeInfo
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
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = DbRollbackTimeInfo()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowlogsRequest(AbstractModel):
    r"""DescribeSlowlogs request structure.

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
        r"""Instance ID in the format of mssql-k8voqdlz
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Start time in the format of `yyyy-MM-dd HH:mm:ss`
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time in the format of `yyyy-MM-dd HH:mm:ss`
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""Number of results per page. Value range: 1-100. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number. Default value: 0
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
    r"""DescribeSlowlogs response structure.

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
        r"""Total number of queries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Slowlogs(self):
        warnings.warn("parameter `Slowlogs` is deprecated", DeprecationWarning) 

        r"""Information list of slow query logs
        :rtype: list of SlowlogInfo
        """
        return self._Slowlogs

    @Slowlogs.setter
    def Slowlogs(self, Slowlogs):
        warnings.warn("parameter `Slowlogs` is deprecated", DeprecationWarning) 

        self._Slowlogs = Slowlogs

    @property
    def SlowLogs(self):
        r"""
        :rtype: list of SlowLog
        """
        return self._SlowLogs

    @SlowLogs.setter
    def SlowLogs(self, SlowLogs):
        self._SlowLogs = SlowLogs

    @property
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


class DescribeSpecSellStatusRequest(AbstractModel):
    r"""DescribeSpecSellStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ ID. For example, ap-guangzhou-3.
        :type Zone: str
        :param _SpecIdSet: Instance specification ID, which can be obtained by calling the DescribeProductConfig API.
        :type SpecIdSet: list of int non-negative
        :param _DBVersion: Database version, which can be obtained by calling the DescribeProductConfig API.
        :type DBVersion: str
        :param _Pid: Product ID, which can be obtained by calling the DescribeProductConfig API.
        :type Pid: int
        :param _PayMode: Payment mode. POST: pay-as-you-go; PRE: monthly subscription.
        :type PayMode: str
        :param _Currency: Currency. CNY; USD.
        :type Currency: str
        """
        self._Zone = None
        self._SpecIdSet = None
        self._DBVersion = None
        self._Pid = None
        self._PayMode = None
        self._Currency = None

    @property
    def Zone(self):
        r"""AZ ID. For example, ap-guangzhou-3.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecIdSet(self):
        r"""Instance specification ID, which can be obtained by calling the DescribeProductConfig API.
        :rtype: list of int non-negative
        """
        return self._SpecIdSet

    @SpecIdSet.setter
    def SpecIdSet(self, SpecIdSet):
        self._SpecIdSet = SpecIdSet

    @property
    def DBVersion(self):
        r"""Database version, which can be obtained by calling the DescribeProductConfig API.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def Pid(self):
        r"""Product ID, which can be obtained by calling the DescribeProductConfig API.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def PayMode(self):
        r"""Payment mode. POST: pay-as-you-go; PRE: monthly subscription.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Currency(self):
        r"""Currency. CNY; USD.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SpecIdSet = params.get("SpecIdSet")
        self._DBVersion = params.get("DBVersion")
        self._Pid = params.get("Pid")
        self._PayMode = params.get("PayMode")
        self._Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecSellStatusResponse(AbstractModel):
    r"""DescribeSpecSellStatus response structure.

    """

    def __init__(self):
        r"""
        :param _DescribeSpecSellStatusSet: Status set of specifications in different regions.
        :type DescribeSpecSellStatusSet: list of SpecSellStatus
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DescribeSpecSellStatusSet = None
        self._RequestId = None

    @property
    def DescribeSpecSellStatusSet(self):
        r"""Status set of specifications in different regions.
        :rtype: list of SpecSellStatus
        """
        return self._DescribeSpecSellStatusSet

    @DescribeSpecSellStatusSet.setter
    def DescribeSpecSellStatusSet(self, DescribeSpecSellStatusSet):
        self._DescribeSpecSellStatusSet = DescribeSpecSellStatusSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DescribeSpecSellStatusSet") is not None:
            self._DescribeSpecSellStatusSet = []
            for item in params.get("DescribeSpecSellStatusSet"):
                obj = SpecSellStatus()
                obj._deserialize(item)
                self._DescribeSpecSellStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUpgradeInstanceCheckRequest(AbstractModel):
    r"""DescribeUpgradeInstanceCheck request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID, in the format of mssql-njj2mtpl.
        :type InstanceId: str
        :param _Cpu: Number of CPU cores after instance configuration adjustment. If it is left blank, no modification is required.
        :type Cpu: int
        :param _Memory: Memory size after instance configuration adjustment, in GB. If it is left blank, no modification is required.
        :type Memory: int
        :param _Storage: Disk size after instance configuration adjustment, in GB. If it is left blank, no modification is required.
        :type Storage: int
        :param _DBVersion: Instance version. If it is left blank, no modification is required.
        :type DBVersion: str
        :param _HAType: Type after instance configuration adjustment. Valid values: CLUSTER - cluster. If it is left blank, no modification is required.
        :type HAType: str
        :param _MultiZones: Cross-AZ type after instance configuration adjustment. Valid values: SameZones - change to the same AZ; MultiZones - change to cross-AZ. If it is left blank, no modification is required.
        :type MultiZones: str
        :param _DrZones: Secondary node AZ of the multi-node architecture instance. The default value is null. It should be specified when modifying the AZ of the specified secondary node needs to be performed during configuration adjustment. When MultiZones = MultiZones, the AZs of the primary nodes and secondary nodes cannot all be the same. The collection of AZs of the secondary node can include 2-5 AZs.
        :type DrZones: list of DrZoneInfo
        """
        self._InstanceId = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._DBVersion = None
        self._HAType = None
        self._MultiZones = None
        self._DrZones = None

    @property
    def InstanceId(self):
        r"""Database instance ID, in the format of mssql-njj2mtpl.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cpu(self):
        r"""Number of CPU cores after instance configuration adjustment. If it is left blank, no modification is required.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""Memory size after instance configuration adjustment, in GB. If it is left blank, no modification is required.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Disk size after instance configuration adjustment, in GB. If it is left blank, no modification is required.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def DBVersion(self):
        r"""Instance version. If it is left blank, no modification is required.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def HAType(self):
        r"""Type after instance configuration adjustment. Valid values: CLUSTER - cluster. If it is left blank, no modification is required.
        :rtype: str
        """
        return self._HAType

    @HAType.setter
    def HAType(self, HAType):
        self._HAType = HAType

    @property
    def MultiZones(self):
        r"""Cross-AZ type after instance configuration adjustment. Valid values: SameZones - change to the same AZ; MultiZones - change to cross-AZ. If it is left blank, no modification is required.
        :rtype: str
        """
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def DrZones(self):
        r"""Secondary node AZ of the multi-node architecture instance. The default value is null. It should be specified when modifying the AZ of the specified secondary node needs to be performed during configuration adjustment. When MultiZones = MultiZones, the AZs of the primary nodes and secondary nodes cannot all be the same. The collection of AZs of the secondary node can include 2-5 AZs.
        :rtype: list of DrZoneInfo
        """
        return self._DrZones

    @DrZones.setter
    def DrZones(self, DrZones):
        self._DrZones = DrZones


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._DBVersion = params.get("DBVersion")
        self._HAType = params.get("HAType")
        self._MultiZones = params.get("MultiZones")
        if params.get("DrZones") is not None:
            self._DrZones = []
            for item in params.get("DrZones"):
                obj = DrZoneInfo()
                obj._deserialize(item)
                self._DrZones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpgradeInstanceCheckResponse(AbstractModel):
    r"""DescribeUpgradeInstanceCheck response structure.

    """

    def __init__(self):
        r"""
        :param _IsAffect: Whether the configuration adjustment has an impact on the instance. 0 - no; 1 - yes.
        :type IsAffect: int
        :param _Passed: Whether the configuration adjustment can be executed. 0 - no; 1 - yes.
        :type Passed: int
        :param _ModifyMode: Whether the configuration adjustment is a downgrade or an upgrade. Down - downgrade; up - upgrade.
        :type ModifyMode: str
        :param _CheckItems: Check item list.
        :type CheckItems: list of CheckItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsAffect = None
        self._Passed = None
        self._ModifyMode = None
        self._CheckItems = None
        self._RequestId = None

    @property
    def IsAffect(self):
        r"""Whether the configuration adjustment has an impact on the instance. 0 - no; 1 - yes.
        :rtype: int
        """
        return self._IsAffect

    @IsAffect.setter
    def IsAffect(self, IsAffect):
        self._IsAffect = IsAffect

    @property
    def Passed(self):
        r"""Whether the configuration adjustment can be executed. 0 - no; 1 - yes.
        :rtype: int
        """
        return self._Passed

    @Passed.setter
    def Passed(self, Passed):
        self._Passed = Passed

    @property
    def ModifyMode(self):
        r"""Whether the configuration adjustment is a downgrade or an upgrade. Down - downgrade; up - upgrade.
        :rtype: str
        """
        return self._ModifyMode

    @ModifyMode.setter
    def ModifyMode(self, ModifyMode):
        self._ModifyMode = ModifyMode

    @property
    def CheckItems(self):
        r"""Check item list.
        :rtype: list of CheckItem
        """
        return self._CheckItems

    @CheckItems.setter
    def CheckItems(self, CheckItems):
        self._CheckItems = CheckItems

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsAffect = params.get("IsAffect")
        self._Passed = params.get("Passed")
        self._ModifyMode = params.get("ModifyMode")
        if params.get("CheckItems") is not None:
            self._CheckItems = []
            for item in params.get("CheckItems"):
                obj = CheckItem()
                obj._deserialize(item)
                self._CheckItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUploadBackupInfoRequest(AbstractModel):
    r"""DescribeUploadBackupInfo request structure.

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
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the API CreateBackupMigration
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
    r"""DescribeUploadBackupInfo response structure.

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
        r"""Bucket name
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def Region(self):
        r"""Bucket location information
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Path(self):
        r"""Storage path
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def TmpSecretId(self):
        r"""Temporary key ID
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        r"""Temporary key (Key)
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def XCosSecurityToken(self):
        warnings.warn("parameter `XCosSecurityToken` is deprecated", DeprecationWarning) 

        r"""Temporary key (Token)
        :rtype: str
        """
        return self._XCosSecurityToken

    @XCosSecurityToken.setter
    def XCosSecurityToken(self, XCosSecurityToken):
        warnings.warn("parameter `XCosSecurityToken` is deprecated", DeprecationWarning) 

        self._XCosSecurityToken = XCosSecurityToken

    @property
    def StartTime(self):
        r"""Temporary key start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        r"""Temporary key expiration time
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CosSecurityToken(self):
        r"""
        :rtype: str
        """
        return self._CosSecurityToken

    @CosSecurityToken.setter
    def CosSecurityToken(self, CosSecurityToken):
        self._CosSecurityToken = CosSecurityToken

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeXEvents request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EventType(self):
        r"""Event type. Valid values: `slow` (Slow SQL event), `blocked` (blocking event),  deadlock` (deadlock event).
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def StartTime(self):
        r"""Generation start time of an extended file in the format of yyyy-MM-dd HH:mm:ss.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Generation end time of an extended file in the format of yyyy-MM-dd HH:mm:ss.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""Page number. Default value: `0`
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries to be returned per page. Value range: 1-100. Default value: `20`
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
    r"""DescribeXEvents response structure.

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
        r"""List of extended events
        :rtype: list of Events
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        r"""Total number of extended events
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
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = Events()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    r"""DescribeZones request structure.

    """


class DescribeZonesResponse(AbstractModel):
    r"""DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of AZs returned.
        :type TotalCount: int
        :param _ZoneSet: Array of AZs.
        :type ZoneSet: list of ZoneInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of AZs returned.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneSet(self):
        r"""Array of AZs.
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


class DisassociateSecurityGroupsRequest(AbstractModel):
    r"""DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group ID.
        :type SecurityGroupId: str
        :param _InstanceIdSet: Instance ID list, which is an array of one or more instance IDs. Multiple instances should be in the same region, AZ, and project.
        :type InstanceIdSet: list of str
        """
        self._SecurityGroupId = None
        self._InstanceIdSet = None

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
    def InstanceIdSet(self):
        r"""Instance ID list, which is an array of one or more instance IDs. Multiple instances should be in the same region, AZ, and project.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    r"""DisassociateSecurityGroups response structure.

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


class DrReadableInfo(AbstractModel):
    r"""Replica server read-only information

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
        r"""Replica server status. Valid values: enable - running; disable - unavailable
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SlaveStatus

    @SlaveStatus.setter
    def SlaveStatus(self, SlaveStatus):
        self._SlaveStatus = SlaveStatus

    @property
    def ReadableStatus(self):
        r"""Replica server readable status. Valid values: enable - enabled; disable - disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReadableStatus

    @ReadableStatus.setter
    def ReadableStatus(self, ReadableStatus):
        self._ReadableStatus = ReadableStatus

    @property
    def Vip(self):
        r"""Replica server read-only VIP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        r"""Replica server read-only port
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def UniqVpcId(self):
        r"""Replica server VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        r"""Replica server VPC subnet ID
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
        


class DrZoneInfo(AbstractModel):
    r"""AZ information on the secondary node.

    """

    def __init__(self):
        r"""
        :param _DrInstanceId: Resource ID of the secondary node.
        :type DrInstanceId: str
        :param _Zone: AZ of the secondary node.
        :type Zone: str
        """
        self._DrInstanceId = None
        self._Zone = None

    @property
    def DrInstanceId(self):
        r"""Resource ID of the secondary node.
        :rtype: str
        """
        return self._DrInstanceId

    @DrInstanceId.setter
    def DrInstanceId(self, DrInstanceId):
        self._DrInstanceId = DrInstanceId

    @property
    def Zone(self):
        r"""AZ of the secondary node.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._DrInstanceId = params.get("DrInstanceId")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventConfig(AbstractModel):
    r"""Threshold setting for an extended event

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
        r"""Event type. Valid values: `slow` (set threshold for slow SQL ), `blocked` (set threshold for the blocking and deadlock).
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Threshold(self):
        r"""Threshold in milliseconds. Valid values: `0`(disable), `non-zero` (enable)
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
    r"""Details of an extended event

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
        r"""ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FileName(self):
        r"""File name of an extended event
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Size(self):
        r"""File size of an extended event
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventType(self):
        r"""Event type. Valid values: `slow` (Slow SQL event), `blocked` (blocking event),  `deadlock` (deadlock event).
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Status(self):
        r"""Event record status. Valid values: `1` (succeeded), `2` (failed).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""Generation start time of an extended file
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Generation end time of an extended file
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InternalAddr(self):
        r"""Download address on the private network
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        r"""Download address on the public network
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
    r"""Information of allowed operation

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
        r"""Allowed operations. Valid values: `view` (view list), `remark` (modify remark), `deploy` (deploy files), `delete` (delete files).
        :rtype: list of str
        """
        return self._AllAction

    @AllAction.setter
    def AllAction(self, AllAction):
        self._AllAction = AllAction

    @property
    def AllowedAction(self):
        r"""Operation allowed in the current status. If the subset of `AllAction` is empty, no operations will be allowed.
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
    r"""InquiryPriceCreateDBInstances request structure.

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
        r"""AZ ID, which can be obtained through the `Zone` field in the returned value of the `DescribeZones` API
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        r"""Memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Instance capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceChargeType(self):
        r"""Billing type. Valid value: POSTPAID.
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Period(self):
        r"""Length of purchase in months. Value range: 1-48. Default value: 1
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def GoodsNum(self):
        r"""Number of instances purchased at a time. Value range: 1-100. Default value: 1
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def DBVersion(self):
        r"""SQL version. Valid values: `2008R2` (SQL Server 2008 R2 Enterprise), `2012SP3` (SQL Server 2012 Enterprise), `201202` (SQL Server 2012 Standard), `2014SP2` (SQL Server 2014 Enterprise), `201402` (SQL Server 2014 Standard)`, `2016SP1` (SQL Server 2016 Enterprise), `201602` (SQL Server 2016 Standard), `2017` (SQL Server 2017 Enterprise), `201702` (SQL Server 2017 Standard), `2019` (SQL Server 2019 Enterprise), `201902` (SQL Server 2019 Standard). Default value: `2008R2`. The purchasable version varies by region. It can be queried by the `DescribeProductConfig` API.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def Cpu(self):
        r"""The number of CPU cores of the instance you want to purchase.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def InstanceType(self):
        r"""The type of instance to be purchased. Valid values: `HA` (high-availability edition, including dual-server high-availability and AlwaysOn cluster edition), `RO` (read-only replica edition), `SI` (single-node edition), `cvmHA` (dual-server high-availability edition for CVM), `cvmRO` (read-only edition for CVM).
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MachineType(self):
        r"""The host type of the instance to be purchased. Valid values: `PM` (physical machine), `CLOUD_PREMIUM` (virtual machine with premium cloud disk), `CLOUD_SSD` (virtual machine with SSD), 
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
    r"""InquiryPriceCreateDBInstances response structure.

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
        r"""Price before discount. This value divided by 100 indicates the price; for example, 10010 means 100.10 USD
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        r"""The actual price to be paid. This value divided by 100 indicates the price; for example, 10010 means 100.10 USD
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
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
        self._RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    r"""InquiryPriceUpgradeDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of mssql-njj2mtpl.
        :type InstanceId: str
        :param _Memory: Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size.
        :type Memory: int
        :param _Storage: Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity.
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
        r"""Instance ID in the format of mssql-njj2mtpl.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        r"""Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        r"""The number of CUP cores after the instance is upgraded, which cannot be smaller than that of the current cores.
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
    r"""InquiryPriceUpgradeDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: Price before discount. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD.
        :type OriginalPrice: int
        :param _Price: The actual price to be paid. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD.
        :type Price: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        r"""Price before discount. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD.
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        r"""The actual price to be paid. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD.
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
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
        self._RequestId = params.get("RequestId")


class InstanceDBDetail(AbstractModel):
    r"""Instance database information

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBDetails(self):
        r"""Database information list
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
        


class InstanceTask(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Id: 
        :type Id: int
        :param _Type: 
        :type Type: int
        :param _Status: 
        :type Status: int
        :param _Progress: 
        :type Progress: int
        :param _StartTime: 
        :type StartTime: str
        :param _EndTime: 
        :type EndTime: str
        :param _ErrorCode: 
        :type ErrorCode: int
        :param _Message: 
        :type Message: str
        """
        self._Id = None
        self._Type = None
        self._Status = None
        self._Progress = None
        self._StartTime = None
        self._EndTime = None
        self._ErrorCode = None
        self._Message = None

    @property
    def Id(self):
        r"""
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        r"""
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        r"""
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StartTime(self):
        r"""
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ErrorCode(self):
        r"""
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def Message(self):
        r"""
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ErrorCode = params.get("ErrorCode")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InterInstance(AbstractModel):
    r"""Details of instances in the interwoking group

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InterVip(self):
        r"""Instance interworking IP, which can be accessed after the instance is added to the interworking group.
        :rtype: str
        """
        return self._InterVip

    @InterVip.setter
    def InterVip(self, InterVip):
        self._InterVip = InterVip

    @property
    def InterPort(self):
        r"""Instance interworking port, which can be accessed after the instance is added to the interworking group.
        :rtype: int
        """
        return self._InterPort

    @InterPort.setter
    def InterPort(self, InterPort):
        self._InterPort = InterPort

    @property
    def Status(self):
        r"""Instance interworking status. Valid values: `1` (Enabling interworking IP), `2` (Enabled interworking IP), `3` (Adding to interworking group), `4` (Added to interworking group), `5` (Reclaiming interworking IP), `6`(Reclaimed interworking IP), `7` (Removing from interworking group), `8` (Removed from interworking group).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""Instance region, such as ap-guangzhou.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""Instance AZ name, such as ap-guangzhou-1.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Version(self):
        r"""Instance version code
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def VersionName(self):
        r"""Instance version
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Name(self):
        r"""Instance name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Vip(self):
        r"""Instance access IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Instance access port
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
    r"""Instance status after enabling or disabling the interworking group

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
        r"""Instance ID, such as mssql-sdf32n1d.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        r"""Instance task ID for enabling or disabling the interworking group. When `FlowId` is less than 0, the interworking group will be enabled or disabled successfully; otherwise, the operation failed.
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
    r"""List of databases to be migrated

    """

    def __init__(self):
        r"""
        :param _DBName: Name of migrated database
        :type DBName: str
        """
        self._DBName = None

    @property
    def DBName(self):
        r"""Name of migrated database
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
    r"""Migration progress details

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
        r"""Name of current step
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def Progress(self):
        r"""Progress of current step in %
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
    r"""Source type of migration task

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
        r"""Source instance ID in the format of `mssql-si2823jyl`, which is used when `MigrateType` is 1 (TencentDB for SQL Server)
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmId(self):
        r"""ID of source CVM instance, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: str
        """
        return self._CvmId

    @CvmId.setter
    def CvmId(self, CvmId):
        self._CvmId = CvmId

    @property
    def VpcId(self):
        r"""VPC ID of source CVM instance in the format of vpc-6ys9ont9, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""VPC subnet ID of source CVM instance in the format of subnet-h9extioi, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def UserName(self):
        r"""Username, which is used when `MigrateType` is 1 or 2
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""Password, which is used when `MigrateType` is 1 or 2
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Ip(self):
        r"""Private IP of source CVM database, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Port number of source CVM database, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Url(self):
        r"""Source backup address for offline migration, which is used when `MigrateType` is 4 or 5
        :rtype: list of str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def UrlPassword(self):
        r"""Source backup password for offline migration, which is used when `MigrateType` is 4 or 5
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
    r"""Target type of migration task

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
        r"""ID of target instance in the format of mssql-si2823jyl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        r"""Username of migration target instance
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""Password of migration target instance
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
    r"""Migration task type

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
        r"""Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def MigrateName(self):
        r"""Migration task name
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def AppId(self):
        r"""User ID of migration task
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        r"""Migration task region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SourceType(self):
        r"""Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def CreateTime(self):
        r"""Migration task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        r"""Migration task start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Migration task end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""Migration task status (1: initializing, 4: migrating, 5: migration failed, 6: migration succeeded, 7: suspended, 8: deleted, 9: suspending, 10: completing, 11: suspension failed, 12: completion failed)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        r"""Information
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def CheckFlag(self):
        r"""Whether migration task has been checked (0: not checked, 1: check succeeded, 2: check failed, 3: checking)
        :rtype: int
        """
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

    @property
    def Progress(self):
        r"""Migration task progress in %
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def MigrateDetail(self):
        r"""Migration task progress details
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
    r"""Cold backup migration import

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
        r"""Backup import task ID or incremental import task ID
        :rtype: str
        """
        return self._MigrationId

    @MigrationId.setter
    def MigrationId(self, MigrationId):
        self._MigrationId = MigrationId

    @property
    def MigrationName(self):
        r"""Backup import task name. For an incremental import task, this field will be left empty.
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def AppId(self):
        r"""Application ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        r"""Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        r"""ID of migrated target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RecoveryType(self):
        r"""Migration task restoration type
        :rtype: str
        """
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        r"""Backup user upload type. COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :rtype: str
        """
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def BackupFiles(self):
        r"""Backup file list, which is determined by UploadType. If the upload type is COS_URL, URL will be saved. If the upload type is COS_UPLOAD, the backup name will be saved.
        :rtype: list of str
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def Status(self):
        r"""Migration task status. Valid values: `2` (Creation completed), `7` (Importing full backups), `8` (Waiting for incremental backups), `9` (Import success), `10` (Import failure), `12` (Importing incremental backups).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""Migration task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        r"""Migration task start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Migration task end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Message(self):
        r"""More information
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Detail(self):
        r"""Migration detail
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrationDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Action(self):
        r"""Operation allowed in the current status
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrationAction`
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def IsRecovery(self):
        r"""Whether this is the final restoration. For a full import task, this field will be left empty.
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery

    @property
    def DBRename(self):
        r"""Name set of renamed databases
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
    r"""Operation allowed by a cold backup import task

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
        r"""All the allowed operations. Values include: view (viewing a task), modify (modifying a task), start (starting a task), incremental (creating an incremental task), delete (deleting a task), and upload (obtaining the upload permission).
        :rtype: list of str
        """
        return self._AllAction

    @AllAction.setter
    def AllAction(self, AllAction):
        self._AllAction = AllAction

    @property
    def AllowedAction(self):
        r"""Operation allowed in the current status. If the subset of AllAction is left empty, no operations will be allowed.
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
    r"""Details of a cold backup import task

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
        r"""Total number of steps
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        r"""Current step
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Progress(self):
        r"""Overall progress. For example, “30” means 30%.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepInfo(self):
        r"""Step information. ‘null’ means the migration has not started
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
    r"""Migration steps of a cold backup import task

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
        r"""Step sequence
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        r"""Step name
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        r"""Step ID in English
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        r"""Step status: 0 (default value), 1 (succeeded), 2 (failed), 3 (in progress), 4 (not started)
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
    r"""ModifyAccountPrivilege request structure.

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
        r"""Database instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        r"""Account permission change information
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
    r"""ModifyAccountPrivilege response structure.

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
        r"""Async task flow ID
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


class ModifyAccountRemarkRequest(AbstractModel):
    r"""ModifyAccountRemark request structure.

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
        r"""Instance ID in the format of mssql-j8kv137v
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        r"""Information of account for which to modify remarks
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


class ModifyBackupMigrationRequest(AbstractModel):
    r"""ModifyBackupMigration request structure.

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
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def MigrationName(self):
        r"""Task name
        :rtype: str
        """
        return self._MigrationName

    @MigrationName.setter
    def MigrationName(self, MigrationName):
        self._MigrationName = MigrationName

    @property
    def RecoveryType(self):
        r"""Migration task restoration type: FULL,FULL_LOG,FULL_DIFF
        :rtype: str
        """
        return self._RecoveryType

    @RecoveryType.setter
    def RecoveryType(self, RecoveryType):
        self._RecoveryType = RecoveryType

    @property
    def UploadType(self):
        r"""COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :rtype: str
        """
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def BackupFiles(self):
        r"""If the UploadType is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :rtype: list of str
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def DBRename(self):
        r"""Name set of databases to be renamed
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
    r"""ModifyBackupMigration response structure.

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
        r"""Backup import task ID
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupMigrationId = params.get("BackupMigrationId")
        self._RequestId = params.get("RequestId")


class ModifyBackupNameRequest(AbstractModel):
    r"""ModifyBackupName request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-3l3fgqn7.
        :type InstanceId: str
        :param _BackupName: Modified backup name.
        :type BackupName: str
        :param _BackupId: The backup ID can be obtained through the [DescribeBackups](https://cloud.tencent.com/document/product/238/19943) API. When the value of GroupId is null, BackupId is required.
        :type BackupId: int
        :param _GroupId: Backup task group ID, which can be obtained through the [DescribeBackups](https://cloud.tencent.com/document/product/238/19943) API in single-database backup file mode. BackupId and GroupId exist simultaneously, and are modified according to BackupId.
        :type GroupId: str
        """
        self._InstanceId = None
        self._BackupName = None
        self._BackupId = None
        self._GroupId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-3l3fgqn7.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        r"""Modified backup name.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def BackupId(self):
        r"""The backup ID can be obtained through the [DescribeBackups](https://cloud.tencent.com/document/product/238/19943) API. When the value of GroupId is null, BackupId is required.
        :rtype: int
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def GroupId(self):
        r"""Backup task group ID, which can be obtained through the [DescribeBackups](https://cloud.tencent.com/document/product/238/19943) API in single-database backup file mode. BackupId and GroupId exist simultaneously, and are modified according to BackupId.
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        self._BackupId = params.get("BackupId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupNameResponse(AbstractModel):
    r"""ModifyBackupName response structure.

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


class ModifyBackupStrategyRequest(AbstractModel):
    r"""ModifyBackupStrategy request structure.

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
        :param _BackupCycle: The days of the week on which backup will be performed when "BackupType" is `weekly`. If data backup retention period is less than 7 days, the values will be 1-7, indicating that backup will be performed everyday by default; if data backup retention period is greater than or equal to 7 days, the values will be at least any two days, indicating that backup will be performed at least twice in a week by default.
        :type BackupCycle: list of int non-negative
        :param _BackupSaveDays: Data (log) backup retention period. Value range: 3-1830 days, default value: 7 days.
        :type BackupSaveDays: int
        :param _RegularBackupEnable: Archive backup status. Valid values: `enable` (enabled); `disable` (disabled). Default value: `disable`.
        :type RegularBackupEnable: str
        :param _RegularBackupSaveDays: Archive backup retention days. Value range: 90-3650 days. Default value: 365 days.
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
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupType(self):
        r"""Backup type. Valid values: `weekly` (when length(BackupDay) <=7 && length(BackupDay) >=2), `daily` (when length(BackupDay)=1). Default value: `daily`.
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupTime(self):
        r"""Backup time. Value range: an integer from 0 to 23.
        :rtype: int
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def BackupDay(self):
        r"""Backup interval in days when the `BackupType` is `daily`. Valid value: 1.
        :rtype: int
        """
        return self._BackupDay

    @BackupDay.setter
    def BackupDay(self, BackupDay):
        self._BackupDay = BackupDay

    @property
    def BackupModel(self):
        r"""Backup mode. Valid values: `master_pkg` (archive the backup files of the primary node), `master_no_pkg` (do not archive the backup files of the primary node), `slave_pkg` (archive the backup files of the replica node), `slave_no_pkg` (do not archive the backup files of the replica node). Backup files of the replica node are supported only when Always On disaster recovery is enabled.
        :rtype: str
        """
        return self._BackupModel

    @BackupModel.setter
    def BackupModel(self, BackupModel):
        self._BackupModel = BackupModel

    @property
    def BackupCycle(self):
        r"""The days of the week on which backup will be performed when "BackupType" is `weekly`. If data backup retention period is less than 7 days, the values will be 1-7, indicating that backup will be performed everyday by default; if data backup retention period is greater than or equal to 7 days, the values will be at least any two days, indicating that backup will be performed at least twice in a week by default.
        :rtype: list of int non-negative
        """
        return self._BackupCycle

    @BackupCycle.setter
    def BackupCycle(self, BackupCycle):
        self._BackupCycle = BackupCycle

    @property
    def BackupSaveDays(self):
        r"""Data (log) backup retention period. Value range: 3-1830 days, default value: 7 days.
        :rtype: int
        """
        return self._BackupSaveDays

    @BackupSaveDays.setter
    def BackupSaveDays(self, BackupSaveDays):
        self._BackupSaveDays = BackupSaveDays

    @property
    def RegularBackupEnable(self):
        r"""Archive backup status. Valid values: `enable` (enabled); `disable` (disabled). Default value: `disable`.
        :rtype: str
        """
        return self._RegularBackupEnable

    @RegularBackupEnable.setter
    def RegularBackupEnable(self, RegularBackupEnable):
        self._RegularBackupEnable = RegularBackupEnable

    @property
    def RegularBackupSaveDays(self):
        r"""Archive backup retention days. Value range: 90-3650 days. Default value: 365 days.
        :rtype: int
        """
        return self._RegularBackupSaveDays

    @RegularBackupSaveDays.setter
    def RegularBackupSaveDays(self, RegularBackupSaveDays):
        self._RegularBackupSaveDays = RegularBackupSaveDays

    @property
    def RegularBackupStrategy(self):
        r"""Archive backup policy. Valid values: `years` (yearly); `quarters (quarterly); `months` (monthly); Default value: `months`.
        :rtype: str
        """
        return self._RegularBackupStrategy

    @RegularBackupStrategy.setter
    def RegularBackupStrategy(self, RegularBackupStrategy):
        self._RegularBackupStrategy = RegularBackupStrategy

    @property
    def RegularBackupCounts(self):
        r"""The number of retained archive backups. Default value: `1`.
        :rtype: int
        """
        return self._RegularBackupCounts

    @RegularBackupCounts.setter
    def RegularBackupCounts(self, RegularBackupCounts):
        self._RegularBackupCounts = RegularBackupCounts

    @property
    def RegularBackupStartTime(self):
        r"""Archive backup start date in YYYY-MM-DD format, which is the current time by default.
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
    r"""ModifyBackupStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Errno: Returned error code.
        :type Errno: int
        :param _Msg: Returned error message.
        :type Msg: str
        :param _Code: Returned error code.
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

        r"""Returned error code.
        :rtype: int
        """
        return self._Errno

    @Errno.setter
    def Errno(self, Errno):
        warnings.warn("parameter `Errno` is deprecated", DeprecationWarning) 

        self._Errno = Errno

    @property
    def Msg(self):
        r"""Returned error message.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Code(self):
        r"""Returned error code.
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyCloseWanIpRequest(AbstractModel):
    r"""ModifyCloseWanIp request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance resource ID. 
        :type InstanceId: str
        :param _RoGroupId: RO group ID.
        :type RoGroupId: str
        """
        self._InstanceId = None
        self._RoGroupId = None

    @property
    def InstanceId(self):
        r"""Instance resource ID. 
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RoGroupId(self):
        r"""RO group ID.
        :rtype: str
        """
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RoGroupId = params.get("RoGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloseWanIpResponse(AbstractModel):
    r"""ModifyCloseWanIp response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: ID of the process of disabling the public network.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""ID of the process of disabling the public network.
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


class ModifyCrossBackupStrategyRequest(AbstractModel):
    r"""ModifyCrossBackupStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _CrossBackupEnabled: Cross-region backup switch (data backup & log backup). enable - enabled; disable - disabled.
        :type CrossBackupEnabled: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceIdSet: Instance ID list.
        :type InstanceIdSet: list of str
        :param _CrossBackupSaveDays: Retention days for cross-region backups. Value range: 7-1830. The default value is 7.
        :type CrossBackupSaveDays: int
        :param _CrossBackupRegion: Target region ID for cross-region backups, with a maximum of two and a minimum of one.
        :type CrossBackupRegion: list of str
        :param _CleanUpCrossBackup: Whether to clean up cross-region backups (data backups & log backups) immediately. This parameter is only valid when the value of BackupEnabled is disabled. 1 - yes; 0 - no. The default value is 0.
        :type CleanUpCrossBackup: int
        """
        self._CrossBackupEnabled = None
        self._InstanceId = None
        self._InstanceIdSet = None
        self._CrossBackupSaveDays = None
        self._CrossBackupRegion = None
        self._CleanUpCrossBackup = None

    @property
    def CrossBackupEnabled(self):
        r"""Cross-region backup switch (data backup & log backup). enable - enabled; disable - disabled.
        :rtype: str
        """
        return self._CrossBackupEnabled

    @CrossBackupEnabled.setter
    def CrossBackupEnabled(self, CrossBackupEnabled):
        self._CrossBackupEnabled = CrossBackupEnabled

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
    def InstanceIdSet(self):
        r"""Instance ID list.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def CrossBackupSaveDays(self):
        r"""Retention days for cross-region backups. Value range: 7-1830. The default value is 7.
        :rtype: int
        """
        return self._CrossBackupSaveDays

    @CrossBackupSaveDays.setter
    def CrossBackupSaveDays(self, CrossBackupSaveDays):
        self._CrossBackupSaveDays = CrossBackupSaveDays

    @property
    def CrossBackupRegion(self):
        r"""Target region ID for cross-region backups, with a maximum of two and a minimum of one.
        :rtype: list of str
        """
        return self._CrossBackupRegion

    @CrossBackupRegion.setter
    def CrossBackupRegion(self, CrossBackupRegion):
        self._CrossBackupRegion = CrossBackupRegion

    @property
    def CleanUpCrossBackup(self):
        r"""Whether to clean up cross-region backups (data backups & log backups) immediately. This parameter is only valid when the value of BackupEnabled is disabled. 1 - yes; 0 - no. The default value is 0.
        :rtype: int
        """
        return self._CleanUpCrossBackup

    @CleanUpCrossBackup.setter
    def CleanUpCrossBackup(self, CleanUpCrossBackup):
        self._CleanUpCrossBackup = CleanUpCrossBackup


    def _deserialize(self, params):
        self._CrossBackupEnabled = params.get("CrossBackupEnabled")
        self._InstanceId = params.get("InstanceId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._CrossBackupSaveDays = params.get("CrossBackupSaveDays")
        self._CrossBackupRegion = params.get("CrossBackupRegion")
        self._CleanUpCrossBackup = params.get("CleanUpCrossBackup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCrossBackupStrategyResponse(AbstractModel):
    r"""ModifyCrossBackupStrategy response structure.

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


class ModifyDBEncryptAttributesRequest(AbstractModel):
    r"""ModifyDBEncryptAttributes request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBTDEEncrypt(self):
        r"""A parameter used to enable or disable TDE of the database
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
    r"""ModifyDBEncryptAttributes response structure.

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
        r"""Task flow ID
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


class ModifyDBInstanceNameRequest(AbstractModel):
    r"""ModifyDBInstanceName request structure.

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
        r"""Database instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""New name of database instance
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


class ModifyDBInstanceNetworkRequest(AbstractModel):
    r"""ModifyDBInstanceNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _NewVpcId: ID of the new VPC.
        :type NewVpcId: str
        :param _NewSubnetId: ID of the new subnet.
        :type NewSubnetId: str
        :param _OldIpRetainTime: Retention period (in hours) of the original VIP. Value range: `0-168`. Default value: `0`, indicating the original VIP is released immediately.
        :type OldIpRetainTime: int
        :param _Vip: New VIP.
        :type Vip: str
        :param _DRNetwork: Target node. 0 - modify the primary node network; 1 - modify the secondary node network. The default value is 0.

        :type DRNetwork: int
        :param _DrInstanceId: Secondary server resource ID. It is required when DRNetwork = 1.
        :type DrInstanceId: str
        """
        self._InstanceId = None
        self._NewVpcId = None
        self._NewSubnetId = None
        self._OldIpRetainTime = None
        self._Vip = None
        self._DRNetwork = None
        self._DrInstanceId = None

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
    def NewVpcId(self):
        r"""ID of the new VPC.
        :rtype: str
        """
        return self._NewVpcId

    @NewVpcId.setter
    def NewVpcId(self, NewVpcId):
        self._NewVpcId = NewVpcId

    @property
    def NewSubnetId(self):
        r"""ID of the new subnet.
        :rtype: str
        """
        return self._NewSubnetId

    @NewSubnetId.setter
    def NewSubnetId(self, NewSubnetId):
        self._NewSubnetId = NewSubnetId

    @property
    def OldIpRetainTime(self):
        r"""Retention period (in hours) of the original VIP. Value range: `0-168`. Default value: `0`, indicating the original VIP is released immediately.
        :rtype: int
        """
        return self._OldIpRetainTime

    @OldIpRetainTime.setter
    def OldIpRetainTime(self, OldIpRetainTime):
        self._OldIpRetainTime = OldIpRetainTime

    @property
    def Vip(self):
        r"""New VIP.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def DRNetwork(self):
        r"""Target node. 0 - modify the primary node network; 1 - modify the secondary node network. The default value is 0.

        :rtype: int
        """
        return self._DRNetwork

    @DRNetwork.setter
    def DRNetwork(self, DRNetwork):
        self._DRNetwork = DRNetwork

    @property
    def DrInstanceId(self):
        r"""Secondary server resource ID. It is required when DRNetwork = 1.
        :rtype: str
        """
        return self._DrInstanceId

    @DrInstanceId.setter
    def DrInstanceId(self, DrInstanceId):
        self._DrInstanceId = DrInstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NewVpcId = params.get("NewVpcId")
        self._NewSubnetId = params.get("NewSubnetId")
        self._OldIpRetainTime = params.get("OldIpRetainTime")
        self._Vip = params.get("Vip")
        self._DRNetwork = params.get("DRNetwork")
        self._DrInstanceId = params.get("DrInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNetworkResponse(AbstractModel):
    r"""ModifyDBInstanceNetwork response structure.

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
        r"""ID of the instance network changing task. You can use the [DescribeFlowStatus](https://intl.cloud.tencent.com/document/product/238/19967?from_cn_redirect=1) API to query the task status.
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


class ModifyDBInstanceNoteRequest(AbstractModel):
    r"""ModifyDBInstanceNote request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID, in the format of mssql-njj2mtpl.
        :type InstanceId: str
        :param _InstanceNote: Instance remarks.
        :type InstanceNote: str
        """
        self._InstanceId = None
        self._InstanceNote = None

    @property
    def InstanceId(self):
        r"""Database instance ID, in the format of mssql-njj2mtpl.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceNote(self):
        r"""Instance remarks.
        :rtype: str
        """
        return self._InstanceNote

    @InstanceNote.setter
    def InstanceNote(self, InstanceNote):
        self._InstanceNote = InstanceNote


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceNote = params.get("InstanceNote")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNoteResponse(AbstractModel):
    r"""ModifyDBInstanceNote response structure.

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


class ModifyDBInstanceProjectRequest(AbstractModel):
    r"""ModifyDBInstanceProject request structure.

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
        r"""Array of instance IDs in the format of mssql-j8kv137v
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def ProjectId(self):
        r"""Project ID. If this parameter is 0, the default project will be used
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
    r"""ModifyDBInstanceProject response structure.

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
        r"""Number of successfully modified instances
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


class ModifyDBInstanceSSLRequest(AbstractModel):
    r"""ModifyDBInstanceSSL request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Type: Operation type. enable - enable SSL; disable - disable SSL; renew - update the validity period of the certificate.
        :type Type: str
        :param _WaitSwitch: Operation settings. 0 - execute immediately; 1 - execute within the maintenance time. The default value is 0.
        :type WaitSwitch: int
        :param _IsKMS: Whether it is protected through KMS encryption. 0 - no; 1 - yes. The default value is 0.
        :type IsKMS: int
        :param _KeyId: This parameter is required when the value of IsKMS is 1.
        :type KeyId: str
        :param _KeyRegion: This parameter is required when the value of IsKMS is 1.
        :type KeyRegion: str
        """
        self._InstanceId = None
        self._Type = None
        self._WaitSwitch = None
        self._IsKMS = None
        self._KeyId = None
        self._KeyRegion = None

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
    def Type(self):
        r"""Operation type. enable - enable SSL; disable - disable SSL; renew - update the validity period of the certificate.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WaitSwitch(self):
        r"""Operation settings. 0 - execute immediately; 1 - execute within the maintenance time. The default value is 0.
        :rtype: int
        """
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch

    @property
    def IsKMS(self):
        r"""Whether it is protected through KMS encryption. 0 - no; 1 - yes. The default value is 0.
        :rtype: int
        """
        return self._IsKMS

    @IsKMS.setter
    def IsKMS(self, IsKMS):
        self._IsKMS = IsKMS

    @property
    def KeyId(self):
        r"""This parameter is required when the value of IsKMS is 1.
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyRegion(self):
        r"""This parameter is required when the value of IsKMS is 1.
        :rtype: str
        """
        return self._KeyRegion

    @KeyRegion.setter
    def KeyRegion(self, KeyRegion):
        self._KeyRegion = KeyRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._WaitSwitch = params.get("WaitSwitch")
        self._IsKMS = params.get("IsKMS")
        self._KeyId = params.get("KeyId")
        self._KeyRegion = params.get("KeyRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSSLResponse(AbstractModel):
    r"""ModifyDBInstanceSSL response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Asynchronous task flow ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Asynchronous task flow ID.
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


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    r"""ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-c1nl9rpv or mssqlro-c1nl9rpv, which is the same as that displayed on the cloud database console page.
        :type InstanceId: str
        :param _SecurityGroupIdSet: List of security group IDs to be modified, which is an array of one or more security group IDs.
        :type SecurityGroupIdSet: list of str
        """
        self._InstanceId = None
        self._SecurityGroupIdSet = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-c1nl9rpv or mssqlro-c1nl9rpv, which is the same as that displayed on the cloud database console page.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIdSet(self):
        r"""List of security group IDs to be modified, which is an array of one or more security group IDs.
        :rtype: list of str
        """
        return self._SecurityGroupIdSet

    @SecurityGroupIdSet.setter
    def SecurityGroupIdSet(self, SecurityGroupIdSet):
        self._SecurityGroupIdSet = SecurityGroupIdSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIdSet = params.get("SecurityGroupIdSet")
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


class ModifyDBNameRequest(AbstractModel):
    r"""ModifyDBName request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldDBName(self):
        r"""Old database name
        :rtype: str
        """
        return self._OldDBName

    @OldDBName.setter
    def OldDBName(self, OldDBName):
        self._OldDBName = OldDBName

    @property
    def NewDBName(self):
        r"""New name of database
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
    r"""ModifyDBName response structure.

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
        r"""Task flow ID
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


class ModifyDBRemarkRequest(AbstractModel):
    r"""ModifyDBRemark request structure.

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
        r"""Instance ID in the format of mssql-rljoi3bf
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBRemarks(self):
        r"""Array of database names and remarks, where each element contains a database name and the corresponding remarks
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
    r"""ModifyDBRemark response structure.

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


class ModifyDReadableRequest(AbstractModel):
    r"""ModifyDReadable request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        r"""Operation type. Valid values: enable - enabling the read-only mode of the replica server; disable - disabling the read-only mode of the replica server
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VpcId(self):
        r"""Replica server network ID, which will be consistent with the primary instance by default if left blank
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Replica server subnet ID, which will be consistent with the primary instance by default if left blank
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        r"""Specified replica server read-only VIP, which will be assigned automatically if left blank
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
    r"""ModifyDReadable response structure.

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


class ModifyDataBaseTuple(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _DatabaseTuple: 
        :type DatabaseTuple: :class:`tencentcloud.sqlserver.v20180328.models.DatabaseTuple`
        :param _NewDatabaseTuple: 
        :type NewDatabaseTuple: :class:`tencentcloud.sqlserver.v20180328.models.DatabaseTuple`
        :param _DeleteDataBasesTuple: 
        :type DeleteDataBasesTuple: bool
        """
        self._DatabaseTuple = None
        self._NewDatabaseTuple = None
        self._DeleteDataBasesTuple = None

    @property
    def DatabaseTuple(self):
        r"""
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DatabaseTuple`
        """
        return self._DatabaseTuple

    @DatabaseTuple.setter
    def DatabaseTuple(self, DatabaseTuple):
        self._DatabaseTuple = DatabaseTuple

    @property
    def NewDatabaseTuple(self):
        r"""
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DatabaseTuple`
        """
        return self._NewDatabaseTuple

    @NewDatabaseTuple.setter
    def NewDatabaseTuple(self, NewDatabaseTuple):
        self._NewDatabaseTuple = NewDatabaseTuple

    @property
    def DeleteDataBasesTuple(self):
        r"""
        :rtype: bool
        """
        return self._DeleteDataBasesTuple

    @DeleteDataBasesTuple.setter
    def DeleteDataBasesTuple(self, DeleteDataBasesTuple):
        self._DeleteDataBasesTuple = DeleteDataBasesTuple


    def _deserialize(self, params):
        if params.get("DatabaseTuple") is not None:
            self._DatabaseTuple = DatabaseTuple()
            self._DatabaseTuple._deserialize(params.get("DatabaseTuple"))
        if params.get("NewDatabaseTuple") is not None:
            self._NewDatabaseTuple = DatabaseTuple()
            self._NewDatabaseTuple._deserialize(params.get("NewDatabaseTuple"))
        self._DeleteDataBasesTuple = params.get("DeleteDataBasesTuple")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseCDCRequest(AbstractModel):
    r"""ModifyDatabaseCDC request structure.

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
        r"""Array of database names
        :rtype: list of str
        """
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def ModifyType(self):
        r"""Enable or disable CDC. Valid values: `enable`, `disable`
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def InstanceId(self):
        r"""Instance ID
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
    r"""ModifyDatabaseCDC response structure.

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


class ModifyDatabaseCTRequest(AbstractModel):
    r"""ModifyDatabaseCT request structure.

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
        r"""Array of database names
        :rtype: list of str
        """
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def ModifyType(self):
        r"""Enable or disable CT. Valid values: `enable`, `disable`
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChangeRetentionDay(self):
        r"""Retention period (in days) of change tracking information when CT is enabled. Value range: 3-30. Default value: `3`
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
    r"""ModifyDatabaseCT response structure.

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


class ModifyDatabaseMdfRequest(AbstractModel):
    r"""ModifyDatabaseMdf request structure.

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
        r"""Array of database names
        :rtype: list of str
        """
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

    @property
    def InstanceId(self):
        r"""Instance ID
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
    r"""ModifyDatabaseMdf response structure.

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


class ModifyDatabasePrivilegeRequest(AbstractModel):
    r"""ModifyDatabasePrivilege request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-njj2mtpl.
        :type InstanceId: str
        :param _DataBaseSet: Database permission change information.
        :type DataBaseSet: list of DataBasePrivilegeModifyInfo
        """
        self._InstanceId = None
        self._DataBaseSet = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-njj2mtpl.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataBaseSet(self):
        r"""Database permission change information.
        :rtype: list of DataBasePrivilegeModifyInfo
        """
        return self._DataBaseSet

    @DataBaseSet.setter
    def DataBaseSet(self, DataBaseSet):
        self._DataBaseSet = DataBaseSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DataBaseSet") is not None:
            self._DataBaseSet = []
            for item in params.get("DataBaseSet"):
                obj = DataBasePrivilegeModifyInfo()
                obj._deserialize(item)
                self._DataBaseSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabasePrivilegeResponse(AbstractModel):
    r"""ModifyDatabasePrivilege response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Asynchronous task flow ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Asynchronous task flow ID.
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


class ModifyDatabaseShrinkMDFRequest(AbstractModel):
    r"""ModifyDatabaseShrinkMDF request structure.

    """

    def __init__(self):
        r"""
        :param _DBNames: Database name array.
        :type DBNames: list of str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._DBNames = None
        self._InstanceId = None

    @property
    def DBNames(self):
        r"""Database name array.
        :rtype: list of str
        """
        return self._DBNames

    @DBNames.setter
    def DBNames(self, DBNames):
        self._DBNames = DBNames

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
        self._DBNames = params.get("DBNames")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseShrinkMDFResponse(AbstractModel):
    r"""ModifyDatabaseShrinkMDF response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Process ID.
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


class ModifyIncrementalMigrationRequest(AbstractModel):
    r"""ModifyIncrementalMigration request structure.

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
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        r"""Incremental backup import task ID, which is returned through the `CreateIncrementalMigration` API.
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId

    @property
    def IsRecovery(self):
        r"""Whether to restore backups. Valid values: `NO`, `YES`. If this parameter is not specified, current settings will be applied.
        :rtype: str
        """
        return self._IsRecovery

    @IsRecovery.setter
    def IsRecovery(self, IsRecovery):
        self._IsRecovery = IsRecovery

    @property
    def BackupFiles(self):
        r"""If the UploadType is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
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
    r"""ModifyIncrementalMigration response structure.

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
        r"""ID of an incremental backup import task
        :rtype: str
        """
        return self._IncrementalMigrationId

    @IncrementalMigrationId.setter
    def IncrementalMigrationId(self, IncrementalMigrationId):
        self._IncrementalMigrationId = IncrementalMigrationId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""ModifyInstanceEncryptAttributes request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CertificateAttribution(self):
        r"""Certificate ownership. Valid values: `self` (certificate of this account), `others` (certificate of the other account). Default value: `self`.
        :rtype: str
        """
        return self._CertificateAttribution

    @CertificateAttribution.setter
    def CertificateAttribution(self, CertificateAttribution):
        self._CertificateAttribution = CertificateAttribution

    @property
    def QuoteUin(self):
        r"""ID of the other referenced root account, which is required when `CertificateAttribution` is `others`.
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
    r"""ModifyInstanceEncryptAttributes response structure.

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
        r"""Task flow ID
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


class ModifyInstanceParamRequest(AbstractModel):
    r"""ModifyInstanceParam request structure.

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
        r"""Instance ID list.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamList(self):
        r"""List of modified parameters. Each list element has two fields: `Name` and `CurrentValue`. Set `Name` to the parameter name and `CurrentValue` to the new value after modification. <b>Note</b>: if the instance needs to be <b>restarted</b> for the modified parameter to take effect, it will be <b>restarted</b> immediately or during the maintenance time. Before you modify a parameter, you can use the `DescribeInstanceParams` API to query whether the instance needs to be restarted.
        :rtype: list of Parameter
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def WaitSwitch(self):
        r"""When to execute the parameter modification task. Valid values: `0` (execute immediately), `1` (execute during maintenance time). Default value: `0`.
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
    r"""ModifyInstanceParam response structure.

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


class ModifyMaintenanceSpanRequest(AbstractModel):
    r"""ModifyMaintenanceSpan request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-k8voqdlz.
        :type InstanceId: str
        :param _Weekly: Specifies the days in each week allowed for maintenance. For example, [1,2,3,4,5,6,7] indicates that all days from Monday to Sunday are allowed for maintenance. If this parameter is left unspecified, this value is not modified.
        :type Weekly: list of int
        :param _StartTime: Maintenance start time each day. For example, 10:24 indicates that the maintenance window starts at 10:24. If this parameter is left unspecified, this value is not modified.
        :type StartTime: str
        :param _Span: Maintenance duration each day, in hours. For example, 1 indicates that the duration is 1 hour after maintenance starts. If this parameter is left unspecified, this value is not modified.
        :type Span: int
        """
        self._InstanceId = None
        self._Weekly = None
        self._StartTime = None
        self._Span = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-k8voqdlz.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weekly(self):
        r"""Specifies the days in each week allowed for maintenance. For example, [1,2,3,4,5,6,7] indicates that all days from Monday to Sunday are allowed for maintenance. If this parameter is left unspecified, this value is not modified.
        :rtype: list of int
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly

    @property
    def StartTime(self):
        r"""Maintenance start time each day. For example, 10:24 indicates that the maintenance window starts at 10:24. If this parameter is left unspecified, this value is not modified.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Span(self):
        r"""Maintenance duration each day, in hours. For example, 1 indicates that the duration is 1 hour after maintenance starts. If this parameter is left unspecified, this value is not modified.
        :rtype: int
        """
        return self._Span

    @Span.setter
    def Span(self, Span):
        self._Span = Span


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Weekly = params.get("Weekly")
        self._StartTime = params.get("StartTime")
        self._Span = params.get("Span")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintenanceSpanResponse(AbstractModel):
    r"""ModifyMaintenanceSpan response structure.

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


class ModifyMigrationRequest(AbstractModel):
    r"""ModifyMigration request structure.

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
        r"""Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def MigrateName(self):
        r"""New name of migration task. If this parameter is left empty, no modification will be made
        :rtype: str
        """
        return self._MigrateName

    @MigrateName.setter
    def MigrateName(self, MigrateName):
        self._MigrateName = MigrateName

    @property
    def MigrateType(self):
        r"""New migration type (1: structure migration, 2: data migration, 3: incremental sync). If this parameter is left empty, no modification will be made
        :rtype: int
        """
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def SourceType(self):
        r"""Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode). If this parameter is left empty, no modification will be made
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Source(self):
        r"""Migration source. If this parameter is left empty, no modification will be made
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""Migration target. If this parameter is left empty, no modification will be made
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def MigrateDBSet(self):
        r"""Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5). If it left empty, no modification will be made
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
    r"""ModifyMigration response structure.

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
        r"""Migration task ID
        :rtype: int
        """
        return self._MigrateId

    @MigrateId.setter
    def MigrateId(self, MigrateId):
        self._MigrateId = MigrateId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MigrateId = params.get("MigrateId")
        self._RequestId = params.get("RequestId")


class ModifyOpenWanIpRequest(AbstractModel):
    r"""ModifyOpenWanIp request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance resource ID. 
        :type InstanceId: str
        :param _RoGroupId: RO group ID.
        :type RoGroupId: str
        """
        self._InstanceId = None
        self._RoGroupId = None

    @property
    def InstanceId(self):
        r"""Instance resource ID. 
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RoGroupId(self):
        r"""RO group ID.
        :rtype: str
        """
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RoGroupId = params.get("RoGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOpenWanIpResponse(AbstractModel):
    r"""ModifyOpenWanIp response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: ID of the process of enabling the public network.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""ID of the process of enabling the public network.
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


class ModifyPublishSubscribeNameRequest(AbstractModel):
    r"""ModifyPublishSubscribeName request structure.

    """

    def __init__(self):
        r"""
        :param _PublishSubscribeId: Publish/subscribe ID.
        :type PublishSubscribeId: int
        :param _PublishSubscribeName: Publish/subscribe name to be modified.
        :type PublishSubscribeName: str
        """
        self._PublishSubscribeId = None
        self._PublishSubscribeName = None

    @property
    def PublishSubscribeId(self):
        r"""Publish/subscribe ID.
        :rtype: int
        """
        return self._PublishSubscribeId

    @PublishSubscribeId.setter
    def PublishSubscribeId(self, PublishSubscribeId):
        self._PublishSubscribeId = PublishSubscribeId

    @property
    def PublishSubscribeName(self):
        r"""Publish/subscribe name to be modified.
        :rtype: str
        """
        return self._PublishSubscribeName

    @PublishSubscribeName.setter
    def PublishSubscribeName(self, PublishSubscribeName):
        self._PublishSubscribeName = PublishSubscribeName


    def _deserialize(self, params):
        self._PublishSubscribeId = params.get("PublishSubscribeId")
        self._PublishSubscribeName = params.get("PublishSubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPublishSubscribeNameResponse(AbstractModel):
    r"""ModifyPublishSubscribeName response structure.

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


class ModifyPublishSubscribeRequest(AbstractModel):
    r"""ModifyPublishSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. For example: mssql-dg32dcv.
        :type InstanceId: str
        :param _PublishSubscribeId: Publish/subscribe ID.
        :type PublishSubscribeId: int
        :param _DatabaseTupleSet: Publish/subscribe relationship collection of the database to be modified.
        :type DatabaseTupleSet: list of ModifyDataBaseTuple
        """
        self._InstanceId = None
        self._PublishSubscribeId = None
        self._DatabaseTupleSet = None

    @property
    def InstanceId(self):
        r"""Instance ID. For example: mssql-dg32dcv.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PublishSubscribeId(self):
        r"""Publish/subscribe ID.
        :rtype: int
        """
        return self._PublishSubscribeId

    @PublishSubscribeId.setter
    def PublishSubscribeId(self, PublishSubscribeId):
        self._PublishSubscribeId = PublishSubscribeId

    @property
    def DatabaseTupleSet(self):
        r"""Publish/subscribe relationship collection of the database to be modified.
        :rtype: list of ModifyDataBaseTuple
        """
        return self._DatabaseTupleSet

    @DatabaseTupleSet.setter
    def DatabaseTupleSet(self, DatabaseTupleSet):
        self._DatabaseTupleSet = DatabaseTupleSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PublishSubscribeId = params.get("PublishSubscribeId")
        if params.get("DatabaseTupleSet") is not None:
            self._DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = ModifyDataBaseTuple()
                obj._deserialize(item)
                self._DatabaseTupleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPublishSubscribeResponse(AbstractModel):
    r"""ModifyPublishSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task flow ID.
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


class ModifyReadOnlyGroupDetailsRequest(AbstractModel):
    r"""ModifyReadOnlyGroupDetails request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Primary instance ID, in the format of mssql-3l3fgqn7.
        :type InstanceId: str
        :param _ReadOnlyGroupId: Read-only group ID.
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: Read-only group name. The modification is not performed if this parameter is left unspecified.
        :type ReadOnlyGroupName: str
        :param _IsOfflineDelay: Whether to enable the delayed read-only instance removal feature. 0 - disabled; 1 - enabled. The modification is not performed if this parameter is left unspecified.
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: Timeout threshold used after the delayed read-only instance removal feature is enabled. The modification is not performed if this parameter is left unspecified.
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: Minimum number of retained read-only replicas in the read-only group, after the delayed read-only instance removal feature is enabled. The modification is not performed if this parameter is left unspecified.
        :type MinReadOnlyInGroup: int
        :param _WeightPairs: Collection of read-only group instance weight modification. The modification is not performed if this parameter is left unspecified.
        :type WeightPairs: list of ReadOnlyInstanceWeightPair
        :param _AutoWeight: 0 - user-defined weight (adjust according to WeightPairs); 1 - automatically assigned weight by the system (invalid WeightPairs). The default value is 0.
        :type AutoWeight: int
        :param _BalanceWeight: 0 - not rebalance the load; 1 - rebalance the load. The default value is 0.
        :type BalanceWeight: int
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._WeightPairs = None
        self._AutoWeight = None
        self._BalanceWeight = None

    @property
    def InstanceId(self):
        r"""Primary instance ID, in the format of mssql-3l3fgqn7.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""Read-only group ID.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""Read-only group name. The modification is not performed if this parameter is left unspecified.
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def IsOfflineDelay(self):
        r"""Whether to enable the delayed read-only instance removal feature. 0 - disabled; 1 - enabled. The modification is not performed if this parameter is left unspecified.
        :rtype: int
        """
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        r"""Timeout threshold used after the delayed read-only instance removal feature is enabled. The modification is not performed if this parameter is left unspecified.
        :rtype: int
        """
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        r"""Minimum number of retained read-only replicas in the read-only group, after the delayed read-only instance removal feature is enabled. The modification is not performed if this parameter is left unspecified.
        :rtype: int
        """
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def WeightPairs(self):
        r"""Collection of read-only group instance weight modification. The modification is not performed if this parameter is left unspecified.
        :rtype: list of ReadOnlyInstanceWeightPair
        """
        return self._WeightPairs

    @WeightPairs.setter
    def WeightPairs(self, WeightPairs):
        self._WeightPairs = WeightPairs

    @property
    def AutoWeight(self):
        r"""0 - user-defined weight (adjust according to WeightPairs); 1 - automatically assigned weight by the system (invalid WeightPairs). The default value is 0.
        :rtype: int
        """
        return self._AutoWeight

    @AutoWeight.setter
    def AutoWeight(self, AutoWeight):
        self._AutoWeight = AutoWeight

    @property
    def BalanceWeight(self):
        r"""0 - not rebalance the load; 1 - rebalance the load. The default value is 0.
        :rtype: int
        """
        return self._BalanceWeight

    @BalanceWeight.setter
    def BalanceWeight(self, BalanceWeight):
        self._BalanceWeight = BalanceWeight


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        if params.get("WeightPairs") is not None:
            self._WeightPairs = []
            for item in params.get("WeightPairs"):
                obj = ReadOnlyInstanceWeightPair()
                obj._deserialize(item)
                self._WeightPairs.append(obj)
        self._AutoWeight = params.get("AutoWeight")
        self._BalanceWeight = params.get("BalanceWeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyGroupDetailsResponse(AbstractModel):
    r"""ModifyReadOnlyGroupDetails response structure.

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


class OldVip(AbstractModel):
    r"""This API is used to return the number of unrecovered IP addresses for the instance.

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
        r"""Unrecovered old IP addresses
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def RecycleTime(self):
        r"""IP recovery time
        :rtype: str
        """
        return self._RecycleTime

    @RecycleTime.setter
    def RecycleTime(self, RecycleTime):
        self._RecycleTime = RecycleTime

    @property
    def OldIpRetainTime(self):
        r"""Old IP retention time (hours)
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
    r"""OpenInterCommunication request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: IDs of instances with interwoking group enabled
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        r"""IDs of instances with interwoking group enabled
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
    r"""OpenInterCommunication response structure.

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
        r"""IDs of instance and async task
        :rtype: list of InterInstanceFlow
        """
        return self._InterInstanceFlowSet

    @InterInstanceFlowSet.setter
    def InterInstanceFlowSet(self, InterInstanceFlowSet):
        self._InterInstanceFlowSet = InterInstanceFlowSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""Instance parameter modification record

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ParamName(self):
        r"""Parameter name
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def OldValue(self):
        r"""Parameter value before modification
        :rtype: str
        """
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        r"""Parameter value after modification
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def Status(self):
        r"""Parameter modification status. Valid values: `1` (initializing and waiting for modification), `2` (modification succeed), `3` (modification failed), `4` (modifying)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        r"""Modification time
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
    r"""Database instance parameter

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
        r"""Parameter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CurrentValue(self):
        r"""Parameter value
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
    r"""Instance parameter details

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
        r"""Parameter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamType(self):
        r"""Data type of the parameter. Valid values: `integer`, `enum`
        :rtype: str
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Default(self):
        r"""Default value of the parameter
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        r"""Parameter description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        r"""Current value of the parameter
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        r"""Whether the database needs to be restarted for the modified parameter to take effect. Valid values: `0` (no),`1` (yes)
        :rtype: int
        """
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        r"""Maximum value of the parameter
        :rtype: int
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        r"""Minimum value of the parameter
        :rtype: int
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        r"""Enumerated values of the parameter
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
        r"""Parameter status. Valid values: `0` (normal), `1` (modifying)
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
        


class Price(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _PrepaidPrice: 
        :type PrepaidPrice: int
        :param _PrepaidPriceUnit: 
        :type PrepaidPriceUnit: str
        :param _PostpaidPrice: 
        :type PostpaidPrice: int
        :param _PostpaidPriceUnit: 
        :type PostpaidPriceUnit: str
        """
        self._PrepaidPrice = None
        self._PrepaidPriceUnit = None
        self._PostpaidPrice = None
        self._PostpaidPriceUnit = None

    @property
    def PrepaidPrice(self):
        r"""
        :rtype: int
        """
        return self._PrepaidPrice

    @PrepaidPrice.setter
    def PrepaidPrice(self, PrepaidPrice):
        self._PrepaidPrice = PrepaidPrice

    @property
    def PrepaidPriceUnit(self):
        r"""
        :rtype: str
        """
        return self._PrepaidPriceUnit

    @PrepaidPriceUnit.setter
    def PrepaidPriceUnit(self, PrepaidPriceUnit):
        self._PrepaidPriceUnit = PrepaidPriceUnit

    @property
    def PostpaidPrice(self):
        r"""
        :rtype: int
        """
        return self._PostpaidPrice

    @PostpaidPrice.setter
    def PostpaidPrice(self, PostpaidPrice):
        self._PostpaidPrice = PostpaidPrice

    @property
    def PostpaidPriceUnit(self):
        r"""
        :rtype: str
        """
        return self._PostpaidPriceUnit

    @PostpaidPriceUnit.setter
    def PostpaidPriceUnit(self, PostpaidPriceUnit):
        self._PostpaidPriceUnit = PostpaidPriceUnit


    def _deserialize(self, params):
        self._PrepaidPrice = params.get("PrepaidPrice")
        self._PrepaidPriceUnit = params.get("PrepaidPriceUnit")
        self._PostpaidPrice = params.get("PostpaidPrice")
        self._PostpaidPriceUnit = params.get("PostpaidPriceUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishSubscribe(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Id: 
        :type Id: int
        :param _Name: 
        :type Name: str
        :param _PublishInstanceId: 
        :type PublishInstanceId: str
        :param _PublishInstanceName: 
        :type PublishInstanceName: str
        :param _PublishInstanceIp: 
        :type PublishInstanceIp: str
        :param _SubscribeInstanceId: 
        :type SubscribeInstanceId: str
        :param _SubscribeInstanceName: 
        :type SubscribeInstanceName: str
        :param _SubscribeInstanceIp: 
        :type SubscribeInstanceIp: str
        :param _DatabaseTupleSet: 
        :type DatabaseTupleSet: list of DatabaseTupleStatus
        """
        self._Id = None
        self._Name = None
        self._PublishInstanceId = None
        self._PublishInstanceName = None
        self._PublishInstanceIp = None
        self._SubscribeInstanceId = None
        self._SubscribeInstanceName = None
        self._SubscribeInstanceIp = None
        self._DatabaseTupleSet = None

    @property
    def Id(self):
        r"""
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PublishInstanceId(self):
        r"""
        :rtype: str
        """
        return self._PublishInstanceId

    @PublishInstanceId.setter
    def PublishInstanceId(self, PublishInstanceId):
        self._PublishInstanceId = PublishInstanceId

    @property
    def PublishInstanceName(self):
        r"""
        :rtype: str
        """
        return self._PublishInstanceName

    @PublishInstanceName.setter
    def PublishInstanceName(self, PublishInstanceName):
        self._PublishInstanceName = PublishInstanceName

    @property
    def PublishInstanceIp(self):
        r"""
        :rtype: str
        """
        return self._PublishInstanceIp

    @PublishInstanceIp.setter
    def PublishInstanceIp(self, PublishInstanceIp):
        self._PublishInstanceIp = PublishInstanceIp

    @property
    def SubscribeInstanceId(self):
        r"""
        :rtype: str
        """
        return self._SubscribeInstanceId

    @SubscribeInstanceId.setter
    def SubscribeInstanceId(self, SubscribeInstanceId):
        self._SubscribeInstanceId = SubscribeInstanceId

    @property
    def SubscribeInstanceName(self):
        r"""
        :rtype: str
        """
        return self._SubscribeInstanceName

    @SubscribeInstanceName.setter
    def SubscribeInstanceName(self, SubscribeInstanceName):
        self._SubscribeInstanceName = SubscribeInstanceName

    @property
    def SubscribeInstanceIp(self):
        r"""
        :rtype: str
        """
        return self._SubscribeInstanceIp

    @SubscribeInstanceIp.setter
    def SubscribeInstanceIp(self, SubscribeInstanceIp):
        self._SubscribeInstanceIp = SubscribeInstanceIp

    @property
    def DatabaseTupleSet(self):
        r"""
        :rtype: list of DatabaseTupleStatus
        """
        return self._DatabaseTupleSet

    @DatabaseTupleSet.setter
    def DatabaseTupleSet(self, DatabaseTupleSet):
        self._DatabaseTupleSet = DatabaseTupleSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._PublishInstanceId = params.get("PublishInstanceId")
        self._PublishInstanceName = params.get("PublishInstanceName")
        self._PublishInstanceIp = params.get("PublishInstanceIp")
        self._SubscribeInstanceId = params.get("SubscribeInstanceId")
        self._SubscribeInstanceName = params.get("SubscribeInstanceName")
        self._SubscribeInstanceIp = params.get("SubscribeInstanceIp")
        if params.get("DatabaseTupleSet") is not None:
            self._DatabaseTupleSet = []
            for item in params.get("DatabaseTupleSet"):
                obj = DatabaseTupleStatus()
                obj._deserialize(item)
                self._DatabaseTupleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMigrationCheckProcessRequest(AbstractModel):
    r"""QueryMigrationCheckProcess request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID.
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        r"""Migration task ID.
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
        


class QueryMigrationCheckProcessResponse(AbstractModel):
    r"""QueryMigrationCheckProcess response structure.

    """

    def __init__(self):
        r"""
        :param _TotalStep: Total number of steps.
        :type TotalStep: int
        :param _CurrentStep: Current step number, starting from 1.
        :type CurrentStep: int
        :param _StepDetails: Details of all steps.
        :type StepDetails: list of StepDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalStep = None
        self._CurrentStep = None
        self._StepDetails = None
        self._RequestId = None

    @property
    def TotalStep(self):
        r"""Total number of steps.
        :rtype: int
        """
        return self._TotalStep

    @TotalStep.setter
    def TotalStep(self, TotalStep):
        self._TotalStep = TotalStep

    @property
    def CurrentStep(self):
        r"""Current step number, starting from 1.
        :rtype: int
        """
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def StepDetails(self):
        r"""Details of all steps.
        :rtype: list of StepDetail
        """
        return self._StepDetails

    @StepDetails.setter
    def StepDetails(self, StepDetails):
        self._StepDetails = StepDetails

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalStep = params.get("TotalStep")
        self._CurrentStep = params.get("CurrentStep")
        if params.get("StepDetails") is not None:
            self._StepDetails = []
            for item in params.get("StepDetails"):
                obj = StepDetail()
                obj._deserialize(item)
                self._StepDetails.append(obj)
        self._RequestId = params.get("RequestId")


class ReadOnlyGroup(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _ReadOnlyGroupId: 
        :type ReadOnlyGroupId: str
        :param _ReadOnlyGroupName: 
        :type ReadOnlyGroupName: str
        :param _RegionId: 
        :type RegionId: str
        :param _ZoneId: 
        :type ZoneId: str
        :param _IsOfflineDelay: 
        :type IsOfflineDelay: int
        :param _ReadOnlyMaxDelayTime: 
        :type ReadOnlyMaxDelayTime: int
        :param _MinReadOnlyInGroup: 
        :type MinReadOnlyInGroup: int
        :param _Vip: 
        :type Vip: str
        :param _Vport: 
        :type Vport: int
        :param _VpcId: 
        :type VpcId: str
        :param _SubnetId: 
        :type SubnetId: str
        :param _Status: 
        :type Status: int
        :param _MasterInstanceId: 
        :type MasterInstanceId: str
        :param _ReadOnlyInstanceSet: 
        :type ReadOnlyInstanceSet: list of ReadOnlyInstance
        :param _DnsPodDomain: RO group's public network address domain name
        :type DnsPodDomain: str
        :param _TgwWanVPort: RO group's public network address port
        :type TgwWanVPort: int
        """
        self._ReadOnlyGroupId = None
        self._ReadOnlyGroupName = None
        self._RegionId = None
        self._ZoneId = None
        self._IsOfflineDelay = None
        self._ReadOnlyMaxDelayTime = None
        self._MinReadOnlyInGroup = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._MasterInstanceId = None
        self._ReadOnlyInstanceSet = None
        self._DnsPodDomain = None
        self._TgwWanVPort = None

    @property
    def ReadOnlyGroupId(self):
        r"""
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId

    @property
    def ReadOnlyGroupName(self):
        r"""
        :rtype: str
        """
        return self._ReadOnlyGroupName

    @ReadOnlyGroupName.setter
    def ReadOnlyGroupName(self, ReadOnlyGroupName):
        self._ReadOnlyGroupName = ReadOnlyGroupName

    @property
    def RegionId(self):
        r"""
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsOfflineDelay(self):
        r"""
        :rtype: int
        """
        return self._IsOfflineDelay

    @IsOfflineDelay.setter
    def IsOfflineDelay(self, IsOfflineDelay):
        self._IsOfflineDelay = IsOfflineDelay

    @property
    def ReadOnlyMaxDelayTime(self):
        r"""
        :rtype: int
        """
        return self._ReadOnlyMaxDelayTime

    @ReadOnlyMaxDelayTime.setter
    def ReadOnlyMaxDelayTime(self, ReadOnlyMaxDelayTime):
        self._ReadOnlyMaxDelayTime = ReadOnlyMaxDelayTime

    @property
    def MinReadOnlyInGroup(self):
        r"""
        :rtype: int
        """
        return self._MinReadOnlyInGroup

    @MinReadOnlyInGroup.setter
    def MinReadOnlyInGroup(self, MinReadOnlyInGroup):
        self._MinReadOnlyInGroup = MinReadOnlyInGroup

    @property
    def Vip(self):
        r"""
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        r"""
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        r"""
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MasterInstanceId(self):
        r"""
        :rtype: str
        """
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def ReadOnlyInstanceSet(self):
        r"""
        :rtype: list of ReadOnlyInstance
        """
        return self._ReadOnlyInstanceSet

    @ReadOnlyInstanceSet.setter
    def ReadOnlyInstanceSet(self, ReadOnlyInstanceSet):
        self._ReadOnlyInstanceSet = ReadOnlyInstanceSet

    @property
    def DnsPodDomain(self):
        r"""RO group's public network address domain name
        :rtype: str
        """
        return self._DnsPodDomain

    @DnsPodDomain.setter
    def DnsPodDomain(self, DnsPodDomain):
        self._DnsPodDomain = DnsPodDomain

    @property
    def TgwWanVPort(self):
        r"""RO group's public network address port
        :rtype: int
        """
        return self._TgwWanVPort

    @TgwWanVPort.setter
    def TgwWanVPort(self, TgwWanVPort):
        self._TgwWanVPort = TgwWanVPort


    def _deserialize(self, params):
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self._ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._IsOfflineDelay = params.get("IsOfflineDelay")
        self._ReadOnlyMaxDelayTime = params.get("ReadOnlyMaxDelayTime")
        self._MinReadOnlyInGroup = params.get("MinReadOnlyInGroup")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._MasterInstanceId = params.get("MasterInstanceId")
        if params.get("ReadOnlyInstanceSet") is not None:
            self._ReadOnlyInstanceSet = []
            for item in params.get("ReadOnlyInstanceSet"):
                obj = ReadOnlyInstance()
                obj._deserialize(item)
                self._ReadOnlyInstanceSet.append(obj)
        self._DnsPodDomain = params.get("DnsPodDomain")
        self._TgwWanVPort = params.get("TgwWanVPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyInstance(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _InstanceId: 
        :type InstanceId: str
        :param _Name: 
        :type Name: str
        :param _Uid: 
        :type Uid: str
        :param _ProjectId: 
        :type ProjectId: int
        :param _Status: 
        :type Status: int
        :param _CreateTime: 
        :type CreateTime: str
        :param _UpdateTime: 
        :type UpdateTime: str
        :param _Memory: 
        :type Memory: int
        :param _Storage: 
        :type Storage: int
        :param _Cpu: 
        :type Cpu: int
        :param _Version: 
        :type Version: str
        :param _Type: 
        :type Type: str
        :param _Model: 
        :type Model: int
        :param _PayMode: 
        :type PayMode: int
        :param _Weight: 
        :type Weight: int
        :param _DelayTime: 
        :type DelayTime: str
        :param _SynStatus: 
        :type SynStatus: str
        :param _DatabaseDifference: 
        :type DatabaseDifference: str
        :param _AccountDifference: 
        :type AccountDifference: str
        :param _StartTime: 
        :type StartTime: str
        :param _EndTime: 
        :type EndTime: str
        :param _IsolateTime: 
        :type IsolateTime: str
        :param _RegionId: 
        :type RegionId: str
        :param _ZoneId: 
        :type ZoneId: str
        """
        self._InstanceId = None
        self._Name = None
        self._Uid = None
        self._ProjectId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Memory = None
        self._Storage = None
        self._Cpu = None
        self._Version = None
        self._Type = None
        self._Model = None
        self._PayMode = None
        self._Weight = None
        self._DelayTime = None
        self._SynStatus = None
        self._DatabaseDifference = None
        self._AccountDifference = None
        self._StartTime = None
        self._EndTime = None
        self._IsolateTime = None
        self._RegionId = None
        self._ZoneId = None

    @property
    def InstanceId(self):
        r"""
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        r"""
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def ProjectId(self):
        r"""
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        r"""
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Memory(self):
        r"""
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Cpu(self):
        r"""
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Version(self):
        r"""
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Type(self):
        r"""
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Model(self):
        r"""
        :rtype: int
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def PayMode(self):
        r"""
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Weight(self):
        r"""
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def DelayTime(self):
        r"""
        :rtype: str
        """
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime

    @property
    def SynStatus(self):
        r"""
        :rtype: str
        """
        return self._SynStatus

    @SynStatus.setter
    def SynStatus(self, SynStatus):
        self._SynStatus = SynStatus

    @property
    def DatabaseDifference(self):
        r"""
        :rtype: str
        """
        return self._DatabaseDifference

    @DatabaseDifference.setter
    def DatabaseDifference(self, DatabaseDifference):
        self._DatabaseDifference = DatabaseDifference

    @property
    def AccountDifference(self):
        r"""
        :rtype: str
        """
        return self._AccountDifference

    @AccountDifference.setter
    def AccountDifference(self, AccountDifference):
        self._AccountDifference = AccountDifference

    @property
    def StartTime(self):
        r"""
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IsolateTime(self):
        r"""
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def RegionId(self):
        r"""
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._Cpu = params.get("Cpu")
        self._Version = params.get("Version")
        self._Type = params.get("Type")
        self._Model = params.get("Model")
        self._PayMode = params.get("PayMode")
        self._Weight = params.get("Weight")
        self._DelayTime = params.get("DelayTime")
        self._SynStatus = params.get("SynStatus")
        self._DatabaseDifference = params.get("DatabaseDifference")
        self._AccountDifference = params.get("AccountDifference")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IsolateTime = params.get("IsolateTime")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyInstanceWeightPair(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _ReadOnlyInstanceId: 
        :type ReadOnlyInstanceId: str
        :param _ReadOnlyWeight: 
        :type ReadOnlyWeight: int
        """
        self._ReadOnlyInstanceId = None
        self._ReadOnlyWeight = None

    @property
    def ReadOnlyInstanceId(self):
        r"""
        :rtype: str
        """
        return self._ReadOnlyInstanceId

    @ReadOnlyInstanceId.setter
    def ReadOnlyInstanceId(self, ReadOnlyInstanceId):
        self._ReadOnlyInstanceId = ReadOnlyInstanceId

    @property
    def ReadOnlyWeight(self):
        r"""
        :rtype: int
        """
        return self._ReadOnlyWeight

    @ReadOnlyWeight.setter
    def ReadOnlyWeight(self, ReadOnlyWeight):
        self._ReadOnlyWeight = ReadOnlyWeight


    def _deserialize(self, params):
        self._ReadOnlyInstanceId = params.get("ReadOnlyInstanceId")
        self._ReadOnlyWeight = params.get("ReadOnlyWeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecycleDBInstanceRequest(AbstractModel):
    r"""RecycleDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID
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
    r"""RecycleDBInstance response structure.

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


class RecycleReadOnlyGroupRequest(AbstractModel):
    r"""RecycleReadOnlyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Primary instance ID.
        :type InstanceId: str
        :param _ReadOnlyGroupId: Read-only group ID.
        :type ReadOnlyGroupId: str
        """
        self._InstanceId = None
        self._ReadOnlyGroupId = None

    @property
    def InstanceId(self):
        r"""Primary instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadOnlyGroupId(self):
        r"""Read-only group ID.
        :rtype: str
        """
        return self._ReadOnlyGroupId

    @ReadOnlyGroupId.setter
    def ReadOnlyGroupId(self, ReadOnlyGroupId):
        self._ReadOnlyGroupId = ReadOnlyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecycleReadOnlyGroupResponse(AbstractModel):
    r"""RecycleReadOnlyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task flow ID.
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


class RegionInfo(AbstractModel):
    r"""Region information

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
        r"""Region ID in the format of ap-guangzhou
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
        r"""Numeric ID of region
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionState(self):
        r"""Current purchasability of this region. UNAVAILABLE: not purchasable, AVAILABLE: purchasable
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
        


class RemoveBackupsRequest(AbstractModel):
    r"""RemoveBackups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. For example, mssql-j8kv137v.
        :type InstanceId: str
        :param _BackupNames: Backup names to be deleted. Backup names can be obtained through the FileName field of the DescribeBackups API. The number of backups for batch deletion in a single request should not exceed 10. This field is required when the values of StartTime and EndTime are null.
        :type BackupNames: list of str
        :param _StartTime: Start time for batch deletion of manual backups. This field is required when the value of BackupNames is null.
        :type StartTime: str
        :param _EndTime: Deadline for batch deletion of manual backups. This field is required when the value of BackupNames is null.
        :type EndTime: str
        """
        self._InstanceId = None
        self._BackupNames = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        r"""Instance ID. For example, mssql-j8kv137v.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupNames(self):
        r"""Backup names to be deleted. Backup names can be obtained through the FileName field of the DescribeBackups API. The number of backups for batch deletion in a single request should not exceed 10. This field is required when the values of StartTime and EndTime are null.
        :rtype: list of str
        """
        return self._BackupNames

    @BackupNames.setter
    def BackupNames(self, BackupNames):
        self._BackupNames = BackupNames

    @property
    def StartTime(self):
        r"""Start time for batch deletion of manual backups. This field is required when the value of BackupNames is null.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Deadline for batch deletion of manual backups. This field is required when the value of BackupNames is null.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupNames = params.get("BackupNames")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveBackupsResponse(AbstractModel):
    r"""RemoveBackups response structure.

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


class RenameRestoreDatabase(AbstractModel):
    r"""It is used to specify and rename the database to be restored through the `RestoreInstance`, `RollbackInstance`, `CreateMigration`, `CloneDB` or `ModifyBackupMigration` APIs.

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
        r"""Database name. If the `OldName` database does not exist, a failure will be returned.
It can be left empty in offline migration tasks.
        :rtype: str
        """
        return self._OldName

    @OldName.setter
    def OldName(self, OldName):
        self._OldName = OldName

    @property
    def NewName(self):
        r"""New database name. In offline migration, `OldName` will be used if `NewName` is left empty (`OldName` and `NewName` cannot be both empty). In database cloning, `OldName` and `NewName` must be both specified and cannot have the same value.
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
        


class RenewPostpaidDBInstanceRequest(AbstractModel):
    r"""RenewPostpaidDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of mssql-3l3fgqn7 or mssqlro-3l3fgqn7.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of mssql-3l3fgqn7 or mssqlro-3l3fgqn7.
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
        


class RenewPostpaidDBInstanceResponse(AbstractModel):
    r"""RenewPostpaidDBInstance response structure.

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


class ResetAccountPasswordRequest(AbstractModel):
    r"""ResetAccountPassword request structure.

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
        r"""Database instance ID in the format of mssql-njj2mtpl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        r"""Updated account password information array
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
    r"""ResetAccountPassword response structure.

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
        r"""ID of asynchronous task flow for account password modification
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
    r"""The information of tags associated with instances

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
        


class RestartDBInstanceRequest(AbstractModel):
    r"""RestartDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Database instance ID in the format of mssql-njj2mtpl
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
    r"""RestartDBInstance response structure.

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
        r"""Async task flow ID
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


class RestoreInstanceRequest(AbstractModel):
    r"""RestoreInstance request structure.

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
        r"""Instance ID in the format of mssql-j8kv137v
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        r"""Backup file ID, which can be obtained through the `Id` field in the returned value of the `DescribeBackups` API
        :rtype: int
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def TargetInstanceId(self):
        r"""ID of the target instance to which the backup is restored. The target instance should be under the same `APPID`. If this parameter is left empty, ID of the source instance will be used.
        :rtype: str
        """
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def RenameRestore(self):
        r"""Restore the databases listed in `ReNameRestoreDatabase` and rename them after restoration. If this parameter is left empty, all databases will be restored and renamed in the default format.
        :rtype: list of RenameRestoreDatabase
        """
        return self._RenameRestore

    @RenameRestore.setter
    def RenameRestore(self, RenameRestore):
        self._RenameRestore = RenameRestore

    @property
    def Type(self):
        r"""Rollback type. Valid values: `0` (overwriting), `1` (renaming).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DBList(self):
        r"""Database to be overwritten, which is required when overwriting a rollback database.
        :rtype: list of str
        """
        return self._DBList

    @DBList.setter
    def DBList(self, DBList):
        self._DBList = DBList

    @property
    def GroupId(self):
        r"""Group ID of unarchived backup files grouped by backup task
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
    r"""RestoreInstance response structure.

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
        r"""Async flow task ID, which can be used to call the `DescribeFlowStatus` API to get the task execution status
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


class RestoreTask(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _TargetInstanceId: 
        :type TargetInstanceId: str
        :param _TargetInstanceName: 
        :type TargetInstanceName: str
        :param _TargetInstanceStatus: 
        :type TargetInstanceStatus: int
        :param _TargetRegion: 
        :type TargetRegion: str
        :param _RestoreId: 
        :type RestoreId: int
        :param _TargetType: 
        :type TargetType: int
        :param _RestoreType: 
        :type RestoreType: int
        :param _RestoreTime: 
        :type RestoreTime: str
        :param _StartTime: 
        :type StartTime: str
        :param _EndTime: 
        :type EndTime: str
        :param _Status: 
        :type Status: int
        :param _FlowId: 
        :type FlowId: int
        """
        self._TargetInstanceId = None
        self._TargetInstanceName = None
        self._TargetInstanceStatus = None
        self._TargetRegion = None
        self._RestoreId = None
        self._TargetType = None
        self._RestoreType = None
        self._RestoreTime = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._FlowId = None

    @property
    def TargetInstanceId(self):
        r"""
        :rtype: str
        """
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def TargetInstanceName(self):
        r"""
        :rtype: str
        """
        return self._TargetInstanceName

    @TargetInstanceName.setter
    def TargetInstanceName(self, TargetInstanceName):
        self._TargetInstanceName = TargetInstanceName

    @property
    def TargetInstanceStatus(self):
        r"""
        :rtype: int
        """
        return self._TargetInstanceStatus

    @TargetInstanceStatus.setter
    def TargetInstanceStatus(self, TargetInstanceStatus):
        self._TargetInstanceStatus = TargetInstanceStatus

    @property
    def TargetRegion(self):
        r"""
        :rtype: str
        """
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def RestoreId(self):
        r"""
        :rtype: int
        """
        return self._RestoreId

    @RestoreId.setter
    def RestoreId(self, RestoreId):
        self._RestoreId = RestoreId

    @property
    def TargetType(self):
        r"""
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def RestoreType(self):
        r"""
        :rtype: int
        """
        return self._RestoreType

    @RestoreType.setter
    def RestoreType(self, RestoreType):
        self._RestoreType = RestoreType

    @property
    def RestoreTime(self):
        r"""
        :rtype: str
        """
        return self._RestoreTime

    @RestoreTime.setter
    def RestoreTime(self, RestoreTime):
        self._RestoreTime = RestoreTime

    @property
    def StartTime(self):
        r"""
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FlowId(self):
        r"""
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._TargetInstanceId = params.get("TargetInstanceId")
        self._TargetInstanceName = params.get("TargetInstanceName")
        self._TargetInstanceStatus = params.get("TargetInstanceStatus")
        self._TargetRegion = params.get("TargetRegion")
        self._RestoreId = params.get("RestoreId")
        self._TargetType = params.get("TargetType")
        self._RestoreType = params.get("RestoreType")
        self._RestoreTime = params.get("RestoreTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstanceRequest(AbstractModel):
    r"""RollbackInstance request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        r"""Rollback type. 0: the database rolled back overwrites the original database; 1: the database rolled back is renamed and does not overwrite the original database
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        r"""Target time point for rollback
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def DBs(self):
        r"""Database to be rolled back
        :rtype: list of str
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs

    @property
    def TargetInstanceId(self):
        r"""ID of the target instance to which the backup is restored. The target instance should be under the same `APPID`. If this parameter is left empty, ID of the source instance will be used.
        :rtype: str
        """
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def RenameRestore(self):
        r"""Rename the databases listed in `ReNameRestoreDatabase`. This parameter takes effect only when `Type = 1` which indicates that backup rollback supports renaming databases. If it is left empty, databases will be renamed in the default format and the `DBs` parameter specifies the databases to be restored.
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
    r"""RollbackInstance response structure.

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
        r"""The async job ID
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


class RunMigrationRequest(AbstractModel):
    r"""RunMigration request structure.

    """

    def __init__(self):
        r"""
        :param _MigrateId: Migration task ID
        :type MigrateId: int
        """
        self._MigrateId = None

    @property
    def MigrateId(self):
        r"""Migration task ID
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
    r"""RunMigration response structure.

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
        r"""After the migration task starts, the flow ID will be returned
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


class SSLConfig(AbstractModel):
    r"""

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
        r"""
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def SSLValidityPeriod(self):
        r"""
        :rtype: str
        """
        return self._SSLValidityPeriod

    @SSLValidityPeriod.setter
    def SSLValidityPeriod(self, SSLValidityPeriod):
        self._SSLValidityPeriod = SSLValidityPeriod

    @property
    def SSLValidity(self):
        r"""
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
        


class SecurityGroup(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _ProjectId: 
        :type ProjectId: int
        :param _CreateTime: 
        :type CreateTime: str
        :param _InboundSet: 
        :type InboundSet: list of SecurityGroupPolicy
        :param _OutboundSet: 
        :type OutboundSet: list of SecurityGroupPolicy
        :param _SecurityGroupId: 
        :type SecurityGroupId: str
        :param _SecurityGroupName: 
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 
        :type SecurityGroupRemark: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._InboundSet = None
        self._OutboundSet = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None

    @property
    def ProjectId(self):
        r"""
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        r"""
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InboundSet(self):
        r"""
        :rtype: list of SecurityGroupPolicy
        """
        return self._InboundSet

    @InboundSet.setter
    def InboundSet(self, InboundSet):
        self._InboundSet = InboundSet

    @property
    def OutboundSet(self):
        r"""
        :rtype: list of SecurityGroupPolicy
        """
        return self._OutboundSet

    @OutboundSet.setter
    def OutboundSet(self, OutboundSet):
        self._OutboundSet = OutboundSet

    @property
    def SecurityGroupId(self):
        r"""
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        r"""
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        r"""
        :rtype: str
        """
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("InboundSet") is not None:
            self._InboundSet = []
            for item in params.get("InboundSet"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self._InboundSet.append(obj)
        if params.get("OutboundSet") is not None:
            self._OutboundSet = []
            for item in params.get("OutboundSet"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self._OutboundSet.append(obj)
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicy(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Action: 
        :type Action: str
        :param _CidrIp: 
        :type CidrIp: str
        :param _PortRange: 
        :type PortRange: str
        :param _IpProtocol: 
        :type IpProtocol: str
        :param _Dir: 
        :type Dir: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Dir = None

    @property
    def Action(self):
        r"""
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        r"""
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        r"""
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        r"""
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Dir(self):
        r"""
        :rtype: str
        """
        return self._Dir

    @Dir.setter
    def Dir(self, Dir):
        self._Dir = Dir


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Dir = params.get("Dir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveZones(AbstractModel):
    r"""Replica AZ information

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
        r"""Replica AZ region code
        :rtype: str
        """
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def SlaveZoneName(self):
        r"""Replica AZ
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
    r"""Slow query log file information

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
        r"""Unique ID of slow query log file
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
    def Count(self):
        r"""Number of logs in file
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def InternalAddr(self):
        r"""Download address for private network
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        r"""Download address for public network
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Status(self):
        r"""Status (1: success, 2: failure)
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
    r"""Slow query log file information

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
        r"""Unique ID of slow query log file
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
    def Count(self):
        r"""Number of logs in file
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def InternalAddr(self):
        r"""Download address for private network
        :rtype: str
        """
        return self._InternalAddr

    @InternalAddr.setter
    def InternalAddr(self, InternalAddr):
        self._InternalAddr = InternalAddr

    @property
    def ExternalAddr(self):
        r"""Download address for public network
        :rtype: str
        """
        return self._ExternalAddr

    @ExternalAddr.setter
    def ExternalAddr(self, ExternalAddr):
        self._ExternalAddr = ExternalAddr

    @property
    def Status(self):
        r"""Status (1: success, 2: failure)
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
    r"""Information of purchasable specification for an instance

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
        r"""Instance specification ID. The `SpecId` returned by `DescribeZones` together with the purchasable specification information returned by `DescribeProductConfig` can be used to find out what specifications can be purchased in a specified AZ
        :rtype: int
        """
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def MachineType(self):
        r"""Model ID
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineTypeName(self):
        r"""Model name
        :rtype: str
        """
        return self._MachineTypeName

    @MachineTypeName.setter
    def MachineTypeName(self, MachineTypeName):
        self._MachineTypeName = MachineTypeName

    @property
    def Version(self):
        r"""Database version information. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise)
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def VersionName(self):
        r"""Version name corresponding to the `Version` field
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Memory(self):
        r"""Memory size in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

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
    def MinStorage(self):
        r"""Minimum disk size under this specification in GB
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def MaxStorage(self):
        r"""Maximum disk size under this specification in GB
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def QPS(self):
        r"""QPS of this specification
        :rtype: int
        """
        return self._QPS

    @QPS.setter
    def QPS(self, QPS):
        self._QPS = QPS

    @property
    def SuitInfo(self):
        r"""Description of this specification
        :rtype: str
        """
        return self._SuitInfo

    @SuitInfo.setter
    def SuitInfo(self, SuitInfo):
        self._SuitInfo = SuitInfo

    @property
    def Pid(self):
        r"""Pid of this specification
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def PostPid(self):
        r"""Pay-as-you-go Pid list corresponding to this specification
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._PostPid

    @PostPid.setter
    def PostPid(self, PostPid):
        self._PostPid = PostPid

    @property
    def PayModeStatus(self):
        r"""Billing mode under this specification. POST: pay-as-you-go
        :rtype: str
        """
        return self._PayModeStatus

    @PayModeStatus.setter
    def PayModeStatus(self, PayModeStatus):
        self._PayModeStatus = PayModeStatus

    @property
    def InstanceType(self):
        r"""Instance type. Valid values: HA (High-Availability Edition, including dual-server high availability and AlwaysOn cluster), RO (read-only replica), SI (Basic Edition)
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MultiZonesStatus(self):
        r"""Whether multi-AZ deployment is supported. Valid values: MultiZones (only multi-AZ deployment is supported), SameZones (only single-AZ deployment is supported), ALL (both deployments are supported)
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
        


class SpecSellStatus(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Id: 
        :type Id: str
        :param _SpecId: 
        :type SpecId: int
        :param _PayModeStatus: 
        :type PayModeStatus: str
        :param _InstanceType: 
        :type InstanceType: str
        :param _MultiZonesStatus: 
        :type MultiZonesStatus: str
        :param _Architecture: 
        :type Architecture: str
        :param _Style: 
        :type Style: str
        :param _Version: 
        :type Version: str
        :param _ZoneStatusSet: 
        :type ZoneStatusSet: list of ZoneStatus
        :param _Price: 
        :type Price: :class:`tencentcloud.sqlserver.v20180328.models.Price`
        :param _Status: 
        :type Status: int
        """
        self._Id = None
        self._SpecId = None
        self._PayModeStatus = None
        self._InstanceType = None
        self._MultiZonesStatus = None
        self._Architecture = None
        self._Style = None
        self._Version = None
        self._ZoneStatusSet = None
        self._Price = None
        self._Status = None

    @property
    def Id(self):
        r"""
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SpecId(self):
        r"""
        :rtype: int
        """
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def PayModeStatus(self):
        r"""
        :rtype: str
        """
        return self._PayModeStatus

    @PayModeStatus.setter
    def PayModeStatus(self, PayModeStatus):
        self._PayModeStatus = PayModeStatus

    @property
    def InstanceType(self):
        r"""
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MultiZonesStatus(self):
        r"""
        :rtype: str
        """
        return self._MultiZonesStatus

    @MultiZonesStatus.setter
    def MultiZonesStatus(self, MultiZonesStatus):
        self._MultiZonesStatus = MultiZonesStatus

    @property
    def Architecture(self):
        r"""
        :rtype: str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def Style(self):
        r"""
        :rtype: str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Version(self):
        r"""
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ZoneStatusSet(self):
        r"""
        :rtype: list of ZoneStatus
        """
        return self._ZoneStatusSet

    @ZoneStatusSet.setter
    def ZoneStatusSet(self, ZoneStatusSet):
        self._ZoneStatusSet = ZoneStatusSet

    @property
    def Price(self):
        r"""
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.Price`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Status(self):
        r"""
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SpecId = params.get("SpecId")
        self._PayModeStatus = params.get("PayModeStatus")
        self._InstanceType = params.get("InstanceType")
        self._MultiZonesStatus = params.get("MultiZonesStatus")
        self._Architecture = params.get("Architecture")
        self._Style = params.get("Style")
        self._Version = params.get("Version")
        if params.get("ZoneStatusSet") is not None:
            self._ZoneStatusSet = []
            for item in params.get("ZoneStatusSet"):
                obj = ZoneStatus()
                obj._deserialize(item)
                self._ZoneStatusSet.append(obj)
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBackupMigrationRequest(AbstractModel):
    r"""StartBackupMigration request structure.

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
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the API CreateBackupMigration
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
    r"""StartBackupMigration response structure.

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


class StartIncrementalMigrationRequest(AbstractModel):
    r"""StartIncrementalMigration request structure.

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
        r"""ID of imported target instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMigrationId(self):
        r"""Backup import task ID, which is returned through the API CreateBackupMigration
        :rtype: str
        """
        return self._BackupMigrationId

    @BackupMigrationId.setter
    def BackupMigrationId(self, BackupMigrationId):
        self._BackupMigrationId = BackupMigrationId

    @property
    def IncrementalMigrationId(self):
        r"""ID of an incremental backup import task
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
    r"""StartIncrementalMigration response structure.

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


class StartInstanceXEventRequest(AbstractModel):
    r"""StartInstanceXEvent request structure.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EventConfig(self):
        r"""Whether to start or stop an extended event
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
    r"""StartInstanceXEvent response structure.

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


class StepDetail(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Msg: 
        :type Msg: str
        :param _Status: 
        :type Status: int
        :param _Name: 
        :type Name: str
        """
        self._Msg = None
        self._Status = None
        self._Name = None

    @property
    def Msg(self):
        r"""
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Status(self):
        r"""
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Name(self):
        r"""
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._Status = params.get("Status")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryDetailRes(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _RegionId: 
        :type RegionId: int
        :param _Status: 
        :type Status: int
        :param _InstanceId: 
        :type InstanceId: str
        :param _Name: 
        :type Name: str
        :param _ActualUsedSpace: 
        :type ActualUsedSpace: int
        :param _DataBackupSpace: 
        :type DataBackupSpace: int
        :param _DataBackupCount: 
        :type DataBackupCount: int
        :param _LogBackupSpace: 
        :type LogBackupSpace: int
        :param _LogBackupCount: 
        :type LogBackupCount: int
        :param _AutoBackupSpace: 
        :type AutoBackupSpace: int
        :param _AutoBackupCount: 
        :type AutoBackupCount: int
        :param _ManualBackupSpace: 
        :type ManualBackupSpace: int
        :param _ManualBackupCount: 
        :type ManualBackupCount: int
        :param _Region: 
        :type Region: str
        """
        self._RegionId = None
        self._Status = None
        self._InstanceId = None
        self._Name = None
        self._ActualUsedSpace = None
        self._DataBackupSpace = None
        self._DataBackupCount = None
        self._LogBackupSpace = None
        self._LogBackupCount = None
        self._AutoBackupSpace = None
        self._AutoBackupCount = None
        self._ManualBackupSpace = None
        self._ManualBackupCount = None
        self._Region = None

    @property
    def RegionId(self):
        r"""
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Status(self):
        r"""
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        r"""
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActualUsedSpace(self):
        r"""
        :rtype: int
        """
        return self._ActualUsedSpace

    @ActualUsedSpace.setter
    def ActualUsedSpace(self, ActualUsedSpace):
        self._ActualUsedSpace = ActualUsedSpace

    @property
    def DataBackupSpace(self):
        r"""
        :rtype: int
        """
        return self._DataBackupSpace

    @DataBackupSpace.setter
    def DataBackupSpace(self, DataBackupSpace):
        self._DataBackupSpace = DataBackupSpace

    @property
    def DataBackupCount(self):
        r"""
        :rtype: int
        """
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def LogBackupSpace(self):
        r"""
        :rtype: int
        """
        return self._LogBackupSpace

    @LogBackupSpace.setter
    def LogBackupSpace(self, LogBackupSpace):
        self._LogBackupSpace = LogBackupSpace

    @property
    def LogBackupCount(self):
        r"""
        :rtype: int
        """
        return self._LogBackupCount

    @LogBackupCount.setter
    def LogBackupCount(self, LogBackupCount):
        self._LogBackupCount = LogBackupCount

    @property
    def AutoBackupSpace(self):
        r"""
        :rtype: int
        """
        return self._AutoBackupSpace

    @AutoBackupSpace.setter
    def AutoBackupSpace(self, AutoBackupSpace):
        self._AutoBackupSpace = AutoBackupSpace

    @property
    def AutoBackupCount(self):
        r"""
        :rtype: int
        """
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def ManualBackupSpace(self):
        r"""
        :rtype: int
        """
        return self._ManualBackupSpace

    @ManualBackupSpace.setter
    def ManualBackupSpace(self, ManualBackupSpace):
        self._ManualBackupSpace = ManualBackupSpace

    @property
    def ManualBackupCount(self):
        r"""
        :rtype: int
        """
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def Region(self):
        r"""
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._ActualUsedSpace = params.get("ActualUsedSpace")
        self._DataBackupSpace = params.get("DataBackupSpace")
        self._DataBackupCount = params.get("DataBackupCount")
        self._LogBackupSpace = params.get("LogBackupSpace")
        self._LogBackupCount = params.get("LogBackupCount")
        self._AutoBackupSpace = params.get("AutoBackupSpace")
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._ManualBackupSpace = params.get("ManualBackupSpace")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchCloudInstanceHARequest(AbstractModel):
    r"""SwitchCloudInstanceHA request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _WaitSwitch: Switch execution method. 0 - execute immediately; 1 - execute within the time window. The default value is 0.
        :type WaitSwitch: int
        """
        self._InstanceId = None
        self._WaitSwitch = None

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
    def WaitSwitch(self):
        r"""Switch execution method. 0 - execute immediately; 1 - execute within the time window. The default value is 0.
        :rtype: int
        """
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchCloudInstanceHAResponse(AbstractModel):
    r"""SwitchCloudInstanceHA response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Asynchronous task flow ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Asynchronous task flow ID.
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


class SwitchLog(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _EventId: 
        :type EventId: str
        :param _SwitchType: 
        :type SwitchType: int
        :param _StartTime: 
        :type StartTime: str
        :param _EndTime: 
        :type EndTime: str
        :param _Reason: 
        :type Reason: str
        """
        self._EventId = None
        self._SwitchType = None
        self._StartTime = None
        self._EndTime = None
        self._Reason = None

    @property
    def EventId(self):
        r"""
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def SwitchType(self):
        r"""
        :rtype: int
        """
        return self._SwitchType

    @SwitchType.setter
    def SwitchType(self, SwitchType):
        self._SwitchType = SwitchType

    @property
    def StartTime(self):
        r"""
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Reason(self):
        r"""
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._SwitchType = params.get("SwitchType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TDEConfigAttribute(AbstractModel):
    r"""TDE configuration

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
        r"""TDE status. Valid values: `enable` (enabled), `disable` (disabled).
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def CertificateAttribution(self):
        r"""Certificate ownership. Valid values: `self` (certificate of the this account), `others` (certificate of the other account), `none` (no certificate).
        :rtype: str
        """
        return self._CertificateAttribution

    @CertificateAttribution.setter
    def CertificateAttribution(self, CertificateAttribution):
        self._CertificateAttribution = CertificateAttribution

    @property
    def QuoteUin(self):
        r"""Note: This field may return null, indicating that no valid values can be obtained.
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
    r"""TerminateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of instance IDs manually terminated in the format of [mssql-3l3fgqn7], which are the same as the instance IDs displayed on the TencentDB Console page
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        r"""List of instance IDs manually terminated in the format of [mssql-3l3fgqn7], which are the same as the instance IDs displayed on the TencentDB Console page
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
    r"""TerminateDBInstance response structure.

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
        :param _DrZones: Secondary node AZ of the multi-node architecture instance. The default value is null. It should be specified when modifying the AZ of the specified secondary node needs to be performed during configuration adjustment. When MultiZones = MultiZones, the AZs of the primary nodes and secondary nodes cannot all be the same. The collection of AZs of the secondary node can include 2-5 AZs.
        :type DrZones: list of DrZoneInfo
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
        self._DrZones = None

    @property
    def InstanceId(self):
        r"""Instance ID in the format of mssql-j8kv137v
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        r"""Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use vouchers. 0: no, 1: yes. Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID (currently, only one voucher can be used per order)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def Cpu(self):
        r"""The number of CUP cores after the instance is upgraded.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DBVersion(self):
        r"""Upgrade the SQL Server version. Supported versions include SQL Server 2008 Enterprise (`2008R2`), SQL Server 2012 Enterprise (`2012SP3`), etc. As the purchasable versions are region-specific, you can use the `DescribeProductConfig` API to query the information of purchasable versions in each region. Downgrading is unsupported. If this parameter is left empty, the SQL Server version will not be changed.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def HAType(self):
        r"""Upgrade the high availability architecture from image-based disaster recovery to Always On cluster disaster recovery. This parameter is valid only for instances which support Always On high availability and run SQL Server 2017 or later. Neither downgrading to image-based disaster recovery nor upgrading from cluster disaster recovery to Always On disaster recovery is supported. If this parameter is left empty, the high availability architecture will not be changed.
        :rtype: str
        """
        return self._HAType

    @HAType.setter
    def HAType(self, HAType):
        self._HAType = HAType

    @property
    def MultiZones(self):
        r"""Change the instance deployment scheme. Valid values: `SameZones` (change to single-AZ deployment, which does not support cross-AZ disaster recovery), `MultiZones` (change to multi-AZ deployment, which supports cross-AZ disaster recovery).
        :rtype: str
        """
        return self._MultiZones

    @MultiZones.setter
    def MultiZones(self, MultiZones):
        self._MultiZones = MultiZones

    @property
    def WaitSwitch(self):
        r"""The time when configuration adjustment task is performed. Valid values: `0` (execute immediately), `1` (execute during maintenance time). Default value: `1`.
        :rtype: int
        """
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch

    @property
    def DrZones(self):
        r"""Secondary node AZ of the multi-node architecture instance. The default value is null. It should be specified when modifying the AZ of the specified secondary node needs to be performed during configuration adjustment. When MultiZones = MultiZones, the AZs of the primary nodes and secondary nodes cannot all be the same. The collection of AZs of the secondary node can include 2-5 AZs.
        :rtype: list of DrZoneInfo
        """
        return self._DrZones

    @DrZones.setter
    def DrZones(self, DrZones):
        self._DrZones = DrZones


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
        if params.get("DrZones") is not None:
            self._DrZones = []
            for item in params.get("DrZones"):
                obj = DrZoneInfo()
                obj._deserialize(item)
                self._DrZones.append(obj)
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
        :param _DealName: Order name.
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order name.
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


class ZoneInfo(AbstractModel):
    r"""AZ information

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
        r"""AZ ID in the format of ap-guangzhou-1 (i.e., Guangzhou Zone 1)
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
        r"""Numeric ID of AZ
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SpecId(self):
        r"""ID of specification purchasable in this AZ, which, together with the returned value of the `DescribeProductConfig` API, can be used to find out the specifications currently purchasable in the AZ
        :rtype: int
        """
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def Version(self):
        r"""Information of database versions purchasable under the current AZ and specification. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise)
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
        


class ZoneStatus(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Zone: 
        :type Zone: str
        :param _Region: 
        :type Region: str
        :param _Status: 
        :type Status: int
        """
        self._Zone = None
        self._Region = None
        self._Status = None

    @property
    def Zone(self):
        r"""
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Region(self):
        r"""
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        r"""
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        