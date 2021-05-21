# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
        """
        :param UserName: Instance username
        :type UserName: str
        :param Password: Instance password
        :type Password: str
        :param DBPrivileges: List of database permissions
        :type DBPrivileges: list of DBPrivilege
        :param Remark: Account remarks
        :type Remark: str
        :param IsAdmin: Whether it is an admin account. Default value: no
        :type IsAdmin: bool
        """
        self.UserName = None
        self.Password = None
        self.DBPrivileges = None
        self.Remark = None
        self.IsAdmin = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        if params.get("DBPrivileges") is not None:
            self.DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self.DBPrivileges.append(obj)
        self.Remark = params.get("Remark")
        self.IsAdmin = params.get("IsAdmin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AccountDetail(AbstractModel):
    """Account details

    """

    def __init__(self):
        """
        :param Name: Account name
        :type Name: str
        :param Remark: Account remarks
        :type Remark: str
        :param CreateTime: Account creation time
        :type CreateTime: str
        :param Status: Account status. 1: creating, 2: normal, 3: modifying, 4: resetting password, -1: deleting
        :type Status: int
        :param UpdateTime: Account update time
        :type UpdateTime: str
        :param PassTime: Password update time
        :type PassTime: str
        :param InternalStatus: Internal account status, which should be `enable` normally
        :type InternalStatus: str
        :param Dbs: Information of read and write permissions of this account on relevant databases
        :type Dbs: list of DBPrivilege
        :param IsAdmin: Whether it is an admin account
        :type IsAdmin: bool
        """
        self.Name = None
        self.Remark = None
        self.CreateTime = None
        self.Status = None
        self.UpdateTime = None
        self.PassTime = None
        self.InternalStatus = None
        self.Dbs = None
        self.IsAdmin = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.UpdateTime = params.get("UpdateTime")
        self.PassTime = params.get("PassTime")
        self.InternalStatus = params.get("InternalStatus")
        if params.get("Dbs") is not None:
            self.Dbs = []
            for item in params.get("Dbs"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self.Dbs.append(obj)
        self.IsAdmin = params.get("IsAdmin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AccountPassword(AbstractModel):
    """Instance account password information

    """

    def __init__(self):
        """
        :param UserName: Username
        :type UserName: str
        :param Password: Password
        :type Password: str
        """
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AccountPrivilege(AbstractModel):
    """Database account permission information, which is set when the database is created

    """

    def __init__(self):
        """
        :param UserName: Database username
        :type UserName: str
        :param Privilege: Database permissions. ReadWrite: read/write, ReadOnly: read-only
        :type Privilege: str
        """
        self.UserName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AccountPrivilegeModifyInfo(AbstractModel):
    """Database account permission change information

    """

    def __init__(self):
        """
        :param UserName: Database username
        :type UserName: str
        :param DBPrivileges: Account permission change information
        :type DBPrivileges: list of DBPrivilegeModifyInfo
        """
        self.UserName = None
        self.DBPrivileges = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        if params.get("DBPrivileges") is not None:
            self.DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilegeModifyInfo()
                obj._deserialize(item)
                self.DBPrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AccountRemark(AbstractModel):
    """Account remarks

    """

    def __init__(self):
        """
        :param UserName: Account name
        :type UserName: str
        :param Remark: New remarks of account
        :type Remark: str
        """
        self.UserName = None
        self.Remark = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Backup(AbstractModel):
    """Backup file details

    """

    def __init__(self):
        """
        :param FileName: Filename
        :type FileName: str
        :param Size: File size in KB
        :type Size: int
        :param StartTime: Backup start time
        :type StartTime: str
        :param EndTime: Backup end time
        :type EndTime: str
        :param InternalAddr: Download address for private network
        :type InternalAddr: str
        :param ExternalAddr: Download address for public network
        :type ExternalAddr: str
        :param Id: Unique ID of backup file, which will be used by the `RestoreInstance` API
        :type Id: int
        :param Status: Backup file status (0: creating, 1: succeeded, 2: failed)
        :type Status: int
        :param DBs: List of databases for multi-database backup
        :type DBs: list of str
        :param Strategy: Backup policy (0: instance backup, 1: multi-database backup)
        :type Strategy: int
        :param BackupWay: Backup mode. 0: scheduled, 1: manual
        :type BackupWay: int
        :param BackupName: Backup name, which can be customized.
        :type BackupName: str
        """
        self.FileName = None
        self.Size = None
        self.StartTime = None
        self.EndTime = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.Id = None
        self.Status = None
        self.DBs = None
        self.Strategy = None
        self.BackupWay = None
        self.BackupName = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Size = params.get("Size")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.DBs = params.get("DBs")
        self.Strategy = params.get("Strategy")
        self.BackupWay = params.get("BackupWay")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CloneDBRequest(AbstractModel):
    """CloneDB request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        :param RenameRestore: Clone and rename the databases specified in `ReNameRestoreDatabase`. Please note that the clones must be renamed.
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self.InstanceId = None
        self.RenameRestore = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("RenameRestore") is not None:
            self.RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self.RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CloneDBResponse(AbstractModel):
    """CloneDB response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task request ID, which can be used in the `DescribeFlowStatus` API to query the execution result of an async task
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CosUploadBackupFile(AbstractModel):
    """Querying the size of uploaded backup files.

    """

    def __init__(self):
        """
        :param FileName: Backup name
        :type FileName: str
        :param Size: Backup size
        :type Size: int
        """
        self.FileName = None
        self.Size = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param Accounts: Database instance account information
        :type Accounts: list of AccountCreateInfo
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountCreateInfo()
                obj._deserialize(item)
                self.Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        """
        :param FlowId: Task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateBackupMigrationRequest(AbstractModel):
    """CreateBackupMigration request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param RecoveryType: Migration task restoration type. FULL: full backup restoration, FULL_LOG: full backup and transaction log restoration, FULL_DIFF: full backup and differential backup restoration
        :type RecoveryType: str
        :param UploadType: Backup upload type. COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :type UploadType: str
        :param MigrationName: Task name
        :type MigrationName: str
        :param BackupFiles: If the UploadType is COS_URL, fill in the URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :type BackupFiles: list of str
        """
        self.InstanceId = None
        self.RecoveryType = None
        self.UploadType = None
        self.MigrationName = None
        self.BackupFiles = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RecoveryType = params.get("RecoveryType")
        self.UploadType = params.get("UploadType")
        self.MigrationName = params.get("MigrationName")
        self.BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateBackupMigrationResponse(AbstractModel):
    """CreateBackupMigration response structure.

    """

    def __init__(self):
        """
        :param BackupMigrationId: Backup import task ID
        :type BackupMigrationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BackupMigrationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        """
        :param Strategy: Backup policy (0: instance backup, 1: multi-database backup)
        :type Strategy: int
        :param DBNames: List of names of databases to be backed up (required only for multi-database backup)
        :type DBNames: list of str
        :param InstanceId: Instance ID in the format of mssql-i1z41iwd
        :type InstanceId: str
        :param BackupName: Backup name. If this parameter is left empty, a backup name in the format of "[Instance ID]_[Backup start timestamp]" will be automatically generated.
        :type BackupName: str
        """
        self.Strategy = None
        self.DBNames = None
        self.InstanceId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.Strategy = params.get("Strategy")
        self.DBNames = params.get("DBNames")
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup response structure.

    """

    def __init__(self):
        """
        :param FlowId: The async job ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDBInstancesRequest(AbstractModel):
    """CreateDBInstances request structure.

    """

    def __init__(self):
        """
        :param Zone: Instance AZ, such as ap-guangzhou-1 (Guangzhou Zone 1). Purchasable AZs for an instance can be obtained through the `DescribeZones` API
        :type Zone: str
        :param Memory: Instance memory size in GB
        :type Memory: int
        :param Storage: Instance storage capacity in GB
        :type Storage: int
        :param InstanceChargeType: Billing mode. Valid value: POSTPAID (pay-as-you-go).
        :type InstanceChargeType: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param GoodsNum: Number of instances purchased this time. Default value: 1. Maximum value: 10
        :type GoodsNum: int
        :param SubnetId: VPC subnet ID in the format of subnet-bdoe83fa. `SubnetId` and `VpcId` should be set or ignored simultaneously
        :type SubnetId: str
        :param VpcId: VPC ID in the format of vpc-dsp338hz. `SubnetId` and `VpcId` should be set or ignored simultaneously
        :type VpcId: str
        :param Period: Length of purchase of instance. The default value is 1, indicating one month. The value cannot exceed 48
        :type Period: int
        :param AutoVoucher: Whether to automatically use voucher. 0: no, 1: yes. Default value: no
        :type AutoVoucher: int
        :param VoucherIds: Array of voucher IDs (currently, only one voucher can be used per order)
        :type VoucherIds: list of str
        :param DBVersion: SQL Server version. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise). The version purchasable varies by region and can be queried by calling the `DescribeProductConfig` API. If this parameter is left empty, 2008R2 will be used by default.
        :type DBVersion: str
        :param AutoRenewFlag: Auto-renewal flag. 0: normal renewal, 1: auto-renewal. Default value: 1.
        :type AutoRenewFlag: int
        :param SecurityGroupList: Security group list, which contains security group IDs in the format of sg-xxx.
        :type SecurityGroupList: list of str
        :param Weekly: Configuration of the maintenance window, which specifies the day of the week when maintenance can be performed. Valid values: 1 (Monday), 2 (Tuesday), 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday).
        :type Weekly: list of int
        :param StartTime: Configuration of the maintenance window, which specifies the start time of daily maintenance.
        :type StartTime: str
        :param Span: Configuration of the maintenance window, which specifies the maintenance duration in hours.
        :type Span: int
        :param HAType: The type of purchased high-availability instance. Valid values: DUAL (dual-server high availability), CLUSTER (cluster). Default value: DUAL.
        :type HAType: str
        :param MultiZones: Whether to deploy across availability zones. Default value: false.
        :type MultiZones: bool
        :param ResourceTags: Tags associated with the instances to be created
        :type ResourceTags: list of ResourceTag
        """
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.InstanceChargeType = None
        self.ProjectId = None
        self.GoodsNum = None
        self.SubnetId = None
        self.VpcId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.DBVersion = None
        self.AutoRenewFlag = None
        self.SecurityGroupList = None
        self.Weekly = None
        self.StartTime = None
        self.Span = None
        self.HAType = None
        self.MultiZones = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.ProjectId = params.get("ProjectId")
        self.GoodsNum = params.get("GoodsNum")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.DBVersion = params.get("DBVersion")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.SecurityGroupList = params.get("SecurityGroupList")
        self.Weekly = params.get("Weekly")
        self.StartTime = params.get("StartTime")
        self.Span = params.get("Span")
        self.HAType = params.get("HAType")
        self.MultiZones = params.get("MultiZones")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances response structure.

    """

    def __init__(self):
        """
        :param DealName: Order name
        :type DealName: str
        :param DealNames: Order name array
        :type DealNames: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealName = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDBRequest(AbstractModel):
    """CreateDB request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DBs: Database creation information
        :type DBs: list of DBCreateInfo
        """
        self.InstanceId = None
        self.DBs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DBs") is not None:
            self.DBs = []
            for item in params.get("DBs"):
                obj = DBCreateInfo()
                obj._deserialize(item)
                self.DBs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDBResponse(AbstractModel):
    """CreateDB response structure.

    """

    def __init__(self):
        """
        :param FlowId: Task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateIncrementalMigrationRequest(AbstractModel):
    """CreateIncrementalMigration request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration.
        :type BackupMigrationId: str
        :param BackupFiles: Incremental backup file. If the UploadType of a full backup file is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :type BackupFiles: list of str
        :param IsRecovery: Whether restoration is required. No: not required. Yes: required. Not required by default.
        :type IsRecovery: str
        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.BackupFiles = None
        self.IsRecovery = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.BackupFiles = params.get("BackupFiles")
        self.IsRecovery = params.get("IsRecovery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateIncrementalMigrationResponse(AbstractModel):
    """CreateIncrementalMigration response structure.

    """

    def __init__(self):
        """
        :param IncrementalMigrationId: ID of an incremental backup import task
        :type IncrementalMigrationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IncrementalMigrationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMigrationRequest(AbstractModel):
    """CreateMigration request structure.

    """

    def __init__(self):
        """
        :param MigrateName: Migration task name
        :type MigrateName: str
        :param MigrateType: Migration type (1: structure migration, 2: data migration, 3: incremental sync)
        :type MigrateType: int
        :param SourceType: Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :type SourceType: int
        :param Source: Migration source
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param Target: Migration target
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param MigrateDBSet: Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5)
        :type MigrateDBSet: list of MigrateDB
        :param RenameRestore: Restore and rename the databases listed in `ReNameRestoreDatabase`. If this parameter is left empty, all restored databases will be renamed in the default format. This parameter takes effect only when `SourceType=5`.
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self.MigrateName = None
        self.MigrateType = None
        self.SourceType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None
        self.RenameRestore = None


    def _deserialize(self, params):
        self.MigrateName = params.get("MigrateName")
        self.MigrateType = params.get("MigrateType")
        self.SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self.Source = MigrateSource()
            self.Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self.Target = MigrateTarget()
            self.Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self.MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self.MigrateDBSet.append(obj)
        if params.get("RenameRestore") is not None:
            self.RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self.RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMigrationResponse(AbstractModel):
    """CreateMigration response structure.

    """

    def __init__(self):
        """
        :param MigrateId: Migration task ID
        :type MigrateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MigrateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DBCreateInfo(AbstractModel):
    """Database creation information

    """

    def __init__(self):
        """
        :param DBName: Database name
        :type DBName: str
        :param Charset: Character set, which can be queried by the `DescribeDBCharsets` API. Default value: `Chinese_PRC_CI_AS`.
        :type Charset: str
        :param Accounts: Database account permission information
        :type Accounts: list of AccountPrivilege
        :param Remark: Remarks
        :type Remark: str
        """
        self.DBName = None
        self.Charset = None
        self.Accounts = None
        self.Remark = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Charset = params.get("Charset")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DBDetail(AbstractModel):
    """Database information

    """

    def __init__(self):
        """
        :param Name: Database name
        :type Name: str
        :param Charset: Character set
        :type Charset: str
        :param Remark: Remarks
        :type Remark: str
        :param CreateTime: Database creation time
        :type CreateTime: str
        :param Status: Database status. 1: creating, 2: running, 3: modifying, -1: dropping
        :type Status: int
        :param Accounts: Database account permission information
        :type Accounts: list of AccountPrivilege
        :param InternalStatus: Internal status. ONLINE: running
        :type InternalStatus: str
        """
        self.Name = None
        self.Charset = None
        self.Remark = None
        self.CreateTime = None
        self.Status = None
        self.Accounts = None
        self.InternalStatus = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Charset = params.get("Charset")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.InternalStatus = params.get("InternalStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DBInstance(AbstractModel):
    """Instance details

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Name: Instance name
        :type Name: str
        :param ProjectId: Project ID of instance
        :type ProjectId: int
        :param RegionId: Instance region ID
        :type RegionId: int
        :param ZoneId: Instance AZ ID
        :type ZoneId: int
        :param VpcId: Instance VPC ID, which will be 0 if the basic network is used
        :type VpcId: int
        :param SubnetId: Instance VPC subnet ID, which will be 0 if the basic network is used
        :type SubnetId: int
        :param Status: Instance status. Valid values: <li>1: applying </li> <li>2: running </li> <li>3: restrictedly running (primary/secondary switching) </li> <li>4: isolated </li> <li>5: repossessing </li> <li>6: repossessed </li> <li>7: task running (e.g., backing up or rolling back the instance) </li> <li>8: decommissioned </li> <li>9: scaling </li> <li>10: migrating </li> <li>11: read-only </li> <li>12: restarting </li>
        :type Status: int
        :param Vip: Instance access IP
        :type Vip: str
        :param Vport: Instance access port
        :type Vport: int
        :param CreateTime: Instance creation time
        :type CreateTime: str
        :param UpdateTime: Instance update time
        :type UpdateTime: str
        :param StartTime: Instance billing start time
        :type StartTime: str
        :param EndTime: Instance billing end time
        :type EndTime: str
        :param IsolateTime: Instance isolation time
        :type IsolateTime: str
        :param Memory: Instance memory size in GB
        :type Memory: int
        :param UsedStorage: Used storage capacity of instance in GB
        :type UsedStorage: int
        :param Storage: Instance storage capacity in GB
        :type Storage: int
        :param VersionName: Instance version
        :type VersionName: str
        :param RenewFlag: Instance renewal flag
        :type RenewFlag: int
        :param Model: High-availability instance type. Valid values: 1 (dual-server high-availability), 2 (standalone), 3 (multi-AZ), 4 (multi-AZ cluster), 5 (cluster), 9 (private consumption)
        :type Model: int
        :param Region: Instance region name, such as ap-guangzhou
        :type Region: str
        :param Zone: Instance AZ name, such as ap-guangzhou-1
        :type Zone: str
        :param BackupTime: Backup time point
        :type BackupTime: str
        :param PayMode: Instance billing mode. 0: pay-as-you-go
        :type PayMode: int
        :param Uid: Instance UID
        :type Uid: str
        :param Cpu: Number of CPU cores of instance
        :type Cpu: int
        :param Version: Instance version code
        :type Version: str
        :param Type: Physical server code
        :type Type: str
        :param Pid: Billing ID
        :type Pid: int
        :param UniqVpcId: Unique string-type ID of instance VPC in the format of `vpc-xxx`, which is an empty string if the basic network is used
        :type UniqVpcId: str
        :param UniqSubnetId: Unique string-type ID of instance subnet in the format of `subnet-xxx`, which is an empty string if the basic network is used
        :type UniqSubnetId: str
        :param IsolateOperator: Instance isolation.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsolateOperator: str
        :param SubFlag: Pub/sub flag. Valid values: SUB (subscribe instance), PUB (publish instance). If it is left empty, it refers to a regular instance without a pub/sub design.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubFlag: str
        :param ROFlag: Read-only flag. Valid values: RO (read-only instance), MASTER (primary instance with read-only instances). If it is left empty, it refers to an instance which is not read-only and has no RO group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ROFlag: str
        :param HAFlag: Disaster recovery type. Valid values: MIRROR (image), ALWAYSON (AlwaysOn), SINGLE (singleton).
Note: this field may return null, indicating that no valid values can be obtained.
        :type HAFlag: str
        :param ResourceTags: The list of tags associated with the instance
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceTags: list of ResourceTag
        """
        self.InstanceId = None
        self.Name = None
        self.ProjectId = None
        self.RegionId = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.UpdateTime = None
        self.StartTime = None
        self.EndTime = None
        self.IsolateTime = None
        self.Memory = None
        self.UsedStorage = None
        self.Storage = None
        self.VersionName = None
        self.RenewFlag = None
        self.Model = None
        self.Region = None
        self.Zone = None
        self.BackupTime = None
        self.PayMode = None
        self.Uid = None
        self.Cpu = None
        self.Version = None
        self.Type = None
        self.Pid = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.IsolateOperator = None
        self.SubFlag = None
        self.ROFlag = None
        self.HAFlag = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsolateTime = params.get("IsolateTime")
        self.Memory = params.get("Memory")
        self.UsedStorage = params.get("UsedStorage")
        self.Storage = params.get("Storage")
        self.VersionName = params.get("VersionName")
        self.RenewFlag = params.get("RenewFlag")
        self.Model = params.get("Model")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.BackupTime = params.get("BackupTime")
        self.PayMode = params.get("PayMode")
        self.Uid = params.get("Uid")
        self.Cpu = params.get("Cpu")
        self.Version = params.get("Version")
        self.Type = params.get("Type")
        self.Pid = params.get("Pid")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.IsolateOperator = params.get("IsolateOperator")
        self.SubFlag = params.get("SubFlag")
        self.ROFlag = params.get("ROFlag")
        self.HAFlag = params.get("HAFlag")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DBPrivilege(AbstractModel):
    """Database permission information of account

    """

    def __init__(self):
        """
        :param DBName: Database name
        :type DBName: str
        :param Privilege: Database permissions. ReadWrite: read/write, ReadOnly: read-only
        :type Privilege: str
        """
        self.DBName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DBPrivilegeModifyInfo(AbstractModel):
    """Database permission change information

    """

    def __init__(self):
        """
        :param DBName: Database name
        :type DBName: str
        :param Privilege: Permission change information. ReadWrite: read/write, ReadOnly: read-only, Delete: the account has the permission to delete this database
        :type Privilege: str
        """
        self.DBName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Privilege = params.get("Privilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DBRemark(AbstractModel):
    """Database remarks

    """

    def __init__(self):
        """
        :param Name: Database name
        :type Name: str
        :param Remark: Remarks
        :type Remark: str
        """
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DbRollbackTimeInfo(AbstractModel):
    """Information of time range available for database rollback

    """

    def __init__(self):
        """
        :param DBName: Database name
        :type DBName: str
        :param StartTime: Start time of time range available for rollback
        :type StartTime: str
        :param EndTime: End time of time range available for rollback
        :type EndTime: str
        """
        self.DBName = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DealInfo(AbstractModel):
    """Order information

    """

    def __init__(self):
        """
        :param DealName: Order name
        :type DealName: str
        :param Count: Number of items
        :type Count: int
        :param FlowId: ID of associated flow, which can be used to query the flow execution status
        :type FlowId: int
        :param InstanceIdSet: This field is required only for an order that creates an instance, indicating the ID of the instance created by the order
        :type InstanceIdSet: list of str
        :param OwnerUin: Account
        :type OwnerUin: str
        :param InstanceChargeType: Instance billing type
        :type InstanceChargeType: str
        """
        self.DealName = None
        self.Count = None
        self.FlowId = None
        self.InstanceIdSet = None
        self.OwnerUin = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.Count = params.get("Count")
        self.FlowId = params.get("FlowId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.OwnerUin = params.get("OwnerUin")
        self.InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param UserNames: Array of instance usernames
        :type UserNames: list of str
        """
        self.InstanceId = None
        self.UserNames = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserNames = params.get("UserNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount response structure.

    """

    def __init__(self):
        """
        :param FlowId: Task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteBackupMigrationRequest(AbstractModel):
    """DeleteBackupMigration request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Target instance ID, which is returned through the API DescribeBackupMigration.
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID, which is returned through the API DescribeBackupMigration.
        :type BackupMigrationId: str
        """
        self.InstanceId = None
        self.BackupMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteBackupMigrationResponse(AbstractModel):
    """DeleteBackupMigration response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteDBRequest(AbstractModel):
    """DeleteDB request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of mssql-rljoi3bf
        :type InstanceId: str
        :param Names: Array of database names
        :type Names: list of str
        """
        self.InstanceId = None
        self.Names = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteDBResponse(AbstractModel):
    """DeleteDB response structure.

    """

    def __init__(self):
        """
        :param FlowId: Task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteIncrementalMigrationRequest(AbstractModel):
    """DeleteIncrementalMigration request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Target instance ID.
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID
        :type BackupMigrationId: str
        :param IncrementalMigrationId: ID of an incremental backup import task
        :type IncrementalMigrationId: str
        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.IncrementalMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteIncrementalMigrationResponse(AbstractModel):
    """DeleteIncrementalMigration response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMigrationRequest(AbstractModel):
    """DeleteMigration request structure.

    """

    def __init__(self):
        """
        :param MigrateId: Migration task ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMigrationResponse(AbstractModel):
    """DeleteMigration response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Limit: Number of results per page. Value range: 1-100. Default value: 20
        :type Limit: int
        :param Offset: Page number. Default value: 0
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Accounts: Account information list
        :type Accounts: list of AccountDetail
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Accounts = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountDetail()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupCommandRequest(AbstractModel):
    """DescribeBackupCommand request structure.

    """

    def __init__(self):
        """
        :param BackupFileType: Backup file type. Full: full backup. FULL_LOG: full backup which needs log increments. FULL_DIFF: full backup which needs differential increments. LOG: log backup. DIFF: differential backup.
        :type BackupFileType: str
        :param DataBaseName: Database name
        :type DataBaseName: str
        :param IsRecovery: Whether restoration is required. No: not required. Yes: required.
        :type IsRecovery: str
        :param LocalPath: Storage path of backup files. If this parameter is left empty, the default storage path will be D:\\.
        :type LocalPath: str
        """
        self.BackupFileType = None
        self.DataBaseName = None
        self.IsRecovery = None
        self.LocalPath = None


    def _deserialize(self, params):
        self.BackupFileType = params.get("BackupFileType")
        self.DataBaseName = params.get("DataBaseName")
        self.IsRecovery = params.get("IsRecovery")
        self.LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupCommandResponse(AbstractModel):
    """DescribeBackupCommand response structure.

    """

    def __init__(self):
        """
        :param Command: Create a backup command
        :type Command: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Command = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Command = params.get("Command")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupMigrationRequest(AbstractModel):
    """DescribeBackupMigration request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration.
        :type BackupMigrationId: str
        :param MigrationName: Import task name
        :type MigrationName: str
        :param BackupFileName: Backup file name
        :type BackupFileName: str
        :param StatusSet: Status set of import tasks
        :type StatusSet: list of int
        :param RecoveryType: Import task restoration type: FULL,FULL_LOG,FULL_DIFF
        :type RecoveryType: str
        :param UploadType: COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :type UploadType: str
        :param Limit: Paging. Page size
        :type Limit: int
        :param Offset: Paging. Number of pages
        :type Offset: int
        :param OrderBy: Field for order: name,createTime,startTime,endTime
        :type OrderBy: str
        :param OrderByType: Type of order: desc,asc
        :type OrderByType: str
        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.MigrationName = None
        self.BackupFileName = None
        self.StatusSet = None
        self.RecoveryType = None
        self.UploadType = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.MigrationName = params.get("MigrationName")
        self.BackupFileName = params.get("BackupFileName")
        self.StatusSet = params.get("StatusSet")
        self.RecoveryType = params.get("RecoveryType")
        self.UploadType = params.get("UploadType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupMigrationResponse(AbstractModel):
    """DescribeBackupMigration response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of tasks
        :type TotalCount: int
        :param BackupMigrationSet: Migration task set
        :type BackupMigrationSet: list of Migration
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupMigrationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupMigrationSet") is not None:
            self.BackupMigrationSet = []
            for item in params.get("BackupMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self.BackupMigrationSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupUploadSizeRequest(AbstractModel):
    """DescribeBackupUploadSize request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param IncrementalMigrationId: Incremental import task ID
        :type IncrementalMigrationId: str
        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.IncrementalMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupUploadSizeResponse(AbstractModel):
    """DescribeBackupUploadSize response structure.

    """

    def __init__(self):
        """
        :param CosUploadBackupFileSet: Information of uploaded backups
        :type CosUploadBackupFileSet: list of CosUploadBackupFile
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CosUploadBackupFileSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CosUploadBackupFileSet") is not None:
            self.CosUploadBackupFileSet = []
            for item in params.get("CosUploadBackupFileSet"):
                obj = CosUploadBackupFile()
                obj._deserialize(item)
                self.CosUploadBackupFileSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start name (yyyy-MM-dd HH:mm:ss)
        :type StartTime: str
        :param EndTime: End time (yyyy-MM-dd HH:mm:ss)
        :type EndTime: str
        :param InstanceId: Instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param Limit: Number of results per page. Value range: 1-100. Default value: 20
        :type Limit: int
        :param Offset: Page number. Default value: 0
        :type Offset: int
        :param BackupName: Filter by backup name. If this parameter is left empty, backup name will not be used in filtering.
        :type BackupName: str
        :param Strategy: Filter by backup policy. Valid values: 0 (instance backup), 1 (multi-database backup). If this parameter is left empty, backup policy will not be used in filtering.
        :type Strategy: int
        :param BackupWay: Filter by backup mode. Valid values: 0 (automatic backup on a regular basis), 1 (manual backup performed by the user at any time). If this parameter is left empty, backup mode will not be used in filtering.
        :type BackupWay: int
        :param BackupId: Filter by backup ID. If this parameter is left empty, backup ID will not be used in filtering.
        :type BackupId: int
        :param DatabaseName: Filter backups by the database name. If the parameter is left empty, this filter criteria will not take effect.
        :type DatabaseName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.BackupName = None
        self.Strategy = None
        self.BackupWay = None
        self.BackupId = None
        self.DatabaseName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BackupName = params.get("BackupName")
        self.Strategy = params.get("Strategy")
        self.BackupWay = params.get("BackupWay")
        self.BackupId = params.get("BackupId")
        self.DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of backups
        :type TotalCount: int
        :param Backups: Backup list details
        :type Backups: list of Backup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Backups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Backups") is not None:
            self.Backups = []
            for item in params.get("Backups"):
                obj = Backup()
                obj._deserialize(item)
                self.Backups.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBCharsetsRequest(AbstractModel):
    """DescribeDBCharsets request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBCharsetsResponse(AbstractModel):
    """DescribeDBCharsets response structure.

    """

    def __init__(self):
        """
        :param DatabaseCharsets: Database character set list
        :type DatabaseCharsets: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DatabaseCharsets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DatabaseCharsets = params.get("DatabaseCharsets")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances request structure.

    """

    def __init__(self):
        """
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Status: Instance status. Valid values:
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
        :param Offset: Page number. Default value: 0
        :type Offset: int
        :param Limit: Number of results per page. Value range: 1-100. Default value: 100
        :type Limit: int
        :param InstanceIdSet: One or more instance IDs in the format of mssql-si2823jyl
        :type InstanceIdSet: list of str
        :param PayMode: Retrieves billing type. 0: pay-as-you-go
        :type PayMode: int
        :param VpcId: Unique string-type ID of instance VPC in the format of `vpc-xxx`. If an empty string ("") is passed in, filtering will be made by basic network.
        :type VpcId: str
        :param SubnetId: Unique string-type ID of instance subnet in the format of `subnet-xxx`. If an empty string ("") is passed in, filtering will be made by basic network.
        :type SubnetId: str
        :param VipSet: The list of instance private IPs, such as 172.1.0.12
        :type VipSet: list of str
        :param InstanceNameSet: The list of instance names used for fuzzy match
        :type InstanceNameSet: list of str
        :param VersionSet: The list of instance version numbers, such as 2008R2, 2012SP3
        :type VersionSet: list of str
        :param Zone: Instance availability zone, such as ap-guangzhou-2
        :type Zone: str
        :param TagKeys: The list of instance tags
        :type TagKeys: list of str
        :param SearchKey: Keyword used for fuzzy match, including instance ID, instance name, and instance private IP
        :type SearchKey: str
        """
        self.ProjectId = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.InstanceIdSet = None
        self.PayMode = None
        self.VpcId = None
        self.SubnetId = None
        self.VipSet = None
        self.InstanceNameSet = None
        self.VersionSet = None
        self.Zone = None
        self.TagKeys = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.PayMode = params.get("PayMode")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.VipSet = params.get("VipSet")
        self.InstanceNameSet = params.get("InstanceNameSet")
        self.VersionSet = params.get("VersionSet")
        self.Zone = params.get("Zone")
        self.TagKeys = params.get("TagKeys")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of eligible instances. If the results are returned in multiple pages, this value will be the number of all eligible instances but not the number of instances returned according to the current values of `Limit` and `Offset`
        :type TotalCount: int
        :param DBInstances: Instance list
        :type DBInstances: list of DBInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstances") is not None:
            self.DBInstances = []
            for item in params.get("DBInstances"):
                obj = DBInstance()
                obj._deserialize(item)
                self.DBInstances.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBsRequest(AbstractModel):
    """DescribeDBs request structure.

    """

    def __init__(self):
        """
        :param InstanceIdSet: Instance ID
        :type InstanceIdSet: list of str
        :param Limit: Number of results per page. Value range: 1-100. Default value: 20
        :type Limit: int
        :param Offset: Page number. Default value: 0
        :type Offset: int
        """
        self.InstanceIdSet = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBsResponse(AbstractModel):
    """DescribeDBs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of databases
        :type TotalCount: int
        :param DBInstances: List of instance databases
        :type DBInstances: list of InstanceDBDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstances") is not None:
            self.DBInstances = []
            for item in params.get("DBInstances"):
                obj = InstanceDBDetail()
                obj._deserialize(item)
                self.DBInstances.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFlowStatusRequest(AbstractModel):
    """DescribeFlowStatus request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFlowStatusResponse(AbstractModel):
    """DescribeFlowStatus response structure.

    """

    def __init__(self):
        """
        :param Status: Flow status. 0: succeeded, 1: failed, 2: running
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIncrementalMigrationRequest(AbstractModel):
    """DescribeIncrementalMigration request structure.

    """

    def __init__(self):
        """
        :param BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param BackupFileName: Backup file name
        :type BackupFileName: str
        :param StatusSet: Status set of import tasks
        :type StatusSet: list of int
        :param Limit: Paging. Page size
        :type Limit: int
        :param Offset: Paging. Number of pages
        :type Offset: int
        :param OrderBy: Field for order: name,createTime,startTime,endTime
        :type OrderBy: str
        :param OrderByType: Type of order: desc,asc
        :type OrderByType: str
        :param IncrementalMigrationId: ID of an incremental backup import task
        :type IncrementalMigrationId: str
        """
        self.BackupMigrationId = None
        self.InstanceId = None
        self.BackupFileName = None
        self.StatusSet = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.IncrementalMigrationId = None


    def _deserialize(self, params):
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.InstanceId = params.get("InstanceId")
        self.BackupFileName = params.get("BackupFileName")
        self.StatusSet = params.get("StatusSet")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIncrementalMigrationResponse(AbstractModel):
    """DescribeIncrementalMigration response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of import tasks
        :type TotalCount: int
        :param IncrementalMigrationSet: Incremental import task set
        :type IncrementalMigrationSet: list of Migration
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.IncrementalMigrationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("IncrementalMigrationSet") is not None:
            self.IncrementalMigrationSet = []
            for item in params.get("IncrementalMigrationSet"):
                obj = Migration()
                obj._deserialize(item)
                self.IncrementalMigrationSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMigrationDetailRequest(AbstractModel):
    """DescribeMigrationDetail request structure.

    """

    def __init__(self):
        """
        :param MigrateId: Migration task ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMigrationDetailResponse(AbstractModel):
    """DescribeMigrationDetail response structure.

    """

    def __init__(self):
        """
        :param MigrateId: Migration task ID
        :type MigrateId: int
        :param MigrateName: Migration task name
        :type MigrateName: str
        :param AppId: User ID of migration task
        :type AppId: int
        :param Region: Migration task region
        :type Region: str
        :param SourceType: Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :type SourceType: int
        :param CreateTime: Migration task creation time
        :type CreateTime: str
        :param StartTime: Migration task start time
        :type StartTime: str
        :param EndTime: Migration task end time
        :type EndTime: str
        :param Status: Migration task status (1: initializing, 4: migrating, 5: migration failed, 6: migration succeeded)
        :type Status: int
        :param Progress: Migration task progress
        :type Progress: int
        :param MigrateType: Migration type (1: structure migration, 2: data migration, 3: incremental sync)
        :type MigrateType: int
        :param Source: Migration source
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param Target: Migration target
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param MigrateDBSet: Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5)
        :type MigrateDBSet: list of MigrateDB
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MigrateId = None
        self.MigrateName = None
        self.AppId = None
        self.Region = None
        self.SourceType = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Progress = None
        self.MigrateType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.MigrateName = params.get("MigrateName")
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.SourceType = params.get("SourceType")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.MigrateType = params.get("MigrateType")
        if params.get("Source") is not None:
            self.Source = MigrateSource()
            self.Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self.Target = MigrateTarget()
            self.Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self.MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self.MigrateDBSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMigrationsRequest(AbstractModel):
    """DescribeMigrations request structure.

    """

    def __init__(self):
        """
        :param StatusSet: Status set. As long as a migration task is in a status therein, it will be listed
        :type StatusSet: list of int
        :param MigrateName: Migration task name (fuzzy match)
        :type MigrateName: str
        :param Limit: Number of results per page. Value range: 1-100. Default value: 100
        :type Limit: int
        :param Offset: Page number. Default value: 0
        :type Offset: int
        :param OrderBy: The query results are sorted by keyword. Valid values: name, createTime, startTime, endTime, status
        :type OrderBy: str
        :param OrderByType: Sorting order. Valid values: desc, asc
        :type OrderByType: str
        """
        self.StatusSet = None
        self.MigrateName = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.StatusSet = params.get("StatusSet")
        self.MigrateName = params.get("MigrateName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMigrationsResponse(AbstractModel):
    """DescribeMigrations response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of query results
        :type TotalCount: int
        :param MigrateTaskSet: List of query results
        :type MigrateTaskSet: list of MigrateTask
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.MigrateTaskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MigrateTaskSet") is not None:
            self.MigrateTaskSet = []
            for item in params.get("MigrateTaskSet"):
                obj = MigrateTask()
                obj._deserialize(item)
                self.MigrateTaskSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders request structure.

    """

    def __init__(self):
        """
        :param DealNames: Order array. The order name will be returned upon shipping, which can be used to call the `DescribeOrders` API to query shipment status
        :type DealNames: list of str
        """
        self.DealNames = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders response structure.

    """

    def __init__(self):
        """
        :param Deals: Order information array
        :type Deals: list of DealInfo
        :param TotalCount: Number of orders returned
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Deals = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = DealInfo()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig request structure.

    """

    def __init__(self):
        """
        :param Zone: AZ ID in the format of ap-guangzhou-1
        :type Zone: str
        :param InstanceType: The type of instances to be purchased. Valid values: HA (High-Availability Edition, including dual-server high availability and AlwaysOn cluster), RO (read-only replica), SI (Basic Edition)
        :type InstanceType: str
        """
        self.Zone = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductConfigResponse(AbstractModel):
    """DescribeProductConfig response structure.

    """

    def __init__(self):
        """
        :param SpecInfoList: Specification information array
        :type SpecInfoList: list of SpecInfo
        :param TotalCount: Number of date entries returned
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of regions returned
        :type TotalCount: int
        :param RegionSet: Region information array
        :type RegionSet: list of RegionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRollbackTimeRequest(AbstractModel):
    """DescribeRollbackTime request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DBs: List of databases to be queried
        :type DBs: list of str
        """
        self.InstanceId = None
        self.DBs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DBs = params.get("DBs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRollbackTimeResponse(AbstractModel):
    """DescribeRollbackTime response structure.

    """

    def __init__(self):
        """
        :param Details: Information of time range available for database rollback
        :type Details: list of DbRollbackTimeInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = DbRollbackTimeInfo()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSlowlogsRequest(AbstractModel):
    """DescribeSlowlogs request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of mssql-k8voqdlz
        :type InstanceId: str
        :param StartTime: Query start time
        :type StartTime: str
        :param EndTime: Query end time
        :type EndTime: str
        :param Limit: Number of results per page. Value range: 1-100. Default value: 20
        :type Limit: int
        :param Offset: Page number. Default value: 0
        :type Offset: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSlowlogsResponse(AbstractModel):
    """DescribeSlowlogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of queries
        :type TotalCount: int
        :param Slowlogs: Information list of slow query logs
        :type Slowlogs: list of SlowlogInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Slowlogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Slowlogs") is not None:
            self.Slowlogs = []
            for item in params.get("Slowlogs"):
                obj = SlowlogInfo()
                obj._deserialize(item)
                self.Slowlogs.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeUploadBackupInfoRequest(AbstractModel):
    """DescribeUploadBackupInfo request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        """
        self.InstanceId = None
        self.BackupMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeUploadBackupInfoResponse(AbstractModel):
    """DescribeUploadBackupInfo response structure.

    """

    def __init__(self):
        """
        :param BucketName: Bucket name
        :type BucketName: str
        :param Region: Bucket location information
        :type Region: str
        :param Path: Storage path
        :type Path: str
        :param TmpSecretId: Temporary key ID
        :type TmpSecretId: str
        :param TmpSecretKey: Temporary key (Key)
        :type TmpSecretKey: str
        :param XCosSecurityToken: Temporary key (Token)
        :type XCosSecurityToken: str
        :param StartTime: Temporary key start time
        :type StartTime: str
        :param ExpiredTime: Temporary key expiration time
        :type ExpiredTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BucketName = None
        self.Region = None
        self.Path = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.XCosSecurityToken = None
        self.StartTime = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.Region = params.get("Region")
        self.Path = params.get("Path")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.XCosSecurityToken = params.get("XCosSecurityToken")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of AZs returned
        :type TotalCount: int
        :param ZoneSet: Array of AZs
        :type ZoneSet: list of ZoneInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances request structure.

    """

    def __init__(self):
        """
        :param Zone: AZ ID, which can be obtained through the `Zone` field in the returned value of the `DescribeZones` API
        :type Zone: str
        :param Memory: Memory size in GB
        :type Memory: int
        :param Storage: Instance capacity in GB
        :type Storage: int
        :param InstanceChargeType: Billing type. Valid value: POSTPAID.
        :type InstanceChargeType: str
        :param Period: Length of purchase in months. Value range: 1-48. Default value: 1
        :type Period: int
        :param GoodsNum: Number of instances purchased at a time. Value range: 1-100. Default value: 1
        :type GoodsNum: int
        :param DBVersion: SQL Server version. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise). Default value: 2008R2.
        :type DBVersion: str
        :param Cpu: The number of CPU cores of the instance you want to purchase.
        :type Cpu: int
        :param InstanceType: The type of purchased instance. Valid values: HA (high-availability edition, including dual-server high availability and AlwaysOn cluster), RO (read-only replica), SI (basic edition). Default value: HA.
        :type InstanceType: str
        :param MachineType: The host type of purchased instance. Valid values: PM (physical machine), CLOUD_PREMIUM (physical machine with premium cloud disk), CLOUD_SSD (physical machine with SSD). Default value: PM.
        :type MachineType: str
        """
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.InstanceChargeType = None
        self.Period = None
        self.GoodsNum = None
        self.DBVersion = None
        self.Cpu = None
        self.InstanceType = None
        self.MachineType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.Period = params.get("Period")
        self.GoodsNum = params.get("GoodsNum")
        self.DBVersion = params.get("DBVersion")
        self.Cpu = params.get("Cpu")
        self.InstanceType = params.get("InstanceType")
        self.MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances response structure.

    """

    def __init__(self):
        """
        :param OriginalPrice: Price before discount. This value divided by 100 indicates the price; for example, 10010 means 100.10 USD
        :type OriginalPrice: int
        :param Price: The actual price to be paid. This value divided by 100 indicates the price; for example, 10010 means 100.10 USD
        :type Price: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param Memory: Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size
        :type Memory: int
        :param Storage: Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity
        :type Storage: int
        :param Cpu: The number of CUP cores after the instance is upgraded, which cannot be smaller than that of the current cores.
        :type Cpu: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None
        self.Cpu = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance response structure.

    """

    def __init__(self):
        """
        :param OriginalPrice: Price before discount. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD
        :type OriginalPrice: int
        :param Price: The actual price to be paid. This value divided by 100 indicates the price; for example, 10094 means 100.94 USD
        :type Price: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceDBDetail(AbstractModel):
    """Instance database information

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DBDetails: Database information list
        :type DBDetails: list of DBDetail
        """
        self.InstanceId = None
        self.DBDetails = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DBDetails") is not None:
            self.DBDetails = []
            for item in params.get("DBDetails"):
                obj = DBDetail()
                obj._deserialize(item)
                self.DBDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MigrateDB(AbstractModel):
    """List of databases to be migrated

    """

    def __init__(self):
        """
        :param DBName: Name of migrated database
        :type DBName: str
        """
        self.DBName = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MigrateDetail(AbstractModel):
    """Migration progress details

    """

    def __init__(self):
        """
        :param StepName: Name of current step
        :type StepName: str
        :param Progress: Progress of current step in %
        :type Progress: int
        """
        self.StepName = None
        self.Progress = None


    def _deserialize(self, params):
        self.StepName = params.get("StepName")
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MigrateSource(AbstractModel):
    """Source type of migration task

    """

    def __init__(self):
        """
        :param InstanceId: Source instance ID in the format of `mssql-si2823jyl`, which is used when `MigrateType` is 1 (TencentDB for SQL Server)
        :type InstanceId: str
        :param CvmId: ID of source CVM instance, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type CvmId: str
        :param VpcId: VPC ID of source CVM instance in the format of vpc-6ys9ont9, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type VpcId: str
        :param SubnetId: VPC subnet ID of source CVM instance in the format of subnet-h9extioi, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type SubnetId: str
        :param UserName: Username, which is used when `MigrateType` is 1 or 2
        :type UserName: str
        :param Password: Password, which is used when `MigrateType` is 1 or 2
        :type Password: str
        :param Ip: Private IP of source CVM database, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type Ip: str
        :param Port: Port number of source CVM database, which is used when `MigrateType` is 2 (CVM-based self-created SQL Server database)
        :type Port: int
        :param Url: Source backup address for offline migration, which is used when `MigrateType` is 4 or 5
        :type Url: list of str
        :param UrlPassword: Source backup password for offline migration, which is used when `MigrateType` is 4 or 5
        :type UrlPassword: str
        """
        self.InstanceId = None
        self.CvmId = None
        self.VpcId = None
        self.SubnetId = None
        self.UserName = None
        self.Password = None
        self.Ip = None
        self.Port = None
        self.Url = None
        self.UrlPassword = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.CvmId = params.get("CvmId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Url = params.get("Url")
        self.UrlPassword = params.get("UrlPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MigrateTarget(AbstractModel):
    """Target type of migration task

    """

    def __init__(self):
        """
        :param InstanceId: ID of target instance in the format of mssql-si2823jyl
        :type InstanceId: str
        :param UserName: Username of migration target instance
        :type UserName: str
        :param Password: Password of migration target instance
        :type Password: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MigrateTask(AbstractModel):
    """Migration task type

    """

    def __init__(self):
        """
        :param MigrateId: Migration task ID
        :type MigrateId: int
        :param MigrateName: Migration task name
        :type MigrateName: str
        :param AppId: User ID of migration task
        :type AppId: int
        :param Region: Migration task region
        :type Region: str
        :param SourceType: Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode)
        :type SourceType: int
        :param CreateTime: Migration task creation time
        :type CreateTime: str
        :param StartTime: Migration task start time
        :type StartTime: str
        :param EndTime: Migration task end time
        :type EndTime: str
        :param Status: Migration task status (1: initializing, 4: migrating, 5: migration failed, 6: migration succeeded, 7: suspended, 8: deleted, 9: suspending, 10: completing, 11: suspension failed, 12: completion failed)
        :type Status: int
        :param Message: Information
        :type Message: str
        :param CheckFlag: Whether migration task has been checked (0: not checked, 1: check succeeded, 2: check failed, 3: checking)
        :type CheckFlag: int
        :param Progress: Migration task progress in %
        :type Progress: int
        :param MigrateDetail: Migration task progress details
        :type MigrateDetail: :class:`tencentcloud.sqlserver.v20180328.models.MigrateDetail`
        """
        self.MigrateId = None
        self.MigrateName = None
        self.AppId = None
        self.Region = None
        self.SourceType = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Message = None
        self.CheckFlag = None
        self.Progress = None
        self.MigrateDetail = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.MigrateName = params.get("MigrateName")
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.SourceType = params.get("SourceType")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.CheckFlag = params.get("CheckFlag")
        self.Progress = params.get("Progress")
        if params.get("MigrateDetail") is not None:
            self.MigrateDetail = MigrateDetail()
            self.MigrateDetail._deserialize(params.get("MigrateDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Migration(AbstractModel):
    """Cold backup migration import

    """

    def __init__(self):
        """
        :param MigrationId: Backup import task ID or incremental import task ID
        :type MigrationId: str
        :param MigrationName: Backup import task name. For an incremental import task, this field will be left empty.
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :type MigrationName: str
        :param AppId: Application ID
        :type AppId: int
        :param Region: Region
        :type Region: str
        :param InstanceId: ID of migrated target instance
        :type InstanceId: str
        :param RecoveryType: Migration task restoration type
        :type RecoveryType: str
        :param UploadType: Backup user upload type. COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :type UploadType: str
        :param BackupFiles: Backup file list, which is determined by UploadType. If the upload type is COS_URL, URL will be saved. If the upload type is COS_UPLOAD, the backup name will be saved.
        :type BackupFiles: list of str
        :param Status: Migration task status. Valid values: `2` (Creation completed), `7` (Importing full backups), `8` (Waiting for incremental backups), `9` (Import success), `10` (Import failure), `12` (Importing incremental backups).
        :type Status: int
        :param CreateTime: Migration task creation time
        :type CreateTime: str
        :param StartTime: Migration task start time
        :type StartTime: str
        :param EndTime: Migration task end time
        :type EndTime: str
        :param Message: More information
        :type Message: str
        :param Detail: Migration detail
        :type Detail: :class:`tencentcloud.sqlserver.v20180328.models.MigrationDetail`
        :param Action: Operation allowed in the current status
        :type Action: :class:`tencentcloud.sqlserver.v20180328.models.MigrationAction`
        :param IsRecovery: Whether this is the final restoration. For a full import task, this field will be left empty.
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :type IsRecovery: str
        """
        self.MigrationId = None
        self.MigrationName = None
        self.AppId = None
        self.Region = None
        self.InstanceId = None
        self.RecoveryType = None
        self.UploadType = None
        self.BackupFiles = None
        self.Status = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Message = None
        self.Detail = None
        self.Action = None
        self.IsRecovery = None


    def _deserialize(self, params):
        self.MigrationId = params.get("MigrationId")
        self.MigrationName = params.get("MigrationName")
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        self.RecoveryType = params.get("RecoveryType")
        self.UploadType = params.get("UploadType")
        self.BackupFiles = params.get("BackupFiles")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Message = params.get("Message")
        if params.get("Detail") is not None:
            self.Detail = MigrationDetail()
            self.Detail._deserialize(params.get("Detail"))
        if params.get("Action") is not None:
            self.Action = MigrationAction()
            self.Action._deserialize(params.get("Action"))
        self.IsRecovery = params.get("IsRecovery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MigrationAction(AbstractModel):
    """Operation allowed by a cold backup import task

    """

    def __init__(self):
        """
        :param AllAction: All the allowed operations. Values include: view (viewing a task), modify (modifying a task), start (starting a task), incremental (creating an incremental task), delete (deleting a task), and upload (obtaining the upload permission).
        :type AllAction: list of str
        :param AllowedAction: Operation allowed in the current status. If the subset of AllAction is left empty, no operations will be allowed.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MigrationDetail(AbstractModel):
    """Details of a cold backup import task

    """

    def __init__(self):
        """
        :param StepAll: Total number of steps
        :type StepAll: int
        :param StepNow: Current step
        :type StepNow: int
        :param Progress: Overall progress. For example, “30” means 30%.
        :type Progress: int
        :param StepInfo: Step information. ‘null’ means the migration has not started
Note: this field may return ‘null’, indicating that no valid values can be obtained.
        :type StepInfo: list of MigrationStep
        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = MigrationStep()
                obj._deserialize(item)
                self.StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MigrationStep(AbstractModel):
    """Migration steps of a cold backup import task

    """

    def __init__(self):
        """
        :param StepNo: Step sequence
        :type StepNo: int
        :param StepName: Step name
        :type StepName: str
        :param StepId: Step ID in English
        :type StepId: str
        :param Status: Step status: 0 (default value), 1 (succeeded), 2 (failed), 3 (in progress), 4 (not started)
        :type Status: int
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAccountPrivilegeRequest(AbstractModel):
    """ModifyAccountPrivilege request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param Accounts: Account permission change information
        :type Accounts: list of AccountPrivilegeModifyInfo
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilegeModifyInfo()
                obj._deserialize(item)
                self.Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAccountPrivilegeResponse(AbstractModel):
    """ModifyAccountPrivilege response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAccountRemarkRequest(AbstractModel):
    """ModifyAccountRemark request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        :param Accounts: Information of account for which to modify remarks
        :type Accounts: list of AccountRemark
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountRemark()
                obj._deserialize(item)
                self.Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAccountRemarkResponse(AbstractModel):
    """ModifyAccountRemark response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyBackupMigrationRequest(AbstractModel):
    """ModifyBackupMigration request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param MigrationName: Task name
        :type MigrationName: str
        :param RecoveryType: Migration task restoration type: FULL,FULL_LOG,FULL_DIFF
        :type RecoveryType: str
        :param UploadType: COS_URL: the backup is stored in user’s Cloud Object Storage, with URL provided. COS_UPLOAD: the backup is stored in the application’s Cloud Object Storage and needs to be uploaded by the user.
        :type UploadType: str
        :param BackupFiles: If the UploadType is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :type BackupFiles: list of str
        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.MigrationName = None
        self.RecoveryType = None
        self.UploadType = None
        self.BackupFiles = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.MigrationName = params.get("MigrationName")
        self.RecoveryType = params.get("RecoveryType")
        self.UploadType = params.get("UploadType")
        self.BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyBackupMigrationResponse(AbstractModel):
    """ModifyBackupMigration response structure.

    """

    def __init__(self):
        """
        :param BackupMigrationId: Backup import task ID
        :type BackupMigrationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BackupMigrationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyBackupStrategyRequest(AbstractModel):
    """ModifyBackupStrategy request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param BackupType: Backup mode, which supports daily backup only. Valid value: daily.
        :type BackupType: str
        :param BackupTime: Backup time. Value range: an integer from 0 to 23.
        :type BackupTime: int
        :param BackupDay: Backup interval in days when the `BackupType` is `daily`. Valid value: 1.
        :type BackupDay: int
        """
        self.InstanceId = None
        self.BackupType = None
        self.BackupTime = None
        self.BackupDay = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupType = params.get("BackupType")
        self.BackupTime = params.get("BackupTime")
        self.BackupDay = params.get("BackupDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyBackupStrategyResponse(AbstractModel):
    """ModifyBackupStrategy response structure.

    """

    def __init__(self):
        """
        :param Errno: Returned error code.
        :type Errno: int
        :param Msg: Returned error message.
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Errno = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Errno = params.get("Errno")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param InstanceName: New name of database instance
        :type InstanceName: str
        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBInstanceNetworkRequest(AbstractModel):
    """ModifyDBInstanceNetwork request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param NewVpcId: ID of the new VPC
        :type NewVpcId: str
        :param NewSubnetId: ID of the new subnet
        :type NewSubnetId: str
        :param OldIpRetainTime: Retention period (in hours) of the original VIP. Value range: `0-168`. Default value: `0`, indicating the original VIP is released immediately.
        :type OldIpRetainTime: int
        """
        self.InstanceId = None
        self.NewVpcId = None
        self.NewSubnetId = None
        self.OldIpRetainTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewVpcId = params.get("NewVpcId")
        self.NewSubnetId = params.get("NewSubnetId")
        self.OldIpRetainTime = params.get("OldIpRetainTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBInstanceNetworkResponse(AbstractModel):
    """ModifyDBInstanceNetwork response structure.

    """

    def __init__(self):
        """
        :param FlowId: ID of the instance network changing task. You can use the [DescribeFlowStatus](https://intl.cloud.tencent.com/document/product/238/19967?from_cn_redirect=1) API to query the task status.
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject request structure.

    """

    def __init__(self):
        """
        :param InstanceIdSet: Array of instance IDs in the format of mssql-j8kv137v
        :type InstanceIdSet: list of str
        :param ProjectId: Project ID. If this parameter is 0, the default project will be used
        :type ProjectId: int
        """
        self.InstanceIdSet = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject response structure.

    """

    def __init__(self):
        """
        :param Count: Number of successfully modified instances
        :type Count: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBNameRequest(AbstractModel):
    """ModifyDBName request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param OldDBName: Old database name
        :type OldDBName: str
        :param NewDBName: New name of database
        :type NewDBName: str
        """
        self.InstanceId = None
        self.OldDBName = None
        self.NewDBName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldDBName = params.get("OldDBName")
        self.NewDBName = params.get("NewDBName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBNameResponse(AbstractModel):
    """ModifyDBName response structure.

    """

    def __init__(self):
        """
        :param FlowId: Task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBRemarkRequest(AbstractModel):
    """ModifyDBRemark request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of mssql-rljoi3bf
        :type InstanceId: str
        :param DBRemarks: Array of database names and remarks, where each element contains a database name and the corresponding remarks
        :type DBRemarks: list of DBRemark
        """
        self.InstanceId = None
        self.DBRemarks = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DBRemarks") is not None:
            self.DBRemarks = []
            for item in params.get("DBRemarks"):
                obj = DBRemark()
                obj._deserialize(item)
                self.DBRemarks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBRemarkResponse(AbstractModel):
    """ModifyDBRemark response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyIncrementalMigrationRequest(AbstractModel):
    """ModifyIncrementalMigration request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param IncrementalMigrationId: Incremental import task ID
        :type IncrementalMigrationId: str
        :param IsRecovery: Whether restoration is required. No: not required. Yes: required.
        :type IsRecovery: str
        :param BackupFiles: If the UploadType is COS_URL, fill in URL here. If the UploadType is COS_UPLOAD, fill in the name of the backup file here. Only 1 backup file is supported, but a backup file can involve multiple databases.
        :type BackupFiles: list of str
        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.IncrementalMigrationId = None
        self.IsRecovery = None
        self.BackupFiles = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        self.IsRecovery = params.get("IsRecovery")
        self.BackupFiles = params.get("BackupFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyIncrementalMigrationResponse(AbstractModel):
    """ModifyIncrementalMigration response structure.

    """

    def __init__(self):
        """
        :param IncrementalMigrationId: ID of an incremental backup import task
        :type IncrementalMigrationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IncrementalMigrationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMigrationRequest(AbstractModel):
    """ModifyMigration request structure.

    """

    def __init__(self):
        """
        :param MigrateId: Migration task ID
        :type MigrateId: int
        :param MigrateName: New name of migration task. If this parameter is left empty, no modification will be made
        :type MigrateName: str
        :param MigrateType: New migration type (1: structure migration, 2: data migration, 3: incremental sync). If this parameter is left empty, no modification will be made
        :type MigrateType: int
        :param SourceType: Migration source type. 1: TencentDB for SQL Server, 2: CVM-based self-created SQL Server database; 3: SQL Server backup restoration, 4: SQL Server backup restoration (in COS mode). If this parameter is left empty, no modification will be made
        :type SourceType: int
        :param Source: Migration source. If this parameter is left empty, no modification will be made
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param Target: Migration target. If this parameter is left empty, no modification will be made
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param MigrateDBSet: Database objects to be migrated. This parameter is not used for offline migration (SourceType=4 or SourceType=5). If it left empty, no modification will be made
        :type MigrateDBSet: list of MigrateDB
        """
        self.MigrateId = None
        self.MigrateName = None
        self.MigrateType = None
        self.SourceType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.MigrateName = params.get("MigrateName")
        self.MigrateType = params.get("MigrateType")
        self.SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self.Source = MigrateSource()
            self.Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self.Target = MigrateTarget()
            self.Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self.MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self.MigrateDBSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMigrationResponse(AbstractModel):
    """ModifyMigration response structure.

    """

    def __init__(self):
        """
        :param MigrateId: Migration task ID
        :type MigrateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MigrateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RecycleDBInstanceRequest(AbstractModel):
    """RecycleDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RecycleDBInstanceResponse(AbstractModel):
    """RecycleDBInstance response structure.

    """

    def __init__(self):
        """
        :param FlowId: Task ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegionInfo(AbstractModel):
    """Region information

    """

    def __init__(self):
        """
        :param Region: Region ID in the format of ap-guangzhou
        :type Region: str
        :param RegionName: Region name
        :type RegionName: str
        :param RegionId: Numeric ID of region
        :type RegionId: int
        :param RegionState: Current purchasability of this region. UNAVAILABLE: not purchasable, AVAILABLE: purchasable
        :type RegionState: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RenameRestoreDatabase(AbstractModel):
    """Used in the `RestoreInstance`, `RollbackInstance`, `CreateMigration`, and `CloneDB` APIs to specify and rename the database to be restored, rolled back, migrated, or cloned.

    """

    def __init__(self):
        """
        :param OldName: Database name. If the `OldName` database does not exist, a failure will be returned.
It can be left empty in offline migration tasks.
        :type OldName: str
        :param NewName: New database name. In offline migration, `OldName` will be used if `NewName` is left empty (`OldName` and `NewName` cannot be both empty). In database cloning, `OldName` and `NewName` must be both specified and cannot have the same value.
        :type NewName: str
        """
        self.OldName = None
        self.NewName = None


    def _deserialize(self, params):
        self.OldName = params.get("OldName")
        self.NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        :param Accounts: Updated account password information array
        :type Accounts: list of AccountPassword
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPassword()
                obj._deserialize(item)
                self.Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword response structure.

    """

    def __init__(self):
        """
        :param FlowId: ID of async task flow for account password change
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResourceTag(AbstractModel):
    """The information of tags associated with instances

    """

    def __init__(self):
        """
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Database instance ID in the format of mssql-njj2mtpl
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RestartDBInstanceResponse(AbstractModel):
    """RestartDBInstance response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        :param BackupId: Backup file ID, which can be obtained through the `Id` field in the returned value of the `DescribeBackups` API
        :type BackupId: int
        :param TargetInstanceId: ID of the target instance to which the backup is restored. The target instance should be under the same `APPID`. If this parameter is left empty, ID of the source instance will be used.
        :type TargetInstanceId: str
        :param RenameRestore: Restore the databases listed in `ReNameRestoreDatabase` and rename them after restoration. If this parameter is left empty, all databases will be restored and renamed in the default format.
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self.InstanceId = None
        self.BackupId = None
        self.TargetInstanceId = None
        self.RenameRestore = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")
        self.TargetInstanceId = params.get("TargetInstanceId")
        if params.get("RenameRestore") is not None:
            self.RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self.RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async flow task ID, which can be used to call the `DescribeFlowStatus` API to get the task execution status
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RollbackInstanceRequest(AbstractModel):
    """RollbackInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Type: Rollback type. 0: the database rolled back overwrites the original database; 1: the database rolled back is renamed and does not overwrite the original database
        :type Type: int
        :param DBs: Database to be rolled back
        :type DBs: list of str
        :param Time: Target time point for rollback
        :type Time: str
        :param TargetInstanceId: ID of the target instance to which the backup is restored. The target instance should be under the same `APPID`. If this parameter is left empty, ID of the source instance will be used.
        :type TargetInstanceId: str
        :param RenameRestore: Rename the databases listed in `ReNameRestoreDatabase`. This parameter takes effect only when `Type = 1` which indicates that backup rollback supports renaming databases. If it is left empty, databases will be renamed in the default format and the `DBs` parameter specifies the databases to be restored.
        :type RenameRestore: list of RenameRestoreDatabase
        """
        self.InstanceId = None
        self.Type = None
        self.DBs = None
        self.Time = None
        self.TargetInstanceId = None
        self.RenameRestore = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.DBs = params.get("DBs")
        self.Time = params.get("Time")
        self.TargetInstanceId = params.get("TargetInstanceId")
        if params.get("RenameRestore") is not None:
            self.RenameRestore = []
            for item in params.get("RenameRestore"):
                obj = RenameRestoreDatabase()
                obj._deserialize(item)
                self.RenameRestore.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RollbackInstanceResponse(AbstractModel):
    """RollbackInstance response structure.

    """

    def __init__(self):
        """
        :param FlowId: The async job ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RunMigrationRequest(AbstractModel):
    """RunMigration request structure.

    """

    def __init__(self):
        """
        :param MigrateId: Migration task ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RunMigrationResponse(AbstractModel):
    """RunMigration response structure.

    """

    def __init__(self):
        """
        :param FlowId: After the migration task starts, the flow ID will be returned
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SlowlogInfo(AbstractModel):
    """Slow query log file information

    """

    def __init__(self):
        """
        :param Id: Unique ID of slow query log file
        :type Id: int
        :param StartTime: File generation start time
        :type StartTime: str
        :param EndTime: File generation end time
        :type EndTime: str
        :param Size: File size in KB
        :type Size: int
        :param Count: Number of logs in file
        :type Count: int
        :param InternalAddr: Download address for private network
        :type InternalAddr: str
        :param ExternalAddr: Download address for public network
        :type ExternalAddr: str
        :param Status: Status (1: success, 2: failure)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Count = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Count = params.get("Count")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SpecInfo(AbstractModel):
    """Information of purchasable specification for an instance

    """

    def __init__(self):
        """
        :param SpecId: Instance specification ID. The `SpecId` returned by `DescribeZones` together with the purchasable specification information returned by `DescribeProductConfig` can be used to find out what specifications can be purchased in a specified AZ
        :type SpecId: int
        :param MachineType: Model ID
        :type MachineType: str
        :param MachineTypeName: Model name
        :type MachineTypeName: str
        :param Version: Database version information. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise)
        :type Version: str
        :param VersionName: Version name corresponding to the `Version` field
        :type VersionName: str
        :param Memory: Memory size in GB
        :type Memory: int
        :param CPU: Number of CPU cores
        :type CPU: int
        :param MinStorage: Minimum disk size under this specification in GB
        :type MinStorage: int
        :param MaxStorage: Maximum disk size under this specification in GB
        :type MaxStorage: int
        :param QPS: QPS of this specification
        :type QPS: int
        :param SuitInfo: Description of this specification
        :type SuitInfo: str
        :param Pid: Pid of this specification
        :type Pid: int
        :param PostPid: Pay-as-you-go Pid list corresponding to this specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type PostPid: list of int
        :param PayModeStatus: Billing mode under this specification. POST: pay-as-you-go
        :type PayModeStatus: str
        :param InstanceType: Instance type. Valid values: HA (High-Availability Edition, including dual-server high availability and AlwaysOn cluster), RO (read-only replica), SI (Basic Edition)
        :type InstanceType: str
        :param MultiZonesStatus: Whether multi-AZ deployment is supported. Valid values: MultiZones (only multi-AZ deployment is supported), SameZones (only single-AZ deployment is supported), ALL (both deployments are supported)
        :type MultiZonesStatus: str
        """
        self.SpecId = None
        self.MachineType = None
        self.MachineTypeName = None
        self.Version = None
        self.VersionName = None
        self.Memory = None
        self.CPU = None
        self.MinStorage = None
        self.MaxStorage = None
        self.QPS = None
        self.SuitInfo = None
        self.Pid = None
        self.PostPid = None
        self.PayModeStatus = None
        self.InstanceType = None
        self.MultiZonesStatus = None


    def _deserialize(self, params):
        self.SpecId = params.get("SpecId")
        self.MachineType = params.get("MachineType")
        self.MachineTypeName = params.get("MachineTypeName")
        self.Version = params.get("Version")
        self.VersionName = params.get("VersionName")
        self.Memory = params.get("Memory")
        self.CPU = params.get("CPU")
        self.MinStorage = params.get("MinStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.QPS = params.get("QPS")
        self.SuitInfo = params.get("SuitInfo")
        self.Pid = params.get("Pid")
        self.PostPid = params.get("PostPid")
        self.PayModeStatus = params.get("PayModeStatus")
        self.InstanceType = params.get("InstanceType")
        self.MultiZonesStatus = params.get("MultiZonesStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartBackupMigrationRequest(AbstractModel):
    """StartBackupMigration request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        """
        self.InstanceId = None
        self.BackupMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartBackupMigrationResponse(AbstractModel):
    """StartBackupMigration response structure.

    """

    def __init__(self):
        """
        :param FlowId: Task ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartIncrementalMigrationRequest(AbstractModel):
    """StartIncrementalMigration request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of imported target instance
        :type InstanceId: str
        :param BackupMigrationId: Backup import task ID, which is returned through the API CreateBackupMigration
        :type BackupMigrationId: str
        :param IncrementalMigrationId: ID of an incremental backup import task
        :type IncrementalMigrationId: str
        """
        self.InstanceId = None
        self.BackupMigrationId = None
        self.IncrementalMigrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMigrationId = params.get("BackupMigrationId")
        self.IncrementalMigrationId = params.get("IncrementalMigrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartIncrementalMigrationResponse(AbstractModel):
    """StartIncrementalMigration response structure.

    """

    def __init__(self):
        """
        :param FlowId: Task ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TerminateDBInstanceRequest(AbstractModel):
    """TerminateDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceIdSet: List of instance IDs manually terminated in the format of [mssql-3l3fgqn7], which are the same as the instance IDs displayed on the TencentDB Console page
        :type InstanceIdSet: list of str
        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of mssql-j8kv137v
        :type InstanceId: str
        :param Memory: Memory size after instance upgrade in GB, which cannot be smaller than the current instance memory size
        :type Memory: int
        :param Storage: Storage capacity after instance upgrade in GB, which cannot be smaller than the current instance storage capacity
        :type Storage: int
        :param AutoVoucher: Whether to automatically use vouchers. 0: no, 1: yes. Default value: 0
        :type AutoVoucher: int
        :param VoucherIds: Voucher ID (currently, only one voucher can be used per order)
        :type VoucherIds: list of str
        :param Cpu: The number of CUP cores after the instance is upgraded.
        :type Cpu: int
        :param DBVersion: Upgrade the SQL Server version. Supported versions include SQL Server 2008 Enterprise (`2008R2`), SQL Server 2012 Enterprise (`2012SP3`), etc. As the purchasable versions are region-specific, you can use the `DescribeProductConfig` API to query the information of purchasable versions in each region. Downgrading is unsupported. If this parameter is left empty, the SQL Server version will not be changed.
        :type DBVersion: str
        :param HAType: Upgrade the high availability architecture from image-based disaster recovery to Always On cluster disaster recovery. This parameter is valid only for instances which support Always On high availability and run SQL Server 2017 or later. Neither downgrading to image-based disaster recovery nor upgrading from cluster disaster recovery to Always On disaster recovery is supported. If this parameter is left empty, the high availability architecture will not be changed.
        :type HAType: str
        :param MultiZones: Change the instance deployment scheme. Valid values: `SameZones` (change to single-AZ deployment, which does not support cross-AZ disaster recovery), `MultiZones` (change to multi-AZ deployment, which supports cross-AZ disaster recovery).
        :type MultiZones: str
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.Cpu = None
        self.DBVersion = None
        self.HAType = None
        self.MultiZones = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.Cpu = params.get("Cpu")
        self.DBVersion = params.get("DBVersion")
        self.HAType = params.get("HAType")
        self.MultiZones = params.get("MultiZones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance response structure.

    """

    def __init__(self):
        """
        :param DealName: Order name
        :type DealName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ZoneInfo(AbstractModel):
    """AZ information

    """

    def __init__(self):
        """
        :param Zone: AZ ID in the format of ap-guangzhou-1 (i.e., Guangzhou Zone 1)
        :type Zone: str
        :param ZoneName: AZ name
        :type ZoneName: str
        :param ZoneId: Numeric ID of AZ
        :type ZoneId: int
        :param SpecId: ID of specification purchasable in this AZ, which, together with the returned value of the `DescribeProductConfig` API, can be used to find out the specifications currently purchasable in the AZ
        :type SpecId: int
        :param Version: Information of database versions purchasable under the current AZ and specification. Valid values: 2008R2 (SQL Server 2008 Enterprise), 2012SP3 (SQL Server 2012 Enterprise), 2016SP1 (SQL Server 2016 Enterprise), 201602 (SQL Server 2016 Standard), 2017 (SQL Server 2017 Enterprise)
        :type Version: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.SpecId = None
        self.Version = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.SpecId = params.get("SpecId")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        