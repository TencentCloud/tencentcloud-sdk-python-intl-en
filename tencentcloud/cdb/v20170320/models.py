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


class Account(AbstractModel):
    """TencentDB account information

    """

    def __init__(self):
        """
        :param User: New account name\n        :type User: str\n        :param Host: New account domain name\n        :type Host: str\n        """
        self.User = None
        self.Host = None


    def _deserialize(self, params):
        self.User = params.get("User")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountInfo(AbstractModel):
    """Account details

    """

    def __init__(self):
        """
        :param Notes: Account remarks\n        :type Notes: str\n        :param Host: Account domain name\n        :type Host: str\n        :param User: Account name\n        :type User: str\n        :param ModifyTime: Account information modification time\n        :type ModifyTime: str\n        :param ModifyPasswordTime: Password modification time\n        :type ModifyPasswordTime: str\n        :param CreateTime: This parameter is no longer supported.\n        :type CreateTime: str\n        :param MaxUserConnections: The maximum number of instance connections supported by an account\n        :type MaxUserConnections: int\n        """
        self.Notes = None
        self.Host = None
        self.User = None
        self.ModifyTime = None
        self.ModifyPasswordTime = None
        self.CreateTime = None
        self.MaxUserConnections = None


    def _deserialize(self, params):
        self.Notes = params.get("Notes")
        self.Host = params.get("Host")
        self.User = params.get("User")
        self.ModifyTime = params.get("ModifyTime")
        self.ModifyPasswordTime = params.get("ModifyPasswordTime")
        self.CreateTime = params.get("CreateTime")
        self.MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTimeWindowRequest(AbstractModel):
    """AddTimeWindow request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Monday: Maintenance window on Monday. The format should be 10:00-12:00. You can set multiple time windows on a day. Each time window lasts from half an hour to three hours, and must start and end on the hour or half hour. At least one time window is required in a week. The same rule applies to the following parameters.\n        :type Monday: list of str\n        :param Tuesday: Maintenance window on Tuesday. At least one time window is required in a week.\n        :type Tuesday: list of str\n        :param Wednesday: Maintenance window on Wednesday. At least one time window is required in a week.\n        :type Wednesday: list of str\n        :param Thursday: Maintenance window on Thursday. At least one time window is required in a week.\n        :type Thursday: list of str\n        :param Friday: Maintenance window on Friday. At least one time window is required in a week.\n        :type Friday: list of str\n        :param Saturday: Maintenance window on Saturday. At least one time window is required in a week.\n        :type Saturday: list of str\n        :param Sunday: Maintenance window on Sunday. At least one time window is required in a week.\n        :type Sunday: list of str\n        """
        self.InstanceId = None
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.Saturday = None
        self.Sunday = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Monday = params.get("Monday")
        self.Tuesday = params.get("Tuesday")
        self.Wednesday = params.get("Wednesday")
        self.Thursday = params.get("Thursday")
        self.Friday = params.get("Friday")
        self.Saturday = params.get("Saturday")
        self.Sunday = params.get("Sunday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTimeWindowResponse(AbstractModel):
    """AddTimeWindow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: Security group ID.\n        :type SecurityGroupId: str\n        :param InstanceIds: List of instance IDs, which is an array of one or more instance IDs.\n        :type InstanceIds: list of str\n        :param ForReadonlyInstance: This parameter takes effect only when the IDs of read-only replicas are passed in. If this parameter is set to `False` or left empty, the security group will be bound to the RO groups of these read-only replicas. If this parameter is set to `True`, the security group will be bound to the read-only replicas themselves.\n        :type ForReadonlyInstance: bool\n        """
        self.SecurityGroupId = None
        self.InstanceIds = None
        self.ForReadonlyInstance = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        self.ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BackupConfig(AbstractModel):
    """Configuration information of ECDB secondary database 2. This field is only applicable to ECDB instances

    """

    def __init__(self):
        """
        :param ReplicationMode: Replication mode of secondary database 2. Value range: async, semi-sync\n        :type ReplicationMode: str\n        :param Zone: Name of the AZ of secondary database 2, such as ap-shanghai-1\n        :type Zone: str\n        :param Vip: Private IP address of secondary database 2\n        :type Vip: str\n        :param Vport: Access port of secondary database 2\n        :type Vport: int\n        """
        self.ReplicationMode = None
        self.Zone = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.ReplicationMode = params.get("ReplicationMode")
        self.Zone = params.get("Zone")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInfo(AbstractModel):
    """Backup details

    """

    def __init__(self):
        """
        :param Name: Backup filename\n        :type Name: str\n        :param Size: Backup file size in bytes\n        :type Size: int\n        :param Date: Backup snapshot time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-03-17 02:10:37\n        :type Date: str\n        :param IntranetUrl: Download address on the private network\n        :type IntranetUrl: str\n        :param InternetUrl: Download address on the public network\n        :type InternetUrl: str\n        :param Type: Log type. Valid values: `logical` (logical cold backup), `physical` (physical cold backup).\n        :type Type: str\n        :param BackupId: Backup subtask ID, which is used when backup files are deleted\n        :type BackupId: int\n        :param Status: Backup task status. Valid values: `SUCCESS` (backup succeeded), `FAILED` (backup failed), `RUNNING` (backup is in progress).\n        :type Status: str\n        :param FinishTime: Backup task completion time\n        :type FinishTime: str\n        :param Creator: (This field will be disused and is thus not recommended) backup creator. Valid values: `SYSTEM` (created by system), `Uin` (initiator's `Uin` value).\n        :type Creator: str\n        :param StartTime: Backup task start time\n        :type StartTime: str\n        :param Method: Backup method. Valid values: `full` (full backup), `partial` (partial backup).\n        :type Method: str\n        :param Way: Backup mode. Valid values: `manual` (manual backup), `automatic` (automatic backup).\n        :type Way: str\n        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None
        self.BackupId = None
        self.Status = None
        self.FinishTime = None
        self.Creator = None
        self.StartTime = None
        self.Method = None
        self.Way = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")
        self.BackupId = params.get("BackupId")
        self.Status = params.get("Status")
        self.FinishTime = params.get("FinishTime")
        self.Creator = params.get("Creator")
        self.StartTime = params.get("StartTime")
        self.Method = params.get("Method")
        self.Way = params.get("Way")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupItem(AbstractModel):
    """When creating a backup, you need to specify the information of the table to be backed up.

    """

    def __init__(self):
        """
        :param Db: Name of the database to be backed up\n        :type Db: str\n        :param Table: Name of the table to be backed up. If this parameter is passed in, the specified table in the database will be backed up; otherwise, the database will be backed up.\n        :type Table: str\n        """
        self.Db = None
        self.Table = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSummaryItem(AbstractModel):
    """Statistical items of instance backup

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param AutoBackupCount: Number of automatic data backups of an instance.\n        :type AutoBackupCount: int\n        :param AutoBackupVolume: Capacity of automatic data backups of an instance.\n        :type AutoBackupVolume: int\n        :param ManualBackupCount: Number of manual data backups of an instance.\n        :type ManualBackupCount: int\n        :param ManualBackupVolume: Capacity of manual data backups of an instance.\n        :type ManualBackupVolume: int\n        :param DataBackupCount: Total number of data backups of an instance (including automatic backups and manual backups).\n        :type DataBackupCount: int\n        :param DataBackupVolume: Total capacity of data backups of an instance.\n        :type DataBackupVolume: int\n        :param BinlogBackupCount: Number of log backups of an instance.\n        :type BinlogBackupCount: int\n        :param BinlogBackupVolume: Capacity of log backups of an instance.\n        :type BinlogBackupVolume: int\n        :param BackupVolume: Total capacity of backups of an instance (including data backups and log backups).\n        :type BackupVolume: int\n        """
        self.InstanceId = None
        self.AutoBackupCount = None
        self.AutoBackupVolume = None
        self.ManualBackupCount = None
        self.ManualBackupVolume = None
        self.DataBackupCount = None
        self.DataBackupVolume = None
        self.BinlogBackupCount = None
        self.BinlogBackupVolume = None
        self.BackupVolume = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AutoBackupCount = params.get("AutoBackupCount")
        self.AutoBackupVolume = params.get("AutoBackupVolume")
        self.ManualBackupCount = params.get("ManualBackupCount")
        self.ManualBackupVolume = params.get("ManualBackupVolume")
        self.DataBackupCount = params.get("DataBackupCount")
        self.DataBackupVolume = params.get("DataBackupVolume")
        self.BinlogBackupCount = params.get("BinlogBackupCount")
        self.BinlogBackupVolume = params.get("BinlogBackupVolume")
        self.BackupVolume = params.get("BackupVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceRoGroupLoadRequest(AbstractModel):
    """BalanceRoGroupLoad request structure.

    """

    def __init__(self):
        """
        :param RoGroupId: RO group ID in the format of `cdbrg-c1nl9rpv`.\n        :type RoGroupId: str\n        """
        self.RoGroupId = None


    def _deserialize(self, params):
        self.RoGroupId = params.get("RoGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceRoGroupLoadResponse(AbstractModel):
    """BalanceRoGroupLoad response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BinlogInfo(AbstractModel):
    """Binlog information

    """

    def __init__(self):
        """
        :param Name: Binlog backup filename\n        :type Name: str\n        :param Size: Backup file size in bytes\n        :type Size: int\n        :param Date: File stored time in the format of 2016-03-17 02:10:37\n        :type Date: str\n        :param IntranetUrl: Download address on the private network\n        :type IntranetUrl: str\n        :param InternetUrl: Download address on the public network\n        :type InternetUrl: str\n        :param Type: Log type. Value range: binlog\n        :type Type: str\n        :param BinlogStartTime: Binlog file start file\n        :type BinlogStartTime: str\n        :param BinlogFinishTime: Binlog file end time\n        :type BinlogFinishTime: str\n        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None
        self.BinlogStartTime = None
        self.BinlogFinishTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")
        self.BinlogStartTime = params.get("BinlogStartTime")
        self.BinlogFinishTime = params.get("BinlogFinishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneItem(AbstractModel):
    """Clone task information.

    """

    def __init__(self):
        """
        :param SrcInstanceId: ID of the original instance in a clone task\n        :type SrcInstanceId: str\n        :param DstInstanceId: ID of the cloned instance in a clone task\n        :type DstInstanceId: str\n        :param CloneJobId: Clone task ID\n        :type CloneJobId: int\n        :param RollbackStrategy: The policy used in a clone task. Valid values: `timepoint` (roll back to a specific point in time), `backupset` (roll back by using a specific backup file).\n        :type RollbackStrategy: str\n        :param RollbackTargetTime: The point in time to which the cloned instance will be rolled back\n        :type RollbackTargetTime: str\n        :param StartTime: Task start time\n        :type StartTime: str\n        :param EndTime: Task end time\n        :type EndTime: str\n        :param TaskStatus: Task status. Valid values: `initial`, `running`, `wait_complete`, `success`, `failed`.\n        :type TaskStatus: str\n        """
        self.SrcInstanceId = None
        self.DstInstanceId = None
        self.CloneJobId = None
        self.RollbackStrategy = None
        self.RollbackTargetTime = None
        self.StartTime = None
        self.EndTime = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.SrcInstanceId = params.get("SrcInstanceId")
        self.DstInstanceId = params.get("DstInstanceId")
        self.CloneJobId = params.get("CloneJobId")
        self.RollbackStrategy = params.get("RollbackStrategy")
        self.RollbackTargetTime = params.get("RollbackTargetTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWanServiceRequest(AbstractModel):
    """CloseWanService request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWanServiceResponse(AbstractModel):
    """CloseWanService response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """Column permission information

    """

    def __init__(self):
        """
        :param Database: Database name\n        :type Database: str\n        :param Table: Table name\n        :type Table: str\n        :param Column: Column name\n        :type Column: str\n        :param Privileges: Permission information\n        :type Privileges: list of str\n        """
        self.Database = None
        self.Table = None
        self.Column = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.Column = params.get("Column")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonTimeWindow(AbstractModel):
    """Common time window

    """

    def __init__(self):
        """
        :param Monday: Time window on Monday in the format of 02:00-06:00\n        :type Monday: str\n        :param Tuesday: Time window on Tuesday in the format of 02:00-06:00\n        :type Tuesday: str\n        :param Wednesday: Time window on Wednesday in the format of 02:00-06:00\n        :type Wednesday: str\n        :param Thursday: Time window on Thursday in the format of 02:00-06:00\n        :type Thursday: str\n        :param Friday: Time window on Friday in the format of 02:00-06:00\n        :type Friday: str\n        :param Saturday: Time window on Saturday in the format of 02:00-06:00\n        :type Saturday: str\n        :param Sunday: Time window on Sunday in the format of 02:00-06:00\n        :type Sunday: str\n        """
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.Saturday = None
        self.Sunday = None


    def _deserialize(self, params):
        self.Monday = params.get("Monday")
        self.Tuesday = params.get("Tuesday")
        self.Wednesday = params.get("Wednesday")
        self.Thursday = params.get("Thursday")
        self.Friday = params.get("Friday")
        self.Saturday = params.get("Saturday")
        self.Sunday = params.get("Sunday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsRequest(AbstractModel):
    """CreateAccounts request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Accounts: TencentDB account.\n        :type Accounts: list of Account\n        :param Password: Password of the new account\n        :type Password: str\n        :param Description: Remarks\n        :type Description: str\n        :param MaxUserConnections: The maximum number of instance connections supported by the new account\n        :type MaxUserConnections: int\n        """
        self.InstanceId = None
        self.Accounts = None
        self.Password = None
        self.Description = None
        self.MaxUserConnections = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.Password = params.get("Password")
        self.Description = params.get("Description")
        self.MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsResponse(AbstractModel):
    """CreateAccounts response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param BackupMethod: Backup method of target instance. Value range: logical (logical cold backup), physical (physical cold backup).\n        :type BackupMethod: str\n        :param BackupDBTableList: Information of the table to be backed up. If this parameter is not set, the entire instance will be backed up by default. It can be set only in logical backup (i.e., BackupMethod = logical). The specified table must exist; otherwise, backup may fail.
For example, if you want to backup tb1 and tb2 in db1 and the entire db2, you should set the parameter as [{"Db": "db1", "Table": "tb1"}, {"Db": "db1", "Table": "tb2"}, {"Db": "db2"} ].\n        :type BackupDBTableList: list of BackupItem\n        """
        self.InstanceId = None
        self.BackupMethod = None
        self.BackupDBTableList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMethod = params.get("BackupMethod")
        if params.get("BackupDBTableList") is not None:
            self.BackupDBTableList = []
            for item in params.get("BackupDBTableList"):
                obj = BackupItem()
                obj._deserialize(item)
                self.BackupDBTableList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup response structure.

    """

    def __init__(self):
        """
        :param BackupId: Backup task ID\n        :type BackupId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.BackupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupId = params.get("BackupId")
        self.RequestId = params.get("RequestId")


class CreateCloneInstanceRequest(AbstractModel):
    """CreateCloneInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the instance to be cloned from\n        :type InstanceId: str\n        :param SpecifiedRollbackTime: To roll back the cloned instance to a specific point in time, set this parameter to a value in the format of "yyyy-mm-dd hh:mm:ss".\n        :type SpecifiedRollbackTime: str\n        :param SpecifiedBackupId: To roll back the cloned instance to a specific physical backup file, set this parameter to the ID of the physical backup file. The ID can be obtained by the [DescribeBackups](https://intl.cloud.tencent.com/document/api/236/15842?from_cn_redirect=1) API.\n        :type SpecifiedBackupId: int\n        :param UniqVpcId: VPC ID, which can be obtained by the [DescribeVpcs](https://intl.cloud.tencent.com/document/api/215/15778?from_cn_redirect=1) API. If this parameter is left empty, the classic network will be used by default.\n        :type UniqVpcId: str\n        :param UniqSubnetId: VPC subnet ID, which can be obtained by the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API. If `UniqVpcId` is set, `UniqSubnetId` will be required.\n        :type UniqSubnetId: str\n        :param Memory: Memory of the cloned instance in MB, which should be equal to (by default) or larger than that of the original instance\n        :type Memory: int\n        :param Volume: Disk capacity of the cloned instance in GB, which should be equal to (by default) or larger than that of the original instance\n        :type Volume: int\n        :param InstanceName: Name of the cloned instance\n        :type InstanceName: str\n        :param SecurityGroup: Security group parameter, which can be obtained by the [DescribeProjectSecurityGroups](https://intl.cloud.tencent.com/document/api/236/15850?from_cn_redirect=1) API\n        :type SecurityGroup: list of str\n        :param ResourceTags: Information of the cloned instance tag\n        :type ResourceTags: list of TagInfo\n        :param Cpu: The number of CPU cores of the cloned instance. It should be equal to (by default) or larger than that of the original instance.\n        :type Cpu: int\n        :param ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). Default value: 0.\n        :type ProtectMode: int\n        :param DeployMode: Multi-AZ or single-AZ. Valid values: 0 (single-AZ), 1 (multi-AZ). Default value: 0.\n        :type DeployMode: int\n        :param SlaveZone: Availability zone information of replica 1 of the cloned instance, which is the same as the value of `Zone` of the original instance by default\n        :type SlaveZone: str\n        :param BackupZone: Availability zone information of replica 2 of the cloned instance, 
which is left empty by default. Specify this parameter when cloning a strong sync source instance.\n        :type BackupZone: str\n        :param DeviceType: Resource isolation type of the clone. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance). Default value: `UNIVERSAL`.\n        :type DeviceType: str\n        :param InstanceNodes: The number of nodes of the clone. If this parameter is set to `3` or the `BackupZone` parameter is specified, the clone will have three nodes. If this parameter is set to `2` or left empty, the clone will have two nodes.\n        :type InstanceNodes: int\n        """
        self.InstanceId = None
        self.SpecifiedRollbackTime = None
        self.SpecifiedBackupId = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.Memory = None
        self.Volume = None
        self.InstanceName = None
        self.SecurityGroup = None
        self.ResourceTags = None
        self.Cpu = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.BackupZone = None
        self.DeviceType = None
        self.InstanceNodes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpecifiedRollbackTime = params.get("SpecifiedRollbackTime")
        self.SpecifiedBackupId = params.get("SpecifiedBackupId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroup = params.get("SecurityGroup")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.Cpu = params.get("Cpu")
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        self.BackupZone = params.get("BackupZone")
        self.DeviceType = params.get("DeviceType")
        self.InstanceNodes = params.get("InstanceNodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloneInstanceResponse(AbstractModel):
    """CreateCloneInstance response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: LimitAsync task request ID, which can be used to query the execution result of an async task\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateDBImportJobRequest(AbstractModel):
    """CreateDBImportJob request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param FileName: Filename. The file should have already been uploaded to Tencent Cloud.\n        :type FileName: str\n        :param User: TencentDB username\n        :type User: str\n        :param Password: Password of a TencentDB instance user account\n        :type Password: str\n        :param DbName: Name of the target database. If this parameter is not passed in, no database is specified.\n        :type DbName: str\n        """
        self.InstanceId = None
        self.FileName = None
        self.User = None
        self.Password = None
        self.DbName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FileName = params.get("FileName")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBImportJobResponse(AbstractModel):
    """CreateDBImportJob response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour request structure.

    """

    def __init__(self):
        """
        :param GoodsNum: Number of instances. Value range: 1-100. Default value: 1.\n        :type GoodsNum: int\n        :param Memory: Instance memory size in MB. Please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported memory specifications.\n        :type Memory: int\n        :param Volume: Instance disk size in GB. Please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported disk specifications.\n        :type Volume: int\n        :param EngineVersion: MySQL version. Valid values: `5.5`, `5.6`, `5.7`, `8.0`. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported versions.\n        :type EngineVersion: str\n        :param UniqVpcId: VPC ID. If this parameter is not passed in, the basic network will be selected by default. Please use the [DescribeVpcs](https://intl.cloud.tencent.com/document/api/215/15778?from_cn_redirect=1) API to query the VPCs.\n        :type UniqVpcId: str\n        :param UniqSubnetId: VPC subnet ID. If `UniqVpcId` is set, then `UniqSubnetId` will be required. Please use the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API to query the subnet lists.\n        :type UniqSubnetId: str\n        :param ProjectId: Project ID. If this is left empty, the default project will be used. Please use the [DescribeProject](https://intl.cloud.tencent.com/document/product/378/4400?from_cn_redirect=1) API to get the project ID.\n        :type ProjectId: int\n        :param Zone: AZ information. By default, the system will automatically select an AZ. Please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported AZs.\n        :type Zone: str\n        :param MasterInstanceId: Instance ID, which is required and the same as the primary instance ID when purchasing read-only or disaster recovery instances. Please use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the instance IDs.\n        :type MasterInstanceId: str\n        :param InstanceRole: Instance type. Valid values: master (primary instance), dr (disaster recovery instance), ro (read-only instance). Default value: master.\n        :type InstanceRole: str\n        :param MasterRegion: AZ information of the primary instance, which is required for purchasing disaster recovery instances.\n        :type MasterRegion: str\n        :param Port: Custom port. Value range: [1024-65535].\n        :type Port: int\n        :param Password: Sets the root account password. Rule: the password can contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special symbols (_+-&=!@#$%^*()). This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.\n        :type Password: str\n        :param ParamList: List of parameters in the format of `ParamList.0.Name=auto_increment&ParamList.0.Value=1`. You can use the [DescribeDefaultParams](https://intl.cloud.tencent.com/document/api/236/32662?from_cn_redirect=1) API to query the configurable parameters.\n        :type ParamList: list of ParamInfo\n        :param ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). Default value: 0. This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.\n        :type ProtectMode: int\n        :param DeployMode: Multi-AZ. Valid value: 0 (single-AZ), 1 (multi-AZ). Default value: 0. This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.\n        :type DeployMode: int\n        :param SlaveZone: AZ information of secondary database 1, which is the `Zone` value by default. This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.\n        :type SlaveZone: str\n        :param BackupZone: The availability zone information of Replica 2, which is left empty by default. Specify this parameter when purchasing a source instance in the one-source-two-replica architecture.\n        :type BackupZone: str\n        :param SecurityGroup: Security group parameter. You can use the [DescribeProjectSecurityGroups](https://intl.cloud.tencent.com/document/api/236/15850?from_cn_redirect=1) API to query the security group details of a project.\n        :type SecurityGroup: list of str\n        :param RoGroup: Read-only instance information. This parameter must be passed in when purchasing read-only instances.\n        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`\n        :param AutoRenewFlag: This field is meaningless when purchasing pay-as-you-go instances.\n        :type AutoRenewFlag: int\n        :param InstanceName: Instance name.\n        :type InstanceName: str\n        :param ResourceTags: Instance tag information.\n        :type ResourceTags: list of TagInfo\n        :param DeployGroupId: Placement group ID.\n        :type DeployGroupId: str\n        :param ClientToken: A string that is used to guarantee the idempotency of the request, which is generated by the user and must be unique in each request on the same day. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\n        :type ClientToken: str\n        :param DeviceType: Instance resource isolation type. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance). Default value: `UNIVERSAL`.\n        :type DeviceType: str\n        :param ParamTemplateId: Parameter template ID.\n        :type ParamTemplateId: int\n        :param AlarmPolicyList: The array of alarm policy IDs.\n        :type AlarmPolicyList: list of int\n        :param InstanceNodes: The number of nodes of the instance. To purchase a read-only replica or a basic instance, set this parameter to `1` or leave it empty. To purchase a three-node instance, set this parameter to `3` or specify the `BackupZone` parameter. If the instance to be purchased is a source instance and both `BackupZone` and this parameter are left empty, the value `2` will be used, which indicates the source instance will have two nodes.\n        :type InstanceNodes: int\n        :param Cpu: The number of CPU cores of the instance. If this parameter is left empty, the number of CPU cores depends on the `Memory` value.\n        :type Cpu: int\n        :param AutoSyncFlag: Whether to automatically start disaster recovery synchronization. This parameter takes effect only for disaster recovery instances. Valid values: `0` (no), `1` (yes).\n        :type AutoSyncFlag: int\n        """
        self.GoodsNum = None
        self.Memory = None
        self.Volume = None
        self.EngineVersion = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.ProjectId = None
        self.Zone = None
        self.MasterInstanceId = None
        self.InstanceRole = None
        self.MasterRegion = None
        self.Port = None
        self.Password = None
        self.ParamList = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.BackupZone = None
        self.SecurityGroup = None
        self.RoGroup = None
        self.AutoRenewFlag = None
        self.InstanceName = None
        self.ResourceTags = None
        self.DeployGroupId = None
        self.ClientToken = None
        self.DeviceType = None
        self.ParamTemplateId = None
        self.AlarmPolicyList = None
        self.InstanceNodes = None
        self.Cpu = None
        self.AutoSyncFlag = None


    def _deserialize(self, params):
        self.GoodsNum = params.get("GoodsNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.EngineVersion = params.get("EngineVersion")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.ProjectId = params.get("ProjectId")
        self.Zone = params.get("Zone")
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.InstanceRole = params.get("InstanceRole")
        self.MasterRegion = params.get("MasterRegion")
        self.Port = params.get("Port")
        self.Password = params.get("Password")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        self.BackupZone = params.get("BackupZone")
        self.SecurityGroup = params.get("SecurityGroup")
        if params.get("RoGroup") is not None:
            self.RoGroup = RoGroup()
            self.RoGroup._deserialize(params.get("RoGroup"))
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DeployGroupId = params.get("DeployGroupId")
        self.ClientToken = params.get("ClientToken")
        self.DeviceType = params.get("DeviceType")
        self.ParamTemplateId = params.get("ParamTemplateId")
        self.AlarmPolicyList = params.get("AlarmPolicyList")
        self.InstanceNodes = params.get("InstanceNodes")
        self.Cpu = params.get("Cpu")
        self.AutoSyncFlag = params.get("AutoSyncFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour response structure.

    """

    def __init__(self):
        """
        :param DealIds: Short order ID.\n        :type DealIds: list of str\n        :param InstanceIds: Instance ID list\n        :type InstanceIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DealIds = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateDeployGroupRequest(AbstractModel):
    """CreateDeployGroup request structure.

    """

    def __init__(self):
        """
        :param DeployGroupName: Name of a placement group, which can contain up to 60 characters.\n        :type DeployGroupName: str\n        :param Description: Description of a placement group, which can contain up to 200 characters.\n        :type Description: str\n        :param Affinity: Affinity policy of placement group. Currently, the value of this parameter can only be 1. Policy 1 indicates the upper limit of instances on one physical machine.\n        :type Affinity: list of int\n        :param LimitNum: Upper limit of instances on one physical machine as defined in affinity policy 1 of placement group.\n        :type LimitNum: int\n        :param DevClass: Model attribute of placement group. Valid values: SH12+SH02, TS85.\n        :type DevClass: list of str\n        """
        self.DeployGroupName = None
        self.Description = None
        self.Affinity = None
        self.LimitNum = None
        self.DevClass = None


    def _deserialize(self, params):
        self.DeployGroupName = params.get("DeployGroupName")
        self.Description = params.get("Description")
        self.Affinity = params.get("Affinity")
        self.LimitNum = params.get("LimitNum")
        self.DevClass = params.get("DevClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeployGroupResponse(AbstractModel):
    """CreateDeployGroup response structure.

    """

    def __init__(self):
        """
        :param DeployGroupId: Placement group ID.\n        :type DeployGroupId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DeployGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate request structure.

    """

    def __init__(self):
        """
        :param Name: Parameter template name.\n        :type Name: str\n        :param Description: Parameter template description.\n        :type Description: str\n        :param EngineVersion: MySQL version number.\n        :type EngineVersion: str\n        :param TemplateId: Source parameter template ID.\n        :type TemplateId: int\n        :param ParamList: List of parameters.\n        :type ParamList: list of Parameter\n        """
        self.Name = None
        self.Description = None
        self.EngineVersion = None
        self.TemplateId = None
        self.ParamList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.EngineVersion = params.get("EngineVersion")
        self.TemplateId = params.get("TemplateId")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParamTemplateResponse(AbstractModel):
    """CreateParamTemplate response structure.

    """

    def __init__(self):
        """
        :param TemplateId: Parameter template ID.\n        :type TemplateId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateRoInstanceIpRequest(AbstractModel):
    """CreateRoInstanceIp request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Read-only instance ID in the format of "cdbro-3i70uj0k". Its value is the same as the read-only instance ID in the TencentDB Console.\n        :type InstanceId: str\n        :param UniqSubnetId: Subnet descriptor, such as "subnet-1typ0s7d".\n        :type UniqSubnetId: str\n        :param UniqVpcId: VPC descriptor, such as "vpc-a23yt67j". If this field is passed in, `UniqSubnetId` will be required.\n        :type UniqVpcId: str\n        """
        self.InstanceId = None
        self.UniqSubnetId = None
        self.UniqVpcId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoInstanceIpResponse(AbstractModel):
    """CreateRoInstanceIp response structure.

    """

    def __init__(self):
        """
        :param RoVpcId: VPC ID of the read-only instance.\n        :type RoVpcId: int\n        :param RoSubnetId: Subnet ID of the read-only instance.\n        :type RoSubnetId: int\n        :param RoVip: Private IP address of the read-only instance.\n        :type RoVip: str\n        :param RoVport: Private port number of the read-only instance.\n        :type RoVport: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RoVpcId = None
        self.RoSubnetId = None
        self.RoVip = None
        self.RoVport = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoVpcId = params.get("RoVpcId")
        self.RoSubnetId = params.get("RoSubnetId")
        self.RoVip = params.get("RoVip")
        self.RoVport = params.get("RoVport")
        self.RequestId = params.get("RequestId")


class DBSwitchInfo(AbstractModel):
    """TencentDB instance switch records

    """

    def __init__(self):
        """
        :param SwitchTime: Switch time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-09-03 01:34:31\n        :type SwitchTime: str\n        :param SwitchType: Switch type. Value range: TRANSFER (data migration), MASTER2SLAVE (primary/secondary switch), RECOVERY (primary/secondary recovery)\n        :type SwitchType: str\n        """
        self.SwitchTime = None
        self.SwitchType = None


    def _deserialize(self, params):
        self.SwitchTime = params.get("SwitchTime")
        self.SwitchType = params.get("SwitchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseName(AbstractModel):
    """Name of a database

    """

    def __init__(self):
        """
        :param DatabaseName: Name of a database\n        :type DatabaseName: str\n        """
        self.DatabaseName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    """Database permission

    """

    def __init__(self):
        """
        :param Privileges: Permission information\n        :type Privileges: list of str\n        :param Database: Database name\n        :type Database: str\n        """
        self.Privileges = None
        self.Database = None


    def _deserialize(self, params):
        self.Privileges = params.get("Privileges")
        self.Database = params.get("Database")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasesWithCharacterLists(AbstractModel):
    """Database name and character set

    """

    def __init__(self):
        """
        :param DatabaseName: Database name\n        :type DatabaseName: str\n        :param CharacterSet: Character set\n        :type CharacterSet: str\n        """
        self.DatabaseName = None
        self.CharacterSet = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.CharacterSet = params.get("CharacterSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsRequest(AbstractModel):
    """DeleteAccounts request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Accounts: TencentDB account.\n        :type Accounts: list of Account\n        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsResponse(AbstractModel):
    """DeleteAccounts response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param BackupId: Backup task ID, which is the task ID returned by the [TencentDB instance backup creating API](https://intl.cloud.tencent.com/document/api/236/15844?from_cn_redirect=1).\n        :type BackupId: int\n        """
        self.InstanceId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupResponse(AbstractModel):
    """DeleteBackup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeployGroupsRequest(AbstractModel):
    """DeleteDeployGroups request structure.

    """

    def __init__(self):
        """
        :param DeployGroupIds: List of IDs of placement groups to be deleted.\n        :type DeployGroupIds: list of str\n        """
        self.DeployGroupIds = None


    def _deserialize(self, params):
        self.DeployGroupIds = params.get("DeployGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeployGroupsResponse(AbstractModel):
    """DeleteDeployGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Parameter template ID.\n        :type TemplateId: int\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParamTemplateResponse(AbstractModel):
    """DeleteParamTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTimeWindowRequest(AbstractModel):
    """DeleteTimeWindow request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimeWindowResponse(AbstractModel):
    """DeleteTimeWindow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeployGroupInfo(AbstractModel):
    """Placement group information

    """

    def __init__(self):
        """
        :param DeployGroupId: ID of a placement group.\n        :type DeployGroupId: str\n        :param DeployGroupName: Name of a placement group.\n        :type DeployGroupName: str\n        :param CreateTime: Creation time.\n        :type CreateTime: str\n        :param Quota: Instance quota of placement group, indicating the maximum number of instances that can be placed in one placement group.\n        :type Quota: int\n        :param Affinity: Affinity policy of placement group. Currently, only policy 1 is supported, indicating to distribute instances across physical machines.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Affinity: str\n        :param LimitNum: Upper limit of instances in one placement group on one physical machine as defined in affinity policy 1 of placement group.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LimitNum: int\n        :param Description: Placement group details.\n        :type Description: str\n        :param DevClass: Physical model attribute of placement group.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DevClass: str\n        """
        self.DeployGroupId = None
        self.DeployGroupName = None
        self.CreateTime = None
        self.Quota = None
        self.Affinity = None
        self.LimitNum = None
        self.Description = None
        self.DevClass = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.DeployGroupName = params.get("DeployGroupName")
        self.CreateTime = params.get("CreateTime")
        self.Quota = params.get("Quota")
        self.Affinity = params.get("Affinity")
        self.LimitNum = params.get("LimitNum")
        self.Description = params.get("Description")
        self.DevClass = params.get("DevClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param User: Database user account.\n        :type User: str\n        :param Host: Database account domain name.\n        :type Host: str\n        """
        self.InstanceId = None
        self.User = None
        self.Host = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.User = params.get("User")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param GlobalPrivileges: Array of global permissions.\n        :type GlobalPrivileges: list of str\n        :param DatabasePrivileges: Array of database permissions.\n        :type DatabasePrivileges: list of DatabasePrivilege\n        :param TablePrivileges: Array of table permissions in the database.\n        :type TablePrivileges: list of TablePrivilege\n        :param ColumnPrivileges: Array of column permissions in the table.\n        :type ColumnPrivileges: list of ColumnPrivilege\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self.DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self.DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self.TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self.TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self.ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self.ColumnPrivileges.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Offset: Record offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of results to be returned for a single request. Value range: 1-100. Default value: 20.\n        :type Limit: int\n        :param AccountRegexp: Regular expression for matching account names, which complies with the rules at MySQL official website.\n        :type AccountRegexp: str\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.AccountRegexp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.AccountRegexp = params.get("AccountRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible accounts.\n        :type TotalCount: int\n        :param Items: Details of eligible accounts.\n        :type Items: list of AccountInfo\n        :param MaxUserConnections: The maximum number of instance connections (set by the MySQL parameter `max_connections`)\n        :type MaxUserConnections: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.MaxUserConnections = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = AccountInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.MaxUserConnections = params.get("MaxUserConnections")
        self.RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID.\n        :type AsyncRequestId: str\n        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo response structure.

    """

    def __init__(self):
        """
        :param Status: Task execution result. Valid values: INITIAL, RUNNING, SUCCESS, FAILED, KILLED, REMOVED, PAUSED.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Status: str\n        :param Info: Task execution information.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Info: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig response structure.

    """

    def __init__(self):
        """
        :param StartTimeMin: Earliest start time point of automatic backup, such as 2 (for 2:00 AM). (This field has been disused. You are recommended to use the `BackupTimeWindow` field)\n        :type StartTimeMin: int\n        :param StartTimeMax: Latest start time point of automatic backup, such as 6 (for 6:00 AM). (This field has been disused. You are recommended to use the `BackupTimeWindow` field)\n        :type StartTimeMax: int\n        :param BackupExpireDays: Backup file retention period in days.\n        :type BackupExpireDays: int\n        :param BackupMethod: Backup mode. Value range: physical, logical\n        :type BackupMethod: str\n        :param BinlogExpireDays: Binlog file retention period in days.\n        :type BinlogExpireDays: int\n        :param BackupTimeWindow: Time window for automatic instance backup.\n        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.StartTimeMin = None
        self.StartTimeMax = None
        self.BackupExpireDays = None
        self.BackupMethod = None
        self.BinlogExpireDays = None
        self.BackupTimeWindow = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTimeMin = params.get("StartTimeMin")
        self.StartTimeMax = params.get("StartTimeMax")
        self.BackupExpireDays = params.get("BackupExpireDays")
        self.BackupMethod = params.get("BackupMethod")
        self.BinlogExpireDays = params.get("BinlogExpireDays")
        if params.get("BackupTimeWindow") is not None:
            self.BackupTimeWindow = CommonTimeWindow()
            self.BackupTimeWindow._deserialize(params.get("BackupTimeWindow"))
        self.RequestId = params.get("RequestId")


class DescribeBackupDatabasesRequest(AbstractModel):
    """DescribeBackupDatabases request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param StartTime: Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-07-12 10:29:20.\n        :type StartTime: str\n        :param SearchDatabase: Prefix of the database to be queried.\n        :type SearchDatabase: str\n        :param Offset: Pagination offset.\n        :type Offset: int\n        :param Limit: Number of entries per page. Value range: 1-2,000.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.StartTime = None
        self.SearchDatabase = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.SearchDatabase = params.get("SearchDatabase")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDatabasesResponse(AbstractModel):
    """DescribeBackupDatabases response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of the returned data entries.\n        :type TotalCount: int\n        :param Items: Array of eligible databases.\n        :type Items: list of DatabaseName\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DatabaseName()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupOverviewRequest(AbstractModel):
    """DescribeBackupOverview request structure.

    """

    def __init__(self):
        """
        :param Product: TencentDB product type to be queried. Currently, only `mysql` is supported.\n        :type Product: str\n        """
        self.Product = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupOverviewResponse(AbstractModel):
    """DescribeBackupOverview response structure.

    """

    def __init__(self):
        """
        :param BackupCount: Total number of backups of a user in the current region (including data backups and log backups).\n        :type BackupCount: int\n        :param BackupVolume: Total capacity of backups of a user in the current region.\n        :type BackupVolume: int\n        :param BillingVolume: Paid capacity of backups of a user in the current region, i.e., capacity that exceeds the free tier.\n        :type BillingVolume: int\n        :param FreeVolume: Backup capacity in the free tier of a user in the current region.\n        :type FreeVolume: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.BackupCount = None
        self.BackupVolume = None
        self.BillingVolume = None
        self.FreeVolume = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupCount = params.get("BackupCount")
        self.BackupVolume = params.get("BackupVolume")
        self.BillingVolume = params.get("BillingVolume")
        self.FreeVolume = params.get("FreeVolume")
        self.RequestId = params.get("RequestId")


class DescribeBackupSummariesRequest(AbstractModel):
    """DescribeBackupSummaries request structure.

    """

    def __init__(self):
        """
        :param Product: TencentDB product type to be queried. Currently, only `mysql` is supported.\n        :type Product: str\n        :param Offset: Pagination offset.\n        :type Offset: int\n        :param Limit: Paginated query limit. Default value: 20.\n        :type Limit: int\n        :param OrderBy: Sorting criterion. Valid values: BackupVolume (backup capacity), DataBackupVolume (data backup capacity), BinlogBackupVolume (log backup capacity), AutoBackupVolume (automatic backup capacity), ManualBackupVolume (manual backup capacity).\n        :type OrderBy: str\n        :param OrderDirection: Sorting order. Valid values: ASC (ascending), DESC (descending).\n        :type OrderDirection: str\n        """
        self.Product = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupSummariesResponse(AbstractModel):
    """DescribeBackupSummaries response structure.

    """

    def __init__(self):
        """
        :param Items: Statistical items of instance backup.\n        :type Items: list of BackupSummaryItem\n        :param TotalCount: Total number of instance backups.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Items = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = BackupSummaryItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBackupTablesRequest(AbstractModel):
    """DescribeBackupTables request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param StartTime: Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-07-12 10:29:20.\n        :type StartTime: str\n        :param DatabaseName: Specified database name.\n        :type DatabaseName: str\n        :param SearchTable: Prefix of the table to be queried.\n        :type SearchTable: str\n        :param Offset: Pagination offset.\n        :type Offset: int\n        :param Limit: Number of entries per page. Value range: 1-2,000.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.StartTime = None
        self.DatabaseName = None
        self.SearchTable = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.DatabaseName = params.get("DatabaseName")
        self.SearchTable = params.get("SearchTable")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupTablesResponse(AbstractModel):
    """DescribeBackupTables response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of the returned data entries.\n        :type TotalCount: int\n        :param Items: Array of eligible tables.\n        :type Items: list of TableName\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = TableName()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Offset: Offset. Minimum value: 0.\n        :type Offset: int\n        :param Limit: Number of entries per page. Value range: 1-100. Default value: 20.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param Items: Details of eligible backups.\n        :type Items: list of BackupInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = BackupInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBinlogBackupOverviewRequest(AbstractModel):
    """DescribeBinlogBackupOverview request structure.

    """

    def __init__(self):
        """
        :param Product: TencentDB product type to be queried. Currently, only `mysql` is supported.\n        :type Product: str\n        """
        self.Product = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogBackupOverviewResponse(AbstractModel):
    """DescribeBinlogBackupOverview response structure.

    """

    def __init__(self):
        """
        :param BinlogBackupVolume: Total capacity of log backups in bytes.\n        :type BinlogBackupVolume: int\n        :param BinlogBackupCount: Total number of log backups.\n        :type BinlogBackupCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.BinlogBackupVolume = None
        self.BinlogBackupCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BinlogBackupVolume = params.get("BinlogBackupVolume")
        self.BinlogBackupCount = params.get("BinlogBackupCount")
        self.RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Offset: Offset. Minimum value: 0.\n        :type Offset: int\n        :param Limit: Number of entries per page. Value range: 1-100. Default value: 20.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible log files.\n        :type TotalCount: int\n        :param Items: Number of eligible binlog files.\n        :type Items: list of BinlogInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = BinlogInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloneListRequest(AbstractModel):
    """DescribeCloneList request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the original instance. This parameter is used to query the clone task list of a specific original instance.\n        :type InstanceId: str\n        :param Offset: Paginated query offset. Default value: `0`.\n        :type Offset: int\n        :param Limit: Number of results per page. Default value: `20`.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloneListResponse(AbstractModel):
    """DescribeCloneList response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of results which meet the conditions\n        :type TotalCount: int\n        :param Items: Clone task list\n        :type Items: list of CloneItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CloneItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBImportRecordsRequest(AbstractModel):
    """DescribeDBImportRecords request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param StartTime: Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-01-01 00:00:01.\n        :type StartTime: str\n        :param EndTime: End time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-01-01 23:59:59.\n        :type EndTime: str\n        :param Offset: Pagination parameter indicating the offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Pagination parameter indicating the number of results to be returned for a single request. Value range: 1-100. Default value: 20.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBImportRecordsResponse(AbstractModel):
    """DescribeDBImportRecords response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible import task operation logs.\n        :type TotalCount: int\n        :param Items: List of import operation records.\n        :type Items: list of ImportRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ImportRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceCharsetRequest(AbstractModel):
    """DescribeDBInstanceCharset request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceCharsetResponse(AbstractModel):
    """DescribeDBInstanceCharset response structure.

    """

    def __init__(self):
        """
        :param Charset: Default character set of the instance, such as "latin1" and "utf8".\n        :type Charset: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Charset = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Charset = params.get("Charset")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceConfigRequest(AbstractModel):
    """DescribeDBInstanceConfig request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceConfigResponse(AbstractModel):
    """DescribeDBInstanceConfig response structure.

    """

    def __init__(self):
        """
        :param ProtectMode: Data protection mode of the primary instance. Value range: 0 (async replication), 1 (semi-sync replication), 2 (strong sync replication).\n        :type ProtectMode: int\n        :param DeployMode: Master instance deployment mode. Value range: 0 (single-AZ), 1 (multi-AZ)\n        :type DeployMode: int\n        :param Zone: Instance AZ information in the format of "ap-shanghai-1".\n        :type Zone: str\n        :param SlaveConfig: Configurations of the replica node
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type SlaveConfig: :class:`tencentcloud.cdb.v20170320.models.SlaveConfig`\n        :param BackupConfig: Configurations of the second replica node of a strong-sync instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type BackupConfig: :class:`tencentcloud.cdb.v20170320.models.BackupConfig`\n        :param Switched: This parameter is only available for multi-AZ instances. It indicates whether the source AZ is the same as the one specified upon purchase. `true`: not the same, `false`: the same.\n        :type Switched: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ProtectMode = None
        self.DeployMode = None
        self.Zone = None
        self.SlaveConfig = None
        self.BackupConfig = None
        self.Switched = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.Zone = params.get("Zone")
        if params.get("SlaveConfig") is not None:
            self.SlaveConfig = SlaveConfig()
            self.SlaveConfig._deserialize(params.get("SlaveConfig"))
        if params.get("BackupConfig") is not None:
            self.BackupConfig = BackupConfig()
            self.BackupConfig._deserialize(params.get("BackupConfig"))
        self.Switched = params.get("Switched")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceGTIDRequest(AbstractModel):
    """DescribeDBInstanceGTID request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceGTIDResponse(AbstractModel):
    """DescribeDBInstanceGTID response structure.

    """

    def __init__(self):
        """
        :param IsGTIDOpen: GTID enablement flag. Value range: 0 (not enabled), 1 (enabled).\n        :type IsGTIDOpen: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.IsGTIDOpen = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsGTIDOpen = params.get("IsGTIDOpen")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceInfoRequest(AbstractModel):
    """DescribeDBInstanceInfo request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceInfoResponse(AbstractModel):
    """DescribeDBInstanceInfo response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param InstanceName: Instance name.\n        :type InstanceName: str\n        :param Encryption: Whether encryption is enabled. YES: enabled, NO: not enabled.\n        :type Encryption: str\n        :param KeyId: Encryption key ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyId: str\n        :param KeyRegion: Key region.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyRegion: str\n        :param DefaultKmsRegion: The default region of the KMS service currently used by the TencentDB backend service.
Note: this field may return `null`, indicating that no valid value can be found.\n        :type DefaultKmsRegion: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.Encryption = None
        self.KeyId = None
        self.KeyRegion = None
        self.DefaultKmsRegion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Encryption = params.get("Encryption")
        self.KeyId = params.get("KeyId")
        self.KeyRegion = params.get("KeyRegion")
        self.DefaultKmsRegion = params.get("DefaultKmsRegion")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceRebootTimeRequest(AbstractModel):
    """DescribeDBInstanceRebootTime request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceIds: list of str\n        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceRebootTimeResponse(AbstractModel):
    """DescribeDBInstanceRebootTime response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param Items: Returned parameter information.\n        :type Items: list of InstanceRebootTime\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceRebootTime()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances request structure.

    """

    def __init__(self):
        """
        :param ProjectId: Project ID. You can use the [project list querying API](https://intl.cloud.tencent.com/document/product/378/4400?from_cn_redirect=1) to query the project ID.\n        :type ProjectId: int\n        :param InstanceTypes: Instance type. Value range: 1 (primary), 2 (disaster recovery), 3 (read-only).\n        :type InstanceTypes: list of int non-negative\n        :param Vips: Private IP address of the instance.\n        :type Vips: list of str\n        :param Status: Instance status. Value range: <br>0 - creating <br>1 - running <br>4 - isolating <br>5 - isolated (the instance can be restored and started in the recycle bin)\n        :type Status: list of int non-negative\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of results to be returned for a single request. Default value: 20. Maximum value: 2,000.\n        :type Limit: int\n        :param SecurityGroupId: Security group ID. When it is used as a filter, the `WithSecurityGroup` parameter should be set to 1.\n        :type SecurityGroupId: str\n        :param PayTypes: Billing method. Value range: 0 (monthly subscribed), 1 (hourly).\n        :type PayTypes: list of int non-negative\n        :param InstanceNames: Instance name.\n        :type InstanceNames: list of str\n        :param TaskStatus: Instance task status. Valid values: <br>0 - no task <br>1 - upgrading <br>2 - importing data <br>3 - enabling secondary instance access <br>4 - enabling public network access <br>5 - batch operation in progress <br>6 - rolling back <br>7 - disabling public network access <br>8 - modifying password <br>9 - renaming instance <br>10 - restarting <br>12 - migrating self-built database <br>13 - dropping tables <br>14 - Disaster recovery instance creating sync task <br>15 - waiting for switch <br>16 - switching <br>17 - upgrade and switch completed <br>19 - parameter settings to be executed\n        :type TaskStatus: list of int non-negative\n        :param EngineVersions: Version of the instance database engine. Value range: 5.1, 5.5, 5.6, 5.7.\n        :type EngineVersions: list of str\n        :param VpcIds: VPC ID.\n        :type VpcIds: list of int non-negative\n        :param ZoneIds: AZ ID.\n        :type ZoneIds: list of int non-negative\n        :param SubnetIds: Subnet ID.\n        :type SubnetIds: list of int non-negative\n        :param CdbErrors: Lock flag.\n        :type CdbErrors: list of int\n        :param OrderBy: Sort by field of the returned result set. Currently, supported values include "InstanceId", "InstanceName", "CreateTime", and "DeadlineTime".\n        :type OrderBy: str\n        :param OrderDirection: Sorting method of the returned result set. Currently, "ASC" or "DESC" is supported.\n        :type OrderDirection: str\n        :param WithSecurityGroup: Whether security group ID is used as a filter\n        :type WithSecurityGroup: int\n        :param WithExCluster: Whether dedicated cluster details are included. Value range: 0 (not included), 1 (included)\n        :type WithExCluster: int\n        :param ExClusterId: Exclusive cluster ID.\n        :type ExClusterId: str\n        :param InstanceIds: Instance ID.\n        :type InstanceIds: list of str\n        :param InitFlag: Initialization flag. Value range: 0 (not initialized), 1 (initialized).\n        :type InitFlag: int\n        :param WithDr: Whether instances corresponding to the disaster recovery relationship are included. Valid values: 0 (not included), 1 (included). Default value: 1. If a primary instance is pulled, the data of the disaster recovery relationship will be in the `DrInfo` field. If a disaster recovery instance is pulled, the data of the disaster recovery relationship will be in the `MasterInfo` field. The disaster recovery relationship contains only partial basic data. To get the detailed data, you need to call an API to pull it.\n        :type WithDr: int\n        :param WithRo: Whether read-only instances are included. Valid values: 0 (not included), 1 (included). Default value: 1.\n        :type WithRo: int\n        :param WithMaster: Whether primary instances are included. Valid values: 0 (not included), 1 (included). Default value: 1.\n        :type WithMaster: int\n        :param DeployGroupIds: Placement group ID list.\n        :type DeployGroupIds: list of str\n        :param TagKeysForSearch: Whether to use the tag key as a filter condition\n        :type TagKeysForSearch: list of str\n        """
        self.ProjectId = None
        self.InstanceTypes = None
        self.Vips = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.SecurityGroupId = None
        self.PayTypes = None
        self.InstanceNames = None
        self.TaskStatus = None
        self.EngineVersions = None
        self.VpcIds = None
        self.ZoneIds = None
        self.SubnetIds = None
        self.CdbErrors = None
        self.OrderBy = None
        self.OrderDirection = None
        self.WithSecurityGroup = None
        self.WithExCluster = None
        self.ExClusterId = None
        self.InstanceIds = None
        self.InitFlag = None
        self.WithDr = None
        self.WithRo = None
        self.WithMaster = None
        self.DeployGroupIds = None
        self.TagKeysForSearch = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.InstanceTypes = params.get("InstanceTypes")
        self.Vips = params.get("Vips")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.PayTypes = params.get("PayTypes")
        self.InstanceNames = params.get("InstanceNames")
        self.TaskStatus = params.get("TaskStatus")
        self.EngineVersions = params.get("EngineVersions")
        self.VpcIds = params.get("VpcIds")
        self.ZoneIds = params.get("ZoneIds")
        self.SubnetIds = params.get("SubnetIds")
        self.CdbErrors = params.get("CdbErrors")
        self.OrderBy = params.get("OrderBy")
        self.OrderDirection = params.get("OrderDirection")
        self.WithSecurityGroup = params.get("WithSecurityGroup")
        self.WithExCluster = params.get("WithExCluster")
        self.ExClusterId = params.get("ExClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.InitFlag = params.get("InitFlag")
        self.WithDr = params.get("WithDr")
        self.WithRo = params.get("WithRo")
        self.WithMaster = params.get("WithMaster")
        self.DeployGroupIds = params.get("DeployGroupIds")
        self.TagKeysForSearch = params.get("TagKeysForSearch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param Items: Instance details.\n        :type Items: list of InstanceInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param ForReadonlyInstance: This parameter takes effect only when the ID of read-only replica is passed in. If this parameter is set to `False` or left empty, the security groups bound with the RO group of the read-only replica will be queried. If this parameter is set to `True`, the security groups bound with the read-only replica itself will be queried.\n        :type ForReadonlyInstance: bool\n        """
        self.InstanceId = None
        self.ForReadonlyInstance = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Groups: Security group details.\n        :type Groups: list of SecurityGroup\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSwitchRecordsRequest(AbstractModel):
    """DescribeDBSwitchRecords request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Offset: Pagination offset.\n        :type Offset: int\n        :param Limit: Number of entries per page. Value range: 1-2,000. Default value: 50.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSwitchRecordsResponse(AbstractModel):
    """DescribeDBSwitchRecords response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of instance switches.\n        :type TotalCount: int\n        :param Items: Details of instance switches.\n        :type Items: list of DBSwitchInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DBSwitchInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBZoneConfigRequest(AbstractModel):
    """DescribeDBZoneConfig request structure.

    """


class DescribeDBZoneConfigResponse(AbstractModel):
    """DescribeDBZoneConfig response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of configurations in purchasable regions\n        :type TotalCount: int\n        :param Items: Details of configurations in purchasable regions\n        :type Items: list of RegionSellConf\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RegionSellConf()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDataBackupOverviewRequest(AbstractModel):
    """DescribeDataBackupOverview request structure.

    """

    def __init__(self):
        """
        :param Product: TencentDB product type to be queried. Currently, only `mysql` is supported.\n        :type Product: str\n        """
        self.Product = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataBackupOverviewResponse(AbstractModel):
    """DescribeDataBackupOverview response structure.

    """

    def __init__(self):
        """
        :param DataBackupVolume: Total capacity of data backups in bytes in the current region (including automatic backups and manual backups).\n        :type DataBackupVolume: int\n        :param DataBackupCount: Total number of data backups in the current region.\n        :type DataBackupCount: int\n        :param AutoBackupVolume: Total capacity of automatic backups in the current region.\n        :type AutoBackupVolume: int\n        :param AutoBackupCount: Total number of automatic backups in the current region.\n        :type AutoBackupCount: int\n        :param ManualBackupVolume: Total capacity of manual backups in the current region.\n        :type ManualBackupVolume: int\n        :param ManualBackupCount: Total number of manual backups in the current region.\n        :type ManualBackupCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DataBackupVolume = None
        self.DataBackupCount = None
        self.AutoBackupVolume = None
        self.AutoBackupCount = None
        self.ManualBackupVolume = None
        self.ManualBackupCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataBackupVolume = params.get("DataBackupVolume")
        self.DataBackupCount = params.get("DataBackupCount")
        self.AutoBackupVolume = params.get("AutoBackupVolume")
        self.AutoBackupCount = params.get("AutoBackupCount")
        self.ManualBackupVolume = params.get("ManualBackupVolume")
        self.ManualBackupCount = params.get("ManualBackupCount")
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Offset: Offset. Minimum value: 0.\n        :type Offset: int\n        :param Limit: Number of results to be returned for a single request. Value range: 1-100. Maximum value: 20.\n        :type Limit: int\n        :param DatabaseRegexp: Regular expression for matching database names.\n        :type DatabaseRegexp: str\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.DatabaseRegexp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DatabaseRegexp = params.get("DatabaseRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param Items: Information of an instance.\n        :type Items: list of str\n        :param DatabaseList: Database name and character set\n        :type DatabaseList: list of DatabasesWithCharacterLists\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.DatabaseList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        if params.get("DatabaseList") is not None:
            self.DatabaseList = []
            for item in params.get("DatabaseList"):
                obj = DatabasesWithCharacterLists()
                obj._deserialize(item)
                self.DatabaseList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDefaultParamsRequest(AbstractModel):
    """DescribeDefaultParams request structure.

    """

    def __init__(self):
        """
        :param EngineVersion: MySQL version. Currently, the supported versions are ["5.1", "5.5", "5.6", "5.7"].\n        :type EngineVersion: str\n        """
        self.EngineVersion = None


    def _deserialize(self, params):
        self.EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultParamsResponse(AbstractModel):
    """DescribeDefaultParams response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of parameters\n        :type TotalCount: int\n        :param Items: Parameter details.\n        :type Items: list of ParameterDetail\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeployGroupListRequest(AbstractModel):
    """DescribeDeployGroupList request structure.

    """

    def __init__(self):
        """
        :param DeployGroupId: ID of a placement group.\n        :type DeployGroupId: str\n        :param DeployGroupName: Name of a placement group.\n        :type DeployGroupName: str\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.DeployGroupId = None
        self.DeployGroupName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.DeployGroupName = params.get("DeployGroupName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployGroupListResponse(AbstractModel):
    """DescribeDeployGroupList response structure.

    """

    def __init__(self):
        """
        :param Total: Number of eligible entries.\n        :type Total: int\n        :param Items: List of returned results.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Items: list of DeployGroupInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Total = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DeployGroupInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceMonitorInfoRequest(AbstractModel):
    """DescribeDeviceMonitorInfo request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Count: This parameter is used to return the monitoring data of Count 5-minute time periods on the day. Value range: 1-288. If this parameter is not passed in, all monitoring data in a 5-minute granularity on the day will be returned by default.\n        :type Count: int\n        """
        self.InstanceId = None
        self.Count = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceMonitorInfoResponse(AbstractModel):
    """DescribeDeviceMonitorInfo response structure.

    """

    def __init__(self):
        """
        :param Cpu: CPU monitoring data of the instance\n        :type Cpu: :class:`tencentcloud.cdb.v20170320.models.DeviceCpuInfo`\n        :param Mem: Memory monitoring data of the instance\n        :type Mem: :class:`tencentcloud.cdb.v20170320.models.DeviceMemInfo`\n        :param Net: Network monitoring data of the instance\n        :type Net: :class:`tencentcloud.cdb.v20170320.models.DeviceNetInfo`\n        :param Disk: Disk monitoring data of the instance\n        :type Disk: :class:`tencentcloud.cdb.v20170320.models.DeviceDiskInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Cpu = None
        self.Mem = None
        self.Net = None
        self.Disk = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cpu") is not None:
            self.Cpu = DeviceCpuInfo()
            self.Cpu._deserialize(params.get("Cpu"))
        if params.get("Mem") is not None:
            self.Mem = DeviceMemInfo()
            self.Mem._deserialize(params.get("Mem"))
        if params.get("Net") is not None:
            self.Net = DeviceNetInfo()
            self.Net._deserialize(params.get("Net"))
        if params.get("Disk") is not None:
            self.Disk = DeviceDiskInfo()
            self.Disk._deserialize(params.get("Disk"))
        self.RequestId = params.get("RequestId")


class DescribeErrorLogDataRequest(AbstractModel):
    """DescribeErrorLogData request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param StartTime: Start timestamp.\n        :type StartTime: int\n        :param EndTime: End timestamp.\n        :type EndTime: int\n        :param KeyWords: List of keywords to match. Up to 15 keywords are supported.\n        :type KeyWords: list of str\n        :param Limit: The number of results per page in paginated queries. Default value: 100. Maximum value: 400.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param InstType: This parameter is valid only for source or disaster recovery instances. Valid value: `slave`, which indicates pulling logs from the replica.\n        :type InstType: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.KeyWords = None
        self.Limit = None
        self.Offset = None
        self.InstType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.KeyWords = params.get("KeyWords")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InstType = params.get("InstType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorLogDataResponse(AbstractModel):
    """DescribeErrorLogData response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param Items: Returned result.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Items: list of ErrlogItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ErrlogItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        :param Offset: Pagination offset.\n        :type Offset: int\n        :param Limit: Number of entries per page.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible records.\n        :type TotalCount: int\n        :param Items: Parameter modification records.\n        :type Items: list of ParamRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParamRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of instance parameters.\n        :type TotalCount: int\n        :param Items: Parameter details.\n        :type Items: list of ParameterDetail\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    """DescribeParamTemplateInfo request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Parameter template ID.\n        :type TemplateId: int\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplateInfoResponse(AbstractModel):
    """DescribeParamTemplateInfo response structure.

    """

    def __init__(self):
        """
        :param TemplateId: Parameter template ID.\n        :type TemplateId: int\n        :param Name: Parameter template name.\n        :type Name: str\n        :param EngineVersion: Database engine version specified in the parameter template\n        :type EngineVersion: str\n        :param TotalCount: Number of parameters in the parameter template\n        :type TotalCount: int\n        :param Items: Parameter details\n        :type Items: list of ParameterDetail\n        :param Description: Parameter template description\n        :type Description: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TemplateId = None
        self.Name = None
        self.EngineVersion = None
        self.TotalCount = None
        self.Items = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.EngineVersion = params.get("EngineVersion")
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates request structure.

    """


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of parameter templates of the user.\n        :type TotalCount: int\n        :param Items: Parameter template details.\n        :type Items: list of ParamTemplateInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param ProjectId: Project ID.\n        :type ProjectId: int\n        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Groups: Security group details.\n        :type Groups: list of SecurityGroup\n        :param TotalCount: Number of security group rules\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Groups = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRoGroupsRequest(AbstractModel):
    """DescribeRoGroups request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `cdb-c1nl9rpv` or `cdb-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoGroupsResponse(AbstractModel):
    """DescribeRoGroups response structure.

    """

    def __init__(self):
        """
        :param RoGroups: RO group information array. An instance can be associated with multiple RO groups.\n        :type RoGroups: list of RoGroup\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RoGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RoGroups") is not None:
            self.RoGroups = []
            for item in params.get("RoGroups"):
                obj = RoGroup()
                obj._deserialize(item)
                self.RoGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoMinScaleRequest(AbstractModel):
    """DescribeRoMinScale request structure.

    """

    def __init__(self):
        """
        :param RoInstanceId: Read-only instance ID in the format of "cdbro-c1nl9rpv". Its value is the same as the instance ID in the TencentDB Console. This parameter and the `MasterInstanceId` parameter cannot both be empty.\n        :type RoInstanceId: str\n        :param MasterInstanceId: Primary instance ID in the format of "cdbro-c1nl9rpv". Its value is the same as the instance ID in the TencentDB Console. This parameter and the `RoInstanceId` parameter cannot both be empty. Note: when the parameters are passed in with `RoInstanceId`, the return value refers to the minimum specification to which a read-only instance can be upgraded; when the parameters are passed in with `MasterInstanceId` but without `RoInstanceId`, the return value refers to the minimum purchasable specification for a read-only instance.\n        :type MasterInstanceId: str\n        """
        self.RoInstanceId = None
        self.MasterInstanceId = None


    def _deserialize(self, params):
        self.RoInstanceId = params.get("RoInstanceId")
        self.MasterInstanceId = params.get("MasterInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoMinScaleResponse(AbstractModel):
    """DescribeRoMinScale response structure.

    """

    def __init__(self):
        """
        :param Memory: Memory size in MB.\n        :type Memory: int\n        :param Volume: Disk size in GB.\n        :type Volume: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Memory = None
        self.Volume = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.RequestId = params.get("RequestId")


class DescribeRollbackRangeTimeRequest(AbstractModel):
    """DescribeRollbackRangeTime request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance ID list. An instance ID is in the format of cdb-c1nl9rpv, which is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceIds: list of str\n        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackRangeTimeResponse(AbstractModel):
    """DescribeRollbackRangeTime response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param Items: Returned parameter information.\n        :type Items: list of InstanceRollbackRangeTime\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceRollbackRangeTime()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackTaskDetailRequest(AbstractModel):
    """DescribeRollbackTaskDetail request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is the same as the instance ID displayed in the TencentDB Console. You can use the [DescribeDBInstances API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID.\n        :type InstanceId: str\n        :param AsyncRequestId: Async task ID.\n        :type AsyncRequestId: str\n        :param Limit: Pagination parameter, i.e., the number of entries to be returned for a single request. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        """
        self.InstanceId = None
        self.AsyncRequestId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTaskDetailResponse(AbstractModel):
    """DescribeRollbackTaskDetail response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param Items: Rollback task details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Items: list of RollbackTask\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RollbackTask()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogDataRequest(AbstractModel):
    """DescribeSlowLogData request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param StartTime: Start timestamp.\n        :type StartTime: int\n        :param EndTime: End timestamp.\n        :type EndTime: int\n        :param UserHosts: Client `Host` list.\n        :type UserHosts: list of str\n        :param UserNames: Client username list.\n        :type UserNames: list of str\n        :param DataBases: Accessed database list.\n        :type DataBases: list of str\n        :param SortBy: Sort by field. Valid values: Timestamp, QueryTime, LockTime, RowsExamined, RowsSent.\n        :type SortBy: str\n        :param OrderBy: Sorting order. Valid values: ASC (ascending), DESC (descending).\n        :type OrderBy: str\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: The number of results per page in paginated queries. Default value: 100. Maximum value: 400.\n        :type Limit: int\n        :param InstType: This parameter is valid only for source or disaster recovery instances. Valid value: `slave`, which indicates pulling logs from the replica.\n        :type InstType: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.UserHosts = None
        self.UserNames = None
        self.DataBases = None
        self.SortBy = None
        self.OrderBy = None
        self.Offset = None
        self.Limit = None
        self.InstType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserHosts = params.get("UserHosts")
        self.UserNames = params.get("UserNames")
        self.DataBases = params.get("DataBases")
        self.SortBy = params.get("SortBy")
        self.OrderBy = params.get("OrderBy")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstType = params.get("InstType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogDataResponse(AbstractModel):
    """DescribeSlowLogData response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param Items: Queried results.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Items: list of SlowLogItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SlowLogItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Offset: Offset. Minimum value: 0.\n        :type Offset: int\n        :param Limit: Number of entries per page. Value range: 1-100. Default value: 20.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogsResponse(AbstractModel):
    """DescribeSlowLogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible slow logs.\n        :type TotalCount: int\n        :param Items: Details of eligible slow logs.\n        :type Items: list of SlowLogInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SlowLogInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSupportedPrivilegesRequest(AbstractModel):
    """DescribeSupportedPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupportedPrivilegesResponse(AbstractModel):
    """DescribeSupportedPrivileges response structure.

    """

    def __init__(self):
        """
        :param GlobalSupportedPrivileges: Global permissions supported by the instance\n        :type GlobalSupportedPrivileges: list of str\n        :param DatabaseSupportedPrivileges: Database permissions supported by the instance.\n        :type DatabaseSupportedPrivileges: list of str\n        :param TableSupportedPrivileges: Table permissions supported by the instance.\n        :type TableSupportedPrivileges: list of str\n        :param ColumnSupportedPrivileges: Column permissions supported by the instance.\n        :type ColumnSupportedPrivileges: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GlobalSupportedPrivileges = None
        self.DatabaseSupportedPrivileges = None
        self.TableSupportedPrivileges = None
        self.ColumnSupportedPrivileges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GlobalSupportedPrivileges = params.get("GlobalSupportedPrivileges")
        self.DatabaseSupportedPrivileges = params.get("DatabaseSupportedPrivileges")
        self.TableSupportedPrivileges = params.get("TableSupportedPrivileges")
        self.ColumnSupportedPrivileges = params.get("ColumnSupportedPrivileges")
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Database: Database name.\n        :type Database: str\n        :param Offset: Record offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of results to be returned for a single request. Default value: 20. Maximum value: 2,000.\n        :type Limit: int\n        :param TableRegexp: Regular expression for matching table names, which complies with the rules at MySQL's official website\n        :type TableRegexp: str\n        """
        self.InstanceId = None
        self.Database = None
        self.Offset = None
        self.Limit = None
        self.TableRegexp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Database = params.get("Database")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TableRegexp = params.get("TableRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible tables.\n        :type TotalCount: int\n        :param Items: Information of a table.\n        :type Items: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeTagsOfInstanceIdsRequest(AbstractModel):
    """DescribeTagsOfInstanceIds request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: List of instances.\n        :type InstanceIds: list of str\n        :param Offset: Pagination offset.\n        :type Offset: int\n        :param Limit: Number of entries per page.\n        :type Limit: int\n        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsOfInstanceIdsResponse(AbstractModel):
    """DescribeTagsOfInstanceIds response structure.

    """

    def __init__(self):
        """
        :param Offset: Pagination offset.\n        :type Offset: int\n        :param Limit: Number of entries per page.\n        :type Limit: int\n        :param Rows: Instance tag information.\n        :type Rows: list of TagsInfoOfInstance\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfInstance()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        :param AsyncRequestId: ID of an async task request, i.e., `AsyncRequestId` returned by relevant TencentDB operations.\n        :type AsyncRequestId: str\n        :param TaskTypes: Task type. If no value is passed in, all task types will be queried. Valid values:
1 - rolling back a database;
2 - performing an SQL operation;
3 - importing data;
5 - setting a parameter;
6 - initializing a TencentDB instance;
7 - restarting a TencentDB instance;
8 - enabling GTID of a TencentDB instance;
9 - upgrading a read-only instance;
10 - rolling back databases in batches;
11 - upgrading a primary instance;
12 - deleting a TencentDB table;
13 - promoting a disaster recovery instance.\n        :type TaskTypes: list of int\n        :param TaskStatus: Task status. If no value is passed in, all task statuses will be queried. Valid values:
-1 - undefined;
0 - initializing;
1 - running;
2 - succeeded;
3 - failed;
4 - terminated;
5 - deleted;
6 - paused.\n        :type TaskStatus: list of int\n        :param StartTimeBegin: Start time of the first task in the format of yyyy-MM-dd HH:mm:ss, such as 2017-12-31 10:40:01. It is used for queries by time range.\n        :type StartTimeBegin: str\n        :param StartTimeEnd: End time of the last task in the format of yyyy-MM-dd HH:mm:ss, such as 2017-12-31 10:40:01. It is used for queries by time range.\n        :type StartTimeEnd: str\n        :param Offset: Record offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of results to be returned for a single request. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
        self.InstanceId = None
        self.AsyncRequestId = None
        self.TaskTypes = None
        self.TaskStatus = None
        self.StartTimeBegin = None
        self.StartTimeEnd = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.TaskTypes = params.get("TaskTypes")
        self.TaskStatus = params.get("TaskStatus")
        self.StartTimeBegin = params.get("StartTimeBegin")
        self.StartTimeEnd = params.get("StartTimeEnd")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param Items: Information of an instance task.\n        :type Items: list of TaskDetail\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = TaskDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimeWindowRequest(AbstractModel):
    """DescribeTimeWindow request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimeWindowResponse(AbstractModel):
    """DescribeTimeWindow response structure.

    """

    def __init__(self):
        """
        :param Monday: List of maintenance time windows on Monday.\n        :type Monday: list of str\n        :param Tuesday: List of maintenance time windows on Tuesday.\n        :type Tuesday: list of str\n        :param Wednesday: List of maintenance time windows on Wednesday.\n        :type Wednesday: list of str\n        :param Thursday: List of maintenance time windows on Thursday.\n        :type Thursday: list of str\n        :param Friday: List of maintenance time windows on Friday.\n        :type Friday: list of str\n        :param Saturday: List of maintenance time windows on Saturday.\n        :type Saturday: list of str\n        :param Sunday: List of maintenance time windows on Sunday.\n        :type Sunday: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.Saturday = None
        self.Sunday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Monday = params.get("Monday")
        self.Tuesday = params.get("Tuesday")
        self.Wednesday = params.get("Wednesday")
        self.Thursday = params.get("Thursday")
        self.Friday = params.get("Friday")
        self.Saturday = params.get("Saturday")
        self.Sunday = params.get("Sunday")
        self.RequestId = params.get("RequestId")


class DescribeUploadedFilesRequest(AbstractModel):
    """DescribeUploadedFiles request structure.

    """

    def __init__(self):
        """
        :param Path: File path. `OwnerUin` information of the root account should be entered in this field.\n        :type Path: str\n        :param Offset: Record offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of results to be returned for a single request. Default value: 20.\n        :type Limit: int\n        """
        self.Path = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadedFilesResponse(AbstractModel):
    """DescribeUploadedFiles response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible SQL files.\n        :type TotalCount: int\n        :param Items: List of returned SQL files.\n        :type Items: list of SqlFileInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SqlFileInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceCpuInfo(AbstractModel):
    """CPU load

    """

    def __init__(self):
        """
        :param Rate: Average instance CPU utilization\n        :type Rate: list of DeviceCpuRateInfo\n        :param Load: CPU monitoring data of the instance\n        :type Load: list of int\n        """
        self.Rate = None
        self.Load = None


    def _deserialize(self, params):
        if params.get("Rate") is not None:
            self.Rate = []
            for item in params.get("Rate"):
                obj = DeviceCpuRateInfo()
                obj._deserialize(item)
                self.Rate.append(obj)
        self.Load = params.get("Load")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceCpuRateInfo(AbstractModel):
    """Average instance CPU utilization

    """

    def __init__(self):
        """
        :param CpuCore: CPU core number\n        :type CpuCore: int\n        :param Rate: CPU utilization\n        :type Rate: list of int\n        """
        self.CpuCore = None
        self.Rate = None


    def _deserialize(self, params):
        self.CpuCore = params.get("CpuCore")
        self.Rate = params.get("Rate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDiskInfo(AbstractModel):
    """Disk monitoring data of the instance

    """

    def __init__(self):
        """
        :param IoRatioPerSec: Time percentage of IO operations per second\n        :type IoRatioPerSec: list of int\n        :param IoWaitTime: Average wait time of device I/O operations * 100 in milliseconds. For example, if the value is 201, the average wait time of I/O operations is 201/100 = 2.1 milliseconds.\n        :type IoWaitTime: list of int\n        :param Read: Average number of read operations completed by the disk per second * 100. For example, if the value is 2,002, the average number of read operations completed by the disk per second is 2,002/100=20.2.\n        :type Read: list of int\n        :param Write: Average number of write operations completed by the disk per second * 100. For example, if the value is 30,001, the average number of write operations completed by the disk per second is 30,001/100=300.01.\n        :type Write: list of int\n        :param CapacityRatio: Disk capacity. Each value is comprised of two data, with the first data representing the used capacity and the second one representing the total disk capacity.\n        :type CapacityRatio: list of int\n        """
        self.IoRatioPerSec = None
        self.IoWaitTime = None
        self.Read = None
        self.Write = None
        self.CapacityRatio = None


    def _deserialize(self, params):
        self.IoRatioPerSec = params.get("IoRatioPerSec")
        self.IoWaitTime = params.get("IoWaitTime")
        self.Read = params.get("Read")
        self.Write = params.get("Write")
        self.CapacityRatio = params.get("CapacityRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceMemInfo(AbstractModel):
    """Memory monitoring information of the physical server where the instance is located

    """

    def __init__(self):
        """
        :param Total: Total memory size in KB, which is the value of `total` in the `Mem:` in the `free` command\n        :type Total: list of int\n        :param Used: Used memory size in KB, which is the value of `used` in the `Mem:` row in the `free` command\n        :type Used: list of int\n        """
        self.Total = None
        self.Used = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceNetInfo(AbstractModel):
    """Network monitoring information of the physical server where the instance is located

    """

    def __init__(self):
        """
        :param Conn: Number of TCP connections\n        :type Conn: list of int\n        :param PackageIn: ENI inbound packets per second\n        :type PackageIn: list of int\n        :param PackageOut: ENI outbound packets per second\n        :type PackageOut: list of int\n        :param FlowIn: Inbound traffic in Kbps\n        :type FlowIn: list of int\n        :param FlowOut: Outbound traffic in Kbps\n        :type FlowOut: list of int\n        """
        self.Conn = None
        self.PackageIn = None
        self.PackageOut = None
        self.FlowIn = None
        self.FlowOut = None


    def _deserialize(self, params):
        self.Conn = params.get("Conn")
        self.PackageIn = params.get("PackageIn")
        self.PackageOut = params.get("PackageOut")
        self.FlowIn = params.get("FlowIn")
        self.FlowOut = params.get("FlowOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: Security group ID.\n        :type SecurityGroupId: str\n        :param InstanceIds: List of instance IDs, which is an array of one or more instance IDs.\n        :type InstanceIds: list of str\n        :param ForReadonlyInstance: This parameter takes effect only when the IDs of read-only replicas are passed in. If this parameter is set to `False` or left empty, the security group will be unbound from the RO groups of these read-only replicas. If this parameter is set to `True`, the security group will be unbound from the read-only replicas themselves.\n        :type ForReadonlyInstance: bool\n        """
        self.SecurityGroupId = None
        self.InstanceIds = None
        self.ForReadonlyInstance = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        self.ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DrInfo(AbstractModel):
    """Disaster recovery instance information

    """

    def __init__(self):
        """
        :param Status: Disaster recovery instance status\n        :type Status: int\n        :param Zone: AZ information\n        :type Zone: str\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param Region: Region information\n        :type Region: str\n        :param SyncStatus: Instance sync status. Possible returned values include:
0 - disaster recovery not synced;
1 - disaster recovery syncing;
2 - disaster recovery synced successfully;
3 - disaster recovery sync failed;
4 - repairing disaster recovery sync;\n        :type SyncStatus: int\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param InstanceType: Instance type\n        :type InstanceType: int\n        """
        self.Status = None
        self.Zone = None
        self.InstanceId = None
        self.Region = None
        self.SyncStatus = None
        self.InstanceName = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Zone = params.get("Zone")
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.SyncStatus = params.get("SyncStatus")
        self.InstanceName = params.get("InstanceName")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrlogItem(AbstractModel):
    """Structured error log details

    """

    def __init__(self):
        """
        :param Timestamp: Error occurrence time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Timestamp: int\n        :param Content: Error details
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Content: str\n        """
        self.Timestamp = None
        self.Content = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportRecord(AbstractModel):
    """Import task records

    """

    def __init__(self):
        """
        :param Status: Status value\n        :type Status: int\n        :param Code: Status value\n        :type Code: int\n        :param CostTime: Execution duration\n        :type CostTime: int\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param WorkId: Backend task ID\n        :type WorkId: str\n        :param FileName: Name of the file to be imported\n        :type FileName: str\n        :param Process: Execution progress\n        :type Process: int\n        :param CreateTime: Task creation time\n        :type CreateTime: str\n        :param FileSize: File size\n        :type FileSize: str\n        :param Message: Task execution information\n        :type Message: str\n        :param JobId: Task ID\n        :type JobId: int\n        :param DbName: Name of the table to be imported\n        :type DbName: str\n        :param AsyncRequestId: Async task request ID\n        :type AsyncRequestId: str\n        """
        self.Status = None
        self.Code = None
        self.CostTime = None
        self.InstanceId = None
        self.WorkId = None
        self.FileName = None
        self.Process = None
        self.CreateTime = None
        self.FileSize = None
        self.Message = None
        self.JobId = None
        self.DbName = None
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.CostTime = params.get("CostTime")
        self.InstanceId = params.get("InstanceId")
        self.WorkId = params.get("WorkId")
        self.FileName = params.get("FileName")
        self.Process = params.get("Process")
        self.CreateTime = params.get("CreateTime")
        self.FileSize = params.get("FileSize")
        self.Message = params.get("Message")
        self.JobId = params.get("JobId")
        self.DbName = params.get("DbName")
        self.AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inbound(AbstractModel):
    """Security group inbound rule

    """

    def __init__(self):
        """
        :param Action: Policy, which can be ACCEPT or DROP\n        :type Action: str\n        :param CidrIp: Source IP or IP range, such as 192.168.0.0/16\n        :type CidrIp: str\n        :param PortRange: Port\n        :type PortRange: str\n        :param IpProtocol: Network protocol. UDP and TCP are supported.\n        :type IpProtocol: str\n        :param Dir: The direction of the rule, which is INPUT for inbound rules\n        :type Dir: str\n        :param Desc: Rule description\n        :type Desc: str\n        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Dir = None
        self.Desc = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Dir = params.get("Dir")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceIds: list of str\n        :param NewPassword: New password of the instance. Rule: It can only contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special characters (!@#$%^*()).\n        :type NewPassword: str\n        :param Parameters: List of instance parameters. Currently, "character_set_server" and "lower_case_table_names" are supported, whose value ranges are ["utf8","latin1","gbk","utf8mb4"] and ["0","1"], respectively.\n        :type Parameters: list of ParamInfo\n        :param Vport: Instance port. Value range: [1024, 65535].\n        :type Vport: int\n        """
        self.InstanceIds = None
        self.NewPassword = None
        self.Parameters = None
        self.Vport = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.NewPassword = params.get("NewPassword")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.Parameters.append(obj)
        self.Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestIds: Array of async task request IDs, which can be used to query the execution results of async tasks.\n        :type AsyncRequestIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """Instance details

    """

    def __init__(self):
        """
        :param WanStatus: Public network access status. Value range: 0 (not enabled), 1 (enabled), 2 (disabled)\n        :type WanStatus: int\n        :param Zone: AZ information\n        :type Zone: str\n        :param InitFlag: Initialization flag. Value range: 0 (not initialized), 1 (initialized)\n        :type InitFlag: int\n        :param RoVipInfo: VIP information of a read-only instance. This field is exclusive to read-only instances where read-only access is enabled separately
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RoVipInfo: :class:`tencentcloud.cdb.v20170320.models.RoVipInfo`\n        :param Memory: Memory capacity in MB\n        :type Memory: int\n        :param Status: Instance status. Value range: 0 (creating), 1 (running), 4 (isolating), 5 (isolated)\n        :type Status: int\n        :param VpcId: VPC ID, such as 51102\n        :type VpcId: int\n        :param SlaveInfo: Information of a secondary server
Note: This field may return null, indicating that no valid values can be obtained.\n        :type SlaveInfo: :class:`tencentcloud.cdb.v20170320.models.SlaveInfo`\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param Volume: Disk capacity in GB\n        :type Volume: int\n        :param AutoRenew: Auto-renewal flag. Value range: 0 (auto-renewal not enabled), 1 (auto-renewal enabled), 2 (auto-renewal disabled)\n        :type AutoRenew: int\n        :param ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync)\n        :type ProtectMode: int\n        :param RoGroups: Details of a read-only group
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RoGroups: list of RoGroup\n        :param SubnetId: Subnet ID, such as 2333\n        :type SubnetId: int\n        :param InstanceType: Instance type. Value range: 1 (primary), 2 (disaster recovery), 3 (read-only)\n        :type InstanceType: int\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param Region: Region information\n        :type Region: str\n        :param DeadlineTime: Instance expiration time\n        :type DeadlineTime: str\n        :param DeployMode: AZ deployment mode. Valid values: 0 (single-AZ), 1 (multi-AZ)\n        :type DeployMode: int\n        :param TaskStatus: Instance task status. 0 - no task; 1 - upgrading; 2 - importing data; 3 - activating secondary; 4 - enabling public network access; 5 - batch operation in progress; 6 - rolling back; 7 - disabling public network access; 8 - changing password; 9 - renaming instance; 10 - restarting; 12 - migrating self-built instance; 13 - dropping table; 14 - creating and syncing disaster recovery instance; 15 - pending upgrade and switch; 16 - upgrade and switch in progress; 17 - upgrade and switch completed\n        :type TaskStatus: int\n        :param MasterInfo: Details of a primary instance
Note: This field may return null, indicating that no valid values can be obtained.\n        :type MasterInfo: :class:`tencentcloud.cdb.v20170320.models.MasterInfo`\n        :param DeviceType: Instance type\n        :type DeviceType: str\n        :param EngineVersion: Kernel version\n        :type EngineVersion: str\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param DrInfo: Details of a disaster recovery instance
Note: This field may return null, indicating that no valid values can be obtained.\n        :type DrInfo: list of DrInfo\n        :param WanDomain: Public domain name\n        :type WanDomain: str\n        :param WanPort: Public network port number\n        :type WanPort: int\n        :param PayType: Billing type\n        :type PayType: int\n        :param CreateTime: Instance creation time\n        :type CreateTime: str\n        :param Vip: Instance IP\n        :type Vip: str\n        :param Vport: Port number\n        :type Vport: int\n        :param CdbError: Lock flag\n        :type CdbError: int\n        :param UniqVpcId: VPC descriptor, such as "vpc-5v8wn9mg"\n        :type UniqVpcId: str\n        :param UniqSubnetId: Subnet descriptor, such as "subnet-1typ0s7d"\n        :type UniqSubnetId: str\n        :param PhysicalId: Physical ID\n        :type PhysicalId: str\n        :param Cpu: Number of cores\n        :type Cpu: int\n        :param Qps: Queries per second\n        :type Qps: int\n        :param ZoneName: AZ name\n        :type ZoneName: str\n        :param DeviceClass: Physical machine model
Note: This field may return null, indicating that no valid values can be obtained.\n        :type DeviceClass: str\n        :param DeployGroupId: Placement group ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeployGroupId: str\n        :param ZoneId: AZ ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ZoneId: int\n        :param InstanceNodes: Number of nodes\n        :type InstanceNodes: int\n        :param TagList: List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TagList: list of TagInfoItem\n        """
        self.WanStatus = None
        self.Zone = None
        self.InitFlag = None
        self.RoVipInfo = None
        self.Memory = None
        self.Status = None
        self.VpcId = None
        self.SlaveInfo = None
        self.InstanceId = None
        self.Volume = None
        self.AutoRenew = None
        self.ProtectMode = None
        self.RoGroups = None
        self.SubnetId = None
        self.InstanceType = None
        self.ProjectId = None
        self.Region = None
        self.DeadlineTime = None
        self.DeployMode = None
        self.TaskStatus = None
        self.MasterInfo = None
        self.DeviceType = None
        self.EngineVersion = None
        self.InstanceName = None
        self.DrInfo = None
        self.WanDomain = None
        self.WanPort = None
        self.PayType = None
        self.CreateTime = None
        self.Vip = None
        self.Vport = None
        self.CdbError = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.PhysicalId = None
        self.Cpu = None
        self.Qps = None
        self.ZoneName = None
        self.DeviceClass = None
        self.DeployGroupId = None
        self.ZoneId = None
        self.InstanceNodes = None
        self.TagList = None


    def _deserialize(self, params):
        self.WanStatus = params.get("WanStatus")
        self.Zone = params.get("Zone")
        self.InitFlag = params.get("InitFlag")
        if params.get("RoVipInfo") is not None:
            self.RoVipInfo = RoVipInfo()
            self.RoVipInfo._deserialize(params.get("RoVipInfo"))
        self.Memory = params.get("Memory")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        if params.get("SlaveInfo") is not None:
            self.SlaveInfo = SlaveInfo()
            self.SlaveInfo._deserialize(params.get("SlaveInfo"))
        self.InstanceId = params.get("InstanceId")
        self.Volume = params.get("Volume")
        self.AutoRenew = params.get("AutoRenew")
        self.ProtectMode = params.get("ProtectMode")
        if params.get("RoGroups") is not None:
            self.RoGroups = []
            for item in params.get("RoGroups"):
                obj = RoGroup()
                obj._deserialize(item)
                self.RoGroups.append(obj)
        self.SubnetId = params.get("SubnetId")
        self.InstanceType = params.get("InstanceType")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.DeadlineTime = params.get("DeadlineTime")
        self.DeployMode = params.get("DeployMode")
        self.TaskStatus = params.get("TaskStatus")
        if params.get("MasterInfo") is not None:
            self.MasterInfo = MasterInfo()
            self.MasterInfo._deserialize(params.get("MasterInfo"))
        self.DeviceType = params.get("DeviceType")
        self.EngineVersion = params.get("EngineVersion")
        self.InstanceName = params.get("InstanceName")
        if params.get("DrInfo") is not None:
            self.DrInfo = []
            for item in params.get("DrInfo"):
                obj = DrInfo()
                obj._deserialize(item)
                self.DrInfo.append(obj)
        self.WanDomain = params.get("WanDomain")
        self.WanPort = params.get("WanPort")
        self.PayType = params.get("PayType")
        self.CreateTime = params.get("CreateTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CdbError = params.get("CdbError")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.PhysicalId = params.get("PhysicalId")
        self.Cpu = params.get("Cpu")
        self.Qps = params.get("Qps")
        self.ZoneName = params.get("ZoneName")
        self.DeviceClass = params.get("DeviceClass")
        self.DeployGroupId = params.get("DeployGroupId")
        self.ZoneId = params.get("ZoneId")
        self.InstanceNodes = params.get("InstanceNodes")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfoItem()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRebootTime(AbstractModel):
    """Estimated time of instance restart

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param TimeInSeconds: Estimated restart time\n        :type TimeInSeconds: int\n        """
        self.InstanceId = None
        self.TimeInSeconds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TimeInSeconds = params.get("TimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRollbackRangeTime(AbstractModel):
    """Time range available for instance rollback

    """

    def __init__(self):
        """
        :param Code: Queries database error code\n        :type Code: int\n        :param Message: Queries database error message\n        :type Message: str\n        :param InstanceId: List of instance IDs. An instance ID is in the format of cdb-c1nl9rpv, which is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Times: Time range available for rollback\n        :type Times: list of RollbackTimeRange\n        """
        self.Code = None
        self.Message = None
        self.InstanceId = None
        self.Times = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.InstanceId = params.get("InstanceId")
        if params.get("Times") is not None:
            self.Times = []
            for item in params.get("Times"):
                obj = RollbackTimeRange()
                obj._deserialize(item)
                self.Times.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task. (This returned field has been disused. You can query the isolation status of an instance through the `DescribeDBInstances` API.)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class MasterInfo(AbstractModel):
    """Master instance information

    """

    def __init__(self):
        """
        :param Region: Region information\n        :type Region: str\n        :param RegionId: Region ID\n        :type RegionId: int\n        :param ZoneId: AZ ID\n        :type ZoneId: int\n        :param Zone: AZ information\n        :type Zone: str\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param ResourceId: Long instance ID\n        :type ResourceId: str\n        :param Status: Instance status\n        :type Status: int\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param InstanceType: Instance type\n        :type InstanceType: int\n        :param TaskStatus: Task status\n        :type TaskStatus: int\n        :param Memory: Memory capacity\n        :type Memory: int\n        :param Volume: Disk capacity\n        :type Volume: int\n        :param DeviceType: Instance model\n        :type DeviceType: str\n        :param Qps: Queries per second\n        :type Qps: int\n        :param VpcId: VPC ID\n        :type VpcId: int\n        :param SubnetId: Subnet ID\n        :type SubnetId: int\n        :param ExClusterId: Dedicated cluster ID\n        :type ExClusterId: str\n        :param ExClusterName: Dedicated cluster name\n        :type ExClusterName: str\n        """
        self.Region = None
        self.RegionId = None
        self.ZoneId = None
        self.Zone = None
        self.InstanceId = None
        self.ResourceId = None
        self.Status = None
        self.InstanceName = None
        self.InstanceType = None
        self.TaskStatus = None
        self.Memory = None
        self.Volume = None
        self.DeviceType = None
        self.Qps = None
        self.VpcId = None
        self.SubnetId = None
        self.ExClusterId = None
        self.ExClusterName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.InstanceId = params.get("InstanceId")
        self.ResourceId = params.get("ResourceId")
        self.Status = params.get("Status")
        self.InstanceName = params.get("InstanceName")
        self.InstanceType = params.get("InstanceType")
        self.TaskStatus = params.get("TaskStatus")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.DeviceType = params.get("DeviceType")
        self.Qps = params.get("Qps")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ExClusterId = params.get("ExClusterId")
        self.ExClusterName = params.get("ExClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Accounts: TencentDB account\n        :type Accounts: list of Account\n        :param Description: Database account remarks\n        :type Description: str\n        """
        self.InstanceId = None
        self.Accounts = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountMaxUserConnectionsRequest(AbstractModel):
    """ModifyAccountMaxUserConnections request structure.

    """

    def __init__(self):
        """
        :param Accounts: List of TencentDB accounts\n        :type Accounts: list of Account\n        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.\n        :type InstanceId: str\n        :param MaxUserConnections: The maximum number of instance connections supported by an account\n        :type MaxUserConnections: int\n        """
        self.Accounts = None
        self.InstanceId = None
        self.MaxUserConnections = None


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountMaxUserConnectionsResponse(AbstractModel):
    """ModifyAccountMaxUserConnections response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountPasswordRequest(AbstractModel):
    """ModifyAccountPassword request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param NewPassword: New password of the database account. It can only contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special characters (_+-&=!@#$%^*()).\n        :type NewPassword: str\n        :param Accounts: TencentDB account\n        :type Accounts: list of Account\n        """
        self.InstanceId = None
        self.NewPassword = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewPassword = params.get("NewPassword")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPasswordResponse(AbstractModel):
    """ModifyAccountPassword response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param Accounts: Database account, including username and domain name.\n        :type Accounts: list of Account\n        :param GlobalPrivileges: Global permission. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "PROCESS", "DROP", "REFERENCES", "INDEX", "ALTER", "SHOW DATABASES", "CREATE TEMPORARY TABLES", "LOCK TABLES", "EXECUTE", "CREATE VIEW", "SHOW VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.\n        :type GlobalPrivileges: list of str\n        :param DatabasePrivileges: Database permission. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", 	"DROP", "REFERENCES", "INDEX", "ALTER", "CREATE TEMPORARY TABLES", "LOCK TABLES", "EXECUTE", "CREATE VIEW", "SHOW VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.\n        :type DatabasePrivileges: list of DatabasePrivilege\n        :param TablePrivileges: Table permission in the database. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", 	"DROP", "REFERENCES", "INDEX", "ALTER", "CREATE VIEW", "SHOW VIEW", "TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.\n        :type TablePrivileges: list of TablePrivilege\n        :param ColumnPrivileges: Column permission in table. Valid values: "SELECT", "INSERT", "UPDATE", "REFERENCES".
Note: if this parameter is not passed in, it means to clear the permission.\n        :type ColumnPrivileges: list of ColumnPrivilege\n        :param ModifyAction: If this parameter is specified, permissions are modified in batches. Valid values: `grant`, `revoke`.\n        :type ModifyAction: str\n        """
        self.InstanceId = None
        self.Accounts = None
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None
        self.ModifyAction = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self.DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self.DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self.TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self.TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self.ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self.ColumnPrivileges.append(obj)
        self.ModifyAction = params.get("ModifyAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceIds: list of str\n        :param AutoRenew: Auto-renewal flag. Value range: 0 (auto-renewal not enabled), 1 (auto-renewal enabled).\n        :type AutoRenew: int\n        """
        self.InstanceIds = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param ExpireDays: Backup file retention period in days. Value range: 7-732.\n        :type ExpireDays: int\n        :param StartTime: (This parameter will be disused. The `BackupTimeWindow` parameter is recommended.) Backup time range in the format of 02:00-06:00, with the start time and end time on the hour. Valid values: 00:00-12:00, 02:00-06:00, 06:00-10:00, 10:00-14:00, 14:00-18:00, 18:00-22:00, 22:00-02:00.\n        :type StartTime: str\n        :param BackupMethod: Automatic backup mode. Only `physical` (physical cold backup) is supported\n        :type BackupMethod: str\n        :param BinlogExpireDays: Binlog retention period in days. Value range: 7-732. It cannot be greater than the retention period of backup files.\n        :type BinlogExpireDays: int\n        :param BackupTimeWindow: Backup time window; for example, to set up backup between 10:00 and 14:00 on every Tuesday and Sunday, you should set this parameter as follows: {"Monday": "", "Tuesday": "10:00-14:00", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday": "", "Sunday": "10:00-14:00"} (Note: You can set up backup on different days, but the backup time windows need to be the same. If this field is set, the `StartTime` field will be ignored)\n        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`\n        """
        self.InstanceId = None
        self.ExpireDays = None
        self.StartTime = None
        self.BackupMethod = None
        self.BinlogExpireDays = None
        self.BackupTimeWindow = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ExpireDays = params.get("ExpireDays")
        self.StartTime = params.get("StartTime")
        self.BackupMethod = params.get("BackupMethod")
        self.BinlogExpireDays = params.get("BinlogExpireDays")
        if params.get("BackupTimeWindow") is not None:
            self.BackupTimeWindow = CommonTimeWindow()
            self.BackupTimeWindow._deserialize(params.get("BackupTimeWindow"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        :param InstanceName: Instance name.\n        :type InstanceName: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Array of instance IDs in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceIds: list of str\n        :param NewProjectId: Project ID.\n        :type NewProjectId: int\n        """
        self.InstanceIds = None
        self.NewProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.NewProjectId = params.get("NewProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.\n        :type SecurityGroupIds: list of str\n        :param ForReadonlyInstance: This parameter takes effect only when the ID of read-only replica is passed in. If this parameter is set to `False` or left empty, the security groups bound with the RO group of the read-only replicas will be modified. If this parameter is set to `True`, the security groups bound with the read-only replica itself will be modified.\n        :type ForReadonlyInstance: bool\n        """
        self.InstanceId = None
        self.SecurityGroupIds = None
        self.ForReadonlyInstance = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceVipVportRequest(AbstractModel):
    """ModifyDBInstanceVipVport request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        :param DstIp: Destination IP. Either this parameter or `DstPort` must be passed in.\n        :type DstIp: str\n        :param DstPort: Destination port number. Value range: [1024-65535]. Either this parameter or `DstIp` must be passed in.\n        :type DstPort: int\n        :param UniqVpcId: Unified VPC ID\n        :type UniqVpcId: str\n        :param UniqSubnetId: Unified subnet ID.\n        :type UniqSubnetId: str\n        :param ReleaseDuration: Repossession duration in hours for old IP in the original network when changing from the basic network to VPC or changing the VPC subnet. Value range: 0-168 hours. Default value: 24 hours.\n        :type ReleaseDuration: int\n        """
        self.InstanceId = None
        self.DstIp = None
        self.DstPort = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.ReleaseDuration = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.ReleaseDuration = params.get("ReleaseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceVipVportResponse(AbstractModel):
    """ModifyDBInstanceVipVport response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task ID. (This returned field has been disused)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: List of short instance IDs.\n        :type InstanceIds: list of str\n        :param ParamList: List of parameters to be modified. Every element is a combination of `Name` (parameter name) and `CurrentValue` (new value).\n        :type ParamList: list of Parameter\n        :param TemplateId: Template ID. At least one of `ParamList` and `TemplateId` must be passed in.\n        :type TemplateId: int\n        :param WaitSwitch: When to perform the parameter adjustment task. Default value: 0. Valid values: 0 - execute immediately, 1 - execute during window. When its value is 1, only one instance ID can be passed in (i.e., only one `InstanceIds` can be passed in).\n        :type WaitSwitch: int\n        """
        self.InstanceIds = None
        self.ParamList = None
        self.TemplateId = None
        self.WaitSwitch = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.TemplateId = params.get("TemplateId")
        self.WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task ID, which can be used to query task progress.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceTagRequest(AbstractModel):
    """ModifyInstanceTag request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param ReplaceTags: Tag to be added or modified.\n        :type ReplaceTags: list of TagInfo\n        :param DeleteTags: Tag to be deleted.\n        :type DeleteTags: list of TagInfo\n        """
        self.InstanceId = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceTagResponse(AbstractModel):
    """ModifyInstanceTag response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNameOrDescByDpIdRequest(AbstractModel):
    """ModifyNameOrDescByDpId request structure.

    """

    def __init__(self):
        """
        :param DeployGroupId: ID of a placement group.\n        :type DeployGroupId: str\n        :param DeployGroupName: Name of a placement group, which can contain up to 60 characters. The placement group name and description cannot both be empty.\n        :type DeployGroupName: str\n        :param Description: Description of a placement group, which can contain up to 200 characters. The placement group name and description cannot both be empty.\n        :type Description: str\n        """
        self.DeployGroupId = None
        self.DeployGroupName = None
        self.Description = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.DeployGroupName = params.get("DeployGroupName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNameOrDescByDpIdResponse(AbstractModel):
    """ModifyNameOrDescByDpId response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param Name: Template name.\n        :type Name: str\n        :param Description: Template description.\n        :type Description: str\n        :param ParamList: List of parameters.\n        :type ParamList: list of Parameter\n        """
        self.TemplateId = None
        self.Name = None
        self.Description = None
        self.ParamList = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateResponse(AbstractModel):
    """ModifyParamTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoGroupInfoRequest(AbstractModel):
    """ModifyRoGroupInfo request structure.

    """

    def __init__(self):
        """
        :param RoGroupId: RO group ID.\n        :type RoGroupId: str\n        :param RoGroupInfo: RO group details.\n        :type RoGroupInfo: :class:`tencentcloud.cdb.v20170320.models.RoGroupAttr`\n        :param RoWeightValues: Weights of instances in RO group. If the weighting mode of an RO group is changed to custom mode, this parameter must be set, and a weight value needs to be set for each RO instance.\n        :type RoWeightValues: list of RoWeightValue\n        :param IsBalanceRoLoad: Whether to rebalance the loads of read-only replicas in the RO group. Valid values: `1` (yes), `0` (no). Default value: `0`. If this parameter is set to `1`, connections to the read-only replicas in the RO group will be interrupted transiently. Please ensure that your application has a reconnection mechanism.\n        :type IsBalanceRoLoad: int\n        """
        self.RoGroupId = None
        self.RoGroupInfo = None
        self.RoWeightValues = None
        self.IsBalanceRoLoad = None


    def _deserialize(self, params):
        self.RoGroupId = params.get("RoGroupId")
        if params.get("RoGroupInfo") is not None:
            self.RoGroupInfo = RoGroupAttr()
            self.RoGroupInfo._deserialize(params.get("RoGroupInfo"))
        if params.get("RoWeightValues") is not None:
            self.RoWeightValues = []
            for item in params.get("RoWeightValues"):
                obj = RoWeightValue()
                obj._deserialize(item)
                self.RoWeightValues.append(obj)
        self.IsBalanceRoLoad = params.get("IsBalanceRoLoad")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoGroupInfoResponse(AbstractModel):
    """ModifyRoGroupInfo response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoReplicationDelayRequest(AbstractModel):
    """ModifyRoReplicationDelay request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param ReplicationDelay: Replication delay in seconds. Value range: 1 to 259200.\n        :type ReplicationDelay: int\n        """
        self.InstanceId = None
        self.ReplicationDelay = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReplicationDelay = params.get("ReplicationDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoReplicationDelayResponse(AbstractModel):
    """ModifyRoReplicationDelay response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoTypeRequest(AbstractModel):
    """ModifyRoType request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param SrcRoInstType: The original type of an RO replica. Valid values: `NORMAL` (do not support delayed replication), `DELAY_REPLICATION` (support delayed replication).\n        :type SrcRoInstType: str\n        :param DstRoInstType: The target type of an RO replica. Valid values: `NORMAL` (do not support delayed replication), `DELAY_REPLICATION` (support delayed replication).\n        :type DstRoInstType: str\n        :param ReplicationDelay: Replication delay in seconds. This parameter is required when a regular RO replica is switched to a delayed one. Value range: 1 to 259200.\n        :type ReplicationDelay: int\n        """
        self.InstanceId = None
        self.SrcRoInstType = None
        self.DstRoInstType = None
        self.ReplicationDelay = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcRoInstType = params.get("SrcRoInstType")
        self.DstRoInstType = params.get("DstRoInstType")
        self.ReplicationDelay = params.get("ReplicationDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoTypeResponse(AbstractModel):
    """ModifyRoType response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTimeWindowRequest(AbstractModel):
    """ModifyTimeWindow request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        :param TimeRanges: Time period available for maintenance after modification in the format of 10:00-12:00. Each period lasts from half an hour to three hours, with the start time and end time aligned by half-hour. Up to two time periods can be set. Start and end time range: [00:00, 24:00].\n        :type TimeRanges: list of str\n        :param Weekdays: Specifies for which day to modify the time period. Value range: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. If it is not specified or is left blank, the time period will be modified for every day by default.\n        :type Weekdays: list of str\n        """
        self.InstanceId = None
        self.TimeRanges = None
        self.Weekdays = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TimeRanges = params.get("TimeRanges")
        self.Weekdays = params.get("Weekdays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTimeWindowResponse(AbstractModel):
    """ModifyTimeWindow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OfflineIsolatedInstancesRequest(AbstractModel):
    """OfflineIsolatedInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceIds: list of str\n        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineIsolatedInstancesResponse(AbstractModel):
    """OfflineIsolatedInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OpenDBInstanceGTIDRequest(AbstractModel):
    """OpenDBInstanceGTID request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBInstanceGTIDResponse(AbstractModel):
    """OpenDBInstanceGTID response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class OpenWanServiceRequest(AbstractModel):
    """OpenWanService request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWanServiceResponse(AbstractModel):
    """OpenWanService response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class Outbound(AbstractModel):
    """Security group outbound rule

    """

    def __init__(self):
        """
        :param Action: Policy, which can be ACCEPT or DROP\n        :type Action: str\n        :param CidrIp: Destination IP or IP range, such as 172.16.0.0/12\n        :type CidrIp: str\n        :param PortRange: Port or port range\n        :type PortRange: str\n        :param IpProtocol: Network protocol. UDP and TCP are supported\n        :type IpProtocol: str\n        :param Dir: The direction of the rule, which is OUTPUT for inbound rules\n        :type Dir: str\n        :param Desc: Rule description\n        :type Desc: str\n        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Dir = None
        self.Desc = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Dir = params.get("Dir")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    """Instance parameter information

    """

    def __init__(self):
        """
        :param Name: Parameter name\n        :type Name: str\n        :param Value: Parameter value\n        :type Value: str\n        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamRecord(AbstractModel):
    """Parameter modification records

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param ParamName: Parameter name\n        :type ParamName: str\n        :param OldValue: Parameter value before modification\n        :type OldValue: str\n        :param NewValue: Parameter value after modification\n        :type NewValue: str\n        :param IsSucess: Whether the parameter is modified successfully\n        :type IsSucess: bool\n        :param ModifyTime: Modification time\n        :type ModifyTime: str\n        """
        self.InstanceId = None
        self.ParamName = None
        self.OldValue = None
        self.NewValue = None
        self.IsSucess = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ParamName = params.get("ParamName")
        self.OldValue = params.get("OldValue")
        self.NewValue = params.get("NewValue")
        self.IsSucess = params.get("IsSucess")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateInfo(AbstractModel):
    """Parameter template information

    """

    def __init__(self):
        """
        :param TemplateId: Parameter template ID\n        :type TemplateId: int\n        :param Name: Parameter template name\n        :type Name: str\n        :param Description: Parameter template description\n        :type Description: str\n        :param EngineVersion: Instance engine version\n        :type EngineVersion: str\n        """
        self.TemplateId = None
        self.Name = None
        self.Description = None
        self.EngineVersion = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Parameter(AbstractModel):
    """Database instance parameter

    """

    def __init__(self):
        """
        :param Name: Parameter name\n        :type Name: str\n        :param CurrentValue: Parameter value\n        :type CurrentValue: str\n        """
        self.Name = None
        self.CurrentValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CurrentValue = params.get("CurrentValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterDetail(AbstractModel):
    """Instance parameter details

    """

    def __init__(self):
        """
        :param Name: Parameter name\n        :type Name: str\n        :param ParamType: Parameter type\n        :type ParamType: str\n        :param Default: Default value of the parameter\n        :type Default: str\n        :param Description: Parameter description\n        :type Description: str\n        :param CurrentValue: Current value of the parameter\n        :type CurrentValue: str\n        :param NeedReboot: Whether the database needs to be restarted for the modified parameter to take effect. Value range: 0 (no); 1 (yes)\n        :type NeedReboot: int\n        :param Max: Maximum value of the parameter\n        :type Max: int\n        :param Min: Minimum value of the parameter\n        :type Min: int\n        :param EnumValue: Enumerated values of the parameter. It is null if the parameter is non-enumerated\n        :type EnumValue: list of str\n        """
        self.Name = None
        self.ParamType = None
        self.Default = None
        self.Description = None
        self.CurrentValue = None
        self.NeedReboot = None
        self.Max = None
        self.Min = None
        self.EnumValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ParamType = params.get("ParamType")
        self.Default = params.get("Default")
        self.Description = params.get("Description")
        self.CurrentValue = params.get("CurrentValue")
        self.NeedReboot = params.get("NeedReboot")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.EnumValue = params.get("EnumValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionSellConf(AbstractModel):
    """Sale configuration of the region

    """

    def __init__(self):
        """
        :param RegionName: Region name\n        :type RegionName: str\n        :param Area: Area\n        :type Area: str\n        :param IsDefaultRegion: Whether it is a default region\n        :type IsDefaultRegion: int\n        :param Region: Region name\n        :type Region: str\n        :param ZonesConf: Sale configuration of the AZ\n        :type ZonesConf: list of ZoneSellConf\n        """
        self.RegionName = None
        self.Area = None
        self.IsDefaultRegion = None
        self.Region = None
        self.ZonesConf = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.Area = params.get("Area")
        self.IsDefaultRegion = params.get("IsDefaultRegion")
        self.Region = params.get("Region")
        if params.get("ZonesConf") is not None:
            self.ZonesConf = []
            for item in params.get("ZonesConf"):
                obj = ZoneSellConf()
                obj._deserialize(item)
                self.ZonesConf.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIsolatedDBInstancesRequest(AbstractModel):
    """ReleaseIsolatedDBInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Array of instance IDs in the format of `cdb-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the ID, whose value is the `InstanceId` value in the output parameters.\n        :type InstanceIds: list of str\n        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIsolatedDBInstancesResponse(AbstractModel):
    """ReleaseIsolatedDBInstances response structure.

    """

    def __init__(self):
        """
        :param Items: Deisolation result set.\n        :type Items: list of ReleaseResult\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ReleaseResult()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class ReleaseResult(AbstractModel):
    """Deisolation task result

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param Code: Result value of instance deisolation. A returned value of 0 indicates success.\n        :type Code: int\n        :param Message: Error message for instance deisolation.\n        :type Message: str\n        """
        self.InstanceId = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstancesRequest(AbstractModel):
    """RestartDBInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Array of instance IDs in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceIds: list of str\n        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstancesResponse(AbstractModel):
    """RestartDBInstances response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class RoGroup(AbstractModel):
    """Read-only group parameter

    """

    def __init__(self):
        """
        :param RoGroupMode: Read-only group mode. Valid values: `alone` (the system assigns a read-only group automatically), `allinone` (a new read-only group will be created), `join` (an existing read-only group will be used).\n        :type RoGroupMode: str\n        :param RoGroupId: Read-only group ID.\n        :type RoGroupId: str\n        :param RoGroupName: Read-only group name.\n        :type RoGroupName: str\n        :param RoOfflineDelay: Whether to enable the function of isolating an instance that exceeds the latency threshold. If it is enabled, when the latency between the read-only instance and the primary instance exceeds the latency threshold, the read-only instance will be isolated. Valid values: 1 (enabled), 0 (not enabled)\n        :type RoOfflineDelay: int\n        :param RoMaxDelayTime: Latency threshold\n        :type RoMaxDelayTime: int\n        :param MinRoInGroup: Minimum number of instances to be retained. If the number of the purchased read-only instances is smaller than the set value, they will not be removed.\n        :type MinRoInGroup: int\n        :param WeightMode: Read/write weight distribution mode. Valid values: `system` (weights are assigned by the system automatically), `custom` (weights are customized)\n        :type WeightMode: str\n        :param Weight: Weight value.\n        :type Weight: int\n        :param RoInstances: Details of read-only instances in read-only group\n        :type RoInstances: list of RoInstanceInfo\n        :param Vip: Private IP of read-only group.\n        :type Vip: str\n        :param Vport: Private network port number of read-only group.\n        :type Vport: int\n        :param UniqVpcId: VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UniqVpcId: str\n        :param UniqSubnetId: Subnet ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UniqSubnetId: str\n        :param RoGroupRegion: Read-only group region.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RoGroupRegion: str\n        :param RoGroupZone: Read-only group AZ.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RoGroupZone: str\n        """
        self.RoGroupMode = None
        self.RoGroupId = None
        self.RoGroupName = None
        self.RoOfflineDelay = None
        self.RoMaxDelayTime = None
        self.MinRoInGroup = None
        self.WeightMode = None
        self.Weight = None
        self.RoInstances = None
        self.Vip = None
        self.Vport = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.RoGroupRegion = None
        self.RoGroupZone = None


    def _deserialize(self, params):
        self.RoGroupMode = params.get("RoGroupMode")
        self.RoGroupId = params.get("RoGroupId")
        self.RoGroupName = params.get("RoGroupName")
        self.RoOfflineDelay = params.get("RoOfflineDelay")
        self.RoMaxDelayTime = params.get("RoMaxDelayTime")
        self.MinRoInGroup = params.get("MinRoInGroup")
        self.WeightMode = params.get("WeightMode")
        self.Weight = params.get("Weight")
        if params.get("RoInstances") is not None:
            self.RoInstances = []
            for item in params.get("RoInstances"):
                obj = RoInstanceInfo()
                obj._deserialize(item)
                self.RoInstances.append(obj)
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.RoGroupRegion = params.get("RoGroupRegion")
        self.RoGroupZone = params.get("RoGroupZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoGroupAttr(AbstractModel):
    """RO group configuration information.

    """

    def __init__(self):
        """
        :param RoGroupName: RO group name.\n        :type RoGroupName: str\n        :param RoMaxDelayTime: Maximum delay threshold for RO instances in seconds. Minimum value: 1. Please note that this value will take effect only if an instance removal policy is enabled in the RO group.\n        :type RoMaxDelayTime: int\n        :param RoOfflineDelay: Whether to enable instance removal. Valid values: 1 (enabled), 0 (not enabled). Please note that if instance removal is enabled, the delay threshold parameter (`RoMaxDelayTime`) must be set.\n        :type RoOfflineDelay: int\n        :param MinRoInGroup: Minimum number of instances to be retained, which can be set to any value less than or equal to the number of RO instances in the RO group. Please note that if this value is set to be greater than the number of RO instances, no removal will be performed, and if it is set to 0, all instances with an excessive delay will be removed.\n        :type MinRoInGroup: int\n        :param WeightMode: Weighting mode. Supported values include `system` (automatically assigned by the system) and `custom` (defined by user). Please note that if the `custom` mode is selected, the RO instance weight configuration parameter (RoWeightValues) must be set.\n        :type WeightMode: str\n        """
        self.RoGroupName = None
        self.RoMaxDelayTime = None
        self.RoOfflineDelay = None
        self.MinRoInGroup = None
        self.WeightMode = None


    def _deserialize(self, params):
        self.RoGroupName = params.get("RoGroupName")
        self.RoMaxDelayTime = params.get("RoMaxDelayTime")
        self.RoOfflineDelay = params.get("RoOfflineDelay")
        self.MinRoInGroup = params.get("MinRoInGroup")
        self.WeightMode = params.get("WeightMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoInstanceInfo(AbstractModel):
    """RO instance details

    """

    def __init__(self):
        """
        :param MasterInstanceId: Master instance ID corresponding to the RO group\n        :type MasterInstanceId: str\n        :param RoStatus: RO instance status in the RO group. Value range: online, offline\n        :type RoStatus: str\n        :param OfflineTime: Last deactivation time of a RO instance in the RO group\n        :type OfflineTime: str\n        :param Weight: RO instance weight in the RO group\n        :type Weight: int\n        :param Region: RO instance region name, such as ap-shanghai\n        :type Region: str\n        :param Zone: Name of RO AZ, such as ap-shanghai-1\n        :type Zone: str\n        :param InstanceId: RO instance ID in the format of cdbro-c1nl9rpv\n        :type InstanceId: str\n        :param Status: RO instance status. Value range: 0 (creating), 1 (running), 4 (deleting)\n        :type Status: int\n        :param InstanceType: Instance type. Value range: 1 (primary), 2 (disaster recovery), 3 (read-only)\n        :type InstanceType: int\n        :param InstanceName: RO instance name\n        :type InstanceName: str\n        :param HourFeeStatus: Pay-as-you-go billing status. Value range: 1 (normal), 2 (in arrears)\n        :type HourFeeStatus: int\n        :param TaskStatus: RO instance task status. Value range: <br>0 - no task <br>1 - upgrading <br>2 - importing data <br>3 - activating secondary <br>4 - public network access enabled <br>5 - batch operation in progress <br>6 - rolling back <br>7 - public network access not enabled <br>8 - modifying password <br>9 - renaming instance <br>10 - restarting <br>12 - migrating self-built instance <br>13 - dropping table <br>14 - creating and syncing disaster recovery instance\n        :type TaskStatus: int\n        :param Memory: RO instance memory size in MB\n        :type Memory: int\n        :param Volume: RO instance disk size in GB\n        :type Volume: int\n        :param Qps: Queries per second\n        :type Qps: int\n        :param Vip: Private IP address of the RO instance\n        :type Vip: str\n        :param Vport: Access port of the RO instance\n        :type Vport: int\n        :param VpcId: VPC ID of the RO instance\n        :type VpcId: int\n        :param SubnetId: VPC subnet ID of the RO instance\n        :type SubnetId: int\n        :param DeviceType: RO instance specification description. Value range: CUSTOM\n        :type DeviceType: str\n        :param EngineVersion: Database engine version of the read-only replica. Valid values: `5.1`, `5.5`, `5.6`, `5.7`, `8.0`\n        :type EngineVersion: str\n        :param DeadlineTime: RO instance expiration time in the format of yyyy-mm-dd hh:mm:ss. If it is a pay-as-you-go instance, the value of this field is 0000-00-00 00:00:00\n        :type DeadlineTime: str\n        :param PayType: RO instance billing method. Value range: 0 (monthly subscribed), 1 (pay-as-you-go), 2 (monthly postpaid)\n        :type PayType: int\n        """
        self.MasterInstanceId = None
        self.RoStatus = None
        self.OfflineTime = None
        self.Weight = None
        self.Region = None
        self.Zone = None
        self.InstanceId = None
        self.Status = None
        self.InstanceType = None
        self.InstanceName = None
        self.HourFeeStatus = None
        self.TaskStatus = None
        self.Memory = None
        self.Volume = None
        self.Qps = None
        self.Vip = None
        self.Vport = None
        self.VpcId = None
        self.SubnetId = None
        self.DeviceType = None
        self.EngineVersion = None
        self.DeadlineTime = None
        self.PayType = None


    def _deserialize(self, params):
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.RoStatus = params.get("RoStatus")
        self.OfflineTime = params.get("OfflineTime")
        self.Weight = params.get("Weight")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.InstanceType = params.get("InstanceType")
        self.InstanceName = params.get("InstanceName")
        self.HourFeeStatus = params.get("HourFeeStatus")
        self.TaskStatus = params.get("TaskStatus")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.Qps = params.get("Qps")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DeviceType = params.get("DeviceType")
        self.EngineVersion = params.get("EngineVersion")
        self.DeadlineTime = params.get("DeadlineTime")
        self.PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoVipInfo(AbstractModel):
    """VIP information of the read-only instance

    """

    def __init__(self):
        """
        :param RoVipStatus: VIP status of the read-only instance\n        :type RoVipStatus: int\n        :param RoSubnetId: VPC subnet of the read-only instance\n        :type RoSubnetId: int\n        :param RoVpcId: VPC of the read-only instance\n        :type RoVpcId: int\n        :param RoVport: VIP port number of the read-only instance\n        :type RoVport: int\n        :param RoVip: VIP of the read-only instance\n        :type RoVip: str\n        """
        self.RoVipStatus = None
        self.RoSubnetId = None
        self.RoVpcId = None
        self.RoVport = None
        self.RoVip = None


    def _deserialize(self, params):
        self.RoVipStatus = params.get("RoVipStatus")
        self.RoSubnetId = params.get("RoSubnetId")
        self.RoVpcId = params.get("RoVpcId")
        self.RoVport = params.get("RoVport")
        self.RoVip = params.get("RoVip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoWeightValue(AbstractModel):
    """RO instance weight value

    """

    def __init__(self):
        """
        :param InstanceId: RO instance ID.\n        :type InstanceId: str\n        :param Weight: Weight value. Value range: [0, 100].\n        :type Weight: int\n        """
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackDBName(AbstractModel):
    """Name of the database for rollback

    """

    def __init__(self):
        """
        :param DatabaseName: Original database name before rollback
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DatabaseName: str\n        :param NewDatabaseName: New database name after rollback
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NewDatabaseName: str\n        """
        self.DatabaseName = None
        self.NewDatabaseName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.NewDatabaseName = params.get("NewDatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstancesInfo(AbstractModel):
    """Details of the instance for rollback

    """

    def __init__(self):
        """
        :param InstanceId: TencentDB instance ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceId: str\n        :param Strategy: Rollback policy. Value range: table, db, full. Default value: full. Table: expedited rollback mode, where only the selected table-level backups and binlogs are imported; for cross-table rollback, if the associated tables are not selected simultaneously, the rollback will fail; the parameter `Databases` must be empty under this mode. db: fast rollback mode, where only the selected database-level backups and binlogs are imported; for cross-database rollback, if the associated databases are not selected simultaneously, the rollback will fail. full: ordinary rollback mode, which imports all the backups and binlogs of the instance at a relatively low speed.\n        :type Strategy: str\n        :param RollbackTime: Database rollback time in the format of yyyy-mm-dd hh:mm:ss\n        :type RollbackTime: str\n        :param Databases: Information of the databases to be rolled back, which means rollback at the database level
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Databases: list of RollbackDBName\n        :param Tables: Information of the tables to be rolled back, which means rollback at the table level
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tables: list of RollbackTables\n        """
        self.InstanceId = None
        self.Strategy = None
        self.RollbackTime = None
        self.Databases = None
        self.Tables = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Strategy = params.get("Strategy")
        self.RollbackTime = params.get("RollbackTime")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = RollbackDBName()
                obj._deserialize(item)
                self.Databases.append(obj)
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = RollbackTables()
                obj._deserialize(item)
                self.Tables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTableName(AbstractModel):
    """Name of the table for rollback

    """

    def __init__(self):
        """
        :param TableName: Original table name before rollback
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableName: str\n        :param NewTableName: New table name after rollback
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NewTableName: str\n        """
        self.TableName = None
        self.NewTableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.NewTableName = params.get("NewTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTables(AbstractModel):
    """Details of the table for rollback

    """

    def __init__(self):
        """
        :param Database: Database name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Database: str\n        :param Table: Table details
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Table: list of RollbackTableName\n        """
        self.Database = None
        self.Table = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        if params.get("Table") is not None:
            self.Table = []
            for item in params.get("Table"):
                obj = RollbackTableName()
                obj._deserialize(item)
                self.Table.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTask(AbstractModel):
    """Rollback task details

    """

    def __init__(self):
        """
        :param Info: Task execution information.\n        :type Info: str\n        :param Status: Task execution result. Valid values: INITIAL: initializing, RUNNING: running, SUCCESS: succeeded, FAILED: failed, KILLED: terminated, REMOVED: deleted, PAUSED: paused.\n        :type Status: str\n        :param Progress: Task execution progress. Value range: [0,100].\n        :type Progress: int\n        :param StartTime: Task start time.\n        :type StartTime: str\n        :param EndTime: Task end time.\n        :type EndTime: str\n        :param Detail: Rollback task details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Detail: list of RollbackInstancesInfo\n        """
        self.Info = None
        self.Status = None
        self.Progress = None
        self.StartTime = None
        self.EndTime = None
        self.Detail = None


    def _deserialize(self, params):
        self.Info = params.get("Info")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = RollbackInstancesInfo()
                obj._deserialize(item)
                self.Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTimeRange(AbstractModel):
    """Time range available for rollback

    """

    def __init__(self):
        """
        :param Begin: Start time available for rollback in the format of yyyy-MM-dd HH:mm:ss, such as 2016-10-29 01:06:04\n        :type Begin: str\n        :param End: End time available for rollback in the format of yyyy-MM-dd HH:mm:ss, such as 2016-11-02 11:44:47\n        :type End: str\n        """
        self.Begin = None
        self.End = None


    def _deserialize(self, params):
        self.Begin = params.get("Begin")
        self.End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """Security group details

    """

    def __init__(self):
        """
        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss\n        :type CreateTime: str\n        :param Inbound: Inbound rule\n        :type Inbound: list of Inbound\n        :param Outbound: Outbound rule\n        :type Outbound: list of Outbound\n        :param SecurityGroupId: Security group ID\n        :type SecurityGroupId: str\n        :param SecurityGroupName: Security group name\n        :type SecurityGroupName: str\n        :param SecurityGroupRemark: Security group remarks\n        :type SecurityGroupRemark: str\n        """
        self.ProjectId = None
        self.CreateTime = None
        self.Inbound = None
        self.Outbound = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self.Outbound.append(obj)
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SellConfig(AbstractModel):
    """Purchasable configuration details

    """

    def __init__(self):
        """
        :param Device: (Disused) Device type\n        :type Device: str\n        :param Type: (Disused) Purchasable specification description \n        :type Type: str\n        :param CdbType: (Disused) Instance type \n        :type CdbType: str\n        :param Memory: Memory size in MB\n        :type Memory: int\n        :param Cpu: CPU core count\n        :type Cpu: int\n        :param VolumeMin: Minimum disk size in GB\n        :type VolumeMin: int\n        :param VolumeMax: Maximum disk size in GB\n        :type VolumeMax: int\n        :param VolumeStep: Disk increment in GB\n        :type VolumeStep: int\n        :param Connection: Number of connections\n        :type Connection: int\n        :param Qps: Queries per second\n        :type Qps: int\n        :param Iops: IOs per second\n        :type Iops: int\n        :param Info: Application scenario description\n        :type Info: str\n        :param Status: Status. Value `0` indicates that this specification is purchasable.\n        :type Status: int\n        :param Tag: (Disused) Tag value\n        :type Tag: int\n        :param DeviceType: Instance resource isolation type. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance).
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type DeviceType: str\n        :param DeviceTypeName: Instance resource isolation type. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance).
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type DeviceTypeName: str\n        """
        self.Device = None
        self.Type = None
        self.CdbType = None
        self.Memory = None
        self.Cpu = None
        self.VolumeMin = None
        self.VolumeMax = None
        self.VolumeStep = None
        self.Connection = None
        self.Qps = None
        self.Iops = None
        self.Info = None
        self.Status = None
        self.Tag = None
        self.DeviceType = None
        self.DeviceTypeName = None


    def _deserialize(self, params):
        self.Device = params.get("Device")
        self.Type = params.get("Type")
        self.CdbType = params.get("CdbType")
        self.Memory = params.get("Memory")
        self.Cpu = params.get("Cpu")
        self.VolumeMin = params.get("VolumeMin")
        self.VolumeMax = params.get("VolumeMax")
        self.VolumeStep = params.get("VolumeStep")
        self.Connection = params.get("Connection")
        self.Qps = params.get("Qps")
        self.Iops = params.get("Iops")
        self.Info = params.get("Info")
        self.Status = params.get("Status")
        self.Tag = params.get("Tag")
        self.DeviceType = params.get("DeviceType")
        self.DeviceTypeName = params.get("DeviceTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SellType(AbstractModel):
    """Purchasable instance type

    """

    def __init__(self):
        """
        :param TypeName: Name of the purchasable instance\n        :type TypeName: str\n        :param EngineVersion: Kernel version number\n        :type EngineVersion: list of str\n        :param Configs: Configuration details of a purchasable specification\n        :type Configs: list of SellConfig\n        """
        self.TypeName = None
        self.EngineVersion = None
        self.Configs = None


    def _deserialize(self, params):
        self.TypeName = params.get("TypeName")
        self.EngineVersion = params.get("EngineVersion")
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = SellConfig()
                obj._deserialize(item)
                self.Configs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveConfig(AbstractModel):
    """Configuration information of the salve database

    """

    def __init__(self):
        """
        :param ReplicationMode: Replication mode of the secondary database. Value range: async, semi-sync\n        :type ReplicationMode: str\n        :param Zone: AZ name of the secondary database, such as ap-shanghai-1\n        :type Zone: str\n        """
        self.ReplicationMode = None
        self.Zone = None


    def _deserialize(self, params):
        self.ReplicationMode = params.get("ReplicationMode")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveInfo(AbstractModel):
    """Slave server information

    """

    def __init__(self):
        """
        :param First: Information of secondary server 1\n        :type First: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`\n        :param Second: Information of secondary server 2
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Second: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`\n        """
        self.First = None
        self.Second = None


    def _deserialize(self, params):
        if params.get("First") is not None:
            self.First = SlaveInstanceInfo()
            self.First._deserialize(params.get("First"))
        if params.get("Second") is not None:
            self.Second = SlaveInstanceInfo()
            self.Second._deserialize(params.get("Second"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveInstanceInfo(AbstractModel):
    """Slave server information

    """

    def __init__(self):
        """
        :param Vport: Port number\n        :type Vport: int\n        :param Region: Region information\n        :type Region: str\n        :param Vip: Virtual IP information\n        :type Vip: str\n        :param Zone: AZ information\n        :type Zone: str\n        """
        self.Vport = None
        self.Region = None
        self.Vip = None
        self.Zone = None


    def _deserialize(self, params):
        self.Vport = params.get("Vport")
        self.Region = params.get("Region")
        self.Vip = params.get("Vip")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogInfo(AbstractModel):
    """Slow log details

    """

    def __init__(self):
        """
        :param Name: Backup filename\n        :type Name: str\n        :param Size: Backup file size in bytes\n        :type Size: int\n        :param Date: Backup snapshot time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-03-17 02:10:37\n        :type Date: str\n        :param IntranetUrl: Download address on the private network\n        :type IntranetUrl: str\n        :param InternetUrl: Download address on the public network\n        :type InternetUrl: str\n        :param Type: Log type. Value range: slowlog (slow log)\n        :type Type: str\n        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogItem(AbstractModel):
    """Structured slow log details

    """

    def __init__(self):
        """
        :param Timestamp: SQL execution time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Timestamp: int\n        :param QueryTime: SQL execution duration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type QueryTime: float\n        :param SqlText: SQL statement.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SqlText: str\n        :param UserHost: Client address.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UserHost: str\n        :param UserName: Username.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UserName: str\n        :param Database: Database name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Database: str\n        :param LockTime: Lock duration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LockTime: float\n        :param RowsExamined: Number of scanned rows.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RowsExamined: int\n        :param RowsSent: Number of rows in result set.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RowsSent: int\n        :param SqlTemplate: SQL template.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SqlTemplate: str\n        :param Md5: SQL statement MD5.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Md5: str\n        """
        self.Timestamp = None
        self.QueryTime = None
        self.SqlText = None
        self.UserHost = None
        self.UserName = None
        self.Database = None
        self.LockTime = None
        self.RowsExamined = None
        self.RowsSent = None
        self.SqlTemplate = None
        self.Md5 = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.QueryTime = params.get("QueryTime")
        self.SqlText = params.get("SqlText")
        self.UserHost = params.get("UserHost")
        self.UserName = params.get("UserName")
        self.Database = params.get("Database")
        self.LockTime = params.get("LockTime")
        self.RowsExamined = params.get("RowsExamined")
        self.RowsSent = params.get("RowsSent")
        self.SqlTemplate = params.get("SqlTemplate")
        self.Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SqlFileInfo(AbstractModel):
    """SQL file information

    """

    def __init__(self):
        """
        :param UploadTime: Upload time\n        :type UploadTime: str\n        :param UploadInfo: Upload progress\n        :type UploadInfo: :class:`tencentcloud.cdb.v20170320.models.UploadInfo`\n        :param FileName: Filename\n        :type FileName: str\n        :param FileSize: File size in bytes\n        :type FileSize: int\n        :param IsUploadFinished: Whether upload is finished. Valid values: 0 (not completed), 1 (completed)\n        :type IsUploadFinished: int\n        :param FileId: File ID\n        :type FileId: str\n        """
        self.UploadTime = None
        self.UploadInfo = None
        self.FileName = None
        self.FileSize = None
        self.IsUploadFinished = None
        self.FileId = None


    def _deserialize(self, params):
        self.UploadTime = params.get("UploadTime")
        if params.get("UploadInfo") is not None:
            self.UploadInfo = UploadInfo()
            self.UploadInfo._deserialize(params.get("UploadInfo"))
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.IsUploadFinished = params.get("IsUploadFinished")
        self.FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBatchRollbackRequest(AbstractModel):
    """StartBatchRollback request structure.

    """

    def __init__(self):
        """
        :param Instances: Details of the instance for rollback\n        :type Instances: list of RollbackInstancesInfo\n        """
        self.Instances = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = RollbackInstancesInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBatchRollbackResponse(AbstractModel):
    """StartBatchRollback response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class StartDelayReplicationRequest(AbstractModel):
    """StartDelayReplication request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param DelayReplicationType: Delayed replication mode. Valid values: `DEFAULT` (replicate according to the specified replication delay), `GTID` (replicate according to the specified GTID), `DUE_TIME` (replicate according to the specified point in time).\n        :type DelayReplicationType: str\n        :param DueTime: Specified point in time. Default value: 0. The maximum value cannot be later than the current time.\n        :type DueTime: int\n        :param Gtid: Specified GITD. This parameter is required when the delayed replication mode is `GTID`.\n        :type Gtid: str\n        """
        self.InstanceId = None
        self.DelayReplicationType = None
        self.DueTime = None
        self.Gtid = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DelayReplicationType = params.get("DelayReplicationType")
        self.DueTime = params.get("DueTime")
        self.Gtid = params.get("Gtid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartDelayReplicationResponse(AbstractModel):
    """StartDelayReplication response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Delayed replication task ID. This parameter will be returned if `DelayReplicationType` is not `DEFAULT`. It can be used to view the status of the delayed replication task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class StopDBImportJobRequest(AbstractModel):
    """StopDBImportJob request structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID.\n        :type AsyncRequestId: str\n        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDBImportJobResponse(AbstractModel):
    """StopDBImportJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopDelayReplicationRequest(AbstractModel):
    """StopDelayReplication request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDelayReplicationResponse(AbstractModel):
    """StopDelayReplication response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopRollbackRequest(AbstractModel):
    """StopRollback request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the instance whose rollback task is canceled\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRollbackResponse(AbstractModel):
    """StopRollback response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SwitchDBInstanceMasterSlaveRequest(AbstractModel):
    """SwitchDBInstanceMasterSlave request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param DstSlave: Specifies the replica server to switched to. Valid values: `first` (the first replica server), `second` (the second replica server). Default value: `first`. `second` is valid only for a multi-AZ instance.\n        :type DstSlave: str\n        :param ForceSwitch: Whether to force the switch. Valid values: `True`, `False` (default). If this parameter is set to `True`, instance data may be lost during the switch.\n        :type ForceSwitch: bool\n        :param WaitSwitch: Whether to perform the switch during a time window. Valid values: `True`, `False` (default). If `ForceSwitch` is set to `True`, this parameter is invalid.\n        :type WaitSwitch: bool\n        """
        self.InstanceId = None
        self.DstSlave = None
        self.ForceSwitch = None
        self.WaitSwitch = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DstSlave = params.get("DstSlave")
        self.ForceSwitch = params.get("ForceSwitch")
        self.WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstanceMasterSlaveResponse(AbstractModel):
    """SwitchDBInstanceMasterSlave response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task ID\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SwitchDrInstanceToMasterRequest(AbstractModel):
    """SwitchDrInstanceToMaster request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Disaster recovery instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDrInstanceToMasterResponse(AbstractModel):
    """SwitchDrInstanceToMaster response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SwitchForUpgradeRequest(AbstractModel):
    """SwitchForUpgrade request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchForUpgradeResponse(AbstractModel):
    """SwitchForUpgrade response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TableName(AbstractModel):
    """Table name

    """

    def __init__(self):
        """
        :param TableName: Table name\n        :type TableName: str\n        """
        self.TableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePrivilege(AbstractModel):
    """Table permission

    """

    def __init__(self):
        """
        :param Database: Database name\n        :type Database: str\n        :param Table: Table name\n        :type Table: str\n        :param Privileges: Permission information\n        :type Privileges: list of str\n        """
        self.Database = None
        self.Table = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Tag information

    """

    def __init__(self):
        """
        :param TagKey: Tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: list of str\n        """
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
        


class TagInfoItem(AbstractModel):
    """Tag information

    """

    def __init__(self):
        """
        :param TagKey: Tag key
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TagKey: str\n        :param TagValue: Tag value
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TagValue: str\n        """
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
        


class TagInfoUnit(AbstractModel):
    """Tag information unit

    """

    def __init__(self):
        """
        :param TagKey: Tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: str\n        """
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
        


class TagsInfoOfInstance(AbstractModel):
    """Instance tag information

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param Tags: Tag information\n        :type Tags: list of TagInfoUnit\n        """
        self.InstanceId = None
        self.Tags = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetail(AbstractModel):
    """Details of an instance task

    """

    def __init__(self):
        """
        :param Code: Error code.\n        :type Code: int\n        :param Message: Error message.\n        :type Message: str\n        :param JobId: ID of an instance task.\n        :type JobId: int\n        :param Progress: Instance task progress.\n        :type Progress: int\n        :param TaskStatus: Instance task status. Valid values:
"UNDEFINED" - undefined;
"INITIAL" - initializing;
"RUNNING" - running;
"SUCCEED" - succeeded;
"FAILED" - failed;
"KILLED" - terminated;
"REMOVED" - deleted;
"PAUSED" - paused.
"WAITING" - waiting (which can be canceled)\n        :type TaskStatus: str\n        :param TaskType: Instance task type. Valid values:
"ROLLBACK" - rolling back a database;
"SQL OPERATION" - performing an SQL operation;
"IMPORT DATA" - importing data;
"MODIFY PARAM" - setting a parameter;
"INITIAL" - initializing a TencentDB instance;
"REBOOT" - restarting a TencentDB instance;
"OPEN GTID" - enabling GTID of a TencentDB instance;
"UPGRADE RO" - upgrading a read-only instance;
"BATCH ROLLBACK" - rolling back databases in batches;
"UPGRADE MASTER" - upgrading a primary instance;
"DROP TABLES" - dropping a TencentDB table;
"SWITCH DR TO MASTER" - promoting a disaster recovery instance.\n        :type TaskType: str\n        :param StartTime: Instance task start time.\n        :type StartTime: str\n        :param EndTime: Instance task end time.\n        :type EndTime: str\n        :param InstanceIds: ID of an instance associated with a task.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type InstanceIds: list of str\n        :param AsyncRequestId: Async task request ID.\n        :type AsyncRequestId: str\n        """
        self.Code = None
        self.Message = None
        self.JobId = None
        self.Progress = None
        self.TaskStatus = None
        self.TaskType = None
        self.StartTime = None
        self.EndTime = None
        self.InstanceIds = None
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskType = params.get("TaskType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceIds = params.get("InstanceIds")
        self.AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceEngineVersionRequest(AbstractModel):
    """UpgradeDBInstanceEngineVersion request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        :param EngineVersion: Version of primary instance database engine. Value range: 5.6, 5.7\n        :type EngineVersion: str\n        :param WaitSwitch: Mode of switch to a new instance. Value range: 0 (switch immediately), 1 (switch within a time window). Default value: 0. If the value is 1, the switch process will be performed within a time window. Or, you can call the [switching to new instance API](https://intl.cloud.tencent.com/document/product/236/15864?from_cn_redirect=1) to trigger the process.\n        :type WaitSwitch: int\n        :param UpgradeSubversion: Whether to upgrade kernel minor version. Valid values: 1 (upgrade kernel minor version), 0 (upgrade database engine).\n        :type UpgradeSubversion: int\n        """
        self.InstanceId = None
        self.EngineVersion = None
        self.WaitSwitch = None
        self.UpgradeSubversion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EngineVersion = params.get("EngineVersion")
        self.WaitSwitch = params.get("WaitSwitch")
        self.UpgradeSubversion = params.get("UpgradeSubversion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceEngineVersionResponse(AbstractModel):
    """UpgradeDBInstanceEngineVersion response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task ID. The task execution result can be queried using the [async task execution result querying API](https://intl.cloud.tencent.com/document/api/236/20410?from_cn_redirect=1).\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `cdb-c1nl9rpv` or `cdbro-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the ID, whose value is the `InstanceId` value in output parameters.\n        :type InstanceId: str\n        :param Memory: Memory size in MB after upgrade. To ensure that the `Memory` value to be passed in is valid, please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/product/236/17229?from_cn_redirect=1) API to query the specifications of the memory that can be upgraded to.\n        :type Memory: int\n        :param Volume: Disk size in GB after upgrade. To ensure that the `Volume` value to be passed in is valid, please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/product/236/17229?from_cn_redirect=1) API to query the specifications of the disk that can be upgraded to.\n        :type Volume: int\n        :param ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). This parameter can be specified when upgrading primary instances and is meaningless for read-only or disaster recovery instances.\n        :type ProtectMode: int\n        :param DeployMode: Deployment mode. Valid values: 0 (single-AZ), 1 (multi-AZ). Default value: 0. This parameter can be specified when upgrading primary instances and is meaningless for read-only or disaster recovery instances.\n        :type DeployMode: int\n        :param SlaveZone: AZ information of secondary database 1, which is the `Zone` value of the instance by default. This parameter can be specified when upgrading primary instances in multi-AZ mode and is meaningless for read-only or disaster recovery instances. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/product/236/17229?from_cn_redirect=1) API to query the supported AZs.\n        :type SlaveZone: str\n        :param EngineVersion: Version of primary instance database engine. Valid values: 5.5, 5.6, 5.7.\n        :type EngineVersion: str\n        :param WaitSwitch: Mode of switch to new instance. Valid values: 0 (switch immediately), 1 (switch within a time window). Default value: 0. If the value is 1, the switch process will be performed within a time window. Or, you can call the [SwitchForUpgrade](https://intl.cloud.tencent.com/document/product/236/15864?from_cn_redirect=1) API to trigger the process.\n        :type WaitSwitch: int\n        :param BackupZone: AZ information of secondary database 2, which is empty by default. This parameter can be specified when upgrading primary instances and is meaningless for read-only or disaster recovery instances.\n        :type BackupZone: str\n        :param InstanceRole: Instance type. Valid values: master (primary instance), dr (disaster recovery instance), ro (read-only instance). Default value: master.\n        :type InstanceRole: str\n        :param DeviceType: The resource isolation type after the instance is upgraded. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance). If this parameter is left empty, the resource isolation type will be the same as the original one.\n        :type DeviceType: str\n        :param Cpu: The number of CPU cores after the instance is upgraded. If this parameter is left empty, the number of CPU cores will be automatically filled in according to the `Memory` value.\n        :type Cpu: int\n        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.EngineVersion = None
        self.WaitSwitch = None
        self.BackupZone = None
        self.InstanceRole = None
        self.DeviceType = None
        self.Cpu = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        self.EngineVersion = params.get("EngineVersion")
        self.WaitSwitch = params.get("WaitSwitch")
        self.BackupZone = params.get("BackupZone")
        self.InstanceRole = params.get("InstanceRole")
        self.DeviceType = params.get("DeviceType")
        self.Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance response structure.

    """

    def __init__(self):
        """
        :param DealIds: Order ID.\n        :type DealIds: list of str\n        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DealIds = None
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UploadInfo(AbstractModel):
    """File upload description

    """

    def __init__(self):
        """
        :param AllSliceNum: Number of parts of file\n        :type AllSliceNum: int\n        :param CompleteNum: Number of completed parts\n        :type CompleteNum: int\n        """
        self.AllSliceNum = None
        self.CompleteNum = None


    def _deserialize(self, params):
        self.AllSliceNum = params.get("AllSliceNum")
        self.CompleteNum = params.get("CompleteNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneConf(AbstractModel):
    """Multi-AZ information

    """

    def __init__(self):
        """
        :param DeployMode: AZ deployment mode. Value range: 0 (single-AZ), 1 (multi-AZ)\n        :type DeployMode: list of int\n        :param MasterZone: AZ where the primary instance is located\n        :type MasterZone: list of str\n        :param SlaveZone: AZ where salve database 1 is located when the instance is deployed in multi-AZ mode\n        :type SlaveZone: list of str\n        :param BackupZone: AZ where salve database 2 is located when the instance is deployed in multi-AZ mode\n        :type BackupZone: list of str\n        """
        self.DeployMode = None
        self.MasterZone = None
        self.SlaveZone = None
        self.BackupZone = None


    def _deserialize(self, params):
        self.DeployMode = params.get("DeployMode")
        self.MasterZone = params.get("MasterZone")
        self.SlaveZone = params.get("SlaveZone")
        self.BackupZone = params.get("BackupZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneSellConf(AbstractModel):
    """AZ sale configurations

    """

    def __init__(self):
        """
        :param Status: AZ status. Value range: 0 (not available), 1 (available), 2 (purchasable), 3 (not purchasable), 4 (not displayed)\n        :type Status: int\n        :param ZoneName: AZ name\n        :type ZoneName: str\n        :param IsCustom: Whether it is a custom instance type\n        :type IsCustom: bool\n        :param IsSupportDr: Whether disaster recovery is supported\n        :type IsSupportDr: bool\n        :param IsSupportVpc: Whether VPC is supported\n        :type IsSupportVpc: bool\n        :param HourInstanceSaleMaxNum: Maximum purchasable quantity of hourly billed instances\n        :type HourInstanceSaleMaxNum: int\n        :param IsDefaultZone: Whether it is a default AZ\n        :type IsDefaultZone: bool\n        :param IsBm: Whether it is a BM zone\n        :type IsBm: bool\n        :param PayType: Supported billing method. Value range: 0 (monthly subscribed), 1 (hourly), 2 (postpaid)\n        :type PayType: list of str\n        :param ProtectMode: Data replication type. Value range: 0 (async), 1 (semi-sync), 2 (strong sync)\n        :type ProtectMode: list of str\n        :param Zone: AZ name\n        :type Zone: str\n        :param SellType: Array of purchasable instance types\n        :type SellType: list of SellType\n        :param ZoneConf: Multi-AZ information\n        :type ZoneConf: :class:`tencentcloud.cdb.v20170320.models.ZoneConf`\n        :param DrZone: Information of the supported disaster recovery AZ\n        :type DrZone: list of str\n        :param IsSupportRemoteRo: Whether cross-AZ read-only access is supported\n        :type IsSupportRemoteRo: bool\n        :param RemoteRoZone: Information of supported cross-AZ read-only zone
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RemoteRoZone: list of str\n        """
        self.Status = None
        self.ZoneName = None
        self.IsCustom = None
        self.IsSupportDr = None
        self.IsSupportVpc = None
        self.HourInstanceSaleMaxNum = None
        self.IsDefaultZone = None
        self.IsBm = None
        self.PayType = None
        self.ProtectMode = None
        self.Zone = None
        self.SellType = None
        self.ZoneConf = None
        self.DrZone = None
        self.IsSupportRemoteRo = None
        self.RemoteRoZone = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ZoneName = params.get("ZoneName")
        self.IsCustom = params.get("IsCustom")
        self.IsSupportDr = params.get("IsSupportDr")
        self.IsSupportVpc = params.get("IsSupportVpc")
        self.HourInstanceSaleMaxNum = params.get("HourInstanceSaleMaxNum")
        self.IsDefaultZone = params.get("IsDefaultZone")
        self.IsBm = params.get("IsBm")
        self.PayType = params.get("PayType")
        self.ProtectMode = params.get("ProtectMode")
        self.Zone = params.get("Zone")
        if params.get("SellType") is not None:
            self.SellType = []
            for item in params.get("SellType"):
                obj = SellType()
                obj._deserialize(item)
                self.SellType.append(obj)
        if params.get("ZoneConf") is not None:
            self.ZoneConf = ZoneConf()
            self.ZoneConf._deserialize(params.get("ZoneConf"))
        self.DrZone = params.get("DrZone")
        self.IsSupportRemoteRo = params.get("IsSupportRemoteRo")
        self.RemoteRoZone = params.get("RemoteRoZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        