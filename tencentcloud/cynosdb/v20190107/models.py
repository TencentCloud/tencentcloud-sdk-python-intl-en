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
        """
        :param AccountName: Database account name\n        :type AccountName: str\n        :param Description: Database account description\n        :type Description: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param UpdateTime: Update time\n        :type UpdateTime: str\n        :param Host: Host\n        :type Host: str\n        """
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
        


class AddInstancesRequest(AbstractModel):
    """AddInstances request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param Cpu: Number of CPU cores\n        :type Cpu: int\n        :param Memory: Memory\n        :type Memory: int\n        :param ReadOnlyCount: Number of added read-only instances\n        :type ReadOnlyCount: int\n        :param InstanceGrpId: Instance group ID, which is used when you add an instance in an existing RO group. If this parameter is left empty, an RO group will be created.\n        :type InstanceGrpId: str\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        :param Port: Port used when adding RO group\n        :type Port: int\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param AutoVoucher: Whether to automatically select a voucher. 1: yes; 0: no. Default value: 0\n        :type AutoVoucher: int\n        :param DbType: Database type. Valid values: 
<li> MYSQL </li>\n        :type DbType: str\n        :param OrderSource: Order source\n        :type OrderSource: str\n        """
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
        """
        :param TranId: Freezing transaction. One freezing transaction ID is generated each time an instance is added.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranId: str\n        :param DealNames: Pay-as-You-Go order ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DealNames: list of str\n        :param ResourceIds: List of IDs of delivered resources
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResourceIds: list of str\n        :param BigDealIds: Big order ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BigDealIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param IP: IP\n        :type IP: str\n        :param Port: Port\n        :type Port: int\n        """
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
        """
        :param SnapshotId: Snapshot file ID used for rollback\n        :type SnapshotId: int\n        :param FileName: Snapshot file name\n        :type FileName: str\n        :param FileSize: Snapshot file size\n        :type FileSize: int\n        :param StartTime: Snapshot backup start time\n        :type StartTime: str\n        :param FinishTime: Snapshot backup end time\n        :type FinishTime: str\n        :param BackupType: Backup type. snapshot: snapshot backup; timepoint: time point backup\n        :type BackupType: str\n        :param BackupMethod: Back mode. auto: auto backup; manual: manual backup\n        :type BackupMethod: str\n        :param BackupStatus: Backup file status. success: backup succeeded; fail: backup failed; creating: creating backup file; deleting: deleting backup file\n        :type BackupStatus: str\n        :param SnapshotTime: Backup file time\n        :type SnapshotTime: str\n        """
        self.SnapshotId = None
        self.FileName = None
        self.FileSize = None
        self.StartTime = None
        self.FinishTime = None
        self.BackupType = None
        self.BackupMethod = None
        self.BackupStatus = None
        self.SnapshotTime = None


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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param InstanceIds: Instance ID list\n        :type InstanceIds: list of str\n        """
        self.ClusterId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
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
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param InstanceType: Engine type\n        :type InstanceType: str\n        :param InstanceStatus: Instance status\n        :type InstanceStatus: str\n        :param InstanceStatusDesc: Instance status description\n        :type InstanceStatusDesc: str\n        :param InstanceCpu: Number of CPU cores\n        :type InstanceCpu: int\n        :param InstanceMemory: Memory\n        :type InstanceMemory: int\n        :param InstanceStorage: Disk\n        :type InstanceStorage: int\n        """
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
        


