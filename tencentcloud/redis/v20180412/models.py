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

from tencentcloud.common.abstract_model import AbstractModel


class Account(AbstractModel):
    """Sub-account information

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param AccountName: Account name (`root` for a root account)
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountName: str
        :param Remark: Account description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param Privilege: Read/write policy. r: read-only; w: write-only; rw: read/write
Note: This field may return null, indicating that no valid values can be obtained.
        :type Privilege: str
        :param ReadonlyPolicy: Routing policy. master: master node; replication: slave node
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReadonlyPolicy: list of str
        :param Status: Sub-account status. 1: account is being changed; 2: account is valid; -4: account has been deleted
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self.InstanceId = None
        self.AccountName = None
        self.Remark = None
        self.Privilege = None
        self.ReadonlyPolicy = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AccountName = params.get("AccountName")
        self.Remark = params.get("Remark")
        self.Privilege = params.get("Privilege")
        self.ReadonlyPolicy = params.get("ReadonlyPolicy")
        self.Status = params.get("Status")


class BigKeyInfo(AbstractModel):
    """Big key details

    """

    def __init__(self):
        """
        :param DB: Database
        :type DB: int
        :param Key: Big key
        :type Key: str
        :param Type: Type
        :type Type: str
        :param Size: Size
        :type Size: int
        :param Updatetime: Data timestamp
        :type Updatetime: int
        """
        self.DB = None
        self.Key = None
        self.Type = None
        self.Size = None
        self.Updatetime = None


    def _deserialize(self, params):
        self.DB = params.get("DB")
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Size = params.get("Size")
        self.Updatetime = params.get("Updatetime")


class BigKeyTypeInfo(AbstractModel):
    """Big key type distribution details

    """

    def __init__(self):
        """
        :param Type: Type
        :type Type: str
        :param Count: Count
        :type Count: int
        :param Size: Size
        :type Size: int
        :param Updatetime: Timestamp
        :type Updatetime: int
        """
        self.Type = None
        self.Count = None
        self.Size = None
        self.Updatetime = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Count = params.get("Count")
        self.Size = params.get("Size")
        self.Updatetime = params.get("Updatetime")


class CleanUpInstanceRequest(AbstractModel):
    """CleanUpInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class CleanUpInstanceResponse(AbstractModel):
    """CleanUpInstance response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ClearInstanceRequest(AbstractModel):
    """ClearInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Password: Redis instance password (this parameter is not required for password-free instances but for password-enabled instances)
        :type Password: str
        """
        self.InstanceId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")


class ClearInstanceResponse(AbstractModel):
    """ClearInstance response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CommandTake(AbstractModel):
    """Command duration

    """

    def __init__(self):
        """
        :param Cmd: Command
        :type Cmd: str
        :param Took: Duration
        :type Took: int
        """
        self.Cmd = None
        self.Took = None


    def _deserialize(self, params):
        self.Cmd = params.get("Cmd")
        self.Took = params.get("Took")


class CreateInstanceAccountRequest(AbstractModel):
    """CreateInstanceAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AccountName: Sub-account name
        :type AccountName: str
        :param AccountPassword: Sub-account password
        :type AccountPassword: str
        :param ReadonlyPolicy: Routing policy. Enter `master` for master node or `replication` for slave node
        :type ReadonlyPolicy: list of str
        :param Privilege: Read/write policy. Enter `r` for read-only, `w` for write-only, or `rw` for read/write
        :type Privilege: str
        :param Remark: Sub-account description information
        :type Remark: str
        """
        self.InstanceId = None
        self.AccountName = None
        self.AccountPassword = None
        self.ReadonlyPolicy = None
        self.Privilege = None
        self.Remark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AccountName = params.get("AccountName")
        self.AccountPassword = params.get("AccountPassword")
        self.ReadonlyPolicy = params.get("ReadonlyPolicy")
        self.Privilege = params.get("Privilege")
        self.Remark = params.get("Remark")


class CreateInstanceAccountResponse(AbstractModel):
    """CreateInstanceAccount response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances request structure.

    """

    def __init__(self):
        """
        :param ZoneId: AZ ID of instance
        :type ZoneId: int
        :param TypeId: Instance type. 2: Redis 2.8 Master-Slave Edition, 3: Redis 3.2 Master-Slave Edition (CKV Master-Slave Edition), 4: Redis 3.2 Cluster Edition (CKV Cluster Edition), 5: Redis 2.8 Standalone Edition, 6: Redis 4.0 Master-Slave Edition, 7: Redis 4.0 Cluster Edition, 8: Redis 5.0 Master-Slave Edition, 9: Redis 5.0 Cluster Edition,
        :type TypeId: int
        :param MemSize: Instance capacity in MB. The actual value is subject to the specifications returned by the purchasable specification querying API |
        :type MemSize: int
        :param GoodsNum: Number of instances. The actual quantity purchasable at a time is subject to the specifications returned by the purchasable specification querying API
        :type GoodsNum: int
        :param Period: Length of purchase in months, which is required when creating a monthly subscribed instances. Value range: [1,2,3,4,5,6,7,8,9,10,11,12,24,36]. For pay-as-you-go instances, enter 1
        :type Period: int
        :param BillingMode: Billing method. 0: pay as you go
        :type BillingMode: int
        :param Password: Instance password. Rules: 1. It can contain 8-16 characters; 2. It must contain at least two of the following three types of characters: letters, digits, and special characters !@^*(). (When creating a password-free instance, you can leave this field along and it will be ignored.)
        :type Password: str
        :param VpcId: VPC ID such as vpc-sad23jfdfk. If this parameter is not passed in, the basic network will be selected by default. Please use the VPC list querying API to query.
        :type VpcId: str
        :param SubnetId: In a basic network, subnetId is invalid. In a VPC subnet, the value is the subnet ID, such as subnet-fdj24n34j2
        :type SubnetId: str
        :param ProjectId: Project ID. The value is subject to the projectId returned by user account > user account-related querying APIs > project list
        :type ProjectId: int
        :param AutoRenew: Auto-renewal flag. 0: default status (manual renewal); 1: auto-renewal enabled; 2: auto-renewal disabled
        :type AutoRenew: int
        :param SecurityGroupIdList: Array of security group IDs
        :type SecurityGroupIdList: list of str
        :param VPort: User-defined port. If this parameter is left empty, 6379 will be used by default. Value range: [1024,65535]
        :type VPort: int
        :param RedisShardNum: Number of instance shards. This parameter can be left blank for Redis 2.8 master-slave edition, CKV master-slave edition, Redis 2.8 standalone edition, and Redis 4.0 master-slave edition
        :type RedisShardNum: int
        :param RedisReplicasNum: Number of instance replicas. This parameter can be left blank for Redis 2.8 master-slave edition, CKV master-slave edition, and Redis 2.8 standalone edition
        :type RedisReplicasNum: int
        :param ReplicasReadonly: Whether to support read-only replicas. This parameter can be left blank for Redis 2.8 master-slave edition, CKV master-slave edition, and Redis 2.8 standalone edition |
        :type ReplicasReadonly: bool
        :param InstanceName: Instance name
        :type InstanceName: str
        :param NoAuth: Whether to support the password-free feature. Value range: true (password-free instance); false (password-enabled instance). Default value: false
        :type NoAuth: bool
        """
        self.ZoneId = None
        self.TypeId = None
        self.MemSize = None
        self.GoodsNum = None
        self.Period = None
        self.BillingMode = None
        self.Password = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.AutoRenew = None
        self.SecurityGroupIdList = None
        self.VPort = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.ReplicasReadonly = None
        self.InstanceName = None
        self.NoAuth = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.TypeId = params.get("TypeId")
        self.MemSize = params.get("MemSize")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.BillingMode = params.get("BillingMode")
        self.Password = params.get("Password")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenew = params.get("AutoRenew")
        self.SecurityGroupIdList = params.get("SecurityGroupIdList")
        self.VPort = params.get("VPort")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.ReplicasReadonly = params.get("ReplicasReadonly")
        self.InstanceName = params.get("InstanceName")
        self.NoAuth = params.get("NoAuth")


