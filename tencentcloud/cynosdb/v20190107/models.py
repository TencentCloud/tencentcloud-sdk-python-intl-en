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
    """Database account information

    """

    def __init__(self):
        r"""
        :param AccountName: Database account name
        :type AccountName: str
        :param Description: Database account description
        :type Description: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Host: Host
        :type Host: str
        """
        self.AccountName = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Host = None


    def _deserialize(self, params):
        self.AccountName = params.get("AccountName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateInstanceRequest(AbstractModel):
    """ActivateInstance request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIdList: List of instance IDs in the format of `cynosdbmysql-ins-n7ocdslw` as displayed in the TDSQL-C for MySQL console. You can use the instance list querying API to query the ID, i.e., the `InstanceId` value in the output parameters.
        :type InstanceIdList: list of str
        """
        self.ClusterId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateInstanceResponse(AbstractModel):
    """ActivateInstance response structure.

    """

    def __init__(self):
        r"""
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


class AddClusterSlaveZoneRequest(AbstractModel):
    """AddClusterSlaveZone request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param SlaveZone: Replica AZ
        :type SlaveZone: str
        """
        self.ClusterId = None
        self.SlaveZone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddClusterSlaveZoneResponse(AbstractModel):
    """AddClusterSlaveZone response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Async FlowId
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class AddInstancesRequest(AbstractModel):
    """AddInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Cpu: Number of CPU cores
        :type Cpu: int
        :param Memory: Memory in GB
        :type Memory: int
        :param ReadOnlyCount: Number of added read-only instances. Value range: (0,16].
        :type ReadOnlyCount: int
        :param InstanceGrpId: Instance group ID, which is used when you add an instance to an existing RO group. If this parameter is left empty, an RO group will be created. We recommend you not pass in this value on the current version.
        :type InstanceGrpId: str
        :param VpcId: VPC ID. This parameter has been disused.
        :type VpcId: str
        :param SubnetId: Subnet ID. If `VpcId` is set, `SubnetId` is required. This parameter has been disused.
        :type SubnetId: str
        :param Port: The port used when adding an RO group. Value range: [0,65535).
        :type Port: int
        :param InstanceName: Instance name. String length range: [0,64).
        :type InstanceName: str
        :param AutoVoucher: Whether to automatically select a voucher. 1: yes; 0: no. Default value: 0
        :type AutoVoucher: int
        :param DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        :param OrderSource: Order source. String length range: [0,64).
        :type OrderSource: str
        :param DealMode: Transaction mode. Valid values: `0` (place and pay for an order), `1` (place an order)
        :type DealMode: int
        """
        self.ClusterId = None
        self.Cpu = None
        self.Memory = None
        self.ReadOnlyCount = None
        self.InstanceGrpId = None
        self.VpcId = None
        self.SubnetId = None
        self.Port = None
        self.InstanceName = None
        self.AutoVoucher = None
        self.DbType = None
        self.OrderSource = None
        self.DealMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.ReadOnlyCount = params.get("ReadOnlyCount")
        self.InstanceGrpId = params.get("InstanceGrpId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Port = params.get("Port")
        self.InstanceName = params.get("InstanceName")
        self.AutoVoucher = params.get("AutoVoucher")
        self.DbType = params.get("DbType")
        self.OrderSource = params.get("OrderSource")
        self.DealMode = params.get("DealMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddInstancesResponse(AbstractModel):
    """AddInstances response structure.

    """

    def __init__(self):
        r"""
        :param TranId: Freezing transaction. One freezing transaction ID is generated each time an instance is added.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param DealNames: Pay-as-You-Go order ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param ResourceIds: List of IDs of delivered resources
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceIds: list of str
        :param BigDealIds: Big order ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BigDealIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TranId = None
        self.DealNames = None
        self.ResourceIds = None
        self.BigDealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.DealNames = params.get("DealNames")
        self.ResourceIds = params.get("ResourceIds")
        self.BigDealIds = params.get("BigDealIds")
        self.RequestId = params.get("RequestId")


class Addr(AbstractModel):
    """Database address

    """

    def __init__(self):
        r"""
        :param IP: IP
        :type IP: str
        :param Port: Port
        :type Port: int
        """
        self.IP = None
        self.Port = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFileInfo(AbstractModel):
    """Backup file information

    """

    def __init__(self):
        r"""
        :param SnapshotId: Snapshot file ID, which is deprecated. You need to use `BackupId`.
        :type SnapshotId: int
        :param FileName: Backup file name
        :type FileName: str
        :param FileSize: Backup file size
        :type FileSize: int
        :param StartTime: Backup start time
        :type StartTime: str
        :param FinishTime: Backup end time
        :type FinishTime: str
        :param BackupType: Backup type. Valid values: `snapshot` (snapshot backup), `logic` (logic backup).
        :type BackupType: str
        :param BackupMethod: Back mode. auto: auto backup; manual: manual backup
        :type BackupMethod: str
        :param BackupStatus: Backup file status. success: backup succeeded; fail: backup failed; creating: creating backup file; deleting: deleting backup file
        :type BackupStatus: str
        :param SnapshotTime: Backup file time
        :type SnapshotTime: str
        :param BackupId: Backup ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupId: int
        :param SnapShotType: 
        :type SnapShotType: str
        :param BackupName: Backup file alias
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupName: str
        """
        self.SnapshotId = None
        self.FileName = None
        self.FileSize = None
        self.StartTime = None
        self.FinishTime = None
        self.BackupType = None
        self.BackupMethod = None
        self.BackupStatus = None
        self.SnapshotTime = None
        self.BackupId = None
        self.SnapShotType = None
        self.BackupName = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.StartTime = params.get("StartTime")
        self.FinishTime = params.get("FinishTime")
        self.BackupType = params.get("BackupType")
        self.BackupMethod = params.get("BackupMethod")
        self.BackupStatus = params.get("BackupStatus")
        self.SnapshotTime = params.get("SnapshotTime")
        self.BackupId = params.get("BackupId")
        self.SnapShotType = params.get("SnapShotType")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingResourceInfo(AbstractModel):
    """Billable resource information

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIds: Instance ID list
        :type InstanceIds: list of str
        :param DealName: Order ID
        :type DealName: str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.DealName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogItem(AbstractModel):
    """Binlog description

    """

    def __init__(self):
        r"""
        :param FileName: Binlog filename
        :type FileName: str
        :param FileSize: File size in bytes
        :type FileSize: int
        :param StartTime: Transaction start time
        :type StartTime: str
        :param FinishTime: Transaction end time
        :type FinishTime: str
        :param BinlogId: Binlog file ID
        :type BinlogId: int
        """
        self.FileName = None
        self.FileSize = None
        self.StartTime = None
        self.FinishTime = None
        self.BinlogId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.StartTime = params.get("StartTime")
        self.FinishTime = params.get("FinishTime")
        self.BinlogId = params.get("BinlogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInstanceDetail(AbstractModel):
    """Cluster instance information

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param InstanceType: Engine type
        :type InstanceType: str
        :param InstanceStatus: Instance status
        :type InstanceStatus: str
        :param InstanceStatusDesc: Instance status description
        :type InstanceStatusDesc: str
        :param InstanceCpu: Number of CPU cores
        :type InstanceCpu: int
        :param InstanceMemory: Memory
        :type InstanceMemory: int
        :param InstanceStorage: Disk
        :type InstanceStorage: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceType = None
        self.InstanceStatus = None
        self.InstanceStatusDesc = None
        self.InstanceCpu = None
        self.InstanceMemory = None
        self.InstanceStorage = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceType = params.get("InstanceType")
        self.InstanceStatus = params.get("InstanceStatus")
        self.InstanceStatusDesc = params.get("InstanceStatusDesc")
        self.InstanceCpu = params.get("InstanceCpu")
        self.InstanceMemory = params.get("InstanceMemory")
        self.InstanceStorage = params.get("InstanceStorage")
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
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Accounts: List of new accounts
        :type Accounts: list of NewAccount
        """
        self.ClusterId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = NewAccount()
                obj._deserialize(item)
                self.Accounts.append(obj)
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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param BackupType: Backup type. Valid values: `logic` (logic backup), `snapshot` (physical backup)
        :type BackupType: str
        :param BackupDatabases: Backup database, which is valid when `BackupType` is `logic`.
        :type BackupDatabases: list of str
        :param BackupTables: Backup table, which is valid when `BackupType` is `logic`.
        :type BackupTables: list of DatabaseTables
        :param BackupName: Backup name
        :type BackupName: str
        """
        self.ClusterId = None
        self.BackupType = None
        self.BackupDatabases = None
        self.BackupTables = None
        self.BackupName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BackupType = params.get("BackupType")
        self.BackupDatabases = params.get("BackupDatabases")
        if params.get("BackupTables") is not None:
            self.BackupTables = []
            for item in params.get("BackupTables"):
                obj = DatabaseTables()
                obj._deserialize(item)
                self.BackupTables.append(obj)
        self.BackupName = params.get("BackupName")
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


class CreateClustersRequest(AbstractModel):
    """CreateClusters request structure.

    """

    def __init__(self):
        r"""
        :param Zone: AZ
        :type Zone: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        :param DbVersion: Database version. Valid values: 
<li> Valid values for `MYSQL`: 5.7 and 8.0 </li>
        :type DbVersion: str
        :param ProjectId: Project ID.
        :type ProjectId: int
        :param Cpu: It is required when `DbMode` is set to `NORMAL` or left empty.
Number of CPU cores of normal instance
        :type Cpu: int
        :param Memory: It is required when `DbMode` is set to `NORMAL` or left empty.
Memory of a non-serverless instance in GB
        :type Memory: int
        :param Storage: This parameter has been deprecated.
Storage capacity in GB
        :type Storage: int
        :param ClusterName: Cluster name, which can contain less than 64 letters, digits, or symbols (-_.).
        :type ClusterName: str
        :param AdminPassword: Account password, which must contain 8-64 characters in at least three of the following four types: uppercase letters, lowercase letters, digits, and symbols (~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/).
        :type AdminPassword: str
        :param Port: Port. Valid range: [0, 65535). Default value: 3306
        :type Port: int
        :param PayMode: Billing mode. `0`: pay-as-you-go; `1`: monthly subscription. Default value: `0`
        :type PayMode: int
        :param Count: Number of purchased clusters. Valid range: [1,50]. Default value: 1
        :type Count: int
        :param RollbackStrategy: Rollback type:
noneRollback: no rollback;
snapRollback: rollback by snapshot;
timeRollback: rollback by time point
        :type RollbackStrategy: str
        :param RollbackId: `snapshotId` for snapshot rollback or `queryId` for time point rollback. 0 indicates to determine whether the time point is valid
        :type RollbackId: int
        :param OriginalClusterId: The source cluster ID passed in during rollback to find the source `poolId`
        :type OriginalClusterId: str
        :param ExpectTime: Specified time for time point rollback or snapshot time for snapshot rollback
        :type ExpectTime: str
        :param ExpectTimeThresh: This parameter has been deprecated.
Specified allowed time range for time point rollback
        :type ExpectTimeThresh: int
        :param StorageLimit: Storage upper limit of normal instance in GB
If `DbType` is `MYSQL` and the storage billing mode is monthly subscription, the parameter value can’t exceed the maximum storage corresponding to the CPU and memory specifications.
        :type StorageLimit: int
        :param InstanceCount: Number of Instances. Valid range: (0,16]
        :type InstanceCount: int
        :param TimeSpan: Purchase duration of monthly subscription plan
        :type TimeSpan: int
        :param TimeUnit: Duration unit of monthly subscription. Valid values: `s`, `d`, `m`, `y`
        :type TimeUnit: str
        :param AutoRenewFlag: Whether auto-renewal is enabled for monthly subscription plan. Default value: `0`
        :type AutoRenewFlag: int
        :param AutoVoucher: Whether to automatically select a voucher. `1`: yes; `0`: no. Default value: `0`
        :type AutoVoucher: int
        :param HaCount: Number of instances (this parameter has been disused and is retained only for compatibility with existing instances)
        :type HaCount: int
        :param OrderSource: Order source
        :type OrderSource: str
        :param ResourceTags: Array of tags to be bound to the created cluster
        :type ResourceTags: list of Tag
        :param DbMode: Database type
Valid values when `DbType` is `MYSQL` (default value: `NORMAL`):
<li>NORMAL</li>
<li>SERVERLESS</li>
        :type DbMode: str
        :param MinCpu: This parameter is required if `DbMode` is `SERVERLESS`.
Minimum number of CPU cores. For the value range, see the returned result of `DescribeServerlessInstanceSpecs`.
        :type MinCpu: float
        :param MaxCpu: This parameter is required if `DbMode` is `SERVERLESS`.
Maximum number of CPU cores. For the value range, see the returned result of `DescribeServerlessInstanceSpecs`.
        :type MaxCpu: float
        :param AutoPause: This parameter specifies whether the cluster will be automatically paused if `DbMode` is `SERVERLESS`. Valid values:
<li>yes</li>
<li>no</li>
Default value: yes
        :type AutoPause: str
        :param AutoPauseDelay: This parameter specifies the delay for automatic cluster pause in seconds if `DbMode` is `SERVERLESS`. Value range: [600,691200]
Default value: `600`
        :type AutoPauseDelay: int
        :param StoragePayMode: The billing mode of cluster storage. Valid values: `0` (pay-as-you-go), `1` (monthly subscription). Default value: `0`.
If `DbType` is `MYSQL` and the billing mode of cluster compute is pay-as-you-go (or the `DbMode` is `SERVERLESS`), the billing mode of cluster storage must be pay-as-you-go.
Clusters with storage billed in monthly subscription can’t be cloned or rolled back.
        :type StoragePayMode: int
        :param SecurityGroupIds: Array of security group IDs
        :type SecurityGroupIds: list of str
        :param AlarmPolicyIds: Array of alarm policy IDs
        :type AlarmPolicyIds: list of str
        :param ClusterParams: Array of parameters
        :type ClusterParams: list of ParamItem
        :param DealMode: Transaction mode. Valid values: `0` (place and pay for an order), `1` (place an order)
        :type DealMode: int
        :param ParamTemplateId: Parameter template ID, which can be obtained by querying parameter template information “DescribeParamTemplates”
        :type ParamTemplateId: int
        :param SlaveZone: Multi-AZ address
        :type SlaveZone: str
        """
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.DbType = None
        self.DbVersion = None
        self.ProjectId = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.ClusterName = None
        self.AdminPassword = None
        self.Port = None
        self.PayMode = None
        self.Count = None
        self.RollbackStrategy = None
        self.RollbackId = None
        self.OriginalClusterId = None
        self.ExpectTime = None
        self.ExpectTimeThresh = None
        self.StorageLimit = None
        self.InstanceCount = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.AutoRenewFlag = None
        self.AutoVoucher = None
        self.HaCount = None
        self.OrderSource = None
        self.ResourceTags = None
        self.DbMode = None
        self.MinCpu = None
        self.MaxCpu = None
        self.AutoPause = None
        self.AutoPauseDelay = None
        self.StoragePayMode = None
        self.SecurityGroupIds = None
        self.AlarmPolicyIds = None
        self.ClusterParams = None
        self.DealMode = None
        self.ParamTemplateId = None
        self.SlaveZone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.ProjectId = params.get("ProjectId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ClusterName = params.get("ClusterName")
        self.AdminPassword = params.get("AdminPassword")
        self.Port = params.get("Port")
        self.PayMode = params.get("PayMode")
        self.Count = params.get("Count")
        self.RollbackStrategy = params.get("RollbackStrategy")
        self.RollbackId = params.get("RollbackId")
        self.OriginalClusterId = params.get("OriginalClusterId")
        self.ExpectTime = params.get("ExpectTime")
        self.ExpectTimeThresh = params.get("ExpectTimeThresh")
        self.StorageLimit = params.get("StorageLimit")
        self.InstanceCount = params.get("InstanceCount")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.AutoVoucher = params.get("AutoVoucher")
        self.HaCount = params.get("HaCount")
        self.OrderSource = params.get("OrderSource")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DbMode = params.get("DbMode")
        self.MinCpu = params.get("MinCpu")
        self.MaxCpu = params.get("MaxCpu")
        self.AutoPause = params.get("AutoPause")
        self.AutoPauseDelay = params.get("AutoPauseDelay")
        self.StoragePayMode = params.get("StoragePayMode")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.AlarmPolicyIds = params.get("AlarmPolicyIds")
        if params.get("ClusterParams") is not None:
            self.ClusterParams = []
            for item in params.get("ClusterParams"):
                obj = ParamItem()
                obj._deserialize(item)
                self.ClusterParams.append(obj)
        self.DealMode = params.get("DealMode")
        self.ParamTemplateId = params.get("ParamTemplateId")
        self.SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClustersResponse(AbstractModel):
    """CreateClusters response structure.

    """

    def __init__(self):
        r"""
        :param TranId: Freezing transaction ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param DealNames: Order ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param ResourceIds: List of resource IDs (This field has been deprecated. You need to use `dealNames` in the `DescribeResourcesByDealName` API to get resource IDs.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceIds: list of str
        :param ClusterIds: List of cluster IDs (This field has been deprecated. You need to use `dealNames` in the `DescribeResourcesByDealName` API to get cluster IDs.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterIds: list of str
        :param BigDealIds: Big order ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BigDealIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TranId = None
        self.DealNames = None
        self.ResourceIds = None
        self.ClusterIds = None
        self.BigDealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.DealNames = params.get("DealNames")
        self.ResourceIds = params.get("ResourceIds")
        self.ClusterIds = params.get("ClusterIds")
        self.BigDealIds = params.get("BigDealIds")
        self.RequestId = params.get("RequestId")


class CynosdbCluster(AbstractModel):
    """Cluster information

    """

    def __init__(self):
        r"""
        :param Status: Cluster status. Valid values are as follows:
creating
running
isolating
isolated
activating (removing isolation)
offlining (deactivating)
offlined (deactivated)
deleting
deleted
        :type Status: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Zone: AZ
        :type Zone: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param Region: Region
        :type Region: str
        :param DbVersion: Database version
        :type DbVersion: str
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceNum: Number of instances
        :type InstanceNum: int
        :param Uin: User `uin`
        :type Uin: str
        :param DbType: Engine type
        :type DbType: str
        :param AppId: User `appid`
        :type AppId: int
        :param StatusDesc: Cluster status description
        :type StatusDesc: str
        :param CreateTime: Cluster creation time
        :type CreateTime: str
        :param PayMode: Billing mode. 0: pay-as-you-go; 1: monthly subscription
        :type PayMode: int
        :param PeriodEndTime: End time
        :type PeriodEndTime: str
        :param Vip: Cluster read-write VIP
        :type Vip: str
        :param Vport: Cluster read-write vport
        :type Vport: int
        :param ProjectID: Project ID
        :type ProjectID: int
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param CynosVersion: TDSQL-C kernel version
        :type CynosVersion: str
        :param StorageLimit: Storage capacity
        :type StorageLimit: int
        :param RenewFlag: Renewal flag
        :type RenewFlag: int
        :param ProcessingTask: Task in progress
        :type ProcessingTask: str
        :param Tasks: Array of tasks in cluster
        :type Tasks: list of ObjectTask
        :param ResourceTags: Array of tags bound to cluster
        :type ResourceTags: list of Tag
        :param DbMode: Database type (`NORMAL` or `SERVERLESS`)
        :type DbMode: str
        :param ServerlessStatus: Serverless cluster status when the database type is `SERVERLESS`. Valid values:
resume
pause
        :type ServerlessStatus: str
        :param Storage: Prepaid cluster storage
        :type Storage: int
        :param StorageId: Cluster storage ID used in prepaid storage modification
        :type StorageId: str
        :param StoragePayMode: Billing mode of cluster storage. Valid values: `0` (postpaid), `1` (prepaid)
        :type StoragePayMode: int
        :param MinStorageSize: The minimum storage corresponding to the compute specifications of the cluster
        :type MinStorageSize: int
        :param MaxStorageSize: The maximum storage corresponding to the compute specifications of the cluster
        :type MaxStorageSize: int
        :param NetAddrs: Network information of the cluster
        :type NetAddrs: list of NetAddr
        """
        self.Status = None
        self.UpdateTime = None
        self.Zone = None
        self.ClusterName = None
        self.Region = None
        self.DbVersion = None
        self.ClusterId = None
        self.InstanceNum = None
        self.Uin = None
        self.DbType = None
        self.AppId = None
        self.StatusDesc = None
        self.CreateTime = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.Vip = None
        self.Vport = None
        self.ProjectID = None
        self.VpcId = None
        self.SubnetId = None
        self.CynosVersion = None
        self.StorageLimit = None
        self.RenewFlag = None
        self.ProcessingTask = None
        self.Tasks = None
        self.ResourceTags = None
        self.DbMode = None
        self.ServerlessStatus = None
        self.Storage = None
        self.StorageId = None
        self.StoragePayMode = None
        self.MinStorageSize = None
        self.MaxStorageSize = None
        self.NetAddrs = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.UpdateTime = params.get("UpdateTime")
        self.Zone = params.get("Zone")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.DbVersion = params.get("DbVersion")
        self.ClusterId = params.get("ClusterId")
        self.InstanceNum = params.get("InstanceNum")
        self.Uin = params.get("Uin")
        self.DbType = params.get("DbType")
        self.AppId = params.get("AppId")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.ProjectID = params.get("ProjectID")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CynosVersion = params.get("CynosVersion")
        self.StorageLimit = params.get("StorageLimit")
        self.RenewFlag = params.get("RenewFlag")
        self.ProcessingTask = params.get("ProcessingTask")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DbMode = params.get("DbMode")
        self.ServerlessStatus = params.get("ServerlessStatus")
        self.Storage = params.get("Storage")
        self.StorageId = params.get("StorageId")
        self.StoragePayMode = params.get("StoragePayMode")
        self.MinStorageSize = params.get("MinStorageSize")
        self.MaxStorageSize = params.get("MaxStorageSize")
        if params.get("NetAddrs") is not None:
            self.NetAddrs = []
            for item in params.get("NetAddrs"):
                obj = NetAddr()
                obj._deserialize(item)
                self.NetAddrs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbClusterDetail(AbstractModel):
    """Cluster details

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param Region: Region
        :type Region: str
        :param Status: Status
        :type Status: str
        :param StatusDesc: Status description
        :type StatusDesc: str
        :param VpcName: VPC name
        :type VpcName: str
        :param VpcId: Unique VPC ID
        :type VpcId: str
        :param SubnetName: Subnet name
        :type SubnetName: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param Charset: Character set
        :type Charset: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param DbType: Database type
        :type DbType: str
        :param DbVersion: Database version
        :type DbVersion: str
        :param UsedStorage: Used capacity
        :type UsedStorage: int
        :param RoAddr: vport for read/write separation
        :type RoAddr: list of Addr
        :param InstanceSet: Instance information
        :type InstanceSet: list of ClusterInstanceDetail
        :param PayMode: Billing mode
        :type PayMode: int
        :param PeriodEndTime: Expiration time
        :type PeriodEndTime: str
        :param Vip: VIP
        :type Vip: str
        :param Vport: vport
        :type Vport: int
        :param ProjectID: Project ID
        :type ProjectID: int
        :param Zone: AZ
        :type Zone: str
        :param ResourceTags: Array of tags bound to instance
        :type ResourceTags: list of Tag
        :param ServerlessStatus: Serverless cluster status when the database type is `SERVERLESS`. Valid values:
resume
resuming
pause
pausing
        :type ServerlessStatus: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Region = None
        self.Status = None
        self.StatusDesc = None
        self.VpcName = None
        self.VpcId = None
        self.SubnetName = None
        self.SubnetId = None
        self.Charset = None
        self.CreateTime = None
        self.DbType = None
        self.DbVersion = None
        self.UsedStorage = None
        self.RoAddr = None
        self.InstanceSet = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.Vip = None
        self.Vport = None
        self.ProjectID = None
        self.Zone = None
        self.ResourceTags = None
        self.ServerlessStatus = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.SubnetId = params.get("SubnetId")
        self.Charset = params.get("Charset")
        self.CreateTime = params.get("CreateTime")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.UsedStorage = params.get("UsedStorage")
        if params.get("RoAddr") is not None:
            self.RoAddr = []
            for item in params.get("RoAddr"):
                obj = Addr()
                obj._deserialize(item)
                self.RoAddr.append(obj)
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ClusterInstanceDetail()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.ProjectID = params.get("ProjectID")
        self.Zone = params.get("Zone")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.ServerlessStatus = params.get("ServerlessStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstance(AbstractModel):
    """Instance information

    """

    def __init__(self):
        r"""
        :param Uin: User `Uin`
        :type Uin: str
        :param AppId: User `AppId`
        :type AppId: int
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Region: Region
        :type Region: str
        :param Zone: AZ
        :type Zone: str
        :param Status: Instance status
        :type Status: str
        :param StatusDesc: Instance status description
        :type StatusDesc: str
        :param DbType: Database type
        :type DbType: str
        :param DbVersion: Database version
        :type DbVersion: str
        :param Cpu: Number of CPU cores
        :type Cpu: int
        :param Memory: Memory in GB
        :type Memory: int
        :param Storage: Storage capacity in GB
        :type Storage: int
        :param InstanceType: Instance type
        :type InstanceType: str
        :param InstanceRole: Current instance role
        :type InstanceRole: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param Vip: Private IP of instance
        :type Vip: str
        :param Vport: Private port of instance
        :type Vport: int
        :param PayMode: Billing mode
        :type PayMode: int
        :param PeriodEndTime: Instance expiration time
        :type PeriodEndTime: str
        :param DestroyDeadlineText: Termination deadline
        :type DestroyDeadlineText: str
        :param IsolateTime: Isolation time
        :type IsolateTime: str
        :param NetType: Network type
        :type NetType: int
        :param WanDomain: Public domain name
        :type WanDomain: str
        :param WanIP: Public IP
        :type WanIP: str
        :param WanPort: Public port
        :type WanPort: int
        :param WanStatus: Public network status
        :type WanStatus: str
        :param DestroyTime: Instance termination time
        :type DestroyTime: str
        :param CynosVersion: TDSQL-C kernel version
        :type CynosVersion: str
        :param ProcessingTask: Task in progress
        :type ProcessingTask: str
        :param RenewFlag: Renewal flag
        :type RenewFlag: int
        :param MinCpu: Minimum number of CPU cores for serverless instance
        :type MinCpu: float
        :param MaxCpu: Maximum number of CPU cores for serverless instance
        :type MaxCpu: float
        :param ServerlessStatus: Serverless instance status. Valid values:
resume
pause
        :type ServerlessStatus: str
        :param StorageId: Prepaid storage ID
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type StorageId: str
        :param StoragePayMode: Storage billing mode
        :type StoragePayMode: int
        """
        self.Uin = None
        self.AppId = None
        self.ClusterId = None
        self.ClusterName = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.Status = None
        self.StatusDesc = None
        self.DbType = None
        self.DbVersion = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.InstanceType = None
        self.InstanceRole = None
        self.UpdateTime = None
        self.CreateTime = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None
        self.Vport = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.DestroyDeadlineText = None
        self.IsolateTime = None
        self.NetType = None
        self.WanDomain = None
        self.WanIP = None
        self.WanPort = None
        self.WanStatus = None
        self.DestroyTime = None
        self.CynosVersion = None
        self.ProcessingTask = None
        self.RenewFlag = None
        self.MinCpu = None
        self.MaxCpu = None
        self.ServerlessStatus = None
        self.StorageId = None
        self.StoragePayMode = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceType = params.get("InstanceType")
        self.InstanceRole = params.get("InstanceRole")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.DestroyDeadlineText = params.get("DestroyDeadlineText")
        self.IsolateTime = params.get("IsolateTime")
        self.NetType = params.get("NetType")
        self.WanDomain = params.get("WanDomain")
        self.WanIP = params.get("WanIP")
        self.WanPort = params.get("WanPort")
        self.WanStatus = params.get("WanStatus")
        self.DestroyTime = params.get("DestroyTime")
        self.CynosVersion = params.get("CynosVersion")
        self.ProcessingTask = params.get("ProcessingTask")
        self.RenewFlag = params.get("RenewFlag")
        self.MinCpu = params.get("MinCpu")
        self.MaxCpu = params.get("MaxCpu")
        self.ServerlessStatus = params.get("ServerlessStatus")
        self.StorageId = params.get("StorageId")
        self.StoragePayMode = params.get("StoragePayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceDetail(AbstractModel):
    """Instance details

    """

    def __init__(self):
        r"""
        :param Uin: User `Uin`
        :type Uin: str
        :param AppId: User `AppId`
        :type AppId: int
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Region: Region
        :type Region: str
        :param Zone: AZ
        :type Zone: str
        :param Status: Instance status
        :type Status: str
        :param StatusDesc: Instance status description
        :type StatusDesc: str
        :param DbType: Database type
        :type DbType: str
        :param DbVersion: Database version
        :type DbVersion: str
        :param Cpu: Number of CPU cores
        :type Cpu: int
        :param Memory: Memory in GB
        :type Memory: int
        :param Storage: Storage capacity in GB
        :type Storage: int
        :param InstanceType: Instance type
        :type InstanceType: str
        :param InstanceRole: Current instance role
        :type InstanceRole: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param PayMode: Billing mode
        :type PayMode: int
        :param PeriodEndTime: Instance expiration time
        :type PeriodEndTime: str
        :param NetType: Network type
        :type NetType: int
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param Vip: Private IP of instance
        :type Vip: str
        :param Vport: Private port of instance
        :type Vport: int
        :param WanDomain: Public domain name of instance
        :type WanDomain: str
        :param Charset: Character set
        :type Charset: str
        :param CynosVersion: TDSQL-C kernel version
        :type CynosVersion: str
        :param RenewFlag: Renewal flag
        :type RenewFlag: int
        :param MinCpu: The minimum number of CPU cores for a serverless instance
        :type MinCpu: float
        :param MaxCpu: The maximum number of CPU cores for a serverless instance
        :type MaxCpu: float
        :param ServerlessStatus: Serverless instance status. Valid values:
resume
pause
        :type ServerlessStatus: str
        """
        self.Uin = None
        self.AppId = None
        self.ClusterId = None
        self.ClusterName = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.Status = None
        self.StatusDesc = None
        self.DbType = None
        self.DbVersion = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.InstanceType = None
        self.InstanceRole = None
        self.UpdateTime = None
        self.CreateTime = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.NetType = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.Charset = None
        self.CynosVersion = None
        self.RenewFlag = None
        self.MinCpu = None
        self.MaxCpu = None
        self.ServerlessStatus = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceType = params.get("InstanceType")
        self.InstanceRole = params.get("InstanceRole")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.NetType = params.get("NetType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.Charset = params.get("Charset")
        self.CynosVersion = params.get("CynosVersion")
        self.RenewFlag = params.get("RenewFlag")
        self.MinCpu = params.get("MinCpu")
        self.MaxCpu = params.get("MaxCpu")
        self.ServerlessStatus = params.get("ServerlessStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceGrp(AbstractModel):
    """Instance group information

    """

    def __init__(self):
        r"""
        :param AppId: appId
        :type AppId: int
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param CreatedTime: Creation time
        :type CreatedTime: str
        :param DeletedTime: Deletion time
        :type DeletedTime: str
        :param InstanceGrpId: Instance group ID
        :type InstanceGrpId: str
        :param Status: Status
        :type Status: str
        :param Type: Instance group type. ha: HA group; ro: RO group
        :type Type: str
        :param UpdatedTime: Update time
        :type UpdatedTime: str
        :param Vip: Private IP
        :type Vip: str
        :param Vport: Private port
        :type Vport: int
        :param WanDomain: Public domain name
        :type WanDomain: str
        :param WanIP: Public IP
        :type WanIP: str
        :param WanPort: Public port
        :type WanPort: int
        :param WanStatus: Public network status
        :type WanStatus: str
        :param InstanceSet: Information of instances contained in instance group
        :type InstanceSet: list of CynosdbInstance
        """
        self.AppId = None
        self.ClusterId = None
        self.CreatedTime = None
        self.DeletedTime = None
        self.InstanceGrpId = None
        self.Status = None
        self.Type = None
        self.UpdatedTime = None
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.WanIP = None
        self.WanPort = None
        self.WanStatus = None
        self.InstanceSet = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.CreatedTime = params.get("CreatedTime")
        self.DeletedTime = params.get("DeletedTime")
        self.InstanceGrpId = params.get("InstanceGrpId")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.UpdatedTime = params.get("UpdatedTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.WanIP = params.get("WanIP")
        self.WanPort = params.get("WanPort")
        self.WanStatus = params.get("WanStatus")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTables(AbstractModel):
    """Database table information

    """

    def __init__(self):
        r"""
        :param Database: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param Tables: Table name list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of str
        """
        self.Database = None
        self.Tables = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Tables = params.get("Tables")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param AccountNames: List of accounts to be filtered
        :type AccountNames: list of str
        :param DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        """
        self.ClusterId = None
        self.AccountNames = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AccountNames = params.get("AccountNames")
        self.DbType = params.get("DbType")
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
        :param AccountSet: Database account list
        :type AccountSet: list of Account
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountSet") is not None:
            self.AccountSet = []
            for item in params.get("AccountSet"):
                obj = Account()
                obj._deserialize(item)
                self.AccountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
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
        :param BackupTimeBeg: Full backup start time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively
        :type BackupTimeBeg: int
        :param BackupTimeEnd: Full backup end time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively
        :type BackupTimeEnd: int
        :param ReserveDuration: Backup retention period in seconds. Backups will be cleared after this period elapses. 7 days is represented by 3600*24*7 = 604800
        :type ReserveDuration: int
        :param BackupFreq: Backup frequency. It is an array of 7 elements corresponding to Monday through Sunday. full: full backup; increment: incremental backup
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupFreq: list of str
        :param BackupType: Backup mode. logic: logic backup; snapshot: snapshot backup
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupType: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BackupTimeBeg = None
        self.BackupTimeEnd = None
        self.ReserveDuration = None
        self.BackupFreq = None
        self.BackupType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupTimeBeg = params.get("BackupTimeBeg")
        self.BackupTimeEnd = params.get("BackupTimeEnd")
        self.ReserveDuration = params.get("ReserveDuration")
        self.BackupFreq = params.get("BackupFreq")
        self.BackupType = params.get("BackupType")
        self.RequestId = params.get("RequestId")


class DescribeBackupDownloadUrlRequest(AbstractModel):
    """DescribeBackupDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param BackupId: Backup ID
        :type BackupId: int
        """
        self.ClusterId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadUrlResponse(AbstractModel):
    """DescribeBackupDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param DownloadUrl: Backup download address
        :type DownloadUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeBackupListRequest(AbstractModel):
    """DescribeBackupList request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Limit: The number of results to be returned. Value range: (0,100]
        :type Limit: int
        :param Offset: Record offset. Value range: [0,INF)
        :type Offset: int
        :param DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        :param BackupIds: Backup ID
        :type BackupIds: list of int
        :param BackupType: Backup type. Valid values: `snapshot` (snapshot backup), `logic` (logic backup).
        :type BackupType: str
        :param BackupMethod: Back mode. Valid values: `auto` (automatic backup), `manual` (manual backup)
        :type BackupMethod: str
        :param SnapShotType: 
        :type SnapShotType: str
        :param StartTime: Backup start time
        :type StartTime: str
        :param EndTime: Backup end time
        :type EndTime: str
        :param FileNames: 
        :type FileNames: list of str
        :param BackupNames: Backup alias, which supports fuzzy query.
        :type BackupNames: list of str
        """
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.DbType = None
        self.BackupIds = None
        self.BackupType = None
        self.BackupMethod = None
        self.SnapShotType = None
        self.StartTime = None
        self.EndTime = None
        self.FileNames = None
        self.BackupNames = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.DbType = params.get("DbType")
        self.BackupIds = params.get("BackupIds")
        self.BackupType = params.get("BackupType")
        self.BackupMethod = params.get("BackupMethod")
        self.SnapShotType = params.get("SnapShotType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.FileNames = params.get("FileNames")
        self.BackupNames = params.get("BackupNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupListResponse(AbstractModel):
    """DescribeBackupList response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of backup files
        :type TotalCount: int
        :param BackupList: Backup file list
        :type BackupList: list of BackupFileInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = BackupFileInfo()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBinlogDownloadUrlRequest(AbstractModel):
    """DescribeBinlogDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param BinlogId: Binlog file ID
        :type BinlogId: int
        """
        self.ClusterId = None
        self.BinlogId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BinlogId = params.get("BinlogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogDownloadUrlResponse(AbstractModel):
    """DescribeBinlogDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param DownloadUrl: Download address
        :type DownloadUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeBinlogSaveDaysRequest(AbstractModel):
    """DescribeBinlogSaveDays request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogSaveDaysResponse(AbstractModel):
    """DescribeBinlogSaveDays response structure.

    """

    def __init__(self):
        r"""
        :param BinlogSaveDays: Binlog retention period in days
        :type BinlogSaveDays: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BinlogSaveDays = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BinlogSaveDays = params.get("BinlogSaveDays")
        self.RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Maximum number
        :type Limit: int
        """
        self.ClusterId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
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
        


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of records
        :type TotalCount: int
        :param Binlogs: Binlog list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Binlogs: list of BinlogItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Binlogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Binlogs") is not None:
            self.Binlogs = []
            for item in params.get("Binlogs"):
                obj = BinlogItem()
                obj._deserialize(item)
                self.Binlogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail response structure.

    """

    def __init__(self):
        r"""
        :param Detail: Cluster details
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbClusterDetail`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self.Detail = CynosdbClusterDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeClusterInstanceGrpsRequest(AbstractModel):
    """DescribeClusterInstanceGrps request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstanceGrpsResponse(AbstractModel):
    """DescribeClusterInstanceGrps response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of instance groups
        :type TotalCount: int
        :param InstanceGrpInfoList: Instance group list
        :type InstanceGrpInfoList: list of CynosdbInstanceGrp
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceGrpInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceGrpInfoList") is not None:
            self.InstanceGrpInfoList = []
            for item in params.get("InstanceGrpInfoList"):
                obj = CynosdbInstanceGrp()
                obj._deserialize(item)
                self.InstanceGrpInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterParamsRequest(AbstractModel):
    """DescribeClusterParams request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterParamsResponse(AbstractModel):
    """DescribeClusterParams response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of parameters
        :type TotalCount: int
        :param Items: Instance parameter list
        :type Items: list of ParamInfo
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
                obj = ParamInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        r"""
        :param DbType: Engine type. Currently, `MYSQL` is supported.
        :type DbType: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param Offset: Record offset. Default value: 0
        :type Offset: int
        :param OrderBy: Sort by field. Valid values:
<li> CREATETIME: creation time</li>
<li> PERIODENDTIME: expiration time</li>
        :type OrderBy: str
        :param OrderByType: Sorting order. Valid values:
<li> ASC: ascending</li>
<li> DESC: descending</li>
        :type OrderByType: str
        :param Filters: Filter. If more than one filter exists, the logical relationship between these filters is `AND`.
        :type Filters: list of QueryFilter
        """
        self.DbType = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.Filters = None


    def _deserialize(self, params):
        self.DbType = params.get("DbType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of clusters
        :type TotalCount: int
        :param ClusterSet: Cluster list
        :type ClusterSet: list of CynosdbCluster
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterSet") is not None:
            self.ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = CynosdbCluster()
                obj._deserialize(item)
                self.ClusterSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance group ID
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
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param Groups: Security group information
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


class DescribeInstanceDetailRequest(AbstractModel):
    """DescribeInstanceDetail request structure.

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
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param Detail: Instance details
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbInstanceDetail`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self.Detail = CynosdbInstanceDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceSlowQueriesRequest(AbstractModel):
    """DescribeInstanceSlowQueries request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param StartTime: Transaction start time
        :type StartTime: str
        :param EndTime: Transaction end time
        :type EndTime: str
        :param Limit: Maximum number
        :type Limit: int
        :param Offset: Offset
        :type Offset: int
        :param Username: Username
        :type Username: str
        :param Host: Client host
        :type Host: str
        :param Database: Database name
        :type Database: str
        :param OrderBy: Sorting field. Valid values: QueryTime, LockTime, RowsExamined, RowsSent.
        :type OrderBy: str
        :param OrderByType: Sorting order. Valid values: asc, desc.
        :type OrderByType: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.Username = None
        self.Host = None
        self.Database = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Username = params.get("Username")
        self.Host = params.get("Host")
        self.Database = params.get("Database")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSlowQueriesResponse(AbstractModel):
    """DescribeInstanceSlowQueries response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param SlowQueries: Slow query record
        :type SlowQueries: list of SlowQueriesItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.SlowQueries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SlowQueries") is not None:
            self.SlowQueries = []
            for item in params.get("SlowQueries"):
                obj = SlowQueriesItem()
                obj._deserialize(item)
                self.SlowQueries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceSpecsRequest(AbstractModel):
    """DescribeInstanceSpecs request structure.

    """

    def __init__(self):
        r"""
        :param DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        :param IncludeZoneStocks: Whether to return the AZ information.
        :type IncludeZoneStocks: bool
        """
        self.DbType = None
        self.IncludeZoneStocks = None


    def _deserialize(self, params):
        self.DbType = params.get("DbType")
        self.IncludeZoneStocks = params.get("IncludeZoneStocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSpecsResponse(AbstractModel):
    """DescribeInstanceSpecs response structure.

    """

    def __init__(self):
        r"""
        :param InstanceSpecSet: Specification information
        :type InstanceSpecSet: list of InstanceSpec
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceSpecSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSpecSet") is not None:
            self.InstanceSpecSet = []
            for item in params.get("InstanceSpecSet"):
                obj = InstanceSpec()
                obj._deserialize(item)
                self.InstanceSpecSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param Offset: Record offset. Default value: 0
        :type Offset: int
        :param OrderBy: Sort by field. Valid values:
<li> CREATETIME: creation time</li>
<li> PERIODENDTIME: expiration time</li>
        :type OrderBy: str
        :param OrderByType: Sorting order. Valid values:
<li> ASC: ascending</li>
<li> DESC: descending</li>
        :type OrderByType: str
        :param Filters: Filter. If more than one filter exists, the logical relationship between these filters is `AND`.
        :type Filters: list of QueryFilter
        :param DbType: Engine type. Currently, `MYSQL` is supported.
        :type DbType: str
        :param Status: Instance status. Valid values:
creating
running
isolating
isolated
activating: Removing the instance from isolation
offlining: Eliminating the instance
offlined: Instance eliminated
        :type Status: str
        :param InstanceIds: Instance ID list
        :type InstanceIds: list of str
        """
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.Filters = None
        self.DbType = None
        self.Status = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DbType = params.get("DbType")
        self.Status = params.get("Status")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of instances
        :type TotalCount: int
        :param InstanceSet: Instance list
        :type InstanceSet: list of CynosdbInstance
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
                obj = CynosdbInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMaintainPeriodRequest(AbstractModel):
    """DescribeMaintainPeriod request structure.

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
        


class DescribeMaintainPeriodResponse(AbstractModel):
    """DescribeMaintainPeriod response structure.

    """

    def __init__(self):
        r"""
        :param MaintainWeekDays: Maintenance days of the week
        :type MaintainWeekDays: list of str
        :param MaintainStartTime: Maintenance start time in seconds
        :type MaintainStartTime: int
        :param MaintainDuration: Maintenance duration in seconds
        :type MaintainDuration: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MaintainWeekDays = None
        self.MaintainStartTime = None
        self.MaintainDuration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaintainWeekDays = params.get("MaintainWeekDays")
        self.MaintainStartTime = params.get("MaintainStartTime")
        self.MaintainDuration = params.get("MaintainDuration")
        self.RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates request structure.

    """


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of parameter templates
        :type TotalCount: int
        :param Items: Parameter template information
        :type Items: list of ParamTemplateListInfo
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
                obj = ParamTemplateListInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param ProjectId: Project ID
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
        :param Groups: Security group details
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


class DescribeResourcesByDealNameRequest(AbstractModel):
    """DescribeResourcesByDealName request structure.

    """

    def __init__(self):
        r"""
        :param DealName: Order ID. (If the cluster is not delivered yet, the `DescribeResourcesByDealName` API may return the `InvalidParameterValue.DealNameNotFound` error. Call the API again until it succeeds.)
        :type DealName: str
        :param DealNames: Order ID, which can be used to query the resource information of multiple orders ID (If the cluster is not delivered yet, the `DescribeResourcesByDealName` API may return the `InvalidParameterValue.DealNameNotFound` error. Call the API again until it succeeds.)
        :type DealNames: list of str
        """
        self.DealName = None
        self.DealNames = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByDealNameResponse(AbstractModel):
    """DescribeResourcesByDealName response structure.

    """

    def __init__(self):
        r"""
        :param BillingResourceInfos: Billable resource ID information array
        :type BillingResourceInfos: list of BillingResourceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BillingResourceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BillingResourceInfos") is not None:
            self.BillingResourceInfos = []
            for item in params.get("BillingResourceInfos"):
                obj = BillingResourceInfo()
                obj._deserialize(item)
                self.BillingResourceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackTimeRangeRequest(AbstractModel):
    """DescribeRollbackTimeRange request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeRangeResponse(AbstractModel):
    """DescribeRollbackTimeRange response structure.

    """

    def __init__(self):
        r"""
        :param TimeRangeStart: Start time of valid rollback time range (disused)
        :type TimeRangeStart: str
        :param TimeRangeEnd: End time of valid rollback time range (disused)
        :type TimeRangeEnd: str
        :param RollbackTimeRanges: Time range available for rollback
        :type RollbackTimeRanges: list of RollbackTimeRange
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TimeRangeStart = None
        self.TimeRangeEnd = None
        self.RollbackTimeRanges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        if params.get("RollbackTimeRanges") is not None:
            self.RollbackTimeRanges = []
            for item in params.get("RollbackTimeRanges"):
                obj = RollbackTimeRange()
                obj._deserialize(item)
                self.RollbackTimeRanges.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackTimeValidityRequest(AbstractModel):
    """DescribeRollbackTimeValidity request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ExpectTime: Expected time point to roll back to
        :type ExpectTime: str
        :param ExpectTimeThresh: Error tolerance range for rollback time point
        :type ExpectTimeThresh: int
        """
        self.ClusterId = None
        self.ExpectTime = None
        self.ExpectTimeThresh = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ExpectTime = params.get("ExpectTime")
        self.ExpectTimeThresh = params.get("ExpectTimeThresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeValidityResponse(AbstractModel):
    """DescribeRollbackTimeValidity response structure.

    """

    def __init__(self):
        r"""
        :param PoolId: Storage `poolID`
        :type PoolId: int
        :param QueryId: Rollback task ID, which needs to be passed in when rolling back to this time point
        :type QueryId: int
        :param Status: Whether the time point is valid. pass: check passed; fail: check failed
        :type Status: str
        :param SuggestTime: Suggested time point. This value takes effect only if `Status` is `fail`
        :type SuggestTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PoolId = None
        self.QueryId = None
        self.Status = None
        self.SuggestTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PoolId = params.get("PoolId")
        self.QueryId = params.get("QueryId")
        self.Status = params.get("Status")
        self.SuggestTime = params.get("SuggestTime")
        self.RequestId = params.get("RequestId")


class ExportInstanceSlowQueriesRequest(AbstractModel):
    """ExportInstanceSlowQueries request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param StartTime: Transaction start time
        :type StartTime: str
        :param EndTime: Transaction end time
        :type EndTime: str
        :param Limit: Maximum number
        :type Limit: int
        :param Offset: Offset
        :type Offset: int
        :param Username: Username
        :type Username: str
        :param Host: Client host
        :type Host: str
        :param Database: Database name
        :type Database: str
        :param FileType: File type. Valid values: csv, original.
        :type FileType: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.Username = None
        self.Host = None
        self.Database = None
        self.FileType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Username = params.get("Username")
        self.Host = params.get("Host")
        self.Database = params.get("Database")
        self.FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInstanceSlowQueriesResponse(AbstractModel):
    """ExportInstanceSlowQueries response structure.

    """

    def __init__(self):
        r"""
        :param FileContent: Slow query export content
        :type FileContent: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FileContent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.RequestId = params.get("RequestId")


class InquirePriceCreateRequest(AbstractModel):
    """InquirePriceCreate request structure.

    """

    def __init__(self):
        r"""
        :param Zone: AZ
        :type Zone: str
        :param GoodsNum: Number of compute node to purchase
        :type GoodsNum: int
        :param InstancePayMode: Instance type for purchase. Valid values: `PREPAID`, `POSTPAID`, `SERVERLESS`.
        :type InstancePayMode: str
        :param StoragePayMode: Storage type for purchase. Valid values: `PREPAID`, `POSTPAID`.
        :type StoragePayMode: str
        :param Cpu: Number of CPU cores, which is required when `InstancePayMode` is `PREPAID` or `POSTPAID`.
        :type Cpu: int
        :param Memory: Memory size in GB, which is required when `InstancePayMode` is `PREPAID` or `POSTPAID`.
        :type Memory: int
        :param Ccu: CCU size, which is required when `InstancePayMode` is `SERVERLESS`.
        :type Ccu: float
        :param StorageLimit: Storage size, which is required when `StoragePayMode` is `PREPAID`.
        :type StorageLimit: int
        :param TimeSpan: Validity period, which is required when `InstancePayMode` is `PREPAID`.
        :type TimeSpan: int
        :param TimeUnit: Duration unit, which is required when `InstancePayMode` is `PREPAID`. Valid values: `m` (month), `d` (day).
        :type TimeUnit: str
        """
        self.Zone = None
        self.GoodsNum = None
        self.InstancePayMode = None
        self.StoragePayMode = None
        self.Cpu = None
        self.Memory = None
        self.Ccu = None
        self.StorageLimit = None
        self.TimeSpan = None
        self.TimeUnit = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.GoodsNum = params.get("GoodsNum")
        self.InstancePayMode = params.get("InstancePayMode")
        self.StoragePayMode = params.get("StoragePayMode")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Ccu = params.get("Ccu")
        self.StorageLimit = params.get("StorageLimit")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateResponse(AbstractModel):
    """InquirePriceCreate response structure.

    """

    def __init__(self):
        r"""
        :param InstancePrice: Instance price
        :type InstancePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param StoragePrice: Storage price
        :type StoragePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstancePrice = None
        self.StoragePrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = TradePrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("StoragePrice") is not None:
            self.StoragePrice = TradePrice()
            self.StoragePrice._deserialize(params.get("StoragePrice"))
        self.RequestId = params.get("RequestId")


class InquirePriceRenewRequest(AbstractModel):
    """InquirePriceRenew request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param TimeSpan: Validity period, which needs to be used together with `TimeUnit`.
        :type TimeSpan: int
        :param TimeUnit: Unit of validity period, which needs to be used together with `TimeSpan`. Valid values: `d` (day), `m` (month).
        :type TimeUnit: str
        """
        self.ClusterId = None
        self.TimeSpan = None
        self.TimeUnit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewResponse(AbstractModel):
    """InquirePriceRenew response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIds: Instance ID list
        :type InstanceIds: list of str
        :param Prices: Price of instance specification in array
        :type Prices: list of TradePrice
        :param InstanceRealTotalPrice: Total renewal price of compute node
        :type InstanceRealTotalPrice: int
        :param StorageRealTotalPrice: Total renewal price of storage node
        :type StorageRealTotalPrice: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.Prices = None
        self.InstanceRealTotalPrice = None
        self.StorageRealTotalPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Prices") is not None:
            self.Prices = []
            for item in params.get("Prices"):
                obj = TradePrice()
                obj._deserialize(item)
                self.Prices.append(obj)
        self.InstanceRealTotalPrice = params.get("InstanceRealTotalPrice")
        self.StorageRealTotalPrice = params.get("StorageRealTotalPrice")
        self.RequestId = params.get("RequestId")


class InstanceSpec(AbstractModel):
    """Details of purchasable instance specifications. `Cpu` and `Memory` determine the instance specification during instance creation. The value range of the storage capacity is [MinStorageSize,MaxStorageSize]

    """

    def __init__(self):
        r"""
        :param Cpu: Number of instance CPU cores
        :type Cpu: int
        :param Memory: Instance memory in GB
        :type Memory: int
        :param MaxStorageSize: Maximum instance storage capacity GB
        :type MaxStorageSize: int
        :param MinStorageSize: Minimum instance storage capacity GB
        :type MinStorageSize: int
        :param HasStock: Whether there is an inventory.
        :type HasStock: bool
        :param MachineType: Machine type
        :type MachineType: str
        :param MaxIops: Maximum IOPS
        :type MaxIops: int
        :param MaxIoBandWidth: Maximum bandwidth
        :type MaxIoBandWidth: int
        :param ZoneStockInfos: Inventory information in a region
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneStockInfos: list of ZoneStockInfo
        """
        self.Cpu = None
        self.Memory = None
        self.MaxStorageSize = None
        self.MinStorageSize = None
        self.HasStock = None
        self.MachineType = None
        self.MaxIops = None
        self.MaxIoBandWidth = None
        self.ZoneStockInfos = None


    def _deserialize(self, params):
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.MaxStorageSize = params.get("MaxStorageSize")
        self.MinStorageSize = params.get("MinStorageSize")
        self.HasStock = params.get("HasStock")
        self.MachineType = params.get("MachineType")
        self.MaxIops = params.get("MaxIops")
        self.MaxIoBandWidth = params.get("MaxIoBandWidth")
        if params.get("ZoneStockInfos") is not None:
            self.ZoneStockInfos = []
            for item in params.get("ZoneStockInfos"):
                obj = ZoneStockInfo()
                obj._deserialize(item)
                self.ZoneStockInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterRequest(AbstractModel):
    """IsolateCluster request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param DbType: This parameter has been disused.
        :type DbType: str
        """
        self.ClusterId = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterResponse(AbstractModel):
    """IsolateCluster response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Task flow ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param DealNames: Refund order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class IsolateInstanceRequest(AbstractModel):
    """IsolateInstance request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIdList: Instance ID array
        :type InstanceIdList: list of str
        :param DbType: This parameter has been disused.
        :type DbType: str
        """
        self.ClusterId = None
        self.InstanceIdList = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateInstanceResponse(AbstractModel):
    """IsolateInstance response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Task flow ID
        :type FlowId: int
        :param DealNames: Order ID for isolated instance (prepaid instance)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param BackupTimeBeg: Full backup start time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively
        :type BackupTimeBeg: int
        :param BackupTimeEnd: Full backup end time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively.
        :type BackupTimeEnd: int
        :param ReserveDuration: Backup retention period in seconds. Backups will be cleared after this period elapses. 7 days is represented by 3600*24*7 = 604800. Maximum value: 158112000.
        :type ReserveDuration: int
        :param BackupFreq: Backup frequency. It is an array of 7 elements corresponding to Monday through Sunday. full: full backup; increment: incremental backup. This parameter cannot be modified currently and doesn't need to be entered.
        :type BackupFreq: list of str
        :param BackupType: Backup mode. logic: logic backup; snapshot: snapshot backup. This parameter cannot be modified currently and doesn't need to be entered.
        :type BackupType: str
        """
        self.ClusterId = None
        self.BackupTimeBeg = None
        self.BackupTimeEnd = None
        self.ReserveDuration = None
        self.BackupFreq = None
        self.BackupType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BackupTimeBeg = params.get("BackupTimeBeg")
        self.BackupTimeEnd = params.get("BackupTimeEnd")
        self.ReserveDuration = params.get("ReserveDuration")
        self.BackupFreq = params.get("BackupFreq")
        self.BackupType = params.get("BackupType")
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


class ModifyBackupNameRequest(AbstractModel):
    """ModifyBackupName request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param BackupId: Backup file ID
        :type BackupId: int
        :param BackupName: Backup name, which can contain up to 60 characters.
        :type BackupName: str
        """
        self.ClusterId = None
        self.BackupId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BackupId = params.get("BackupId")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupNameResponse(AbstractModel):
    """ModifyBackupName response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        """
        self.ClusterId = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterParamRequest(AbstractModel):
    """ModifyClusterParam request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ParamList: List of the parameters to be modified. Each element in the list is a combination of `ParamName`, `CurrentValue`, and `OldValue`. `ParamName` is the parameter name; `CurrentValue` is the current value; `OldValue` is the old value that doesn’t need to be verified.
        :type ParamList: list of ParamItem
        :param IsInMaintainPeriod: Valid values: `yes` (execute during maintenance time), `no` (execute now)
        :type IsInMaintainPeriod: str
        """
        self.ClusterId = None
        self.ParamList = None
        self.IsInMaintainPeriod = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = ParamItem()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterParamResponse(AbstractModel):
    """ModifyClusterParam response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async request ID used to query the result
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyClusterSlaveZoneRequest(AbstractModel):
    """ModifyClusterSlaveZone request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param OldSlaveZone: Old replica AZ
        :type OldSlaveZone: str
        :param NewSlaveZone: New replica AZ
        :type NewSlaveZone: str
        """
        self.ClusterId = None
        self.OldSlaveZone = None
        self.NewSlaveZone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.OldSlaveZone = params.get("OldSlaveZone")
        self.NewSlaveZone = params.get("NewSlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterSlaveZoneResponse(AbstractModel):
    """ModifyClusterSlaveZone response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Async FlowId
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance group ID
        :type InstanceId: str
        :param SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.
        :type SecurityGroupIds: list of str
        :param Zone: AZ
        :type Zone: str
        """
        self.InstanceId = None
        self.SecurityGroupIds = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.Zone = params.get("Zone")
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


class ModifyInstanceNameRequest(AbstractModel):
    """ModifyInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
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
        


class ModifyInstanceNameResponse(AbstractModel):
    """ModifyInstanceName response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMaintainPeriodConfigRequest(AbstractModel):
    """ModifyMaintainPeriodConfig request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param MaintainStartTime: Maintenance start time in seconds. For example, 03:00 AM is represented by 10800
        :type MaintainStartTime: int
        :param MaintainDuration: Maintenance duration in seconds. For example, one hour is represented by 3600
        :type MaintainDuration: int
        :param MaintainWeekDays: Maintenance days of the week. Valid values: [Mon, Tue, Wed, Thu, Fri, Sat, Sun].
        :type MaintainWeekDays: list of str
        """
        self.InstanceId = None
        self.MaintainStartTime = None
        self.MaintainDuration = None
        self.MaintainWeekDays = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MaintainStartTime = params.get("MaintainStartTime")
        self.MaintainDuration = params.get("MaintainDuration")
        self.MaintainWeekDays = params.get("MaintainWeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintainPeriodConfigResponse(AbstractModel):
    """ModifyMaintainPeriodConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NetAddr(AbstractModel):
    """Network information

    """

    def __init__(self):
        r"""
        :param Vip: Private network IP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Vip: str
        :param Vport: Private network port number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Vport: int
        :param WanDomain: Public network domain name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WanDomain: str
        :param WanPort: Public network port number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WanPort: int
        :param NetType: Network type. Valid values: `ro` (read-only), `rw` or `ha` (read-write)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type NetType: str
        :param UniqSubnetId: Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqSubnetId: str
        :param UniqVpcId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.WanPort = None
        self.NetType = None
        self.UniqSubnetId = None
        self.UniqVpcId = None
        self.Description = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.WanPort = params.get("WanPort")
        self.NetType = params.get("NetType")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewAccount(AbstractModel):
    """Newly created account

    """

    def __init__(self):
        r"""
        :param AccountName: Account name
        :type AccountName: str
        :param AccountPassword: Password
        :type AccountPassword: str
        :param Host: Host
        :type Host: str
        :param Description: Description
        :type Description: str
        """
        self.AccountName = None
        self.AccountPassword = None
        self.Host = None
        self.Description = None


    def _deserialize(self, params):
        self.AccountName = params.get("AccountName")
        self.AccountPassword = params.get("AccountPassword")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTask(AbstractModel):
    """Task information

    """

    def __init__(self):
        r"""
        :param TaskId: Auto-Incrementing task ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param TaskType: Task type
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskType: str
        :param TaskStatus: Task status
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskStatus: str
        :param ObjectId: Task ID (cluster ID | instance group ID | instance ID)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ObjectId: str
        :param ObjectType: Task type
Note: this field may return null, indicating that no valid values can be obtained.
        :type ObjectType: str
        """
        self.TaskId = None
        self.TaskType = None
        self.TaskStatus = None
        self.ObjectId = None
        self.ObjectType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.TaskStatus = params.get("TaskStatus")
        self.ObjectId = params.get("ObjectId")
        self.ObjectType = params.get("ObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineClusterRequest(AbstractModel):
    """OfflineCluster request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineClusterResponse(AbstractModel):
    """OfflineCluster response structure.

    """

    def __init__(self):
        r"""
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


class OfflineInstanceRequest(AbstractModel):
    """OfflineInstance request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIdList: Instance ID array
        :type InstanceIdList: list of str
        """
        self.ClusterId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineInstanceResponse(AbstractModel):
    """OfflineInstance response structure.

    """

    def __init__(self):
        r"""
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


class ParamInfo(AbstractModel):
    """Parameter information

    """

    def __init__(self):
        r"""
        :param CurrentValue: Current value
        :type CurrentValue: str
        :param Default: Default value
        :type Default: str
        :param EnumValue: List of valid values when parameter type is `enum`, `string` or `bool`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnumValue: list of str
        :param Max: Maximum value when parameter type is `float` or `integer`.
        :type Max: str
        :param Min: Minimum value when parameter type is `float` or `integer`.
        :type Min: str
        :param ParamName: Parameter name
        :type ParamName: str
        :param NeedReboot: Whether to restart the instance for the modified parameters to take effect.
        :type NeedReboot: int
        :param ParamType: Parameter type: `integer`, `float`, `string`, `enum`, `bool`.
        :type ParamType: str
        :param MatchType: Match type. Regex can be used when parameter type is `string`. Valid value: `multiVal`.
        :type MatchType: str
        :param MatchValue: Match values, which will be separated by semicolon when match type is `multiVal`.
        :type MatchValue: str
        :param Description: Parameter description
        :type Description: str
        """
        self.CurrentValue = None
        self.Default = None
        self.EnumValue = None
        self.Max = None
        self.Min = None
        self.ParamName = None
        self.NeedReboot = None
        self.ParamType = None
        self.MatchType = None
        self.MatchValue = None
        self.Description = None


    def _deserialize(self, params):
        self.CurrentValue = params.get("CurrentValue")
        self.Default = params.get("Default")
        self.EnumValue = params.get("EnumValue")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.ParamName = params.get("ParamName")
        self.NeedReboot = params.get("NeedReboot")
        self.ParamType = params.get("ParamType")
        self.MatchType = params.get("MatchType")
        self.MatchValue = params.get("MatchValue")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamItem(AbstractModel):
    """Parameter to be modified

    """

    def __init__(self):
        r"""
        :param ParamName: Parameter name
        :type ParamName: str
        :param CurrentValue: New value
        :type CurrentValue: str
        :param OldValue: Original value
        :type OldValue: str
        """
        self.ParamName = None
        self.CurrentValue = None
        self.OldValue = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.CurrentValue = params.get("CurrentValue")
        self.OldValue = params.get("OldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateListInfo(AbstractModel):
    """Parameter template information

    """

    def __init__(self):
        r"""
        :param Id: Parameter template ID
        :type Id: int
        :param TemplateName: Parameter template name
        :type TemplateName: str
        :param TemplateDescription: Parameter template description
        :type TemplateDescription: str
        :param EngineVersion: Engine version
        :type EngineVersion: str
        """
        self.Id = None
        self.TemplateName = None
        self.TemplateDescription = None
        self.EngineVersion = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TemplateName = params.get("TemplateName")
        self.TemplateDescription = params.get("TemplateDescription")
        self.EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseServerlessRequest(AbstractModel):
    """PauseServerless request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ForcePause: Whether to pause forcibly and ignore the current user connections. Valid values: `0` (no), `1` (yes). Default value: `1`
        :type ForcePause: int
        """
        self.ClusterId = None
        self.ForcePause = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ForcePause = params.get("ForcePause")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseServerlessResponse(AbstractModel):
    """PauseServerless response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Async task ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class PolicyRule(AbstractModel):
    """Security group rule

    """

    def __init__(self):
        r"""
        :param Action: Policy, which can be `ACCEPT` or `DROP`
        :type Action: str
        :param CidrIp: Source IP or IP range, such as 192.168.0.0/16
        :type CidrIp: str
        :param PortRange: Port
        :type PortRange: str
        :param IpProtocol: Network protocol, such as UDP and TCP
        :type IpProtocol: str
        :param ServiceModule: Protocol port ID or protocol port group ID.
        :type ServiceModule: str
        :param AddressModule: IP address ID or IP address group ID.
        :type AddressModule: str
        :param Id: id
        :type Id: str
        :param Desc: Description
        :type Desc: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.ServiceModule = None
        self.AddressModule = None
        self.Id = None
        self.Desc = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.ServiceModule = params.get("ServiceModule")
        self.AddressModule = params.get("AddressModule")
        self.Id = params.get("Id")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """Query filter

    """

    def __init__(self):
        r"""
        :param Names: Search field. Valid values: "InstanceId", "ProjectId", "InstanceName", "Vip"
        :type Names: list of str
        :param Values: Search string
        :type Values: list of str
        :param ExactMatch: Whether to use exact match
        :type ExactMatch: bool
        :param Name: Search field
        :type Name: str
        """
        self.Names = None
        self.Values = None
        self.ExactMatch = None
        self.Name = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveClusterSlaveZoneRequest(AbstractModel):
    """RemoveClusterSlaveZone request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param SlaveZone: Replica AZ
        :type SlaveZone: str
        """
        self.ClusterId = None
        self.SlaveZone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveClusterSlaveZoneResponse(AbstractModel):
    """RemoveClusterSlaveZone response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Async FlowId
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ResumeServerlessRequest(AbstractModel):
    """ResumeServerless request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeServerlessResponse(AbstractModel):
    """ResumeServerless response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Async task ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RollbackTimeRange(AbstractModel):
    """Rollback time range

    """

    def __init__(self):
        r"""
        :param TimeRangeStart: Start time
        :type TimeRangeStart: str
        :param TimeRangeEnd: End time
        :type TimeRangeEnd: str
        """
        self.TimeRangeStart = None
        self.TimeRangeEnd = None


    def _deserialize(self, params):
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
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
        :type Inbound: list of PolicyRule
        :param Outbound: Outbound rule
        :type Outbound: list of PolicyRule
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
                obj = PolicyRule()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = PolicyRule()
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
        


class SetRenewFlagRequest(AbstractModel):
    """SetRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param ResourceIds: ID of the instance to be manipulated
        :type ResourceIds: list of str
        :param AutoRenewFlag: Auto-renewal flag. 0: normal renewal, 1: auto-renewal, 2: no renewal.
        :type AutoRenewFlag: int
        """
        self.ResourceIds = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewFlagResponse(AbstractModel):
    """SetRenewFlag response structure.

    """

    def __init__(self):
        r"""
        :param Count: Number of successfully manipulated instances
        :type Count: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class SlowQueriesItem(AbstractModel):
    """Slow query information of the instance

    """

    def __init__(self):
        r"""
        :param Timestamp: Execution timestamp
        :type Timestamp: int
        :param QueryTime: Execution duration in seconds
        :type QueryTime: float
        :param SqlText: SQL statement
        :type SqlText: str
        :param UserHost: Client host
        :type UserHost: str
        :param UserName: Username
        :type UserName: str
        :param Database: Database name
        :type Database: str
        :param LockTime: Lock duration in seconds
        :type LockTime: float
        :param RowsExamined: Number of scanned rows
        :type RowsExamined: int
        :param RowsSent: Number of returned rows
        :type RowsSent: int
        :param SqlTemplate: SQL template
        :type SqlTemplate: str
        :param SqlMd5: MD5 value of the SQL statement
        :type SqlMd5: str
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
        self.SqlMd5 = None


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
        self.SqlMd5 = params.get("SqlMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterZoneRequest(AbstractModel):
    """SwitchClusterZone request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param OldZone: The current AZ
        :type OldZone: str
        :param NewZone: New AZ
        :type NewZone: str
        :param IsInMaintainPeriod: Valid values: `yes` (execute during maintenance time), `no` (execute now)
        :type IsInMaintainPeriod: str
        """
        self.ClusterId = None
        self.OldZone = None
        self.NewZone = None
        self.IsInMaintainPeriod = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.OldZone = params.get("OldZone")
        self.NewZone = params.get("NewZone")
        self.IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterZoneResponse(AbstractModel):
    """SwitchClusterZone response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Async FlowId
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Information of tags associated with cluster, including `TagKey` and `TagValue`

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
        


class TradePrice(AbstractModel):
    """Billing details

    """

    def __init__(self):
        r"""
        :param TotalPrice: The non-discounted total price of monthly subscribed resources (unit: US cent)
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPrice: int
        :param Discount: Total discount. `100` means no discount.
        :type Discount: float
        :param TotalPriceDiscount: The discounted total price of monthly subscribed resources (unit: US cent). If a discount is applied, `TotalPriceDiscount` will be the product of `TotalPrice` and `Discount`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPriceDiscount: int
        :param UnitPrice: The non-discounted unit price of pay-as-you-go resources (unit: US cent)
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPrice: int
        :param UnitPriceDiscount: The discounted unit price of pay-as-you-go resources (unit: US cent). If a discount is applied, `UnitPriceDiscount` will be the product of `UnitPrice` and `Discount`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: int
        :param ChargeUnit: Price unit
        :type ChargeUnit: str
        """
        self.TotalPrice = None
        self.Discount = None
        self.TotalPriceDiscount = None
        self.UnitPrice = None
        self.UnitPriceDiscount = None
        self.ChargeUnit = None


    def _deserialize(self, params):
        self.TotalPrice = params.get("TotalPrice")
        self.Discount = params.get("Discount")
        self.TotalPriceDiscount = params.get("TotalPriceDiscount")
        self.UnitPrice = params.get("UnitPrice")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")
        self.ChargeUnit = params.get("ChargeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Cpu: Database CPU
        :type Cpu: int
        :param Memory: Database memory in GB
        :type Memory: int
        :param UpgradeType: Upgrade type. Valid values: upgradeImmediate, upgradeInMaintain
        :type UpgradeType: str
        :param StorageLimit: This parameter has been disused.
        :type StorageLimit: int
        :param AutoVoucher: Whether to automatically select a voucher. 1: yes; 0: no. Default value: 0
        :type AutoVoucher: int
        :param DbType: This parameter has been disused.
        :type DbType: str
        :param DealMode: Transaction mode. Valid values: `0` (place and pay for an order), `1` (place an order)
        :type DealMode: int
        """
        self.InstanceId = None
        self.Cpu = None
        self.Memory = None
        self.UpgradeType = None
        self.StorageLimit = None
        self.AutoVoucher = None
        self.DbType = None
        self.DealMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.UpgradeType = params.get("UpgradeType")
        self.StorageLimit = params.get("StorageLimit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.DbType = params.get("DbType")
        self.DealMode = params.get("DealMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance response structure.

    """

    def __init__(self):
        r"""
        :param TranId: Freezing transaction ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param BigDealIds: Big order ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BigDealIds: list of str
        :param DealNames: Order ID
        :type DealNames: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TranId = None
        self.BigDealIds = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.BigDealIds = params.get("BigDealIds")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class ZoneStockInfo(AbstractModel):
    """Inventory information in an AZ

    """

    def __init__(self):
        r"""
        :param Zone: AZ
        :type Zone: str
        :param HasStock: Whether there is an inventory.
        :type HasStock: bool
        """
        self.Zone = None
        self.HasStock = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.HasStock = params.get("HasStock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        