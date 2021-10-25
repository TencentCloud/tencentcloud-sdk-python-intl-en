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


class AssignProjectRequest(AbstractModel):
    """AssignProject request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: List of instance IDs in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceIds: list of str
        :param ProjectId: Project ID
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignProjectResponse(AbstractModel):
    """AssignProject response structure.

    """

    def __init__(self):
        r"""
        :param FlowIds: List of the returned async task IDs
        :type FlowIds: list of int non-negative
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.RequestId = params.get("RequestId")


class BackupDownloadTask(AbstractModel):
    """Backup download task information

    """

    def __init__(self):
        r"""
        :param CreateTime: Task creation time
        :type CreateTime: str
        :param BackupName: Backup name
        :type BackupName: str
        :param ReplicaSetId: Shard name
        :type ReplicaSetId: str
        :param BackupSize: Backup size in bytes
        :type BackupSize: int
        :param Status: Task status. Valid values: `0` (waiting for execution), `1` (downloading), `2` (downloaded), `3` (download failed), `4` (waiting for retry)
        :type Status: int
        :param Percent: Task progress in percentage
        :type Percent: int
        :param TimeSpend: Task duration in seconds
        :type TimeSpend: int
        :param Url: Backup download address
        :type Url: str
        """
        self.CreateTime = None
        self.BackupName = None
        self.ReplicaSetId = None
        self.BackupSize = None
        self.Status = None
        self.Percent = None
        self.TimeSpend = None
        self.Url = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.BackupName = params.get("BackupName")
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.BackupSize = params.get("BackupSize")
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        self.TimeSpend = params.get("TimeSpend")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadTaskStatus(AbstractModel):
    """The result of the created backup download task

    """

    def __init__(self):
        r"""
        :param ReplicaSetId: Shard name
        :type ReplicaSetId: str
        :param Status: Task status. Valid values: `0` (waiting for execution), `1` (downloading), `2` (downloaded), `3` (download failed), `4` (waiting for retry)
        :type Status: int
        """
        self.ReplicaSetId = None
        self.Status = None


    def _deserialize(self, params):
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFile(AbstractModel):
    """Storage information of a backup file

    """

    def __init__(self):
        r"""
        :param ReplicateSetId: ID of the replica set/shard to which a backup file belongs
        :type ReplicateSetId: str
        :param File: Path to a backup file
        :type File: str
        """
        self.ReplicateSetId = None
        self.File = None


    def _deserialize(self, params):
        self.ReplicateSetId = params.get("ReplicateSetId")
        self.File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInfo(AbstractModel):
    """Backup information

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param BackupType: Backup mode. 0: automatic backup; 1: manual backup
        :type BackupType: int
        :param BackupName: Backup name
        :type BackupName: str
        :param BackupDesc: Backup remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupDesc: str
        :param BackupSize: Backup file size in KB
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupSize: int
        :param StartTime: Backup start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param EndTime: Backup end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param Status: Backup status. 1: backing up; 2: backed up successful
        :type Status: int
        :param BackupMethod: Backup method. 0: logical backup; 1: physical backup
        :type BackupMethod: int
        """
        self.InstanceId = None
        self.BackupType = None
        self.BackupName = None
        self.BackupDesc = None
        self.BackupSize = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.BackupMethod = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupType = params.get("BackupType")
        self.BackupName = params.get("BackupName")
        self.BackupDesc = params.get("BackupDesc")
        self.BackupSize = params.get("BackupSize")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.BackupMethod = params.get("BackupMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientConnection(AbstractModel):
    """Client connection information, including client IP and number of connections

    """

    def __init__(self):
        r"""
        :param IP: Client IP of a connection
        :type IP: str
        :param Count: Number of connections corresponding to a client IP
        :type Count: int
        """
        self.IP = None
        self.Count = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDBInstanceRequest(AbstractModel):
    """CreateBackupDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param BackupMethod: Valid values: 0 (logical backup), 1 (physical backup)
        :type BackupMethod: int
        :param BackupRemark: Backup remarks
        :type BackupRemark: str
        """
        self.InstanceId = None
        self.BackupMethod = None
        self.BackupRemark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMethod = params.get("BackupMethod")
        self.BackupRemark = params.get("BackupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDBInstanceResponse(AbstractModel):
    """CreateBackupDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: The status of the queried backup process.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateBackupDownloadTaskRequest(AbstractModel):
    """CreateBackupDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of "cmgo-p8vnipr5", which is the same as the instance ID displayed in the TencentDB console
        :type InstanceId: str
        :param BackupName: The name of the backup file to be downloaded, which can be obtained by the `DescribeDBBackups` API
        :type BackupName: str
        :param BackupSets: The list of shards with backups to be downloaded
        :type BackupSets: list of ReplicaSetInfo
        """
        self.InstanceId = None
        self.BackupName = None
        self.BackupSets = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        if params.get("BackupSets") is not None:
            self.BackupSets = []
            for item in params.get("BackupSets"):
                obj = ReplicaSetInfo()
                obj._deserialize(item)
                self.BackupSets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDownloadTaskResponse(AbstractModel):
    """CreateBackupDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param Tasks: Download task status
        :type Tasks: list of BackupDownloadTaskStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = BackupDownloadTaskStatus()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour request structure.

    """

    def __init__(self):
        r"""
        :param Memory: Instance memory size in GB
        :type Memory: int
        :param Volume: Instance disk size in GB
        :type Volume: int
        :param ReplicateSetNum: Number of replica sets. When a replica set instance is created, this parameter must be set to 1. When a sharding instance is created, please see the parameters returned by the DescribeSpecInfo API
        :type ReplicateSetNum: int
        :param NodeNum: The number of nodes in each replica set. The value range is subject to the response parameter of the `DescribeSpecInfo` API.
        :type NodeNum: int
        :param MongoVersion: Version number. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API. The correspondences between parameters and versions are as follows: MONGO_3_WT: MongoDB 3.2 WiredTiger Edition; MONGO_3_ROCKS: MongoDB 3.2 RocksDB Edition; MONGO_36_WT: MongoDB 3.6 WiredTiger Edition; MONGO_40_WT: MongoDB 4.0 WiredTiger Edition; MONGO_42_WT: MongoDB 4.2 WiredTiger Edition.
        :type MongoVersion: str
        :param MachineCode: Server type. HIO: high IO; HIO10G: 10-Gigabit high IO
        :type MachineCode: str
        :param GoodsNum: Number of instances. Minimum value: 1. Maximum value: 10
        :type GoodsNum: int
        :param Zone: AZ in the format of ap-guangzhou-2. If multi-AZ deployment is enabled, this parameter refers to the primary AZ and must be one of the values of `AvailabilityZoneList`.
        :type Zone: str
        :param ClusterType: Instance type. REPLSET: replica set; SHARD: sharding cluster
        :type ClusterType: str
        :param VpcId: VPC ID. If this parameter is not set, the basic network will be selected by default
        :type VpcId: str
        :param SubnetId: VPC subnet ID. If VpcId is set, then SubnetId will be required
        :type SubnetId: str
        :param Password: Instance password, which must contain 8 to 16 characters and comprise at least two of the following types: letters, digits, and symbols (!@#%^*()). If it is left empty, the password is in the format of "instance ID+@+root account UIN". For example, if the instance ID is "cmgo-higv73ed" and the root account UIN "100000001", the instance password will be "cmgo-higv73ed@100000001".
        :type Password: str
        :param ProjectId: Project ID. If this parameter is not set, the default project will be used
        :type ProjectId: int
        :param Tags: Instance tag information
        :type Tags: list of TagInfo
        :param Clone: Instance type. Valid values: `1` (primary instance), `2` (temp instance), `3` (read-only instance), `4` (disaster recovery instance), `5` (cloned instance).
        :type Clone: int
        :param Father: Parent instance ID. It is required if the `Clone` is 3 or 4.
        :type Father: str
        :param SecurityGroup: Security group.
        :type SecurityGroup: list of str
        :param RestoreTime: The point in time to which the cloned instance will be rolled back. This parameter is required for a cloned instance. The point in time in the format of 2021-08-13 16:30:00 must be within the last seven days.
        :type RestoreTime: str
        :param InstanceName: Instance name, which can contain up to 60 letters, digits, or symbols (_-).
        :type InstanceName: str
        :param AvailabilityZoneList: AZ list when multi-AZ deployment is enabled. For the specific purchasable versions which support multi-AZ deployment, please see the return result of the `DescribeSpecInfo` API. Notes: 1. Nodes of a multi-AZ instance must be deployed across three AZs. 2. To ensure a successful cross-AZ switch, you should not deploy most of the nodes to the same AZ. (For example, a three-node sharded cluster instance does not support deploying two or more nodes in the same AZ.) 3. MongoDB 4.2 and later versions do not support multi-AZ deployment. 4. Read-Only and disaster recovery instances do not support multi-AZ deployment. 5. Instances in the classic network do not support multi-AZ deployment.
        :type AvailabilityZoneList: list of str
        :param MongosCpu: The number of mongos CPUs, which is required for a sharded cluster instance of MongoDB 4.2 WiredTiger. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API.
        :type MongosCpu: int
        :param MongosMemory: The size of mongos memory, which is required for a sharded cluster instance of MongoDB 4.2 WiredTiger. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API.
        :type MongosMemory: int
        :param MongosNodeNum: The number of mongos routers, which is required for a sharded cluster instance of MongoDB 4.2 WiredTiger. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API. Note: please purchase 3-32 mongos routers for high availability.
        :type MongosNodeNum: int
        """
        self.Memory = None
        self.Volume = None
        self.ReplicateSetNum = None
        self.NodeNum = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Zone = None
        self.ClusterType = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.ProjectId = None
        self.Tags = None
        self.Clone = None
        self.Father = None
        self.SecurityGroup = None
        self.RestoreTime = None
        self.InstanceName = None
        self.AvailabilityZoneList = None
        self.MongosCpu = None
        self.MongosMemory = None
        self.MongosNodeNum = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.NodeNum = params.get("NodeNum")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Clone = params.get("Clone")
        self.Father = params.get("Father")
        self.SecurityGroup = params.get("SecurityGroup")
        self.RestoreTime = params.get("RestoreTime")
        self.InstanceName = params.get("InstanceName")
        self.AvailabilityZoneList = params.get("AvailabilityZoneList")
        self.MongosCpu = params.get("MongosCpu")
        self.MongosMemory = params.get("MongosMemory")
        self.MongosNodeNum = params.get("MongosNodeNum")
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
        :param DealId: Order ID
        :type DealId: str
        :param InstanceIds: List of IDs of created instances
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


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param NodeNum: The number of nodes in each replica set. The value range is subject to the response parameter of the `DescribeSpecInfo` API.
        :type NodeNum: int
        :param Memory: Instance memory size in GB.
        :type Memory: int
        :param Volume: Instance disk size in GB.
        :type Volume: int
        :param MongoVersion: Version number. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API. The correspondences between parameters and versions are as follows: MONGO_3_WT: MongoDB 3.2 WiredTiger Edition; MONGO_3_ROCKS: MongoDB 3.2 RocksDB Edition; MONGO_36_WT: MongoDB 3.6 WiredTiger Edition; MONGO_40_WT: MongoDB 4.0 WiredTiger Edition; MONGO_42_WT: MongoDB 4.2 WiredTiger Edition.
        :type MongoVersion: str
        :param GoodsNum: Number of instances. Minimum value: 1. Maximum value: 10.
        :type GoodsNum: int
        :param Zone: AZ in the format of ap-guangzhou-2. If multi-AZ deployment is enabled, this parameter refers to the primary AZ and must be one of the values of `AvailabilityZoneList`.
        :type Zone: str
        :param Period: Instance validity period in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param MachineCode: Server type. Valid values: HIO (high IO), HIO10G (10-gigabit high IO), STDS5 (standard).
        :type MachineCode: str
        :param ClusterType: Instance type. Valid values: REPLSET (replica set), SHARD (sharded cluster), STANDALONE (single-node).
        :type ClusterType: str
        :param ReplicateSetNum: Number of replica sets. To create a replica set instance, set this parameter to 1; to create a shard instance, see the parameters returned by the `DescribeSpecInfo` API; to create a single-node instance, set this parameter to 0.
        :type ReplicateSetNum: int
        :param ProjectId: Project ID. If this parameter is not set, the default project will be used.
        :type ProjectId: int
        :param VpcId: VPC ID. If this parameter is not set, the classic network will be used. Please use the `DescribeVpcs` API to query the VPC list.
        :type VpcId: str
        :param SubnetId: VPC subnet ID. If `UniqVpcId` is set, then `UniqSubnetId` will be required. Please use the `DescribeSubnets` API to query the subnet list.
        :type SubnetId: str
        :param Password: Instance password, which must contain 8 to 16 characters and comprise at least two of the following types: letters, digits, and symbols (!@#%^*()). If it is left empty, the password is in the format of "instance ID+@+root account UIN". For example, if the instance ID is "cmgo-higv73ed" and the root account UIN "100000001", the instance password will be "cmgo-higv73ed@100000001".
        :type Password: str
        :param Tags: Instance tag information.
        :type Tags: list of TagInfo
        :param AutoRenewFlag: Auto-renewal flag. Valid values: 0 (auto-renewal not enabled), 1 (auto-renewal enabled). Default value: 0.
        :type AutoRenewFlag: int
        :param AutoVoucher: Whether to automatically use a voucher. Valid values: 1 (yes), 0 (no). Default value: 0.
        :type AutoVoucher: int
        :param Clone: Instance type. Valid values: `1` (primary instance), `2` (temp instance), `3` (read-only instance), `4` (disaster recovery instance), `5` (cloned instance).
        :type Clone: int
        :param Father: Primary instance ID. It is required for read-only, disaster recovery, and cloned instances.
        :type Father: str
        :param SecurityGroup: Security group.
        :type SecurityGroup: list of str
        :param RestoreTime: The point in time to which the cloned instance will be rolled back. This parameter is required for a cloned instance. The point in time in the format of 2021-08-13 16:30:00 must be within the last seven days.
        :type RestoreTime: str
        :param InstanceName: Instance name, which can contain up to 60 letters, digits, or symbols (_-).
        :type InstanceName: str
        :param AvailabilityZoneList: AZ list when multi-AZ deployment is enabled. For the specific purchasable versions which support multi-AZ deployment, please see the return result of the `DescribeSpecInfo` API. Notes: 1. Nodes of a multi-AZ instance must be deployed across three AZs. 2. To ensure a successful cross-AZ switch, you should not deploy most of the nodes to the same AZ. (For example, a three-node sharded cluster instance does not support deploying two or more nodes in the same AZ.) 3. MongoDB 4.2 and later versions do not support multi-AZ deployment. 4. Read-Only and disaster recovery instances do not support multi-AZ deployment. 5. Instances in the classic network do not support multi-AZ deployment.
        :type AvailabilityZoneList: list of str
        :param MongosCpu: The number of mongos CPUs, which is required for a sharded cluster instance of MongoDB 4.2 WiredTiger. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API.
        :type MongosCpu: int
        :param MongosMemory: The size of mongos memory, which is required for a sharded cluster instance of MongoDB 4.2 WiredTiger. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API.
        :type MongosMemory: int
        :param MongosNodeNum: The number of mongos routers, which is required for a sharded cluster instance of MongoDB 4.2 WiredTiger. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API. Note: please purchase 3-32 mongos routers for high availability.
        :type MongosNodeNum: int
        """
        self.NodeNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.GoodsNum = None
        self.Zone = None
        self.Period = None
        self.MachineCode = None
        self.ClusterType = None
        self.ReplicateSetNum = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.Tags = None
        self.AutoRenewFlag = None
        self.AutoVoucher = None
        self.Clone = None
        self.Father = None
        self.SecurityGroup = None
        self.RestoreTime = None
        self.InstanceName = None
        self.AvailabilityZoneList = None
        self.MongosCpu = None
        self.MongosMemory = None
        self.MongosNodeNum = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.Period = params.get("Period")
        self.MachineCode = params.get("MachineCode")
        self.ClusterType = params.get("ClusterType")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.AutoVoucher = params.get("AutoVoucher")
        self.Clone = params.get("Clone")
        self.Father = params.get("Father")
        self.SecurityGroup = params.get("SecurityGroup")
        self.RestoreTime = params.get("RestoreTime")
        self.InstanceName = params.get("InstanceName")
        self.AvailabilityZoneList = params.get("AvailabilityZoneList")
        self.MongosCpu = params.get("MongosCpu")
        self.MongosMemory = params.get("MongosMemory")
        self.MongosNodeNum = params.get("MongosNodeNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param DealId: Order ID.
        :type DealId: str
        :param InstanceIds: List of IDs of created instances.
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


class DBInstanceInfo(AbstractModel):
    """Instance information

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Region: Region information
        :type Region: str
        """
        self.InstanceId = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstancePrice(AbstractModel):
    """Instance price

    """

    def __init__(self):
        r"""
        :param UnitPrice: Unit price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param OriginalPrice: Original price.
        :type OriginalPrice: float
        :param DiscountPrice: Discounted price.
        :type DiscountPrice: float
        """
        self.UnitPrice = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task ID, which is returned by APIs related to async tasks, such as `CreateBackupDBInstance`.
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
        :param Status: Status. Valid values: `initial` (initializing), `running`, `paused` (paused due to failure), `undoed` (rolled back due to failure), `failed` (ended due to failure), `success`
        :type Status: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeBackupAccessRequest(AbstractModel):
    """DescribeBackupAccess request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param BackupName: Name of the backup file for which to get the download permission
        :type BackupName: str
        """
        self.InstanceId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupAccessResponse(AbstractModel):
    """DescribeBackupAccess response structure.

    """

    def __init__(self):
        r"""
        :param Region: Instance region
        :type Region: str
        :param Bucket: The bucket where a backup file is located
        :type Bucket: str
        :param Files: Storage information of a backup file
        :type Files: list of BackupFile
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Region = None
        self.Bucket = None
        self.Files = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = BackupFile()
                obj._deserialize(item)
                self.Files.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupDownloadTaskRequest(AbstractModel):
    """DescribeBackupDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of "cmgo-p8vnipr5", which is the same as the instance ID displayed in the TencentDB console
        :type InstanceId: str
        :param BackupName: The name of a backup file with download tasks to be queried
        :type BackupName: str
        :param StartTime: The start time of the query period. Tasks whose start time and end time fall within the query period will be queried. If it is left empty, the start time can be any time earlier than the end time.
        :type StartTime: str
        :param EndTime: The end time of the query period. Tasks whose start time and end time fall within the query period will be queried. If it is left empty, the end time can be any time later than the start time.
        :type EndTime: str
        :param Limit: The maximum number of results returned per page. Value range: 1-100. Default value: `20`.
        :type Limit: int
        :param Offset: Offset for pagination. Default value: `0`.
        :type Offset: int
        :param OrderBy: The field used to sort the results. Valid values: `createTime` (default), `finishTime`.
        :type OrderBy: str
        :param OrderByType: Sort order. Valid values: `asc`, `desc` (default).
        :type OrderByType: str
        :param Status: The status of the tasks to be queried. Valid values: `0` (waiting for execution), `1` (downloading), `2` (downloaded), `3` (download failed), `4` (waiting for retry). If it is left empty, tasks in any status will be returned.
        :type Status: list of int
        """
        self.InstanceId = None
        self.BackupName = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadTaskResponse(AbstractModel):
    """DescribeBackupDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param Tasks: The list of download tasks
        :type Tasks: list of BackupDownloadTask
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
                obj = BackupDownloadTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClientConnectionsRequest(AbstractModel):
    """DescribeClientConnections request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param Limit: The number of records that will be returned. Default value: 10,000.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientConnectionsResponse(AbstractModel):
    """DescribeClientConnections response structure.

    """

    def __init__(self):
        r"""
        :param Clients: Client connection information, including client IP and number of connections
        :type Clients: list of ClientConnection
        :param TotalCount: The total number of records that meet the query condition, which can be used for paginated queries.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Clients = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Clients") is not None:
            self.Clients = []
            for item in params.get("Clients"):
                obj = ClientConnection()
                obj._deserialize(item)
                self.Clients.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param BackupMethod: Backup mode. Valid values: `0` (logical backup), `1` (physical backup), `2` (both modes). Default value: `0`.
        :type BackupMethod: int
        :param Limit: Number of entries per page. Maximum value: `100`. If this parameter is left empty, all entries will be returned.
        :type Limit: int
        :param Offset: Pagination offset, starting from `0`. Default value: `0`.
        :type Offset: int
        """
        self.InstanceId = None
        self.BackupMethod = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMethod = params.get("BackupMethod")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBBackupsResponse(AbstractModel):
    """DescribeDBBackups response structure.

    """

    def __init__(self):
        r"""
        :param BackupList: Backup list
        :type BackupList: list of BackupInfo
        :param TotalCount: Total number of backups
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BackupList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = BackupInfo()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceDealRequest(AbstractModel):
    """DescribeDBInstanceDeal request structure.

    """

    def __init__(self):
        r"""
        :param DealId: Order ID. It is returned by the `CreateDBInstance` and other APIs.
        :type DealId: str
        """
        self.DealId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceDealResponse(AbstractModel):
    """DescribeDBInstanceDeal response structure.

    """

    def __init__(self):
        r"""
        :param Status: Order status. Valid values: 1 (unpaid), 2 (paid), 3 (delivering), 4 (delivered), 5 (delivery failed), 6 (refunded), 7 (order closed), 8 (order closed because it failed to be paid within timeout period).
        :type Status: int
        :param OriginalPrice: Original price of the order.
        :type OriginalPrice: float
        :param DiscountPrice: Discounted price of the order.
        :type DiscountPrice: float
        :param Action: Operation performed by the order. Valid values: purchase, renew, upgrade, downgrade, refund.
        :type Action: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.Action = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.Action = params.get("Action")
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: List of instance IDs in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceIds: list of str
        :param InstanceType: Instance type. Valid values: 0 (all instances), 1 (promoted), 2 (temp), 3 (read-only), -1 (promoted + read-only + disaster recovery)
        :type InstanceType: int
        :param ClusterType: Cluster type. Valid values: 0 (replica set instance), 1 (sharding instance), -1 (all instances)
        :type ClusterType: int
        :param Status: Instance status. Valid values: `0` (to be initialized), `1` (executing task), `2` (running), `-2` (isolated monthly-subscribed instance), `-3` (isolated pay-as-you-go instance)
        :type Status: list of int
        :param VpcId: VPC ID. This parameter can be left empty for the basic network
        :type VpcId: str
        :param SubnetId: Subnet ID of VPC. This parameter can be left empty for the basic network. If it is passed in as an input parameter, the corresponding VpcId must be set
        :type SubnetId: str
        :param PayMode: Billing type. Valid value: 0 (pay-as-you-go)
        :type PayMode: int
        :param Limit: Number of results to be returned for a single request. Valid values: 1-100. Default value: 20
        :type Limit: int
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param OrderBy: Sort by field of the returned result set. Currently, supported values include "ProjectId", "InstanceName", and "CreateTime". The return results are sorted in ascending order by default.
        :type OrderBy: str
        :param OrderByType: Sorting method of the return result set. Currently, "ASC" or "DESC" is supported
        :type OrderByType: str
        :param ProjectIds: Project ID
        :type ProjectIds: list of int non-negative
        :param SearchKey: Search keyword, which can be instance ID, instance name, or complete IP
        :type SearchKey: str
        :param Tags: Tag information
        :type Tags: :class:`tencentcloud.mongodb.v20190725.models.TagInfo`
        """
        self.InstanceIds = None
        self.InstanceType = None
        self.ClusterType = None
        self.Status = None
        self.VpcId = None
        self.SubnetId = None
        self.PayMode = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.ProjectIds = None
        self.SearchKey = None
        self.Tags = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        self.ClusterType = params.get("ClusterType")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PayMode = params.get("PayMode")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKey = params.get("SearchKey")
        if params.get("Tags") is not None:
            self.Tags = TagInfo()
            self.Tags._deserialize(params.get("Tags"))
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
        :param InstanceDetails: List of instance details
        :type InstanceDetails: list of InstanceDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self.InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self.InstanceDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of "cmgo-p8vnipr5"
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
        


class DescribeSecurityGroupResponse(AbstractModel):
    """DescribeSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param Groups: Security groups associated with the instance
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


class DescribeSlowLogPatternsRequest(AbstractModel):
    """DescribeSlowLogPatterns request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of `cmgo-p8vnipr5`, which is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param StartTime: Start time of slow log in the format of `yyyy-mm-dd hh:mm:ss`, such as 2019-06-01 10:00:00. The query time range cannot exceed 24 hours. Only slow logs for the last 7 days can be queried.
        :type StartTime: str
        :param EndTime: End time of slow log in the format of `yyyy-mm-dd hh:mm:ss`, such as 2019-06-02 12:00:00. The query time range cannot exceed 24 hours. Only slow logs for the last 7 days can be queried.
        :type EndTime: str
        :param SlowMS: Threshold of slow log execution time in milliseconds. Minimum value: 100. Slow logs whose execution time exceeds the threshold will be returned.
        :type SlowMS: int
        :param Offset: Offset. Minimum value: 0. Maximum value: 10000. Default value: 0.
        :type Offset: int
        :param Limit: Number of entries per page. Minimum value: 1. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param Format: Slow log format, which can be JSON. If this parameter is left empty, the slow log will be returned in its native format.
        :type Format: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SlowMS = None
        self.Offset = None
        self.Limit = None
        self.Format = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SlowMS = params.get("SlowMS")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogPatternsResponse(AbstractModel):
    """DescribeSlowLogPatterns response structure.

    """

    def __init__(self):
        r"""
        :param Count: Total number of slow logs
        :type Count: int
        :param SlowLogPatterns: Slow log statistics
        :type SlowLogPatterns: list of SlowLogPattern
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.SlowLogPatterns = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("SlowLogPatterns") is not None:
            self.SlowLogPatterns = []
            for item in params.get("SlowLogPatterns"):
                obj = SlowLogPattern()
                obj._deserialize(item)
                self.SlowLogPatterns.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of `cmgo-p8vnipr5`, which is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param StartTime: Start time of slow log in the format of `yyyy-mm-dd hh:mm:ss`, such as 2019-06-01 10:00:00. The query time range cannot exceed 24 hours. Only slow logs for the last 7 days can be queried.
        :type StartTime: str
        :param EndTime: End time of slow log in the format of `yyyy-mm-dd hh:mm:ss`, such as 2019-06-02 12:00:00. The query time range cannot exceed 24 hours. Only slow logs for the last 7 days can be queried.
        :type EndTime: str
        :param SlowMS: Threshold of slow log execution time in milliseconds. Minimum value: 100. Slow logs whose execution time exceeds the threshold will be returned.
        :type SlowMS: int
        :param Offset: Offset. Minimum value: 0. Maximum value: 10000. Default value: 0.
        :type Offset: int
        :param Limit: Number of entries per page. Minimum value: 1. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param Format: Slow log format, which can be JSON. If this parameter is left empty, the slow log will be returned in its native format.
        :type Format: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SlowMS = None
        self.Offset = None
        self.Limit = None
        self.Format = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SlowMS = params.get("SlowMS")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Format = params.get("Format")
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
        :param Count: Total number of slow logs
        :type Count: int
        :param SlowLogs: Slow log details
        :type SlowLogs: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.SlowLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.SlowLogs = params.get("SlowLogs")
        self.RequestId = params.get("RequestId")


class DescribeSpecInfoRequest(AbstractModel):
    """DescribeSpecInfo request structure.

    """

    def __init__(self):
        r"""
        :param Zone: AZ to be queried
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecInfoResponse(AbstractModel):
    """DescribeSpecInfo response structure.

    """

    def __init__(self):
        r"""
        :param SpecInfoList: List of purchasable instance specifications
        :type SpecInfoList: list of SpecificationInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecificationInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class FlushInstanceRouterConfigRequest(AbstractModel):
    """FlushInstanceRouterConfig request structure.

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
        


class FlushInstanceRouterConfigResponse(AbstractModel):
    """FlushInstanceRouterConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InquirePriceCreateDBInstancesRequest(AbstractModel):
    """InquirePriceCreateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param Zone: Instance region name in the format of ap-guangzhou-2.
        :type Zone: str
        :param NodeNum: Number of nodes in each replica set. Currently, the number of nodes per replica set is fixed at 3, while the number of secondary nodes per shard is customizable. For more information, please see the parameter returned by the `DescribeSpecInfo` API.
        :type NodeNum: int
        :param Memory: Instance memory size in GB.
        :type Memory: int
        :param Volume: Instance disk size in GB.
        :type Volume: int
        :param MongoVersion: Version number. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API. The correspondences between parameters and versions are as follows: MONGO_3_WT: MongoDB 3.2 WiredTiger Edition; MONGO_3_ROCKS: MongoDB 3.2 RocksDB Edition; MONGO_36_WT: MongoDB 3.6 WiredTiger Edition; MONGO_40_WT: MongoDB 4.0 WiredTiger Edition.
        :type MongoVersion: str
        :param MachineCode: Server type. Valid values: HIO (high IO), HIO10G (10-gigabit high IO), STDS5 (standard).
        :type MachineCode: str
        :param GoodsNum: Number of instances. Minimum value: 1. Maximum value: 10.
        :type GoodsNum: int
        :param Period: Instance validity period in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param ClusterType: Instance type. Valid values: REPLSET (replica set), SHARD (sharded cluster), STANDALONE (single-node).
        :type ClusterType: str
        :param ReplicateSetNum: Number of replica sets. To create a replica set instance, set this parameter to 1; to create a shard instance, see the parameters returned by the `DescribeSpecInfo` API; to create a single-node instance, set this parameter to 0.
        :type ReplicateSetNum: int
        """
        self.Zone = None
        self.NodeNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Period = None
        self.ClusterType = None
        self.ReplicateSetNum = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeNum = params.get("NodeNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.ClusterType = params.get("ClusterType")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateDBInstancesResponse(AbstractModel):
    """InquirePriceCreateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price.
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = DBInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquirePriceModifyDBInstanceSpecRequest(AbstractModel):
    """InquirePriceModifyDBInstanceSpec request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed in the TencentDB Console.
        :type InstanceId: str
        :param Memory: Instance memory size in GB after specification adjustment.
        :type Memory: int
        :param Volume: Instance disk size in GB after specification adjustment.
        :type Volume: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDBInstanceSpecResponse(AbstractModel):
    """InquirePriceModifyDBInstanceSpec response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price.
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = DBInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquirePriceRenewDBInstancesRequest(AbstractModel):
    """InquirePriceRenewDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed in the TencentDB Console. This API supports operations on up to 5 instances at a time.
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: The parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set automatic renewal, and other attributes of the monthly subscription instance.
        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewDBInstancesResponse(AbstractModel):
    """InquirePriceRenewDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price.
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = DBInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """Description on the billing mode of an instance

    """

    def __init__(self):
        r"""
        :param Period: Purchased usage period (in month). Valid values: `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36`. Default value: `1`.
(This parameter is required in `InquirePriceRenewDBInstances` and `RenewDBInstances` APIs.)
        :type Period: int
        :param RenewFlag: Auto-renewal flag. Valid values:
`NOTIFY_AND_AUTO_RENEW`: notify expiration and renew automatically
`NOTIFY_AND_MANUAL_RENEW`: notify expiration but not renew automatically
`DISABLE_NOTIFY_AND_MANUAL_RENEW`: neither notify expiration nor renew automatically

Default value: `NOTIFY_AND_MANUAL_RENEW`. If this parameter is specified as `NOTIFY_AND_AUTO_RENEW`, the instance will be automatically renewed on a monthly basis when the account balance is sufficient.
(This parameter is required in `InquirePriceRenewDBInstances` and `RenewDBInstances` APIs.)
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """Instance details

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param PayMode: Billing type. Valid value: 0 (pay-as-you-go)
        :type PayMode: int
        :param ProjectId: Project ID
        :type ProjectId: int
        :param ClusterType: Cluster type. Valid values: 0 (replica set instance), 1 (sharding instance),
        :type ClusterType: int
        :param Region: Region information
        :type Region: str
        :param Zone: AZ information
        :type Zone: str
        :param NetType: Network type. Valid values: 0 (basic network), 1 (VPC)
        :type NetType: int
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID of VPC
        :type SubnetId: str
        :param Status: Instance status. Valid values: 0 (to be initialized), 1 (in process), 2 (running), -2 (expired)
        :type Status: int
        :param Vip: Instance IP
        :type Vip: str
        :param Vport: Port number
        :type Vport: int
        :param CreateTime: Instance creation time
        :type CreateTime: str
        :param DeadLine: Instance expiration time
        :type DeadLine: str
        :param MongoVersion: Instance version information
        :type MongoVersion: str
        :param Memory: Instance memory size in MB
        :type Memory: int
        :param Volume: Instance disk size in MB
        :type Volume: int
        :param CpuNum: Number of CPU cores of an instance
        :type CpuNum: int
        :param MachineType: Instance machine type
        :type MachineType: str
        :param SecondaryNum: Number of secondary nodes of an instance
        :type SecondaryNum: int
        :param ReplicationSetNum: Number of instance shards
        :type ReplicationSetNum: int
        :param AutoRenewFlag: Instance auto-renewal flag. Valid values: 0 (manual renewal), 1 (auto-renewal), 2 (no renewal upon expiration)
        :type AutoRenewFlag: int
        :param UsedVolume: Used capacity in MB
        :type UsedVolume: int
        :param MaintenanceStart: Start time of the maintenance time window
        :type MaintenanceStart: str
        :param MaintenanceEnd: End time of the maintenance time window
        :type MaintenanceEnd: str
        :param ReplicaSets: Shard information
        :type ReplicaSets: list of ShardInfo
        :param ReadonlyInstances: Information of read-only instances
        :type ReadonlyInstances: list of DBInstanceInfo
        :param StandbyInstances: Information of disaster recovery instances
        :type StandbyInstances: list of DBInstanceInfo
        :param CloneInstances: Information of temp instances
        :type CloneInstances: list of DBInstanceInfo
        :param RelatedInstance: Information of associated instances. For a promoted instance, this field represents information of its temp instance; for a temp instance, this field represents information of its promoted instance; and for a read-only/disaster recovery instance, this field represents information of its primary instance
        :type RelatedInstance: :class:`tencentcloud.mongodb.v20190725.models.DBInstanceInfo`
        :param Tags: Instance tag information set
        :type Tags: list of TagInfo
        :param InstanceVer: Instance version tag
        :type InstanceVer: int
        :param ClusterVer: Instance version tag
        :type ClusterVer: int
        :param Protocol: Protocol information. Valid values: 1 (mongodb), 2 (dynamodb)
        :type Protocol: int
        :param InstanceType: Instance type. Valid values: 1 (promoted instance), 2 (temp instance), 3 (read-only instance), 4 (disaster recovery instance)
        :type InstanceType: int
        :param InstanceStatusDesc: Instance status description
        :type InstanceStatusDesc: str
        :param RealInstanceId: Physical instance ID. For an instance that has been rolled back and replaced, its InstanceId and RealInstanceId are different. The physical instance ID is needed in such scenarios as getting monitoring data from Barad
        :type RealInstanceId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.PayMode = None
        self.ProjectId = None
        self.ClusterType = None
        self.Region = None
        self.Zone = None
        self.NetType = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.DeadLine = None
        self.MongoVersion = None
        self.Memory = None
        self.Volume = None
        self.CpuNum = None
        self.MachineType = None
        self.SecondaryNum = None
        self.ReplicationSetNum = None
        self.AutoRenewFlag = None
        self.UsedVolume = None
        self.MaintenanceStart = None
        self.MaintenanceEnd = None
        self.ReplicaSets = None
        self.ReadonlyInstances = None
        self.StandbyInstances = None
        self.CloneInstances = None
        self.RelatedInstance = None
        self.Tags = None
        self.InstanceVer = None
        self.ClusterVer = None
        self.Protocol = None
        self.InstanceType = None
        self.InstanceStatusDesc = None
        self.RealInstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PayMode = params.get("PayMode")
        self.ProjectId = params.get("ProjectId")
        self.ClusterType = params.get("ClusterType")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.NetType = params.get("NetType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.DeadLine = params.get("DeadLine")
        self.MongoVersion = params.get("MongoVersion")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.CpuNum = params.get("CpuNum")
        self.MachineType = params.get("MachineType")
        self.SecondaryNum = params.get("SecondaryNum")
        self.ReplicationSetNum = params.get("ReplicationSetNum")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.UsedVolume = params.get("UsedVolume")
        self.MaintenanceStart = params.get("MaintenanceStart")
        self.MaintenanceEnd = params.get("MaintenanceEnd")
        if params.get("ReplicaSets") is not None:
            self.ReplicaSets = []
            for item in params.get("ReplicaSets"):
                obj = ShardInfo()
                obj._deserialize(item)
                self.ReplicaSets.append(obj)
        if params.get("ReadonlyInstances") is not None:
            self.ReadonlyInstances = []
            for item in params.get("ReadonlyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.ReadonlyInstances.append(obj)
        if params.get("StandbyInstances") is not None:
            self.StandbyInstances = []
            for item in params.get("StandbyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.StandbyInstances.append(obj)
        if params.get("CloneInstances") is not None:
            self.CloneInstances = []
            for item in params.get("CloneInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.CloneInstances.append(obj)
        if params.get("RelatedInstance") is not None:
            self.RelatedInstance = DBInstanceInfo()
            self.RelatedInstance._deserialize(params.get("RelatedInstance"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceVer = params.get("InstanceVer")
        self.ClusterVer = params.get("ClusterVer")
        self.Protocol = params.get("Protocol")
        self.InstanceType = params.get("InstanceType")
        self.InstanceStatusDesc = params.get("InstanceStatusDesc")
        self.RealInstanceId = params.get("RealInstanceId")
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
        :param InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
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


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param Memory: Memory size after instance configuration change in GB. Memory and disk must be upgraded or degraded simultaneously
        :type Memory: int
        :param Volume: Disk size after instance configuration change in GB. Memory and disk must be upgraded or degraded simultaneously. For degradation, the new disk capacity must be greater than 1.2 times the used disk capacity
        :type Volume: int
        :param OplogSize: Oplog size after instance configuration change in GB, which ranges from 10% to 90% of the disk capacity and is 10% of the disk capacity by default
        :type OplogSize: int
        :param NodeNum: Node quantity after configuration modification. The value range is subject to the response parameter of the `DescribeSpecInfo` API. If this parameter is left empty, the node quantity remains unchanged.
        :type NodeNum: int
        :param ReplicateSetNum: Shard quantity after configuration modification, which can only be increased rather than decreased. The value range is subject to the response parameter of the `DescribeSpecInfo` API. If this parameter is left empty, the shard quantity remains unchanged.
        :type ReplicateSetNum: int
        :param InMaintenance: Switch time. Valid values: `0` (upon modification completion), `1` (during maintenance time). Default value: `0`. If the quantity of nodes or shards is modified, the value will be `0`.
        :type InMaintenance: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None
        self.NodeNum = None
        self.ReplicateSetNum = None
        self.InMaintenance = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")
        self.NodeNum = params.get("NodeNum")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.InMaintenance = params.get("InMaintenance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSpecResponse(AbstractModel):
    """ModifyDBInstanceSpec response structure.

    """

    def __init__(self):
        r"""
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


class OfflineIsolatedDBInstanceRequest(AbstractModel):
    """OfflineIsolatedDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
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
        


class OfflineIsolatedDBInstanceResponse(AbstractModel):
    """OfflineIsolatedDBInstance response structure.

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


class RenameInstanceRequest(AbstractModel):
    """RenameInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param NewName: Instance name
        :type NewName: str
        """
        self.InstanceId = None
        self.NewName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameInstanceResponse(AbstractModel):
    """RenameInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewDBInstancesRequest(AbstractModel):
    """RenewDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: IDs of one or more instances to be operated. The value can be obtained from the `InstanceId` parameter returned by the `DescribeInstances` API. Up to 100 instances can be requested at a time.
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: The parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set automatic renewal, and other attributes of the monthly subscription instance. This parameter is mandatory in monthly subscription.
        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstancesResponse(AbstractModel):
    """RenewDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplicaSetInfo(AbstractModel):
    """Shard information

    """

    def __init__(self):
        r"""
        :param ReplicaSetId: Shard name
        :type ReplicaSetId: str
        """
        self.ReplicaSetId = None


    def _deserialize(self, params):
        self.ReplicaSetId = params.get("ReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDBInstancePasswordRequest(AbstractModel):
    """ResetDBInstancePassword request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param UserName: Instance account name
        :type UserName: str
        :param Password: New password
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDBInstancePasswordResponse(AbstractModel):
    """ResetDBInstancePassword response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async request ID, which is used to query the running status of the process.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """Security group information

    """

    def __init__(self):
        r"""
        :param ProjectId: Project ID
        :type ProjectId: int
        :param CreateTime: Creation time
        :type CreateTime: str
        :param Inbound: Inbound rule
        :type Inbound: list of SecurityGroupBound
        :param Outbound: Outbound rule
        :type Outbound: list of SecurityGroupBound
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
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
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
        


class SecurityGroupBound(AbstractModel):
    """Security group rule

    """

    def __init__(self):
        r"""
        :param Action: Execution rule. Valid values: `ACCEPT`, `DROP`
        :type Action: str
        :param CidrIp: IP range
        :type CidrIp: str
        :param PortRange: Port range
        :type PortRange: str
        :param IpProtocol: Transport layer protocol. Valid values: `tcp`, `udp`, `ALL`
        :type IpProtocol: str
        :param Id: All the addresses that the security group ID represents
        :type Id: str
        :param AddressModule: All the addresses that the address group ID represents
        :type AddressModule: str
        :param ServiceModule: All the protocols and ports that the service group ID represents
        :type ServiceModule: str
        :param Desc: Description
        :type Desc: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Id = None
        self.AddressModule = None
        self.ServiceModule = None
        self.Desc = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Id = params.get("Id")
        self.AddressModule = params.get("AddressModule")
        self.ServiceModule = params.get("ServiceModule")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardInfo(AbstractModel):
    """Details of an instance shard

    """

    def __init__(self):
        r"""
        :param UsedVolume: Used shard capacity
        :type UsedVolume: float
        :param ReplicaSetId: Shard ID
        :type ReplicaSetId: str
        :param ReplicaSetName: Shard name
        :type ReplicaSetName: str
        :param Memory: Shard memory size in MB
        :type Memory: int
        :param Volume: Shard disk size in MB
        :type Volume: int
        :param OplogSize: Shard oplog size in MB
        :type OplogSize: int
        :param SecondaryNum: Number of secondary nodes of a shard
        :type SecondaryNum: int
        :param RealReplicaSetId: Shard physical ID
        :type RealReplicaSetId: str
        """
        self.UsedVolume = None
        self.ReplicaSetId = None
        self.ReplicaSetName = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None
        self.SecondaryNum = None
        self.RealReplicaSetId = None


    def _deserialize(self, params):
        self.UsedVolume = params.get("UsedVolume")
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.ReplicaSetName = params.get("ReplicaSetName")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")
        self.SecondaryNum = params.get("SecondaryNum")
        self.RealReplicaSetId = params.get("RealReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogPattern(AbstractModel):
    """Slow log statistics of MongoDB database

    """

    def __init__(self):
        r"""
        :param Pattern: Slow log pattern
        :type Pattern: str
        :param MaxTime: Maximum execution time
        :type MaxTime: int
        :param AverageTime: Average execution time
        :type AverageTime: int
        :param Total: Number of slow logs in this pattern
        :type Total: int
        """
        self.Pattern = None
        self.MaxTime = None
        self.AverageTime = None
        self.Total = None


    def _deserialize(self, params):
        self.Pattern = params.get("Pattern")
        self.MaxTime = params.get("MaxTime")
        self.AverageTime = params.get("AverageTime")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecItem(AbstractModel):
    """Specifications of purchasable MongoDB instances

    """

    def __init__(self):
        r"""
        :param SpecCode: Specification information identifier
        :type SpecCode: str
        :param Status: Specification purchasable flag. Valid values: 0 (not purchasable), 1 (purchasable)
        :type Status: int
        :param Cpu: Computing resource specification in terms of CPU core
        :type Cpu: int
        :param Memory: Memory size in MB
        :type Memory: int
        :param DefaultStorage: Default disk size in MB
        :type DefaultStorage: int
        :param MaxStorage: Maximum disk size in MB
        :type MaxStorage: int
        :param MinStorage: Minimum disk size in MB
        :type MinStorage: int
        :param Qps: Maximum QPS
        :type Qps: int
        :param Conns: Maximum number of connections
        :type Conns: int
        :param MongoVersionCode: MongoDB version information of an instance
        :type MongoVersionCode: str
        :param MongoVersionValue: MongoDB version number of an instance
        :type MongoVersionValue: int
        :param Version: MongoDB version number of an instance (short)
        :type Version: str
        :param EngineName: Storage engine
        :type EngineName: str
        :param ClusterType: Cluster type. Valid values: 1 (sharding cluster), 0 (replica set cluster)
        :type ClusterType: int
        :param MinNodeNum: Minimum number of secondary nodes in a replica set
        :type MinNodeNum: int
        :param MaxNodeNum: Maximum number of secondary nodes in a replica set
        :type MaxNodeNum: int
        :param MinReplicateSetNum: Minimum number of shards
        :type MinReplicateSetNum: int
        :param MaxReplicateSetNum: Maximum number of shards
        :type MaxReplicateSetNum: int
        :param MinReplicateSetNodeNum: Minimum number of secondary nodes in a shard
        :type MinReplicateSetNodeNum: int
        :param MaxReplicateSetNodeNum: Maximum number of secondary nodes in a shard
        :type MaxReplicateSetNodeNum: int
        :param MachineType: Server type. Valid values: 0 (HIO), 4 (HIO10G)
        :type MachineType: str
        """
        self.SpecCode = None
        self.Status = None
        self.Cpu = None
        self.Memory = None
        self.DefaultStorage = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Conns = None
        self.MongoVersionCode = None
        self.MongoVersionValue = None
        self.Version = None
        self.EngineName = None
        self.ClusterType = None
        self.MinNodeNum = None
        self.MaxNodeNum = None
        self.MinReplicateSetNum = None
        self.MaxReplicateSetNum = None
        self.MinReplicateSetNodeNum = None
        self.MaxReplicateSetNodeNum = None
        self.MachineType = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Status = params.get("Status")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.DefaultStorage = params.get("DefaultStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Conns = params.get("Conns")
        self.MongoVersionCode = params.get("MongoVersionCode")
        self.MongoVersionValue = params.get("MongoVersionValue")
        self.Version = params.get("Version")
        self.EngineName = params.get("EngineName")
        self.ClusterType = params.get("ClusterType")
        self.MinNodeNum = params.get("MinNodeNum")
        self.MaxNodeNum = params.get("MaxNodeNum")
        self.MinReplicateSetNum = params.get("MinReplicateSetNum")
        self.MaxReplicateSetNum = params.get("MaxReplicateSetNum")
        self.MinReplicateSetNodeNum = params.get("MinReplicateSetNodeNum")
        self.MaxReplicateSetNodeNum = params.get("MaxReplicateSetNodeNum")
        self.MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificationInfo(AbstractModel):
    """Instance specification information

    """

    def __init__(self):
        r"""
        :param Region: Region information
        :type Region: str
        :param Zone: AZ information
        :type Zone: str
        :param SpecItems: Purchasable specification information
        :type SpecItems: list of SpecItem
        """
        self.Region = None
        self.Zone = None
        self.SpecItems = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItems") is not None:
            self.SpecItems = []
            for item in params.get("SpecItems"):
                obj = SpecItem()
                obj._deserialize(item)
                self.SpecItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Instance tag information

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
        