class CreateInstancesResponse(AbstractModel):
    """CreateInstances response structure.

    """

    def __init__(self):
        """
        :param DealId: Transaction ID
        :type DealId: str
        :param InstanceIds: Instance ID (this field is during beta test and is not displayed in some regions)
        :type InstanceIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class DelayDistribution(AbstractModel):
    """Delay distribution details

    """

    def __init__(self):
        """
        :param Ladder: Distribution ladder
        :type Ladder: int
        :param Size: Size
        :type Size: int
        :param Updatetime: Modification time
        :type Updatetime: int
        """
        self.Ladder = None
        self.Size = None
        self.Updatetime = None


    def _deserialize(self, params):
        self.Ladder = params.get("Ladder")
        self.Size = params.get("Size")
        self.Updatetime = params.get("Updatetime")


class DeleteInstanceAccountRequest(AbstractModel):
    """DeleteInstanceAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AccountName: Sub-account name
        :type AccountName: str
        """
        self.InstanceId = None
        self.AccountName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AccountName = params.get("AccountName")


class DeleteInstanceAccountResponse(AbstractModel):
    """DeleteInstanceAccount response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeAutoBackupConfigRequest(AbstractModel):
    """DescribeAutoBackupConfig request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeAutoBackupConfigResponse(AbstractModel):
    """DescribeAutoBackupConfig response structure.

    """

    def __init__(self):
        """
        :param AutoBackupType: Backup type. Auto backup type: 1 "scheduled rollback"
        :type AutoBackupType: int
        :param WeekDays: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.
        :type WeekDays: list of str
        :param TimePeriod: Time period.
        :type TimePeriod: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AutoBackupType = None
        self.WeekDays = None
        self.TimePeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoBackupType = params.get("AutoBackupType")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.RequestId = params.get("RequestId")


class DescribeBackupUrlRequest(AbstractModel):
    """DescribeBackupUrl request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param BackupId: Backup ID, which can be queried through the `DescribeInstanceBackups` API
        :type BackupId: str
        """
        self.InstanceId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")


class DescribeBackupUrlResponse(AbstractModel):
    """DescribeBackupUrl response structure.

    """

    def __init__(self):
        """
        :param DownloadUrl: Download address on the public network (valid for 6 hours)
        :type DownloadUrl: list of str
        :param InnerDownloadUrl: Download address on the private network (valid for 6 hours)
        :type InnerDownloadUrl: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.InnerDownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.InnerDownloadUrl = params.get("InnerDownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeInstanceAccountRequest(AbstractModel):
    """DescribeInstanceAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Page offset
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeInstanceAccountResponse(AbstractModel):
    """DescribeInstanceAccount response structure.

    """

    def __init__(self):
        """
        :param Accounts: Account details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Accounts: list of Account
        :param TotalCount: Number of accounts
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Accounts = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstanceBackupsRequest(AbstractModel):
    """DescribeInstanceBackups request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the instance to be operated on, which can be obtained through the `InstanceId` field in the return value of the DescribeInstance API.
        :type InstanceId: str
        :param Limit: Instance list size. Default value: 20
        :type Limit: int
        :param Offset: Offset, which is an integral multiple of `Limit`
        :type Offset: int
        :param BeginTime: Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-02-08 16:46:34. This parameter is used to query the list of instance backups started during the [beginTime, endTime] range.
        :type BeginTime: str
        :param EndTime: End time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-02-08 19:09:26. This parameter is used to query the list of instance backups started during the [beginTime, endTime] range.
        :type EndTime: str
        :param Status: 1: backup in process; 2: backing up normally; 3: converting from backup to RDB file; 4: RDB conversion completed; -1: backup expired; -2: backup deleted.
        :type Status: list of int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")


class DescribeInstanceBackupsResponse(AbstractModel):
    """DescribeInstanceBackups response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of backups
        :type TotalCount: int
        :param BackupSet: Array of instance backups
        :type BackupSet: list of RedisBackupSet
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupSet") is not None:
            self.BackupSet = []
            for item in params.get("BackupSet"):
                obj = RedisBackupSet()
                obj._deserialize(item)
                self.BackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceDealDetailRequest(AbstractModel):
    """DescribeInstanceDealDetail request structure.

    """

    def __init__(self):
        """
        :param DealIds: Array of order IDs
        :type DealIds: list of str
        """
        self.DealIds = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")


class DescribeInstanceDealDetailResponse(AbstractModel):
    """DescribeInstanceDealDetail response structure.

    """

    def __init__(self):
        """
        :param DealDetails: Order details
        :type DealDetails: list of TradeDealDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DealDetails") is not None:
            self.DealDetails = []
            for item in params.get("DealDetails"):
                obj = TradeDealDetail()
                obj._deserialize(item)
                self.DealDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyRequest(AbstractModel):
    """DescribeInstanceMonitorBigKey request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ReqType: Request type. 1: string type; 2: all types
        :type ReqType: int
        :param Date: Time, such as "20190219"
        :type Date: str
        """
        self.InstanceId = None
        self.ReqType = None
        self.Date = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReqType = params.get("ReqType")
        self.Date = params.get("Date")


class DescribeInstanceMonitorBigKeyResponse(AbstractModel):
    """DescribeInstanceMonitorBigKey response structure.

    """

    def __init__(self):
        """
        :param Data: Big key details
        :type Data: list of BigKeyInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BigKeyInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeySizeDistRequest(AbstractModel):
    """DescribeInstanceMonitorBigKeySizeDist request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Date: Time, such as "20190219"
        :type Date: str
        """
        self.InstanceId = None
        self.Date = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")


class DescribeInstanceMonitorBigKeySizeDistResponse(AbstractModel):
    """DescribeInstanceMonitorBigKeySizeDist response structure.

    """

    def __init__(self):
        """
        :param Data: Big key size distribution details
        :type Data: list of DelayDistribution
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyTypeDistRequest(AbstractModel):
    """DescribeInstanceMonitorBigKeyTypeDist request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Date: Time, such as "20190219"
        :type Date: str
        """
        self.InstanceId = None
        self.Date = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")


class DescribeInstanceMonitorBigKeyTypeDistResponse(AbstractModel):
    """DescribeInstanceMonitorBigKeyTypeDist response structure.

    """

    def __init__(self):
        """
        :param Data: Big key type distribution details
        :type Data: list of BigKeyTypeInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BigKeyTypeInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorHotKeyRequest(AbstractModel):
    """DescribeInstanceMonitorHotKey request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SpanType: Time span. 1: real time; 2: past 30 minutes; 3: past 6 hours; 4: past 24 hours
        :type SpanType: int
        """
        self.InstanceId = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpanType = params.get("SpanType")


class DescribeInstanceMonitorHotKeyResponse(AbstractModel):
    """DescribeInstanceMonitorHotKey response structure.

    """

    def __init__(self):
        """
        :param Data: Hot key details
        :type Data: list of HotKeyInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = HotKeyInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorSIPRequest(AbstractModel):
    """DescribeInstanceMonitorSIP request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeInstanceMonitorSIPResponse(AbstractModel):
    """DescribeInstanceMonitorSIP response structure.

    """

    def __init__(self):
        """
        :param Data: Access source information
        :type Data: list of SourceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SourceInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorTookDistRequest(AbstractModel):
    """DescribeInstanceMonitorTookDist request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Date: Time, such as "20190219"
        :type Date: str
        :param SpanType: Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours
        :type SpanType: int
        """
        self.InstanceId = None
        self.Date = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        self.SpanType = params.get("SpanType")


class DescribeInstanceMonitorTookDistResponse(AbstractModel):
    """DescribeInstanceMonitorTookDist response structure.

    """

    def __init__(self):
        """
        :param Data: Latency distribution information
        :type Data: list of DelayDistribution
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdRequest(AbstractModel):
    """DescribeInstanceMonitorTopNCmd request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SpanType: Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours
        :type SpanType: int
        """
        self.InstanceId = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpanType = params.get("SpanType")


class DescribeInstanceMonitorTopNCmdResponse(AbstractModel):
    """DescribeInstanceMonitorTopNCmd response structure.

    """

    def __init__(self):
        """
        :param Data: Access command information
        :type Data: list of SourceCommand
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SourceCommand()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdTookRequest(AbstractModel):
    """DescribeInstanceMonitorTopNCmdTook request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SpanType: Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours
        :type SpanType: int
        """
        self.InstanceId = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpanType = params.get("SpanType")