class CreateClustersRequest(AbstractModel):
    """CreateClusters request structure.

    """

    def __init__(self):
        """
        :param Zone: AZ\n        :type Zone: str\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        :param DbType: Database type. Valid values: 
<li> MYSQL </li>\n        :type DbType: str\n        :param DbVersion: Database version. Valid values: 
<li> Valid values for `MYSQL`: 5.7 </li>\n        :type DbVersion: str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param Cpu: Number of CPU cores of normal instance\n        :type Cpu: int\n        :param Memory: Memory of a non-serverless instance in GB\n        :type Memory: int\n        :param Storage: Storage capacity in GB\n        :type Storage: int\n        :param ClusterName: Cluster name\n        :type ClusterName: str\n        :param AdminPassword: Account password (it must contain 8-64 characters in at least three of the following four types: uppercase letters, lowercase letters, digits, and symbols (~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/).)\n        :type AdminPassword: str\n        :param Port: Port. Default value: 5432\n        :type Port: int\n        :param PayMode: Billing mode. 0: pay-as-you-go; 1: monthly subscription. Default value: 0\n        :type PayMode: int\n        :param Count: Number of purchased items. Currently, only 1 can be passed in. If this parameter is left empty, 1 will be used by default.\n        :type Count: int\n        :param RollbackStrategy: Rollback type:
noneRollback: no rollback
snapRollback: rollback by snapshot
timeRollback: rollback by time point\n        :type RollbackStrategy: str\n        :param RollbackId: `snapshotId` for snapshot rollback or `queryId` for time point rollback. 0 indicates to determine whether the time point is valid\n        :type RollbackId: int\n        :param OriginalClusterId: Pass in the source cluster ID during rollback to find the source `poolId`\n        :type OriginalClusterId: str\n        :param ExpectTime: Specified time for time point rollback or snapshot time for snapshot rollback\n        :type ExpectTime: str\n        :param ExpectTimeThresh: Specified allowed time range for time point rollback\n        :type ExpectTimeThresh: int\n        :param StorageLimit: The maximum storage of a non-serverless instance in GB
If `DbType` is `MYSQL` and the storage billing mode is prepaid, the parameter value cannot exceed the maximum storage corresponding to the CPU and memory specifications.\n        :type StorageLimit: int\n        :param InstanceCount: Number of instances\n        :type InstanceCount: int\n        :param TimeSpan: Purchase duration of monthly subscription plan\n        :type TimeSpan: int\n        :param TimeUnit: Purchase duration unit of monthly subscription plan\n        :type TimeUnit: str\n        :param AutoRenewFlag: Whether auto-renewal is enabled for monthly subscription plan\n        :type AutoRenewFlag: int\n        :param AutoVoucher: Whether to automatically select a voucher. 1: yes; 0: no. Default value: 0\n        :type AutoVoucher: int\n        :param HaCount: Number of instances (this parameter has been disused and is retained only for compatibility with existing instances)\n        :type HaCount: int\n        :param OrderSource: Order source\n        :type OrderSource: str\n        :param ResourceTags: Array of tags to be bound to the created cluster\n        :type ResourceTags: list of Tag\n        :param DbMode: Database type
Valid values when `DbType` is `MYSQL` (default value: NORMAL):
<li>NORMAL</li>
<li>SERVERLESS</li>\n        :type DbMode: str\n        :param MinCpu: This parameter is required if `DbMode` is `SERVERLESS`
Minimum number of CPU cores. For the value range, please see the returned result of `DescribeServerlessInstanceSpecs`\n        :type MinCpu: float\n        :param MaxCpu: This parameter is required if `DbMode` is `SERVERLESS`:
Maximum number of CPU cores. For the value range, please see the returned result of `DescribeServerlessInstanceSpecs`\n        :type MaxCpu: float\n        :param AutoPause: This parameter specifies whether the cluster will be automatically paused if `DbMode` is `SERVERLESS`. Valid values:
<li>yes</li>
<li>no</li>
Default value: yes\n        :type AutoPause: str\n        :param AutoPauseDelay: This parameter specifies the delay for automatic cluster pause in seconds if `DbMode` is `SERVERLESS`. Value range: [600,691200]
Default value: 600\n        :type AutoPauseDelay: int\n        :param StoragePayMode: The billing mode of cluster storage. Valid values: `0` (postpaid), `1` (prepaid). Default value: `0`.
If `DbType` is `MYSQL` and the billing mode of cluster compute is pay-as-you-go (or the `DbMode` is `SERVERLESS`), the billing mode of cluster storage must be postpaid.
Clusters with storage billed in prepaid mode cannot be cloned or rolled back.\n        :type StoragePayMode: int\n        """
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
        """
        :param TranId: Freezing transaction ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranId: str\n        :param DealNames: Order ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DealNames: list of str\n        :param ResourceIds: List of resource IDs (this parameter may not be returned in case of asynchronous delivery. We strongly recommend you call the `DescribeResourcesByDealName` API with the `dealNames` field to get the IDs of asynchronously delivered resources)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResourceIds: list of str\n        :param ClusterIds: List of cluster IDs (this parameter may not be returned in case of asynchronous delivery. We strongly recommend you call the `DescribeResourcesByDealName` API with the `dealNames` field to get the IDs of asynchronously delivered clusters)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClusterIds: list of str\n        :param BigDealIds: Big order ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BigDealIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Status: Cluster status\n        :type Status: str\n        :param UpdateTime: Update time\n        :type UpdateTime: str\n        :param Zone: AZ\n        :type Zone: str\n        :param ClusterName: Cluster name\n        :type ClusterName: str\n        :param Region: Region\n        :type Region: str\n        :param DbVersion: Database version\n        :type DbVersion: str\n        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param InstanceNum: Number of instances\n        :type InstanceNum: int\n        :param Uin: User `uin`\n        :type Uin: str\n        :param DbType: Engine type\n        :type DbType: str\n        :param AppId: User `appid`\n        :type AppId: int\n        :param StatusDesc: Cluster status description\n        :type StatusDesc: str\n        :param CreateTime: Cluster creation time\n        :type CreateTime: str\n        :param PayMode: Billing mode. 0: pay-as-you-go; 1: monthly subscription\n        :type PayMode: int\n        :param PeriodEndTime: End time\n        :type PeriodEndTime: str\n        :param Vip: Cluster read-write VIP\n        :type Vip: str\n        :param Vport: Cluster read-write vport\n        :type Vport: int\n        :param ProjectID: Project ID\n        :type ProjectID: int\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        :param CynosVersion: TDSQL-C kernel version\n        :type CynosVersion: str\n        :param StorageLimit: Storage capacity\n        :type StorageLimit: int\n        :param RenewFlag: Renewal flag\n        :type RenewFlag: int\n        :param ProcessingTask: Task in progress\n        :type ProcessingTask: str\n        :param Tasks: Array of tasks in cluster\n        :type Tasks: list of ObjectTask\n        :param ResourceTags: Array of tags bound to cluster\n        :type ResourceTags: list of Tag\n        :param DbMode: Database type (`NORMAL` or `SERVERLESS`)\n        :type DbMode: str\n        :param ServerlessStatus: Serverless cluster status when the database type is `SERVERLESS`. Valid values:
resume
pause\n        :type ServerlessStatus: str\n        :param Storage: Prepaid cluster storage\n        :type Storage: int\n        :param StorageId: Cluster storage ID used in prepaid storage modification\n        :type StorageId: str\n        :param StoragePayMode: Billing mode of cluster storage. Valid values: `0` (postpaid), `1` (prepaid)\n        :type StoragePayMode: int\n        :param MinStorageSize: The minimum storage corresponding to the compute specifications of the cluster\n        :type MinStorageSize: int\n        :param MaxStorageSize: The maximum storage corresponding to the compute specifications of the cluster\n        :type MaxStorageSize: int\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param ClusterName: Cluster name\n        :type ClusterName: str\n        :param Region: Region\n        :type Region: str\n        :param Status: Status\n        :type Status: str\n        :param StatusDesc: Status description\n        :type StatusDesc: str\n        :param VpcName: VPC name\n        :type VpcName: str\n        :param VpcId: Unique VPC ID\n        :type VpcId: str\n        :param SubnetName: Subnet name\n        :type SubnetName: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        :param Charset: Character set\n        :type Charset: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param DbType: Database type\n        :type DbType: str\n        :param DbVersion: Database version\n        :type DbVersion: str\n        :param UsedStorage: Used capacity\n        :type UsedStorage: int\n        :param RoAddr: vport for read/write separation\n        :type RoAddr: list of Addr\n        :param InstanceSet: Instance information\n        :type InstanceSet: list of ClusterInstanceDetail\n        :param PayMode: Billing mode\n        :type PayMode: int\n        :param PeriodEndTime: Expiration time\n        :type PeriodEndTime: str\n        :param Vip: VIP\n        :type Vip: str\n        :param Vport: vport\n        :type Vport: int\n        :param ProjectID: Project ID\n        :type ProjectID: int\n        :param Zone: AZ\n        :type Zone: str\n        :param ResourceTags: Array of tags bound to instance\n        :type ResourceTags: list of Tag\n        :param ServerlessStatus: Serverless cluster status when the database type is `SERVERLESS`. Valid values:
resume
resuming
pause
pausing\n        :type ServerlessStatus: str\n        """
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
        """
        :param Uin: User `Uin`\n        :type Uin: str\n        :param AppId: User `AppId`\n        :type AppId: int\n        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param ClusterName: Cluster name\n        :type ClusterName: str\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param Region: Region\n        :type Region: str\n        :param Zone: AZ\n        :type Zone: str\n        :param Status: Instance status\n        :type Status: str\n        :param StatusDesc: Instance status description\n        :type StatusDesc: str\n        :param DbType: Database type\n        :type DbType: str\n        :param DbVersion: Database version\n        :type DbVersion: str\n        :param Cpu: Number of CPU cores\n        :type Cpu: int\n        :param Memory: Memory in GB\n        :type Memory: int\n        :param Storage: Storage capacity in GB\n        :type Storage: int\n        :param InstanceType: Instance type\n        :type InstanceType: str\n        :param InstanceRole: Current instance role\n        :type InstanceRole: str\n        :param UpdateTime: Update time\n        :type UpdateTime: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        :param Vip: Private IP of instance\n        :type Vip: str\n        :param Vport: Private port of instance\n        :type Vport: int\n        :param PayMode: Billing mode\n        :type PayMode: int\n        :param PeriodEndTime: Instance expiration time\n        :type PeriodEndTime: str\n        :param DestroyDeadlineText: Termination deadline\n        :type DestroyDeadlineText: str\n        :param IsolateTime: Isolation time\n        :type IsolateTime: str\n        :param NetType: Network type\n        :type NetType: int\n        :param WanDomain: Public domain name\n        :type WanDomain: str\n        :param WanIP: Public IP\n        :type WanIP: str\n        :param WanPort: Public port\n        :type WanPort: int\n        :param WanStatus: Public network status\n        :type WanStatus: str\n        :param DestroyTime: Instance termination time\n        :type DestroyTime: str\n        :param CynosVersion: TDSQL-C kernel version\n        :type CynosVersion: str\n        :param ProcessingTask: Task in progress\n        :type ProcessingTask: str\n        :param RenewFlag: Renewal flag\n        :type RenewFlag: int\n        :param MinCpu: Minimum number of CPU cores for serverless instance\n        :type MinCpu: float\n        :param MaxCpu: Maximum number of CPU cores for serverless instance\n        :type MaxCpu: float\n        :param ServerlessStatus: Serverless instance status. Valid values:
resume
pause\n        :type ServerlessStatus: str\n        :param StoragePayMode: Storage billing mode
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type StoragePayMode: int\n        :param StorageId: Prepaid storage ID
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type StorageId: str\n        """
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
        self.StoragePayMode = None
        self.StorageId = None


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
        self.StoragePayMode = params.get("StoragePayMode")
        self.StorageId = params.get("StorageId")
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
        """
        :param Uin: User `Uin`\n        :type Uin: str\n        :param AppId: User `AppId`\n        :type AppId: int\n        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param ClusterName: Cluster name\n        :type ClusterName: str\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param Region: Region\n        :type Region: str\n        :param Zone: AZ\n        :type Zone: str\n        :param Status: Instance status\n        :type Status: str\n        :param StatusDesc: Instance status description\n        :type StatusDesc: str\n        :param DbType: Database type\n        :type DbType: str\n        :param DbVersion: Database version\n        :type DbVersion: str\n        :param Cpu: Number of CPU cores\n        :type Cpu: int\n        :param Memory: Memory in GB\n        :type Memory: int\n        :param Storage: Storage capacity in GB\n        :type Storage: int\n        :param InstanceType: Instance type\n        :type InstanceType: str\n        :param InstanceRole: Current instance role\n        :type InstanceRole: str\n        :param UpdateTime: Update time\n        :type UpdateTime: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param PayMode: Billing mode\n        :type PayMode: int\n        :param PeriodEndTime: Instance expiration time\n        :type PeriodEndTime: str\n        :param NetType: Network type\n        :type NetType: int\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        :param Vip: Private IP of instance\n        :type Vip: str\n        :param Vport: Private port of instance\n        :type Vport: int\n        :param WanDomain: Public domain name of instance\n        :type WanDomain: str\n        :param Charset: Character set\n        :type Charset: str\n        :param CynosVersion: TDSQL-C kernel version\n        :type CynosVersion: str\n        :param RenewFlag: Renewal flag\n        :type RenewFlag: int\n        :param MinCpu: The minimum number of CPU cores for a serverless instance\n        :type MinCpu: float\n        :param MaxCpu: The maximum number of CPU cores for a serverless instance\n        :type MaxCpu: float\n        :param ServerlessStatus: Serverless instance status. Valid values:
resume
pause\n        :type ServerlessStatus: str\n        """
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
        """
        :param AppId: appId\n        :type AppId: int\n        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param CreatedTime: Creation time\n        :type CreatedTime: str\n        :param DeletedTime: Deletion time\n        :type DeletedTime: str\n        :param InstanceGrpId: Instance group ID\n        :type InstanceGrpId: str\n        :param Status: Status\n        :type Status: str\n        :param Type: Instance group type. ha: HA group; ro: RO group\n        :type Type: str\n        :param UpdatedTime: Update time\n        :type UpdatedTime: str\n        :param Vip: Private IP\n        :type Vip: str\n        :param Vport: Private port\n        :type Vport: int\n        :param WanDomain: Public domain name\n        :type WanDomain: str\n        :param WanIP: Public IP\n        :type WanIP: str\n        :param WanPort: Public port\n        :type WanPort: int\n        :param WanStatus: Public network status\n        :type WanStatus: str\n        :param InstanceSet: Information of instances contained in instance group\n        :type InstanceSet: list of CynosdbInstance\n        """
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
        


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param AccountNames: List of accounts to be filtered\n        :type AccountNames: list of str\n        :param DbType: Database type. Valid values: 
<li> MYSQL </li>\n        :type DbType: str\n        """
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
        """
        :param AccountSet: Database account list\n        :type AccountSet: list of Account\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        """
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
        """
        :param BackupTimeBeg: Full backup start time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively\n        :type BackupTimeBeg: int\n        :param BackupTimeEnd: Full backup end time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively\n        :type BackupTimeEnd: int\n        :param ReserveDuration: Backup retention period in seconds. Backups will be cleared after this period elapses. 7 days is represented by 3600*24*7 = 604800\n        :type ReserveDuration: int\n        :param BackupFreq: Backup frequency. It is an array of 7 elements corresponding to Monday through Sunday. full: full backup; increment: incremental backup
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BackupFreq: list of str\n        :param BackupType: Backup mode. logic: logic backup; snapshot: snapshot backup
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BackupType: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeBackupListRequest(AbstractModel):
    """DescribeBackupList request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param Limit: Backup file list offset\n        :type Limit: int\n        :param Offset: Backup file list start\n        :type Offset: int\n        :param DbType: Database type. Valid values: 
<li> MYSQL </li>\n        :type DbType: str\n        """
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.DbType = params.get("DbType")
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
        """
        :param TotalCount: Total number of backup files\n        :type TotalCount: int\n        :param BackupList: Backup file list\n        :type BackupList: list of BackupFileInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        """
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
        """
        :param Detail: Cluster details\n        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbClusterDetail`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        """
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
        """
        :param TotalCount: Number of instance groups\n        :type TotalCount: int\n        :param InstanceGrpInfoList: Instance group list\n        :type InstanceGrpInfoList: list of CynosdbInstanceGrp\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        """
        :param DbType: Engine type. Valid values: MYSQL, POSTGRESQL\n        :type DbType: str\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100\n        :type Limit: int\n        :param Offset: Record offset. Default value: 0\n        :type Offset: int\n        :param OrderBy: Sort by field. Valid values:
