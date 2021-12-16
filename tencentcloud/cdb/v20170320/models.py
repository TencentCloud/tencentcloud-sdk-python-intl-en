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
        r"""
        :param User: New account name
        :type User: str
        :param Host: New account domain name
        :type Host: str
        """
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
        r"""
        :param Notes: Account remarks
        :type Notes: str
        :param Host: Account domain name
        :type Host: str
        :param User: Account name
        :type User: str
        :param ModifyTime: Account information modification time
        :type ModifyTime: str
        :param ModifyPasswordTime: Password modification time
        :type ModifyPasswordTime: str
        :param CreateTime: This parameter is no longer supported.
        :type CreateTime: str
        :param MaxUserConnections: The maximum number of instance connections supported by an account
        :type MaxUserConnections: int
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Monday: Maintenance window on Monday. The format should be 10:00-12:00. You can set multiple time windows on a day. Each time window lasts from half an hour to three hours, and must start and end on the hour or half hour. At least one time window is required in a week. The same rule applies to the following parameters.
        :type Monday: list of str
        :param Tuesday: Maintenance window on Tuesday. At least one time window is required in a week.
        :type Tuesday: list of str
        :param Wednesday: Maintenance window on Wednesday. At least one time window is required in a week.
        :type Wednesday: list of str
        :param Thursday: Maintenance window on Thursday. At least one time window is required in a week.
        :type Thursday: list of str
        :param Friday: Maintenance window on Friday. At least one time window is required in a week.
        :type Friday: list of str
        :param Saturday: Maintenance window on Saturday. At least one time window is required in a week.
        :type Saturday: list of str
        :param Sunday: Maintenance window on Sunday. At least one time window is required in a week.
        :type Sunday: list of str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroupId: Security group ID.
        :type SecurityGroupId: str
        :param InstanceIds: List of instance IDs, which is an array of one or more instance IDs.
        :type InstanceIds: list of str
        :param ForReadonlyInstance: This parameter takes effect only when the IDs of read-only replicas are passed in. If this parameter is set to `False` or left empty, the security group will be bound to the RO groups of these read-only replicas. If this parameter is set to `True`, the security group will be bound to the read-only replicas themselves.
        :type ForReadonlyInstance: bool
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BackupConfig(AbstractModel):
    """Configuration information of ECDB secondary database 2. This field is only applicable to ECDB instances

    """

    def __init__(self):
        r"""
        :param ReplicationMode: Replication mode of secondary database 2. Value range: async, semi-sync
        :type ReplicationMode: str
        :param Zone: Name of the AZ of secondary database 2, such as ap-shanghai-1
        :type Zone: str
        :param Vip: Private IP address of secondary database 2
        :type Vip: str
        :param Vport: Access port of secondary database 2
        :type Vport: int
        """
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
        r"""
        :param Name: Backup filename
        :type Name: str
        :param Size: Backup file size in bytes
        :type Size: int
        :param Date: Backup snapshot time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: Download address
        :type IntranetUrl: str
        :param InternetUrl: Download address
        :type InternetUrl: str
        :param Type: Log type. Valid values: `logical` (logical cold backup), `physical` (physical cold backup).
        :type Type: str
        :param BackupId: Backup subtask ID, which is used when backup files are deleted
        :type BackupId: int
        :param Status: Backup task status. Valid values: `SUCCESS` (backup succeeded), `FAILED` (backup failed), `RUNNING` (backup is in progress).
        :type Status: str
        :param FinishTime: Backup task completion time
        :type FinishTime: str
        :param Creator: (This field will be disused and is thus not recommended) backup creator. Valid values: `SYSTEM` (created by system), `Uin` (initiator's `Uin` value).
        :type Creator: str
        :param StartTime: Backup task start time
        :type StartTime: str
        :param Method: Backup method. Valid values: `full` (full backup), `partial` (partial backup).
        :type Method: str
        :param Way: Backup mode. Valid values: `manual` (manual backup), `automatic` (automatic backup).
        :type Way: str
        :param ManualBackupName: Manual backup alias
        :type ManualBackupName: str
        """
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
        self.ManualBackupName = None


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
        self.ManualBackupName = params.get("ManualBackupName")
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
        r"""
        :param Db: Name of the database to be backed up
        :type Db: str
        :param Table: Name of the table to be backed up. If this parameter is passed in, the specified table in the database will be backed up; otherwise, the database will be backed up.
        :type Table: str
        """
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
        


class BackupLimitVpcItem(AbstractModel):
    """VPCs used to restrict backup download

    """

    def __init__(self):
        r"""
        :param Region: The region where the backup download restrictions take effect. It must be the same as the common request parameter `Region` of the API.
        :type Region: str
        :param VpcList: The list of VPCs used to restrict backup download
        :type VpcList: list of str
        """
        self.Region = None
        self.VpcList = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.VpcList = params.get("VpcList")
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
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param AutoBackupCount: Number of automatic data backups of an instance.
        :type AutoBackupCount: int
        :param AutoBackupVolume: Capacity of automatic data backups of an instance.
        :type AutoBackupVolume: int
        :param ManualBackupCount: Number of manual data backups of an instance.
        :type ManualBackupCount: int
        :param ManualBackupVolume: Capacity of manual data backups of an instance.
        :type ManualBackupVolume: int
        :param DataBackupCount: Total number of data backups of an instance (including automatic backups and manual backups).
        :type DataBackupCount: int
        :param DataBackupVolume: Total capacity of data backups of an instance.
        :type DataBackupVolume: int
        :param BinlogBackupCount: Number of log backups of an instance.
        :type BinlogBackupCount: int
        :param BinlogBackupVolume: Capacity of log backups of an instance.
        :type BinlogBackupVolume: int
        :param BackupVolume: Total capacity of backups of an instance (including data backups and log backups).
        :type BackupVolume: int
        """
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
        r"""
        :param RoGroupId: RO group ID in the format of `cdbrg-c1nl9rpv`.
        :type RoGroupId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BinlogInfo(AbstractModel):
    """Binlog information

    """

    def __init__(self):
        r"""
        :param Name: Binlog backup filename
        :type Name: str
        :param Size: Backup file size in bytes
        :type Size: int
        :param Date: File stored time in the format of 2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: Download address
        :type IntranetUrl: str
        :param InternetUrl: Download address
        :type InternetUrl: str
        :param Type: Log type. Value range: binlog
        :type Type: str
        :param BinlogStartTime: Binlog file start file
        :type BinlogStartTime: str
        :param BinlogFinishTime: Binlog file end time
        :type BinlogFinishTime: str
        """
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
        r"""
        :param SrcInstanceId: ID of the original instance in a clone task
        :type SrcInstanceId: str
        :param DstInstanceId: ID of the cloned instance in a clone task
        :type DstInstanceId: str
        :param CloneJobId: Clone task ID
        :type CloneJobId: int
        :param RollbackStrategy: The policy used in a clone task. Valid values: `timepoint` (roll back to a specific point in time), `backupset` (roll back by using a specific backup file).
        :type RollbackStrategy: str
        :param RollbackTargetTime: The point in time to which the cloned instance will be rolled back
        :type RollbackTargetTime: str
        :param StartTime: Task start time
        :type StartTime: str
        :param EndTime: Task end time
        :type EndTime: str
        :param TaskStatus: Task status. Valid values: `initial`, `running`, `wait_complete`, `success`, `failed`.
        :type TaskStatus: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWanServiceResponse(AbstractModel):
    """CloseWanService response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """Column permission information

    """

    def __init__(self):
        r"""
        :param Database: Database name
        :type Database: str
        :param Table: Table name
        :type Table: str
        :param Column: Column name
        :type Column: str
        :param Privileges: Permission information
        :type Privileges: list of str
        """
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
        r"""
        :param Monday: Time window on Monday in the format of 02:00-06:00
        :type Monday: str
        :param Tuesday: Time window on Tuesday in the format of 02:00-06:00
        :type Tuesday: str
        :param Wednesday: Time window on Wednesday in the format of 02:00-06:00
        :type Wednesday: str
        :param Thursday: Time window on Thursday in the format of 02:00-06:00
        :type Thursday: str
        :param Friday: Time window on Friday in the format of 02:00-06:00
        :type Friday: str
        :param Saturday: Time window on Saturday in the format of 02:00-06:00
        :type Saturday: str
        :param Sunday: Time window on Sunday in the format of 02:00-06:00
        :type Sunday: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Accounts: TencentDB account.
        :type Accounts: list of Account
        :param Password: Password of the new account
        :type Password: str
        :param Description: Remarks
        :type Description: str
        :param MaxUserConnections: Maximum connections of the new account. Default value: `10240`. Maximum value: `10240`.
        :type MaxUserConnections: int
        """
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
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateAuditPolicyRequest(AbstractModel):
    """CreateAuditPolicy request structure.

    """

    def __init__(self):
        r"""
        :param Name: Audit policy name.
        :type Name: str
        :param RuleId: Audit rule ID.
        :type RuleId: str
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param LogExpireDay: Retention period of audit logs. Valid values:
7: seven days (a week);
30: 30 days (a month);
180: 180 days (six months);
365: 365 days (a year);
1095: 1095 days (three years);
1825: 1825 days (five years).
This parameter specifies the retention period (30 days by default) of audit logs, which is valid when you create the first audit policy for an instance. If the instance already has audit policies, this parameter is invalid, but you can use the `ModifyAuditConfig` API to modify the retention period.
        :type LogExpireDay: int
        """
        self.Name = None
        self.RuleId = None
        self.InstanceId = None
        self.LogExpireDay = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RuleId = params.get("RuleId")
        self.InstanceId = params.get("InstanceId")
        self.LogExpireDay = params.get("LogExpireDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditPolicyResponse(AbstractModel):
    """CreateAuditPolicy response structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Audit policy ID.
        :type PolicyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param BackupMethod: Backup method of target instance. Value range: logical (logical cold backup), physical (physical cold backup).
        :type BackupMethod: str
        :param BackupDBTableList: Information of the table to be backed up. If this parameter is not set, the entire instance will be backed up by default. It can be set only in logical backup (i.e., BackupMethod = logical). The specified table must exist; otherwise, backup may fail.
For example, if you want to backup tb1 and tb2 in db1 and the entire db2, you should set the parameter as [{"Db": "db1", "Table": "tb1"}, {"Db": "db1", "Table": "tb2"}, {"Db": "db2"} ].
        :type BackupDBTableList: list of BackupItem
        :param ManualBackupName: Manual backup alias
        :type ManualBackupName: str
        """
        self.InstanceId = None
        self.BackupMethod = None
        self.BackupDBTableList = None
        self.ManualBackupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMethod = params.get("BackupMethod")
        if params.get("BackupDBTableList") is not None:
            self.BackupDBTableList = []
            for item in params.get("BackupDBTableList"):
                obj = BackupItem()
                obj._deserialize(item)
                self.BackupDBTableList.append(obj)
        self.ManualBackupName = params.get("ManualBackupName")
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
        r"""
        :param BackupId: Backup task ID
        :type BackupId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BackupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupId = params.get("BackupId")
        self.RequestId = params.get("RequestId")


class CreateCloneInstanceRequest(AbstractModel):
    """CreateCloneInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ID of the instance to be cloned from
        :type InstanceId: str
        :param SpecifiedRollbackTime: To roll back the cloned instance to a specific point in time, set this parameter to a value in the format of "yyyy-mm-dd hh:mm:ss".
        :type SpecifiedRollbackTime: str
        :param SpecifiedBackupId: To roll back the cloned instance to a specific physical backup file, set this parameter to the ID of the physical backup file. The ID can be obtained by the [DescribeBackups](https://intl.cloud.tencent.com/document/api/236/15842?from_cn_redirect=1) API.
        :type SpecifiedBackupId: int
        :param UniqVpcId: VPC ID, which can be obtained by the [DescribeVpcs](https://intl.cloud.tencent.com/document/api/215/15778?from_cn_redirect=1) API. If this parameter is left empty, the classic network will be used by default.
        :type UniqVpcId: str
        :param UniqSubnetId: VPC subnet ID, which can be obtained by the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API. If `UniqVpcId` is set, `UniqSubnetId` will be required.
        :type UniqSubnetId: str
        :param Memory: Memory of the cloned instance in MB, which should be equal to (by default) or larger than that of the original instance
        :type Memory: int
        :param Volume: Disk capacity of the cloned instance in GB, which should be equal to (by default) or larger than that of the original instance
        :type Volume: int
        :param InstanceName: Name of the cloned instance
        :type InstanceName: str
        :param SecurityGroup: Security group parameter, which can be obtained by the [DescribeProjectSecurityGroups](https://intl.cloud.tencent.com/document/api/236/15850?from_cn_redirect=1) API
        :type SecurityGroup: list of str
        :param ResourceTags: Information of the cloned instance tag
        :type ResourceTags: list of TagInfo
        :param Cpu: The number of CPU cores of the cloned instance. It should be equal to (by default) or larger than that of the original instance.
        :type Cpu: int
        :param ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). Default value: 0.
        :type ProtectMode: int
        :param DeployMode: Multi-AZ or single-AZ. Valid values: 0 (single-AZ), 1 (multi-AZ). Default value: 0.
        :type DeployMode: int
        :param SlaveZone: Availability zone information of replica 1 of the cloned instance, which is the same as the value of `Zone` of the original instance by default
        :type SlaveZone: str
        :param BackupZone: Availability zone information of replica 2 of the cloned instance, 
which is left empty by default. Specify this parameter when cloning a strong sync source instance.
        :type BackupZone: str
        :param DeviceType: Resource isolation type of the clone. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance). Default value: `UNIVERSAL`.
        :type DeviceType: str
        :param InstanceNodes: The number of nodes of the clone. If this parameter is set to `3` or the `BackupZone` parameter is specified, the clone will have three nodes. If this parameter is set to `2` or left empty, the clone will have two nodes.
        :type InstanceNodes: int
        :param DeployGroupId: Placement group ID.
        :type DeployGroupId: str
        :param DryRun: Whether to check the request without creating any instance. Valid values: `true`, `false` (default). After being submitted, the request will be checked to see if it is in correct format and has all required parameters with valid values. An error code is returned if the check failed, and `RequestId` is returned if the check succeeded. After a successful check, no instance will be created if this parameter is set to `true`, whereas an instance will be created and if it is set to `false`.
        :type DryRun: bool
        """
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
        self.DeployGroupId = None
        self.DryRun = None


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
        self.DeployGroupId = params.get("DeployGroupId")
        self.DryRun = params.get("DryRun")
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
        r"""
        :param AsyncRequestId: LimitAsync task request ID, which can be used to query the execution result of an async task
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateDBImportJobRequest(AbstractModel):
    """CreateDBImportJob request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param FileName: Filename. The file must be a .sql file uploaded to Tencent Cloud.
        :type FileName: str
        :param User: TencentDB username
        :type User: str
        :param Password: Password of a TencentDB instance user account
        :type Password: str
        :param DbName: Name of the target database. If this parameter is not passed in, no database is specified.
        :type DbName: str
        """
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
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour request structure.

    """

    def __init__(self):
        r"""
        :param GoodsNum: Number of instances. Value range: 1-100. Default value: 1.
        :type GoodsNum: int
        :param Memory: Instance memory size in MB. Please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported memory specifications.
        :type Memory: int
        :param Volume: Instance disk size in GB. Please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported disk specifications.
        :type Volume: int
        :param EngineVersion: MySQL version. Valid values: `5.5`, `5.6`, `5.7`, `8.0`. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported versions.
        :type EngineVersion: str
        :param UniqVpcId: VPC ID. If this parameter is not passed in, the basic network will be selected by default. Please use the [DescribeVpcs](https://intl.cloud.tencent.com/document/api/215/15778?from_cn_redirect=1) API to query the VPCs.
        :type UniqVpcId: str
        :param UniqSubnetId: VPC subnet ID. If `UniqVpcId` is set, then `UniqSubnetId` will be required. Please use the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API to query the subnet lists.
        :type UniqSubnetId: str
        :param ProjectId: Project ID. If this is left empty, the default project will be used.
        :type ProjectId: int
        :param Zone: AZ information. By default, the system will automatically select an AZ. Please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported AZs.
        :type Zone: str
        :param MasterInstanceId: Instance ID, which is required and the same as the primary instance ID when purchasing read-only or disaster recovery instances. Please use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the instance IDs.
        :type MasterInstanceId: str
        :param InstanceRole: Instance type. Valid values: master (primary instance), dr (disaster recovery instance), ro (read-only instance). Default value: master.
        :type InstanceRole: str
        :param MasterRegion: AZ information of the primary instance, which is required for purchasing disaster recovery instances.
        :type MasterRegion: str
        :param Port: Custom port. Value range: [1024-65535].
        :type Port: int
        :param Password: Sets the root account password. Rule: the password can contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special symbols (_+-&=!@#$%^*()). This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.
        :type Password: str
        :param ParamList: List of parameters in the format of `ParamList.0.Name=auto_increment&ParamList.0.Value=1`. You can use the [DescribeDefaultParams](https://intl.cloud.tencent.com/document/api/236/32662?from_cn_redirect=1) API to query the configurable parameters.
        :type ParamList: list of ParamInfo
        :param ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). Default value: 0. This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.
        :type ProtectMode: int
        :param DeployMode: Multi-AZ. Valid value: 0 (single-AZ), 1 (multi-AZ). Default value: 0. This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.
        :type DeployMode: int
        :param SlaveZone: AZ information of secondary database 1, which is the `Zone` value by default. This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.
        :type SlaveZone: str
        :param BackupZone: The availability zone information of Replica 2, which is left empty by default. Specify this parameter when purchasing a source instance in the one-source-two-replica architecture.
        :type BackupZone: str
        :param SecurityGroup: Security group parameter. You can use the [DescribeProjectSecurityGroups](https://intl.cloud.tencent.com/document/api/236/15850?from_cn_redirect=1) API to query the security group details of a project.
        :type SecurityGroup: list of str
        :param RoGroup: Read-only instance information. This parameter must be passed in when purchasing read-only instances.
        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`
        :param AutoRenewFlag: This field is meaningless when purchasing pay-as-you-go instances.
        :type AutoRenewFlag: int
        :param InstanceName: Instance name.
        :type InstanceName: str
        :param ResourceTags: Instance tag information.
        :type ResourceTags: list of TagInfo
        :param DeployGroupId: Placement group ID.
        :type DeployGroupId: str
        :param ClientToken: A string that is used to guarantee the idempotency of the request, which is generated by the user and must be unique in each request on the same day. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param DeviceType: Instance resource isolation type. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance). Default value: `UNIVERSAL`.
        :type DeviceType: str
        :param ParamTemplateId: Parameter template ID.
        :type ParamTemplateId: int
        :param AlarmPolicyList: The array of alarm policy IDs.
        :type AlarmPolicyList: list of int
        :param InstanceNodes: The number of nodes of the instance. To purchase a read-only replica or a basic instance, set this parameter to `1` or leave it empty. To purchase a three-node instance, set this parameter to `3` or specify the `BackupZone` parameter. If the instance to be purchased is a source instance and both `BackupZone` and this parameter are left empty, the value `2` will be used, which indicates the source instance will have two nodes.
        :type InstanceNodes: int
        :param Cpu: The number of CPU cores of the instance. If this parameter is left empty, the number of CPU cores depends on the `Memory` value.
        :type Cpu: int
        :param AutoSyncFlag: Whether to automatically start disaster recovery synchronization. This parameter takes effect only for disaster recovery instances. Valid values: `0` (no), `1` (yes).
        :type AutoSyncFlag: int
        :param CageId: Financial cage ID.
        :type CageId: str
        :param AlarmPolicyIdList: The array of alarm policy names, such as ["policy-uyoee9wg"]. If the `AlarmPolicyList` parameter is specified, this parameter is invalid.
        :type AlarmPolicyIdList: list of str
        :param DryRun: Whether to check the request without creating any instance. Valid values: `true`, `false` (default). After being submitted, the request will be checked to see if it is in correct format and has all required parameters with valid values. An error code is returned if the check failed, and `RequestId` is returned if the check succeeded. After a successful check, no instance will be created if this parameter is set to `true`, whereas an instance will be created and if it is set to `false`.
        :type DryRun: bool
        """
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
        self.CageId = None
        self.AlarmPolicyIdList = None
        self.DryRun = None


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
        self.CageId = params.get("CageId")
        self.AlarmPolicyIdList = params.get("AlarmPolicyIdList")
        self.DryRun = params.get("DryRun")
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
        r"""
        :param DealIds: Short order ID.
        :type DealIds: list of str
        :param InstanceIds: Instance ID list
        :type InstanceIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param DeployGroupName: Name of a placement group, which can contain up to 60 characters.
        :type DeployGroupName: str
        :param Description: Description of a placement group, which can contain up to 200 characters.
        :type Description: str
        :param Affinity: Affinity policy of placement group. Currently, the value of this parameter can only be 1. Policy 1 indicates the upper limit of instances on one physical machine.
        :type Affinity: list of int
        :param LimitNum: Upper limit of instances on one physical machine as defined in affinity policy 1 of placement group.
        :type LimitNum: int
        :param DevClass: Model attribute of placement group. Valid values: SH12+SH02, TS85.
        :type DevClass: list of str
        """
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
        r"""
        :param DeployGroupId: Placement group ID.
        :type DeployGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DeployGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param Name: Parameter template name.
        :type Name: str
        :param Description: Parameter template description.
        :type Description: str
        :param EngineVersion: MySQL version number.
        :type EngineVersion: str
        :param TemplateId: Source parameter template ID.
        :type TemplateId: int
        :param ParamList: List of parameters.
        :type ParamList: list of Parameter
        """
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
        r"""
        :param TemplateId: Parameter template ID.
        :type TemplateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateRoInstanceIpRequest(AbstractModel):
    """CreateRoInstanceIp request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Read-only instance ID in the format of "cdbro-3i70uj0k". Its value is the same as the read-only instance ID in the TencentDB Console.
        :type InstanceId: str
        :param UniqSubnetId: Subnet descriptor, such as "subnet-1typ0s7d".
        :type UniqSubnetId: str
        :param UniqVpcId: VPC descriptor, such as "vpc-a23yt67j". If this field is passed in, `UniqSubnetId` will be required.
        :type UniqVpcId: str
        """
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
        r"""
        :param RoVpcId: VPC ID of the read-only instance.
        :type RoVpcId: int
        :param RoSubnetId: Subnet ID of the read-only instance.
        :type RoSubnetId: int
        :param RoVip: Private IP address of the read-only instance.
        :type RoVip: str
        :param RoVport: Private port number of the read-only instance.
        :type RoVport: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param SwitchTime: Switch time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-09-03 01:34:31
        :type SwitchTime: str
        :param SwitchType: Switch type. Value range: TRANSFER (data migration), MASTER2SLAVE (primary/secondary switch), RECOVERY (primary/secondary recovery)
        :type SwitchType: str
        """
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
        


class DatabasePrivilege(AbstractModel):
    """Database permission

    """

    def __init__(self):
        r"""
        :param Privileges: Permission information
        :type Privileges: list of str
        :param Database: Database name
        :type Database: str
        """
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
        r"""
        :param DatabaseName: Database name
        :type DatabaseName: str
        :param CharacterSet: Character set
        :type CharacterSet: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Accounts: TencentDB account.
        :type Accounts: list of Account
        """
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
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param BackupId: Backup task ID, which is the task ID returned by the [TencentDB instance backup creating API](https://intl.cloud.tencent.com/document/api/236/15844?from_cn_redirect=1).
        :type BackupId: int
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeployGroupsRequest(AbstractModel):
    """DeleteDeployGroups request structure.

    """

    def __init__(self):
        r"""
        :param DeployGroupIds: List of IDs of placement groups to be deleted.
        :type DeployGroupIds: list of str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Parameter template ID.
        :type TemplateId: int
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTimeWindowRequest(AbstractModel):
    """DeleteTimeWindow request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimeWindowResponse(AbstractModel):
    """DeleteTimeWindow response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeployGroupInfo(AbstractModel):
    """Placement group information

    """

    def __init__(self):
        r"""
        :param DeployGroupId: ID of a placement group.
        :type DeployGroupId: str
        :param DeployGroupName: Name of a placement group.
        :type DeployGroupName: str
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param Quota: Instance quota of placement group, indicating the maximum number of instances that can be placed in one placement group.
        :type Quota: int
        :param Affinity: Affinity policy of placement group. Currently, only policy 1 is supported, indicating to distribute instances across physical machines.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Affinity: str
        :param LimitNum: Upper limit of instances in one placement group on one physical machine as defined in affinity policy 1 of placement group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LimitNum: int
        :param Description: Placement group details.
        :type Description: str
        :param DevClass: Physical model attribute of placement group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DevClass: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param User: Database user account.
        :type User: str
        :param Host: Database account domain name.
        :type Host: str
        """
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
        r"""
        :param GlobalPrivileges: Array of global permissions.
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: Array of database permissions.
        :type DatabasePrivileges: list of DatabasePrivilege
        :param TablePrivileges: Array of table permissions in the database.
        :type TablePrivileges: list of TablePrivilege
        :param ColumnPrivileges: Array of column permissions in the table.
        :type ColumnPrivileges: list of ColumnPrivilege
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Offset: Record offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned for a single request. Value range: 1-100. Default value: 20.
        :type Limit: int
        :param AccountRegexp: Regular expression for matching account names, which complies with the rules at MySQL official website.
        :type AccountRegexp: str
        """
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
        r"""
        :param TotalCount: Number of eligible accounts.
        :type TotalCount: int
        :param Items: Details of eligible accounts.
        :type Items: list of AccountInfo
        :param MaxUserConnections: The maximum number of instance connections (set by the MySQL parameter `max_connections`)
        :type MaxUserConnections: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param AsyncRequestId: Async task request ID.
        :type AsyncRequestId: str
        """
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
        r"""
        :param Status: Task execution result. Valid values: INITIAL, RUNNING, SUCCESS, FAILED, KILLED, REMOVED, PAUSED.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Info: Task execution information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Info: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig response structure.

    """

    def __init__(self):
        r"""
        :param StartTimeMin: Earliest start time point of automatic backup, such as 2 (for 2:00 AM). (This field has been disused. You are recommended to use the `BackupTimeWindow` field)
        :type StartTimeMin: int
        :param StartTimeMax: Latest start time point of automatic backup, such as 6 (for 6:00 AM). (This field has been disused. You are recommended to use the `BackupTimeWindow` field)
        :type StartTimeMax: int
        :param BackupExpireDays: Backup file retention period in days.
        :type BackupExpireDays: int
        :param BackupMethod: Backup mode. Value range: physical, logical
        :type BackupMethod: str
        :param BinlogExpireDays: Binlog file retention period in days.
        :type BinlogExpireDays: int
        :param BackupTimeWindow: Time window for automatic instance backup.
        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    """DescribeBackupDownloadRestriction request structure.

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    """DescribeBackupDownloadRestriction response structure.

    """

    def __init__(self):
        r"""
        :param LimitType: Valid values: `NoLimit` (backups can be downloaded over both private and public networks with any IPs), `LimitOnlyIntranet` (backups can be downloaded over the private network with any private IPs), `Customize` (backups can be downloaded over specified VPCs with specified IPs). The `LimitVpc` and `LimitIp` parameters are valid only when this parameter is set to `Customize`.
        :type LimitType: str
        :param VpcComparisonSymbol: Valid value: `In` (backups can only be downloaded over the VPCs specified in `LimitVpc`).
        :type VpcComparisonSymbol: str
        :param IpComparisonSymbol: Valid values: `In` (backups can only be downloaded with the IPs specified in `LimitIp`), `NotIn` (backups cannot be downloaded with the IPs specified in `LimitIp`).
        :type IpComparisonSymbol: str
        :param LimitVpc: VPCs used to restrict backup download.
        :type LimitVpc: list of BackupLimitVpcItem
        :param LimitIp: IPs used to restrict backup download.
        :type LimitIp: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LimitType = None
        self.VpcComparisonSymbol = None
        self.IpComparisonSymbol = None
        self.LimitVpc = None
        self.LimitIp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LimitType = params.get("LimitType")
        self.VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self.IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self.LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self.LimitVpc.append(obj)
        self.LimitIp = params.get("LimitIp")
        self.RequestId = params.get("RequestId")


class DescribeBackupOverviewRequest(AbstractModel):
    """DescribeBackupOverview request structure.

    """

    def __init__(self):
        r"""
        :param Product: TencentDB product type to be queried. Currently, only `mysql` is supported.
        :type Product: str
        """
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
        r"""
        :param BackupCount: Total number of backups of a user in the current region (including data backups and log backups).
        :type BackupCount: int
        :param BackupVolume: Total capacity of backups of a user in the current region.
        :type BackupVolume: int
        :param BillingVolume: Paid capacity of backups of a user in the current region, i.e., capacity that exceeds the free tier.
        :type BillingVolume: int
        :param FreeVolume: Backup capacity in the free tier of a user in the current region.
        :type FreeVolume: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Product: TencentDB product type to be queried. Currently, only `mysql` is supported.
        :type Product: str
        :param Offset: Pagination offset.
        :type Offset: int
        :param Limit: Paginated query limit. Default value: 20.
        :type Limit: int
        :param OrderBy: Sorting criterion. Valid values: BackupVolume (backup capacity), DataBackupVolume (data backup capacity), BinlogBackupVolume (log backup capacity), AutoBackupVolume (automatic backup capacity), ManualBackupVolume (manual backup capacity).
        :type OrderBy: str
        :param OrderDirection: Sorting order. Valid values: ASC (ascending), DESC (descending).
        :type OrderDirection: str
        """
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
        r"""
        :param Items: Statistical items of instance backup.
        :type Items: list of BackupSummaryItem
        :param TotalCount: Total number of instance backups.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Offset: Offset. Minimum value: 0.
        :type Offset: int
        :param Limit: Number of entries per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        """
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
        r"""
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param Items: Details of eligible backups.
        :type Items: list of BackupInfo
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
                obj = BackupInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBinlogBackupOverviewRequest(AbstractModel):
    """DescribeBinlogBackupOverview request structure.

    """

    def __init__(self):
        r"""
        :param Product: TencentDB product type to be queried. Currently, only `mysql` is supported.
        :type Product: str
        """
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
        r"""
        :param BinlogBackupVolume: Total capacity of log backups in bytes.
        :type BinlogBackupVolume: int
        :param BinlogBackupCount: Total number of log backups.
        :type BinlogBackupCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Offset: Offset. Minimum value: 0.
        :type Offset: int
        :param Limit: Number of entries per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        """
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
        r"""
        :param TotalCount: Number of eligible log files.
        :type TotalCount: int
        :param Items: Number of eligible binlog files.
        :type Items: list of BinlogInfo
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
                obj = BinlogInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloneListRequest(AbstractModel):
    """DescribeCloneList request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ID of the original instance. This parameter is used to query the clone task list of a specific original instance.
        :type InstanceId: str
        :param Offset: Paginated query offset. Default value: `0`.
        :type Offset: int
        :param Limit: Number of results per page. Default value: `20`.
        :type Limit: int
        """
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
        r"""
        :param TotalCount: The number of results which meet the conditions
        :type TotalCount: int
        :param Items: Clone task list
        :type Items: list of CloneItem
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
                obj = CloneItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBImportRecordsRequest(AbstractModel):
    """DescribeDBImportRecords request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param StartTime: Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-01-01 00:00:01.
        :type StartTime: str
        :param EndTime: End time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-01-01 23:59:59.
        :type EndTime: str
        :param Offset: Pagination parameter indicating the offset. Default value: 0.
        :type Offset: int
        :param Limit: Pagination parameter indicating the number of results to be returned for a single request. Value range: 1-100. Default value: 20.
        :type Limit: int
        """
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
        r"""
        :param TotalCount: Number of eligible import task operation logs.
        :type TotalCount: int
        :param Items: List of import operation records.
        :type Items: list of ImportRecord
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
                obj = ImportRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceCharsetRequest(AbstractModel):
    """DescribeDBInstanceCharset request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceCharsetResponse(AbstractModel):
    """DescribeDBInstanceCharset response structure.

    """

    def __init__(self):
        r"""
        :param Charset: Default character set of the instance, such as "latin1" and "utf8".
        :type Charset: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Charset = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Charset = params.get("Charset")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceConfigRequest(AbstractModel):
    """DescribeDBInstanceConfig request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceConfigResponse(AbstractModel):
    """DescribeDBInstanceConfig response structure.

    """

    def __init__(self):
        r"""
        :param ProtectMode: Data protection mode of the primary instance. Value range: 0 (async replication), 1 (semi-sync replication), 2 (strong sync replication).
        :type ProtectMode: int
        :param DeployMode: Master instance deployment mode. Value range: 0 (single-AZ), 1 (multi-AZ)
        :type DeployMode: int
        :param Zone: Instance AZ information in the format of "ap-shanghai-1".
        :type Zone: str
        :param SlaveConfig: Configurations of the replica node
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SlaveConfig: :class:`tencentcloud.cdb.v20170320.models.SlaveConfig`
        :param BackupConfig: Configurations of the second replica node of a strong-sync instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type BackupConfig: :class:`tencentcloud.cdb.v20170320.models.BackupConfig`
        :param Switched: This parameter is only available for multi-AZ instances. It indicates whether the source AZ is the same as the one specified upon purchase. `true`: not the same, `false`: the same.
        :type Switched: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceGTIDResponse(AbstractModel):
    """DescribeDBInstanceGTID response structure.

    """

    def __init__(self):
        r"""
        :param IsGTIDOpen: GTID enablement flag. Value range: 0 (not enabled), 1 (enabled).
        :type IsGTIDOpen: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsGTIDOpen = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsGTIDOpen = params.get("IsGTIDOpen")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceInfoRequest(AbstractModel):
    """DescribeDBInstanceInfo request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceInfoResponse(AbstractModel):
    """DescribeDBInstanceInfo response structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param InstanceName: Instance name.
        :type InstanceName: str
        :param Encryption: Whether encryption is enabled. YES: enabled, NO: not enabled.
        :type Encryption: str
        :param KeyId: Encryption key ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param KeyRegion: Key region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyRegion: str
        :param DefaultKmsRegion: The default region of the KMS service currently used by the TencentDB backend service.
Note: this field may return `null`, indicating that no valid value can be found.
        :type DefaultKmsRegion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        """
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
        r"""
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param Items: Returned parameter information.
        :type Items: list of InstanceRebootTime
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
                obj = InstanceRebootTime()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param ProjectId: Project ID.
        :type ProjectId: int
        :param InstanceTypes: Instance type. Value range: 1 (primary), 2 (disaster recovery), 3 (read-only).
        :type InstanceTypes: list of int non-negative
        :param Vips: Private IP address of the instance.
        :type Vips: list of str
        :param Status: Instance status. Value range: <br>0 - creating <br>1 - running <br>4 - isolating <br>5 - isolated (the instance can be restored and started in the recycle bin)
        :type Status: list of int non-negative
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned for a single request. Default value: 20. Maximum value: 2,000.
        :type Limit: int
        :param SecurityGroupId: Security group ID. When it is used as a filter, the `WithSecurityGroup` parameter should be set to 1.
        :type SecurityGroupId: str
        :param PayTypes: Billing method. Value range: 0 (monthly subscribed), 1 (hourly).
        :type PayTypes: list of int non-negative
        :param InstanceNames: Instance name.
        :type InstanceNames: list of str
        :param TaskStatus: Instance task status. Valid values: <br>0 - no task <br>1 - upgrading <br>2 - importing data <br>3 - enabling secondary instance access <br>4 - enabling public network access <br>5 - batch operation in progress <br>6 - rolling back <br>7 - disabling public network access <br>8 - modifying password <br>9 - renaming instance <br>10 - restarting <br>12 - migrating self-built database <br>13 - dropping tables <br>14 - Disaster recovery instance creating sync task <br>15 - waiting for switch <br>16 - switching <br>17 - upgrade and switch completed <br>19 - parameter settings to be executed
        :type TaskStatus: list of int non-negative
        :param EngineVersions: Version of the instance database engine. Value range: 5.1, 5.5, 5.6, 5.7.
        :type EngineVersions: list of str
        :param VpcIds: VPC ID.
        :type VpcIds: list of int non-negative
        :param ZoneIds: AZ ID.
        :type ZoneIds: list of int non-negative
        :param SubnetIds: Subnet ID.
        :type SubnetIds: list of int non-negative
        :param CdbErrors: Lock flag.
        :type CdbErrors: list of int
        :param OrderBy: Sort by field of the returned result set. Currently, supported values include "InstanceId", "InstanceName", "CreateTime", and "DeadlineTime".
        :type OrderBy: str
        :param OrderDirection: Sorting method of the returned result set. Currently, "ASC" or "DESC" is supported.
        :type OrderDirection: str
        :param WithSecurityGroup: Whether security group ID is used as a filter
        :type WithSecurityGroup: int
        :param WithExCluster: Whether dedicated cluster details are included. Value range: 0 (not included), 1 (included)
        :type WithExCluster: int
        :param ExClusterId: Exclusive cluster ID.
        :type ExClusterId: str
        :param InstanceIds: Instance ID.
        :type InstanceIds: list of str
        :param InitFlag: Initialization flag. Value range: 0 (not initialized), 1 (initialized).
        :type InitFlag: int
        :param WithDr: Whether instances corresponding to the disaster recovery relationship are included. Valid values: 0 (not included), 1 (included). Default value: 1. If a primary instance is pulled, the data of the disaster recovery relationship will be in the `DrInfo` field. If a disaster recovery instance is pulled, the data of the disaster recovery relationship will be in the `MasterInfo` field. The disaster recovery relationship contains only partial basic data. To get the detailed data, you need to call an API to pull it.
        :type WithDr: int
        :param WithRo: Whether read-only instances are included. Valid values: 0 (not included), 1 (included). Default value: 1.
        :type WithRo: int
        :param WithMaster: Whether primary instances are included. Valid values: 0 (not included), 1 (included). Default value: 1.
        :type WithMaster: int
        :param DeployGroupIds: Placement group ID list.
        :type DeployGroupIds: list of str
        :param TagKeysForSearch: Whether to use the tag key as a filter condition
        :type TagKeysForSearch: list of str
        :param CageIds: Financial cage IDs.
        :type CageIds: list of str
        """
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
        self.CageIds = None


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
        self.CageIds = params.get("CageIds")
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
        r"""
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param Items: Instance details.
        :type Items: list of InstanceInfo
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
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param ForReadonlyInstance: This parameter takes effect only when the ID of read-only replica is passed in. If this parameter is set to `False` or left empty, the security groups bound with the RO group of the read-only replica will be queried. If this parameter is set to `True`, the security groups bound with the read-only replica itself will be queried.
        :type ForReadonlyInstance: bool
        """
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
        r"""
        :param Groups: Security group details.
        :type Groups: list of SecurityGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Offset: Pagination offset.
        :type Offset: int
        :param Limit: Number of entries per page. Value range: 1-2,000. Default value: 50.
        :type Limit: int
        """
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
        r"""
        :param TotalCount: Number of instance switches.
        :type TotalCount: int
        :param Items: Details of instance switches.
        :type Items: list of DBSwitchInfo
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
        r"""
        :param TotalCount: Number of configurations in purchasable regions
        :type TotalCount: int
        :param Items: Details of configurations in purchasable regions
        :type Items: list of RegionSellConf
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
                obj = RegionSellConf()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDataBackupOverviewRequest(AbstractModel):
    """DescribeDataBackupOverview request structure.

    """

    def __init__(self):
        r"""
        :param Product: TencentDB product type to be queried. Currently, only `mysql` is supported.
        :type Product: str
        """
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
        r"""
        :param DataBackupVolume: Total capacity of data backups in bytes in the current region (including automatic backups and manual backups).
        :type DataBackupVolume: int
        :param DataBackupCount: Total number of data backups in the current region.
        :type DataBackupCount: int
        :param AutoBackupVolume: Total capacity of automatic backups in the current region.
        :type AutoBackupVolume: int
        :param AutoBackupCount: Total number of automatic backups in the current region.
        :type AutoBackupCount: int
        :param ManualBackupVolume: Total capacity of manual backups in the current region.
        :type ManualBackupVolume: int
        :param ManualBackupCount: Total number of manual backups in the current region.
        :type ManualBackupCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Offset: Offset. Minimum value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned for a single request. Value range: 1-100. Maximum value: 20.
        :type Limit: int
        :param DatabaseRegexp: Regular expression for matching database names.
        :type DatabaseRegexp: str
        """
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
        r"""
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param Items: Information of an instance.
        :type Items: list of str
        :param DatabaseList: Database name and character set
        :type DatabaseList: list of DatabasesWithCharacterLists
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param EngineVersion: MySQL version. Currently, the supported versions are ["5.1", "5.5", "5.6", "5.7"].
        :type EngineVersion: str
        """
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
        r"""
        :param TotalCount: Number of parameters
        :type TotalCount: int
        :param Items: Parameter details.
        :type Items: list of ParameterDetail
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
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeployGroupListRequest(AbstractModel):
    """DescribeDeployGroupList request structure.

    """

    def __init__(self):
        r"""
        :param DeployGroupId: ID of a placement group.
        :type DeployGroupId: str
        :param DeployGroupName: Name of a placement group.
        :type DeployGroupName: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
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
        r"""
        :param Total: Number of eligible entries.
        :type Total: int
        :param Items: List of returned results.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of DeployGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Count: This parameter is used to return the monitoring data of Count 5-minute time periods on the day. Value range: 1-288. If this parameter is not passed in, all monitoring data in a 5-minute granularity on the day will be returned by default.
        :type Count: int
        """
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
        r"""
        :param Cpu: CPU monitoring data of the instance
        :type Cpu: :class:`tencentcloud.cdb.v20170320.models.DeviceCpuInfo`
        :param Mem: Memory monitoring data of the instance
        :type Mem: :class:`tencentcloud.cdb.v20170320.models.DeviceMemInfo`
        :param Net: Network monitoring data of the instance
        :type Net: :class:`tencentcloud.cdb.v20170320.models.DeviceNetInfo`
        :param Disk: Disk monitoring data of the instance
        :type Disk: :class:`tencentcloud.cdb.v20170320.models.DeviceDiskInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param StartTime: Start timestamp.
        :type StartTime: int
        :param EndTime: End timestamp.
        :type EndTime: int
        :param KeyWords: List of keywords to match. Up to 15 keywords are supported.
        :type KeyWords: list of str
        :param Limit: The number of results per page in paginated queries. Default value: 100. Maximum value: 400.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param InstType: This parameter is valid only for source or disaster recovery instances. Valid value: `slave`, which indicates pulling logs from the replica.
        :type InstType: str
        """
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
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param Items: Returned result.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Items: list of ErrlogItem
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
                obj = ErrlogItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param Offset: Pagination offset.
        :type Offset: int
        :param Limit: Number of entries per page.
        :type Limit: int
        """
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
        r"""
        :param TotalCount: Number of eligible records.
        :type TotalCount: int
        :param Items: Parameter modification records.
        :type Items: list of ParamRecord
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
                obj = ParamRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of instance parameters.
        :type TotalCount: int
        :param Items: Parameter details.
        :type Items: list of ParameterDetail
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
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    """DescribeParamTemplateInfo request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Parameter template ID.
        :type TemplateId: int
        """
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
        r"""
        :param TemplateId: Parameter template ID.
        :type TemplateId: int
        :param Name: Parameter template name.
        :type Name: str
        :param EngineVersion: Database engine version specified in the parameter template
        :type EngineVersion: str
        :param TotalCount: Number of parameters in the parameter template
        :type TotalCount: int
        :param Items: Parameter details
        :type Items: list of ParameterDetail
        :param Description: Parameter template description
        :type Description: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param TotalCount: Number of parameter templates of the user.
        :type TotalCount: int
        :param Items: Parameter template details.
        :type Items: list of ParamTemplateInfo
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
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param ProjectId: Project ID.
        :type ProjectId: int
        """
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
        r"""
        :param Groups: Security group details.
        :type Groups: list of SecurityGroup
        :param TotalCount: Number of security group rules
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of `cdb-c1nl9rpv` or `cdb-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoGroupsResponse(AbstractModel):
    """DescribeRoGroups response structure.

    """

    def __init__(self):
        r"""
        :param RoGroups: RO group information array. An instance can be associated with multiple RO groups.
        :type RoGroups: list of RoGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param RoInstanceId: Read-only instance ID in the format of "cdbro-c1nl9rpv". Its value is the same as the instance ID in the TencentDB Console. This parameter and the `MasterInstanceId` parameter cannot both be empty.
        :type RoInstanceId: str
        :param MasterInstanceId: Primary instance ID in the format of "cdbro-c1nl9rpv". Its value is the same as the instance ID in the TencentDB Console. This parameter and the `RoInstanceId` parameter cannot both be empty. Note: when the parameters are passed in with `RoInstanceId`, the return value refers to the minimum specification to which a read-only instance can be upgraded; when the parameters are passed in with `MasterInstanceId` but without `RoInstanceId`, the return value refers to the minimum purchasable specification for a read-only instance.
        :type MasterInstanceId: str
        """
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
        r"""
        :param Memory: Memory size in MB.
        :type Memory: int
        :param Volume: Disk size in GB.
        :type Volume: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceIds: Instance ID list. An instance ID is in the format of cdb-c1nl9rpv, which is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        """
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
        r"""
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param Items: Returned parameter information.
        :type Items: list of InstanceRollbackRangeTime
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
                obj = InstanceRollbackRangeTime()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackTaskDetailRequest(AbstractModel):
    """DescribeRollbackTaskDetail request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID, which is the same as the instance ID displayed in the TencentDB Console. You can use the [DescribeDBInstances API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID.
        :type InstanceId: str
        :param AsyncRequestId: Async task ID.
        :type AsyncRequestId: str
        :param Limit: Pagination parameter, i.e., the number of entries to be returned for a single request. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Pagination offset. Default value: 0.
        :type Offset: int
        """
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
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param Items: Rollback task details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Items: list of RollbackTask
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
                obj = RollbackTask()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogDataRequest(AbstractModel):
    """DescribeSlowLogData request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param StartTime: Start timestamp.
        :type StartTime: int
        :param EndTime: End timestamp.
        :type EndTime: int
        :param UserHosts: Client `Host` list.
        :type UserHosts: list of str
        :param UserNames: Client username list.
        :type UserNames: list of str
        :param DataBases: Accessed database list.
        :type DataBases: list of str
        :param SortBy: Sort by field. Valid values: Timestamp, QueryTime, LockTime, RowsExamined, RowsSent.
        :type SortBy: str
        :param OrderBy: Sorting order. Valid values: ASC (ascending), DESC (descending).
        :type OrderBy: str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: The number of results per page in paginated queries. Default value: 100. Maximum value: 400.
        :type Limit: int
        :param InstType: This parameter is valid only for source or disaster recovery instances. Valid value: `slave`, which indicates pulling logs from the replica.
        :type InstType: str
        """
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
        r"""
        :param TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param Items: Queried results.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Items: list of SlowLogItem
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
                obj = SlowLogItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Offset: Offset. Minimum value: 0.
        :type Offset: int
        :param Limit: Number of entries per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        """
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
        r"""
        :param TotalCount: Number of eligible slow logs.
        :type TotalCount: int
        :param Items: Details of eligible slow logs.
        :type Items: list of SlowLogInfo
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
                obj = SlowLogInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSupportedPrivilegesRequest(AbstractModel):
    """DescribeSupportedPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupportedPrivilegesResponse(AbstractModel):
    """DescribeSupportedPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param GlobalSupportedPrivileges: Global permissions supported by the instance
        :type GlobalSupportedPrivileges: list of str
        :param DatabaseSupportedPrivileges: Database permissions supported by the instance.
        :type DatabaseSupportedPrivileges: list of str
        :param TableSupportedPrivileges: Table permissions supported by the instance.
        :type TableSupportedPrivileges: list of str
        :param ColumnSupportedPrivileges: Column permissions supported by the instance.
        :type ColumnSupportedPrivileges: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Database: Database name.
        :type Database: str
        :param Offset: Record offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned for a single request. Default value: 20. Maximum value: 2,000.
        :type Limit: int
        :param TableRegexp: Regular expression for matching table names, which complies with the rules at MySQL's official website
        :type TableRegexp: str
        """
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
        r"""
        :param TotalCount: Number of eligible tables.
        :type TotalCount: int
        :param Items: Information of a table.
        :type Items: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceIds: List of instances.
        :type InstanceIds: list of str
        :param Offset: Pagination offset.
        :type Offset: int
        :param Limit: Number of entries per page.
        :type Limit: int
        """
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
        r"""
        :param Offset: Pagination offset.
        :type Offset: int
        :param Limit: Number of entries per page.
        :type Limit: int
        :param Rows: Instance tag information.
        :type Rows: list of TagsInfoOfInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param AsyncRequestId: ID of an async task request, i.e., `AsyncRequestId` returned by relevant TencentDB operations.
        :type AsyncRequestId: str
        :param TaskTypes: Task type. If no value is passed in, all task types will be queried. Valid values:
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
13 - promoting a disaster recovery instance.
        :type TaskTypes: list of int
        :param TaskStatus: Task status. If no value is passed in, all task statuses will be queried. Valid values:
-1 - undefined;
0 - initializing;
1 - running;
2 - succeeded;
3 - failed;
4 - terminated;
5 - deleted;
6 - paused.
        :type TaskStatus: list of int
        :param StartTimeBegin: Start time of the first task in the format of yyyy-MM-dd HH:mm:ss, such as 2017-12-31 10:40:01. It is used for queries by time range.
        :type StartTimeBegin: str
        :param StartTimeEnd: End time of the last task in the format of yyyy-MM-dd HH:mm:ss, such as 2017-12-31 10:40:01. It is used for queries by time range.
        :type StartTimeEnd: str
        :param Offset: Record offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned for a single request. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
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
        r"""
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param Items: Information of an instance task.
        :type Items: list of TaskDetail
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
                obj = TaskDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimeWindowRequest(AbstractModel):
    """DescribeTimeWindow request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimeWindowResponse(AbstractModel):
    """DescribeTimeWindow response structure.

    """

    def __init__(self):
        r"""
        :param Monday: List of maintenance time windows on Monday.
        :type Monday: list of str
        :param Tuesday: List of maintenance time windows on Tuesday.
        :type Tuesday: list of str
        :param Wednesday: List of maintenance time windows on Wednesday.
        :type Wednesday: list of str
        :param Thursday: List of maintenance time windows on Thursday.
        :type Thursday: list of str
        :param Friday: List of maintenance time windows on Friday.
        :type Friday: list of str
        :param Saturday: List of maintenance time windows on Saturday.
        :type Saturday: list of str
        :param Sunday: List of maintenance time windows on Sunday.
        :type Sunday: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Path: File path. `OwnerUin` information of the root account should be entered in this field.
        :type Path: str
        :param Offset: Record offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned for a single request. Default value: 20.
        :type Limit: int
        """
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
        r"""
        :param TotalCount: Number of eligible SQL files.
        :type TotalCount: int
        :param Items: List of returned SQL files.
        :type Items: list of SqlFileInfo
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
                obj = SqlFileInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceCpuInfo(AbstractModel):
    """CPU load

    """

    def __init__(self):
        r"""
        :param Rate: Average instance CPU utilization
        :type Rate: list of DeviceCpuRateInfo
        :param Load: CPU monitoring data of the instance
        :type Load: list of int
        """
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
        r"""
        :param CpuCore: CPU core number
        :type CpuCore: int
        :param Rate: CPU utilization
        :type Rate: list of int
        """
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
        r"""
        :param IoRatioPerSec: Time percentage of IO operations per second
        :type IoRatioPerSec: list of int
        :param IoWaitTime: Average wait time of device I/O operations * 100 in milliseconds. For example, if the value is 201, the average wait time of I/O operations is 201/100 = 2.1 milliseconds.
        :type IoWaitTime: list of int
        :param Read: Average number of read operations completed by the disk per second * 100. For example, if the value is 2,002, the average number of read operations completed by the disk per second is 2,002/100=20.2.
        :type Read: list of int
        :param Write: Average number of write operations completed by the disk per second * 100. For example, if the value is 30,001, the average number of write operations completed by the disk per second is 30,001/100=300.01.
        :type Write: list of int
        :param CapacityRatio: Disk capacity. Each value is comprised of two data, with the first data representing the used capacity and the second one representing the total disk capacity.
        :type CapacityRatio: list of int
        """
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
        r"""
        :param Total: Total memory size in KB, which is the value of `total` in the `Mem:` in the `free` command
        :type Total: list of int
        :param Used: Used memory size in KB, which is the value of `used` in the `Mem:` row in the `free` command
        :type Used: list of int
        """
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
        r"""
        :param Conn: Number of TCP connections
        :type Conn: list of int
        :param PackageIn: ENI inbound packets per second
        :type PackageIn: list of int
        :param PackageOut: ENI outbound packets per second
        :type PackageOut: list of int
        :param FlowIn: Inbound traffic in Kbps
        :type FlowIn: list of int
        :param FlowOut: Outbound traffic in Kbps
        :type FlowOut: list of int
        """
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
        r"""
        :param SecurityGroupId: Security group ID.
        :type SecurityGroupId: str
        :param InstanceIds: List of instance IDs, which is an array of one or more instance IDs.
        :type InstanceIds: list of str
        :param ForReadonlyInstance: This parameter takes effect only when the IDs of read-only replicas are passed in. If this parameter is set to `False` or left empty, the security group will be unbound from the RO groups of these read-only replicas. If this parameter is set to `True`, the security group will be unbound from the read-only replicas themselves.
        :type ForReadonlyInstance: bool
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DrInfo(AbstractModel):
    """Disaster recovery instance information

    """

    def __init__(self):
        r"""
        :param Status: Disaster recovery instance status
        :type Status: int
        :param Zone: AZ information
        :type Zone: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Region: Region information
        :type Region: str
        :param SyncStatus: Instance sync status. Possible returned values include:
0 - disaster recovery not synced;
1 - disaster recovery syncing;
2 - disaster recovery synced successfully;
3 - disaster recovery sync failed;
4 - repairing disaster recovery sync;
        :type SyncStatus: int
        :param InstanceName: Instance name
        :type InstanceName: str
        :param InstanceType: Instance type
        :type InstanceType: int
        """
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
        r"""
        :param Timestamp: Error occurrence time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Timestamp: int
        :param Content: Error details
Note: this field may return null, indicating that no valid values can be obtained.
        :type Content: str
        """
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
        r"""
        :param Status: Status value
        :type Status: int
        :param Code: Status value
        :type Code: int
        :param CostTime: Execution duration
        :type CostTime: int
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param WorkId: Backend task ID
        :type WorkId: str
        :param FileName: Name of the file to be imported
        :type FileName: str
        :param Process: Execution progress
        :type Process: int
        :param CreateTime: Task creation time
        :type CreateTime: str
        :param FileSize: File size
        :type FileSize: str
        :param Message: Task execution information
        :type Message: str
        :param JobId: Task ID
        :type JobId: int
        :param DbName: Name of the table to be imported
        :type DbName: str
        :param AsyncRequestId: Async task request ID
        :type AsyncRequestId: str
        """
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
        r"""
        :param Action: Policy, which can be ACCEPT or DROP
        :type Action: str
        :param CidrIp: Source IP or IP range, such as 192.168.0.0/16
        :type CidrIp: str
        :param PortRange: Port
        :type PortRange: str
        :param IpProtocol: Network protocol. UDP and TCP are supported.
        :type IpProtocol: str
        :param Dir: The direction of the rule, which is INPUT for inbound rules
        :type Dir: str
        :param Desc: Rule description
        :type Desc: str
        """
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
        r"""
        :param InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceIds: list of str
        :param NewPassword: New password of the instance. Rule: It can only contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special characters (!@#$%^*()).
        :type NewPassword: str
        :param Parameters: List of instance parameters. Currently, "character_set_server" and "lower_case_table_names" are supported, whose value ranges are ["utf8","latin1","gbk","utf8mb4"] and ["0","1"], respectively.
        :type Parameters: list of ParamInfo
        :param Vport: Instance port. Value range: [1024, 65535].
        :type Vport: int
        """
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
        r"""
        :param AsyncRequestIds: Array of async task request IDs, which can be used to query the execution results of async tasks.
        :type AsyncRequestIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """Instance details

    """

    def __init__(self):
        r"""
        :param WanStatus: Public network access status. Value range: 0 (not enabled), 1 (enabled), 2 (disabled)
        :type WanStatus: int
        :param Zone: AZ information
        :type Zone: str
        :param InitFlag: Initialization flag. Value range: 0 (not initialized), 1 (initialized)
        :type InitFlag: int
        :param RoVipInfo: VIP information of a read-only instance. This field is exclusive to read-only instances where read-only access is enabled separately
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoVipInfo: :class:`tencentcloud.cdb.v20170320.models.RoVipInfo`
        :param Memory: Memory capacity in MB
        :type Memory: int
        :param Status: Instance status. Value range: 0 (creating), 1 (running), 4 (isolating), 5 (isolated)
        :type Status: int
        :param VpcId: VPC ID, such as 51102
        :type VpcId: int
        :param SlaveInfo: Information of a secondary server
Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaveInfo: :class:`tencentcloud.cdb.v20170320.models.SlaveInfo`
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Volume: Disk capacity in GB
        :type Volume: int
        :param AutoRenew: Auto-renewal flag. Value range: 0 (auto-renewal not enabled), 1 (auto-renewal enabled), 2 (auto-renewal disabled)
        :type AutoRenew: int
        :param ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync)
        :type ProtectMode: int
        :param RoGroups: Details of a read-only group
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoGroups: list of RoGroup
        :param SubnetId: Subnet ID, such as 2333
        :type SubnetId: int
        :param InstanceType: Instance type. Value range: 1 (primary), 2 (disaster recovery), 3 (read-only)
        :type InstanceType: int
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Region: Region information
        :type Region: str
        :param DeadlineTime: Instance expiration time
        :type DeadlineTime: str
        :param DeployMode: AZ deployment mode. Valid values: 0 (single-AZ), 1 (multi-AZ)
        :type DeployMode: int
        :param TaskStatus: Instance task status. 0 - no task; 1 - upgrading; 2 - importing data; 3 - activating secondary; 4 - enabling public network access; 5 - batch operation in progress; 6 - rolling back; 7 - disabling public network access; 8 - changing password; 9 - renaming instance; 10 - restarting; 12 - migrating self-built instance; 13 - dropping table; 14 - creating and syncing disaster recovery instance; 15 - pending upgrade and switch; 16 - upgrade and switch in progress; 17 - upgrade and switch completed
        :type TaskStatus: int
        :param MasterInfo: Details of a primary instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterInfo: :class:`tencentcloud.cdb.v20170320.models.MasterInfo`
        :param DeviceType: Instance type
        :type DeviceType: str
        :param EngineVersion: Kernel version
        :type EngineVersion: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param DrInfo: Details of a disaster recovery instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type DrInfo: list of DrInfo
        :param WanDomain: Public domain name
        :type WanDomain: str
        :param WanPort: Public network port number
        :type WanPort: int
        :param PayType: Billing type
        :type PayType: int
        :param CreateTime: Instance creation time
        :type CreateTime: str
        :param Vip: Instance IP
        :type Vip: str
        :param Vport: Port number
        :type Vport: int
        :param CdbError: Lock flag
        :type CdbError: int
        :param UniqVpcId: VPC descriptor, such as "vpc-5v8wn9mg"
        :type UniqVpcId: str
        :param UniqSubnetId: Subnet descriptor, such as "subnet-1typ0s7d"
        :type UniqSubnetId: str
        :param PhysicalId: Physical ID
        :type PhysicalId: str
        :param Cpu: Number of cores
        :type Cpu: int
        :param Qps: Queries per second
        :type Qps: int
        :param ZoneName: AZ name
        :type ZoneName: str
        :param DeviceClass: Physical machine model
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeviceClass: str
        :param DeployGroupId: Placement group ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployGroupId: str
        :param ZoneId: AZ ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param InstanceNodes: Number of nodes
        :type InstanceNodes: int
        :param TagList: List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagList: list of TagInfoItem
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param TimeInSeconds: Estimated restart time
        :type TimeInSeconds: int
        """
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
        r"""
        :param Code: Queries database error code
        :type Code: int
        :param Message: Queries database error message
        :type Message: str
        :param InstanceId: List of instance IDs. An instance ID is in the format of cdb-c1nl9rpv, which is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Times: Time range available for rollback
        :type Times: list of RollbackTimeRange
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task. (This returned field has been disused. You can query the isolation status of an instance through the `DescribeDBInstances` API.)
Note: this field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class MasterInfo(AbstractModel):
    """Master instance information

    """

    def __init__(self):
        r"""
        :param Region: Region information
        :type Region: str
        :param RegionId: Region ID
        :type RegionId: int
        :param ZoneId: AZ ID
        :type ZoneId: int
        :param Zone: AZ information
        :type Zone: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ResourceId: Long instance ID
        :type ResourceId: str
        :param Status: Instance status
        :type Status: int
        :param InstanceName: Instance name
        :type InstanceName: str
        :param InstanceType: Instance type
        :type InstanceType: int
        :param TaskStatus: Task status
        :type TaskStatus: int
        :param Memory: Memory capacity
        :type Memory: int
        :param Volume: Disk capacity
        :type Volume: int
        :param DeviceType: Instance model
        :type DeviceType: str
        :param Qps: Queries per second
        :type Qps: int
        :param VpcId: VPC ID
        :type VpcId: int
        :param SubnetId: Subnet ID
        :type SubnetId: int
        :param ExClusterId: Dedicated cluster ID
        :type ExClusterId: str
        :param ExClusterName: Dedicated cluster name
        :type ExClusterName: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Accounts: TencentDB account
        :type Accounts: list of Account
        :param Description: Database account remarks
        :type Description: str
        """
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
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountMaxUserConnectionsRequest(AbstractModel):
    """ModifyAccountMaxUserConnections request structure.

    """

    def __init__(self):
        r"""
        :param Accounts: List of TencentDB accounts
        :type Accounts: list of Account
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param MaxUserConnections: Maximum connections of the account. Maximum value: `10240`.
        :type MaxUserConnections: int
        """
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
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountPasswordRequest(AbstractModel):
    """ModifyAccountPassword request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param NewPassword: New password of the database account. It can only contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special characters (_+-&=!@#$%^*()).
        :type NewPassword: str
        :param Accounts: TencentDB account
        :type Accounts: list of Account
        """
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
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param Accounts: Database account, including username and domain name.
        :type Accounts: list of Account
        :param GlobalPrivileges: Global permission. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "PROCESS", "DROP", "REFERENCES", "INDEX", "ALTER", "SHOW DATABASES", "CREATE TEMPORARY TABLES", "LOCK TABLES", "EXECUTE", "CREATE VIEW", "SHOW VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: Database permission. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", 	"DROP", "REFERENCES", "INDEX", "ALTER", "CREATE TEMPORARY TABLES", "LOCK TABLES", "EXECUTE", "CREATE VIEW", "SHOW VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.
        :type DatabasePrivileges: list of DatabasePrivilege
        :param TablePrivileges: Table permission in the database. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", 	"DROP", "REFERENCES", "INDEX", "ALTER", "CREATE VIEW", "SHOW VIEW", "TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.
        :type TablePrivileges: list of TablePrivilege
        :param ColumnPrivileges: Column permission in table. Valid values: "SELECT", "INSERT", "UPDATE", "REFERENCES".
Note: if this parameter is not passed in, it means to clear the permission.
        :type ColumnPrivileges: list of ColumnPrivilege
        :param ModifyAction: If this parameter is specified, permissions are modified in batches. Valid values: `grant`, `revoke`.
        :type ModifyAction: str
        """
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
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        :param AutoRenew: Auto-renewal flag. Value range: 0 (auto-renewal not enabled), 1 (auto-renewal enabled).
        :type AutoRenew: int
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param ExpireDays: Backup file retention period in days. Value range: 7-732.
        :type ExpireDays: int
        :param StartTime: (This parameter will be disused. The `BackupTimeWindow` parameter is recommended.) Backup time range in the format of 02:00-06:00, with the start time and end time on the hour. Valid values: 00:00-12:00, 02:00-06:00, 06:00-10:00, 10:00-14:00, 14:00-18:00, 18:00-22:00, 22:00-02:00.
        :type StartTime: str
        :param BackupMethod: Automatic backup mode. Only `physical` (physical cold backup) is supported
        :type BackupMethod: str
        :param BinlogExpireDays: Binlog retention period in days. Value range: 7-732. It cannot be greater than the retention period of backup files.
        :type BinlogExpireDays: int
        :param BackupTimeWindow: Backup time window; for example, to set up backup between 10:00 and 14:00 on every Tuesday and Sunday, you should set this parameter as follows: {"Monday": "", "Tuesday": "10:00-14:00", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday": "", "Sunday": "10:00-14:00"} (Note: You can set up backup on different days, but the backup time windows need to be the same. If this field is set, the `StartTime` field will be ignored)
        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    """ModifyBackupDownloadRestriction request structure.

    """

    def __init__(self):
        r"""
        :param LimitType: Valid values: `NoLimit` (backups can be downloaded over both private and public networks with any IPs), `LimitOnlyIntranet` (backups can be downloaded over the private network with any private IPs), `Customize` (backups can be downloaded over specified VPCs with specified IPs). The `LimitVpc` and `LimitIp` parameters are valid only when this parameter is set to `Customize`.
        :type LimitType: str
        :param VpcComparisonSymbol: Valid value: `In` (backups can only be downloaded over the VPCs specified in `LimitVpc`). Default value: `In`.
        :type VpcComparisonSymbol: str
        :param IpComparisonSymbol: Valid values: `In` (backups can only be downloaded with the IPs specified in `LimitIp`), `NotIn` (backups cannot be downloaded with the IPs specified in `LimitIp`). Default value: `In`.
        :type IpComparisonSymbol: str
        :param LimitVpc: VPCs used to restrict backup download.
        :type LimitVpc: list of BackupLimitVpcItem
        :param LimitIp: IPs used to restrict backup download.
        :type LimitIp: list of str
        """
        self.LimitType = None
        self.VpcComparisonSymbol = None
        self.IpComparisonSymbol = None
        self.LimitVpc = None
        self.LimitIp = None


    def _deserialize(self, params):
        self.LimitType = params.get("LimitType")
        self.VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self.IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self.LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self.LimitVpc.append(obj)
        self.LimitIp = params.get("LimitIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadRestrictionResponse(AbstractModel):
    """ModifyBackupDownloadRestriction response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param InstanceName: Instance name.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Array of instance IDs in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceIds: list of str
        :param NewProjectId: Project ID.
        :type NewProjectId: int
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.
        :type SecurityGroupIds: list of str
        :param ForReadonlyInstance: This parameter takes effect only when the ID of read-only replica is passed in. If this parameter is set to `False` or left empty, the security groups bound with the RO group of the read-only replicas will be modified. If this parameter is set to `True`, the security groups bound with the read-only replica itself will be modified.
        :type ForReadonlyInstance: bool
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceVipVportRequest(AbstractModel):
    """ModifyDBInstanceVipVport request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param DstIp: Destination IP. Either this parameter or `DstPort` must be passed in.
        :type DstIp: str
        :param DstPort: Destination port number. Value range: [1024-65535]. Either this parameter or `DstIp` must be passed in.
        :type DstPort: int
        :param UniqVpcId: Unified VPC ID
        :type UniqVpcId: str
        :param UniqSubnetId: Unified subnet ID.
        :type UniqSubnetId: str
        :param ReleaseDuration: Repossession duration in hours for old IP in the original network when changing from the basic network to VPC or changing the VPC subnet. Value range: 0-168 hours. Default value: 24 hours.
        :type ReleaseDuration: int
        """
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
        r"""
        :param AsyncRequestId: Async task ID. (This returned field has been disused)
Note: this field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: List of short instance IDs.
        :type InstanceIds: list of str
        :param ParamList: List of parameters to be modified. Every element is a combination of `Name` (parameter name) and `CurrentValue` (new value).
        :type ParamList: list of Parameter
        :param TemplateId: Template ID. At least one of `ParamList` and `TemplateId` must be passed in.
        :type TemplateId: int
        :param WaitSwitch: When to perform the parameter adjustment task. Default value: 0. Valid values: 0 - execute immediately, 1 - execute during window. When its value is 1, only one instance ID can be passed in (i.e., only one `InstanceIds` can be passed in).
        :type WaitSwitch: int
        """
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
        r"""
        :param AsyncRequestId: Async task ID, which can be used to query task progress.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceTagRequest(AbstractModel):
    """ModifyInstanceTag request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param ReplaceTags: Tag to be added or modified.
        :type ReplaceTags: list of TagInfo
        :param DeleteTags: Tag to be deleted.
        :type DeleteTags: list of TagInfo
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNameOrDescByDpIdRequest(AbstractModel):
    """ModifyNameOrDescByDpId request structure.

    """

    def __init__(self):
        r"""
        :param DeployGroupId: ID of a placement group.
        :type DeployGroupId: str
        :param DeployGroupName: Name of a placement group, which can contain up to 60 characters. The placement group name and description cannot both be empty.
        :type DeployGroupName: str
        :param Description: Description of a placement group, which can contain up to 200 characters. The placement group name and description cannot both be empty.
        :type Description: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param Name: Template name.
        :type Name: str
        :param Description: Template description.
        :type Description: str
        :param ParamList: List of parameters.
        :type ParamList: list of Parameter
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoGroupInfoRequest(AbstractModel):
    """ModifyRoGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param RoGroupId: RO group ID.
        :type RoGroupId: str
        :param RoGroupInfo: RO group details.
        :type RoGroupInfo: :class:`tencentcloud.cdb.v20170320.models.RoGroupAttr`
        :param RoWeightValues: Weights of instances in RO group. If the weighting mode of an RO group is changed to custom mode, this parameter must be set, and a weight value needs to be set for each RO instance.
        :type RoWeightValues: list of RoWeightValue
        :param IsBalanceRoLoad: Whether to rebalance the loads of read-only replicas in the RO group. Valid values: `1` (yes), `0` (no). Default value: `0`. If this parameter is set to `1`, connections to the read-only replicas in the RO group will be interrupted transiently. Please ensure that your application has a reconnection mechanism.
        :type IsBalanceRoLoad: int
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoReplicationDelayRequest(AbstractModel):
    """ModifyRoReplicationDelay request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ReplicationDelay: Replication delay in seconds. Value range: 1 to 259200.
        :type ReplicationDelay: int
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTimeWindowRequest(AbstractModel):
    """ModifyTimeWindow request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param TimeRanges: Time period available for maintenance after modification in the format of 10:00-12:00. Each period lasts from half an hour to three hours, with the start time and end time aligned by half-hour. Up to two time periods can be set. Start and end time range: [00:00, 24:00].
        :type TimeRanges: list of str
        :param Weekdays: Specifies for which day to modify the time period. Value range: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. If it is not specified or is left blank, the time period will be modified for every day by default.
        :type Weekdays: list of str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OfflineIsolatedInstancesRequest(AbstractModel):
    """OfflineIsolatedInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OpenDBInstanceGTIDRequest(AbstractModel):
    """OpenDBInstanceGTID request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBInstanceGTIDResponse(AbstractModel):
    """OpenDBInstanceGTID response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class OpenWanServiceRequest(AbstractModel):
    """OpenWanService request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWanServiceResponse(AbstractModel):
    """OpenWanService response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class Outbound(AbstractModel):
    """Security group outbound rule

    """

    def __init__(self):
        r"""
        :param Action: Policy, which can be ACCEPT or DROP
        :type Action: str
        :param CidrIp: Destination IP or IP range, such as 172.16.0.0/12
        :type CidrIp: str
        :param PortRange: Port or port range
        :type PortRange: str
        :param IpProtocol: Network protocol. UDP and TCP are supported
        :type IpProtocol: str
        :param Dir: The direction of the rule, which is OUTPUT for inbound rules
        :type Dir: str
        :param Desc: Rule description
        :type Desc: str
        """
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
        r"""
        :param Name: Parameter name
        :type Name: str
        :param Value: Parameter value
        :type Value: str
        """
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
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ParamName: Parameter name
        :type ParamName: str
        :param OldValue: Parameter value before modification
        :type OldValue: str
        :param NewValue: Parameter value after modification
        :type NewValue: str
        :param IsSucess: Whether the parameter is modified successfully
        :type IsSucess: bool
        :param ModifyTime: Modification time
        :type ModifyTime: str
        """
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
        r"""
        :param TemplateId: Parameter template ID
        :type TemplateId: int
        :param Name: Parameter template name
        :type Name: str
        :param Description: Parameter template description
        :type Description: str
        :param EngineVersion: Instance engine version
        :type EngineVersion: str
        """
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
        r"""
        :param Name: Parameter name
        :type Name: str
        :param CurrentValue: Parameter value
        :type CurrentValue: str
        """
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
        r"""
        :param Name: Parameter name
        :type Name: str
        :param ParamType: Parameter type
        :type ParamType: str
        :param Default: Default value of the parameter
        :type Default: str
        :param Description: Parameter description
        :type Description: str
        :param CurrentValue: Current value of the parameter
        :type CurrentValue: str
        :param NeedReboot: Whether the database needs to be restarted for the modified parameter to take effect. Value range: 0 (no); 1 (yes)
        :type NeedReboot: int
        :param Max: Maximum value of the parameter
        :type Max: int
        :param Min: Minimum value of the parameter
        :type Min: int
        :param EnumValue: Enumerated values of the parameter. It is null if the parameter is non-enumerated
        :type EnumValue: list of str
        """
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
        r"""
        :param RegionName: Region name
        :type RegionName: str
        :param Area: Area
        :type Area: str
        :param IsDefaultRegion: Whether it is a default region
        :type IsDefaultRegion: int
        :param Region: Region name
        :type Region: str
        :param ZonesConf: Sale configuration of the AZ
        :type ZonesConf: list of ZoneSellConf
        """
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
        r"""
        :param InstanceIds: Array of instance IDs in the format of `cdb-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the ID, whose value is the `InstanceId` value in the output parameters.
        :type InstanceIds: list of str
        """
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
        r"""
        :param Items: Deisolation result set.
        :type Items: list of ReleaseResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param Code: Result value of instance deisolation. A returned value of 0 indicates success.
        :type Code: int
        :param Message: Error message for instance deisolation.
        :type Message: str
        """
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
        r"""
        :param InstanceIds: Array of instance IDs in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        """
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
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class RoGroup(AbstractModel):
    """Read-only group parameter

    """

    def __init__(self):
        r"""
        :param RoGroupMode: Read-only group mode. Valid values: `alone` (the system assigns a read-only group automatically), `allinone` (a new read-only group will be created), `join` (an existing read-only group will be used).
        :type RoGroupMode: str
        :param RoGroupId: Read-only group ID.
        :type RoGroupId: str
        :param RoGroupName: Read-only group name.
        :type RoGroupName: str
        :param RoOfflineDelay: Whether to enable the function of isolating an instance that exceeds the latency threshold. If it is enabled, when the latency between the read-only instance and the primary instance exceeds the latency threshold, the read-only instance will be isolated. Valid values: 1 (enabled), 0 (not enabled)
        :type RoOfflineDelay: int
        :param RoMaxDelayTime: Latency threshold
        :type RoMaxDelayTime: int
        :param MinRoInGroup: Minimum number of instances to be retained. If the number of the purchased read-only instances is smaller than the set value, they will not be removed.
        :type MinRoInGroup: int
        :param WeightMode: Read/write weight distribution mode. Valid values: `system` (weights are assigned by the system automatically), `custom` (weights are customized)
        :type WeightMode: str
        :param Weight: Weight value.
        :type Weight: int
        :param RoInstances: Details of read-only instances in read-only group
        :type RoInstances: list of RoInstanceInfo
        :param Vip: Private IP of read-only group.
        :type Vip: str
        :param Vport: Private network port number of read-only group.
        :type Vport: int
        :param UniqVpcId: VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param UniqSubnetId: Subnet ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UniqSubnetId: str
        :param RoGroupRegion: Read-only group region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoGroupRegion: str
        :param RoGroupZone: Read-only group AZ.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoGroupZone: str
        """
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
        r"""
        :param RoGroupName: RO group name.
        :type RoGroupName: str
        :param RoMaxDelayTime: Maximum delay threshold for RO instances in seconds. Minimum value: 1. Please note that this value will take effect only if an instance removal policy is enabled in the RO group.
        :type RoMaxDelayTime: int
        :param RoOfflineDelay: Whether to enable instance removal. Valid values: 1 (enabled), 0 (not enabled). Please note that if instance removal is enabled, the delay threshold parameter (`RoMaxDelayTime`) must be set.
        :type RoOfflineDelay: int
        :param MinRoInGroup: Minimum number of instances to be retained, which can be set to any value less than or equal to the number of RO instances in the RO group. Please note that if this value is set to be greater than the number of RO instances, no removal will be performed, and if it is set to 0, all instances with an excessive delay will be removed.
        :type MinRoInGroup: int
        :param WeightMode: Weighting mode. Supported values include `system` (automatically assigned by the system) and `custom` (defined by user). Please note that if the `custom` mode is selected, the RO instance weight configuration parameter (RoWeightValues) must be set.
        :type WeightMode: str
        """
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
        r"""
        :param MasterInstanceId: Master instance ID corresponding to the RO group
        :type MasterInstanceId: str
        :param RoStatus: RO instance status in the RO group. Value range: online, offline
        :type RoStatus: str
        :param OfflineTime: Last deactivation time of a RO instance in the RO group
        :type OfflineTime: str
        :param Weight: RO instance weight in the RO group
        :type Weight: int
        :param Region: RO instance region name, such as ap-shanghai
        :type Region: str
        :param Zone: Name of RO AZ, such as ap-shanghai-1
        :type Zone: str
        :param InstanceId: RO instance ID in the format of cdbro-c1nl9rpv
        :type InstanceId: str
        :param Status: RO instance status. Value range: 0 (creating), 1 (running), 4 (deleting)
        :type Status: int
        :param InstanceType: Instance type. Value range: 1 (primary), 2 (disaster recovery), 3 (read-only)
        :type InstanceType: int
        :param InstanceName: RO instance name
        :type InstanceName: str
        :param HourFeeStatus: Pay-as-you-go billing status. Value range: 1 (normal), 2 (in arrears)
        :type HourFeeStatus: int
        :param TaskStatus: RO instance task status. Value range: <br>0 - no task <br>1 - upgrading <br>2 - importing data <br>3 - activating secondary <br>4 - public network access enabled <br>5 - batch operation in progress <br>6 - rolling back <br>7 - public network access not enabled <br>8 - modifying password <br>9 - renaming instance <br>10 - restarting <br>12 - migrating self-built instance <br>13 - dropping table <br>14 - creating and syncing disaster recovery instance
        :type TaskStatus: int
        :param Memory: RO instance memory size in MB
        :type Memory: int
        :param Volume: RO instance disk size in GB
        :type Volume: int
        :param Qps: Queries per second
        :type Qps: int
        :param Vip: Private IP address of the RO instance
        :type Vip: str
        :param Vport: Access port of the RO instance
        :type Vport: int
        :param VpcId: VPC ID of the RO instance
        :type VpcId: int
        :param SubnetId: VPC subnet ID of the RO instance
        :type SubnetId: int
        :param DeviceType: RO instance specification description. Value range: CUSTOM
        :type DeviceType: str
        :param EngineVersion: Database engine version of the read-only replica. Valid values: `5.1`, `5.5`, `5.6`, `5.7`, `8.0`
        :type EngineVersion: str
        :param DeadlineTime: RO instance expiration time in the format of yyyy-mm-dd hh:mm:ss. If it is a pay-as-you-go instance, the value of this field is 0000-00-00 00:00:00
        :type DeadlineTime: str
        :param PayType: RO instance billing method. Value range: 0 (monthly subscribed), 1 (pay-as-you-go), 2 (monthly postpaid)
        :type PayType: int
        """
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
        r"""
        :param RoVipStatus: VIP status of the read-only instance
        :type RoVipStatus: int
        :param RoSubnetId: VPC subnet of the read-only instance
        :type RoSubnetId: int
        :param RoVpcId: VPC of the read-only instance
        :type RoVpcId: int
        :param RoVport: VIP port number of the read-only instance
        :type RoVport: int
        :param RoVip: VIP of the read-only instance
        :type RoVip: str
        """
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
        r"""
        :param InstanceId: RO instance ID.
        :type InstanceId: str
        :param Weight: Weight value. Value range: [0, 100].
        :type Weight: int
        """
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
        r"""
        :param DatabaseName: Original database name before rollback
Note: this field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param NewDatabaseName: New database name after rollback
Note: this field may return null, indicating that no valid values can be obtained.
        :type NewDatabaseName: str
        """
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
        r"""
        :param InstanceId: TencentDB instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param Strategy: Rollback policy. Valid values: `table` (ultrafast mode), `db` (faster mode), and `full` (fast mode). Default value: `full`. In the ultrafast mode, only backups and binlogs of the tables specified by the `Tables` parameter are imported; if `Tables` does not include all of the tables involved in cross-table operations, the rollback may fail; and the `Database` parameter must be left empty. In the faster mode, only backups and binlogs of the databases specified by the `Databases` parameter are imported, and if `Databases` does not include all of the databases involved in cross-database operations, the rollback may fail. In the fast mode, backups and binlogs of the entire instance will be imported in a speed slower than the other modes.
        :type Strategy: str
        :param RollbackTime: Database rollback time in the format of yyyy-mm-dd hh:mm:ss
        :type RollbackTime: str
        :param Databases: Information of the databases to be rolled back, which means rollback at the database level
Note: this field may return null, indicating that no valid values can be obtained.
        :type Databases: list of RollbackDBName
        :param Tables: Information of the tables to be rolled back, which means rollback at the table level
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tables: list of RollbackTables
        """
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
        r"""
        :param TableName: Original table name before rollback
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param NewTableName: New table name after rollback
Note: this field may return null, indicating that no valid values can be obtained.
        :type NewTableName: str
        """
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
        r"""
        :param Database: Database name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param Table: Table details
Note: this field may return null, indicating that no valid values can be obtained.
        :type Table: list of RollbackTableName
        """
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
        r"""
        :param Info: Task execution information.
        :type Info: str
        :param Status: Task execution result. Valid values: INITIAL: initializing, RUNNING: running, SUCCESS: succeeded, FAILED: failed, KILLED: terminated, REMOVED: deleted, PAUSED: paused.
        :type Status: str
        :param Progress: Task execution progress. Value range: [0,100].
        :type Progress: int
        :param StartTime: Task start time.
        :type StartTime: str
        :param EndTime: Task end time.
        :type EndTime: str
        :param Detail: Rollback task details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Detail: list of RollbackInstancesInfo
        """
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
        r"""
        :param Begin: Start time available for rollback in the format of yyyy-MM-dd HH:mm:ss, such as 2016-10-29 01:06:04
        :type Begin: str
        :param End: End time available for rollback in the format of yyyy-MM-dd HH:mm:ss, such as 2016-11-02 11:44:47
        :type End: str
        """
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
        r"""
        :param ProjectId: Project ID
        :type ProjectId: int
        :param CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param Inbound: Inbound rule
        :type Inbound: list of Inbound
        :param Outbound: Outbound rule
        :type Outbound: list of Outbound
        :param SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        """
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
        r"""
        :param Device: (Disused) Device type
        :type Device: str
        :param Type: (Disused) Purchasable specification description 
        :type Type: str
        :param CdbType: (Disused) Instance type 
        :type CdbType: str
        :param Memory: Memory size in MB
        :type Memory: int
        :param Cpu: CPU core count
        :type Cpu: int
        :param VolumeMin: Minimum disk size in GB
        :type VolumeMin: int
        :param VolumeMax: Maximum disk size in GB
        :type VolumeMax: int
        :param VolumeStep: Disk increment in GB
        :type VolumeStep: int
        :param Connection: Number of connections
        :type Connection: int
        :param Qps: Queries per second
        :type Qps: int
        :param Iops: IOs per second
        :type Iops: int
        :param Info: Application scenario description
        :type Info: str
        :param Status: Status. Value `0` indicates that this specification is purchasable.
        :type Status: int
        :param Tag: (Disused) Tag value
        :type Tag: int
        :param DeviceType: Instance resource isolation type. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance).
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type DeviceType: str
        :param DeviceTypeName: Instance resource isolation type. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance).
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type DeviceTypeName: str
        """
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
        r"""
        :param TypeName: Name of the purchasable instance
        :type TypeName: str
        :param EngineVersion: Kernel version number
        :type EngineVersion: list of str
        :param Configs: Configuration details of a purchasable specification
        :type Configs: list of SellConfig
        """
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
        r"""
        :param ReplicationMode: Replication mode of the secondary database. Value range: async, semi-sync
        :type ReplicationMode: str
        :param Zone: AZ name of the secondary database, such as ap-shanghai-1
        :type Zone: str
        """
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
        r"""
        :param First: Information of secondary server 1
        :type First: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`
        :param Second: Information of secondary server 2
Note: This field may return null, indicating that no valid values can be obtained.
        :type Second: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`
        """
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
        r"""
        :param Vport: Port number
        :type Vport: int
        :param Region: Region information
        :type Region: str
        :param Vip: Virtual IP information
        :type Vip: str
        :param Zone: AZ information
        :type Zone: str
        """
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
        r"""
        :param Name: Backup filename
        :type Name: str
        :param Size: Backup file size in bytes
        :type Size: int
        :param Date: Backup snapshot time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: Download address on the private network
        :type IntranetUrl: str
        :param InternetUrl: Download address on the public network
        :type InternetUrl: str
        :param Type: Log type. Value range: slowlog (slow log)
        :type Type: str
        """
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
        r"""
        :param Timestamp: SQL execution time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Timestamp: int
        :param QueryTime: SQL execution duration in seconds.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type QueryTime: float
        :param SqlText: SQL statement.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SqlText: str
        :param UserHost: Client address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserHost: str
        :param UserName: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param Database: Database name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param LockTime: Lock duration in seconds.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LockTime: float
        :param RowsExamined: Number of scanned rows.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RowsExamined: int
        :param RowsSent: Number of rows in result set.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RowsSent: int
        :param SqlTemplate: SQL template.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SqlTemplate: str
        :param Md5: SQL statement MD5.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Md5: str
        """
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
        r"""
        :param UploadTime: Upload time
        :type UploadTime: str
        :param UploadInfo: Upload progress
        :type UploadInfo: :class:`tencentcloud.cdb.v20170320.models.UploadInfo`
        :param FileName: Filename
        :type FileName: str
        :param FileSize: File size in bytes
        :type FileSize: int
        :param IsUploadFinished: Whether upload is finished. Valid values: 0 (not completed), 1 (completed)
        :type IsUploadFinished: int
        :param FileId: File ID
        :type FileId: str
        """
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
        r"""
        :param Instances: Details of the instance for rollback
        :type Instances: list of RollbackInstancesInfo
        """
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
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class StartDelayReplicationRequest(AbstractModel):
    """StartDelayReplication request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DelayReplicationType: Delayed replication mode. Valid values: `DEFAULT` (replicate according to the specified replication delay), `GTID` (replicate according to the specified GTID), `DUE_TIME` (replicate according to the specified point in time).
        :type DelayReplicationType: str
        :param DueTime: Specified point in time. Default value: 0. The maximum value cannot be later than the current time.
        :type DueTime: int
        :param Gtid: Specified GITD. This parameter is required when the delayed replication mode is `GTID`.
        :type Gtid: str
        """
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
        r"""
        :param AsyncRequestId: Delayed replication task ID. This parameter will be returned if `DelayReplicationType` is not `DEFAULT`. It can be used to view the status of the delayed replication task.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class StopDBImportJobRequest(AbstractModel):
    """StopDBImportJob request structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task request ID.
        :type AsyncRequestId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopDelayReplicationRequest(AbstractModel):
    """StopDelayReplication request structure.

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDelayReplicationResponse(AbstractModel):
    """StopDelayReplication response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopRollbackRequest(AbstractModel):
    """StopRollback request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ID of the instance whose rollback task is canceled
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRollbackResponse(AbstractModel):
    """StopRollback response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task request ID
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SwitchDBInstanceMasterSlaveRequest(AbstractModel):
    """SwitchDBInstanceMasterSlave request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DstSlave: Specifies the replica server to switched to. Valid values: `first` (the first replica server), `second` (the second replica server). Default value: `first`. `second` is valid only for a multi-AZ instance.
        :type DstSlave: str
        :param ForceSwitch: Whether to force the switch. Valid values: `True`, `False` (default). If this parameter is set to `True`, instance data may be lost during the switch.
        :type ForceSwitch: bool
        :param WaitSwitch: Whether to perform the switch during a time window. Valid values: `True`, `False` (default). If `ForceSwitch` is set to `True`, this parameter is invalid.
        :type WaitSwitch: bool
        """
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
        r"""
        :param AsyncRequestId: Async task ID
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SwitchDrInstanceToMasterRequest(AbstractModel):
    """SwitchDrInstanceToMaster request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Disaster recovery instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDrInstanceToMasterResponse(AbstractModel):
    """SwitchDrInstanceToMaster response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SwitchForUpgradeRequest(AbstractModel):
    """SwitchForUpgrade request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchForUpgradeResponse(AbstractModel):
    """SwitchForUpgrade response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TablePrivilege(AbstractModel):
    """Table permission

    """

    def __init__(self):
        r"""
        :param Database: Database name
        :type Database: str
        :param Table: Table name
        :type Table: str
        :param Privileges: Permission information
        :type Privileges: list of str
        """
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
        


class TagInfoItem(AbstractModel):
    """Tag information

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: Tag value
Note: this field may return `null`, indicating that no valid values can be obtained.
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
        


class TagInfoUnit(AbstractModel):
    """Tag information unit

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfInstance(AbstractModel):
    """Instance tag information

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Tags: Tag information
        :type Tags: list of TagInfoUnit
        """
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
        r"""
        :param Code: Error code.
        :type Code: int
        :param Message: Error message.
        :type Message: str
        :param JobId: ID of an instance task.
        :type JobId: int
        :param Progress: Instance task progress.
        :type Progress: int
        :param TaskStatus: Instance task status. Valid values:
"UNDEFINED" - undefined;
"INITIAL" - initializing;
"RUNNING" - running;
"SUCCEED" - succeeded;
"FAILED" - failed;
"KILLED" - terminated;
"REMOVED" - deleted;
"PAUSED" - paused.
"WAITING" - waiting (which can be canceled)
        :type TaskStatus: str
        :param TaskType: Instance task type. Valid values:
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
"SWITCH DR TO MASTER" - promoting a disaster recovery instance.
        :type TaskType: str
        :param StartTime: Instance task start time.
        :type StartTime: str
        :param EndTime: Instance task end time.
        :type EndTime: str
        :param InstanceIds: ID of an instance associated with a task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIds: list of str
        :param AsyncRequestId: Async task request ID.
        :type AsyncRequestId: str
        """
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
        r"""
        :param InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param EngineVersion: Version of primary instance database engine. Value range: 5.6, 5.7
        :type EngineVersion: str
        :param WaitSwitch: Mode of switch to a new instance. Value range: 0 (switch immediately), 1 (switch within a time window). Default value: 0. If the value is 1, the switch process will be performed within a time window. Or, you can call the [switching to new instance API](https://intl.cloud.tencent.com/document/product/236/15864?from_cn_redirect=1) to trigger the process.
        :type WaitSwitch: int
        :param UpgradeSubversion: Whether to upgrade kernel minor version. Valid values: 1 (upgrade kernel minor version), 0 (upgrade database engine).
        :type UpgradeSubversion: int
        :param MaxDelayTime: Delay threshold. Value range: 1-10
        :type MaxDelayTime: int
        """
        self.InstanceId = None
        self.EngineVersion = None
        self.WaitSwitch = None
        self.UpgradeSubversion = None
        self.MaxDelayTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EngineVersion = params.get("EngineVersion")
        self.WaitSwitch = params.get("WaitSwitch")
        self.UpgradeSubversion = params.get("UpgradeSubversion")
        self.MaxDelayTime = params.get("MaxDelayTime")
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
        r"""
        :param AsyncRequestId: Async task ID. The task execution result can be queried using the [async task execution result querying API](https://intl.cloud.tencent.com/document/api/236/20410?from_cn_redirect=1).
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of `cdb-c1nl9rpv` or `cdbro-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param Memory: Memory size in MB after upgrade. To ensure that the `Memory` value to be passed in is valid, please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/product/236/17229?from_cn_redirect=1) API to query the specifications of the memory that can be upgraded to.
        :type Memory: int
        :param Volume: Disk size in GB after upgrade. To ensure that the `Volume` value to be passed in is valid, please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/product/236/17229?from_cn_redirect=1) API to query the specifications of the disk that can be upgraded to.
        :type Volume: int
        :param ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). This parameter can be specified when upgrading primary instances and is meaningless for read-only or disaster recovery instances.
        :type ProtectMode: int
        :param DeployMode: Deployment mode. Valid values: 0 (single-AZ), 1 (multi-AZ). Default value: 0. This parameter can be specified when upgrading primary instances and is meaningless for read-only or disaster recovery instances.
        :type DeployMode: int
        :param SlaveZone: AZ information of secondary database 1, which is the `Zone` value of the instance by default. This parameter can be specified when upgrading primary instances in multi-AZ mode and is meaningless for read-only or disaster recovery instances. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/product/236/17229?from_cn_redirect=1) API to query the supported AZs.
        :type SlaveZone: str
        :param EngineVersion: Version of primary instance database engine. Valid values: 5.5, 5.6, 5.7.
        :type EngineVersion: str
        :param WaitSwitch: Mode of switch to new instance. Valid values: 0 (switch immediately), 1 (switch within a time window). Default value: 0. If the value is 1, the switch process will be performed within a time window. Or, you can call the [SwitchForUpgrade](https://intl.cloud.tencent.com/document/product/236/15864?from_cn_redirect=1) API to trigger the process.
        :type WaitSwitch: int
        :param BackupZone: AZ information of secondary database 2, which is empty by default. This parameter can be specified when upgrading primary instances and is meaningless for read-only or disaster recovery instances.
        :type BackupZone: str
        :param InstanceRole: Instance type. Valid values: master (primary instance), dr (disaster recovery instance), ro (read-only instance). Default value: master.
        :type InstanceRole: str
        :param DeviceType: The resource isolation type after the instance is upgraded. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance). If this parameter is left empty, the resource isolation type will be the same as the original one.
        :type DeviceType: str
        :param Cpu: The number of CPU cores after the instance is upgraded. If this parameter is left empty, the number of CPU cores will be automatically filled in according to the `Memory` value.
        :type Cpu: int
        :param FastUpgrade: Whether to enable QuickChange. Valid values: `0` (no), `1` (yes). After QuickChange is enabled, the required resources will be checked. QuickChange is performed only when the required resources support the feature; otherwise, an error message will be returned.
        :type FastUpgrade: int
        :param MaxDelayTime: Delay threshold. Value range: 1-10. Default value: `10`.
        :type MaxDelayTime: int
        """
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
        self.FastUpgrade = None
        self.MaxDelayTime = None


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
        self.FastUpgrade = params.get("FastUpgrade")
        self.MaxDelayTime = params.get("MaxDelayTime")
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
        r"""
        :param DealIds: Order ID.
        :type DealIds: list of str
        :param AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param AllSliceNum: Number of parts of file
        :type AllSliceNum: int
        :param CompleteNum: Number of completed parts
        :type CompleteNum: int
        """
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
        r"""
        :param DeployMode: AZ deployment mode. Value range: 0 (single-AZ), 1 (multi-AZ)
        :type DeployMode: list of int
        :param MasterZone: AZ where the primary instance is located
        :type MasterZone: list of str
        :param SlaveZone: AZ where salve database 1 is located when the instance is deployed in multi-AZ mode
        :type SlaveZone: list of str
        :param BackupZone: AZ where salve database 2 is located when the instance is deployed in multi-AZ mode
        :type BackupZone: list of str
        """
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
        r"""
        :param Status: AZ status. Value range: 0 (not available), 1 (available), 2 (purchasable), 3 (not purchasable), 4 (not displayed)
        :type Status: int
        :param ZoneName: AZ name
        :type ZoneName: str
        :param IsCustom: Whether it is a custom instance type
        :type IsCustom: bool
        :param IsSupportDr: Whether disaster recovery is supported
        :type IsSupportDr: bool
        :param IsSupportVpc: Whether VPC is supported
        :type IsSupportVpc: bool
        :param HourInstanceSaleMaxNum: Maximum purchasable quantity of hourly billed instances
        :type HourInstanceSaleMaxNum: int
        :param IsDefaultZone: Whether it is a default AZ
        :type IsDefaultZone: bool
        :param IsBm: Whether it is a BM zone
        :type IsBm: bool
        :param PayType: Supported billing method. Value range: 0 (monthly subscribed), 1 (hourly), 2 (postpaid)
        :type PayType: list of str
        :param ProtectMode: Data replication type. Value range: 0 (async), 1 (semi-sync), 2 (strong sync)
        :type ProtectMode: list of str
        :param Zone: AZ name
        :type Zone: str
        :param SellType: Array of purchasable instance types
        :type SellType: list of SellType
        :param ZoneConf: Multi-AZ information
        :type ZoneConf: :class:`tencentcloud.cdb.v20170320.models.ZoneConf`
        :param DrZone: Information of the supported disaster recovery AZ
        :type DrZone: list of str
        :param IsSupportRemoteRo: Whether cross-AZ read-only access is supported
        :type IsSupportRemoteRo: bool
        :param RemoteRoZone: Information of supported cross-AZ read-only zone
Note: this field may return null, indicating that no valid values can be obtained.
        :type RemoteRoZone: list of str
        """
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
        