class DescribeInstanceMonitorTopNCmdTookResponse(AbstractModel):
    """DescribeInstanceMonitorTopNCmdTook response structure.

    """

    def __init__(self):
        """
        :param Data: Duration details
        :type Data: list of CommandTake
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CommandTake()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Offset, which is an integral multiple of `Limit`
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of modifications.
        :type TotalCount: int
        :param InstanceParamHistory: Information of modifications.
        :type InstanceParamHistory: list of InstanceParamHistory
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceParamHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceParamHistory") is not None:
            self.InstanceParamHistory = []
            for item in params.get("InstanceParamHistory"):
                obj = InstanceParamHistory()
                obj._deserialize(item)
                self.InstanceParamHistory.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of instance parameters
        :type TotalCount: int
        :param InstanceEnumParam: Instance parameter in Enum type
        :type InstanceEnumParam: list of InstanceEnumParam
        :param InstanceIntegerParam: Instance parameter in Integer type
        :type InstanceIntegerParam: list of InstanceIntegerParam
        :param InstanceTextParam: Instance parameter in Char type
        :type InstanceTextParam: list of InstanceTextParam
        :param InstanceMultiParam: Instance parameter in Multi type
        :type InstanceMultiParam: list of InstanceMultiParam
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceEnumParam = None
        self.InstanceIntegerParam = None
        self.InstanceTextParam = None
        self.InstanceMultiParam = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceEnumParam") is not None:
            self.InstanceEnumParam = []
            for item in params.get("InstanceEnumParam"):
                obj = InstanceEnumParam()
                obj._deserialize(item)
                self.InstanceEnumParam.append(obj)
        if params.get("InstanceIntegerParam") is not None:
            self.InstanceIntegerParam = []
            for item in params.get("InstanceIntegerParam"):
                obj = InstanceIntegerParam()
                obj._deserialize(item)
                self.InstanceIntegerParam.append(obj)
        if params.get("InstanceTextParam") is not None:
            self.InstanceTextParam = []
            for item in params.get("InstanceTextParam"):
                obj = InstanceTextParam()
                obj._deserialize(item)
                self.InstanceTextParam.append(obj)
        if params.get("InstanceMultiParam") is not None:
            self.InstanceMultiParam = []
            for item in params.get("InstanceMultiParam"):
                obj = InstanceMultiParam()
                obj._deserialize(item)
                self.InstanceMultiParam.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceSecurityGroupRequest(AbstractModel):
    """DescribeInstanceSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance list
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeInstanceSecurityGroupResponse(AbstractModel):
    """DescribeInstanceSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param InstanceSecurityGroupsDetail: Security group information of an instance
        :type InstanceSecurityGroupsDetail: list of InstanceSecurityGroupDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceSecurityGroupsDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSecurityGroupsDetail") is not None:
            self.InstanceSecurityGroupsDetail = []
            for item in params.get("InstanceSecurityGroupsDetail"):
                obj = InstanceSecurityGroupDetail()
                obj._deserialize(item)
                self.InstanceSecurityGroupsDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceShardsRequest(AbstractModel):
    """DescribeInstanceShards request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param FilterSlave: Whether to filter out the slave node information
        :type FilterSlave: bool
        """
        self.InstanceId = None
        self.FilterSlave = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FilterSlave = params.get("FilterSlave")


class DescribeInstanceShardsResponse(AbstractModel):
    """DescribeInstanceShards response structure.

    """

    def __init__(self):
        """
        :param InstanceShards: Information list of instance shards
        :type InstanceShards: list of InstanceClusterShard
        :param TotalCount: Total number of instance shard nodes
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceShards = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceShards") is not None:
            self.InstanceShards = []
            for item in params.get("InstanceShards"):
                obj = InstanceClusterShard()
                obj._deserialize(item)
                self.InstanceShards.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        """
        :param Limit: Instance list size. Default value: 20
        :type Limit: int
        :param Offset: Offset, which is an integral multiple of `Limit`
        :type Offset: int
        :param InstanceId: Instance ID, such as crs-6ubhgouj
        :type InstanceId: str
        :param OrderBy: Enumerated values: projectId, createtime, instancename, type, curDeadline
        :type OrderBy: str
        :param OrderType: 1: reverse; 0: sequential; reverse by default
        :type OrderType: int
        :param VpcIds: Array of VPC IDs such as 47525. The array subscript starts from 0. If this parameter is not passed in, the basic network will be selected by default
        :type VpcIds: list of str
        :param SubnetIds: Array of subnet IDs such as 56854. The array subscript starts from 0
        :type SubnetIds: list of str
        :param ProjectIds: Array of project IDs. The array subscript starts from 0
        :type ProjectIds: list of int
        :param SearchKey: ID of the instance to be searched for.
        :type SearchKey: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param UniqVpcIds: Array of VPC IDs such as vpc-sad23jfdfk. The array subscript starts from 0. If this parameter is not passed in, the basic network will be selected by default
        :type UniqVpcIds: list of str
        :param UniqSubnetIds: Array of subnet IDs such as subnet-fdj24n34j2. The array subscript starts from 0
        :type UniqSubnetIds: list of str
        :param RegionIds: Region ID, which has already been disused. The corresponding region can be queried through the common parameter `Region`
        :type RegionIds: list of int
        :param Status: Instance status. 0: to be initialized; 1: in process; 2: running; -2: isolated; -3: to be deleted
        :type Status: list of int
        :param TypeVersion: Type edition. 1: standalone edition; 2: master-slave edition; 3: cluster edition
        :type TypeVersion: int
        :param EngineName: Engine information: Redis-2.8, Redis-4.0, CKV
        :type EngineName: str
        :param AutoRenew: Renewal mode. 0: default status (manual renewal); 1: auto-renewal enabled; 2: auto-renewal disabled
        :type AutoRenew: list of int
        :param BillingMode: Billing method. postpaid: pay-as-you-go; prepaid: monthly subscription
        :type BillingMode: str
        :param Type: Instance type. 1: legacy Redis Cluster Edition, 2: Redis 2.8 Master-Slave Edition, 3: CKV Master-Slave Edition, 4: CKV Cluster Edition, 5: Redis 2.8 Standalone Edition, 6: Redis 4.0 Master-Slave Edition, 7: Redis 4.0 Cluster Edition, 8: Redis 5.0 Master-Slave Edition, 9: Redis 5.0 Cluster Edition,
        :type Type: int
        :param SearchKeys: Search keywords, which can be instance ID, instance name, or complete IP
        :type SearchKeys: list of str
        :param TypeList: Internal parameter, which can be ignored
        :type TypeList: list of int
        """
        self.Limit = None
        self.Offset = None
        self.InstanceId = None
        self.OrderBy = None
        self.OrderType = None
        self.VpcIds = None
        self.SubnetIds = None
        self.ProjectIds = None
        self.SearchKey = None
        self.InstanceName = None
        self.UniqVpcIds = None
        self.UniqSubnetIds = None
        self.RegionIds = None
        self.Status = None
        self.TypeVersion = None
        self.EngineName = None
        self.AutoRenew = None
        self.BillingMode = None
        self.Type = None
        self.SearchKeys = None
        self.TypeList = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InstanceId = params.get("InstanceId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.VpcIds = params.get("VpcIds")
        self.SubnetIds = params.get("SubnetIds")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKey = params.get("SearchKey")
        self.InstanceName = params.get("InstanceName")
        self.UniqVpcIds = params.get("UniqVpcIds")
        self.UniqSubnetIds = params.get("UniqSubnetIds")
        self.RegionIds = params.get("RegionIds")
        self.Status = params.get("Status")
        self.TypeVersion = params.get("TypeVersion")
        self.EngineName = params.get("EngineName")
        self.AutoRenew = params.get("AutoRenew")
        self.BillingMode = params.get("BillingMode")
        self.Type = params.get("Type")
        self.SearchKeys = params.get("SearchKeys")
        self.TypeList = params.get("TypeList")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of instances
        :type TotalCount: int
        :param InstanceSet: List of instance details
        :type InstanceSet: list of InstanceSet
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = InstanceSet()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductInfoRequest(AbstractModel):
    """DescribeProductInfo request structure.

    """


class DescribeProductInfoResponse(AbstractModel):
    """DescribeProductInfo response structure.

    """

    def __init__(self):
        """
        :param RegionSet: Sale information of a region
        :type RegionSet: list of RegionConf
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionConf()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupRequest(AbstractModel):
    """DescribeProjectSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param ProjectId: 0: default project; -1: all projects; >0: specified project
        :type ProjectId: int
        :param SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        """
        self.ProjectId = None
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroupId = params.get("SecurityGroupId")


class DescribeProjectSecurityGroupResponse(AbstractModel):
    """DescribeProjectSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param SecurityGroupDetails: Security group of a project
        :type SecurityGroupDetails: list of SecurityGroupDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityGroupDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupDetails") is not None:
            self.SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self.SecurityGroupDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    """DescribeSlowLog request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param BeginTime: Start time
        :type BeginTime: str
        :param EndTime: End time
        :type EndTime: str
        :param MinQueryTime: Slow log threshold in microseconds
        :type MinQueryTime: int
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Offset, which is an integral multiple of `Limit`
        :type Offset: int
        """
        self.InstanceId = None
        self.BeginTime = None
        self.EndTime = None
        self.MinQueryTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.MinQueryTime = params.get("MinQueryTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSlowLogResponse(AbstractModel):
    """DescribeSlowLog response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of slow logs
        :type TotalCount: int
        :param InstanceSlowlogDetail: Slow log details
        :type InstanceSlowlogDetail: list of InstanceSlowlogDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSlowlogDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSlowlogDetail") is not None:
            self.InstanceSlowlogDetail = []
            for item in params.get("InstanceSlowlogDetail"):
                obj = InstanceSlowlogDetail()
                obj._deserialize(item)
                self.InstanceSlowlogDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo request structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo response structure.

    """

    def __init__(self):
        """
        :param Status: Task status. preparing: to be run; running: running; succeed: succeeded; failed: failed; error: running error.
        :type Status: str
        :param StartTime: Task start time
        :type StartTime: str
        :param TaskType: Task type
        :type TaskType: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param TaskMessage: Task message, which is displayed in case of an error. It will be blank if the status is running or succeeded
        :type TaskMessage: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.StartTime = None
        self.TaskType = None
        self.InstanceId = None
        self.TaskMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.TaskType = params.get("TaskType")
        self.InstanceId = params.get("InstanceId")
        self.TaskMessage = params.get("TaskMessage")
        self.RequestId = params.get("RequestId")


class DescribeTaskListRequest(AbstractModel):
    """DescribeTaskList request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Offset, which is an integral multiple of `Limit` (rounded down automatically)
        :type Offset: int
        :param ProjectIds: Project ID
        :type ProjectIds: list of int
        :param TaskTypes: Task type
        :type TaskTypes: list of str
        :param BeginTime: Start time
        :type BeginTime: str
        :param EndTime: End time
        :type EndTime: str
        :param TaskStatus: Task status
        :type TaskStatus: list of int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Limit = None
        self.Offset = None
        self.ProjectIds = None
        self.TaskTypes = None
        self.BeginTime = None
        self.EndTime = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ProjectIds = params.get("ProjectIds")
        self.TaskTypes = params.get("TaskTypes")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TaskStatus = params.get("TaskStatus")


class DescribeTaskListResponse(AbstractModel):
    """DescribeTaskList response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of tasks
        :type TotalCount: int
        :param Tasks: Task details
        :type Tasks: list of TaskInfoDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfoDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyPostpaidInstanceRequest(AbstractModel):
    """DestroyPostpaidInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DestroyPostpaidInstanceResponse(AbstractModel):
    """DestroyPostpaidInstance response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DestroyPrepaidInstanceRequest(AbstractModel):
    """DestroyPrepaidInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DestroyPrepaidInstanceResponse(AbstractModel):
    """DestroyPrepaidInstance response structure.

    """

    def __init__(self):
        """
        :param DealId: Order ID
        :type DealId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class DisableReplicaReadonlyRequest(AbstractModel):
    """DisableReplicaReadonly request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Serial ID of an instance
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DisableReplicaReadonlyResponse(AbstractModel):
    """DisableReplicaReadonly response structure.

    """

    def __init__(self):
        """
        :param Status: ERROR: failure; OK: success
        :type Status: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class EnableReplicaReadonlyRequest(AbstractModel):
    """EnableReplicaReadonly request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Serial ID of an instance
        :type InstanceId: str
        :param ReadonlyPolicy: Account routing policy. If `master` or `replication` is entered, it means to route to the master or slave node; if this is left blank, it means to write into the master node and read from the slave node by default
        :type ReadonlyPolicy: list of str
        """
        self.InstanceId = None
        self.ReadonlyPolicy = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReadonlyPolicy = params.get("ReadonlyPolicy")


class EnableReplicaReadonlyResponse(AbstractModel):
    """EnableReplicaReadonly response structure.

    """

    def __init__(self):
        """
        :param Status: ERROR: erroneous; OK: correct.
        :type Status: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class HotKeyInfo(AbstractModel):
    """Hot key details

    """

    def __init__(self):
        """
        :param Key: Hot key
        :type Key: str
        :param Type: Type
        :type Type: str
        :param Count: Count
        :type Count: int
        """
        self.Key = None
        self.Type = None
        self.Count = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Count = params.get("Count")


class InstanceClusterNode(AbstractModel):
    """Instance node type

    """

    def __init__(self):
        """
        :param Name: Node name
        :type Name: str
        :param RunId: ID of the runtime node of an instance
        :type RunId: str
        :param Role: Cluster role. 0: master; 1: slave
        :type Role: int
        :param Status: Node status. 0: readwrite; 1: read; 2: backup
        :type Status: int
        :param Connected: Service status. 0: down; 1: on
        :type Connected: int
        :param CreateTime: Node creation time
        :type CreateTime: str
        :param DownTime: Node deactivation time
        :type DownTime: str
        :param Slots: Distribution of node slots
        :type Slots: str
        :param Keys: Distribution of node keys
        :type Keys: int
        :param Qps: Node QPS
        :type Qps: int
        :param QpsSlope: QPS slope of a node
        :type QpsSlope: float
        :param Storage: Node storage
        :type Storage: int
        :param StorageSlope: Storage slope of a node
        :type StorageSlope: float
        """
        self.Name = None
        self.RunId = None
        self.Role = None
        self.Status = None
        self.Connected = None
        self.CreateTime = None
        self.DownTime = None
        self.Slots = None
        self.Keys = None
        self.Qps = None
        self.QpsSlope = None
        self.Storage = None
        self.StorageSlope = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RunId = params.get("RunId")
        self.Role = params.get("Role")
        self.Status = params.get("Status")
        self.Connected = params.get("Connected")
        self.CreateTime = params.get("CreateTime")
        self.DownTime = params.get("DownTime")
        self.Slots = params.get("Slots")
        self.Keys = params.get("Keys")
        self.Qps = params.get("Qps")
        self.QpsSlope = params.get("QpsSlope")
        self.Storage = params.get("Storage")
        self.StorageSlope = params.get("StorageSlope")


class InstanceClusterShard(AbstractModel):
    """Information list of instance shards

    """

    def __init__(self):
        """
        :param ShardName: Shard node name
        :type ShardName: str
        :param ShardId: Shard node ID
        :type ShardId: str
        :param Role: Role
        :type Role: int
        :param Keys: Number of keys
        :type Keys: int
        :param Slots: Slot information
        :type Slots: str
        :param Storage: Storage capacity
        :type Storage: int
        :param StorageSlope: Capacity slope
        :type StorageSlope: float
        :param Runid: ID of the runtime node of an instance
        :type Runid: str
        :param Connected: Service status. 0: down; 1: on
        :type Connected: int
        """
        self.ShardName = None
        self.ShardId = None
        self.Role = None
        self.Keys = None
        self.Slots = None
        self.Storage = None
        self.StorageSlope = None
        self.Runid = None
        self.Connected = None


    def _deserialize(self, params):
        self.ShardName = params.get("ShardName")
        self.ShardId = params.get("ShardId")
        self.Role = params.get("Role")
        self.Keys = params.get("Keys")
        self.Slots = params.get("Slots")
        self.Storage = params.get("Storage")
        self.StorageSlope = params.get("StorageSlope")
        self.Runid = params.get("Runid")
        self.Connected = params.get("Connected")


class InstanceEnumParam(AbstractModel):
    """Descriptions of enumeration parameters of the instance

    """

    def __init__(self):
        """
        :param ParamName: Parameter name
        :type ParamName: str
        :param ValueType: Parameter type: Enum
        :type ValueType: str
        :param NeedRestart: Whether restart is required after a modification is made. Value range: true, false
        :type NeedRestart: str
        :param DefaultValue: Default value of the parameter
        :type DefaultValue: str
        :param CurrentValue: Current value of a parameter
        :type CurrentValue: str
        :param Tips: Parameter description
        :type Tips: str
        :param EnumValue: Value range of a parameter
        :type EnumValue: list of str
        :param Status: Parameter status. 1: modifying; 2: modified
        :type Status: int
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.EnumValue = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.EnumValue = params.get("EnumValue")
        self.Status = params.get("Status")


class InstanceIntegerParam(AbstractModel):
    """Descriptions of integer parameters of the instance

    """

    def __init__(self):
        """
        :param ParamName: Parameter name
        :type ParamName: str
        :param ValueType: Parameter type: Integer
        :type ValueType: str
        :param NeedRestart: Whether restart is required after a modification is made. Value range: true, false
        :type NeedRestart: str
        :param DefaultValue: Default value of the parameter
        :type DefaultValue: str
        :param CurrentValue: Current value of a parameter
        :type CurrentValue: str
        :param Tips: Parameter description
        :type Tips: str
        :param Min: Minimum value of a parameter
        :type Min: str
        :param Max: Maximum value of a parameter
        :type Max: str
        :param Status: Parameter status. 1: modifying; 2: modified
        :type Status: int
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.Min = None
        self.Max = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        self.Status = params.get("Status")


class InstanceMultiParam(AbstractModel):
    """Description of an instance parameter in Multi type

    """

    def __init__(self):
        """
        :param ParamName: Parameter name
        :type ParamName: str
        :param ValueType: Parameter type: Multi
        :type ValueType: str
        :param NeedRestart: Whether restart is required after a modification is made. Value range: true, false
        :type NeedRestart: str
        :param DefaultValue: Default value of the parameter
        :type DefaultValue: str
        :param CurrentValue: Current value of a parameter
        :type CurrentValue: str
        :param Tips: Parameter description
        :type Tips: str
        :param EnumValue: Parameter description
        :type EnumValue: str
        :param Status: Parameter status. 1: modifying; 2: modified
        :type Status: int
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.EnumValue = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.EnumValue = params.get("EnumValue")
        self.Status = params.get("Status")


class InstanceNode(AbstractModel):
    """Instance node

    """

    def __init__(self):
        """
        :param Id: Id
        :type Id: int
        :param InstanceClusterNode: Node details
        :type InstanceClusterNode: list of InstanceClusterNode
        """
        self.Id = None
        self.InstanceClusterNode = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        if params.get("InstanceClusterNode") is not None:
            self.InstanceClusterNode = []
            for item in params.get("InstanceClusterNode"):
                obj = InstanceClusterNode()
                obj._deserialize(item)
                self.InstanceClusterNode.append(obj)


class InstanceParam(AbstractModel):
    """Instance parameter

    """

    def __init__(self):
        """
        :param Key: Sets a parameter name
        :type Key: str
        :param Value: Sets a parameter value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class InstanceParamHistory(AbstractModel):
    """History of instance parameter modifications

    """

    def __init__(self):
        """
        :param ParamName: Parameter name
        :type ParamName: str
        :param PreValue: Value before modification
        :type PreValue: str
        :param NewValue: Value after modification
        :type NewValue: str
        :param Status: Status. 1: modifying parameter configuration; 2: parameter configuration modified successfully; 3: failed to modify parameter configuration
        :type Status: int
        :param ModifyTime: Modification time
        :type ModifyTime: str
        """
        self.ParamName = None
        self.PreValue = None
        self.NewValue = None
        self.Status = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.PreValue = params.get("PreValue")
        self.NewValue = params.get("NewValue")
        self.Status = params.get("Status")
        self.ModifyTime = params.get("ModifyTime")


class InstanceSecurityGroupDetail(AbstractModel):
    """Security group information of an instance

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SecurityGroupDetails: Security group information
        :type SecurityGroupDetails: list of SecurityGroupDetail
        """
        self.InstanceId = None
        self.SecurityGroupDetails = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("SecurityGroupDetails") is not None:
            self.SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self.SecurityGroupDetails.append(obj)


class InstanceSet(AbstractModel):
    """List of instance details

    """

    def __init__(self):
        """
        :param InstanceName: Instance name
        :type InstanceName: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Appid: User's Appid
        :type Appid: int
        :param ProjectId: Project ID
        :type ProjectId: int
        :param RegionId: Region ID. 1: Guangzhou; 4: Shanghai; 5: Hong Kong, China; 6: Toronto; 7: Shanghai Finance; 8: Beijing; 9: Singapore; 11: Shenzhen Finance; 15: West US (Silicon Valley); 16: Chengdu; 17: Germany; 18: South Korea; 19: Chongqing; 21: India; 22: East US (Virginia); 23: Thailand; 24: Russia; 25: Japan
        :type RegionId: int
        :param ZoneId: Region ID
        :type ZoneId: int
        :param VpcId: VPC ID, such as 75101
        :type VpcId: int
        :param SubnetId: VPC subnet ID, such as 46315
        :type SubnetId: int
        :param Status: Current instance status. 0: to be initialized; 1: instance in process; 2: instance running; -2: instance isolated; -3: instance to be deleted
        :type Status: int
        :param WanIp: Instance VIP
        :type WanIp: str
        :param Port: Port number of an instance
        :type Port: int
        :param Createtime: Instance creation time
        :type Createtime: str
        :param Size: Instance capacity in MB
        :type Size: float
        :param SizeUsed: This field has been disused
        :type SizeUsed: float
        :param Type: Instance type. 1: Redis 2.8 cluster edition; 2: Redis 2.8 master-slave edition; 3: CKV master-slave edition (Redis 3.2); 4: CKV cluster edition (Redis 3.2); 5: Redis 2.8 standalone edition; 6: Redis 4.0 master-slave edition; 7: Redis 4.0 cluster edition
        :type Type: int
        :param AutoRenewFlag: Whether to set the auto-renewal flag for an instance. 1: auto-renewal set; 0: auto-renewal not set
        :type AutoRenewFlag: int
        :param DeadlineTime: Instance expiration time
        :type DeadlineTime: str
        :param Engine: Engine: Redis community edition, Tencent Cloud CKV
        :type Engine: str
        :param ProductType: Product type: Redis 2.8 cluster edition, Redis 2.8 master-slave edition, Redis 3.2 master-slave edition (CKV master-slave edition), Redis 3.2 cluster edition (CKV cluster edition), Redis 2.8 standalone edition, Redis 4.0 cluster edition
        :type ProductType: str
        :param UniqVpcId: VPC ID, such as vpc-fk33jsf43kgv
        :type UniqVpcId: str
        :param UniqSubnetId: VPC subnet ID, such as subnet-fd3j6l35mm0
        :type UniqSubnetId: str
        :param BillingMode: Billing method. 0: pay-as-you-go; 1: monthly subscription
        :type BillingMode: int
        :param InstanceTitle: Description of an instance status, such as "instance running"
        :type InstanceTitle: str
        :param OfflineTime: Scheduled deactivation time
        :type OfflineTime: str
        :param SubStatus: Sub-status returned for an instance in process
        :type SubStatus: int
        :param Tags: Anti-affinity tag
        :type Tags: list of str
        :param InstanceNode: Instance node information
        :type InstanceNode: list of InstanceNode
        :param RedisShardSize: Shard size
        :type RedisShardSize: int
        :param RedisShardNum: Number of shards
        :type RedisShardNum: int
        :param RedisReplicasNum: Number of replicas
        :type RedisReplicasNum: int
        :param PriceId: Billing ID
        :type PriceId: int
        :param CloseTime: Isolation time
        :type CloseTime: str
        :param SlaveReadWeight: Read weight of a slave node
        :type SlaveReadWeight: int
        :param InstanceTags: Instance tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceTags: list of InstanceTagInfo
        :param ProjectName: Project name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param NoAuth: Whether an instance is password-free. true: yes; false: no
Note: This field may return null, indicating that no valid values can be obtained.
        :type NoAuth: bool
        :param ClientLimit: Number of client connections
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientLimit: int
        :param DtsStatus: DTS status (internal parameter, which can be ignored)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DtsStatus: int
        :param NetLimit: Upper shard bandwidth limit in MB
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetLimit: int
        :param PasswordFree: Password-free instance flag (internal parameter, which can be ignored)
Note: this field may return null, indicating that no valid values can be obtained.
        :type PasswordFree: int
        :param ReadOnly: Read-only instance flag (internal parameter, which can be ignored)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReadOnly: int
        :param Vip6: Internal parameter, which can be ignored
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vip6: str
        :param RemainBandwidthDuration: Internal parameter, which can be ignored
Note: this field may return null, indicating that no valid values can be obtained.
        :type RemainBandwidthDuration: str
        """
        self.InstanceName = None
        self.InstanceId = None
        self.Appid = None
        self.ProjectId = None
        self.RegionId = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.WanIp = None
        self.Port = None
        self.Createtime = None
        self.Size = None
        self.SizeUsed = None
        self.Type = None
        self.AutoRenewFlag = None
        self.DeadlineTime = None
        self.Engine = None
        self.ProductType = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.BillingMode = None
        self.InstanceTitle = None
        self.OfflineTime = None
        self.SubStatus = None
        self.Tags = None
        self.InstanceNode = None
        self.RedisShardSize = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.PriceId = None
        self.CloseTime = None
        self.SlaveReadWeight = None
        self.InstanceTags = None
        self.ProjectName = None
        self.NoAuth = None
        self.ClientLimit = None
        self.DtsStatus = None
        self.NetLimit = None
        self.PasswordFree = None
        self.ReadOnly = None
        self.Vip6 = None
        self.RemainBandwidthDuration = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.Appid = params.get("Appid")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.WanIp = params.get("WanIp")
        self.Port = params.get("Port")
        self.Createtime = params.get("Createtime")
        self.Size = params.get("Size")
        self.SizeUsed = params.get("SizeUsed")
        self.Type = params.get("Type")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Engine = params.get("Engine")
        self.ProductType = params.get("ProductType")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.BillingMode = params.get("BillingMode")
        self.InstanceTitle = params.get("InstanceTitle")
        self.OfflineTime = params.get("OfflineTime")
        self.SubStatus = params.get("SubStatus")
        self.Tags = params.get("Tags")
        if params.get("InstanceNode") is not None:
            self.InstanceNode = []
            for item in params.get("InstanceNode"):
                obj = InstanceNode()
                obj._deserialize(item)
                self.InstanceNode.append(obj)
        self.RedisShardSize = params.get("RedisShardSize")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.PriceId = params.get("PriceId")
        self.CloseTime = params.get("CloseTime")
        self.SlaveReadWeight = params.get("SlaveReadWeight")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.ProjectName = params.get("ProjectName")
        self.NoAuth = params.get("NoAuth")
        self.ClientLimit = params.get("ClientLimit")
        self.DtsStatus = params.get("DtsStatus")
        self.NetLimit = params.get("NetLimit")
        self.PasswordFree = params.get("PasswordFree")
        self.ReadOnly = params.get("ReadOnly")
        self.Vip6 = params.get("Vip6")
        self.RemainBandwidthDuration = params.get("RemainBandwidthDuration")


class InstanceSlowlogDetail(AbstractModel):
    """Slow log details

    """

    def __init__(self):
        """
        :param Duration: Slow log duration
        :type Duration: int
        :param Client: Client address
        :type Client: str
        :param Command: Command
        :type Command: str
        :param CommandLine: Command line details
        :type CommandLine: str
        :param ExecuteTime: Execution duration
        :type ExecuteTime: str
        """
        self.Duration = None
        self.Client = None
        self.Command = None
        self.CommandLine = None
        self.ExecuteTime = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.Client = params.get("Client")
        self.Command = params.get("Command")
        self.CommandLine = params.get("CommandLine")
        self.ExecuteTime = params.get("ExecuteTime")


class InstanceTagInfo(AbstractModel):
    """Instance tag information

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


class InstanceTextParam(AbstractModel):
    """Descriptions of text parameters of the instance

    """

    def __init__(self):
        """
        :param ParamName: Parameter name
        :type ParamName: str
        :param ValueType: Parameter type: Text
        :type ValueType: str
        :param NeedRestart: Whether restart is required after a modification is made. Value range: true, false
        :type NeedRestart: str
        :param DefaultValue: Default value of the parameter
        :type DefaultValue: str
        :param CurrentValue: Current value of a parameter
        :type CurrentValue: str
        :param Tips: Parameter description
        :type Tips: str
        :param TextValue: Value range of a parameter
        :type TextValue: list of str
        :param Status: Parameter status. 1: modifying; 2: modified
        :type Status: int
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.TextValue = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.TextValue = params.get("TextValue")
        self.Status = params.get("Status")


class ManualBackupInstanceRequest(AbstractModel):
    """ManualBackupInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the instance to be operated on, which can be obtained through the `InstanceId` field in the return value of the DescribeInstance API.
        :type InstanceId: str
        :param Remark: Backup remarks
        :type Remark: str
        """
        self.InstanceId = None
        self.Remark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Remark = params.get("Remark")


class ManualBackupInstanceResponse(AbstractModel):
    """ManualBackupInstance response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModfiyInstancePasswordRequest(AbstractModel):
    """ModfiyInstancePassword request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param OldPassword: Old password of an instance
        :type OldPassword: str
        :param Password: New password of an instance
        :type Password: str
        """
        self.InstanceId = None
        self.OldPassword = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldPassword = params.get("OldPassword")
        self.Password = params.get("Password")


class ModfiyInstancePasswordResponse(AbstractModel):
    """ModfiyInstancePassword response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyAutoBackupConfigRequest(AbstractModel):
    """ModifyAutoBackupConfig request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param WeekDays: Date. Value range: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
        :type WeekDays: list of str
        :param TimePeriod: Time period. Value range: 00:00-01:00, 01:00-02:00...... 23:00-00:00
        :type TimePeriod: str
        :param AutoBackupType: Auto backup type: 1 "scheduled rollback"
        :type AutoBackupType: int
        """
        self.InstanceId = None
        self.WeekDays = None
        self.TimePeriod = None
        self.AutoBackupType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.AutoBackupType = params.get("AutoBackupType")


class ModifyAutoBackupConfigResponse(AbstractModel):
    """ModifyAutoBackupConfig response structure.

    """

    def __init__(self):
        """
        :param AutoBackupType: Auto backup type: 1 "scheduled rollback"
        :type AutoBackupType: int
        :param WeekDays: Date. Value range: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.
        :type WeekDays: list of str
        :param TimePeriod: Time period. Value range: 00:00-01:00, 01:00-02:00...... 23:00-00:00
        :type TimePeriod: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AutoBackupType = None
        self.WeekDays = None
        self.TimePeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoBackupType = params.get("AutoBackupType")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.RequestId = params.get("RequestId")


class ModifyInstanceAccountRequest(AbstractModel):
    """ModifyInstanceAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AccountName: Sub-account name. If the root account is to be modified, enter `root`
        :type AccountName: str
        :param AccountPassword: Sub-account password
        :type AccountPassword: str
        :param Remark: Sub-account description information
        :type Remark: str
        :param ReadonlyPolicy: Sub-account routing policy. Enter `master` to route to the master node or `slave` to route to the slave node
        :type ReadonlyPolicy: list of str
        :param Privilege: Sub-account read/write policy. Enter `r` for read-only, `w` for write-only, or `rw` for read/write
        :type Privilege: str
        :param NoAuth: true: make the root account password-free. This is applicable to root accounts only; sub-accounts cannot be made password-free
        :type NoAuth: bool
        """
        self.InstanceId = None
        self.AccountName = None
        self.AccountPassword = None
        self.Remark = None
        self.ReadonlyPolicy = None
        self.Privilege = None
        self.NoAuth = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AccountName = params.get("AccountName")
        self.AccountPassword = params.get("AccountPassword")
        self.Remark = params.get("Remark")
        self.ReadonlyPolicy = params.get("ReadonlyPolicy")
        self.Privilege = params.get("Privilege")
        self.NoAuth = params.get("NoAuth")


class ModifyInstanceAccountResponse(AbstractModel):
    """ModifyInstanceAccount response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceParamsRequest(AbstractModel):
    """ModifyInstanceParams request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceParams: List of instance parameters modified
        :type InstanceParams: list of InstanceParam
        """
        self.InstanceId = None
        self.InstanceParams = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("InstanceParams") is not None:
            self.InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self.InstanceParams.append(obj)


class ModifyInstanceParamsResponse(AbstractModel):
    """ModifyInstanceParams response structure.

    """

    def __init__(self):
        """
        :param Changed: Whether a modification is successfully made.
        :type Changed: bool
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Changed = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Changed = params.get("Changed")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        """
        :param Operation: Instance modification type. rename: rename an instance; modifyProject: modify the project of an instance; modifyAutoRenew: modify the auto-renewal flag of an instance
        :type Operation: str
        :param InstanceIds: Instance ID
        :type InstanceIds: list of str
        :param InstanceNames: New name of instance
        :type InstanceNames: list of str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param AutoRenews: Auto-renewal flag. 0: default status (manual renewal), 1: auto-renewal enabled, 2: auto-renewal disabled
        :type AutoRenews: list of int
        :param InstanceId: Disused
        :type InstanceId: str
        :param InstanceName: Disused
        :type InstanceName: str
        :param AutoRenew: Disused
        :type AutoRenew: int
        """
        self.Operation = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.ProjectId = None
        self.AutoRenews = None
        self.InstanceId = None
        self.InstanceName = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenews = params.get("AutoRenews")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AutoRenew = params.get("AutoRenew")


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkConfigRequest(AbstractModel):
    """ModifyNetworkConfig request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Operation: Operation type. changeVip: modify the VIP of an instance; changeVpc: modify the subnet of an instance; changeBaseToVpc: change from basic network to VPC
        :type Operation: str
        :param Vip: VIP address, which is required for the `changeVip` operation. If this parameter is left blank, a random one will be assigned by default
        :type Vip: str
        :param VpcId: VPC ID, which is required for `changeVpc` and `changeBaseToVpc` operations
        :type VpcId: str
        :param SubnetId: Subnet ID, which is required for `changeVpc` and `changeBaseToVpc` operations
        :type SubnetId: str
        """
        self.InstanceId = None
        self.Operation = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Operation = params.get("Operation")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class ModifyNetworkConfigResponse(AbstractModel):
    """ModifyNetworkConfig response structure.

    """

    def __init__(self):
        """
        :param Status: Execution status: true or false
        :type Status: bool
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param Vip: VIP address
        :type Vip: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.SubnetId = None
        self.VpcId = None
        self.Vip = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Vip = params.get("Vip")
        self.RequestId = params.get("RequestId")


class ProductConf(AbstractModel):
    """Product information

    """

    def __init__(self):
        """
        :param Type: Product type. 2: Redis master-slave edition; 3: CKV master-slave edition; 4: CKV cluster edition; 5: Redis standalone edition; 7: Redis cluster edition
        :type Type: int
        :param TypeName: Product name: Redis master-slave edition, CKV master-slave edition, CKV cluster edition, Redis standalone edition, or Redis cluster edition
        :type TypeName: str
        :param MinBuyNum: Minimum purchasable quantity
        :type MinBuyNum: int
        :param MaxBuyNum: Maximum purchasable quantity
        :type MaxBuyNum: int
        :param Saleout: Whether a product is sold out
        :type Saleout: bool
        :param Engine: Product engine: Tencent Cloud CKV or Redis community edition
        :type Engine: str
        :param Version: Compatible version: Redis 2.8, Redis 3.2, or Redis 4.0
        :type Version: str
        :param TotalSize: Total capacity in GB
        :type TotalSize: list of str
        :param ShardSize: Shard size in GB
        :type ShardSize: list of str
        :param ReplicaNum: Number of replicas
        :type ReplicaNum: list of str
        :param ShardNum: Number of shards
        :type ShardNum: list of str
        :param PayMode: Supported billing method. 1: monthly subscription; 0: pay-as-you-go
        :type PayMode: str
        :param EnableRepicaReadOnly: Whether to support read-only replicas
        :type EnableRepicaReadOnly: bool
        """
        self.Type = None
        self.TypeName = None
        self.MinBuyNum = None
        self.MaxBuyNum = None
        self.Saleout = None
        self.Engine = None
        self.Version = None
        self.TotalSize = None
        self.ShardSize = None
        self.ReplicaNum = None
        self.ShardNum = None
        self.PayMode = None
        self.EnableRepicaReadOnly = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TypeName = params.get("TypeName")
        self.MinBuyNum = params.get("MinBuyNum")
        self.MaxBuyNum = params.get("MaxBuyNum")
        self.Saleout = params.get("Saleout")
        self.Engine = params.get("Engine")
        self.Version = params.get("Version")
        self.TotalSize = params.get("TotalSize")
        self.ShardSize = params.get("ShardSize")
        self.ReplicaNum = params.get("ReplicaNum")
        self.ShardNum = params.get("ShardNum")
        self.PayMode = params.get("PayMode")
        self.EnableRepicaReadOnly = params.get("EnableRepicaReadOnly")


class RedisBackupSet(AbstractModel):
    """Array of instance backups

    """

    def __init__(self):
        """
        :param StartTime: Backup start time
        :type StartTime: str
        :param BackupId: Backup ID
        :type BackupId: str
        :param BackupType: Backup type. manualBackupInstance: manual backup initiated by user; systemBackupInstance: midnight backup initiated by system
        :type BackupType: str
        :param Status: Backup status. 1: backup is locked by another process; 2: backup is normal and not locked by any process; -1: backup has expired; 3: backup is being exported; 4: backup is exported successfully
        :type Status: int
        :param Remark: Backup remarks
        :type Remark: str
        :param Locked: Whether a backup is locked. 0: no; 1: yes
        :type Locked: int
        """
        self.StartTime = None
        self.BackupId = None
        self.BackupType = None
        self.Status = None
        self.Remark = None
        self.Locked = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.BackupId = params.get("BackupId")
        self.BackupType = params.get("BackupType")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.Locked = params.get("Locked")


class RegionConf(AbstractModel):
    """Region information

    """

    def __init__(self):
        """
        :param RegionId: Region ID
        :type RegionId: str
        :param RegionName: Region name
        :type RegionName: str
        :param RegionShortName: Region abbreviation
        :type RegionShortName: str
        :param Area: Name of the area where a region is located
        :type Area: str
        :param ZoneSet: AZ information
        :type ZoneSet: list of ZoneCapacityConf
        """
        self.RegionId = None
        self.RegionName = None
        self.RegionShortName = None
        self.Area = None
        self.ZoneSet = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RegionShortName = params.get("RegionShortName")
        self.Area = params.get("Area")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneCapacityConf()
                obj._deserialize(item)
                self.ZoneSet.append(obj)


class RenewInstanceRequest(AbstractModel):
    """RenewInstance request structure.

    """

    def __init__(self):
        """
        :param Period: Length of purchase in months
        :type Period: int
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.Period = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.InstanceId = params.get("InstanceId")


class RenewInstanceResponse(AbstractModel):
    """RenewInstance response structure.

    """

    def __init__(self):
        """
        :param DealId: Transaction ID
        :type DealId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ResetPasswordRequest(AbstractModel):
    """ResetPassword request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Redis instance ID
        :type InstanceId: str
        :param Password: Password reset (this parameter can be left blank when switching to password-free instance mode and is required in other cases)
        :type Password: str
        :param NoAuth: Whether to switch to password-free instance mode. false: switch to password-enabled instance mode; true: switch to password-free instance mode. Default value: false
        :type NoAuth: bool
        """
        self.InstanceId = None
        self.Password = None
        self.NoAuth = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")
        self.NoAuth = params.get("NoAuth")


class ResetPasswordResponse(AbstractModel):
    """ResetPassword response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID (this parameter is the task ID when changing a password. If you are switching between password-free and password-enabled instance mode, you can leave this parameter alone)
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the instance to be operated on, which can be obtained through the `redisId` field in the return value of the DescribeRedis API.
        :type InstanceId: str
        :param BackupId: Backup ID, which can be obtained through the `backupId` field in the return value of the GetRedisBackupList API
        :type BackupId: str
        :param Password: Instance password, which needs to be validated during instance restoration (this parameter is not required for password-free instances)
        :type Password: str
        """
        self.InstanceId = None
        self.BackupId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")
        self.Password = params.get("Password")


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID, which can be used to query the task execution status through the DescribeTaskInfo API
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SecurityGroupDetail(AbstractModel):
    """Security group details

    """

    def __init__(self):
        """
        :param ProjectId: Project ID
        :type ProjectId: int
        :param CreateTime: Creation time
        :type CreateTime: str
        :param SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        :param InboundRule: Security group inbound rule
        :type InboundRule: list of SecurityGroupsInboundAndOutbound
        :param OutboundRule: Security group outbound rule
        :type OutboundRule: list of SecurityGroupsInboundAndOutbound
        """
        self.ProjectId = None
        self.CreateTime = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None
        self.InboundRule = None
        self.OutboundRule = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("InboundRule") is not None:
            self.InboundRule = []
            for item in params.get("InboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self.InboundRule.append(obj)
        if params.get("OutboundRule") is not None:
            self.OutboundRule = []
            for item in params.get("OutboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self.OutboundRule.append(obj)


class SecurityGroupsInboundAndOutbound(AbstractModel):
    """Inbound and outbound rules of the security group

    """

    def __init__(self):
        """
        :param Action: Action to be executed
        :type Action: str
        :param Ip: IP address
        :type Ip: str
        :param Port: Port number
        :type Port: str
        :param Proto: Protocol type
        :type Proto: str
        """
        self.Action = None
        self.Ip = None
        self.Port = None
        self.Proto = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Proto = params.get("Proto")


class SourceCommand(AbstractModel):
    """Access command

    """

    def __init__(self):
        """
        :param Cmd: Command
        :type Cmd: str
        :param Count: Number of executions
        :type Count: int
        """
        self.Cmd = None
        self.Count = None


    def _deserialize(self, params):
        self.Cmd = params.get("Cmd")
        self.Count = params.get("Count")


class SourceInfo(AbstractModel):
    """Access source information

    """

    def __init__(self):
        """
        :param Ip: Source IP
        :type Ip: str
        :param Conn: Number of connections
        :type Conn: int
        :param Cmd: Command
        :type Cmd: int
        """
        self.Ip = None
        self.Conn = None
        self.Cmd = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Conn = params.get("Conn")
        self.Cmd = params.get("Cmd")


class StartupInstanceRequest(AbstractModel):
    """StartupInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class StartupInstanceResponse(AbstractModel):
    """StartupInstance response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class TaskInfoDetail(AbstractModel):
    """Task details

    """

    def __init__(self):
        """
        :param TaskId: Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param StartTime: Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param TaskType: Task type
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskType: str
        :param InstanceName: Instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param ProjectId: Project ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param Progress: Task progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: float
        :param EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param Result: Task status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: int
        """
        self.TaskId = None
        self.StartTime = None
        self.TaskType = None
        self.InstanceName = None
        self.InstanceId = None
        self.ProjectId = None
        self.Progress = None
        self.EndTime = None
        self.Result = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.StartTime = params.get("StartTime")
        self.TaskType = params.get("TaskType")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.ProjectId = params.get("ProjectId")
        self.Progress = params.get("Progress")
        self.EndTime = params.get("EndTime")
        self.Result = params.get("Result")


class TradeDealDetail(AbstractModel):
    """Order deal information

    """

    def __init__(self):
        """
        :param DealId: Order ID, which is used when a TencentCloud API is called
        :type DealId: str
        :param DealName: Long order ID, which is used when an order issue is submitted for assistance
        :type DealName: str
        :param ZoneId: AZ ID
        :type ZoneId: int
        :param GoodsNum: Number of instances associated with an order
        :type GoodsNum: int
        :param Creater: Creates a user uin
        :type Creater: str
        :param CreatTime: Order creation time
        :type CreatTime: str
        :param OverdueTime: Order timeout period
        :type OverdueTime: str
        :param EndTime: Order completion time
        :type EndTime: str
        :param Status: Order status. 1: unpaid; 2: paid but not delivered; 3: In delivery; 4: successfully delivered; 5: delivery failed; 6: refunded; 7: order closed; 8: order expired; 9: order invalidated; 10: product invalidated; 11: requested payment rejected; 12: paying
        :type Status: int
        :param Description: Order status description
        :type Description: str
        :param Price: Actual total price of an order in 0.01 CNY
        :type Price: int
        :param InstanceIds: Instance ID
        :type InstanceIds: list of str
        """
        self.DealId = None
        self.DealName = None
        self.ZoneId = None
        self.GoodsNum = None
        self.Creater = None
        self.CreatTime = None
        self.OverdueTime = None
        self.EndTime = None
        self.Status = None
        self.Description = None
        self.Price = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.DealName = params.get("DealName")
        self.ZoneId = params.get("ZoneId")
        self.GoodsNum = params.get("GoodsNum")
        self.Creater = params.get("Creater")
        self.CreatTime = params.get("CreatTime")
        self.OverdueTime = params.get("OverdueTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Price = params.get("Price")
        self.InstanceIds = params.get("InstanceIds")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param MemSize: Shard size in MB
        :type MemSize: int
        :param RedisShardNum: Number of shards. This parameter can be left blank for Redis 2.8 master-slave edition, CKV master-slave edition, and Redis 2.8 standalone edition
        :type RedisShardNum: int
        :param RedisReplicasNum: Number of replicas. This parameter can be left blank for Redis 2.8 master-slave edition, CKV master-slave edition, and Redis 2.8 standalone edition
        :type RedisReplicasNum: int
        """
        self.InstanceId = None
        self.MemSize = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MemSize = params.get("MemSize")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance response structure.

    """

    def __init__(self):
        """
        :param DealId: Order ID
        :type DealId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ZoneCapacityConf(AbstractModel):
    """Product information in the availability zone

    """

    def __init__(self):
        """
        :param ZoneId: AZ ID, such as ap-guangzhou-3
        :type ZoneId: str
        :param ZoneName: AZ name
        :type ZoneName: str
        :param IsSaleout: Whether a product is sold out in an AZ
        :type IsSaleout: bool
        :param IsDefault: Whether it is a default AZ
        :type IsDefault: bool
        :param NetWorkType: Network type. basenet: basic network; vpcnet: VPC
        :type NetWorkType: list of str
        :param ProductSet: Information of an AZ, such as product specifications in it
        :type ProductSet: list of ProductConf
        :param OldZoneId: AZ ID, such as 100003
        :type OldZoneId: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.IsSaleout = None
        self.IsDefault = None
        self.NetWorkType = None
        self.ProductSet = None
        self.OldZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.IsSaleout = params.get("IsSaleout")
        self.IsDefault = params.get("IsDefault")
        self.NetWorkType = params.get("NetWorkType")
        if params.get("ProductSet") is not None:
            self.ProductSet = []
            for item in params.get("ProductSet"):
                obj = ProductConf()
                obj._deserialize(item)
                self.ProductSet.append(obj)
        self.OldZoneId = params.get("OldZoneId")