<li> CREATETIME: creation time</li>
<li> PERIODENDTIME: expiration time</li>\n        :type OrderBy: str\n        :param OrderByType: Sorting order. Valid values:
<li> ASC: ascending</li>
<li> DESC: descending</li>\n        :type OrderByType: str\n        :param Filters: Filter. If more than one filter exists, the logical relationship between these filters is `AND`.\n        :type Filters: list of QueryFilter\n        """
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
        """
        :param TotalCount: Number of clusters\n        :type TotalCount: int\n        :param ClusterSet: Cluster list\n        :type ClusterSet: list of CynosdbCluster\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param InstanceId: Instance group ID\n        :type InstanceId: str\n        """
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
        """
        :param Groups: Security group information\n        :type Groups: list of SecurityGroup\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail response structure.

    """

    def __init__(self):
        """
        :param Detail: Instance details\n        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbInstanceDetail`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self.Detail = CynosdbInstanceDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceSpecsRequest(AbstractModel):
    """DescribeInstanceSpecs request structure.

    """

    def __init__(self):
        """
        :param DbType: Database type. Valid values: 
<li> MYSQL </li>\n        :type DbType: str\n        """
        self.DbType = None


    def _deserialize(self, params):
        self.DbType = params.get("DbType")
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
        """
        :param InstanceSpecSet: Specification information\n        :type InstanceSpecSet: list of InstanceSpec\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100\n        :type Limit: int\n        :param Offset: Record offset. Default value: 0\n        :type Offset: int\n        :param OrderBy: Sort by field. Valid values:
<li> CREATETIME: creation time</li>
<li> PERIODENDTIME: expiration time</li>\n        :type OrderBy: str\n        :param OrderByType: Sorting order. Valid values:
<li> ASC: ascending</li>
<li> DESC: descending</li>\n        :type OrderByType: str\n        :param Filters: Filter. If more than one filter exists, the logical relationship between these filters is `AND`.\n        :type Filters: list of QueryFilter\n        :param DbType: Engine type. Valid values: MYSQL, POSTGRESQL\n        :type DbType: str\n        :param Status: Instance status\n        :type Status: str\n        :param InstanceIds: Instance ID list\n        :type InstanceIds: list of str\n        """
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
        """
        :param TotalCount: Number of instances\n        :type TotalCount: int\n        :param InstanceSet: Instance list\n        :type InstanceSet: list of CynosdbInstance\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        


class DescribeMaintainPeriodResponse(AbstractModel):
    """DescribeMaintainPeriod response structure.

    """

    def __init__(self):
        """
        :param MaintainWeekDays: Maintenance days of the week\n        :type MaintainWeekDays: list of str\n        :param MaintainStartTime: Maintenance start time in seconds\n        :type MaintainStartTime: int\n        :param MaintainDuration: Maintenance duration in seconds\n        :type MaintainDuration: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MaintainWeekDays = None
        self.MaintainStartTime = None
        self.MaintainDuration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaintainWeekDays = params.get("MaintainWeekDays")
        self.MaintainStartTime = params.get("MaintainStartTime")
        self.MaintainDuration = params.get("MaintainDuration")
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param ProjectId: Project ID\n        :type ProjectId: int\n        """
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
        :param Groups: Security group details\n        :type Groups: list of SecurityGroup\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DealName: Order ID. (If the cluster is not delivered yet, the `DescribeResourcesByDealName` API may return the `InvalidParameterValue.DealNameNotFound` error. Please call the API again until it succeeds.)\n        :type DealName: str\n        """
        self.DealName = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
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
        """
        :param BillingResourceInfos: Billable resource ID information array\n        :type BillingResourceInfos: list of BillingResourceInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        """
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
        """
        :param TimeRangeStart: Start time point of valid rollback time range\n        :type TimeRangeStart: str\n        :param TimeRangeEnd: End time point of valid rollback time range\n        :type TimeRangeEnd: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TimeRangeStart = None
        self.TimeRangeEnd = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        self.RequestId = params.get("RequestId")


class DescribeRollbackTimeValidityRequest(AbstractModel):
    """DescribeRollbackTimeValidity request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param ExpectTime: Expected time point to roll back to\n        :type ExpectTime: str\n        :param ExpectTimeThresh: Error tolerance range for rollback time point\n        :type ExpectTimeThresh: int\n        """
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
        """
        :param PoolId: Storage `poolID`\n        :type PoolId: int\n        :param QueryId: Rollback task ID, which needs to be passed in when rolling back to this time point\n        :type QueryId: int\n        :param Status: Whether the time point is valid. pass: check passed; fail: check failed\n        :type Status: str\n        :param SuggestTime: Suggested time point. This value takes effect only if `Status` is `fail`\n        :type SuggestTime: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class InstanceSpec(AbstractModel):
    """Details of purchasable instance specifications. `Cpu` and `Memory` determine the instance specification during instance creation. The value range of the storage capacity is [MinStorageSize,MaxStorageSize]

    """

    def __init__(self):
        """
        :param Cpu: Number of instance CPU cores\n        :type Cpu: int\n        :param Memory: Instance memory in GB\n        :type Memory: int\n        :param MaxStorageSize: Maximum instance storage capacity GB\n        :type MaxStorageSize: int\n        :param MinStorageSize: Minimum instance storage capacity GB\n        :type MinStorageSize: int\n        """
        self.Cpu = None
        self.Memory = None
        self.MaxStorageSize = None
        self.MinStorageSize = None


    def _deserialize(self, params):
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.MaxStorageSize = params.get("MaxStorageSize")
        self.MinStorageSize = params.get("MinStorageSize")
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param DbType: Database type. Valid values: 
<li> MYSQL </li>\n        :type DbType: str\n        """
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
        """
        :param FlowId: Task flow ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FlowId: int\n        :param DealNames: Refund order ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DealNames: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param InstanceIdList: Instance ID array\n        :type InstanceIdList: list of str\n        :param DbType: Database type. Valid values: 
<li> MYSQL </li>\n        :type DbType: str\n        """
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
        """
        :param FlowId: Task flow ID\n        :type FlowId: int\n        :param DealNames: Order ID for isolated instance (prepaid instance)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DealNames: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param BackupTimeBeg: Full backup start time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively\n        :type BackupTimeBeg: int\n        :param BackupTimeEnd: Full backup start time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively\n        :type BackupTimeEnd: int\n        :param ReserveDuration: Backup retention period in seconds. Backups will be cleared after this period elapses. 7 days is represented by 3600*24*7 = 604800\n        :type ReserveDuration: int\n        :param BackupFreq: Backup frequency. It is an array of 7 elements corresponding to Monday through Sunday. full: full backup; increment: incremental backup\n        :type BackupFreq: list of str\n        :param BackupType: Backup mode. logic: logic backup; snapshot: snapshot backup\n        :type BackupType: str\n        """
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
        :param InstanceId: Instance group ID\n        :type InstanceId: str\n        :param SecurityGroupIds: List of IDs of the security groups to be modified, which is an array of one or more security group IDs.\n        :type SecurityGroupIds: list of str\n        :param Zone: AZ\n        :type Zone: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMaintainPeriodConfigRequest(AbstractModel):
    """ModifyMaintainPeriodConfig request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param MaintainStartTime: Maintenance start time in seconds. For example, 03:00 AM is represented by 10800\n        :type MaintainStartTime: int\n        :param MaintainDuration: Maintenance duration in seconds. For example, one hour is represented by 3600\n        :type MaintainDuration: int\n        :param MaintainWeekDays: Maintenance days of the week\n        :type MaintainWeekDays: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ObjectTask(AbstractModel):
    """Task information

    """

    def __init__(self):
        """
        :param TaskId: Auto-Incrementing task ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskId: int\n        :param TaskType: Task type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskType: str\n        :param TaskStatus: Task status
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskStatus: str\n        :param ObjectId: Task ID (cluster ID | instance group ID | instance ID)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ObjectId: str\n        :param ObjectType: Task type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ObjectType: str\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        """
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
        """
        :param FlowId: Task flow ID\n        :type FlowId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class OfflineInstanceRequest(AbstractModel):
    """OfflineInstance request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param InstanceIdList: Instance ID array\n        :type InstanceIdList: list of str\n        """
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
        """
        :param FlowId: Task flow ID\n        :type FlowId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class PolicyRule(AbstractModel):
    """Security group rule

    """

    def __init__(self):
        """
        :param Action: Policy, which can be `ACCEPT` or `DROP`\n        :type Action: str\n        :param CidrIp: Source IP or IP range, such as 192.168.0.0/16\n        :type CidrIp: str\n        :param PortRange: Port\n        :type PortRange: str\n        :param IpProtocol: Network protocol, such as UDP and TCP\n        :type IpProtocol: str\n        :param ServiceModule: Protocol port ID or protocol port group ID.\n        :type ServiceModule: str\n        :param AddressModule: IP address ID or IP address group ID.\n        :type AddressModule: str\n        :param Id: id\n        :type Id: str\n        :param Desc: Description\n        :type Desc: str\n        """
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
        """
        :param Names: Search field. Valid values: "InstanceId", "ProjectId", "InstanceName", "Vip"\n        :type Names: list of str\n        :param Values: Search string\n        :type Values: list of str\n        :param ExactMatch: Whether to use exact match\n        :type ExactMatch: bool\n        :param Name: Search field\n        :type Name: str\n        """
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
        


class SecurityGroup(AbstractModel):
    """Security group details

    """

    def __init__(self):
        """
        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss\n        :type CreateTime: str\n        :param Inbound: Inbound rule\n        :type Inbound: list of PolicyRule\n        :param Outbound: Outbound rule\n        :type Outbound: list of PolicyRule\n        :param SecurityGroupId: Security group ID\n        :type SecurityGroupId: str\n        :param SecurityGroupName: Security group name\n        :type SecurityGroupName: str\n        :param SecurityGroupRemark: Security group remarks\n        :type SecurityGroupRemark: str\n        """
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
        """
        :param ResourceIds: ID of the instance to be manipulated\n        :type ResourceIds: list of str\n        :param AutoRenewFlag: Auto-Renewal flag\n        :type AutoRenewFlag: int\n        """
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
        """
        :param Count: Number of successfully manipulated instances\n        :type Count: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Information of tags associated with cluster, including `TagKey` and `TagValue`

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
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param Cpu: Database CPU\n        :type Cpu: int\n        :param Memory: Database memory\n        :type Memory: int\n        :param UpgradeType: Upgrade type. Valid values: upgradeImmediate, upgradeInMaintain\n        :type UpgradeType: str\n        :param StorageLimit: Storage upper limit. 0 indicates to use the standard configuration\n        :type StorageLimit: int\n        :param AutoVoucher: Whether to automatically select a voucher. 1: yes; 0: no. Default value: 0\n        :type AutoVoucher: int\n        :param DbType: Database type. Valid values: 
<li> MYSQL </li>\n        :type DbType: str\n        """
        self.InstanceId = None
        self.Cpu = None
        self.Memory = None
        self.UpgradeType = None
        self.StorageLimit = None
        self.AutoVoucher = None
        self.DbType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.UpgradeType = params.get("UpgradeType")
        self.StorageLimit = params.get("StorageLimit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.DbType = params.get("DbType")
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
        """
        :param TranId: Freezing transaction ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranId: str\n        :param BigDealIds: Big order ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BigDealIds: list of str\n        :param DealNames: Order ID\n        :type DealNames: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TranId = None
        self.BigDealIds = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.BigDealIds = params.get("BigDealIds")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")