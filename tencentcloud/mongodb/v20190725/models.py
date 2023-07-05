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
        :param _InstanceIds: List of instance IDs in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceIds: list of str
        :param _ProjectId: Unique ID of an existing project (instead of a new project).
        :type ProjectId: int
        """
        self._InstanceIds = None
        self._ProjectId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignProjectResponse(AbstractModel):
    """AssignProject response structure.

    """

    def __init__(self):
        r"""
        :param _FlowIds: List of the returned async task IDs
        :type FlowIds: list of int non-negative
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowIds = None
        self._RequestId = None

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowIds = params.get("FlowIds")
        self._RequestId = params.get("RequestId")


class BackupDownloadTask(AbstractModel):
    """Backup download task information

    """

    def __init__(self):
        r"""
        :param _CreateTime: Task creation time
        :type CreateTime: str
        :param _BackupName: Backup name
        :type BackupName: str
        :param _ReplicaSetId: Shard name
        :type ReplicaSetId: str
        :param _BackupSize: Backup size in bytes
        :type BackupSize: int
        :param _Status: Task status. Valid values: `0` (waiting for execution), `1` (downloading), `2` (downloaded), `3` (download failed), `4` (waiting for retry)
        :type Status: int
        :param _Percent: Task progress in percentage
        :type Percent: int
        :param _TimeSpend: Task duration in seconds
        :type TimeSpend: int
        :param _Url: Backup download address
        :type Url: str
        :param _BackupMethod: Backup type of the backup file. Valid values: `0` (logical backup), `1` (physical backup)
        :type BackupMethod: int
        :param _BackupDesc: Backup description you set when starting a backup task
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BackupDesc: str
        """
        self._CreateTime = None
        self._BackupName = None
        self._ReplicaSetId = None
        self._BackupSize = None
        self._Status = None
        self._Percent = None
        self._TimeSpend = None
        self._Url = None
        self._BackupMethod = None
        self._BackupDesc = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def ReplicaSetId(self):
        return self._ReplicaSetId

    @ReplicaSetId.setter
    def ReplicaSetId(self, ReplicaSetId):
        self._ReplicaSetId = ReplicaSetId

    @property
    def BackupSize(self):
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def TimeSpend(self):
        return self._TimeSpend

    @TimeSpend.setter
    def TimeSpend(self, TimeSpend):
        self._TimeSpend = TimeSpend

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupDesc(self):
        return self._BackupDesc

    @BackupDesc.setter
    def BackupDesc(self, BackupDesc):
        self._BackupDesc = BackupDesc


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._BackupName = params.get("BackupName")
        self._ReplicaSetId = params.get("ReplicaSetId")
        self._BackupSize = params.get("BackupSize")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        self._TimeSpend = params.get("TimeSpend")
        self._Url = params.get("Url")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupDesc = params.get("BackupDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadTaskStatus(AbstractModel):
    """The result of the created backup download task

    """

    def __init__(self):
        r"""
        :param _ReplicaSetId: Shard name
        :type ReplicaSetId: str
        :param _Status: Task status. Valid values: `0` (waiting for execution), `1` (downloading), `2` (downloaded), `3` (download failed), `4` (waiting for retry)
        :type Status: int
        """
        self._ReplicaSetId = None
        self._Status = None

    @property
    def ReplicaSetId(self):
        return self._ReplicaSetId

    @ReplicaSetId.setter
    def ReplicaSetId(self, ReplicaSetId):
        self._ReplicaSetId = ReplicaSetId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ReplicaSetId = params.get("ReplicaSetId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInfo(AbstractModel):
    """Backup information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _BackupType: Backup mode. 0: automatic backup; 1: manual backup
        :type BackupType: int
        :param _BackupName: Backup name
        :type BackupName: str
        :param _BackupDesc: Backup remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupDesc: str
        :param _BackupSize: Backup file size in KB
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupSize: int
        :param _StartTime: Backup start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: Backup end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _Status: Backup status. 1: backing up; 2: backed up successful
        :type Status: int
        :param _BackupMethod: Backup method. 0: logical backup; 1: physical backup
        :type BackupMethod: int
        """
        self._InstanceId = None
        self._BackupType = None
        self._BackupName = None
        self._BackupDesc = None
        self._BackupSize = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._BackupMethod = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def BackupDesc(self):
        return self._BackupDesc

    @BackupDesc.setter
    def BackupDesc(self, BackupDesc):
        self._BackupDesc = BackupDesc

    @property
    def BackupSize(self):
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupType = params.get("BackupType")
        self._BackupName = params.get("BackupName")
        self._BackupDesc = params.get("BackupDesc")
        self._BackupSize = params.get("BackupSize")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._BackupMethod = params.get("BackupMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientConnection(AbstractModel):
    """Client connection information, including client IP and number of connections

    """

    def __init__(self):
        r"""
        :param _IP: Client IP of a connection
        :type IP: str
        :param _Count: Number of connections corresponding to a client IP
        :type Count: int
        :param _InternalService: Whether it is the Tencent Cloud IP for automated testing
        :type InternalService: bool
        """
        self._IP = None
        self._Count = None
        self._InternalService = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def InternalService(self):
        return self._InternalService

    @InternalService.setter
    def InternalService(self, InternalService):
        self._InternalService = InternalService


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Count = params.get("Count")
        self._InternalService = params.get("InternalService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDBInstanceRequest(AbstractModel):
    """CreateBackupDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _BackupMethod: Valid values: 0 (logical backup), 1 (physical backup)
        :type BackupMethod: int
        :param _BackupRemark: Backup remarks
        :type BackupRemark: str
        """
        self._InstanceId = None
        self._BackupMethod = None
        self._BackupRemark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupRemark(self):
        return self._BackupRemark

    @BackupRemark.setter
    def BackupRemark(self, BackupRemark):
        self._BackupRemark = BackupRemark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupRemark = params.get("BackupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDBInstanceResponse(AbstractModel):
    """CreateBackupDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: The status of the queried backup process.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateBackupDownloadTaskRequest(AbstractModel):
    """CreateBackupDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of "cmgo-p8vnipr5", which is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _BackupName: The name of the backup file to be downloaded, which can be obtained by the `DescribeDBBackups` API.
        :type BackupName: str
        :param _BackupSets: Specify the node name of a replica set instance or the shard name list of a sharded cluster instance. Only backups of the specified node or shards will be downloaded.
Suppose you have a replica set instance (ID: cmgo-p8vnipr5), you can use the sample code `BackupSets.0=cmgo-p8vnipr5_0` to download the full backup. For a replica set instance, the parameter value must be in the format of "instance ID_0".
Suppose you have a sharded cluster instance (ID: cmgo-p8vnipr5), you can use the sample code `BackupSets.0=cmgo-p8vnipr5_0&BackupSets.1=cmgo-p8vnipr5_1` to download the backup data of shard 0 and shard 1. To download the full backup, please specify all shard names.
        :type BackupSets: list of ReplicaSetInfo
        """
        self._InstanceId = None
        self._BackupName = None
        self._BackupSets = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def BackupSets(self):
        return self._BackupSets

    @BackupSets.setter
    def BackupSets(self, BackupSets):
        self._BackupSets = BackupSets


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        if params.get("BackupSets") is not None:
            self._BackupSets = []
            for item in params.get("BackupSets"):
                obj = ReplicaSetInfo()
                obj._deserialize(item)
                self._BackupSets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDownloadTaskResponse(AbstractModel):
    """CreateBackupDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param _Tasks: Download task status
        :type Tasks: list of BackupDownloadTaskStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = BackupDownloadTaskStatus()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour request structure.

    """

    def __init__(self):
        r"""
        :param _Memory: Instance memory size in GB
        :type Memory: int
        :param _Volume: Instance disk size in GB
        :type Volume: int
        :param _ReplicateSetNum: Number of replica sets
- Number of the replica set instances to be created. Valid value: `1`.
- Number of sharded cluster instances to be created. You can get the specific purchasable specifications through the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API.
        :type ReplicateSetNum: int
        :param _NodeNum: The number of nodes in each replica set. You can get the specific purchasable specifications through the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API.
        :type NodeNum: int
        :param _MongoVersion: Version information. You can get the specific purchasable specifications through the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API.
- MONGO_36_WT：MongoDB 3.6 WiredTiger storage engine
- MONGO_40_WT：MongoDB 4.0 WiredTiger storage engine
- MONGO_42_WT：MongoDB 4.2 WiredTiger storage engine
- MONGO_44_WT：MongoDB 4.4 WiredTiger storage engine
        :type MongoVersion: str
        :param _MachineCode: Machine type
- HIO: High IO
- HIO10G: 10-Gigabit high IO
        :type MachineCode: str
        :param _GoodsNum: Number of instances. Value range: 1-10.
        :type GoodsNum: int
        :param _Zone: AZ information in the format of ap-guangzhou-2
- For more information, query through the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API.
- If multi-AZ deployment is enabled, this parameter refers to the primary AZ and must be one of the values of `AvailabilityZoneList`.
        :type Zone: str
        :param _ClusterType: Instance architecture type
- REPLSET: Replica set
- SHARD: Sharded cluster
        :type ClusterType: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: VPC subnet ID. If `VpcId` is set, then `SubnetId` will be required.
        :type SubnetId: str
        :param _Password: Instance password
- If it is left empty, the password is in the default format of "instance ID+@+root account UIN". For example, if the instance ID is "cmgo-higv73ed" and the root account UIN "100000001", the instance password will be "cmgo-higv73ed@100000001". 
- The custom password must contain 8-32 characters in at least two of the following types: letters, digits, and symbols (!@#%^*()_).
        :type Password: str
        :param _ProjectId: Project ID. If it is left empty, `Default project` will be used.
        :type ProjectId: int
        :param _Tags: Instance tag information
        :type Tags: list of TagInfo
        :param _Clone: Instance type. Valid values:
- `1`: Primary instance
- `3`: Read-only instance
- `4`: Disaster recovery instance
        :type Clone: int
        :param _Father: Parent instance ID. It is required if the `Clone` is `3` or `4`, that is, read-only instance or disaster recovery instance
        :type Father: str
        :param _SecurityGroup: Security group
        :type SecurityGroup: list of str
        :param _RestoreTime: Rollback time of the cloned instance
- This parameter is required for a cloned instance in the format of 2021-08-13 16:30:00.
- Time range for rollback: You can roll back data in the last 7 days.
        :type RestoreTime: str
        :param _InstanceName: Instance name, which can contain up to 60 letters, digits, and symbols (_-).
        :type InstanceName: str
        :param _AvailabilityZoneList: List of multi-AZ deployed nodes. For more information, query through the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API.
- Nodes of a multi-AZ instance must be deployed across three AZs. Most nodes of the cluster can’t be deployed in the same AZ. For example, a three-node sharded cluster instance does not support deploying two or more nodes in the same AZ.
- MongoDB 4.2 and later versions do not support multi-AZ deployment.
- Read-only and disaster recovery instances do not support multi-AZ deployment.
-Instances in the classic network do not support multi-AZ deployment.
        :type AvailabilityZoneList: list of str
        :param _MongosCpu: Number of Mongos CPU cores
- This parameter is not required for a sharded cluster instance of MongoDB 3.6 WiredTiger or later.
- If this parameter is not configured, the mongos specification will be configured based on the mongod specification, and the default specification is free of charge.
        :type MongosCpu: int
        :param _MongosMemory: Mongos memory size
- This parameter is not required for a sharded cluster instance of MongoDB 3.6 WiredTiger or later.
- If this parameter is not configured, the mongos specification will be configured based on the mongod specification, and the default specification is free of charge.
        :type MongosMemory: int
        :param _MongosNodeNum: Number of Monogs
- This parameter is not required for a sharded cluster instance of MongoDB 3.6 WiredTiger or later.
- If this parameter is not configured, the mongos specification will be configured based on the mongod specification, and the default specification is free of charge.
        :type MongosNodeNum: int
        :param _ReadonlyNodeNum: Number of read-only nodes. Value range: 0-5.
        :type ReadonlyNodeNum: int
        :param _ReadonlyNodeAvailabilityZoneList: AZ of read-only nodes, which is required when `ReadonlyNodeNum` is not `0` in cross-AZ instance deployment.
        :type ReadonlyNodeAvailabilityZoneList: list of str
        :param _HiddenZone: AZ where the hidden node resides, which is required in cross-AZ instance deployment.
        :type HiddenZone: str
        """
        self._Memory = None
        self._Volume = None
        self._ReplicateSetNum = None
        self._NodeNum = None
        self._MongoVersion = None
        self._MachineCode = None
        self._GoodsNum = None
        self._Zone = None
        self._ClusterType = None
        self._VpcId = None
        self._SubnetId = None
        self._Password = None
        self._ProjectId = None
        self._Tags = None
        self._Clone = None
        self._Father = None
        self._SecurityGroup = None
        self._RestoreTime = None
        self._InstanceName = None
        self._AvailabilityZoneList = None
        self._MongosCpu = None
        self._MongosMemory = None
        self._MongosNodeNum = None
        self._ReadonlyNodeNum = None
        self._ReadonlyNodeAvailabilityZoneList = None
        self._HiddenZone = None

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def ReplicateSetNum(self):
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum

    @property
    def NodeNum(self):
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def MongoVersion(self):
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def MachineCode(self):
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Clone(self):
        return self._Clone

    @Clone.setter
    def Clone(self, Clone):
        self._Clone = Clone

    @property
    def Father(self):
        return self._Father

    @Father.setter
    def Father(self, Father):
        self._Father = Father

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RestoreTime(self):
        return self._RestoreTime

    @RestoreTime.setter
    def RestoreTime(self, RestoreTime):
        self._RestoreTime = RestoreTime

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AvailabilityZoneList(self):
        return self._AvailabilityZoneList

    @AvailabilityZoneList.setter
    def AvailabilityZoneList(self, AvailabilityZoneList):
        self._AvailabilityZoneList = AvailabilityZoneList

    @property
    def MongosCpu(self):
        return self._MongosCpu

    @MongosCpu.setter
    def MongosCpu(self, MongosCpu):
        self._MongosCpu = MongosCpu

    @property
    def MongosMemory(self):
        return self._MongosMemory

    @MongosMemory.setter
    def MongosMemory(self, MongosMemory):
        self._MongosMemory = MongosMemory

    @property
    def MongosNodeNum(self):
        return self._MongosNodeNum

    @MongosNodeNum.setter
    def MongosNodeNum(self, MongosNodeNum):
        self._MongosNodeNum = MongosNodeNum

    @property
    def ReadonlyNodeNum(self):
        return self._ReadonlyNodeNum

    @ReadonlyNodeNum.setter
    def ReadonlyNodeNum(self, ReadonlyNodeNum):
        self._ReadonlyNodeNum = ReadonlyNodeNum

    @property
    def ReadonlyNodeAvailabilityZoneList(self):
        return self._ReadonlyNodeAvailabilityZoneList

    @ReadonlyNodeAvailabilityZoneList.setter
    def ReadonlyNodeAvailabilityZoneList(self, ReadonlyNodeAvailabilityZoneList):
        self._ReadonlyNodeAvailabilityZoneList = ReadonlyNodeAvailabilityZoneList

    @property
    def HiddenZone(self):
        return self._HiddenZone

    @HiddenZone.setter
    def HiddenZone(self, HiddenZone):
        self._HiddenZone = HiddenZone


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        self._NodeNum = params.get("NodeNum")
        self._MongoVersion = params.get("MongoVersion")
        self._MachineCode = params.get("MachineCode")
        self._GoodsNum = params.get("GoodsNum")
        self._Zone = params.get("Zone")
        self._ClusterType = params.get("ClusterType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Password = params.get("Password")
        self._ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Clone = params.get("Clone")
        self._Father = params.get("Father")
        self._SecurityGroup = params.get("SecurityGroup")
        self._RestoreTime = params.get("RestoreTime")
        self._InstanceName = params.get("InstanceName")
        self._AvailabilityZoneList = params.get("AvailabilityZoneList")
        self._MongosCpu = params.get("MongosCpu")
        self._MongosMemory = params.get("MongosMemory")
        self._MongosNodeNum = params.get("MongosNodeNum")
        self._ReadonlyNodeNum = params.get("ReadonlyNodeNum")
        self._ReadonlyNodeAvailabilityZoneList = params.get("ReadonlyNodeAvailabilityZoneList")
        self._HiddenZone = params.get("HiddenZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID
        :type DealId: str
        :param _InstanceIds: List of IDs of the created instances
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _NodeNum: The number of nodes in each replica set. The value range is subject to the response parameter of the `DescribeSpecInfo` API.
        :type NodeNum: int
        :param _Memory: Instance memory size in GB.
        :type Memory: int
        :param _Volume: Instance disk size in GB.
        :type Volume: int
        :param _MongoVersion: Version number. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API. The correspondences between parameters and versions are as follows: MONGO_3_WT: MongoDB 3.2 WiredTiger Edition; MONGO_3_ROCKS: MongoDB 3.2 RocksDB Edition; MONGO_36_WT: MongoDB 3.6 WiredTiger Edition; MONGO_40_WT: MongoDB 4.0 WiredTiger Edition; MONGO_42_WT: MongoDB 4.2 WiredTiger Edition.
        :type MongoVersion: str
        :param _GoodsNum: Number of instances. Minimum value: 1. Maximum value: 10.
        :type GoodsNum: int
        :param _Zone: AZ in the format of ap-guangzhou-2. If multi-AZ deployment is enabled, this parameter refers to the primary AZ and must be one of the values of `AvailabilityZoneList`.
        :type Zone: str
        :param _Period: Instance validity period in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param _MachineCode: Server type. Valid values: HIO (high IO), HIO10G (10-gigabit high IO), STDS5 (standard).
        :type MachineCode: str
        :param _ClusterType: Instance type. Valid values: REPLSET (replica set), SHARD (sharded cluster), STANDALONE (single-node).
        :type ClusterType: str
        :param _ReplicateSetNum: Number of replica sets. To create a replica set instance, set this parameter to 1; to create a shard instance, see the parameters returned by the `DescribeSpecInfo` API; to create a single-node instance, set this parameter to 0.
        :type ReplicateSetNum: int
        :param _ProjectId: Project ID. If this parameter is not set, the default project will be used.
        :type ProjectId: int
        :param _VpcId: VPC ID. If this parameter is not set, the classic network will be used. Please use the `DescribeVpcs` API to query the VPC list.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID. If `UniqVpcId` is set, then `UniqSubnetId` will be required. Please use the `DescribeSubnets` API to query the subnet list.
        :type SubnetId: str
        :param _Password: Instance password. If it is left empty, the password is in the default format of "instance ID+@+root account UIN". For example, if the instance ID is "cmgo-higv73ed" and the root account UIN "100000001", the instance password will be "cmgo-higv73ed@100000001". The custom password must contain 8-32 characters in at least two of the following types: letters, digits, and symbols (!@#%^*()_).
        :type Password: str
        :param _Tags: Instance tag information.
        :type Tags: list of TagInfo
        :param _AutoRenewFlag: Auto-renewal flag. Valid values: 0 (auto-renewal not enabled), 1 (auto-renewal enabled). Default value: 0.
        :type AutoRenewFlag: int
        :param _AutoVoucher: Whether to automatically use a voucher. Valid values: 1 (yes), 0 (no). Default value: 0.
        :type AutoVoucher: int
        :param _Clone: Instance type. Valid values: `1` (primary instance), `2` (temp instance), `3` (read-only instance), `4` (disaster recovery instance), `5` (cloned instance).
        :type Clone: int
        :param _Father: Primary instance ID. It is required for read-only, disaster recovery, and cloned instances.
        :type Father: str
        :param _SecurityGroup: Security group.
        :type SecurityGroup: list of str
        :param _RestoreTime: The point in time to which the cloned instance will be rolled back. This parameter is required for a cloned instance. The point in time in the format of 2021-08-13 16:30:00 must be within the last seven days.
        :type RestoreTime: str
        :param _InstanceName: Instance name, which can contain up to 60 letters, digits, or symbols (_-).
        :type InstanceName: str
        :param _AvailabilityZoneList: AZ list when multi-AZ deployment is enabled. For the specific purchasable versions which support multi-AZ deployment, please see the return result of the `DescribeSpecInfo` API. Notes: 1. Nodes of a multi-AZ instance must be deployed across three AZs. 2. To ensure a successful cross-AZ switch, you should not deploy most of the nodes to the same AZ. (For example, a three-node sharded cluster instance does not support deploying two or more nodes in the same AZ.) 3. MongoDB 4.2 and later versions do not support multi-AZ deployment. 4. Read-Only and disaster recovery instances do not support multi-AZ deployment. 5. Instances in the classic network do not support multi-AZ deployment.
        :type AvailabilityZoneList: list of str
        :param _MongosCpu: The number of mongos CPUs, which is required for a sharded cluster instance of MongoDB 4.2 WiredTiger. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API.
        :type MongosCpu: int
        :param _MongosMemory: The size of mongos memory, which is required for a sharded cluster instance of MongoDB 4.2 WiredTiger. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API.
        :type MongosMemory: int
        :param _MongosNodeNum: The number of mongos routers, which is required for a sharded cluster instance of MongoDB 4.2 WiredTiger. For the specific purchasable versions supported, please see the return result of the `DescribeSpecInfo` API. Note: please purchase 3-32 mongos routers for high availability.
        :type MongosNodeNum: int
        :param _ReadonlyNodeNum: Number of read-only nodes. Value range: 2-7.
        :type ReadonlyNodeNum: int
        :param _ReadonlyNodeAvailabilityZoneList: The AZ where the read-only node is deployed
        :type ReadonlyNodeAvailabilityZoneList: list of str
        :param _HiddenZone: The AZ where the hidden node resides. It is required for cross-AZ instances.
        :type HiddenZone: str
        """
        self._NodeNum = None
        self._Memory = None
        self._Volume = None
        self._MongoVersion = None
        self._GoodsNum = None
        self._Zone = None
        self._Period = None
        self._MachineCode = None
        self._ClusterType = None
        self._ReplicateSetNum = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._Password = None
        self._Tags = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None
        self._Clone = None
        self._Father = None
        self._SecurityGroup = None
        self._RestoreTime = None
        self._InstanceName = None
        self._AvailabilityZoneList = None
        self._MongosCpu = None
        self._MongosMemory = None
        self._MongosNodeNum = None
        self._ReadonlyNodeNum = None
        self._ReadonlyNodeAvailabilityZoneList = None
        self._HiddenZone = None

    @property
    def NodeNum(self):
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def MongoVersion(self):
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def MachineCode(self):
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ReplicateSetNum(self):
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def Clone(self):
        return self._Clone

    @Clone.setter
    def Clone(self, Clone):
        self._Clone = Clone

    @property
    def Father(self):
        return self._Father

    @Father.setter
    def Father(self, Father):
        self._Father = Father

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RestoreTime(self):
        return self._RestoreTime

    @RestoreTime.setter
    def RestoreTime(self, RestoreTime):
        self._RestoreTime = RestoreTime

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AvailabilityZoneList(self):
        return self._AvailabilityZoneList

    @AvailabilityZoneList.setter
    def AvailabilityZoneList(self, AvailabilityZoneList):
        self._AvailabilityZoneList = AvailabilityZoneList

    @property
    def MongosCpu(self):
        return self._MongosCpu

    @MongosCpu.setter
    def MongosCpu(self, MongosCpu):
        self._MongosCpu = MongosCpu

    @property
    def MongosMemory(self):
        return self._MongosMemory

    @MongosMemory.setter
    def MongosMemory(self, MongosMemory):
        self._MongosMemory = MongosMemory

    @property
    def MongosNodeNum(self):
        return self._MongosNodeNum

    @MongosNodeNum.setter
    def MongosNodeNum(self, MongosNodeNum):
        self._MongosNodeNum = MongosNodeNum

    @property
    def ReadonlyNodeNum(self):
        return self._ReadonlyNodeNum

    @ReadonlyNodeNum.setter
    def ReadonlyNodeNum(self, ReadonlyNodeNum):
        self._ReadonlyNodeNum = ReadonlyNodeNum

    @property
    def ReadonlyNodeAvailabilityZoneList(self):
        return self._ReadonlyNodeAvailabilityZoneList

    @ReadonlyNodeAvailabilityZoneList.setter
    def ReadonlyNodeAvailabilityZoneList(self, ReadonlyNodeAvailabilityZoneList):
        self._ReadonlyNodeAvailabilityZoneList = ReadonlyNodeAvailabilityZoneList

    @property
    def HiddenZone(self):
        return self._HiddenZone

    @HiddenZone.setter
    def HiddenZone(self, HiddenZone):
        self._HiddenZone = HiddenZone


    def _deserialize(self, params):
        self._NodeNum = params.get("NodeNum")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._MongoVersion = params.get("MongoVersion")
        self._GoodsNum = params.get("GoodsNum")
        self._Zone = params.get("Zone")
        self._Period = params.get("Period")
        self._MachineCode = params.get("MachineCode")
        self._ClusterType = params.get("ClusterType")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Password = params.get("Password")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        self._Clone = params.get("Clone")
        self._Father = params.get("Father")
        self._SecurityGroup = params.get("SecurityGroup")
        self._RestoreTime = params.get("RestoreTime")
        self._InstanceName = params.get("InstanceName")
        self._AvailabilityZoneList = params.get("AvailabilityZoneList")
        self._MongosCpu = params.get("MongosCpu")
        self._MongosMemory = params.get("MongosMemory")
        self._MongosNodeNum = params.get("MongosNodeNum")
        self._ReadonlyNodeNum = params.get("ReadonlyNodeNum")
        self._ReadonlyNodeAvailabilityZoneList = params.get("ReadonlyNodeAvailabilityZoneList")
        self._HiddenZone = params.get("HiddenZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID.
        :type DealId: str
        :param _InstanceIds: List of IDs of created instances.
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class DBInstanceInfo(AbstractModel):
    """Instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Region: Region information
        :type Region: str
        """
        self._InstanceId = None
        self._Region = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstancePrice(AbstractModel):
    """Instance price

    """

    def __init__(self):
        r"""
        :param _UnitPrice: Unit price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param _OriginalPrice: Original price.
        :type OriginalPrice: float
        :param _DiscountPrice: Discounted price.
        :type DiscountPrice: float
        """
        self._UnitPrice = None
        self._OriginalPrice = None
        self._DiscountPrice = None

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID, which is returned by APIs related to async tasks, such as `CreateBackupDBInstance`.
        :type AsyncRequestId: str
        """
        self._AsyncRequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status. Valid values: `initial` (initializing), `running`, `paused` (paused due to failure), `undoed` (rolled back due to failure), `failed` (ended due to failure), `success`
        :type Status: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadTaskRequest(AbstractModel):
    """DescribeBackupDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of "cmgo-p8vnipr5", which is the same as the instance ID displayed in the TencentDB console
        :type InstanceId: str
        :param _BackupName: The name of a backup file with download tasks to be queried
        :type BackupName: str
        :param _StartTime: The start time of the query period. Tasks whose start time and end time fall within the query period will be queried. If it is left empty, the start time can be any time earlier than the end time.
        :type StartTime: str
        :param _EndTime: The end time of the query period. Tasks will be queried if their start and end times fall within the query period. If it is left empty, the end time can be any time later than the start time.
        :type EndTime: str
        :param _Limit: The maximum number of results returned per page. Value range: 1-100. Default value: `20`.
        :type Limit: int
        :param _Offset: Offset for pagination. Default value: `0`.
        :type Offset: int
        :param _OrderBy: The field used to sort the results. Valid values: `createTime` (default), `finishTime`.
        :type OrderBy: str
        :param _OrderByType: Sort order. Valid values: `asc`, `desc` (default).
        :type OrderByType: str
        :param _Status: The status of the tasks to be queried. Valid values: `0` (waiting for execution), `1` (downloading), `2` (downloaded), `3` (download failed), `4` (waiting for retry). If it is left empty, tasks in any status will be returned.
        :type Status: list of int
        """
        self._InstanceId = None
        self._BackupName = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Status = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadTaskResponse(AbstractModel):
    """DescribeBackupDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _Tasks: The list of download tasks
        :type Tasks: list of BackupDownloadTask
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = BackupDownloadTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClientConnectionsRequest(AbstractModel):
    """DescribeClientConnections request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param _Limit: Number of results to be returned for a single request. Value range: 1-1,000. Default value: 1,000
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientConnectionsResponse(AbstractModel):
    """DescribeClientConnections response structure.

    """

    def __init__(self):
        r"""
        :param _Clients: Client connection information, including client IP and number of connections
        :type Clients: list of ClientConnection
        :param _TotalCount: The total number of records that meet the query condition, which can be used for paginated queries.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Clients = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Clients(self):
        return self._Clients

    @Clients.setter
    def Clients(self, Clients):
        self._Clients = Clients

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Clients") is not None:
            self._Clients = []
            for item in params.get("Clients"):
                obj = ClientConnection()
                obj._deserialize(item)
                self._Clients.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param _BackupMethod: Backup mode. Valid values: `0` (logical backup), `1` (physical backup), `2` (both modes). Default value: `0`.
        :type BackupMethod: int
        :param _Limit: Number of entries per page. Maximum value: `100`. If this parameter is left empty, all entries will be returned.
        :type Limit: int
        :param _Offset: Pagination offset, starting from `0`. Default value: `0`.
        :type Offset: int
        """
        self._InstanceId = None
        self._BackupMethod = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMethod = params.get("BackupMethod")
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
    """DescribeDBBackups response structure.

    """

    def __init__(self):
        r"""
        :param _BackupList: Backup list
        :type BackupList: list of BackupInfo
        :param _TotalCount: Total number of backups
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BackupList(self):
        return self._BackupList

    @BackupList.setter
    def BackupList(self, BackupList):
        self._BackupList = BackupList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackupList") is not None:
            self._BackupList = []
            for item in params.get("BackupList"):
                obj = BackupInfo()
                obj._deserialize(item)
                self._BackupList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceDealRequest(AbstractModel):
    """DescribeDBInstanceDeal request structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID. It is returned by the `CreateDBInstance` and other APIs.
        :type DealId: str
        """
        self._DealId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceDealResponse(AbstractModel):
    """DescribeDBInstanceDeal response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Order status. Valid values: 1 (unpaid), 2 (paid), 3 (delivering), 4 (delivered), 5 (delivery failed), 6 (refunded), 7 (order closed), 8 (order closed because it failed to be paid within timeout period).
        :type Status: int
        :param _OriginalPrice: Original price of the order.
        :type OriginalPrice: float
        :param _DiscountPrice: Discounted price of the order.
        :type DiscountPrice: float
        :param _Action: Operation performed by the order. Valid values: purchase, renew, upgrade, downgrade, refund.
        :type Action: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Action = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Action = params.get("Action")
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of instance IDs in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB console page.
        :type InstanceIds: list of str
        :param _InstanceType: Instance type. Valid values: <ul><li>`0`: All instances. </li><li>`1`: Regular instances. </li><li>`2`: Temp instances. </li><li>`3`: Read-only instances. </li><li>`-1`: Regular instances, read-only instances, disaster recovery instances.</li></ul>
        :type InstanceType: int
        :param _ClusterType: Cluster type. Valid values: <ul><li>`0`: Replica set instances. </li><li>`1`: Sharded cluster instances. </li><li>`-1`: All instances.</li></ul>
        :type ClusterType: int
        :param _Status: Instance status. Valid values: <ul><li>`0`: To be initialized. </li><li>`1`: In process. </li><li>`2`: Valid. </li><li>`-2`: Isolated (for monthly subscribed instances). </li><li>`-3`: Isolated (for pay-as-you-go instances).</li></ul>
        :type Status: list of int
        :param _VpcId: VPC ID. This parameter can be left empty for the classic network.
        :type VpcId: str
        :param _SubnetId: Subnet ID of VPC. This parameter can be left empty for the classic network. If it is passed in as an input parameter, the corresponding VpcId must be set.
        :type SubnetId: str
        :param _PayMode: Billing type. Valid value: 0 (pay-as-you-go)
        :type PayMode: int
        :param _Limit: Number of results returned per request. Default value: `20`. Value range: [1,100].
        :type Limit: int
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _OrderBy: Sort by field of the returned result set. Valid values: `ProjectId`, `InstanceName`, `CreateTime`. The return results are sorted in ascending order by default.
        :type OrderBy: str
        :param _OrderByType: Sorting method of the return result set. Valid values: `ASC`, `DESC`.
        :type OrderByType: str
        :param _ProjectIds: Project ID
        :type ProjectIds: list of int non-negative
        :param _SearchKey: Search keyword, which can be instance ID, instance name, or complete IP.
        :type SearchKey: str
        :param _Tags: Tag information
        :type Tags: list of TagInfo
        """
        self._InstanceIds = None
        self._InstanceType = None
        self._ClusterType = None
        self._Status = None
        self._VpcId = None
        self._SubnetId = None
        self._PayMode = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._ProjectIds = None
        self._SearchKey = None
        self._Tags = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceType = params.get("InstanceType")
        self._ClusterType = params.get("ClusterType")
        self._Status = params.get("Status")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PayMode = params.get("PayMode")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._ProjectIds = params.get("ProjectIds")
        self._SearchKey = params.get("SearchKey")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
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
        :param _TotalCount: Number of eligible instances
        :type TotalCount: int
        :param _InstanceDetails: List of instance details
        :type InstanceDetails: list of InstanceDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceDetails(self):
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self._InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self._InstanceDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        :param _InstanceEnumParam: The collection of enum parameters
        :type InstanceEnumParam: list of InstanceEnumParam
        :param _InstanceIntegerParam: The collection of integer parameters
        :type InstanceIntegerParam: list of InstanceIntegerParam
        :param _InstanceTextParam: The collection of text parameters
        :type InstanceTextParam: list of InstanceTextParam
        :param _InstanceMultiParam: The collection of string parameters used to represent time ranges
        :type InstanceMultiParam: list of InstanceMultiParam
        :param _TotalCount: The total number of modifiable parameters of the instance, such as 0
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceEnumParam = None
        self._InstanceIntegerParam = None
        self._InstanceTextParam = None
        self._InstanceMultiParam = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceEnumParam(self):
        return self._InstanceEnumParam

    @InstanceEnumParam.setter
    def InstanceEnumParam(self, InstanceEnumParam):
        self._InstanceEnumParam = InstanceEnumParam

    @property
    def InstanceIntegerParam(self):
        return self._InstanceIntegerParam

    @InstanceIntegerParam.setter
    def InstanceIntegerParam(self, InstanceIntegerParam):
        self._InstanceIntegerParam = InstanceIntegerParam

    @property
    def InstanceTextParam(self):
        return self._InstanceTextParam

    @InstanceTextParam.setter
    def InstanceTextParam(self, InstanceTextParam):
        self._InstanceTextParam = InstanceTextParam

    @property
    def InstanceMultiParam(self):
        return self._InstanceMultiParam

    @InstanceMultiParam.setter
    def InstanceMultiParam(self, InstanceMultiParam):
        self._InstanceMultiParam = InstanceMultiParam

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceEnumParam") is not None:
            self._InstanceEnumParam = []
            for item in params.get("InstanceEnumParam"):
                obj = InstanceEnumParam()
                obj._deserialize(item)
                self._InstanceEnumParam.append(obj)
        if params.get("InstanceIntegerParam") is not None:
            self._InstanceIntegerParam = []
            for item in params.get("InstanceIntegerParam"):
                obj = InstanceIntegerParam()
                obj._deserialize(item)
                self._InstanceIntegerParam.append(obj)
        if params.get("InstanceTextParam") is not None:
            self._InstanceTextParam = []
            for item in params.get("InstanceTextParam"):
                obj = InstanceTextParam()
                obj._deserialize(item)
                self._InstanceTextParam.append(obj)
        if params.get("InstanceMultiParam") is not None:
            self._InstanceMultiParam = []
            for item in params.get("InstanceMultiParam"):
                obj = InstanceMultiParam()
                obj._deserialize(item)
                self._InstanceMultiParam.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of "cmgo-p8vnipr5"
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeSecurityGroupResponse(AbstractModel):
    """DescribeSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security groups associated with the instance
        :type Groups: list of SecurityGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogPatternsRequest(AbstractModel):
    """DescribeSlowLogPatterns request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `cmgo-p8vnipr5`, which is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param _StartTime: Start time of slow log in the format of `yyyy-mm-dd hh:mm:ss`, such as 2019-06-01 10:00:00. The query time range cannot exceed 24 hours. Only slow logs for the last 7 days can be queried.
        :type StartTime: str
        :param _EndTime: End time of slow log in the format of `yyyy-mm-dd hh:mm:ss`, such as 2019-06-02 12:00:00. The query time range cannot exceed 24 hours. Only slow logs for the last 7 days can be queried.
        :type EndTime: str
        :param _SlowMS: Threshold of slow log execution time in milliseconds. Minimum value: 100. Slow logs whose execution time exceeds the threshold will be returned.
        :type SlowMS: int
        :param _Offset: Offset. Minimum value: 0. Maximum value: 10000. Default value: 0.
        :type Offset: int
        :param _Limit: Number of entries per page. Minimum value: 1. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _Format: Slow log format, which can be JSON. If this parameter is left empty, the slow log will be returned in its native format.
        :type Format: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SlowMS = None
        self._Offset = None
        self._Limit = None
        self._Format = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SlowMS(self):
        return self._SlowMS

    @SlowMS.setter
    def SlowMS(self, SlowMS):
        self._SlowMS = SlowMS

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SlowMS = params.get("SlowMS")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogPatternsResponse(AbstractModel):
    """DescribeSlowLogPatterns response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Total number of slow logs
        :type Count: int
        :param _SlowLogPatterns: Slow log statistics
        :type SlowLogPatterns: list of SlowLogPattern
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._SlowLogPatterns = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def SlowLogPatterns(self):
        return self._SlowLogPatterns

    @SlowLogPatterns.setter
    def SlowLogPatterns(self, SlowLogPatterns):
        self._SlowLogPatterns = SlowLogPatterns

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("SlowLogPatterns") is not None:
            self._SlowLogPatterns = []
            for item in params.get("SlowLogPatterns"):
                obj = SlowLogPattern()
                obj._deserialize(item)
                self._SlowLogPatterns.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `cmgo-p8vnipr5`, which is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param _StartTime: Start time of slow log in the format of `yyyy-mm-dd hh:mm:ss`, such as 2019-06-01 10:00:00. The query time range cannot exceed 24 hours. Only slow logs for the last 7 days can be queried.
        :type StartTime: str
        :param _EndTime: End time of slow log in the format of `yyyy-mm-dd hh:mm:ss`, such as 2019-06-02 12:00:00. The query time range cannot exceed 24 hours. Only slow logs for the last 7 days can be queried.
        :type EndTime: str
        :param _SlowMS: Threshold of slow log execution time in milliseconds. Minimum value: 100. Slow logs whose execution time exceeds the threshold will be returned.
        :type SlowMS: int
        :param _Offset: Offset. Minimum value: 0. Maximum value: 10000. Default value: 0.
        :type Offset: int
        :param _Limit: Number of entries per page. Minimum value: 1. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _Format: Return format of slow log. The original slow log format is returned by default, and the format can be set to JSON on versions 4.4 and later.
        :type Format: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SlowMS = None
        self._Offset = None
        self._Limit = None
        self._Format = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SlowMS(self):
        return self._SlowMS

    @SlowMS.setter
    def SlowMS(self, SlowMS):
        self._SlowMS = SlowMS

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SlowMS = params.get("SlowMS")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogsResponse(AbstractModel):
    """DescribeSlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Total number of slow logs
        :type Count: int
        :param _SlowLogs: Slow log details
        :type SlowLogs: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._SlowLogs = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def SlowLogs(self):
        return self._SlowLogs

    @SlowLogs.setter
    def SlowLogs(self, SlowLogs):
        self._SlowLogs = SlowLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._SlowLogs = params.get("SlowLogs")
        self._RequestId = params.get("RequestId")


class DescribeSpecInfoRequest(AbstractModel):
    """DescribeSpecInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ to be queried
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecInfoResponse(AbstractModel):
    """DescribeSpecInfo response structure.

    """

    def __init__(self):
        r"""
        :param _SpecInfoList: List of purchasable instance specifications
        :type SpecInfoList: list of SpecificationInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SpecInfoList = None
        self._RequestId = None

    @property
    def SpecInfoList(self):
        return self._SpecInfoList

    @SpecInfoList.setter
    def SpecInfoList(self, SpecInfoList):
        self._SpecInfoList = SpecInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self._SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecificationInfo()
                obj._deserialize(item)
                self._SpecInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class FlushInstanceRouterConfigRequest(AbstractModel):
    """FlushInstanceRouterConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class FlushInstanceRouterConfigResponse(AbstractModel):
    """FlushInstanceRouterConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class InquirePriceCreateDBInstancesRequest(AbstractModel):
    """InquirePriceCreateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Instance region name in the format of ap-guangzhou-2.
        :type Zone: str
        :param _NodeNum: Number of primary and secondary nodes per shard. <br>Value range: It can be queried by the <a href="https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1">DescribeSpecInfo</a> API, and the `MinNodeNum` and `MaxNodeNum` parameters are the minimal and maximum value respectively.</li></ul>
        :type NodeNum: int
        :param _Memory: Instance memory size in GB.
        :type Memory: int
        :param _Volume:  Instance disk size. <ul><li>Unit: GB</li><li>Value range: It can be queried by the <a href="https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1">DescribeSpecInfo</a> API, and `MinStorage` and `MaxStorage` parameters are the minimal and maximum value of the disk size respectively.</br>
        :type Volume: int
        :param _MongoVersion: Instance version information. <ul><li>For specific supported versions, query through the <a href="https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1">DescribeSpecInfo</a> API, the returned parameter `MongoVersionCode` in data structure `SpecItems` is the supported version information. </li><li>The correspondences between parameters and versions are as follows <ul><li>MONGO_3_WT: MongoDB 3.2 WiredTiger storage engine version. </li><li>MONGO_3_ROCKS: MongoDB 3.2 RocksDB storage engine version. </li><li>MONGO_36_WT: MongoDB 3.6 WiredTiger storage engine version. </li><li>MONGO_40_WT: MongoDB 4.0 WiredTiger storage engine version. </li><li>MONGO_42_WT: MongoDB 4.2 WiredTiger storage engine version. </li><li>MONGO_44_WT: MongoDB 4.4 WiredTiger storage engine version. </li></ul>
        :type MongoVersion: str
        :param _MachineCode: Server type. Valid values: `HIO` (high IO), `HIO10G` (ten-gigabit high IO)
        :type MachineCode: str
        :param _GoodsNum: Number of instances. Minimum value: 1. Maximum value: 10.
        :type GoodsNum: int
        :param _ClusterType: Instance type. Valid values: REPLSET (replica set), SHARD (sharded cluster), STANDALONE (single-node).
        :type ClusterType: str
        :param _ReplicateSetNum: Number of replica sets. To create a replica set instance, set this parameter to 1; to create a shard instance, see the parameters returned by the `DescribeSpecInfo` API; to create a single-node instance, set this parameter to 0.
        :type ReplicateSetNum: int
        :param _Period: Instance validity period in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param _InstanceChargeType: 
        :type InstanceChargeType: str
        :param _MongosCpu: 
        :type MongosCpu: int
        :param _MongosMemory: 
        :type MongosMemory: int
        :param _MongosNum: 
        :type MongosNum: int
        :param _ConfigServerCpu: 
        :type ConfigServerCpu: int
        :param _ConfigServerMemory: 
        :type ConfigServerMemory: int
        :param _ConfigServerVolume: 
        :type ConfigServerVolume: int
        """
        self._Zone = None
        self._NodeNum = None
        self._Memory = None
        self._Volume = None
        self._MongoVersion = None
        self._MachineCode = None
        self._GoodsNum = None
        self._ClusterType = None
        self._ReplicateSetNum = None
        self._Period = None
        self._InstanceChargeType = None
        self._MongosCpu = None
        self._MongosMemory = None
        self._MongosNum = None
        self._ConfigServerCpu = None
        self._ConfigServerMemory = None
        self._ConfigServerVolume = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeNum(self):
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def MongoVersion(self):
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def MachineCode(self):
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ReplicateSetNum(self):
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def MongosCpu(self):
        return self._MongosCpu

    @MongosCpu.setter
    def MongosCpu(self, MongosCpu):
        self._MongosCpu = MongosCpu

    @property
    def MongosMemory(self):
        return self._MongosMemory

    @MongosMemory.setter
    def MongosMemory(self, MongosMemory):
        self._MongosMemory = MongosMemory

    @property
    def MongosNum(self):
        return self._MongosNum

    @MongosNum.setter
    def MongosNum(self, MongosNum):
        self._MongosNum = MongosNum

    @property
    def ConfigServerCpu(self):
        return self._ConfigServerCpu

    @ConfigServerCpu.setter
    def ConfigServerCpu(self, ConfigServerCpu):
        self._ConfigServerCpu = ConfigServerCpu

    @property
    def ConfigServerMemory(self):
        return self._ConfigServerMemory

    @ConfigServerMemory.setter
    def ConfigServerMemory(self, ConfigServerMemory):
        self._ConfigServerMemory = ConfigServerMemory

    @property
    def ConfigServerVolume(self):
        return self._ConfigServerVolume

    @ConfigServerVolume.setter
    def ConfigServerVolume(self, ConfigServerVolume):
        self._ConfigServerVolume = ConfigServerVolume


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._NodeNum = params.get("NodeNum")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._MongoVersion = params.get("MongoVersion")
        self._MachineCode = params.get("MachineCode")
        self._GoodsNum = params.get("GoodsNum")
        self._ClusterType = params.get("ClusterType")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        self._Period = params.get("Period")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._MongosCpu = params.get("MongosCpu")
        self._MongosMemory = params.get("MongosMemory")
        self._MongosNum = params.get("MongosNum")
        self._ConfigServerCpu = params.get("ConfigServerCpu")
        self._ConfigServerMemory = params.get("ConfigServerMemory")
        self._ConfigServerVolume = params.get("ConfigServerVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateDBInstancesResponse(AbstractModel):
    """InquirePriceCreateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price.
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = DBInstancePrice()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquirePriceModifyDBInstanceSpecRequest(AbstractModel):
    """InquirePriceModifyDBInstanceSpec request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cmgo-p8vn****. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _Memory: Instance memory size in GB after specification adjustment.
        :type Memory: int
        :param _Volume: Instance disk size in GB after specification adjustment.
        :type Volume: int
        :param _NodeNum: Number of instance nodes. The number of nodes is left unchanged by default and cannot be changed currently.
        :type NodeNum: int
        :param _ReplicateSetNum: Number of instance shards. The number of shards is left unchanged by default and cannot be changed currently.
        :type ReplicateSetNum: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Volume = None
        self._NodeNum = None
        self._ReplicateSetNum = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def NodeNum(self):
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def ReplicateSetNum(self):
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._NodeNum = params.get("NodeNum")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDBInstanceSpecResponse(AbstractModel):
    """InquirePriceModifyDBInstanceSpec response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price.
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = DBInstancePrice()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquirePriceRenewDBInstancesRequest(AbstractModel):
    """InquirePriceRenewDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed in the TencentDB Console. This API supports operations on up to 5 instances at a time.
        :type InstanceIds: list of str
        :param _InstanceChargePrepaid: The parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set automatic renewal, and other attributes of the monthly subscription instance.
        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        self._InstanceIds = None
        self._InstanceChargePrepaid = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewDBInstancesResponse(AbstractModel):
    """InquirePriceRenewDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price.
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = DBInstancePrice()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """Description on the billing mode of an instance

    """

    def __init__(self):
        r"""
        :param _Period: Purchased usage period (in month). Valid values: `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36`. Default value: `1`.
(This parameter is required in `InquirePriceRenewDBInstances` and `RenewDBInstances` APIs.)
        :type Period: int
        :param _RenewFlag: Auto-renewal flag. Valid values:
`NOTIFY_AND_AUTO_RENEW`: notify expiration and renew automatically
`NOTIFY_AND_MANUAL_RENEW`: notify expiration but not renew automatically
`DISABLE_NOTIFY_AND_MANUAL_RENEW`: neither notify expiration nor renew automatically

Default value: `NOTIFY_AND_MANUAL_RENEW`. If this parameter is specified as `NOTIFY_AND_AUTO_RENEW`, the instance will be automatically renewed on a monthly basis when the account balance is sufficient.
(This parameter is required in `InquirePriceRenewDBInstances` and `RenewDBInstances` APIs.)
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """Instance details

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _PayMode: Billing type. Valid value: 0 (pay-as-you-go)
        :type PayMode: int
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ClusterType: Cluster type. Valid values: `0` (replica set instance), `1` (sharded instance).
        :type ClusterType: int
        :param _Region: Region information
        :type Region: str
        :param _Zone: AZ information
        :type Zone: str
        :param _NetType: Network type. Valid values: 0 (basic network), 1 (VPC)
        :type NetType: int
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID of VPC
        :type SubnetId: str
        :param _Status: Instance status. Valid values: `0` (to be initialized), `1` (in process), `2` (running), `-2` (expired).
        :type Status: int
        :param _Vip: Instance IP
        :type Vip: str
        :param _Vport: Port number
        :type Vport: int
        :param _CreateTime: Instance creation time
        :type CreateTime: str
        :param _DeadLine: Instance expiration time
        :type DeadLine: str
        :param _MongoVersion: Instance version information
        :type MongoVersion: str
        :param _Memory: Instance memory size in MB
        :type Memory: int
        :param _Volume: Instance disk size in MB
        :type Volume: int
        :param _CpuNum: Number of CPU cores of an instance
        :type CpuNum: int
        :param _MachineType: Instance machine type
        :type MachineType: str
        :param _SecondaryNum: Number of secondary nodes of an instance
        :type SecondaryNum: int
        :param _ReplicationSetNum: Number of instance shards
        :type ReplicationSetNum: int
        :param _AutoRenewFlag: Instance auto-renewal flag. Valid values: `0` (manual renewal), `1` (auto-renewal), `2` (no renewal upon expiration)
        :type AutoRenewFlag: int
        :param _UsedVolume: Used capacity in MB
        :type UsedVolume: int
        :param _MaintenanceStart: Start time of the maintenance time
        :type MaintenanceStart: str
        :param _MaintenanceEnd: End time of the maintenance time
        :type MaintenanceEnd: str
        :param _ReplicaSets: Shard information
        :type ReplicaSets: list of ShardInfo
        :param _ReadonlyInstances: Information of read-only instances
        :type ReadonlyInstances: list of DBInstanceInfo
        :param _StandbyInstances: Information of disaster recovery instances
        :type StandbyInstances: list of DBInstanceInfo
        :param _CloneInstances: Information of temp instances
        :type CloneInstances: list of DBInstanceInfo
        :param _RelatedInstance: Information of associated instances. For a regular instance, this field represents the information of its temp instance; for a temp instance, this field represents the information of its regular instance; and for a read-only instance or a disaster recovery instance, this field represents the information of its primary instance.
        :type RelatedInstance: :class:`tencentcloud.mongodb.v20190725.models.DBInstanceInfo`
        :param _Tags: Instance tag information set
        :type Tags: list of TagInfo
        :param _InstanceVer: Instance version
        :type InstanceVer: int
        :param _ClusterVer: Instance version
        :type ClusterVer: int
        :param _Protocol: Protocol information. Valid values: `1` (mongodb), `2` (dynamodb).
        :type Protocol: int
        :param _InstanceType: Instance type. Valid values: 1 (promoted instance), 2 (temp instance), 3 (read-only instance), 4 (disaster recovery instance)
        :type InstanceType: int
        :param _InstanceStatusDesc: Instance status description
        :type InstanceStatusDesc: str
        :param _RealInstanceId: Physical instance ID. For an instance that has been rolled back and replaced, its InstanceId and RealInstanceId are different. The physical instance ID is needed in such scenarios as getting monitoring data from Barad
        :type RealInstanceId: str
        :param _MongosNodeNum: Number of mongos nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type MongosNodeNum: int
        :param _MongosMemory: mongos node memory
Note: This field may return null, indicating that no valid values can be obtained.
        :type MongosMemory: int
        :param _MongosCpuNum: Number of mongos nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type MongosCpuNum: int
        :param _ConfigServerNodeNum: Number of ConfigServer nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigServerNodeNum: int
        :param _ConfigServerMemory: Memory of ConfigServer node
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigServerMemory: int
        :param _ConfigServerVolume: Disk size of ConfigServer node
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigServerVolume: int
        :param _ConfigServerCpuNum: CPU number of ConfigServer node
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigServerCpuNum: int
        :param _ReadonlyNodeNum: Number of read-only nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReadonlyNodeNum: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._PayMode = None
        self._ProjectId = None
        self._ClusterType = None
        self._Region = None
        self._Zone = None
        self._NetType = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._Vip = None
        self._Vport = None
        self._CreateTime = None
        self._DeadLine = None
        self._MongoVersion = None
        self._Memory = None
        self._Volume = None
        self._CpuNum = None
        self._MachineType = None
        self._SecondaryNum = None
        self._ReplicationSetNum = None
        self._AutoRenewFlag = None
        self._UsedVolume = None
        self._MaintenanceStart = None
        self._MaintenanceEnd = None
        self._ReplicaSets = None
        self._ReadonlyInstances = None
        self._StandbyInstances = None
        self._CloneInstances = None
        self._RelatedInstance = None
        self._Tags = None
        self._InstanceVer = None
        self._ClusterVer = None
        self._Protocol = None
        self._InstanceType = None
        self._InstanceStatusDesc = None
        self._RealInstanceId = None
        self._MongosNodeNum = None
        self._MongosMemory = None
        self._MongosCpuNum = None
        self._ConfigServerNodeNum = None
        self._ConfigServerMemory = None
        self._ConfigServerVolume = None
        self._ConfigServerCpuNum = None
        self._ReadonlyNodeNum = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeadLine(self):
        return self._DeadLine

    @DeadLine.setter
    def DeadLine(self, DeadLine):
        self._DeadLine = DeadLine

    @property
    def MongoVersion(self):
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def CpuNum(self):
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def SecondaryNum(self):
        return self._SecondaryNum

    @SecondaryNum.setter
    def SecondaryNum(self, SecondaryNum):
        self._SecondaryNum = SecondaryNum

    @property
    def ReplicationSetNum(self):
        return self._ReplicationSetNum

    @ReplicationSetNum.setter
    def ReplicationSetNum(self, ReplicationSetNum):
        self._ReplicationSetNum = ReplicationSetNum

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def UsedVolume(self):
        return self._UsedVolume

    @UsedVolume.setter
    def UsedVolume(self, UsedVolume):
        self._UsedVolume = UsedVolume

    @property
    def MaintenanceStart(self):
        return self._MaintenanceStart

    @MaintenanceStart.setter
    def MaintenanceStart(self, MaintenanceStart):
        self._MaintenanceStart = MaintenanceStart

    @property
    def MaintenanceEnd(self):
        return self._MaintenanceEnd

    @MaintenanceEnd.setter
    def MaintenanceEnd(self, MaintenanceEnd):
        self._MaintenanceEnd = MaintenanceEnd

    @property
    def ReplicaSets(self):
        return self._ReplicaSets

    @ReplicaSets.setter
    def ReplicaSets(self, ReplicaSets):
        self._ReplicaSets = ReplicaSets

    @property
    def ReadonlyInstances(self):
        return self._ReadonlyInstances

    @ReadonlyInstances.setter
    def ReadonlyInstances(self, ReadonlyInstances):
        self._ReadonlyInstances = ReadonlyInstances

    @property
    def StandbyInstances(self):
        return self._StandbyInstances

    @StandbyInstances.setter
    def StandbyInstances(self, StandbyInstances):
        self._StandbyInstances = StandbyInstances

    @property
    def CloneInstances(self):
        return self._CloneInstances

    @CloneInstances.setter
    def CloneInstances(self, CloneInstances):
        self._CloneInstances = CloneInstances

    @property
    def RelatedInstance(self):
        return self._RelatedInstance

    @RelatedInstance.setter
    def RelatedInstance(self, RelatedInstance):
        self._RelatedInstance = RelatedInstance

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceVer(self):
        return self._InstanceVer

    @InstanceVer.setter
    def InstanceVer(self, InstanceVer):
        self._InstanceVer = InstanceVer

    @property
    def ClusterVer(self):
        return self._ClusterVer

    @ClusterVer.setter
    def ClusterVer(self, ClusterVer):
        self._ClusterVer = ClusterVer

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatusDesc(self):
        return self._InstanceStatusDesc

    @InstanceStatusDesc.setter
    def InstanceStatusDesc(self, InstanceStatusDesc):
        self._InstanceStatusDesc = InstanceStatusDesc

    @property
    def RealInstanceId(self):
        return self._RealInstanceId

    @RealInstanceId.setter
    def RealInstanceId(self, RealInstanceId):
        self._RealInstanceId = RealInstanceId

    @property
    def MongosNodeNum(self):
        return self._MongosNodeNum

    @MongosNodeNum.setter
    def MongosNodeNum(self, MongosNodeNum):
        self._MongosNodeNum = MongosNodeNum

    @property
    def MongosMemory(self):
        return self._MongosMemory

    @MongosMemory.setter
    def MongosMemory(self, MongosMemory):
        self._MongosMemory = MongosMemory

    @property
    def MongosCpuNum(self):
        return self._MongosCpuNum

    @MongosCpuNum.setter
    def MongosCpuNum(self, MongosCpuNum):
        self._MongosCpuNum = MongosCpuNum

    @property
    def ConfigServerNodeNum(self):
        return self._ConfigServerNodeNum

    @ConfigServerNodeNum.setter
    def ConfigServerNodeNum(self, ConfigServerNodeNum):
        self._ConfigServerNodeNum = ConfigServerNodeNum

    @property
    def ConfigServerMemory(self):
        return self._ConfigServerMemory

    @ConfigServerMemory.setter
    def ConfigServerMemory(self, ConfigServerMemory):
        self._ConfigServerMemory = ConfigServerMemory

    @property
    def ConfigServerVolume(self):
        return self._ConfigServerVolume

    @ConfigServerVolume.setter
    def ConfigServerVolume(self, ConfigServerVolume):
        self._ConfigServerVolume = ConfigServerVolume

    @property
    def ConfigServerCpuNum(self):
        return self._ConfigServerCpuNum

    @ConfigServerCpuNum.setter
    def ConfigServerCpuNum(self, ConfigServerCpuNum):
        self._ConfigServerCpuNum = ConfigServerCpuNum

    @property
    def ReadonlyNodeNum(self):
        return self._ReadonlyNodeNum

    @ReadonlyNodeNum.setter
    def ReadonlyNodeNum(self, ReadonlyNodeNum):
        self._ReadonlyNodeNum = ReadonlyNodeNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._PayMode = params.get("PayMode")
        self._ProjectId = params.get("ProjectId")
        self._ClusterType = params.get("ClusterType")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._NetType = params.get("NetType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._CreateTime = params.get("CreateTime")
        self._DeadLine = params.get("DeadLine")
        self._MongoVersion = params.get("MongoVersion")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._CpuNum = params.get("CpuNum")
        self._MachineType = params.get("MachineType")
        self._SecondaryNum = params.get("SecondaryNum")
        self._ReplicationSetNum = params.get("ReplicationSetNum")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._UsedVolume = params.get("UsedVolume")
        self._MaintenanceStart = params.get("MaintenanceStart")
        self._MaintenanceEnd = params.get("MaintenanceEnd")
        if params.get("ReplicaSets") is not None:
            self._ReplicaSets = []
            for item in params.get("ReplicaSets"):
                obj = ShardInfo()
                obj._deserialize(item)
                self._ReplicaSets.append(obj)
        if params.get("ReadonlyInstances") is not None:
            self._ReadonlyInstances = []
            for item in params.get("ReadonlyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self._ReadonlyInstances.append(obj)
        if params.get("StandbyInstances") is not None:
            self._StandbyInstances = []
            for item in params.get("StandbyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self._StandbyInstances.append(obj)
        if params.get("CloneInstances") is not None:
            self._CloneInstances = []
            for item in params.get("CloneInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self._CloneInstances.append(obj)
        if params.get("RelatedInstance") is not None:
            self._RelatedInstance = DBInstanceInfo()
            self._RelatedInstance._deserialize(params.get("RelatedInstance"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceVer = params.get("InstanceVer")
        self._ClusterVer = params.get("ClusterVer")
        self._Protocol = params.get("Protocol")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatusDesc = params.get("InstanceStatusDesc")
        self._RealInstanceId = params.get("RealInstanceId")
        self._MongosNodeNum = params.get("MongosNodeNum")
        self._MongosMemory = params.get("MongosMemory")
        self._MongosCpuNum = params.get("MongosCpuNum")
        self._ConfigServerNodeNum = params.get("ConfigServerNodeNum")
        self._ConfigServerMemory = params.get("ConfigServerMemory")
        self._ConfigServerVolume = params.get("ConfigServerVolume")
        self._ConfigServerCpuNum = params.get("ConfigServerCpuNum")
        self._ReadonlyNodeNum = params.get("ReadonlyNodeNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnumParam(AbstractModel):
    """The collection of modifiable enum parameters of an instance.

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _DefaultValue: Default value
        :type DefaultValue: str
        :param _EnumValue: Acceptable values
        :type EnumValue: list of str
        :param _NeedRestart: Whether to restart the instance for the parameter to take effect. Valid values: `1` (yes), `0` (no, which means the parameter setting takes effect immediately)
        :type NeedRestart: str
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _Tips: Parameter description
        :type Tips: list of str
        :param _ValueType: Data type of the parameter
        :type ValueType: str
        :param _Status: Whether `CurrentValue` is the parameter value actually in use. Valid values: `1` (yes), `0` (no)
        :type Status: int
        """
        self._CurrentValue = None
        self._DefaultValue = None
        self._EnumValue = None
        self._NeedRestart = None
        self._ParamName = None
        self._Tips = None
        self._ValueType = None
        self._Status = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._DefaultValue = params.get("DefaultValue")
        self._EnumValue = params.get("EnumValue")
        self._NeedRestart = params.get("NeedRestart")
        self._ParamName = params.get("ParamName")
        self._Tips = params.get("Tips")
        self._ValueType = params.get("ValueType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceIntegerParam(AbstractModel):
    """The collection of modifiable integer parameters of an instance.

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _DefaultValue: Default value
        :type DefaultValue: str
        :param _Max: Maximum value
        :type Max: str
        :param _Min: Minimum value
        :type Min: str
        :param _NeedRestart: Whether to restart the instance for the parameter to take effect. Valid values: `1` (yes), `0` (no, which means the parameter setting takes effect immediately)
        :type NeedRestart: str
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _Tips: Parameter description
        :type Tips: list of str
        :param _ValueType: Data type of the parameter
        :type ValueType: str
        :param _Status: Whether `CurrentValue` is the parameter value actually in use. Valid values: `1` (yes), `0` (no)
        :type Status: int
        :param _Unit: Redundant field which can be ignored
        :type Unit: str
        """
        self._CurrentValue = None
        self._DefaultValue = None
        self._Max = None
        self._Min = None
        self._NeedRestart = None
        self._ParamName = None
        self._Tips = None
        self._ValueType = None
        self._Status = None
        self._Unit = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._DefaultValue = params.get("DefaultValue")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._NeedRestart = params.get("NeedRestart")
        self._ParamName = params.get("ParamName")
        self._Tips = params.get("Tips")
        self._ValueType = params.get("ValueType")
        self._Status = params.get("Status")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMultiParam(AbstractModel):
    """The collection of modifiable string parameters of an instance which are used to represent time ranges.

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _DefaultValue: Default value
        :type DefaultValue: str
        :param _EnumValue: Acceptable values
        :type EnumValue: list of str
        :param _NeedRestart: Whether to restart the instance for the parameter to take effect. Valid values: `1` (yes), `0` (no, which means the parameter setting takes effect immediately)
        :type NeedRestart: str
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _Status: Whether `CurrentValue` is the parameter value actually in use. Valid values: `1` (yes), `0` (no)
        :type Status: int
        :param _Tips: Parameter description
        :type Tips: list of str
        :param _ValueType: Data type of the current value. Default value: `multi`
        :type ValueType: str
        """
        self._CurrentValue = None
        self._DefaultValue = None
        self._EnumValue = None
        self._NeedRestart = None
        self._ParamName = None
        self._Status = None
        self._Tips = None
        self._ValueType = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._DefaultValue = params.get("DefaultValue")
        self._EnumValue = params.get("EnumValue")
        self._NeedRestart = params.get("NeedRestart")
        self._ParamName = params.get("ParamName")
        self._Status = params.get("Status")
        self._Tips = params.get("Tips")
        self._ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTextParam(AbstractModel):
    """The collection of modifiable text parameters of an instance.

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _DefaultValue: Default value
        :type DefaultValue: str
        :param _NeedRestart: Whether to restart the instance for the parameter to take effect
        :type NeedRestart: str
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _TextValue: Value of a text parameter
        :type TextValue: str
        :param _Tips: Parameter description
        :type Tips: list of str
        :param _ValueType: Value type
        :type ValueType: str
        :param _Status: Whether `CurrentValue` is the parameter value actually in use. Valid values: `1` (yes), `0` (no)
        :type Status: str
        """
        self._CurrentValue = None
        self._DefaultValue = None
        self._NeedRestart = None
        self._ParamName = None
        self._TextValue = None
        self._Tips = None
        self._ValueType = None
        self._Status = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def TextValue(self):
        return self._TextValue

    @TextValue.setter
    def TextValue(self, TextValue):
        self._TextValue = TextValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._DefaultValue = params.get("DefaultValue")
        self._NeedRestart = params.get("NeedRestart")
        self._ParamName = params.get("ParamName")
        self._TextValue = params.get("TextValue")
        self._Tips = params.get("Tips")
        self._ValueType = params.get("ValueType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceNetworkAddressRequest(AbstractModel):
    """ModifyDBInstanceNetworkAddress request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _OldIpExpiredTime: Old IP retention period in minutes. The old IP will be released after the specified time, and both the old and new IPs can be accessed before the release. The value `0` indicates that the old IP will be reclaimed immediately.
        :type OldIpExpiredTime: int
        :param _NewUniqVpcId: ID of the VPC to which the new IP belongs after the switch. When it is classic network, this field will be empty.
        :type NewUniqVpcId: str
        :param _NewUniqSubnetId: ID of the subnet to which the new IP belongs after the switch. When it is classic network, this field will be empty.
        :type NewUniqSubnetId: str
        :param _NetworkAddresses: IP information to be modified
        :type NetworkAddresses: list of ModifyNetworkAddress
        """
        self._InstanceId = None
        self._OldIpExpiredTime = None
        self._NewUniqVpcId = None
        self._NewUniqSubnetId = None
        self._NetworkAddresses = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldIpExpiredTime(self):
        return self._OldIpExpiredTime

    @OldIpExpiredTime.setter
    def OldIpExpiredTime(self, OldIpExpiredTime):
        self._OldIpExpiredTime = OldIpExpiredTime

    @property
    def NewUniqVpcId(self):
        return self._NewUniqVpcId

    @NewUniqVpcId.setter
    def NewUniqVpcId(self, NewUniqVpcId):
        self._NewUniqVpcId = NewUniqVpcId

    @property
    def NewUniqSubnetId(self):
        return self._NewUniqSubnetId

    @NewUniqSubnetId.setter
    def NewUniqSubnetId(self, NewUniqSubnetId):
        self._NewUniqSubnetId = NewUniqSubnetId

    @property
    def NetworkAddresses(self):
        return self._NetworkAddresses

    @NetworkAddresses.setter
    def NetworkAddresses(self, NetworkAddresses):
        self._NetworkAddresses = NetworkAddresses


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldIpExpiredTime = params.get("OldIpExpiredTime")
        self._NewUniqVpcId = params.get("NewUniqVpcId")
        self._NewUniqSubnetId = params.get("NewUniqSubnetId")
        if params.get("NetworkAddresses") is not None:
            self._NetworkAddresses = []
            for item in params.get("NetworkAddresses"):
                obj = ModifyNetworkAddress()
                obj._deserialize(item)
                self._NetworkAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNetworkAddressResponse(AbstractModel):
    """ModifyDBInstanceNetworkAddress response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SecurityGroupIds: Target security group IDs
        :type SecurityGroupIds: list of str
        """
        self._InstanceId = None
        self._SecurityGroupIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param _Memory: Memory size after instance configuration change in GB. Memory and disk must be upgraded or degraded simultaneously
        :type Memory: int
        :param _Volume: Disk size after instance configuration change in GB. Memory and disk must be upgraded or degraded simultaneously. For degradation, the new disk capacity must be greater than 1.2 times the used disk capacity
        :type Volume: int
        :param _OplogSize: Oplog size after instance configuration change in GB, which ranges from 10% to 90% of the disk capacity and is 10% of the disk capacity by default
        :type OplogSize: int
        :param _NodeNum: Node quantity after configuration modification. The value range is subject to the response parameter of the `DescribeSpecInfo` API. If this parameter is left empty, the node quantity remains unchanged.
        :type NodeNum: int
        :param _ReplicateSetNum: Shard quantity after configuration modification, which can only be increased rather than decreased. The value range is subject to the response parameter of the `DescribeSpecInfo` API. If this parameter is left empty, the shard quantity remains unchanged.
        :type ReplicateSetNum: int
        :param _InMaintenance: Switch time. Valid values: `0` (upon modification completion), `1` (during maintenance time). Default value: `0`. If the quantity of nodes or shards is modified, the value will be `0`.
        :type InMaintenance: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Volume = None
        self._OplogSize = None
        self._NodeNum = None
        self._ReplicateSetNum = None
        self._InMaintenance = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def OplogSize(self):
        return self._OplogSize

    @OplogSize.setter
    def OplogSize(self, OplogSize):
        self._OplogSize = OplogSize

    @property
    def NodeNum(self):
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def ReplicateSetNum(self):
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum

    @property
    def InMaintenance(self):
        return self._InMaintenance

    @InMaintenance.setter
    def InMaintenance(self, InMaintenance):
        self._InMaintenance = InMaintenance


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._OplogSize = params.get("OplogSize")
        self._NodeNum = params.get("NodeNum")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        self._InMaintenance = params.get("InMaintenance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSpecResponse(AbstractModel):
    """ModifyDBInstanceSpec response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID
        :type DealId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class ModifyNetworkAddress(AbstractModel):
    """Database IP to be modified

    """

    def __init__(self):
        r"""
        :param _NewIPAddress: New IP
        :type NewIPAddress: str
        :param _OldIpAddress: Old IP
        :type OldIpAddress: str
        """
        self._NewIPAddress = None
        self._OldIpAddress = None

    @property
    def NewIPAddress(self):
        return self._NewIPAddress

    @NewIPAddress.setter
    def NewIPAddress(self, NewIPAddress):
        self._NewIPAddress = NewIPAddress

    @property
    def OldIpAddress(self):
        return self._OldIpAddress

    @OldIpAddress.setter
    def OldIpAddress(self, OldIpAddress):
        self._OldIpAddress = OldIpAddress


    def _deserialize(self, params):
        self._NewIPAddress = params.get("NewIPAddress")
        self._OldIpAddress = params.get("OldIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineIsolatedDBInstanceRequest(AbstractModel):
    """OfflineIsolatedDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class OfflineIsolatedDBInstanceResponse(AbstractModel):
    """OfflineIsolatedDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class RenameInstanceRequest(AbstractModel):
    """RenameInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cmgo-p8vnipr5. It is the same as the instance ID displayed on the TencentDB Console page
        :type InstanceId: str
        :param _NewName: Custom name of the instance, which can contain up to 60 letters, digits, or symbols (_-)
        :type NewName: str
        """
        self._InstanceId = None
        self._NewName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NewName(self):
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameInstanceResponse(AbstractModel):
    """RenameInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RenewDBInstancesRequest(AbstractModel):
    """RenewDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: IDs of one or more instances to be operated. The value can be obtained from the `InstanceId` parameter returned by the `DescribeInstances` API. Up to 100 instances can be requested at a time.
        :type InstanceIds: list of str
        :param _InstanceChargePrepaid: The parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set automatic renewal, and other attributes of the monthly subscription instance. This parameter is mandatory in monthly subscription.
        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        self._InstanceIds = None
        self._InstanceChargePrepaid = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstancesResponse(AbstractModel):
    """RenewDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReplicaSetInfo(AbstractModel):
    """Shard information

    """

    def __init__(self):
        r"""
        :param _ReplicaSetId: Replica set ID
        :type ReplicaSetId: str
        """
        self._ReplicaSetId = None

    @property
    def ReplicaSetId(self):
        return self._ReplicaSetId

    @ReplicaSetId.setter
    def ReplicaSetId(self, ReplicaSetId):
        self._ReplicaSetId = ReplicaSetId


    def _deserialize(self, params):
        self._ReplicaSetId = params.get("ReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDBInstancePasswordRequest(AbstractModel):
    """ResetDBInstancePassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _UserName: Instance account name
        :type UserName: str
        :param _Password: New password, which must contain at least eight characters
        :type Password: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
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
        


class ResetDBInstancePasswordResponse(AbstractModel):
    """ResetDBInstancePassword response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async request ID, which is used to query the running status of the process.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """Security group information

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Inbound: Inbound rule
        :type Inbound: list of SecurityGroupBound
        :param _Outbound: Outbound rule
        :type Outbound: list of SecurityGroupBound
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._Inbound = None
        self._Outbound = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Inbound(self):
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Outbound.append(obj)
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
        


class SecurityGroupBound(AbstractModel):
    """Security group rule

    """

    def __init__(self):
        r"""
        :param _Action: Execution rule. Valid values: `ACCEPT`, `DROP`
        :type Action: str
        :param _CidrIp: IP range
        :type CidrIp: str
        :param _PortRange: Port range
        :type PortRange: str
        :param _IpProtocol: Transport layer protocol. Valid values: `tcp`, `udp`, `ALL`
        :type IpProtocol: str
        :param _Id: All the addresses that the security group ID represents
        :type Id: str
        :param _AddressModule: All the addresses that the address group ID represents
        :type AddressModule: str
        :param _ServiceModule: All the protocols and ports that the service group ID represents
        :type ServiceModule: str
        :param _Desc: Description
        :type Desc: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Id = None
        self._AddressModule = None
        self._ServiceModule = None
        self._Desc = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def ServiceModule(self):
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Id = params.get("Id")
        self._AddressModule = params.get("AddressModule")
        self._ServiceModule = params.get("ServiceModule")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardInfo(AbstractModel):
    """Details of an instance shard

    """

    def __init__(self):
        r"""
        :param _UsedVolume: Used shard capacity
        :type UsedVolume: float
        :param _ReplicaSetId: Shard ID
        :type ReplicaSetId: str
        :param _ReplicaSetName: Shard name
        :type ReplicaSetName: str
        :param _Memory: Shard memory size in MB
        :type Memory: int
        :param _Volume: Shard disk size in MB
        :type Volume: int
        :param _OplogSize: Shard oplog size in MB
        :type OplogSize: int
        :param _SecondaryNum: Number of secondary nodes of a shard
        :type SecondaryNum: int
        :param _RealReplicaSetId: Shard physical ID
        :type RealReplicaSetId: str
        """
        self._UsedVolume = None
        self._ReplicaSetId = None
        self._ReplicaSetName = None
        self._Memory = None
        self._Volume = None
        self._OplogSize = None
        self._SecondaryNum = None
        self._RealReplicaSetId = None

    @property
    def UsedVolume(self):
        return self._UsedVolume

    @UsedVolume.setter
    def UsedVolume(self, UsedVolume):
        self._UsedVolume = UsedVolume

    @property
    def ReplicaSetId(self):
        return self._ReplicaSetId

    @ReplicaSetId.setter
    def ReplicaSetId(self, ReplicaSetId):
        self._ReplicaSetId = ReplicaSetId

    @property
    def ReplicaSetName(self):
        return self._ReplicaSetName

    @ReplicaSetName.setter
    def ReplicaSetName(self, ReplicaSetName):
        self._ReplicaSetName = ReplicaSetName

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def OplogSize(self):
        return self._OplogSize

    @OplogSize.setter
    def OplogSize(self, OplogSize):
        self._OplogSize = OplogSize

    @property
    def SecondaryNum(self):
        return self._SecondaryNum

    @SecondaryNum.setter
    def SecondaryNum(self, SecondaryNum):
        self._SecondaryNum = SecondaryNum

    @property
    def RealReplicaSetId(self):
        return self._RealReplicaSetId

    @RealReplicaSetId.setter
    def RealReplicaSetId(self, RealReplicaSetId):
        self._RealReplicaSetId = RealReplicaSetId


    def _deserialize(self, params):
        self._UsedVolume = params.get("UsedVolume")
        self._ReplicaSetId = params.get("ReplicaSetId")
        self._ReplicaSetName = params.get("ReplicaSetName")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._OplogSize = params.get("OplogSize")
        self._SecondaryNum = params.get("SecondaryNum")
        self._RealReplicaSetId = params.get("RealReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogPattern(AbstractModel):
    """Slow log statistics of MongoDB database

    """

    def __init__(self):
        r"""
        :param _Pattern: Slow log pattern
        :type Pattern: str
        :param _MaxTime: Maximum execution time
        :type MaxTime: int
        :param _AverageTime: Average execution time
        :type AverageTime: int
        :param _Total: Number of slow logs in this pattern
        :type Total: int
        """
        self._Pattern = None
        self._MaxTime = None
        self._AverageTime = None
        self._Total = None

    @property
    def Pattern(self):
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def AverageTime(self):
        return self._AverageTime

    @AverageTime.setter
    def AverageTime(self, AverageTime):
        self._AverageTime = AverageTime

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Pattern = params.get("Pattern")
        self._MaxTime = params.get("MaxTime")
        self._AverageTime = params.get("AverageTime")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecItem(AbstractModel):
    """Specifications of purchasable MongoDB instances

    """

    def __init__(self):
        r"""
        :param _SpecCode: Specification information identifier
        :type SpecCode: str
        :param _Status: Specification purchasable flag. Valid values: 0 (not purchasable), 1 (purchasable)
        :type Status: int
        :param _Cpu: Computing resource specification in terms of CPU core
        :type Cpu: int
        :param _Memory: Memory size in MB
        :type Memory: int
        :param _DefaultStorage: Default disk size in MB
        :type DefaultStorage: int
        :param _MaxStorage: Maximum disk size in MB
        :type MaxStorage: int
        :param _MinStorage: Minimum disk size in MB
        :type MinStorage: int
        :param _Qps: Maximum QPS
        :type Qps: int
        :param _Conns: Maximum number of connections
        :type Conns: int
        :param _MongoVersionCode: MongoDB version information of an instance
        :type MongoVersionCode: str
        :param _MongoVersionValue: MongoDB version number of an instance
        :type MongoVersionValue: int
        :param _Version: MongoDB version number of an instance (short)
        :type Version: str
        :param _EngineName: Storage engine
        :type EngineName: str
        :param _ClusterType: Cluster type. Valid values: 1 (sharding cluster), 0 (replica set cluster)
        :type ClusterType: int
        :param _MinNodeNum: Minimum number of secondary nodes in a replica set
        :type MinNodeNum: int
        :param _MaxNodeNum: Maximum number of secondary nodes in a replica set
        :type MaxNodeNum: int
        :param _MinReplicateSetNum: Minimum number of shards
        :type MinReplicateSetNum: int
        :param _MaxReplicateSetNum: Maximum number of shards
        :type MaxReplicateSetNum: int
        :param _MinReplicateSetNodeNum: Minimum number of secondary nodes in a shard
        :type MinReplicateSetNodeNum: int
        :param _MaxReplicateSetNodeNum: Maximum number of secondary nodes in a shard
        :type MaxReplicateSetNodeNum: int
        :param _MachineType: Server type. Valid values: 0 (HIO), 4 (HIO10G)
        :type MachineType: str
        """
        self._SpecCode = None
        self._Status = None
        self._Cpu = None
        self._Memory = None
        self._DefaultStorage = None
        self._MaxStorage = None
        self._MinStorage = None
        self._Qps = None
        self._Conns = None
        self._MongoVersionCode = None
        self._MongoVersionValue = None
        self._Version = None
        self._EngineName = None
        self._ClusterType = None
        self._MinNodeNum = None
        self._MaxNodeNum = None
        self._MinReplicateSetNum = None
        self._MaxReplicateSetNum = None
        self._MinReplicateSetNodeNum = None
        self._MaxReplicateSetNodeNum = None
        self._MachineType = None

    @property
    def SpecCode(self):
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DefaultStorage(self):
        return self._DefaultStorage

    @DefaultStorage.setter
    def DefaultStorage(self, DefaultStorage):
        self._DefaultStorage = DefaultStorage

    @property
    def MaxStorage(self):
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def MinStorage(self):
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Conns(self):
        return self._Conns

    @Conns.setter
    def Conns(self, Conns):
        self._Conns = Conns

    @property
    def MongoVersionCode(self):
        return self._MongoVersionCode

    @MongoVersionCode.setter
    def MongoVersionCode(self, MongoVersionCode):
        self._MongoVersionCode = MongoVersionCode

    @property
    def MongoVersionValue(self):
        return self._MongoVersionValue

    @MongoVersionValue.setter
    def MongoVersionValue(self, MongoVersionValue):
        self._MongoVersionValue = MongoVersionValue

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def EngineName(self):
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def MinNodeNum(self):
        return self._MinNodeNum

    @MinNodeNum.setter
    def MinNodeNum(self, MinNodeNum):
        self._MinNodeNum = MinNodeNum

    @property
    def MaxNodeNum(self):
        return self._MaxNodeNum

    @MaxNodeNum.setter
    def MaxNodeNum(self, MaxNodeNum):
        self._MaxNodeNum = MaxNodeNum

    @property
    def MinReplicateSetNum(self):
        return self._MinReplicateSetNum

    @MinReplicateSetNum.setter
    def MinReplicateSetNum(self, MinReplicateSetNum):
        self._MinReplicateSetNum = MinReplicateSetNum

    @property
    def MaxReplicateSetNum(self):
        return self._MaxReplicateSetNum

    @MaxReplicateSetNum.setter
    def MaxReplicateSetNum(self, MaxReplicateSetNum):
        self._MaxReplicateSetNum = MaxReplicateSetNum

    @property
    def MinReplicateSetNodeNum(self):
        return self._MinReplicateSetNodeNum

    @MinReplicateSetNodeNum.setter
    def MinReplicateSetNodeNum(self, MinReplicateSetNodeNum):
        self._MinReplicateSetNodeNum = MinReplicateSetNodeNum

    @property
    def MaxReplicateSetNodeNum(self):
        return self._MaxReplicateSetNodeNum

    @MaxReplicateSetNodeNum.setter
    def MaxReplicateSetNodeNum(self, MaxReplicateSetNodeNum):
        self._MaxReplicateSetNodeNum = MaxReplicateSetNodeNum

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._Status = params.get("Status")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._DefaultStorage = params.get("DefaultStorage")
        self._MaxStorage = params.get("MaxStorage")
        self._MinStorage = params.get("MinStorage")
        self._Qps = params.get("Qps")
        self._Conns = params.get("Conns")
        self._MongoVersionCode = params.get("MongoVersionCode")
        self._MongoVersionValue = params.get("MongoVersionValue")
        self._Version = params.get("Version")
        self._EngineName = params.get("EngineName")
        self._ClusterType = params.get("ClusterType")
        self._MinNodeNum = params.get("MinNodeNum")
        self._MaxNodeNum = params.get("MaxNodeNum")
        self._MinReplicateSetNum = params.get("MinReplicateSetNum")
        self._MaxReplicateSetNum = params.get("MaxReplicateSetNum")
        self._MinReplicateSetNodeNum = params.get("MinReplicateSetNodeNum")
        self._MaxReplicateSetNodeNum = params.get("MaxReplicateSetNodeNum")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificationInfo(AbstractModel):
    """Instance specification information

    """

    def __init__(self):
        r"""
        :param _Region: Region information
        :type Region: str
        :param _Zone: AZ information
        :type Zone: str
        :param _SpecItems: Purchasable specification information
        :type SpecItems: list of SpecItem
        :param _SupportMultiAZ: Whether cross-AZ deployment is supported. Valid values: `1` (yes), `0` (no).
        :type SupportMultiAZ: int
        """
        self._Region = None
        self._Zone = None
        self._SpecItems = None
        self._SupportMultiAZ = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecItems(self):
        return self._SpecItems

    @SpecItems.setter
    def SpecItems(self, SpecItems):
        self._SpecItems = SpecItems

    @property
    def SupportMultiAZ(self):
        return self._SupportMultiAZ

    @SupportMultiAZ.setter
    def SupportMultiAZ(self, SupportMultiAZ):
        self._SupportMultiAZ = SupportMultiAZ


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        if params.get("SpecItems") is not None:
            self._SpecItems = []
            for item in params.get("SpecItems"):
                obj = SpecItem()
                obj._deserialize(item)
                self._SpecItems.append(obj)
        self._SupportMultiAZ = params.get("SupportMultiAZ")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Instance tag information

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
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        