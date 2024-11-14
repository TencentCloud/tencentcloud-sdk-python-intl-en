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


class AccountDetailInfo(AbstractModel):
    """Account details

    """

    def __init__(self):
        r"""
        :param _UserName: Username

Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Host: Host name or IP address, which indicates the host to which the user belongs.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param _UserDescription: User description information

Note: This field may return null, indicating that no valid values can be obtained.
        :type UserDescription: str
        """
        self._UserName = None
        self._Host = None
        self._UserDescription = None

    @property
    def UserName(self):
        """Username

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Host name or IP address, which indicates the host to which the user belongs.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def UserDescription(self):
        """User description information

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserDescription

    @UserDescription.setter
    def UserDescription(self, UserDescription):
        self._UserDescription = UserDescription


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._UserDescription = params.get("UserDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionAlterUserRequest(AbstractModel):
    """ActionAlterUser request structure.

    """

    def __init__(self):
        r"""
        :param _UserInfo: User information
        :type UserInfo: :class:`tencentcloud.cdwdoris.v20211228.models.UserInfo`
        :param _ApiType: API type
        :type ApiType: str
        :param _UserPrivilege: User permission type. 0: ordinary user; 1: administrator.
        :type UserPrivilege: int
        """
        self._UserInfo = None
        self._ApiType = None
        self._UserPrivilege = None

    @property
    def UserInfo(self):
        """User information
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.UserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def ApiType(self):
        """API type
        :rtype: str
        """
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def UserPrivilege(self):
        """User permission type. 0: ordinary user; 1: administrator.
        :rtype: int
        """
        return self._UserPrivilege

    @UserPrivilege.setter
    def UserPrivilege(self, UserPrivilege):
        self._UserPrivilege = UserPrivilege


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = UserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._ApiType = params.get("ApiType")
        self._UserPrivilege = params.get("UserPrivilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionAlterUserResponse(AbstractModel):
    """ActionAlterUser response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class AttachCBSSpec(AbstractModel):
    """Specifications of nodes in the cluster and disk specifications description

    """

    def __init__(self):
        r"""
        :param _DiskType: Node disk type, such as CLOUD_SSD"\"CLOUD_PREMIUM
        :type DiskType: str
        :param _DiskSize: Disk capacity, in GB
        :type DiskSize: int
        :param _DiskCount: Total number of disks
        :type DiskCount: int
        :param _DiskDesc: Description
        :type DiskDesc: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None
        self._DiskDesc = None

    @property
    def DiskType(self):
        """Node disk type, such as CLOUD_SSD"\"CLOUD_PREMIUM
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """Disk capacity, in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        """Total number of disks
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskDesc(self):
        """Description
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskCount = params.get("DiskCount")
        self._DiskDesc = params.get("DiskDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackUpJobDisplay(AbstractModel):
    """Backup instance details

    """

    def __init__(self):
        r"""
        :param _JobId: Backup instance ID
        :type JobId: int
        :param _Snapshot: Backup instance name
        :type Snapshot: str
        :param _BackUpSize: Backup data volume
        :type BackUpSize: int
        :param _BackUpSingleSize: Backup single replica data volume
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackUpSingleSize: int
        :param _BackUpTime: Instance creation time
        :type BackUpTime: str
        :param _ExpireTime: Instance expiration time
        :type ExpireTime: str
        :param _JobStatus: Instance status
        :type JobStatus: str
        :param _BackupType: 0: default; 1: one-time backup for the remote Doris
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupType: int
        :param _BackupTimeType: 0: default; 1: immediate backup; 2: migration
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupTimeType: int
        :param _DorisSourceInfo: Connection information of the remote Doris
Note: This field may return null, indicating that no valid values can be obtained.
        :type DorisSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        :param _JobStatusNum: The value corresponding to the instance status
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobStatusNum: int
        :param _BackupCosInfo: Information about cos in the backup instance	
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupCosInfo: :class:`tencentcloud.cdwdoris.v20211228.models.BackupCosInfo`
        """
        self._JobId = None
        self._Snapshot = None
        self._BackUpSize = None
        self._BackUpSingleSize = None
        self._BackUpTime = None
        self._ExpireTime = None
        self._JobStatus = None
        self._BackupType = None
        self._BackupTimeType = None
        self._DorisSourceInfo = None
        self._JobStatusNum = None
        self._BackupCosInfo = None

    @property
    def JobId(self):
        """Backup instance ID
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Snapshot(self):
        """Backup instance name
        :rtype: str
        """
        return self._Snapshot

    @Snapshot.setter
    def Snapshot(self, Snapshot):
        self._Snapshot = Snapshot

    @property
    def BackUpSize(self):
        """Backup data volume
        :rtype: int
        """
        return self._BackUpSize

    @BackUpSize.setter
    def BackUpSize(self, BackUpSize):
        self._BackUpSize = BackUpSize

    @property
    def BackUpSingleSize(self):
        """Backup single replica data volume
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackUpSingleSize

    @BackUpSingleSize.setter
    def BackUpSingleSize(self, BackUpSingleSize):
        self._BackUpSingleSize = BackUpSingleSize

    @property
    def BackUpTime(self):
        """Instance creation time
        :rtype: str
        """
        return self._BackUpTime

    @BackUpTime.setter
    def BackUpTime(self, BackUpTime):
        self._BackUpTime = BackUpTime

    @property
    def ExpireTime(self):
        """Instance expiration time
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def JobStatus(self):
        """Instance status
        :rtype: str
        """
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def BackupType(self):
        """0: default; 1: one-time backup for the remote Doris
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupTimeType(self):
        """0: default; 1: immediate backup; 2: migration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupTimeType

    @BackupTimeType.setter
    def BackupTimeType(self, BackupTimeType):
        self._BackupTimeType = BackupTimeType

    @property
    def DorisSourceInfo(self):
        """Connection information of the remote Doris
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        """
        return self._DorisSourceInfo

    @DorisSourceInfo.setter
    def DorisSourceInfo(self, DorisSourceInfo):
        self._DorisSourceInfo = DorisSourceInfo

    @property
    def JobStatusNum(self):
        """The value corresponding to the instance status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._JobStatusNum

    @JobStatusNum.setter
    def JobStatusNum(self, JobStatusNum):
        self._JobStatusNum = JobStatusNum

    @property
    def BackupCosInfo(self):
        """Information about cos in the backup instance	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.BackupCosInfo`
        """
        return self._BackupCosInfo

    @BackupCosInfo.setter
    def BackupCosInfo(self, BackupCosInfo):
        self._BackupCosInfo = BackupCosInfo


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Snapshot = params.get("Snapshot")
        self._BackUpSize = params.get("BackUpSize")
        self._BackUpSingleSize = params.get("BackUpSingleSize")
        self._BackUpTime = params.get("BackUpTime")
        self._ExpireTime = params.get("ExpireTime")
        self._JobStatus = params.get("JobStatus")
        self._BackupType = params.get("BackupType")
        self._BackupTimeType = params.get("BackupTimeType")
        if params.get("DorisSourceInfo") is not None:
            self._DorisSourceInfo = DorisSourceInfo()
            self._DorisSourceInfo._deserialize(params.get("DorisSourceInfo"))
        self._JobStatusNum = params.get("JobStatusNum")
        if params.get("BackupCosInfo") is not None:
            self._BackupCosInfo = BackupCosInfo()
            self._BackupCosInfo._deserialize(params.get("BackupCosInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupCosInfo(AbstractModel):
    """Information about cos in the backup instance

    """

    def __init__(self):
        r"""
        :param _CosBucket: The cos bucket where the backup file is located.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosBucket: str
        :param _CosPath: The full cos path where the backup file is located.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosPath: str
        :param _SnapShotPath: Backup file name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SnapShotPath: str
        """
        self._CosBucket = None
        self._CosPath = None
        self._SnapShotPath = None

    @property
    def CosBucket(self):
        """The cos bucket where the backup file is located.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosPath(self):
        """The full cos path where the backup file is located.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath

    @property
    def SnapShotPath(self):
        """Backup file name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SnapShotPath

    @SnapShotPath.setter
    def SnapShotPath(self, SnapShotPath):
        self._SnapShotPath = SnapShotPath


    def _deserialize(self, params):
        self._CosBucket = params.get("CosBucket")
        self._CosPath = params.get("CosPath")
        self._SnapShotPath = params.get("SnapShotPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupStatus(AbstractModel):
    """Progress details of the backup task

    """

    def __init__(self):
        r"""
        :param _JobId: Backup task ID
        :type JobId: int
        :param _SnapshotName: Snapshot name
        :type SnapshotName: str
        :param _DbName: Database name
        :type DbName: str
        :param _State: Status
        :type State: str
        :param _BackupObjects: Backup object
        :type BackupObjects: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _SnapshotFinishedTime: Snapshot end time
        :type SnapshotFinishedTime: str
        :param _UploadFinishedTime: Upload end time
        :type UploadFinishedTime: str
        :param _FinishedTime: End time
        :type FinishedTime: str
        :param _UnfinishedTasks: Unfinished tasks
        :type UnfinishedTasks: str
        :param _Progress: Progress
        :type Progress: str
        :param _TaskErrMsg: Error message
        :type TaskErrMsg: str
        :param _Status: Status
        :type Status: str
        :param _Timeout: Timeout information
        :type Timeout: int
        :param _BackupJobId: Backup instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupJobId: int
        :param _TaskId: The ID of the snapshoit corresponding to the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        """
        self._JobId = None
        self._SnapshotName = None
        self._DbName = None
        self._State = None
        self._BackupObjects = None
        self._CreateTime = None
        self._SnapshotFinishedTime = None
        self._UploadFinishedTime = None
        self._FinishedTime = None
        self._UnfinishedTasks = None
        self._Progress = None
        self._TaskErrMsg = None
        self._Status = None
        self._Timeout = None
        self._BackupJobId = None
        self._TaskId = None

    @property
    def JobId(self):
        """Backup task ID
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def SnapshotName(self):
        """Snapshot name
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def DbName(self):
        """Database name
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def State(self):
        """Status
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def BackupObjects(self):
        """Backup object
        :rtype: str
        """
        return self._BackupObjects

    @BackupObjects.setter
    def BackupObjects(self, BackupObjects):
        self._BackupObjects = BackupObjects

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SnapshotFinishedTime(self):
        """Snapshot end time
        :rtype: str
        """
        return self._SnapshotFinishedTime

    @SnapshotFinishedTime.setter
    def SnapshotFinishedTime(self, SnapshotFinishedTime):
        self._SnapshotFinishedTime = SnapshotFinishedTime

    @property
    def UploadFinishedTime(self):
        """Upload end time
        :rtype: str
        """
        return self._UploadFinishedTime

    @UploadFinishedTime.setter
    def UploadFinishedTime(self, UploadFinishedTime):
        self._UploadFinishedTime = UploadFinishedTime

    @property
    def FinishedTime(self):
        """End time
        :rtype: str
        """
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def UnfinishedTasks(self):
        """Unfinished tasks
        :rtype: str
        """
        return self._UnfinishedTasks

    @UnfinishedTasks.setter
    def UnfinishedTasks(self, UnfinishedTasks):
        self._UnfinishedTasks = UnfinishedTasks

    @property
    def Progress(self):
        """Progress
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskErrMsg(self):
        """Error message
        :rtype: str
        """
        return self._TaskErrMsg

    @TaskErrMsg.setter
    def TaskErrMsg(self, TaskErrMsg):
        self._TaskErrMsg = TaskErrMsg

    @property
    def Status(self):
        """Status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Timeout(self):
        """Timeout information
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def BackupJobId(self):
        """Backup instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupJobId

    @BackupJobId.setter
    def BackupJobId(self, BackupJobId):
        self._BackupJobId = BackupJobId

    @property
    def TaskId(self):
        """The ID of the snapshoit corresponding to the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._SnapshotName = params.get("SnapshotName")
        self._DbName = params.get("DbName")
        self._State = params.get("State")
        self._BackupObjects = params.get("BackupObjects")
        self._CreateTime = params.get("CreateTime")
        self._SnapshotFinishedTime = params.get("SnapshotFinishedTime")
        self._UploadFinishedTime = params.get("UploadFinishedTime")
        self._FinishedTime = params.get("FinishedTime")
        self._UnfinishedTasks = params.get("UnfinishedTasks")
        self._Progress = params.get("Progress")
        self._TaskErrMsg = params.get("TaskErrMsg")
        self._Status = params.get("Status")
        self._Timeout = params.get("Timeout")
        self._BackupJobId = params.get("BackupJobId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupTableContent(AbstractModel):
    """Backup table information

    """

    def __init__(self):
        r"""
        :param _Database: Database
Note: This field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param _Table: Table
Note: This field may return null, indicating that no valid values can be obtained.
        :type Table: str
        :param _TotalBytes: Total number of bytes in the table
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalBytes: int
        :param _SingleReplicaBytes: Size of a single replica
Note: This field may return null, indicating that no valid values can be obtained.
        :type SingleReplicaBytes: str
        :param _BackupStatus: Backup status
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupStatus: int
        :param _BackupErrorMsg: Error message of the backup
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupErrorMsg: str
        :param _IsOpenCoolDown: Whether to bind the cold storage policy to the database and table
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsOpenCoolDown: bool
        """
        self._Database = None
        self._Table = None
        self._TotalBytes = None
        self._SingleReplicaBytes = None
        self._BackupStatus = None
        self._BackupErrorMsg = None
        self._IsOpenCoolDown = None

    @property
    def Database(self):
        """Database
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """Table
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def TotalBytes(self):
        """Total number of bytes in the table
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalBytes

    @TotalBytes.setter
    def TotalBytes(self, TotalBytes):
        self._TotalBytes = TotalBytes

    @property
    def SingleReplicaBytes(self):
        """Size of a single replica
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SingleReplicaBytes

    @SingleReplicaBytes.setter
    def SingleReplicaBytes(self, SingleReplicaBytes):
        self._SingleReplicaBytes = SingleReplicaBytes

    @property
    def BackupStatus(self):
        """Backup status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def BackupErrorMsg(self):
        """Error message of the backup
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupErrorMsg

    @BackupErrorMsg.setter
    def BackupErrorMsg(self, BackupErrorMsg):
        self._BackupErrorMsg = BackupErrorMsg

    @property
    def IsOpenCoolDown(self):
        """Whether to bind the cold storage policy to the database and table
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsOpenCoolDown

    @IsOpenCoolDown.setter
    def IsOpenCoolDown(self, IsOpenCoolDown):
        self._IsOpenCoolDown = IsOpenCoolDown


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._TotalBytes = params.get("TotalBytes")
        self._SingleReplicaBytes = params.get("SingleReplicaBytes")
        self._BackupStatus = params.get("BackupStatus")
        self._BackupErrorMsg = params.get("BackupErrorMsg")
        self._IsOpenCoolDown = params.get("IsOpenCoolDown")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindUser(AbstractModel):
    """User information bound to the resource group requires username and host information for authorization.

    """

    def __init__(self):
        r"""
        :param _UserName: Username
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Host: Host information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: str
        """
        self._UserName = None
        self._Host = None

    @property
    def UserName(self):
        """Username
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """Host information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelBackupJobRequest(AbstractModel):
    """CancelBackupJob request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _BackUpJobId: Backup instance ID to be canceled
        :type BackUpJobId: int
        """
        self._InstanceId = None
        self._BackUpJobId = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        """Backup instance ID to be canceled
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelBackupJobResponse(AbstractModel):
    """CancelBackupJob response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class CatalogPermission(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _CatalogName: 
        :type CatalogName: str
        :param _Permissions: 
        :type Permissions: list of str
        """
        self._CatalogName = None
        self._Permissions = None

    @property
    def CatalogName(self):
        """
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def Permissions(self):
        """
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._CatalogName = params.get("CatalogName")
        self._Permissions = params.get("Permissions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargeProperties(AbstractModel):
    """Cluster billing-related information

    """

    def __init__(self):
        r"""
        :param _ChargeType: Billing type: PREPAID for prepayment, and POSTPAID_BY_HOUR for postpayment.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _RenewFlag: Whether to automatically renew. 1 means automatic renewal is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param _TimeSpan: Billing duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param _TimeUnit: Billing time unit, and "m" means month, etc.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        """
        self._ChargeType = None
        self._RenewFlag = None
        self._TimeSpan = None
        self._TimeUnit = None

    @property
    def ChargeType(self):
        """Billing type: PREPAID for prepayment, and POSTPAID_BY_HOUR for postpayment.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def RenewFlag(self):
        """Whether to automatically renew. 1 means automatic renewal is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        """Billing duration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """Billing time unit, and "m" means month, etc.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._ChargeType = params.get("ChargeType")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCoolDownWorkingVariableConfigCorrectRequest(AbstractModel):
    """CheckCoolDownWorkingVariableConfigCorrect request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster ID
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
        


class CheckCoolDownWorkingVariableConfigCorrectResponse(AbstractModel):
    """CheckCoolDownWorkingVariableConfigCorrect response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ClusterConfigsHistory(AbstractModel):
    """Modification history of the cluster configuration files

    """

    def __init__(self):
        r"""
        :param _FileName: Configuration file's name
        :type FileName: str
        :param _NewConfValue: Modified configuration file content; base64 code
        :type NewConfValue: str
        :param _OldConfValue: Configuration file content before modification; base64 code
        :type OldConfValue: str
        :param _Remark: Reason for modification
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        :param _UserUin: Modify sub-account ID
        :type UserUin: str
        """
        self._FileName = None
        self._NewConfValue = None
        self._OldConfValue = None
        self._Remark = None
        self._ModifyTime = None
        self._UserUin = None

    @property
    def FileName(self):
        """Configuration file's name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def NewConfValue(self):
        """Modified configuration file content; base64 code
        :rtype: str
        """
        return self._NewConfValue

    @NewConfValue.setter
    def NewConfValue(self, NewConfValue):
        self._NewConfValue = NewConfValue

    @property
    def OldConfValue(self):
        """Configuration file content before modification; base64 code
        :rtype: str
        """
        return self._OldConfValue

    @OldConfValue.setter
    def OldConfValue(self, OldConfValue):
        self._OldConfValue = OldConfValue

    @property
    def Remark(self):
        """Reason for modification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ModifyTime(self):
        """Modification time
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def UserUin(self):
        """Modify sub-account ID
        :rtype: str
        """
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._NewConfValue = params.get("NewConfValue")
        self._OldConfValue = params.get("OldConfValue")
        self._Remark = params.get("Remark")
        self._ModifyTime = params.get("ModifyTime")
        self._UserUin = params.get("UserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterConfigsInfoFromEMR(AbstractModel):
    """It is used to return configuration files and content in XML format, as well as other information related to the configuration files.

    """

    def __init__(self):
        r"""
        :param _FileName: Configuration file's name
        :type FileName: str
        :param _FileConf: Related attribute information corresponding to the configuration files
        :type FileConf: str
        :param _KeyConf: Other attribute information corresponding to the configuration files
        :type KeyConf: str
        :param _OriParam: Contents of the configuration files, base64 encoded
        :type OriParam: str
        :param _NeedRestart: This is used to indicate whether the current configuration file has been modified without a restart, and reminds the user that a restart is needed.
        :type NeedRestart: int
        :param _FilePath: Configuration file path
Note: This field may return null, indicating that no valid values can be obtained.
        :type FilePath: str
        :param _FileKeyValues: kv value of a configuration file
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileKeyValues: str
        :param _FileKeyValuesNew: kv value of a configuration file
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileKeyValuesNew: list of ConfigKeyValue
        """
        self._FileName = None
        self._FileConf = None
        self._KeyConf = None
        self._OriParam = None
        self._NeedRestart = None
        self._FilePath = None
        self._FileKeyValues = None
        self._FileKeyValuesNew = None

    @property
    def FileName(self):
        """Configuration file's name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileConf(self):
        """Related attribute information corresponding to the configuration files
        :rtype: str
        """
        return self._FileConf

    @FileConf.setter
    def FileConf(self, FileConf):
        self._FileConf = FileConf

    @property
    def KeyConf(self):
        """Other attribute information corresponding to the configuration files
        :rtype: str
        """
        return self._KeyConf

    @KeyConf.setter
    def KeyConf(self, KeyConf):
        self._KeyConf = KeyConf

    @property
    def OriParam(self):
        """Contents of the configuration files, base64 encoded
        :rtype: str
        """
        return self._OriParam

    @OriParam.setter
    def OriParam(self, OriParam):
        self._OriParam = OriParam

    @property
    def NeedRestart(self):
        """This is used to indicate whether the current configuration file has been modified without a restart, and reminds the user that a restart is needed.
        :rtype: int
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def FilePath(self):
        """Configuration file path
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileKeyValues(self):
        warnings.warn("parameter `FileKeyValues` is deprecated", DeprecationWarning) 

        """kv value of a configuration file
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FileKeyValues

    @FileKeyValues.setter
    def FileKeyValues(self, FileKeyValues):
        warnings.warn("parameter `FileKeyValues` is deprecated", DeprecationWarning) 

        self._FileKeyValues = FileKeyValues

    @property
    def FileKeyValuesNew(self):
        """kv value of a configuration file
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ConfigKeyValue
        """
        return self._FileKeyValuesNew

    @FileKeyValuesNew.setter
    def FileKeyValuesNew(self, FileKeyValuesNew):
        self._FileKeyValuesNew = FileKeyValuesNew


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileConf = params.get("FileConf")
        self._KeyConf = params.get("KeyConf")
        self._OriParam = params.get("OriParam")
        self._NeedRestart = params.get("NeedRestart")
        self._FilePath = params.get("FilePath")
        self._FileKeyValues = params.get("FileKeyValues")
        if params.get("FileKeyValuesNew") is not None:
            self._FileKeyValuesNew = []
            for item in params.get("FileKeyValuesNew"):
                obj = ConfigKeyValue()
                obj._deserialize(item)
                self._FileKeyValuesNew.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Column(AbstractModel):
    """Column information of the table

    """

    def __init__(self):
        r"""
        :param _Name: Column name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Type: Column type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _AggType: Aggregation type: When the table is an aggregation model (AGG_KEY), the column with the aggregation type is set as the metric column, and other columns are dimension columns. Aggregation type: ●SUM: sum; the values of multiple rows are accumulated. ●REPLACE: replacement; the values in the next batch of data will replace the values in the previously imported rows. ●MAX: retain the maximum value.
 ●MIN: retain the minimum value. ●REPLACE_IF_NOT_NULL: non-null values replacement. The difference from REPLACE is that null values are not replaced. ●HLL_UNION: aggregation method for HLL type columns, which is aggregated by HyperLogLog algorithm. ●BITMAP_UNION: aggregation method for BIMTAP type columns; bitmap union aggregation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AggType: str
        :param _IsNull: Whether the column value is allowed to be Null
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsNull: bool
        :param _IsKey: Whether it is a Key column. The meaning of different data models:
●DUP_KEY: The column specified afterwards is the sorting column.
●AGG_KEY: The column specified afterwards is the dimension column.
●UNI_KEY: The column specified afterward is the primary key column.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsKey: bool
        :param _DefaultValue: Column's default value
Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultValue: str
        :param _IsPartition: Whether it is a partition column. The partition column must be a Key column.

Note: This field may return null, indicating that no valid values can be obtained.
        :type IsPartition: bool
        :param _IsDistribution: Whether it is a bucket column. The bucket column of the aggregation model and primary key model must be Key columns, while the bucket column of the detail model can be any column.

Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDistribution: bool
        :param _AutoInc: Whether it is an auto-increment column. Supported by TCHouse-D 2.1 version and later.
Limit:
1. Only DUP_KEY and UNI_KEY model tables can contain auto-increment columns.
2. A table can contain at most one auto-increment column.
3. The type of the auto-increment column must be BIGINT type and cannot be null.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoInc: bool
        :param _Comment: Column description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Comment: str
        """
        self._Name = None
        self._Type = None
        self._AggType = None
        self._IsNull = None
        self._IsKey = None
        self._DefaultValue = None
        self._IsPartition = None
        self._IsDistribution = None
        self._AutoInc = None
        self._Comment = None

    @property
    def Name(self):
        """Column name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Column type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AggType(self):
        """Aggregation type: When the table is an aggregation model (AGG_KEY), the column with the aggregation type is set as the metric column, and other columns are dimension columns. Aggregation type: ●SUM: sum; the values of multiple rows are accumulated. ●REPLACE: replacement; the values in the next batch of data will replace the values in the previously imported rows. ●MAX: retain the maximum value.
 ●MIN: retain the minimum value. ●REPLACE_IF_NOT_NULL: non-null values replacement. The difference from REPLACE is that null values are not replaced. ●HLL_UNION: aggregation method for HLL type columns, which is aggregated by HyperLogLog algorithm. ●BITMAP_UNION: aggregation method for BIMTAP type columns; bitmap union aggregation.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AggType

    @AggType.setter
    def AggType(self, AggType):
        self._AggType = AggType

    @property
    def IsNull(self):
        """Whether the column value is allowed to be Null
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsNull

    @IsNull.setter
    def IsNull(self, IsNull):
        self._IsNull = IsNull

    @property
    def IsKey(self):
        """Whether it is a Key column. The meaning of different data models:
●DUP_KEY: The column specified afterwards is the sorting column.
●AGG_KEY: The column specified afterwards is the dimension column.
●UNI_KEY: The column specified afterward is the primary key column.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsKey

    @IsKey.setter
    def IsKey(self, IsKey):
        self._IsKey = IsKey

    @property
    def DefaultValue(self):
        """Column's default value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def IsPartition(self):
        """Whether it is a partition column. The partition column must be a Key column.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsPartition

    @IsPartition.setter
    def IsPartition(self, IsPartition):
        self._IsPartition = IsPartition

    @property
    def IsDistribution(self):
        """Whether it is a bucket column. The bucket column of the aggregation model and primary key model must be Key columns, while the bucket column of the detail model can be any column.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsDistribution

    @IsDistribution.setter
    def IsDistribution(self, IsDistribution):
        self._IsDistribution = IsDistribution

    @property
    def AutoInc(self):
        """Whether it is an auto-increment column. Supported by TCHouse-D 2.1 version and later.
Limit:
1. Only DUP_KEY and UNI_KEY model tables can contain auto-increment columns.
2. A table can contain at most one auto-increment column.
3. The type of the auto-increment column must be BIGINT type and cannot be null.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._AutoInc

    @AutoInc.setter
    def AutoInc(self, AutoInc):
        self._AutoInc = AutoInc

    @property
    def Comment(self):
        """Column description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._AggType = params.get("AggType")
        self._IsNull = params.get("IsNull")
        self._IsKey = params.get("IsKey")
        self._DefaultValue = params.get("DefaultValue")
        self._IsPartition = params.get("IsPartition")
        self._IsDistribution = params.get("IsDistribution")
        self._AutoInc = params.get("AutoInc")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigKeyValue(AbstractModel):
    """Return the configuration file content (key-value)

    """

    def __init__(self):
        r"""
        :param _KeyName: key
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyName: str
        :param _Value: Value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param _Message: Notes
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _Display: 1 indicates read-only, 2 indicates editable but undeletable, and 3 indicates deletable.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Display: int
        :param _SupportHotUpdate: 0 means not supported, and 1 means hot update is supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportHotUpdate: int
        """
        self._KeyName = None
        self._Value = None
        self._Message = None
        self._Display = None
        self._SupportHotUpdate = None

    @property
    def KeyName(self):
        """key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def Value(self):
        """Value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Message(self):
        """Notes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Display(self):
        """1 indicates read-only, 2 indicates editable but undeletable, and 3 indicates deletable.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Display

    @Display.setter
    def Display(self, Display):
        self._Display = Display

    @property
    def SupportHotUpdate(self):
        """0 means not supported, and 1 means hot update is supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SupportHotUpdate

    @SupportHotUpdate.setter
    def SupportHotUpdate(self, SupportHotUpdate):
        self._SupportHotUpdate = SupportHotUpdate


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._Value = params.get("Value")
        self._Message = params.get("Message")
        self._Display = params.get("Display")
        self._SupportHotUpdate = params.get("SupportHotUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigSubmitContext(AbstractModel):
    """Configuration file modification information

    """

    def __init__(self):
        r"""
        :param _FileName: Configuration file's name
        :type FileName: str
        :param _NewConfValue: New Base64-encoded content of the configuration file
        :type NewConfValue: str
        :param _OldConfValue: Original Base64-encoded content of the configuration file
        :type OldConfValue: str
        :param _FilePath: File path
        :type FilePath: str
        """
        self._FileName = None
        self._NewConfValue = None
        self._OldConfValue = None
        self._FilePath = None

    @property
    def FileName(self):
        """Configuration file's name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def NewConfValue(self):
        """New Base64-encoded content of the configuration file
        :rtype: str
        """
        return self._NewConfValue

    @NewConfValue.setter
    def NewConfValue(self, NewConfValue):
        self._NewConfValue = NewConfValue

    @property
    def OldConfValue(self):
        """Original Base64-encoded content of the configuration file
        :rtype: str
        """
        return self._OldConfValue

    @OldConfValue.setter
    def OldConfValue(self, OldConfValue):
        self._OldConfValue = OldConfValue

    @property
    def FilePath(self):
        """File path
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._NewConfValue = params.get("NewConfValue")
        self._OldConfValue = params.get("OldConfValue")
        self._FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoolDownBackend(AbstractModel):
    """Information on the backend node supporting hot/cold data layering

    """

    def __init__(self):
        r"""
        :param _Host: Field: Host
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param _DataUsedCapacity: Field: DataUsedCapacity
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataUsedCapacity: str
        :param _TotalCapacity: Field: TotalCapacity
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCapacity: str
        :param _RemoteUsedCapacity: Field: RemoteUsedCapacity
Note: This field may return null, indicating that no valid values can be obtained.
        :type RemoteUsedCapacity: str
        """
        self._Host = None
        self._DataUsedCapacity = None
        self._TotalCapacity = None
        self._RemoteUsedCapacity = None

    @property
    def Host(self):
        """Field: Host
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DataUsedCapacity(self):
        """Field: DataUsedCapacity
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DataUsedCapacity

    @DataUsedCapacity.setter
    def DataUsedCapacity(self, DataUsedCapacity):
        self._DataUsedCapacity = DataUsedCapacity

    @property
    def TotalCapacity(self):
        """Field: TotalCapacity
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TotalCapacity

    @TotalCapacity.setter
    def TotalCapacity(self, TotalCapacity):
        self._TotalCapacity = TotalCapacity

    @property
    def RemoteUsedCapacity(self):
        """Field: RemoteUsedCapacity
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RemoteUsedCapacity

    @RemoteUsedCapacity.setter
    def RemoteUsedCapacity(self, RemoteUsedCapacity):
        self._RemoteUsedCapacity = RemoteUsedCapacity


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._DataUsedCapacity = params.get("DataUsedCapacity")
        self._TotalCapacity = params.get("TotalCapacity")
        self._RemoteUsedCapacity = params.get("RemoteUsedCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoolDownPolicyInfo(AbstractModel):
    """Hot/cold data layering policy

    """

    def __init__(self):
        r"""
        :param _PolicyName: Policy name

Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyName: str
        :param _CooldownDatetime: cooldown_ttl
Note: This field may return null, indicating that no valid values can be obtained.
        :type CooldownDatetime: str
        :param _CooldownTtl: cooldown_datetime
Note: This field may return null, indicating that no valid values can be obtained.
        :type CooldownTtl: str
        """
        self._PolicyName = None
        self._CooldownDatetime = None
        self._CooldownTtl = None

    @property
    def PolicyName(self):
        """Policy name

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CooldownDatetime(self):
        """cooldown_ttl
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CooldownDatetime

    @CooldownDatetime.setter
    def CooldownDatetime(self, CooldownDatetime):
        self._CooldownDatetime = CooldownDatetime

    @property
    def CooldownTtl(self):
        """cooldown_datetime
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CooldownTtl

    @CooldownTtl.setter
    def CooldownTtl(self, CooldownTtl):
        self._CooldownTtl = CooldownTtl


    def _deserialize(self, params):
        self._PolicyName = params.get("PolicyName")
        self._CooldownDatetime = params.get("CooldownDatetime")
        self._CooldownTtl = params.get("CooldownTtl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoolDownTableDataInfo(AbstractModel):
    """Information on the table containing layered cold and hot data

    """

    def __init__(self):
        r"""
        :param _DatabaseName: Column: DatabaseName
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param _TableName: Column: TableName
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _Size: Column: Size
Note: This field may return null, indicating that no valid values can be obtained.
        :type Size: str
        :param _RemoteSize: Column: RemoteSize
Note: This field may return null, indicating that no valid values can be obtained.
        :type RemoteSize: str
        """
        self._DatabaseName = None
        self._TableName = None
        self._Size = None
        self._RemoteSize = None

    @property
    def DatabaseName(self):
        """Column: DatabaseName
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        """Column: TableName
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Size(self):
        """Column: Size
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def RemoteSize(self):
        """Column: RemoteSize
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RemoteSize

    @RemoteSize.setter
    def RemoteSize(self, RemoteSize):
        self._RemoteSize = RemoteSize


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._Size = params.get("Size")
        self._RemoteSize = params.get("RemoteSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyTableDatasRequest(AbstractModel):
    """CopyTableDatas request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Resource ID, which is the TCHouse-D resource ID used for table creation.
        :type InstanceId: str
        :param _CopiedFromDb: Name of the database where the source table is located.
        :type CopiedFromDb: str
        :param _CopiedFromTable: Source table name
        :type CopiedFromTable: str
        :param _CopyToDb: Name of the database where the target table is located
        :type CopyToDb: str
        :param _CopyToTable: Target table name. If the table already exists, the structure of the source table and target table should be the same.
        :type CopyToTable: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _IsDataOverwrite: Whether the data in the target table is overwritten. The default value is False.
        :type IsDataOverwrite: bool
        """
        self._InstanceId = None
        self._CopiedFromDb = None
        self._CopiedFromTable = None
        self._CopyToDb = None
        self._CopyToTable = None
        self._UserName = None
        self._PassWord = None
        self._IsDataOverwrite = None

    @property
    def InstanceId(self):
        """Resource ID, which is the TCHouse-D resource ID used for table creation.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CopiedFromDb(self):
        """Name of the database where the source table is located.
        :rtype: str
        """
        return self._CopiedFromDb

    @CopiedFromDb.setter
    def CopiedFromDb(self, CopiedFromDb):
        self._CopiedFromDb = CopiedFromDb

    @property
    def CopiedFromTable(self):
        """Source table name
        :rtype: str
        """
        return self._CopiedFromTable

    @CopiedFromTable.setter
    def CopiedFromTable(self, CopiedFromTable):
        self._CopiedFromTable = CopiedFromTable

    @property
    def CopyToDb(self):
        """Name of the database where the target table is located
        :rtype: str
        """
        return self._CopyToDb

    @CopyToDb.setter
    def CopyToDb(self, CopyToDb):
        self._CopyToDb = CopyToDb

    @property
    def CopyToTable(self):
        """Target table name. If the table already exists, the structure of the source table and target table should be the same.
        :rtype: str
        """
        return self._CopyToTable

    @CopyToTable.setter
    def CopyToTable(self, CopyToTable):
        self._CopyToTable = CopyToTable

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def IsDataOverwrite(self):
        """Whether the data in the target table is overwritten. The default value is False.
        :rtype: bool
        """
        return self._IsDataOverwrite

    @IsDataOverwrite.setter
    def IsDataOverwrite(self, IsDataOverwrite):
        self._IsDataOverwrite = IsDataOverwrite


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CopiedFromDb = params.get("CopiedFromDb")
        self._CopiedFromTable = params.get("CopiedFromTable")
        self._CopyToDb = params.get("CopyToDb")
        self._CopyToTable = params.get("CopyToTable")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._IsDataOverwrite = params.get("IsDataOverwrite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyTableDatasResponse(AbstractModel):
    """CopyTableDatas response structure.

    """

    def __init__(self):
        r"""
        :param _Message: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Message = None
        self._RequestId = None

    @property
    def Message(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class CosSourceInfo(AbstractModel):
    """The customer provides cos authentication information.

    """

    def __init__(self):
        r"""
        :param _SecretId: ID in cos authentication
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecretId: str
        :param _SecretKey: Key in cos authentication
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _CosPath: Path in cos authentication
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosPath: str
        """
        self._SecretId = None
        self._SecretKey = None
        self._CosPath = None

    @property
    def SecretId(self):
        """ID in cos authentication
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        """Key in cos authentication
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def CosPath(self):
        """Path in cos authentication
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath


    def _deserialize(self, params):
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._CosPath = params.get("CosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleRequest(AbstractModel):
    """CreateBackUpSchedule request structure.

    """

    def __init__(self):
        r"""
        :param _ScheduleId: Required to be uploaded when editing
        :type ScheduleId: int
        :param _WeekDays: Selected weeks, separated by commas.
Discarded: Use ScheduleInfo.
        :type WeekDays: str
        :param _ExecuteHour: Hour for executing the backup taskDiscarded: Use ScheduleInfo.
        :type ExecuteHour: int
        :param _BackUpTables: Backup table list
        :type BackUpTables: list of BackupTableContent
        :param _BackupType: 0: default; 1: one-time backup for the remote Doris
        :type BackupType: int
        :param _DorisSourceInfo: Connection information of the remote doris cluster
        :type DorisSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        :param _BackupTimeType: 0: default; 1: one-time backup; 2: remote backup
        :type BackupTimeType: int
        :param _RestoreType: 0: default; 1: immediate recovery after the backup is completed.
        :type RestoreType: int
        :param _AuthType: 0: default; 1: connecting to COS using a custom key.
        :type AuthType: int
        :param _CosSourceInfo: Cos certification information
        :type CosSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        """
        self._ScheduleId = None
        self._WeekDays = None
        self._ExecuteHour = None
        self._BackUpTables = None
        self._BackupType = None
        self._DorisSourceInfo = None
        self._BackupTimeType = None
        self._RestoreType = None
        self._AuthType = None
        self._CosSourceInfo = None

    @property
    def ScheduleId(self):
        """Required to be uploaded when editing
        :rtype: int
        """
        return self._ScheduleId

    @ScheduleId.setter
    def ScheduleId(self, ScheduleId):
        self._ScheduleId = ScheduleId

    @property
    def WeekDays(self):
        """Selected weeks, separated by commas.
Discarded: Use ScheduleInfo.
        :rtype: str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def ExecuteHour(self):
        """Hour for executing the backup taskDiscarded: Use ScheduleInfo.
        :rtype: int
        """
        return self._ExecuteHour

    @ExecuteHour.setter
    def ExecuteHour(self, ExecuteHour):
        self._ExecuteHour = ExecuteHour

    @property
    def BackUpTables(self):
        """Backup table list
        :rtype: list of BackupTableContent
        """
        return self._BackUpTables

    @BackUpTables.setter
    def BackUpTables(self, BackUpTables):
        self._BackUpTables = BackUpTables

    @property
    def BackupType(self):
        """0: default; 1: one-time backup for the remote Doris
        :rtype: int
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def DorisSourceInfo(self):
        """Connection information of the remote doris cluster
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        """
        return self._DorisSourceInfo

    @DorisSourceInfo.setter
    def DorisSourceInfo(self, DorisSourceInfo):
        self._DorisSourceInfo = DorisSourceInfo

    @property
    def BackupTimeType(self):
        """0: default; 1: one-time backup; 2: remote backup
        :rtype: int
        """
        return self._BackupTimeType

    @BackupTimeType.setter
    def BackupTimeType(self, BackupTimeType):
        self._BackupTimeType = BackupTimeType

    @property
    def RestoreType(self):
        """0: default; 1: immediate recovery after the backup is completed.
        :rtype: int
        """
        return self._RestoreType

    @RestoreType.setter
    def RestoreType(self, RestoreType):
        self._RestoreType = RestoreType

    @property
    def AuthType(self):
        """0: default; 1: connecting to COS using a custom key.
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def CosSourceInfo(self):
        """Cos certification information
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        """
        return self._CosSourceInfo

    @CosSourceInfo.setter
    def CosSourceInfo(self, CosSourceInfo):
        self._CosSourceInfo = CosSourceInfo


    def _deserialize(self, params):
        self._ScheduleId = params.get("ScheduleId")
        self._WeekDays = params.get("WeekDays")
        self._ExecuteHour = params.get("ExecuteHour")
        if params.get("BackUpTables") is not None:
            self._BackUpTables = []
            for item in params.get("BackUpTables"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self._BackUpTables.append(obj)
        self._BackupType = params.get("BackupType")
        if params.get("DorisSourceInfo") is not None:
            self._DorisSourceInfo = DorisSourceInfo()
            self._DorisSourceInfo._deserialize(params.get("DorisSourceInfo"))
        self._BackupTimeType = params.get("BackupTimeType")
        self._RestoreType = params.get("RestoreType")
        self._AuthType = params.get("AuthType")
        if params.get("CosSourceInfo") is not None:
            self._CosSourceInfo = CosSourceInfo()
            self._CosSourceInfo._deserialize(params.get("CosSourceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleResponse(AbstractModel):
    """CreateBackUpSchedule response structure.

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


class CreateCoolDownPolicyRequest(AbstractModel):
    """CreateCoolDownPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _PolicyName: Policy name
        :type PolicyName: str
        :param _CoolDownTtl: cooldown_ttl
        :type CoolDownTtl: str
        :param _CoolDownDatetime: cooldown_datetime
        :type CoolDownDatetime: str
        """
        self._InstanceId = None
        self._PolicyName = None
        self._CoolDownTtl = None
        self._CoolDownDatetime = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        """Policy name
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CoolDownTtl(self):
        """cooldown_ttl
        :rtype: str
        """
        return self._CoolDownTtl

    @CoolDownTtl.setter
    def CoolDownTtl(self, CoolDownTtl):
        self._CoolDownTtl = CoolDownTtl

    @property
    def CoolDownDatetime(self):
        """cooldown_datetime
        :rtype: str
        """
        return self._CoolDownDatetime

    @CoolDownDatetime.setter
    def CoolDownDatetime(self, CoolDownDatetime):
        self._CoolDownDatetime = CoolDownDatetime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyName = params.get("PolicyName")
        self._CoolDownTtl = params.get("CoolDownTtl")
        self._CoolDownDatetime = params.get("CoolDownDatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCoolDownPolicyResponse(AbstractModel):
    """CreateCoolDownPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class CreateDatabaseRequest(AbstractModel):
    """CreateDatabase request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Resource ID, which is the TCHouse-D resource ID used for table creation.
        :type InstanceId: str
        :param _DbName: Name of database to be created
        :type DbName: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _Properties: Database attributes. For keys with the same attributes, the priority of the table attribute is higher than that of the database attribute.
        :type Properties: list of Property
        """
        self._InstanceId = None
        self._DbName = None
        self._UserName = None
        self._PassWord = None
        self._Properties = None

    @property
    def InstanceId(self):
        """Resource ID, which is the TCHouse-D resource ID used for table creation.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """Name of database to be created
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def Properties(self):
        """Database attributes. For keys with the same attributes, the priority of the table attribute is higher than that of the database attribute.
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatabaseResponse(AbstractModel):
    """CreateDatabase response structure.

    """

    def __init__(self):
        r"""
        :param _Message: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Message = None
        self._RequestId = None

    @property
    def Message(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class CreateInstanceNewRequest(AbstractModel):
    """CreateInstanceNew request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone
        :type Zone: str
        :param _FeSpec: FE specifications
        :type FeSpec: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        :param _BeSpec: BE specifications.
        :type BeSpec: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        :param _HaFlag: Whether it is highly available.
        :type HaFlag: bool
        :param _UserVPCId: User VPCID
        :type UserVPCId: str
        :param _UserSubnetId: User subnet ID
        :type UserSubnetId: str
        :param _ProductVersion: Product version number
        :type ProductVersion: str
        :param _ChargeProperties: Payment type
        :type ChargeProperties: :class:`tencentcloud.cdwdoris.v20211228.models.ChargeProperties`
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _DorisUserPwd: Database password
        :type DorisUserPwd: str
        :param _Tags: Tag list
        :type Tags: list of Tag
        :param _HaType: High availability type:
0 indicates non-high availability (only one FE, FeSpec.CreateInstanceSpec.Count=1),
1 indicates read high availability (at least 3 FEs must be deployed, FeSpec.CreateInstanceSpec.Count>=3, and it must be an odd number),
2 indicates read and write high availability (at least 5 FEs must be deployed, FeSpec.CreateInstanceSpec.Count>=5, and it must be an odd number).
        :type HaType: int
        :param _CaseSensitive: Whether the table name is case sensitive, 0 refers to sensitive, 1 refers to insensitive, compared in lowercase; 2 refers to insensitive, and the table name is changed to lowercase for storage.
        :type CaseSensitive: int
        :param _EnableMultiZones: Whether to enable multi-availability zone.
        :type EnableMultiZones: bool
        :param _UserMultiZoneInfos: After the Multi-AZ is enabled, all user's Availability Zones and Subnets information are shown.
        :type UserMultiZoneInfos: :class:`tencentcloud.cdwdoris.v20211228.models.NetworkInfo`
        """
        self._Zone = None
        self._FeSpec = None
        self._BeSpec = None
        self._HaFlag = None
        self._UserVPCId = None
        self._UserSubnetId = None
        self._ProductVersion = None
        self._ChargeProperties = None
        self._InstanceName = None
        self._DorisUserPwd = None
        self._Tags = None
        self._HaType = None
        self._CaseSensitive = None
        self._EnableMultiZones = None
        self._UserMultiZoneInfos = None

    @property
    def Zone(self):
        """Availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def FeSpec(self):
        """FE specifications
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        """
        return self._FeSpec

    @FeSpec.setter
    def FeSpec(self, FeSpec):
        self._FeSpec = FeSpec

    @property
    def BeSpec(self):
        """BE specifications.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        """
        return self._BeSpec

    @BeSpec.setter
    def BeSpec(self, BeSpec):
        self._BeSpec = BeSpec

    @property
    def HaFlag(self):
        """Whether it is highly available.
        :rtype: bool
        """
        return self._HaFlag

    @HaFlag.setter
    def HaFlag(self, HaFlag):
        self._HaFlag = HaFlag

    @property
    def UserVPCId(self):
        """User VPCID
        :rtype: str
        """
        return self._UserVPCId

    @UserVPCId.setter
    def UserVPCId(self, UserVPCId):
        self._UserVPCId = UserVPCId

    @property
    def UserSubnetId(self):
        """User subnet ID
        :rtype: str
        """
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def ProductVersion(self):
        """Product version number
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def ChargeProperties(self):
        """Payment type
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ChargeProperties`
        """
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def DorisUserPwd(self):
        """Database password
        :rtype: str
        """
        return self._DorisUserPwd

    @DorisUserPwd.setter
    def DorisUserPwd(self, DorisUserPwd):
        self._DorisUserPwd = DorisUserPwd

    @property
    def Tags(self):
        """Tag list
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HaType(self):
        """High availability type:
0 indicates non-high availability (only one FE, FeSpec.CreateInstanceSpec.Count=1),
1 indicates read high availability (at least 3 FEs must be deployed, FeSpec.CreateInstanceSpec.Count>=3, and it must be an odd number),
2 indicates read and write high availability (at least 5 FEs must be deployed, FeSpec.CreateInstanceSpec.Count>=5, and it must be an odd number).
        :rtype: int
        """
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType

    @property
    def CaseSensitive(self):
        """Whether the table name is case sensitive, 0 refers to sensitive, 1 refers to insensitive, compared in lowercase; 2 refers to insensitive, and the table name is changed to lowercase for storage.
        :rtype: int
        """
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def EnableMultiZones(self):
        """Whether to enable multi-availability zone.
        :rtype: bool
        """
        return self._EnableMultiZones

    @EnableMultiZones.setter
    def EnableMultiZones(self, EnableMultiZones):
        self._EnableMultiZones = EnableMultiZones

    @property
    def UserMultiZoneInfos(self):
        """After the Multi-AZ is enabled, all user's Availability Zones and Subnets information are shown.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.NetworkInfo`
        """
        return self._UserMultiZoneInfos

    @UserMultiZoneInfos.setter
    def UserMultiZoneInfos(self, UserMultiZoneInfos):
        self._UserMultiZoneInfos = UserMultiZoneInfos


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        if params.get("FeSpec") is not None:
            self._FeSpec = CreateInstanceSpec()
            self._FeSpec._deserialize(params.get("FeSpec"))
        if params.get("BeSpec") is not None:
            self._BeSpec = CreateInstanceSpec()
            self._BeSpec._deserialize(params.get("BeSpec"))
        self._HaFlag = params.get("HaFlag")
        self._UserVPCId = params.get("UserVPCId")
        self._UserSubnetId = params.get("UserSubnetId")
        self._ProductVersion = params.get("ProductVersion")
        if params.get("ChargeProperties") is not None:
            self._ChargeProperties = ChargeProperties()
            self._ChargeProperties._deserialize(params.get("ChargeProperties"))
        self._InstanceName = params.get("InstanceName")
        self._DorisUserPwd = params.get("DorisUserPwd")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HaType = params.get("HaType")
        self._CaseSensitive = params.get("CaseSensitive")
        self._EnableMultiZones = params.get("EnableMultiZones")
        if params.get("UserMultiZoneInfos") is not None:
            self._UserMultiZoneInfos = NetworkInfo()
            self._UserMultiZoneInfos._deserialize(params.get("UserMultiZoneInfos"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNewResponse(AbstractModel):
    """CreateInstanceNew response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID
        :type FlowId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class CreateInstanceSpec(AbstractModel):
    """Cluster specifications

    """

    def __init__(self):
        r"""
        :param _SpecName: Specification name
        :type SpecName: str
        :param _Count: Quantities
        :type Count: int
        :param _DiskSize: Cloud disk size
        :type DiskSize: int
        """
        self._SpecName = None
        self._Count = None
        self._DiskSize = None

    @property
    def SpecName(self):
        """Specification name
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        """Quantities
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSize(self):
        """Cloud disk size
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTableRequest(AbstractModel):
    """CreateTable request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Resource ID, which is the TCHouse-D resource ID used for table creation.
        :type InstanceId: str
        :param _DbName: The database where the table is located; if it does not exist, create one.
        :type DbName: str
        :param _TableName: Name of the table to be created
        :type TableName: str
        :param _KeysType: Table data model: 
AGG_KEY: aggregation model; 
UNI_KEY: primary key model; 
DUP_KEY: detail model
        :type KeysType: str
        :param _Columns: Column information of the table
        :type Columns: list of Column
        :param _Distribution: Bucket information
        :type Distribution: :class:`tencentcloud.cdwdoris.v20211228.models.Distribution`
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _IndexInfos: Index information. The inverted index and N-Gram index can be configured through this parameter. The Prefix index is related to the sort key and key column, and do not require additional configuration. Configure bloom_filter_columns in the table attribute when BloomFilter index is required.
        :type IndexInfos: list of IndexInfo
        :param _Partition: Partition information
        :type Partition: :class:`tencentcloud.cdwdoris.v20211228.models.Partition`
        :param _TableComment: Table description
        :type TableComment: str
        :param _Properties: Table attribute
        :type Properties: list of Property
        """
        self._InstanceId = None
        self._DbName = None
        self._TableName = None
        self._KeysType = None
        self._Columns = None
        self._Distribution = None
        self._UserName = None
        self._PassWord = None
        self._IndexInfos = None
        self._Partition = None
        self._TableComment = None
        self._Properties = None

    @property
    def InstanceId(self):
        """Resource ID, which is the TCHouse-D resource ID used for table creation.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """The database where the table is located; if it does not exist, create one.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableName(self):
        """Name of the table to be created
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def KeysType(self):
        """Table data model: 
AGG_KEY: aggregation model; 
UNI_KEY: primary key model; 
DUP_KEY: detail model
        :rtype: str
        """
        return self._KeysType

    @KeysType.setter
    def KeysType(self, KeysType):
        self._KeysType = KeysType

    @property
    def Columns(self):
        """Column information of the table
        :rtype: list of Column
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Distribution(self):
        """Bucket information
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.Distribution`
        """
        return self._Distribution

    @Distribution.setter
    def Distribution(self, Distribution):
        self._Distribution = Distribution

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def IndexInfos(self):
        """Index information. The inverted index and N-Gram index can be configured through this parameter. The Prefix index is related to the sort key and key column, and do not require additional configuration. Configure bloom_filter_columns in the table attribute when BloomFilter index is required.
        :rtype: list of IndexInfo
        """
        return self._IndexInfos

    @IndexInfos.setter
    def IndexInfos(self, IndexInfos):
        self._IndexInfos = IndexInfos

    @property
    def Partition(self):
        """Partition information
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.Partition`
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def TableComment(self):
        """Table description
        :rtype: str
        """
        return self._TableComment

    @TableComment.setter
    def TableComment(self, TableComment):
        self._TableComment = TableComment

    @property
    def Properties(self):
        """Table attribute
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._TableName = params.get("TableName")
        self._KeysType = params.get("KeysType")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Distribution") is not None:
            self._Distribution = Distribution()
            self._Distribution._deserialize(params.get("Distribution"))
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        if params.get("IndexInfos") is not None:
            self._IndexInfos = []
            for item in params.get("IndexInfos"):
                obj = IndexInfo()
                obj._deserialize(item)
                self._IndexInfos.append(obj)
        if params.get("Partition") is not None:
            self._Partition = Partition()
            self._Partition._deserialize(params.get("Partition"))
        self._TableComment = params.get("TableComment")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTableResponse(AbstractModel):
    """CreateTable response structure.

    """

    def __init__(self):
        r"""
        :param _Message: Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Message = None
        self._RequestId = None

    @property
    def Message(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class CreateTablesDDL(AbstractModel):
    """DDL information for creating a table

    """

    def __init__(self):
        r"""
        :param _DbName: Database name

Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _TablesDDLs: DDL information of the table

Note: This field may return null, indicating that no valid values can be obtained.
        :type TablesDDLs: list of TablesDDL
        """
        self._DbName = None
        self._TablesDDLs = None

    @property
    def DbName(self):
        """Database name

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TablesDDLs(self):
        """DDL information of the table

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TablesDDL
        """
        return self._TablesDDLs

    @TablesDDLs.setter
    def TablesDDLs(self, TablesDDLs):
        self._TablesDDLs = TablesDDLs


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        if params.get("TablesDDLs") is not None:
            self._TablesDDLs = []
            for item in params.get("TablesDDLs"):
                obj = TablesDDL()
                obj._deserialize(item)
                self._TablesDDLs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkloadGroupRequest(AbstractModel):
    """CreateWorkloadGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID	
        :type InstanceId: str
        :param _WorkloadGroup: Resource group configuration
        :type WorkloadGroup: :class:`tencentcloud.cdwdoris.v20211228.models.WorkloadGroupConfig`
        """
        self._InstanceId = None
        self._WorkloadGroup = None

    @property
    def InstanceId(self):
        """Cluster ID	
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WorkloadGroup(self):
        """Resource group configuration
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.WorkloadGroupConfig`
        """
        return self._WorkloadGroup

    @WorkloadGroup.setter
    def WorkloadGroup(self, WorkloadGroup):
        self._WorkloadGroup = WorkloadGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("WorkloadGroup") is not None:
            self._WorkloadGroup = WorkloadGroupConfig()
            self._WorkloadGroup._deserialize(params.get("WorkloadGroup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkloadGroupResponse(AbstractModel):
    """CreateWorkloadGroup response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DataBaseAuditRecord(AbstractModel):
    """Database audit

    """

    def __init__(self):
        r"""
        :param _OsUser: Query user
Note: This field may return null, indicating that no valid values can be obtained.
        :type OsUser: str
        :param _InitialQueryId: Query ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InitialQueryId: str
        :param _Sql: SQL statement
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sql: str
        :param _QueryStartTime: Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type QueryStartTime: str
        :param _DurationMs: Execution duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type DurationMs: int
        :param _ReadRows: The number of read rows
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReadRows: int
        :param _ResultRows: Total number of read bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultRows: int
        :param _ResultBytes: Result bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultBytes: int
        :param _MemoryUsage: Memory
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemoryUsage: int
        :param _InitialAddress: Initial query IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type InitialAddress: str
        :param _DbName: Database
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _SqlType: SQL type
Note: This field may return null, indicating that no valid values can be obtained.
        :type SqlType: str
        :param _Catalog: Catalog name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Catalog: str
        """
        self._OsUser = None
        self._InitialQueryId = None
        self._Sql = None
        self._QueryStartTime = None
        self._DurationMs = None
        self._ReadRows = None
        self._ResultRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._InitialAddress = None
        self._DbName = None
        self._SqlType = None
        self._Catalog = None

    @property
    def OsUser(self):
        """Query user
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OsUser

    @OsUser.setter
    def OsUser(self, OsUser):
        self._OsUser = OsUser

    @property
    def InitialQueryId(self):
        """Query ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InitialQueryId

    @InitialQueryId.setter
    def InitialQueryId(self, InitialQueryId):
        self._InitialQueryId = InitialQueryId

    @property
    def Sql(self):
        """SQL statement
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def QueryStartTime(self):
        """Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._QueryStartTime

    @QueryStartTime.setter
    def QueryStartTime(self, QueryStartTime):
        self._QueryStartTime = QueryStartTime

    @property
    def DurationMs(self):
        """Execution duration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def ReadRows(self):
        """The number of read rows
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultRows(self):
        """Total number of read bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ResultRows

    @ResultRows.setter
    def ResultRows(self, ResultRows):
        self._ResultRows = ResultRows

    @property
    def ResultBytes(self):
        """Result bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        """Memory
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def InitialAddress(self):
        """Initial query IP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InitialAddress

    @InitialAddress.setter
    def InitialAddress(self, InitialAddress):
        self._InitialAddress = InitialAddress

    @property
    def DbName(self):
        """Database
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SqlType(self):
        """SQL type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def Catalog(self):
        """Catalog name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog


    def _deserialize(self, params):
        self._OsUser = params.get("OsUser")
        self._InitialQueryId = params.get("InitialQueryId")
        self._Sql = params.get("Sql")
        self._QueryStartTime = params.get("QueryStartTime")
        self._DurationMs = params.get("DurationMs")
        self._ReadRows = params.get("ReadRows")
        self._ResultRows = params.get("ResultRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._InitialAddress = params.get("InitialAddress")
        self._DbName = params.get("DbName")
        self._SqlType = params.get("SqlType")
        self._Catalog = params.get("Catalog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePermissions(AbstractModel):
    """Database permission

    """

    def __init__(self):
        r"""
        :param _DatabaseName: Database name

Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param _Permissions: Permission name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Permissions: list of str
        """
        self._DatabaseName = None
        self._Permissions = None

    @property
    def DatabaseName(self):
        """Database name

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Permissions(self):
        """Permission name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._Permissions = params.get("Permissions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbInfo(AbstractModel):
    """Database information

    """

    def __init__(self):
        r"""
        :param _DbName: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _Properties: Database attribute
Note: This field may return null, indicating that no valid values can be obtained.
        :type Properties: list of Property
        :param _Location: Metadata address (Available when the data source is Hive or DLC.)

Note: This field may return null, indicating that no valid values can be obtained.
        :type Location: str
        """
        self._DbName = None
        self._Properties = None
        self._Location = None

    @property
    def DbName(self):
        """Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Properties(self):
        """Database attribute
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def Location(self):
        """Metadata address (Available when the data source is Hive or DLC.)

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbTablesInfo(AbstractModel):
    """Database and table information

    """

    def __init__(self):
        r"""
        :param _DbName: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _TablesName: The corresponding table list under this database.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TablesName: list of str
        """
        self._DbName = None
        self._TablesName = None

    @property
    def DbName(self):
        """Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TablesName(self):
        """The corresponding table list under this database.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._TablesName

    @TablesName.setter
    def TablesName(self, TablesName):
        self._TablesName = TablesName


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._TablesName = params.get("TablesName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackUpDataRequest(AbstractModel):
    """DeleteBackUpData request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _BackUpJobId: Task ID
        :type BackUpJobId: int
        :param _IsDeleteAll: Whether to delete all instances
        :type IsDeleteAll: bool
        """
        self._InstanceId = None
        self._BackUpJobId = None
        self._IsDeleteAll = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        """Task ID
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId

    @property
    def IsDeleteAll(self):
        """Whether to delete all instances
        :rtype: bool
        """
        return self._IsDeleteAll

    @IsDeleteAll.setter
    def IsDeleteAll(self, IsDeleteAll):
        self._IsDeleteAll = IsDeleteAll


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        self._IsDeleteAll = params.get("IsDeleteAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackUpDataResponse(AbstractModel):
    """DeleteBackUpData response structure.

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


class DeleteTableRequest(AbstractModel):
    """DeleteTable request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Resource ID, which is the TCHouse-D resource ID used for table creation.
        :type InstanceId: str
        :param _DbName: The name of the database where the table belongs needs to be deleted.
        :type DbName: str
        :param _TableName: Table name to be deleted
        :type TableName: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _IsForce: True: The system will not check whether there are unfinished transactions in the table. The table will be deleted directly and cannot be recovered. False: The deleted table can be recovered within a period of time (default value).
        :type IsForce: bool
        """
        self._InstanceId = None
        self._DbName = None
        self._TableName = None
        self._UserName = None
        self._PassWord = None
        self._IsForce = None

    @property
    def InstanceId(self):
        """Resource ID, which is the TCHouse-D resource ID used for table creation.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """The name of the database where the table belongs needs to be deleted.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableName(self):
        """Table name to be deleted
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def IsForce(self):
        """True: The system will not check whether there are unfinished transactions in the table. The table will be deleted directly and cannot be recovered. False: The deleted table can be recovered within a period of time (default value).
        :rtype: bool
        """
        return self._IsForce

    @IsForce.setter
    def IsForce(self, IsForce):
        self._IsForce = IsForce


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._TableName = params.get("TableName")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._IsForce = params.get("IsForce")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableResponse(AbstractModel):
    """DeleteTable response structure.

    """

    def __init__(self):
        r"""
        :param _Message: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Message = None
        self._RequestId = None

    @property
    def Message(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DeleteWorkloadGroupRequest(AbstractModel):
    """DeleteWorkloadGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _WorkloadGroupName: Resource group name to be deleted
        :type WorkloadGroupName: str
        """
        self._InstanceId = None
        self._WorkloadGroupName = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WorkloadGroupName(self):
        """Resource group name to be deleted
        :rtype: str
        """
        return self._WorkloadGroupName

    @WorkloadGroupName.setter
    def WorkloadGroupName(self, WorkloadGroupName):
        self._WorkloadGroupName = WorkloadGroupName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._WorkloadGroupName = params.get("WorkloadGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkloadGroupResponse(AbstractModel):
    """DeleteWorkloadGroup response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeAreaRegionRequest(AbstractModel):
    """DescribeAreaRegion request structure.

    """

    def __init__(self):
        r"""
        :param _IsInternationalSite: Whether it is an international site
        :type IsInternationalSite: bool
        """
        self._IsInternationalSite = None

    @property
    def IsInternationalSite(self):
        """Whether it is an international site
        :rtype: bool
        """
        return self._IsInternationalSite

    @IsInternationalSite.setter
    def IsInternationalSite(self, IsInternationalSite):
        self._IsInternationalSite = IsInternationalSite


    def _deserialize(self, params):
        self._IsInternationalSite = params.get("IsInternationalSite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAreaRegionResponse(AbstractModel):
    """DescribeAreaRegion response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Region list
        :type Items: list of RegionAreaInfo
        :param _FrontEndRules: Front-end rule description
Note: This field may return null, indicating that no valid values can be obtained.
        :type FrontEndRules: list of FrontEndRule
        :param _AvailableWhiteListNames: Return available allowlist names
Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailableWhiteListNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._FrontEndRules = None
        self._AvailableWhiteListNames = None
        self._RequestId = None

    @property
    def Items(self):
        """Region list
        :rtype: list of RegionAreaInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def FrontEndRules(self):
        """Front-end rule description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of FrontEndRule
        """
        return self._FrontEndRules

    @FrontEndRules.setter
    def FrontEndRules(self, FrontEndRules):
        self._FrontEndRules = FrontEndRules

    @property
    def AvailableWhiteListNames(self):
        """Return available allowlist names
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AvailableWhiteListNames

    @AvailableWhiteListNames.setter
    def AvailableWhiteListNames(self, AvailableWhiteListNames):
        self._AvailableWhiteListNames = AvailableWhiteListNames

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RegionAreaInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("FrontEndRules") is not None:
            self._FrontEndRules = []
            for item in params.get("FrontEndRules"):
                obj = FrontEndRule()
                obj._deserialize(item)
                self._FrontEndRules.append(obj)
        self._AvailableWhiteListNames = params.get("AvailableWhiteListNames")
        self._RequestId = params.get("RequestId")


class DescribeBackUpJobDetailRequest(AbstractModel):
    """DescribeBackUpJobDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _BackUpJobId: Task ID
        :type BackUpJobId: int
        """
        self._InstanceId = None
        self._BackUpJobId = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        """Task ID
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpJobDetailResponse(AbstractModel):
    """DescribeBackUpJobDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TableContents: Backup table details
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableContents: list of BackupTableContent
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TableContents = None
        self._RequestId = None

    @property
    def TableContents(self):
        """Backup table details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BackupTableContent
        """
        return self._TableContents

    @TableContents.setter
    def TableContents(self, TableContents):
        self._TableContents = TableContents

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
        if params.get("TableContents") is not None:
            self._TableContents = []
            for item in params.get("TableContents"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self._TableContents.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackUpJobRequest(AbstractModel):
    """DescribeBackUpJob request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _PageSize: Pagination size
        :type PageSize: int
        :param _PageNum: Page number
        :type PageNum: int
        :param _BeginTime: Start time
        :type BeginTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _JobIdFiltersStr: String type of jobid
        :type JobIdFiltersStr: str
        """
        self._InstanceId = None
        self._PageSize = None
        self._PageNum = None
        self._BeginTime = None
        self._EndTime = None
        self._JobIdFiltersStr = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PageSize(self):
        """Pagination size
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        """Page number
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def BeginTime(self):
        """Start time
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def JobIdFiltersStr(self):
        """String type of jobid
        :rtype: str
        """
        return self._JobIdFiltersStr

    @JobIdFiltersStr.setter
    def JobIdFiltersStr(self, JobIdFiltersStr):
        self._JobIdFiltersStr = JobIdFiltersStr


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._JobIdFiltersStr = params.get("JobIdFiltersStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpJobResponse(AbstractModel):
    """DescribeBackUpJob response structure.

    """

    def __init__(self):
        r"""
        :param _BackUpJobs: Task list
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackUpJobs: list of BackUpJobDisplay
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackUpJobs = None
        self._RequestId = None

    @property
    def BackUpJobs(self):
        """Task list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BackUpJobDisplay
        """
        return self._BackUpJobs

    @BackUpJobs.setter
    def BackUpJobs(self, BackUpJobs):
        self._BackUpJobs = BackUpJobs

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
        if params.get("BackUpJobs") is not None:
            self._BackUpJobs = []
            for item in params.get("BackUpJobs"):
                obj = BackUpJobDisplay()
                obj._deserialize(item)
                self._BackUpJobs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackUpSchedulesRequest(AbstractModel):
    """DescribeBackUpSchedules request structure.

    """


class DescribeBackUpSchedulesResponse(AbstractModel):
    """DescribeBackUpSchedules response structure.

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


class DescribeBackUpTablesRequest(AbstractModel):
    """DescribeBackUpTables request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _BackupType: It is 0 by default. It is 1 when a one-time backup of the remote doris is performed. It is 2 when one-time COS recovery is performed.
        :type BackupType: int
        :param _DorisSourceInfo: Connection information of the remote doris cluster
        :type DorisSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        :param _CosSourceInfo: COS information
        :type CosSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        """
        self._InstanceId = None
        self._BackupType = None
        self._DorisSourceInfo = None
        self._CosSourceInfo = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupType(self):
        """It is 0 by default. It is 1 when a one-time backup of the remote doris is performed. It is 2 when one-time COS recovery is performed.
        :rtype: int
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def DorisSourceInfo(self):
        """Connection information of the remote doris cluster
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DorisSourceInfo`
        """
        return self._DorisSourceInfo

    @DorisSourceInfo.setter
    def DorisSourceInfo(self, DorisSourceInfo):
        self._DorisSourceInfo = DorisSourceInfo

    @property
    def CosSourceInfo(self):
        """COS information
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        """
        return self._CosSourceInfo

    @CosSourceInfo.setter
    def CosSourceInfo(self, CosSourceInfo):
        self._CosSourceInfo = CosSourceInfo


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupType = params.get("BackupType")
        if params.get("DorisSourceInfo") is not None:
            self._DorisSourceInfo = DorisSourceInfo()
            self._DorisSourceInfo._deserialize(params.get("DorisSourceInfo"))
        if params.get("CosSourceInfo") is not None:
            self._CosSourceInfo = CosSourceInfo()
            self._CosSourceInfo._deserialize(params.get("CosSourceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpTablesResponse(AbstractModel):
    """DescribeBackUpTables response structure.

    """

    def __init__(self):
        r"""
        :param _AvailableTables: List of tables available for backup
        :type AvailableTables: list of BackupTableContent
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AvailableTables = None
        self._RequestId = None

    @property
    def AvailableTables(self):
        """List of tables available for backup
        :rtype: list of BackupTableContent
        """
        return self._AvailableTables

    @AvailableTables.setter
    def AvailableTables(self, AvailableTables):
        self._AvailableTables = AvailableTables

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
        if params.get("AvailableTables") is not None:
            self._AvailableTables = []
            for item in params.get("AvailableTables"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self._AvailableTables.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackUpTaskDetailRequest(AbstractModel):
    """DescribeBackUpTaskDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _BackUpJobId: Task ID
        :type BackUpJobId: int
        """
        self._InstanceId = None
        self._BackUpJobId = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        """Task ID
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackUpTaskDetailResponse(AbstractModel):
    """DescribeBackUpTaskDetail response structure.

    """

    def __init__(self):
        r"""
        :param _BackupStatus: Progress details of the backup task
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupStatus: list of BackupStatus
        :param _ErrorMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupStatus = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def BackupStatus(self):
        """Progress details of the backup task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BackupStatus
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def ErrorMsg(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("BackupStatus") is not None:
            self._BackupStatus = []
            for item in params.get("BackupStatus"):
                obj = BackupStatus()
                obj._deserialize(item)
                self._BackupStatus.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeClusterConfigsHistoryRequest(AbstractModel):
    """DescribeClusterConfigsHistory request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _Offset: Pagination parameters. The first page is 0, and the second page is 10.
        :type Offset: int
        :param _Limit: Pagination parameters. The pagination step length is 10 by default.
        :type Limit: int
        :param _StartTime: Start of the time range for configuration modification history
        :type StartTime: str
        :param _EndTime: End of the time range for configuration modification history
        :type EndTime: str
        :param _ConfigFileNames: Configuration file name array to be queried. If it is empty, all historical records will be queried. Currently supported configuration file names are as follows:
apache_hdfs_broker.conf; be.conf; fe.conf; core-site.xml; hdfs-site.xml; odbcinst.ini
        :type ConfigFileNames: list of str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None
        self._ConfigFileNames = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """Pagination parameters. The first page is 0, and the second page is 10.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameters. The pagination step length is 10 by default.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        """Start of the time range for configuration modification history
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End of the time range for configuration modification history
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ConfigFileNames(self):
        """Configuration file name array to be queried. If it is empty, all historical records will be queried. Currently supported configuration file names are as follows:
apache_hdfs_broker.conf; be.conf; fe.conf; core-site.xml; hdfs-site.xml; odbcinst.ini
        :rtype: list of str
        """
        return self._ConfigFileNames

    @ConfigFileNames.setter
    def ConfigFileNames(self, ConfigFileNames):
        self._ConfigFileNames = ConfigFileNames


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ConfigFileNames = params.get("ConfigFileNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterConfigsHistoryResponse(AbstractModel):
    """DescribeClusterConfigsHistory response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances
        :type TotalCount: int
        :param _ClusterConfHistory: Modification history of the configuration file
        :type ClusterConfHistory: list of ClusterConfigsHistory
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterConfHistory = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterConfHistory(self):
        """Modification history of the configuration file
        :rtype: list of ClusterConfigsHistory
        """
        return self._ClusterConfHistory

    @ClusterConfHistory.setter
    def ClusterConfHistory(self, ClusterConfHistory):
        self._ClusterConfHistory = ClusterConfHistory

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
        if params.get("ClusterConfHistory") is not None:
            self._ClusterConfHistory = []
            for item in params.get("ClusterConfHistory"):
                obj = ClusterConfigsHistory()
                obj._deserialize(item)
                self._ClusterConfHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterConfigsRequest(AbstractModel):
    """DescribeClusterConfigs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        :param _ConfigType: 0 indicates public cloud query, and 1 Qinge query. Qinge query shows all that needs to be displayed.
        :type ConfigType: int
        :param _FileName: Search for files with fuzzy keywords
        :type FileName: str
        :param _ClusterConfigType: 0 indicates cluster dimension and 1 node dimension
        :type ClusterConfigType: int
        :param _IPAddress: eth0's IP address
        :type IPAddress: str
        """
        self._InstanceId = None
        self._ConfigType = None
        self._FileName = None
        self._ClusterConfigType = None
        self._IPAddress = None

    @property
    def InstanceId(self):
        """Cluster instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigType(self):
        """0 indicates public cloud query, and 1 Qinge query. Qinge query shows all that needs to be displayed.
        :rtype: int
        """
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType

    @property
    def FileName(self):
        """Search for files with fuzzy keywords
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ClusterConfigType(self):
        """0 indicates cluster dimension and 1 node dimension
        :rtype: int
        """
        return self._ClusterConfigType

    @ClusterConfigType.setter
    def ClusterConfigType(self, ClusterConfigType):
        self._ClusterConfigType = ClusterConfigType

    @property
    def IPAddress(self):
        """eth0's IP address
        :rtype: str
        """
        return self._IPAddress

    @IPAddress.setter
    def IPAddress(self, IPAddress):
        self._IPAddress = IPAddress


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConfigType = params.get("ConfigType")
        self._FileName = params.get("FileName")
        self._ClusterConfigType = params.get("ClusterConfigType")
        self._IPAddress = params.get("IPAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterConfigsResponse(AbstractModel):
    """DescribeClusterConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterConfList: Return information about the instance's configuration file.
        :type ClusterConfList: list of ClusterConfigsInfoFromEMR
        :param _BuildVersion: Return the current kernel version. If it does not exist, a null character string is returned.
        :type BuildVersion: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterConfList = None
        self._BuildVersion = None
        self._RequestId = None

    @property
    def ClusterConfList(self):
        """Return information about the instance's configuration file.
        :rtype: list of ClusterConfigsInfoFromEMR
        """
        return self._ClusterConfList

    @ClusterConfList.setter
    def ClusterConfList(self, ClusterConfList):
        self._ClusterConfList = ClusterConfList

    @property
    def BuildVersion(self):
        """Return the current kernel version. If it does not exist, a null character string is returned.
        :rtype: str
        """
        return self._BuildVersion

    @BuildVersion.setter
    def BuildVersion(self, BuildVersion):
        self._BuildVersion = BuildVersion

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
        if params.get("ClusterConfList") is not None:
            self._ClusterConfList = []
            for item in params.get("ClusterConfList"):
                obj = ClusterConfigsInfoFromEMR()
                obj._deserialize(item)
                self._ClusterConfList.append(obj)
        self._BuildVersion = params.get("BuildVersion")
        self._RequestId = params.get("RequestId")


class DescribeCoolDownBackendsRequest(AbstractModel):
    """DescribeCoolDownBackends request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster ID
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
        


class DescribeCoolDownBackendsResponse(AbstractModel):
    """DescribeCoolDownBackends response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _List: Node information list

Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of CoolDownBackend
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._List = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def List(self):
        """Node information list

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CoolDownBackend
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CoolDownBackend()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCoolDownPoliciesRequest(AbstractModel):
    """DescribeCoolDownPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster ID
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
        


class DescribeCoolDownPoliciesResponse(AbstractModel):
    """DescribeCoolDownPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _List: List of hot/cold data layering policies
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of CoolDownPolicyInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._List = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def List(self):
        """List of hot/cold data layering policies
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CoolDownPolicyInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CoolDownPolicyInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCoolDownTableDataRequest(AbstractModel):
    """DescribeCoolDownTableData request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _DatabaseName: Database name
        :type DatabaseName: str
        """
        self._InstanceId = None
        self._DatabaseName = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DatabaseName(self):
        """Database name
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCoolDownTableDataResponse(AbstractModel):
    """DescribeCoolDownTableData response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _List: List of tables containing layered hot and cold data
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of CoolDownTableDataInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._List = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def List(self):
        """List of tables containing layered hot and cold data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CoolDownTableDataInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CoolDownTableDataInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCreateTablesDDLRequest(AbstractModel):
    """DescribeCreateTablesDDL request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Resource ID, TCHouse-D resource ID.
        :type InstanceId: str
        :param _DbTablesInfos: Require the database and table for the table creation DDL.
        :type DbTablesInfos: list of DbTablesInfo
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _IsBrief: Whether to hide partition information
        :type IsBrief: bool
        """
        self._InstanceId = None
        self._DbTablesInfos = None
        self._UserName = None
        self._PassWord = None
        self._IsBrief = None

    @property
    def InstanceId(self):
        """Resource ID, TCHouse-D resource ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbTablesInfos(self):
        """Require the database and table for the table creation DDL.
        :rtype: list of DbTablesInfo
        """
        return self._DbTablesInfos

    @DbTablesInfos.setter
    def DbTablesInfos(self, DbTablesInfos):
        self._DbTablesInfos = DbTablesInfos

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def IsBrief(self):
        """Whether to hide partition information
        :rtype: bool
        """
        return self._IsBrief

    @IsBrief.setter
    def IsBrief(self, IsBrief):
        self._IsBrief = IsBrief


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DbTablesInfos") is not None:
            self._DbTablesInfos = []
            for item in params.get("DbTablesInfos"):
                obj = DbTablesInfo()
                obj._deserialize(item)
                self._DbTablesInfos.append(obj)
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._IsBrief = params.get("IsBrief")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCreateTablesDDLResponse(AbstractModel):
    """DescribeCreateTablesDDL response structure.

    """

    def __init__(self):
        r"""
        :param _CreateTablesDDLs: DDL information for creating a table
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTablesDDLs: list of CreateTablesDDL
        :param _Message: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CreateTablesDDLs = None
        self._Message = None
        self._RequestId = None

    @property
    def CreateTablesDDLs(self):
        """DDL information for creating a table
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CreateTablesDDL
        """
        return self._CreateTablesDDLs

    @CreateTablesDDLs.setter
    def CreateTablesDDLs(self, CreateTablesDDLs):
        self._CreateTablesDDLs = CreateTablesDDLs

    @property
    def Message(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        if params.get("CreateTablesDDLs") is not None:
            self._CreateTablesDDLs = []
            for item in params.get("CreateTablesDDLs"):
                obj = CreateTablesDDL()
                obj._deserialize(item)
                self._CreateTablesDDLs.append(obj)
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseAuditDownloadRequest(AbstractModel):
    """DescribeDatabaseAuditDownload request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Paging
        :type PageSize: int
        :param _PageNum: Paging
        :type PageNum: int
        :param _OrderType: Sort parameters
        :type OrderType: str
        :param _User: User
        :type User: str
        :param _DbName: Database
        :type DbName: str
        :param _SqlType: SQL type
        :type SqlType: str
        :param _Sql: SQL statement
        :type Sql: str
        :param _Users: Users (multiple selections)
        :type Users: list of str
        :param _DbNames: Databases (multiple selections)
        :type DbNames: list of str
        :param _SqlTypes: SQL types (multiple selections)
        :type SqlTypes: list of str
        :param _Catalogs: Catalog names (multiple selections)
        :type Catalogs: list of str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNum = None
        self._OrderType = None
        self._User = None
        self._DbName = None
        self._SqlType = None
        self._Sql = None
        self._Users = None
        self._DbNames = None
        self._SqlTypes = None
        self._Catalogs = None

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
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Paging
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        """Paging
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def OrderType(self):
        """Sort parameters
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def User(self):
        """User
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DbName(self):
        """Database
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SqlType(self):
        """SQL type
        :rtype: str
        """
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def Sql(self):
        """SQL statement
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Users(self):
        """Users (multiple selections)
        :rtype: list of str
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def DbNames(self):
        """Databases (multiple selections)
        :rtype: list of str
        """
        return self._DbNames

    @DbNames.setter
    def DbNames(self, DbNames):
        self._DbNames = DbNames

    @property
    def SqlTypes(self):
        """SQL types (multiple selections)
        :rtype: list of str
        """
        return self._SqlTypes

    @SqlTypes.setter
    def SqlTypes(self, SqlTypes):
        self._SqlTypes = SqlTypes

    @property
    def Catalogs(self):
        """Catalog names (multiple selections)
        :rtype: list of str
        """
        return self._Catalogs

    @Catalogs.setter
    def Catalogs(self, Catalogs):
        self._Catalogs = Catalogs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._OrderType = params.get("OrderType")
        self._User = params.get("User")
        self._DbName = params.get("DbName")
        self._SqlType = params.get("SqlType")
        self._Sql = params.get("Sql")
        self._Users = params.get("Users")
        self._DbNames = params.get("DbNames")
        self._SqlTypes = params.get("SqlTypes")
        self._Catalogs = params.get("Catalogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseAuditDownloadResponse(AbstractModel):
    """DescribeDatabaseAuditDownload response structure.

    """

    def __init__(self):
        r"""
        :param _CosUrl: The cos address of the log
        :type CosUrl: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CosUrl = None
        self._RequestId = None

    @property
    def CosUrl(self):
        """The cos address of the log
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

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
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseAuditRecordsRequest(AbstractModel):
    """DescribeDatabaseAuditRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Paging
        :type PageSize: int
        :param _PageNum: Paging
        :type PageNum: int
        :param _OrderType: Sort parameters
        :type OrderType: str
        :param _User: User
        :type User: str
        :param _DbName: Database
        :type DbName: str
        :param _SqlType: SQL type
        :type SqlType: str
        :param _Sql: SQL statement
        :type Sql: str
        :param _Users: Users (multiple selections)
        :type Users: list of str
        :param _DbNames: Databases (multiple selections)
        :type DbNames: list of str
        :param _SqlTypes: SQL types (multiple selections)
        :type SqlTypes: list of str
        :param _Catalogs: Catalog names (multiple selections)
        :type Catalogs: list of str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNum = None
        self._OrderType = None
        self._User = None
        self._DbName = None
        self._SqlType = None
        self._Sql = None
        self._Users = None
        self._DbNames = None
        self._SqlTypes = None
        self._Catalogs = None

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
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Paging
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        """Paging
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def OrderType(self):
        """Sort parameters
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def User(self):
        """User
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DbName(self):
        """Database
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SqlType(self):
        """SQL type
        :rtype: str
        """
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def Sql(self):
        """SQL statement
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Users(self):
        """Users (multiple selections)
        :rtype: list of str
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def DbNames(self):
        """Databases (multiple selections)
        :rtype: list of str
        """
        return self._DbNames

    @DbNames.setter
    def DbNames(self, DbNames):
        self._DbNames = DbNames

    @property
    def SqlTypes(self):
        """SQL types (multiple selections)
        :rtype: list of str
        """
        return self._SqlTypes

    @SqlTypes.setter
    def SqlTypes(self, SqlTypes):
        self._SqlTypes = SqlTypes

    @property
    def Catalogs(self):
        """Catalog names (multiple selections)
        :rtype: list of str
        """
        return self._Catalogs

    @Catalogs.setter
    def Catalogs(self, Catalogs):
        self._Catalogs = Catalogs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._OrderType = params.get("OrderType")
        self._User = params.get("User")
        self._DbName = params.get("DbName")
        self._SqlType = params.get("SqlType")
        self._Sql = params.get("Sql")
        self._Users = params.get("Users")
        self._DbNames = params.get("DbNames")
        self._SqlTypes = params.get("SqlTypes")
        self._Catalogs = params.get("Catalogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseAuditRecordsResponse(AbstractModel):
    """DescribeDatabaseAuditRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total
        :type TotalCount: int
        :param _SlowQueryRecords: Record list
        :type SlowQueryRecords: :class:`tencentcloud.cdwdoris.v20211228.models.DataBaseAuditRecord`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowQueryRecords = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowQueryRecords(self):
        """Record list
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DataBaseAuditRecord`
        """
        return self._SlowQueryRecords

    @SlowQueryRecords.setter
    def SlowQueryRecords(self, SlowQueryRecords):
        self._SlowQueryRecords = SlowQueryRecords

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
        if params.get("SlowQueryRecords") is not None:
            self._SlowQueryRecords = DataBaseAuditRecord()
            self._SlowQueryRecords._deserialize(params.get("SlowQueryRecords"))
        self._RequestId = params.get("RequestId")


class DescribeDatabaseRequest(AbstractModel):
    """DescribeDatabase request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Resource ID, which is the TCHouse-D resource ID used for table creation.
        :type InstanceId: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _CatalogName: Query the data source where the database is located. If it is not filled in, the internal data source (internal) will be used by default.
        :type CatalogName: str
        :param _DbNames: The database information to be queried. If this parameter and FilterDbName are not filled in, all database information of the current data source will be queried by default.
        :type DbNames: list of str
        :param _FilterDbName: Display the filtered database information. For example, %infor indicates database names ending with infor. This parameter only supports scenarios where CatalogName is internal.
        :type FilterDbName: str
        """
        self._InstanceId = None
        self._UserName = None
        self._PassWord = None
        self._CatalogName = None
        self._DbNames = None
        self._FilterDbName = None

    @property
    def InstanceId(self):
        """Resource ID, which is the TCHouse-D resource ID used for table creation.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def CatalogName(self):
        """Query the data source where the database is located. If it is not filled in, the internal data source (internal) will be used by default.
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def DbNames(self):
        """The database information to be queried. If this parameter and FilterDbName are not filled in, all database information of the current data source will be queried by default.
        :rtype: list of str
        """
        return self._DbNames

    @DbNames.setter
    def DbNames(self, DbNames):
        self._DbNames = DbNames

    @property
    def FilterDbName(self):
        """Display the filtered database information. For example, %infor indicates database names ending with infor. This parameter only supports scenarios where CatalogName is internal.
        :rtype: str
        """
        return self._FilterDbName

    @FilterDbName.setter
    def FilterDbName(self, FilterDbName):
        self._FilterDbName = FilterDbName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._CatalogName = params.get("CatalogName")
        self._DbNames = params.get("DbNames")
        self._FilterDbName = params.get("FilterDbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseResponse(AbstractModel):
    """DescribeDatabase response structure.

    """

    def __init__(self):
        r"""
        :param _DbInfos: Database information
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbInfos: list of DbInfo
        :param _Message: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DbInfos = None
        self._Message = None
        self._RequestId = None

    @property
    def DbInfos(self):
        """Database information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DbInfo
        """
        return self._DbInfos

    @DbInfos.setter
    def DbInfos(self, DbInfos):
        self._DbInfos = DbInfos

    @property
    def Message(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        if params.get("DbInfos") is not None:
            self._DbInfos = []
            for item in params.get("DbInfos"):
                obj = DbInfo()
                obj._deserialize(item)
                self._DbInfos.append(obj)
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesInfoRequest(AbstractModel):
    """DescribeInstanceNodesInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceID: Cluster ID
        :type InstanceID: str
        """
        self._InstanceID = None

    @property
    def InstanceID(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesInfoResponse(AbstractModel):
    """DescribeInstanceNodesInfo response structure.

    """

    def __init__(self):
        r"""
        :param _BeNodes: Be node
Note: This field may return null, indicating that no valid values can be obtained.
        :type BeNodes: list of str
        :param _FeNodes: Fe node
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeNodes: list of str
        :param _FeMaster: Fe master node
        :type FeMaster: str
        :param _BeNodeInfos: Be node information
Note: This field may return null, indicating that no valid values can be obtained.
        :type BeNodeInfos: list of NodeInfo
        :param _FeNodeInfos: Fe node information
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeNodeInfos: list of NodeInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BeNodes = None
        self._FeNodes = None
        self._FeMaster = None
        self._BeNodeInfos = None
        self._FeNodeInfos = None
        self._RequestId = None

    @property
    def BeNodes(self):
        """Be node
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._BeNodes

    @BeNodes.setter
    def BeNodes(self, BeNodes):
        self._BeNodes = BeNodes

    @property
    def FeNodes(self):
        """Fe node
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._FeNodes

    @FeNodes.setter
    def FeNodes(self, FeNodes):
        self._FeNodes = FeNodes

    @property
    def FeMaster(self):
        """Fe master node
        :rtype: str
        """
        return self._FeMaster

    @FeMaster.setter
    def FeMaster(self, FeMaster):
        self._FeMaster = FeMaster

    @property
    def BeNodeInfos(self):
        """Be node information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of NodeInfo
        """
        return self._BeNodeInfos

    @BeNodeInfos.setter
    def BeNodeInfos(self, BeNodeInfos):
        self._BeNodeInfos = BeNodeInfos

    @property
    def FeNodeInfos(self):
        """Fe node information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of NodeInfo
        """
        return self._FeNodeInfos

    @FeNodeInfos.setter
    def FeNodeInfos(self, FeNodeInfos):
        self._FeNodeInfos = FeNodeInfos

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
        self._BeNodes = params.get("BeNodes")
        self._FeNodes = params.get("FeNodes")
        self._FeMaster = params.get("FeMaster")
        if params.get("BeNodeInfos") is not None:
            self._BeNodeInfos = []
            for item in params.get("BeNodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._BeNodeInfos.append(obj)
        if params.get("FeNodeInfos") is not None:
            self._FeNodeInfos = []
            for item in params.get("FeNodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._FeNodeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesRequest(AbstractModel):
    """DescribeInstanceNodes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        :param _NodeRole: Cluster role type, defaulted as "data node".
        :type NodeRole: str
        :param _Offset: Pagination parameters. The first page is 0, and the second page is 10.
        :type Offset: int
        :param _Limit: Pagination parameters. The pagination step length is 10 by default.
        :type Limit: int
        :param _DisplayPolicy: Display policy, and all items are displayed when All is selected.
        :type DisplayPolicy: str
        """
        self._InstanceId = None
        self._NodeRole = None
        self._Offset = None
        self._Limit = None
        self._DisplayPolicy = None

    @property
    def InstanceId(self):
        """Cluster instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeRole(self):
        """Cluster role type, defaulted as "data node".
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def Offset(self):
        """Pagination parameters. The first page is 0, and the second page is 10.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameters. The pagination step length is 10 by default.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DisplayPolicy(self):
        """Display policy, and all items are displayed when All is selected.
        :rtype: str
        """
        return self._DisplayPolicy

    @DisplayPolicy.setter
    def DisplayPolicy(self, DisplayPolicy):
        self._DisplayPolicy = DisplayPolicy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeRole = params.get("NodeRole")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DisplayPolicy = params.get("DisplayPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesResponse(AbstractModel):
    """DescribeInstanceNodes response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _InstanceNodesList: Total number of instance nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceNodesList: list of InstanceNode
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceNodesList = None
        self._RequestId = None

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
    def InstanceNodesList(self):
        """Total number of instance nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceNode
        """
        return self._InstanceNodesList

    @InstanceNodesList.setter
    def InstanceNodesList(self, InstanceNodesList):
        self._InstanceNodesList = InstanceNodesList

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
        if params.get("InstanceNodesList") is not None:
            self._InstanceNodesList = []
            for item in params.get("InstanceNodesList"):
                obj = InstanceNode()
                obj._deserialize(item)
                self._InstanceNodesList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesRoleRequest(AbstractModel):
    """DescribeInstanceNodesRole request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _IpFilter: Filter IP addresses
        :type IpFilter: str
        """
        self._InstanceId = None
        self._IpFilter = None

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
    def IpFilter(self):
        """Filter IP addresses
        :rtype: str
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IpFilter = params.get("IpFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesRoleResponse(AbstractModel):
    """DescribeInstanceNodesRole response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error code
        :type ErrorMsg: str
        :param _TotalCount: Total number of nodes
        :type TotalCount: int
        :param _NodeInfos: None
        :type NodeInfos: list of NodeInfos
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._TotalCount = None
        self._NodeInfos = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error code
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def TotalCount(self):
        """Total number of nodes
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeInfos(self):
        """None
        :rtype: list of NodeInfos
        """
        return self._NodeInfos

    @NodeInfos.setter
    def NodeInfos(self, NodeInfos):
        self._NodeInfos = NodeInfos

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._TotalCount = params.get("TotalCount")
        if params.get("NodeInfos") is not None:
            self._NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfos()
                obj._deserialize(item)
                self._NodeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceOperationHistoryRequest(AbstractModel):
    """DescribeInstanceOperationHistory request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _PageNum: Page number, which is 1 by default.
        :type PageNum: int
        :param _PageSize: Number of records per page, which is 10 by default.
        :type PageSize: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        """
        self._InstanceId = None
        self._PageNum = None
        self._PageSize = None
        self._StartTime = None
        self._EndTime = None
        self._UserName = None
        self._PassWord = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PageNum(self):
        """Page number, which is 1 by default.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Number of records per page, which is 10 by default.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceOperationHistoryResponse(AbstractModel):
    """DescribeInstanceOperationHistory response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of operation records
        :type TotalCount: int
        :param _Operations: Specific data of operation records
        :type Operations: list of InstanceOperation
        :param _Message: Error message
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Operations = None
        self._Message = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of operation records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Operations(self):
        """Specific data of operation records
        :rtype: list of InstanceOperation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

    @property
    def Message(self):
        """Error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = InstanceOperation()
                obj._deserialize(item)
                self._Operations.append(obj)
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    """DescribeInstanceOperations request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: 
        :type InstanceId: str
        :param _Offset: 
        :type Offset: int
        :param _Limit: 
        :type Limit: int
        :param _StartTime: 
        :type StartTime: str
        :param _EndTime: 
        :type EndTime: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None

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
    def Offset(self):
        """
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

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
    def EndTime(self):
        """
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: 
        :type TotalCount: int
        :param _Operations: Note: This field may return null, indicating that no valid values can be obtained.
        :type Operations: list of InstanceOperation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Operations = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Operations(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceOperation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

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
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = InstanceOperation()
                obj._deserialize(item)
                self._Operations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster instance ID
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
        


class DescribeInstanceResponse(AbstractModel):
    """DescribeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceInfo: Instance description information
        :type InstanceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceInfo = None
        self._RequestId = None

    @property
    def InstanceInfo(self):
        """Instance description information
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceInfo`
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

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
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceStateRequest(AbstractModel):
    """DescribeInstanceState request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance name
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster instance name
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
        


class DescribeInstanceStateResponse(AbstractModel):
    """DescribeInstanceState response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceState: Cluster status. Example: Serving
        :type InstanceState: str
        :param _FlowCreateTime: Creation time of cluster operation
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowCreateTime: str
        :param _FlowName: Cluster operation name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowName: str
        :param _FlowProgress: Cluster operation progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowProgress: float
        :param _InstanceStateDesc: Cluster status description. Example: running
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceStateDesc: str
        :param _FlowMsg: Cluster process error messages, such as "Creation failed, insufficient resources"
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._RequestId = None

    @property
    def InstanceState(self):
        """Cluster status. Example: Serving
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        """Creation time of cluster operation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        """Cluster operation name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        """Cluster operation progress
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        """Cluster status description. Example: running
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        """Cluster process error messages, such as "Creation failed, insufficient resources"
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

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
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceUsedSubnetsRequest(AbstractModel):
    """DescribeInstanceUsedSubnets request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster ID
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
        


class DescribeInstanceUsedSubnetsResponse(AbstractModel):
    """DescribeInstanceUsedSubnets response structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC information used by the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _UsedSubnets: Subnet information used by the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsedSubnets: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VpcId = None
        self._UsedSubnets = None
        self._RequestId = None

    @property
    def VpcId(self):
        """VPC information used by the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UsedSubnets(self):
        """Subnet information used by the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._UsedSubnets

    @UsedSubnets.setter
    def UsedSubnets(self, UsedSubnets):
        self._UsedSubnets = UsedSubnets

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
        self._VpcId = params.get("VpcId")
        self._UsedSubnets = params.get("UsedSubnets")
        self._RequestId = params.get("RequestId")


class DescribeInstancesHealthStateRequest(AbstractModel):
    """DescribeInstancesHealthState request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceID: Cluster ID
        :type InstanceID: str
        :param _Input: If this parameter is left blank, all clusters corresponding to the current appId are involved. Otherwise, a specific cluster is involved.
        :type Input: str
        """
        self._InstanceID = None
        self._Input = None

    @property
    def InstanceID(self):
        warnings.warn("parameter `InstanceID` is deprecated", DeprecationWarning) 

        """Cluster ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        warnings.warn("parameter `InstanceID` is deprecated", DeprecationWarning) 

        self._InstanceID = InstanceID

    @property
    def Input(self):
        """If this parameter is left blank, all clusters corresponding to the current appId are involved. Otherwise, a specific cluster is involved.
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Input = params.get("Input")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesHealthStateResponse(AbstractModel):
    """DescribeInstancesHealthState response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Base64-encoded data, which contains the cluster health information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Base64-encoded data, which contains the cluster health information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: The name of the cluster ID for the search
        :type SearchInstanceId: str
        :param _SearchInstanceName: The cluster name for the search
        :type SearchInstanceName: str
        :param _Offset: Pagination parameters. The first page is 0, and the second page is 10.
        :type Offset: int
        :param _Limit: Pagination parameters. The pagination step length is 10 by default.
        :type Limit: int
        :param _SearchTags: Search tag list
        :type SearchTags: list of SearchTags
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None

    @property
    def SearchInstanceId(self):
        """The name of the cluster ID for the search
        :rtype: str
        """
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        """The cluster name for the search
        :rtype: str
        """
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        """Pagination parameters. The first page is 0, and the second page is 10.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameters. The pagination step length is 10 by default.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchTags(self):
        """Search tag list
        :rtype: list of SearchTags
        """
        return self._SearchTags

    @SearchTags.setter
    def SearchTags(self, SearchTags):
        self._SearchTags = SearchTags


    def _deserialize(self, params):
        self._SearchInstanceId = params.get("SearchInstanceId")
        self._SearchInstanceName = params.get("SearchInstanceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("SearchTags") is not None:
            self._SearchTags = []
            for item in params.get("SearchTags"):
                obj = SearchTags()
                obj._deserialize(item)
                self._SearchTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total Number of Instances
        :type TotalCount: int
        :param _InstancesList: Quantities of instances array
        :type InstancesList: list of InstanceInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstancesList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total Number of Instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        """Quantities of instances array
        :rtype: list of InstanceInfo
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

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
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeQueryAnalyseRequest(AbstractModel):
    """DescribeQueryAnalyse request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _StartTime: Start time of operation period
        :type StartTime: str
        :param _EndTime: End time of operation period.
        :type EndTime: str
        :param _SQLFragment: SQL fragments (fuzzy query supported)
        :type SQLFragment: str
        :param _CatalogFilter: Catalog filter condition
        :type CatalogFilter: str
        :param _DatabaseFilter: Database name filter condition
        :type DatabaseFilter: str
        :param _SQLTypeFilter: SQL type filter criteria
        :type SQLTypeFilter: str
        :param _SortField: Sorting field
        :type SortField: str
        :param _SortOrder: Sorting order: asc (ascending) or desc (descending)
        :type SortOrder: str
        :param _QueryTime: Minimum query execution time, in milliseconds.
        :type QueryTime: int
        :param _PageNum: Page number, defaults to 1.
        :type PageNum: int
        :param _PageSize: Number of records per page, defaults to 10.
        :type PageSize: int
        """
        self._InstanceId = None
        self._UserName = None
        self._PassWord = None
        self._StartTime = None
        self._EndTime = None
        self._SQLFragment = None
        self._CatalogFilter = None
        self._DatabaseFilter = None
        self._SQLTypeFilter = None
        self._SortField = None
        self._SortOrder = None
        self._QueryTime = None
        self._PageNum = None
        self._PageSize = None

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
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def StartTime(self):
        """Start time of operation period
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of operation period.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SQLFragment(self):
        """SQL fragments (fuzzy query supported)
        :rtype: str
        """
        return self._SQLFragment

    @SQLFragment.setter
    def SQLFragment(self, SQLFragment):
        self._SQLFragment = SQLFragment

    @property
    def CatalogFilter(self):
        """Catalog filter condition
        :rtype: str
        """
        return self._CatalogFilter

    @CatalogFilter.setter
    def CatalogFilter(self, CatalogFilter):
        self._CatalogFilter = CatalogFilter

    @property
    def DatabaseFilter(self):
        """Database name filter condition
        :rtype: str
        """
        return self._DatabaseFilter

    @DatabaseFilter.setter
    def DatabaseFilter(self, DatabaseFilter):
        self._DatabaseFilter = DatabaseFilter

    @property
    def SQLTypeFilter(self):
        """SQL type filter criteria
        :rtype: str
        """
        return self._SQLTypeFilter

    @SQLTypeFilter.setter
    def SQLTypeFilter(self, SQLTypeFilter):
        self._SQLTypeFilter = SQLTypeFilter

    @property
    def SortField(self):
        """Sorting field
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortOrder(self):
        """Sorting order: asc (ascending) or desc (descending)
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def QueryTime(self):
        """Minimum query execution time, in milliseconds.
        :rtype: int
        """
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def PageNum(self):
        """Page number, defaults to 1.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Number of records per page, defaults to 10.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SQLFragment = params.get("SQLFragment")
        self._CatalogFilter = params.get("CatalogFilter")
        self._DatabaseFilter = params.get("DatabaseFilter")
        self._SQLTypeFilter = params.get("SQLTypeFilter")
        self._SortField = params.get("SortField")
        self._SortOrder = params.get("SortOrder")
        self._QueryTime = params.get("QueryTime")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueryAnalyseResponse(AbstractModel):
    """DescribeQueryAnalyse response structure.

    """

    def __init__(self):
        r"""
        :param _QueryDetails: Query details
        :type QueryDetails: list of QueryDetails
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _CurrentPage: Current page
        :type CurrentPage: int
        :param _PageSize: Number of records per page
        :type PageSize: int
        :param _TotalPages: Total pages
        :type TotalPages: int
        :param _Message: Error message
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QueryDetails = None
        self._TotalCount = None
        self._CurrentPage = None
        self._PageSize = None
        self._TotalPages = None
        self._Message = None
        self._RequestId = None

    @property
    def QueryDetails(self):
        """Query details
        :rtype: list of QueryDetails
        """
        return self._QueryDetails

    @QueryDetails.setter
    def QueryDetails(self, QueryDetails):
        self._QueryDetails = QueryDetails

    @property
    def TotalCount(self):
        """Total number of records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CurrentPage(self):
        """Current page
        :rtype: int
        """
        return self._CurrentPage

    @CurrentPage.setter
    def CurrentPage(self, CurrentPage):
        self._CurrentPage = CurrentPage

    @property
    def PageSize(self):
        """Number of records per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPages(self):
        """Total pages
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages

    @property
    def Message(self):
        """Error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        if params.get("QueryDetails") is not None:
            self._QueryDetails = []
            for item in params.get("QueryDetails"):
                obj = QueryDetails()
                obj._deserialize(item)
                self._QueryDetails.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._CurrentPage = params.get("CurrentPage")
        self._PageSize = params.get("PageSize")
        self._TotalPages = params.get("TotalPages")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeRestoreTaskDetailRequest(AbstractModel):
    """DescribeRestoreTaskDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _BackUpJobId: Task ID
        :type BackUpJobId: int
        """
        self._InstanceId = None
        self._BackUpJobId = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        """Task ID
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTaskDetailResponse(AbstractModel):
    """DescribeRestoreTaskDetail response structure.

    """

    def __init__(self):
        r"""
        :param _RestoreStatus: Progress details of the recovery tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type RestoreStatus: list of RestoreStatus
        :param _ErrorMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RestoreStatus = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def RestoreStatus(self):
        """Progress details of the recovery tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RestoreStatus
        """
        return self._RestoreStatus

    @RestoreStatus.setter
    def RestoreStatus(self, RestoreStatus):
        self._RestoreStatus = RestoreStatus

    @property
    def ErrorMsg(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("RestoreStatus") is not None:
            self._RestoreStatus = []
            for item in params.get("RestoreStatus"):
                obj = RestoreStatus()
                obj._deserialize(item)
                self._RestoreStatus.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryRecordsDownloadRequest(AbstractModel):
    """DescribeSlowQueryRecordsDownload request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _QueryDurationMs: Slow log time
        :type QueryDurationMs: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _DurationMs: Sort parameters
        :type DurationMs: str
        :param _Sql: Query SQL
        :type Sql: str
        :param _ReadRows: Sort parameters
        :type ReadRows: str
        :param _ResultBytes: Sort parameters
        :type ResultBytes: str
        :param _MemoryUsage: Sort parameters
        :type MemoryUsage: str
        :param _IsQuery: IsQuery condition
        :type IsQuery: int
        :param _DbName: Database name
        :type DbName: list of str
        :param _CatalogName: catalog name
        :type CatalogName: list of str
        """
        self._InstanceId = None
        self._QueryDurationMs = None
        self._StartTime = None
        self._EndTime = None
        self._DurationMs = None
        self._Sql = None
        self._ReadRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._IsQuery = None
        self._DbName = None
        self._CatalogName = None

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
    def QueryDurationMs(self):
        """Slow log time
        :rtype: int
        """
        return self._QueryDurationMs

    @QueryDurationMs.setter
    def QueryDurationMs(self, QueryDurationMs):
        self._QueryDurationMs = QueryDurationMs

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DurationMs(self):
        """Sort parameters
        :rtype: str
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def Sql(self):
        """Query SQL
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def ReadRows(self):
        """Sort parameters
        :rtype: str
        """
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultBytes(self):
        """Sort parameters
        :rtype: str
        """
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        """Sort parameters
        :rtype: str
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def IsQuery(self):
        """IsQuery condition
        :rtype: int
        """
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def DbName(self):
        """Database name
        :rtype: list of str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CatalogName(self):
        """catalog name
        :rtype: list of str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._QueryDurationMs = params.get("QueryDurationMs")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DurationMs = params.get("DurationMs")
        self._Sql = params.get("Sql")
        self._ReadRows = params.get("ReadRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._IsQuery = params.get("IsQuery")
        self._DbName = params.get("DbName")
        self._CatalogName = params.get("CatalogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryRecordsDownloadResponse(AbstractModel):
    """DescribeSlowQueryRecordsDownload response structure.

    """

    def __init__(self):
        r"""
        :param _CosUrl: cos address
        :type CosUrl: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CosUrl = None
        self._RequestId = None

    @property
    def CosUrl(self):
        """cos address
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

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
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryRecordsRequest(AbstractModel):
    """DescribeSlowQueryRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _QueryDurationMs: Slow log time
        :type QueryDurationMs: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Paging
        :type PageSize: int
        :param _PageNum: Paging
        :type PageNum: int
        :param _DurationMs: Sort parameters
        :type DurationMs: str
        :param _DbName: Database name
        :type DbName: list of str
        :param _IsQuery: Whether it is a query. 0 indicates no, and 1 indicates yes.
        :type IsQuery: int
        :param _CatalogName: catalog name
        :type CatalogName: list of str
        :param _Sql: SQL name
        :type Sql: str
        :param _ReadRows: ReadRows sort field
        :type ReadRows: str
        :param _ResultBytes: ResultBytes sort field
        :type ResultBytes: str
        :param _MemoryUsage: MemoryUsage sort field
        :type MemoryUsage: str
        """
        self._InstanceId = None
        self._QueryDurationMs = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNum = None
        self._DurationMs = None
        self._DbName = None
        self._IsQuery = None
        self._CatalogName = None
        self._Sql = None
        self._ReadRows = None
        self._ResultBytes = None
        self._MemoryUsage = None

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
    def QueryDurationMs(self):
        """Slow log time
        :rtype: int
        """
        return self._QueryDurationMs

    @QueryDurationMs.setter
    def QueryDurationMs(self, QueryDurationMs):
        self._QueryDurationMs = QueryDurationMs

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Paging
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        """Paging
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def DurationMs(self):
        """Sort parameters
        :rtype: str
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def DbName(self):
        """Database name
        :rtype: list of str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def IsQuery(self):
        """Whether it is a query. 0 indicates no, and 1 indicates yes.
        :rtype: int
        """
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def CatalogName(self):
        """catalog name
        :rtype: list of str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def Sql(self):
        """SQL name
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def ReadRows(self):
        """ReadRows sort field
        :rtype: str
        """
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultBytes(self):
        """ResultBytes sort field
        :rtype: str
        """
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        """MemoryUsage sort field
        :rtype: str
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._QueryDurationMs = params.get("QueryDurationMs")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._DurationMs = params.get("DurationMs")
        self._DbName = params.get("DbName")
        self._IsQuery = params.get("IsQuery")
        self._CatalogName = params.get("CatalogName")
        self._Sql = params.get("Sql")
        self._ReadRows = params.get("ReadRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryRecordsResponse(AbstractModel):
    """DescribeSlowQueryRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total
        :type TotalCount: int
        :param _SlowQueryRecords: Record list
        :type SlowQueryRecords: list of SlowQueryRecord
        :param _DBNameList: All database names
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBNameList: list of str
        :param _CatalogNameList: All catalog names
Note: This field may return null, indicating that no valid values can be obtained.
        :type CatalogNameList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowQueryRecords = None
        self._DBNameList = None
        self._CatalogNameList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowQueryRecords(self):
        """Record list
        :rtype: list of SlowQueryRecord
        """
        return self._SlowQueryRecords

    @SlowQueryRecords.setter
    def SlowQueryRecords(self, SlowQueryRecords):
        self._SlowQueryRecords = SlowQueryRecords

    @property
    def DBNameList(self):
        """All database names
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DBNameList

    @DBNameList.setter
    def DBNameList(self, DBNameList):
        self._DBNameList = DBNameList

    @property
    def CatalogNameList(self):
        """All catalog names
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._CatalogNameList

    @CatalogNameList.setter
    def CatalogNameList(self, CatalogNameList):
        self._CatalogNameList = CatalogNameList

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
        if params.get("SlowQueryRecords") is not None:
            self._SlowQueryRecords = []
            for item in params.get("SlowQueryRecords"):
                obj = SlowQueryRecord()
                obj._deserialize(item)
                self._SlowQueryRecords.append(obj)
        self._DBNameList = params.get("DBNameList")
        self._CatalogNameList = params.get("CatalogNameList")
        self._RequestId = params.get("RequestId")


class DescribeSpecRequest(AbstractModel):
    """DescribeSpec request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Region information, such as ap-guangzhou-1.
        :type Zone: str
        :param _PayMode: Billing type. PREPAID: annual/monthly package; POSTPAID_BY_HOUR: pay-as-you-go
        :type PayMode: str
        :param _Zones: Multi-availability zone
        :type Zones: list of str
        :param _SpecName: Model name
        :type SpecName: str
        """
        self._Zone = None
        self._PayMode = None
        self._Zones = None
        self._SpecName = None

    @property
    def Zone(self):
        """Region information, such as ap-guangzhou-1.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def PayMode(self):
        """Billing type. PREPAID: annual/monthly package; POSTPAID_BY_HOUR: pay-as-you-go
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Zones(self):
        """Multi-availability zone
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SpecName(self):
        """Model name
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._PayMode = params.get("PayMode")
        self._Zones = params.get("Zones")
        self._SpecName = params.get("SpecName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecResponse(AbstractModel):
    """DescribeSpec response structure.

    """

    def __init__(self):
        r"""
        :param _MasterSpec: Zookeeper node specification description
        :type MasterSpec: list of ResourceSpec
        :param _CoreSpec: Data node specification description
        :type CoreSpec: list of ResourceSpec
        :param _AttachCBSSpec: Cloud disk list
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttachCBSSpec: list of DiskSpec
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MasterSpec = None
        self._CoreSpec = None
        self._AttachCBSSpec = None
        self._RequestId = None

    @property
    def MasterSpec(self):
        """Zookeeper node specification description
        :rtype: list of ResourceSpec
        """
        return self._MasterSpec

    @MasterSpec.setter
    def MasterSpec(self, MasterSpec):
        self._MasterSpec = MasterSpec

    @property
    def CoreSpec(self):
        """Data node specification description
        :rtype: list of ResourceSpec
        """
        return self._CoreSpec

    @CoreSpec.setter
    def CoreSpec(self, CoreSpec):
        self._CoreSpec = CoreSpec

    @property
    def AttachCBSSpec(self):
        """Cloud disk list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DiskSpec
        """
        return self._AttachCBSSpec

    @AttachCBSSpec.setter
    def AttachCBSSpec(self, AttachCBSSpec):
        self._AttachCBSSpec = AttachCBSSpec

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
        if params.get("MasterSpec") is not None:
            self._MasterSpec = []
            for item in params.get("MasterSpec"):
                obj = ResourceSpec()
                obj._deserialize(item)
                self._MasterSpec.append(obj)
        if params.get("CoreSpec") is not None:
            self._CoreSpec = []
            for item in params.get("CoreSpec"):
                obj = ResourceSpec()
                obj._deserialize(item)
                self._CoreSpec.append(obj)
        if params.get("AttachCBSSpec") is not None:
            self._AttachCBSSpec = []
            for item in params.get("AttachCBSSpec"):
                obj = DiskSpec()
                obj._deserialize(item)
                self._AttachCBSSpec.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSqlApisRequest(AbstractModel):
    """DescribeSqlApis request structure.

    """

    def __init__(self):
        r"""
        :param _WhiteHost: The IP address of the user link
        :type WhiteHost: str
        :param _Catalog: catalog name
        :type Catalog: str
        :param _Catalogs: Catalog collection
        :type Catalogs: list of str
        """
        self._WhiteHost = None
        self._Catalog = None
        self._Catalogs = None

    @property
    def WhiteHost(self):
        """The IP address of the user link
        :rtype: str
        """
        return self._WhiteHost

    @WhiteHost.setter
    def WhiteHost(self, WhiteHost):
        self._WhiteHost = WhiteHost

    @property
    def Catalog(self):
        """catalog name
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Catalogs(self):
        """Catalog collection
        :rtype: list of str
        """
        return self._Catalogs

    @Catalogs.setter
    def Catalogs(self, Catalogs):
        self._Catalogs = Catalogs


    def _deserialize(self, params):
        self._WhiteHost = params.get("WhiteHost")
        self._Catalog = params.get("Catalog")
        self._Catalogs = params.get("Catalogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSqlApisResponse(AbstractModel):
    """DescribeSqlApis response structure.

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


class DescribeTableListRequest(AbstractModel):
    """DescribeTableList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Resource ID, which is the TCHouse-D resource ID used for table creation.
        :type InstanceId: str
        :param _DbName: Database for obtaining the list of tables
        :type DbName: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _CatalogName: Query the data source where the database is located. If it is not filled in, the internal data source (internal) will be used by default.
        :type CatalogName: str
        """
        self._InstanceId = None
        self._DbName = None
        self._UserName = None
        self._PassWord = None
        self._CatalogName = None

    @property
    def InstanceId(self):
        """Resource ID, which is the TCHouse-D resource ID used for table creation.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """Database for obtaining the list of tables
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def CatalogName(self):
        """Query the data source where the database is located. If it is not filled in, the internal data source (internal) will be used by default.
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._CatalogName = params.get("CatalogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableListResponse(AbstractModel):
    """DescribeTableList response structure.

    """

    def __init__(self):
        r"""
        :param _TableNames: List of table names
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableNames: list of str
        :param _Message: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TableNames = None
        self._Message = None
        self._RequestId = None

    @property
    def TableNames(self):
        """List of table names
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._TableNames

    @TableNames.setter
    def TableNames(self, TableNames):
        self._TableNames = TableNames

    @property
    def Message(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._TableNames = params.get("TableNames")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeTableRequest(AbstractModel):
    """DescribeTable request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Resource ID, which is the TCHouse-D resource ID used for table creation.
        :type InstanceId: str
        :param _DbName: Name of database where the table is located
        :type DbName: str
        :param _TableName: Table name (Currently only internal tables are supported.)
        :type TableName: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        """
        self._InstanceId = None
        self._DbName = None
        self._TableName = None
        self._UserName = None
        self._PassWord = None

    @property
    def InstanceId(self):
        """Resource ID, which is the TCHouse-D resource ID used for table creation.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """Name of database where the table is located
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableName(self):
        """Table name (Currently only internal tables are supported.)
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._TableName = params.get("TableName")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableResponse(AbstractModel):
    """DescribeTable response structure.

    """

    def __init__(self):
        r"""
        :param _KeysType: Note: This field may return null, indicating that no valid values can be obtained.
        :type KeysType: str
        :param _Columns: Note: This field may return null, indicating that no valid values can be obtained.
        :type Columns: list of Column
        :param _IndexInfos: Note: This field may return null, indicating that no valid values can be obtained.
        :type IndexInfos: list of IndexInfo
        :param _Partition: Note: This field may return null, indicating that no valid values can be obtained.
        :type Partition: :class:`tencentcloud.cdwdoris.v20211228.models.Partition`
        :param _Distribution: Note: This field may return null, indicating that no valid values can be obtained.
        :type Distribution: :class:`tencentcloud.cdwdoris.v20211228.models.Distribution`
        :param _TableComment: Note: This field may return null, indicating that no valid values can be obtained.
        :type TableComment: str
        :param _Properties: Note: This field may return null, indicating that no valid values can be obtained.
        :type Properties: list of Property
        :param _Message: Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeysType = None
        self._Columns = None
        self._IndexInfos = None
        self._Partition = None
        self._Distribution = None
        self._TableComment = None
        self._Properties = None
        self._Message = None
        self._RequestId = None

    @property
    def KeysType(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeysType

    @KeysType.setter
    def KeysType(self, KeysType):
        self._KeysType = KeysType

    @property
    def Columns(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Column
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def IndexInfos(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of IndexInfo
        """
        return self._IndexInfos

    @IndexInfos.setter
    def IndexInfos(self, IndexInfos):
        self._IndexInfos = IndexInfos

    @property
    def Partition(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.Partition`
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Distribution(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.Distribution`
        """
        return self._Distribution

    @Distribution.setter
    def Distribution(self, Distribution):
        self._Distribution = Distribution

    @property
    def TableComment(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableComment

    @TableComment.setter
    def TableComment(self, TableComment):
        self._TableComment = TableComment

    @property
    def Properties(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def Message(self):
        """Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._KeysType = params.get("KeysType")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("IndexInfos") is not None:
            self._IndexInfos = []
            for item in params.get("IndexInfos"):
                obj = IndexInfo()
                obj._deserialize(item)
                self._IndexInfos.append(obj)
        if params.get("Partition") is not None:
            self._Partition = Partition()
            self._Partition._deserialize(params.get("Partition"))
        if params.get("Distribution") is not None:
            self._Distribution = Distribution()
            self._Distribution._deserialize(params.get("Distribution"))
        self._TableComment = params.get("TableComment")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeUserBindWorkloadGroupRequest(AbstractModel):
    """DescribeUserBindWorkloadGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster ID
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
        


class DescribeUserBindWorkloadGroupResponse(AbstractModel):
    """DescribeUserBindWorkloadGroup response structure.

    """

    def __init__(self):
        r"""
        :param _UserBindInfos: Resource group information bound to the user
        :type UserBindInfos: list of UserWorkloadGroup
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserBindInfos = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def UserBindInfos(self):
        """Resource group information bound to the user
        :rtype: list of UserWorkloadGroup
        """
        return self._UserBindInfos

    @UserBindInfos.setter
    def UserBindInfos(self, UserBindInfos):
        self._UserBindInfos = UserBindInfos

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("UserBindInfos") is not None:
            self._UserBindInfos = []
            for item in params.get("UserBindInfos"):
                obj = UserWorkloadGroup()
                obj._deserialize(item)
                self._UserBindInfos.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeUserPolicyRequest(AbstractModel):
    """DescribeUserPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _WhiteHost: You can specify one IP address or specify a percent sign (%) to indicate no limit.
        :type WhiteHost: str
        """
        self._InstanceId = None
        self._UserName = None
        self._PassWord = None
        self._WhiteHost = None

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
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def WhiteHost(self):
        """You can specify one IP address or specify a percent sign (%) to indicate no limit.
        :rtype: str
        """
        return self._WhiteHost

    @WhiteHost.setter
    def WhiteHost(self, WhiteHost):
        self._WhiteHost = WhiteHost


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._WhiteHost = params.get("WhiteHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserPolicyResponse(AbstractModel):
    """DescribeUserPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AccountInfo: Account details
        :type AccountInfo: :class:`tencentcloud.cdwdoris.v20211228.models.AccountDetailInfo`
        :param _Permissions: Permission configuration information associated with different hosts
        :type Permissions: :class:`tencentcloud.cdwdoris.v20211228.models.PermissionHostInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountInfo = None
        self._Permissions = None
        self._RequestId = None

    @property
    def AccountInfo(self):
        """Account details
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.AccountDetailInfo`
        """
        return self._AccountInfo

    @AccountInfo.setter
    def AccountInfo(self, AccountInfo):
        self._AccountInfo = AccountInfo

    @property
    def Permissions(self):
        """Permission configuration information associated with different hosts
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.PermissionHostInfo`
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

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
        if params.get("AccountInfo") is not None:
            self._AccountInfo = AccountDetailInfo()
            self._AccountInfo._deserialize(params.get("AccountInfo"))
        if params.get("Permissions") is not None:
            self._Permissions = PermissionHostInfo()
            self._Permissions._deserialize(params.get("Permissions"))
        self._RequestId = params.get("RequestId")


class DescribeWorkloadGroupRequest(AbstractModel):
    """DescribeWorkloadGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster ID
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
        


class DescribeWorkloadGroupResponse(AbstractModel):
    """DescribeWorkloadGroup response structure.

    """

    def __init__(self):
        r"""
        :param _WorkloadGroups: Resource group information
        :type WorkloadGroups: list of WorkloadGroupConfig
        :param _Status: Whether to enable the resource group: open and close
        :type Status: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WorkloadGroups = None
        self._Status = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def WorkloadGroups(self):
        """Resource group information
        :rtype: list of WorkloadGroupConfig
        """
        return self._WorkloadGroups

    @WorkloadGroups.setter
    def WorkloadGroups(self, WorkloadGroups):
        self._WorkloadGroups = WorkloadGroups

    @property
    def Status(self):
        """Whether to enable the resource group: open and close
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("WorkloadGroups") is not None:
            self._WorkloadGroups = []
            for item in params.get("WorkloadGroups"):
                obj = WorkloadGroupConfig()
                obj._deserialize(item)
                self._WorkloadGroups.append(obj)
        self._Status = params.get("Status")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DestroyInstanceRequest(AbstractModel):
    """DestroyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster ID
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
        


class DestroyInstanceResponse(AbstractModel):
    """DestroyInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID
        :type FlowId: str
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DiskSpec(AbstractModel):
    """Disk specification description

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type, such as CLOUD_SSD and LOCAL_SSD
        :type DiskType: str
        :param _DiskDesc: Disk type description, such as cloud SSD and local SSD
        :type DiskDesc: str
        :param _MinDiskSize: Minimum disk size, in GB
        :type MinDiskSize: int
        :param _MaxDiskSize: Maximum disk size, in GB
        :type MaxDiskSize: int
        :param _DiskCount: Number of disks
        :type DiskCount: int
        """
        self._DiskType = None
        self._DiskDesc = None
        self._MinDiskSize = None
        self._MaxDiskSize = None
        self._DiskCount = None

    @property
    def DiskType(self):
        """Disk type, such as CLOUD_SSD and LOCAL_SSD
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        """Disk type description, such as cloud SSD and local SSD
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def MinDiskSize(self):
        """Minimum disk size, in GB
        :rtype: int
        """
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def MaxDiskSize(self):
        """Maximum disk size, in GB
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def DiskCount(self):
        """Number of disks
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskDesc = params.get("DiskDesc")
        self._MinDiskSize = params.get("MinDiskSize")
        self._MaxDiskSize = params.get("MaxDiskSize")
        self._DiskCount = params.get("DiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Distribution(AbstractModel):
    """Bucket information of the table

    """

    def __init__(self):
        r"""
        :param _DistributionType: Bucket type:
●Hash: hash bucket
●Random: random number bucket

Note: This field may return null, indicating that no valid values can be obtained.
        :type DistributionType: str
        :param _Count: Number of buckets
Note: This field may return null, indicating that no valid values can be obtained.
        :type Count: int
        """
        self._DistributionType = None
        self._Count = None

    @property
    def DistributionType(self):
        """Bucket type:
●Hash: hash bucket
●Random: random number bucket

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DistributionType

    @DistributionType.setter
    def DistributionType(self, DistributionType):
        self._DistributionType = DistributionType

    @property
    def Count(self):
        """Number of buckets
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._DistributionType = params.get("DistributionType")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DorisSourceInfo(AbstractModel):
    """Connection information of external Doris clusters

    """

    def __init__(self):
        r"""
        :param _Host: The IP address of fe in the Doris cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param _Port: The fe port number of the Doris cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _User: Account of the Doris cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: str
        :param _Password: Password of the Doris cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type Password: str
        """
        self._Host = None
        self._Port = None
        self._User = None
        self._Password = None

    @property
    def Host(self):
        """The IP address of fe in the Doris cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        """The fe port number of the Doris cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        """Account of the Doris cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """Password of the Doris cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._User = params.get("User")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteParametrizedQueryRequest(AbstractModel):
    """ExecuteParametrizedQuery request structure.

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Sql: SQL query statement
        :type Sql: str
        :param _InstanceId: InstanceId
        :type InstanceId: str
        :param _QueryParameter: Query parameter array.
        :type QueryParameter: list of PropertiesMap
        :param _PageNum: Page number, which is 1 by default.
        :type PageNum: int
        :param _PageSize: Number of records per page, which is 10 by default.
        :type PageSize: int
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _CatalogName: Catalog name, defaults to 'internal' if not specified.
        :type CatalogName: str
        """
        self._Database = None
        self._Sql = None
        self._InstanceId = None
        self._QueryParameter = None
        self._PageNum = None
        self._PageSize = None
        self._UserName = None
        self._PassWord = None
        self._CatalogName = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Sql(self):
        """SQL query statement
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def InstanceId(self):
        """InstanceId
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def QueryParameter(self):
        """Query parameter array.
        :rtype: list of PropertiesMap
        """
        return self._QueryParameter

    @QueryParameter.setter
    def QueryParameter(self, QueryParameter):
        self._QueryParameter = QueryParameter

    @property
    def PageNum(self):
        """Page number, which is 1 by default.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Number of records per page, which is 10 by default.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def CatalogName(self):
        """Catalog name, defaults to 'internal' if not specified.
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Sql = params.get("Sql")
        self._InstanceId = params.get("InstanceId")
        if params.get("QueryParameter") is not None:
            self._QueryParameter = []
            for item in params.get("QueryParameter"):
                obj = PropertiesMap()
                obj._deserialize(item)
                self._QueryParameter.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._CatalogName = params.get("CatalogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteParametrizedQueryResponse(AbstractModel):
    """ExecuteParametrizedQuery response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total records of query results
        :type TotalCount: int
        :param _Fields: Field name array of query results
        :type Fields: list of str
        :param _FieldTypes: Field type array of query results
        :type FieldTypes: list of str
        :param _Rows: Returned data record array. Each element is an array, containing the value of the corresponding field.
        :type Rows: list of Rows
        :param _Message: Error message
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Fields = None
        self._FieldTypes = None
        self._Rows = None
        self._Message = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total records of query results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Fields(self):
        """Field name array of query results
        :rtype: list of str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def FieldTypes(self):
        """Field type array of query results
        :rtype: list of str
        """
        return self._FieldTypes

    @FieldTypes.setter
    def FieldTypes(self, FieldTypes):
        self._FieldTypes = FieldTypes

    @property
    def Rows(self):
        """Returned data record array. Each element is an array, containing the value of the corresponding field.
        :rtype: list of Rows
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def Message(self):
        """Error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Fields = params.get("Fields")
        self._FieldTypes = params.get("FieldTypes")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = Rows()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class ExecuteSelectQueryRequest(AbstractModel):
    """ExecuteSelectQuery request structure.

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Query: SQL query statements only support select statements.
        :type Query: str
        :param _InstanceId: InstanceId
        :type InstanceId: str
        :param _PageNum: Page number, which is 1 by default.
        :type PageNum: int
        :param _PageSize: Number of records per page, which is 10 by default.
        :type PageSize: int
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _CatalogName: Catalog name, defaults to 'internal' if not specified.

        :type CatalogName: str
        """
        self._Database = None
        self._Query = None
        self._InstanceId = None
        self._PageNum = None
        self._PageSize = None
        self._UserName = None
        self._PassWord = None
        self._CatalogName = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Query(self):
        """SQL query statements only support select statements.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def InstanceId(self):
        """InstanceId
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PageNum(self):
        """Page number, which is 1 by default.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Number of records per page, which is 10 by default.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def CatalogName(self):
        """Catalog name, defaults to 'internal' if not specified.

        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Query = params.get("Query")
        self._InstanceId = params.get("InstanceId")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._CatalogName = params.get("CatalogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteSelectQueryResponse(AbstractModel):
    """ExecuteSelectQuery response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total records of query results
        :type TotalCount: int
        :param _Fields: Field name array of query results
        :type Fields: list of str
        :param _FieldTypes: Field type array of query results
        :type FieldTypes: list of str
        :param _Rows: Returned data record array. Each element is an array, containing the value of the corresponding field.
        :type Rows: list of Rows
        :param _Message: Error message
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Fields = None
        self._FieldTypes = None
        self._Rows = None
        self._Message = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total records of query results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Fields(self):
        """Field name array of query results
        :rtype: list of str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def FieldTypes(self):
        """Field type array of query results
        :rtype: list of str
        """
        return self._FieldTypes

    @FieldTypes.setter
    def FieldTypes(self, FieldTypes):
        self._FieldTypes = FieldTypes

    @property
    def Rows(self):
        """Returned data record array. Each element is an array, containing the value of the corresponding field.
        :rtype: list of Rows
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def Message(self):
        """Error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Fields = params.get("Fields")
        self._FieldTypes = params.get("FieldTypes")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = Rows()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class FrontEndRule(AbstractModel):
    """Front-end rule description

    """

    def __init__(self):
        r"""
        :param _ID: ID sequence
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: int
        :param _Name: Rule name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Rule: Detailed rules
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rule: str
        """
        self._ID = None
        self._Name = None
        self._Rule = None

    @property
    def ID(self):
        """ID sequence
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        """Rule name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rule(self):
        """Detailed rules
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Rule = params.get("Rule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexInfo(AbstractModel):
    """Index information of the table

    """

    def __init__(self):
        r"""
        :param _IdxName: Index name
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdxName: str
        :param _ColumnName: Column name for creating the index
Note: This field may return null, indicating that no valid values can be obtained.
        :type ColumnName: str
        :param _IdxType: Index type:
INVERTED: inverted index
NGRAM_BF: N-Gram index

Note: This field may return null, indicating that no valid values can be obtained.
        :type IdxType: str
        :param _IdxProperties: Index attributes
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdxProperties: list of Property
        :param _IdxComment: Index description
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdxComment: str
        """
        self._IdxName = None
        self._ColumnName = None
        self._IdxType = None
        self._IdxProperties = None
        self._IdxComment = None

    @property
    def IdxName(self):
        """Index name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IdxName

    @IdxName.setter
    def IdxName(self, IdxName):
        self._IdxName = IdxName

    @property
    def ColumnName(self):
        """Column name for creating the index
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def IdxType(self):
        """Index type:
INVERTED: inverted index
NGRAM_BF: N-Gram index

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IdxType

    @IdxType.setter
    def IdxType(self, IdxType):
        self._IdxType = IdxType

    @property
    def IdxProperties(self):
        """Index attributes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Property
        """
        return self._IdxProperties

    @IdxProperties.setter
    def IdxProperties(self, IdxProperties):
        self._IdxProperties = IdxProperties

    @property
    def IdxComment(self):
        """Index description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IdxComment

    @IdxComment.setter
    def IdxComment(self, IdxComment):
        self._IdxComment = IdxComment


    def _deserialize(self, params):
        self._IdxName = params.get("IdxName")
        self._ColumnName = params.get("ColumnName")
        self._IdxType = params.get("IdxType")
        if params.get("IdxProperties") is not None:
            self._IdxProperties = []
            for item in params.get("IdxProperties"):
                obj = Property()
                obj._deserialize(item)
                self._IdxProperties.append(obj)
        self._IdxComment = params.get("IdxComment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InsertDatasToTableRequest(AbstractModel):
    """InsertDatasToTable request structure.

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Table: Table name
        :type Table: str
        :param _Columns: Array of column names
        :type Columns: list of str
        :param _Rows: Data line
        :type Rows: list of Rows
        :param _Types: Array of column types

        :type Types: list of str
        :param _InstanceId: InstanceId
        :type InstanceId: str
        :param _Strict: Whether to use the strict mode
        :type Strict: bool
        :param _MaxFilterRatio: Maximum filtration ratio, ranging from 0 to 1.0
        :type MaxFilterRatio: float
        :param _Label: Tags for inserting data
        :type Label: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _CatalogName: Catalog name, defaults to 'internal' if not specified.
        :type CatalogName: str
        """
        self._Database = None
        self._Table = None
        self._Columns = None
        self._Rows = None
        self._Types = None
        self._InstanceId = None
        self._Strict = None
        self._MaxFilterRatio = None
        self._Label = None
        self._UserName = None
        self._PassWord = None
        self._CatalogName = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """Table name
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Columns(self):
        """Array of column names
        :rtype: list of str
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Rows(self):
        """Data line
        :rtype: list of Rows
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def Types(self):
        """Array of column types

        :rtype: list of str
        """
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def InstanceId(self):
        """InstanceId
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Strict(self):
        """Whether to use the strict mode
        :rtype: bool
        """
        return self._Strict

    @Strict.setter
    def Strict(self, Strict):
        self._Strict = Strict

    @property
    def MaxFilterRatio(self):
        """Maximum filtration ratio, ranging from 0 to 1.0
        :rtype: float
        """
        return self._MaxFilterRatio

    @MaxFilterRatio.setter
    def MaxFilterRatio(self, MaxFilterRatio):
        self._MaxFilterRatio = MaxFilterRatio

    @property
    def Label(self):
        """Tags for inserting data
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def CatalogName(self):
        """Catalog name, defaults to 'internal' if not specified.
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Columns = params.get("Columns")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = Rows()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._Types = params.get("Types")
        self._InstanceId = params.get("InstanceId")
        self._Strict = params.get("Strict")
        self._MaxFilterRatio = params.get("MaxFilterRatio")
        self._Label = params.get("Label")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._CatalogName = params.get("CatalogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InsertDatasToTableResponse(AbstractModel):
    """InsertDatasToTable response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Whether the insertion operation is successful
        :type Success: bool
        :param _Message: Message description of the operation result
        :type Message: str
        :param _InsertCount: Number of inserted data rows
        :type InsertCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._Message = None
        self._InsertCount = None
        self._RequestId = None

    @property
    def Success(self):
        """Whether the insertion operation is successful
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def Message(self):
        """Message description of the operation result
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InsertCount(self):
        """Number of inserted data rows
        :rtype: int
        """
        return self._InsertCount

    @InsertCount.setter
    def InsertCount(self, InsertCount):
        self._InsertCount = InsertCount

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
        self._Success = params.get("Success")
        self._Message = params.get("Message")
        self._InsertCount = params.get("InsertCount")
        self._RequestId = params.get("RequestId")


class InstanceConfigItem(AbstractModel):
    """KV configuration

    """

    def __init__(self):
        r"""
        :param _ConfKey: key
        :type ConfKey: str
        :param _ConfValue: value
        :type ConfValue: str
        """
        self._ConfKey = None
        self._ConfValue = None

    @property
    def ConfKey(self):
        """key
        :rtype: str
        """
        return self._ConfKey

    @ConfKey.setter
    def ConfKey(self, ConfKey):
        self._ConfKey = ConfKey

    @property
    def ConfValue(self):
        """value
        :rtype: str
        """
        return self._ConfValue

    @ConfValue.setter
    def ConfValue(self, ConfValue):
        self._ConfValue = ConfValue


    def _deserialize(self, params):
        self._ConfKey = params.get("ConfKey")
        self._ConfValue = params.get("ConfValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """Detail field of the Instance table

    """

    def __init__(self):
        r"""
        :param _EnableAlarmStrategy: Whether the alarm policy is available	
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableAlarmStrategy: bool
        """
        self._EnableAlarmStrategy = None

    @property
    def EnableAlarmStrategy(self):
        """Whether the alarm policy is available	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableAlarmStrategy

    @EnableAlarmStrategy.setter
    def EnableAlarmStrategy(self, EnableAlarmStrategy):
        self._EnableAlarmStrategy = EnableAlarmStrategy


    def _deserialize(self, params):
        self._EnableAlarmStrategy = params.get("EnableAlarmStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """Instance description information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID, "cdw-xxxx" string type
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Cluster instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Status: Status,
Init is being created. Serving is running. 
Deleted indicates the cluster has been terminated. Deleting indicates the cluster is being terminated.
Modify indicates the cluster is being changed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _Region: Region, ap-guangzhou
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zone: Availability zone, ap-guangzhou-3
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _VpcId: VPC name
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _PayMode: Payment type: hour and prepay
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ExpireTime: Expiration time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _MasterSummary: Data node description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterSummary: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        :param _CoreSummary: Zookeeper node description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type CoreSummary: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        :param _HA: High availability, being true or false
Note: This field may return null, indicating that no valid values can be obtained.
        :type HA: str
        :param _HaType: High availability type:
0: non-high availability
1: read high availability
2: read-write high availability
Note: This field may return null, indicating that no valid values can be obtained.
        :type HaType: int
        :param _AccessInfo: Access address. Example: 10.0.0.1:9000
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessInfo: str
        :param _Id: Record ID, in numerical type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _RegionId: Region ID, indicating the region
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _ZoneDesc: Note about availability zone, such as Guangzhou Zone 2
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneDesc: str
        :param _FlowMsg: Error process description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowMsg: str
        :param _StatusDesc: Status description, such as "running"
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusDesc: str
        :param _RenewFlag: Automatic renewal marker
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: bool
        :param _Tags: Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Monitor: Monitoring Information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Monitor: str
        :param _HasClsTopic: Whether to enable logs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasClsTopic: bool
        :param _ClsTopicId: Log Topic ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClsTopicId: str
        :param _ClsLogSetId: Logset ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClsLogSetId: str
        :param _EnableXMLConfig: Whether to support XML configuration management.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableXMLConfig: int
        :param _RegionDesc: Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionDesc: str
        :param _Eip: Elastic network interface address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Eip: str
        :param _CosMoveFactor: Cold and hot stratification coefficient
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosMoveFactor: int
        :param _Kind: external/local/yunti
Note: This field may return null, indicating that no valid values can be obtained.
        :type Kind: str
        :param _CosBucketName: COS bucket
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosBucketName: str
        :param _CanAttachCbs: cbs
Note: This field may return null, indicating that no valid values can be obtained.
        :type CanAttachCbs: bool
        :param _BuildVersion: Minor versions
Note: This field may return null, indicating that no valid values can be obtained.
        :type BuildVersion: str
        :param _Components: Component Information
Note: The return type here is map[string]struct, not the string type displayed. You can refer to "Sample Value" to parse the data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Components: str
        :param _IfExistCatalog: Determine whether the audit log table has a catalog field.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IfExistCatalog: int
        :param _Characteristic: Page features, used to block some page entrances on the front end.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Characteristic: list of str
        :param _RestartTimeout: Timeout period, in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type RestartTimeout: str
        :param _GraceShutdownWaitSeconds: The timeout time for the graceful restart of the kernel. If it is -1, it means it is not set.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GraceShutdownWaitSeconds: str
        :param _CaseSensitive: Whether the table name is case sensitive, 0 refers to sensitive, 1 refers to insensitive, compared in lowercase; 2 refers to insensitive, and the table name is changed to lowercase for storage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CaseSensitive: int
        :param _IsWhiteSGs: Whether users can bind security groups.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsWhiteSGs: bool
        :param _BindSGs: Bound security group information
Note: This field may return null, indicating that no valid values can be obtained.
        :type BindSGs: list of str
        :param _EnableMultiZones: Whether it is a multi-AZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableMultiZones: bool
        :param _UserNetworkInfos: User availability zone and subnet information
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserNetworkInfos: str
        :param _EnableCoolDown: Whether to enable hot and cold stratification. 0 refers to disabled, and 1 refers to enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableCoolDown: int
        :param _CoolDownBucket: COS buckets are used for hot and cold stratification
Note: This field may return null, indicating that no valid values can be obtained.
        :type CoolDownBucket: str
        :param _Details: Instance extension information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Details: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceDetail`
        :param _EnableDlc: Whether to enable DLC. 0: disable; 1: enable.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableDlc: int
        :param _AccountType: Account type. 0: ordinary user; 1: CAM user.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountType: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._Version = None
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._PayMode = None
        self._CreateTime = None
        self._ExpireTime = None
        self._MasterSummary = None
        self._CoreSummary = None
        self._HA = None
        self._HaType = None
        self._AccessInfo = None
        self._Id = None
        self._RegionId = None
        self._ZoneDesc = None
        self._FlowMsg = None
        self._StatusDesc = None
        self._RenewFlag = None
        self._Tags = None
        self._Monitor = None
        self._HasClsTopic = None
        self._ClsTopicId = None
        self._ClsLogSetId = None
        self._EnableXMLConfig = None
        self._RegionDesc = None
        self._Eip = None
        self._CosMoveFactor = None
        self._Kind = None
        self._CosBucketName = None
        self._CanAttachCbs = None
        self._BuildVersion = None
        self._Components = None
        self._IfExistCatalog = None
        self._Characteristic = None
        self._RestartTimeout = None
        self._GraceShutdownWaitSeconds = None
        self._CaseSensitive = None
        self._IsWhiteSGs = None
        self._BindSGs = None
        self._EnableMultiZones = None
        self._UserNetworkInfos = None
        self._EnableCoolDown = None
        self._CoolDownBucket = None
        self._Details = None
        self._EnableDlc = None
        self._AccountType = None

    @property
    def InstanceId(self):
        """Cluster instance ID, "cdw-xxxx" string type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Cluster instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        """Status,
Init is being created. Serving is running. 
Deleted indicates the cluster has been terminated. Deleting indicates the cluster is being terminated.
Modify indicates the cluster is being changed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Version(self):
        """Version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        """Region, ap-guangzhou
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """Availability zone, ap-guangzhou-3
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """VPC name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PayMode(self):
        """Payment type: hour and prepay
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        """Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """Expiration time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def MasterSummary(self):
        """Data node description information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        """
        return self._MasterSummary

    @MasterSummary.setter
    def MasterSummary(self, MasterSummary):
        self._MasterSummary = MasterSummary

    @property
    def CoreSummary(self):
        """Zookeeper node description information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        """
        return self._CoreSummary

    @CoreSummary.setter
    def CoreSummary(self, CoreSummary):
        self._CoreSummary = CoreSummary

    @property
    def HA(self):
        """High availability, being true or false
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HA

    @HA.setter
    def HA(self, HA):
        self._HA = HA

    @property
    def HaType(self):
        """High availability type:
0: non-high availability
1: read high availability
2: read-write high availability
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType

    @property
    def AccessInfo(self):
        """Access address. Example: 10.0.0.1:9000
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def Id(self):
        """Record ID, in numerical type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RegionId(self):
        """Region ID, indicating the region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneDesc(self):
        """Note about availability zone, such as Guangzhou Zone 2
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def FlowMsg(self):
        """Error process description information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def StatusDesc(self):
        """Status description, such as "running"
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def RenewFlag(self):
        """Automatic renewal marker
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Tags(self):
        """Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Monitor(self):
        """Monitoring Information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Monitor

    @Monitor.setter
    def Monitor(self, Monitor):
        self._Monitor = Monitor

    @property
    def HasClsTopic(self):
        """Whether to enable logs.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._HasClsTopic

    @HasClsTopic.setter
    def HasClsTopic(self, HasClsTopic):
        self._HasClsTopic = HasClsTopic

    @property
    def ClsTopicId(self):
        """Log Topic ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def ClsLogSetId(self):
        """Logset ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClsLogSetId

    @ClsLogSetId.setter
    def ClsLogSetId(self, ClsLogSetId):
        self._ClsLogSetId = ClsLogSetId

    @property
    def EnableXMLConfig(self):
        """Whether to support XML configuration management.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EnableXMLConfig

    @EnableXMLConfig.setter
    def EnableXMLConfig(self, EnableXMLConfig):
        self._EnableXMLConfig = EnableXMLConfig

    @property
    def RegionDesc(self):
        """Region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def Eip(self):
        """Elastic network interface address
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def CosMoveFactor(self):
        """Cold and hot stratification coefficient
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CosMoveFactor

    @CosMoveFactor.setter
    def CosMoveFactor(self, CosMoveFactor):
        self._CosMoveFactor = CosMoveFactor

    @property
    def Kind(self):
        """external/local/yunti
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def CosBucketName(self):
        """COS bucket
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CanAttachCbs(self):
        """cbs
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._CanAttachCbs

    @CanAttachCbs.setter
    def CanAttachCbs(self, CanAttachCbs):
        self._CanAttachCbs = CanAttachCbs

    @property
    def BuildVersion(self):
        """Minor versions
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BuildVersion

    @BuildVersion.setter
    def BuildVersion(self, BuildVersion):
        self._BuildVersion = BuildVersion

    @property
    def Components(self):
        """Component Information
Note: The return type here is map[string]struct, not the string type displayed. You can refer to "Sample Value" to parse the data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def IfExistCatalog(self):
        warnings.warn("parameter `IfExistCatalog` is deprecated", DeprecationWarning) 

        """Determine whether the audit log table has a catalog field.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IfExistCatalog

    @IfExistCatalog.setter
    def IfExistCatalog(self, IfExistCatalog):
        warnings.warn("parameter `IfExistCatalog` is deprecated", DeprecationWarning) 

        self._IfExistCatalog = IfExistCatalog

    @property
    def Characteristic(self):
        """Page features, used to block some page entrances on the front end.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Characteristic

    @Characteristic.setter
    def Characteristic(self, Characteristic):
        self._Characteristic = Characteristic

    @property
    def RestartTimeout(self):
        """Timeout period, in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RestartTimeout

    @RestartTimeout.setter
    def RestartTimeout(self, RestartTimeout):
        self._RestartTimeout = RestartTimeout

    @property
    def GraceShutdownWaitSeconds(self):
        """The timeout time for the graceful restart of the kernel. If it is -1, it means it is not set.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GraceShutdownWaitSeconds

    @GraceShutdownWaitSeconds.setter
    def GraceShutdownWaitSeconds(self, GraceShutdownWaitSeconds):
        self._GraceShutdownWaitSeconds = GraceShutdownWaitSeconds

    @property
    def CaseSensitive(self):
        """Whether the table name is case sensitive, 0 refers to sensitive, 1 refers to insensitive, compared in lowercase; 2 refers to insensitive, and the table name is changed to lowercase for storage.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def IsWhiteSGs(self):
        """Whether users can bind security groups.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsWhiteSGs

    @IsWhiteSGs.setter
    def IsWhiteSGs(self, IsWhiteSGs):
        self._IsWhiteSGs = IsWhiteSGs

    @property
    def BindSGs(self):
        """Bound security group information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._BindSGs

    @BindSGs.setter
    def BindSGs(self, BindSGs):
        self._BindSGs = BindSGs

    @property
    def EnableMultiZones(self):
        """Whether it is a multi-AZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableMultiZones

    @EnableMultiZones.setter
    def EnableMultiZones(self, EnableMultiZones):
        self._EnableMultiZones = EnableMultiZones

    @property
    def UserNetworkInfos(self):
        """User availability zone and subnet information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserNetworkInfos

    @UserNetworkInfos.setter
    def UserNetworkInfos(self, UserNetworkInfos):
        self._UserNetworkInfos = UserNetworkInfos

    @property
    def EnableCoolDown(self):
        """Whether to enable hot and cold stratification. 0 refers to disabled, and 1 refers to enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EnableCoolDown

    @EnableCoolDown.setter
    def EnableCoolDown(self, EnableCoolDown):
        self._EnableCoolDown = EnableCoolDown

    @property
    def CoolDownBucket(self):
        """COS buckets are used for hot and cold stratification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CoolDownBucket

    @CoolDownBucket.setter
    def CoolDownBucket(self, CoolDownBucket):
        self._CoolDownBucket = CoolDownBucket

    @property
    def Details(self):
        """Instance extension information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceDetail`
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def EnableDlc(self):
        """Whether to enable DLC. 0: disable; 1: enable.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EnableDlc

    @EnableDlc.setter
    def EnableDlc(self, EnableDlc):
        self._EnableDlc = EnableDlc

    @property
    def AccountType(self):
        """Account type. 0: ordinary user; 1: CAM user.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._Version = params.get("Version")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        if params.get("MasterSummary") is not None:
            self._MasterSummary = NodesSummary()
            self._MasterSummary._deserialize(params.get("MasterSummary"))
        if params.get("CoreSummary") is not None:
            self._CoreSummary = NodesSummary()
            self._CoreSummary._deserialize(params.get("CoreSummary"))
        self._HA = params.get("HA")
        self._HaType = params.get("HaType")
        self._AccessInfo = params.get("AccessInfo")
        self._Id = params.get("Id")
        self._RegionId = params.get("RegionId")
        self._ZoneDesc = params.get("ZoneDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._StatusDesc = params.get("StatusDesc")
        self._RenewFlag = params.get("RenewFlag")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Monitor = params.get("Monitor")
        self._HasClsTopic = params.get("HasClsTopic")
        self._ClsTopicId = params.get("ClsTopicId")
        self._ClsLogSetId = params.get("ClsLogSetId")
        self._EnableXMLConfig = params.get("EnableXMLConfig")
        self._RegionDesc = params.get("RegionDesc")
        self._Eip = params.get("Eip")
        self._CosMoveFactor = params.get("CosMoveFactor")
        self._Kind = params.get("Kind")
        self._CosBucketName = params.get("CosBucketName")
        self._CanAttachCbs = params.get("CanAttachCbs")
        self._BuildVersion = params.get("BuildVersion")
        self._Components = params.get("Components")
        self._IfExistCatalog = params.get("IfExistCatalog")
        self._Characteristic = params.get("Characteristic")
        self._RestartTimeout = params.get("RestartTimeout")
        self._GraceShutdownWaitSeconds = params.get("GraceShutdownWaitSeconds")
        self._CaseSensitive = params.get("CaseSensitive")
        self._IsWhiteSGs = params.get("IsWhiteSGs")
        self._BindSGs = params.get("BindSGs")
        self._EnableMultiZones = params.get("EnableMultiZones")
        self._UserNetworkInfos = params.get("UserNetworkInfos")
        self._EnableCoolDown = params.get("EnableCoolDown")
        self._CoolDownBucket = params.get("CoolDownBucket")
        if params.get("Details") is not None:
            self._Details = InstanceDetail()
            self._Details._deserialize(params.get("Details"))
        self._EnableDlc = params.get("EnableDlc")
        self._AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    """Instance node description information

    """

    def __init__(self):
        r"""
        :param _Ip: IP address
        :type Ip: str
        :param _Spec: Model, such as S1
        :type Spec: str
        :param _Core: Number of CPU cores
        :type Core: int
        :param _Memory: Memory size
        :type Memory: int
        :param _DiskType: Disk type
        :type DiskType: str
        :param _DiskSize: Disk size
        :type DiskSize: int
        :param _Role: The name of the clickhouse cluster to which it belongs.
        :type Role: str
        :param _Status: Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Rip: rip
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rip: str
        :param _FeRole: FE node role
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeRole: str
        :param _UUID: UUID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UUID: str
        """
        self._Ip = None
        self._Spec = None
        self._Core = None
        self._Memory = None
        self._DiskType = None
        self._DiskSize = None
        self._Role = None
        self._Status = None
        self._Rip = None
        self._FeRole = None
        self._UUID = None

    @property
    def Ip(self):
        """IP address
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Spec(self):
        """Model, such as S1
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Core(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._Core

    @Core.setter
    def Core(self, Core):
        self._Core = Core

    @property
    def Memory(self):
        """Memory size
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DiskType(self):
        """Disk type
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """Disk size
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Role(self):
        """The name of the clickhouse cluster to which it belongs.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        """Status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rip(self):
        """rip
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Rip

    @Rip.setter
    def Rip(self, Rip):
        self._Rip = Rip

    @property
    def FeRole(self):
        """FE node role
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FeRole

    @FeRole.setter
    def FeRole(self, FeRole):
        self._FeRole = FeRole

    @property
    def UUID(self):
        """UUID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UUID

    @UUID.setter
    def UUID(self, UUID):
        self._UUID = UUID


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Spec = params.get("Spec")
        self._Core = params.get("Core")
        self._Memory = params.get("Memory")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._Rip = params.get("Rip")
        self._FeRole = params.get("FeRole")
        self._UUID = params.get("UUID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceOperation(AbstractModel):
    """Cluster operation description

    """

    def __init__(self):
        r"""
        :param _Name: Operation name, such as create_instance, and scaleout_instance
        :type Name: str
        :param _Result: Operation result. Success indicates success; Fail indicates failure.
        :type Result: str
        :param _Desc: Operation name description, such as create, and modify the cluster name
        :type Desc: str
        :param _Level: Operation level, such as Critical, Normal
        :type Level: str
        :param _LevelDesc: Operation level description, such as high risk, and normal
        :type LevelDesc: str
        :param _StartTime: Operation start time
        :type StartTime: str
        :param _EndTime: Operation end time
        :type EndTime: str
        :param _ResultDesc: Operation result description, such as Success and Fail.
        :type ResultDesc: str
        :param _OperateUin: Operation user ID
        :type OperateUin: str
        :param _JobId: The jobid corresponding to the operation
        :type JobId: int
        :param _OperationDetail: Operation details
        :type OperationDetail: str
        """
        self._Name = None
        self._Result = None
        self._Desc = None
        self._Level = None
        self._LevelDesc = None
        self._StartTime = None
        self._EndTime = None
        self._ResultDesc = None
        self._OperateUin = None
        self._JobId = None
        self._OperationDetail = None

    @property
    def Name(self):
        """Operation name, such as create_instance, and scaleout_instance
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Result(self):
        """Operation result. Success indicates success; Fail indicates failure.
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Desc(self):
        """Operation name description, such as create, and modify the cluster name
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Level(self):
        """Operation level, such as Critical, Normal
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def LevelDesc(self):
        """Operation level description, such as high risk, and normal
        :rtype: str
        """
        return self._LevelDesc

    @LevelDesc.setter
    def LevelDesc(self, LevelDesc):
        self._LevelDesc = LevelDesc

    @property
    def StartTime(self):
        """Operation start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Operation end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ResultDesc(self):
        """Operation result description, such as Success and Fail.
        :rtype: str
        """
        return self._ResultDesc

    @ResultDesc.setter
    def ResultDesc(self, ResultDesc):
        self._ResultDesc = ResultDesc

    @property
    def OperateUin(self):
        """Operation user ID
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def JobId(self):
        """The jobid corresponding to the operation
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def OperationDetail(self):
        """Operation details
        :rtype: str
        """
        return self._OperationDetail

    @OperationDetail.setter
    def OperationDetail(self, OperationDetail):
        self._OperationDetail = OperationDetail


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Result = params.get("Result")
        self._Desc = params.get("Desc")
        self._Level = params.get("Level")
        self._LevelDesc = params.get("LevelDesc")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ResultDesc = params.get("ResultDesc")
        self._OperateUin = params.get("OperateUin")
        self._JobId = params.get("JobId")
        self._OperationDetail = params.get("OperationDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListInfo(AbstractModel):
    """List type partition information

    """

    def __init__(self):
        r"""
        :param _PartitionName: Partition name

Note: This field may return null, indicating that no valid values can be obtained.
        :type PartitionName: str
        :param _EnumValues: Enumeration values of each partition column

Note: This field may return null, indicating that no valid values can be obtained.
        :type EnumValues: list of str
        """
        self._PartitionName = None
        self._EnumValues = None

    @property
    def PartitionName(self):
        """Partition name

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PartitionName

    @PartitionName.setter
    def PartitionName(self, PartitionName):
        self._PartitionName = PartitionName

    @property
    def EnumValues(self):
        """Enumeration values of each partition column

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._EnumValues

    @EnumValues.setter
    def EnumValues(self, EnumValues):
        self._EnumValues = EnumValues


    def _deserialize(self, params):
        self._PartitionName = params.get("PartitionName")
        self._EnumValues = params.get("EnumValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterConfigsRequest(AbstractModel):
    """ModifyClusterConfigs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID, for example, cdwch-xxxx
        :type InstanceId: str
        :param _ModifyConfContext: Configuration file modification information
        :type ModifyConfContext: list of ConfigSubmitContext
        :param _Remark: Reason for modification
        :type Remark: str
        """
        self._InstanceId = None
        self._ModifyConfContext = None
        self._Remark = None

    @property
    def InstanceId(self):
        """Cluster ID, for example, cdwch-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ModifyConfContext(self):
        """Configuration file modification information
        :rtype: list of ConfigSubmitContext
        """
        return self._ModifyConfContext

    @ModifyConfContext.setter
    def ModifyConfContext(self, ModifyConfContext):
        self._ModifyConfContext = ModifyConfContext

    @property
    def Remark(self):
        """Reason for modification
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ModifyConfContext") is not None:
            self._ModifyConfContext = []
            for item in params.get("ModifyConfContext"):
                obj = ConfigSubmitContext()
                obj._deserialize(item)
                self._ModifyConfContext.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterConfigsResponse(AbstractModel):
    """ModifyClusterConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process related information
        :type FlowId: int
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process related information
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyCoolDownPolicyRequest(AbstractModel):
    """ModifyCoolDownPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _PolicyName: Policy name
        :type PolicyName: str
        :param _CoolDownTtl: cooldown_ttl
        :type CoolDownTtl: str
        :param _CoolDownDatetime: cooldown_datetime
        :type CoolDownDatetime: str
        """
        self._InstanceId = None
        self._PolicyName = None
        self._CoolDownTtl = None
        self._CoolDownDatetime = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        """Policy name
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CoolDownTtl(self):
        """cooldown_ttl
        :rtype: str
        """
        return self._CoolDownTtl

    @CoolDownTtl.setter
    def CoolDownTtl(self, CoolDownTtl):
        self._CoolDownTtl = CoolDownTtl

    @property
    def CoolDownDatetime(self):
        """cooldown_datetime
        :rtype: str
        """
        return self._CoolDownDatetime

    @CoolDownDatetime.setter
    def CoolDownDatetime(self, CoolDownDatetime):
        self._CoolDownDatetime = CoolDownDatetime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyName = params.get("PolicyName")
        self._CoolDownTtl = params.get("CoolDownTtl")
        self._CoolDownDatetime = params.get("CoolDownDatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCoolDownPolicyResponse(AbstractModel):
    """ModifyCoolDownPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyDatabaseTableAccessRequest(AbstractModel):
    """ModifyDatabaseTableAccess request structure.

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Privileges: Permission list
        :type Privileges: list of str
        :param _GrantOrRevoke: Operation type: GRANT or REVOKE
        :type GrantOrRevoke: str
        :param _InstanceId: InstanceId
        :type InstanceId: str
        :param _Table: Table name. If it is null, it indicates that the entire database is authorized.
        :type Table: str
        :param _Role: Role name, if authorized to the role
        :type Role: str
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _CatalogName: Catalog name, defaults to internal if not specified.
        :type CatalogName: str
        :param _WhiteHost: Machine Group, defaults to % if not specified.
        :type WhiteHost: str
        """
        self._Database = None
        self._Privileges = None
        self._GrantOrRevoke = None
        self._InstanceId = None
        self._Table = None
        self._Role = None
        self._UserName = None
        self._PassWord = None
        self._CatalogName = None
        self._WhiteHost = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Privileges(self):
        """Permission list
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def GrantOrRevoke(self):
        """Operation type: GRANT or REVOKE
        :rtype: str
        """
        return self._GrantOrRevoke

    @GrantOrRevoke.setter
    def GrantOrRevoke(self, GrantOrRevoke):
        self._GrantOrRevoke = GrantOrRevoke

    @property
    def InstanceId(self):
        """InstanceId
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Table(self):
        """Table name. If it is null, it indicates that the entire database is authorized.
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Role(self):
        """Role name, if authorized to the role
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def CatalogName(self):
        """Catalog name, defaults to internal if not specified.
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def WhiteHost(self):
        """Machine Group, defaults to % if not specified.
        :rtype: str
        """
        return self._WhiteHost

    @WhiteHost.setter
    def WhiteHost(self, WhiteHost):
        self._WhiteHost = WhiteHost


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Privileges = params.get("Privileges")
        self._GrantOrRevoke = params.get("GrantOrRevoke")
        self._InstanceId = params.get("InstanceId")
        self._Table = params.get("Table")
        self._Role = params.get("Role")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._CatalogName = params.get("CatalogName")
        self._WhiteHost = params.get("WhiteHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseTableAccessResponse(AbstractModel):
    """ModifyDatabaseTableAccess response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Whether the operation is successful
        :type Success: bool
        :param _Message: Error message
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._Message = None
        self._RequestId = None

    @property
    def Success(self):
        """Whether the operation is successful
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def Message(self):
        """Error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Success = params.get("Success")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class ModifyInstanceKeyValConfigsRequest(AbstractModel):
    """ModifyInstanceKeyValConfigs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _FileName: File name
        :type FileName: str
        :param _AddItems: Add configuration list
        :type AddItems: list of InstanceConfigItem
        :param _UpdateItems: Update configuration list
        :type UpdateItems: list of InstanceConfigItem
        :param _DelItems: Delete configuration list
        :type DelItems: list of InstanceConfigItem
        :param _Message: Remarks (within 50 words)
        :type Message: str
        :param _HotUpdateItems: Hot update list
        :type HotUpdateItems: list of InstanceConfigItem
        :param _DeleteItems: Delete configuration list
        :type DeleteItems: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceConfigItem`
        :param _IPAddress: IP address
        :type IPAddress: str
        """
        self._InstanceId = None
        self._FileName = None
        self._AddItems = None
        self._UpdateItems = None
        self._DelItems = None
        self._Message = None
        self._HotUpdateItems = None
        self._DeleteItems = None
        self._IPAddress = None

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
    def AddItems(self):
        """Add configuration list
        :rtype: list of InstanceConfigItem
        """
        return self._AddItems

    @AddItems.setter
    def AddItems(self, AddItems):
        self._AddItems = AddItems

    @property
    def UpdateItems(self):
        """Update configuration list
        :rtype: list of InstanceConfigItem
        """
        return self._UpdateItems

    @UpdateItems.setter
    def UpdateItems(self, UpdateItems):
        self._UpdateItems = UpdateItems

    @property
    def DelItems(self):
        """Delete configuration list
        :rtype: list of InstanceConfigItem
        """
        return self._DelItems

    @DelItems.setter
    def DelItems(self, DelItems):
        self._DelItems = DelItems

    @property
    def Message(self):
        """Remarks (within 50 words)
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def HotUpdateItems(self):
        """Hot update list
        :rtype: list of InstanceConfigItem
        """
        return self._HotUpdateItems

    @HotUpdateItems.setter
    def HotUpdateItems(self, HotUpdateItems):
        self._HotUpdateItems = HotUpdateItems

    @property
    def DeleteItems(self):
        """Delete configuration list
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceConfigItem`
        """
        return self._DeleteItems

    @DeleteItems.setter
    def DeleteItems(self, DeleteItems):
        self._DeleteItems = DeleteItems

    @property
    def IPAddress(self):
        """IP address
        :rtype: str
        """
        return self._IPAddress

    @IPAddress.setter
    def IPAddress(self, IPAddress):
        self._IPAddress = IPAddress


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileName = params.get("FileName")
        if params.get("AddItems") is not None:
            self._AddItems = []
            for item in params.get("AddItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self._AddItems.append(obj)
        if params.get("UpdateItems") is not None:
            self._UpdateItems = []
            for item in params.get("UpdateItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self._UpdateItems.append(obj)
        if params.get("DelItems") is not None:
            self._DelItems = []
            for item in params.get("DelItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self._DelItems.append(obj)
        self._Message = params.get("Message")
        if params.get("HotUpdateItems") is not None:
            self._HotUpdateItems = []
            for item in params.get("HotUpdateItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self._HotUpdateItems.append(obj)
        if params.get("DeleteItems") is not None:
            self._DeleteItems = InstanceConfigItem()
            self._DeleteItems._deserialize(params.get("DeleteItems"))
        self._IPAddress = params.get("IPAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceKeyValConfigsResponse(AbstractModel):
    """ModifyInstanceKeyValConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _FlowId: ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._FlowId = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def FlowId(self):
        """ID
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
        self._ErrorMsg = params.get("ErrorMsg")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Newly modified instance name
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

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
    def InstanceName(self):
        """Newly modified instance name
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
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance response structure.

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


class ModifyNodeStatusRequest(AbstractModel):
    """ModifyNodeStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID, such as cdwch-xxxx
        :type InstanceId: str
        :param _NodeInfos: Node information
        :type NodeInfos: list of NodeInfos
        :param _OperationCode: Node operation
        :type OperationCode: str
        :param _RestartTimeOut: Timeout period (s)
        :type RestartTimeOut: str
        """
        self._InstanceId = None
        self._NodeInfos = None
        self._OperationCode = None
        self._RestartTimeOut = None

    @property
    def InstanceId(self):
        """Cluster ID, such as cdwch-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeInfos(self):
        """Node information
        :rtype: list of NodeInfos
        """
        return self._NodeInfos

    @NodeInfos.setter
    def NodeInfos(self, NodeInfos):
        self._NodeInfos = NodeInfos

    @property
    def OperationCode(self):
        """Node operation
        :rtype: str
        """
        return self._OperationCode

    @OperationCode.setter
    def OperationCode(self, OperationCode):
        self._OperationCode = OperationCode

    @property
    def RestartTimeOut(self):
        """Timeout period (s)
        :rtype: str
        """
        return self._RestartTimeOut

    @RestartTimeOut.setter
    def RestartTimeOut(self, RestartTimeOut):
        self._RestartTimeOut = RestartTimeOut


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("NodeInfos") is not None:
            self._NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfos()
                obj._deserialize(item)
                self._NodeInfos.append(obj)
        self._OperationCode = params.get("OperationCode")
        self._RestartTimeOut = params.get("RestartTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodeStatusResponse(AbstractModel):
    """ModifyNodeStatus response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process related information
        :type FlowId: int
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process related information
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupsRequest(AbstractModel):
    """ModifySecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _OldSecurityGroupIds: Security group information before modification
        :type OldSecurityGroupIds: list of str
        :param _ModifySecurityGroupIds: Modified security group information
        :type ModifySecurityGroupIds: list of str
        """
        self._InstanceId = None
        self._OldSecurityGroupIds = None
        self._ModifySecurityGroupIds = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldSecurityGroupIds(self):
        """Security group information before modification
        :rtype: list of str
        """
        return self._OldSecurityGroupIds

    @OldSecurityGroupIds.setter
    def OldSecurityGroupIds(self, OldSecurityGroupIds):
        self._OldSecurityGroupIds = OldSecurityGroupIds

    @property
    def ModifySecurityGroupIds(self):
        """Modified security group information
        :rtype: list of str
        """
        return self._ModifySecurityGroupIds

    @ModifySecurityGroupIds.setter
    def ModifySecurityGroupIds(self, ModifySecurityGroupIds):
        self._ModifySecurityGroupIds = ModifySecurityGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldSecurityGroupIds = params.get("OldSecurityGroupIds")
        self._ModifySecurityGroupIds = params.get("ModifySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupsResponse(AbstractModel):
    """ModifySecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyUserBindWorkloadGroupRequest(AbstractModel):
    """ModifyUserBindWorkloadGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _BindUsers: The user information of the resource group needs to be bound. If an account has information of multiple hosts, all information needs to be uploaded.
        :type BindUsers: list of BindUser
        :param _OldWorkloadGroupName: Name of the resource group bound before modification
        :type OldWorkloadGroupName: str
        :param _NewWorkloadGroupName: Name of the resource group bound after modification
        :type NewWorkloadGroupName: str
        """
        self._InstanceId = None
        self._BindUsers = None
        self._OldWorkloadGroupName = None
        self._NewWorkloadGroupName = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BindUsers(self):
        """The user information of the resource group needs to be bound. If an account has information of multiple hosts, all information needs to be uploaded.
        :rtype: list of BindUser
        """
        return self._BindUsers

    @BindUsers.setter
    def BindUsers(self, BindUsers):
        self._BindUsers = BindUsers

    @property
    def OldWorkloadGroupName(self):
        """Name of the resource group bound before modification
        :rtype: str
        """
        return self._OldWorkloadGroupName

    @OldWorkloadGroupName.setter
    def OldWorkloadGroupName(self, OldWorkloadGroupName):
        self._OldWorkloadGroupName = OldWorkloadGroupName

    @property
    def NewWorkloadGroupName(self):
        """Name of the resource group bound after modification
        :rtype: str
        """
        return self._NewWorkloadGroupName

    @NewWorkloadGroupName.setter
    def NewWorkloadGroupName(self, NewWorkloadGroupName):
        self._NewWorkloadGroupName = NewWorkloadGroupName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("BindUsers") is not None:
            self._BindUsers = []
            for item in params.get("BindUsers"):
                obj = BindUser()
                obj._deserialize(item)
                self._BindUsers.append(obj)
        self._OldWorkloadGroupName = params.get("OldWorkloadGroupName")
        self._NewWorkloadGroupName = params.get("NewWorkloadGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserBindWorkloadGroupResponse(AbstractModel):
    """ModifyUserBindWorkloadGroup response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyUserPrivilegesV3Request(AbstractModel):
    """ModifyUserPrivilegesV3 request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _UserName: Username
        :type UserName: str
        :param _UserPrivileges: User permission
        :type UserPrivileges: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateUserPrivileges`
        :param _WhiteHost: The IP address of the user link	
        :type WhiteHost: str
        """
        self._InstanceId = None
        self._UserName = None
        self._UserPrivileges = None
        self._WhiteHost = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def UserPrivileges(self):
        """User permission
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateUserPrivileges`
        """
        return self._UserPrivileges

    @UserPrivileges.setter
    def UserPrivileges(self, UserPrivileges):
        self._UserPrivileges = UserPrivileges

    @property
    def WhiteHost(self):
        """The IP address of the user link	
        :rtype: str
        """
        return self._WhiteHost

    @WhiteHost.setter
    def WhiteHost(self, WhiteHost):
        self._WhiteHost = WhiteHost


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        if params.get("UserPrivileges") is not None:
            self._UserPrivileges = UpdateUserPrivileges()
            self._UserPrivileges._deserialize(params.get("UserPrivileges"))
        self._WhiteHost = params.get("WhiteHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserPrivilegesV3Response(AbstractModel):
    """ModifyUserPrivilegesV3 response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message; null means no error.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message; null means no error.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class ModifyWorkloadGroupRequest(AbstractModel):
    """ModifyWorkloadGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _WorkloadGroup: Modified resource group information
        :type WorkloadGroup: :class:`tencentcloud.cdwdoris.v20211228.models.WorkloadGroupConfig`
        """
        self._InstanceId = None
        self._WorkloadGroup = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WorkloadGroup(self):
        """Modified resource group information
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.WorkloadGroupConfig`
        """
        return self._WorkloadGroup

    @WorkloadGroup.setter
    def WorkloadGroup(self, WorkloadGroup):
        self._WorkloadGroup = WorkloadGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("WorkloadGroup") is not None:
            self._WorkloadGroup = WorkloadGroupConfig()
            self._WorkloadGroup._deserialize(params.get("WorkloadGroup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkloadGroupResponse(AbstractModel):
    """ModifyWorkloadGroup response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message	
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message	
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyWorkloadGroupStatusRequest(AbstractModel):
    """ModifyWorkloadGroupStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _OperationType: Whether to enable resource group: open and close
        :type OperationType: str
        """
        self._InstanceId = None
        self._OperationType = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OperationType(self):
        """Whether to enable resource group: open and close
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkloadGroupStatusResponse(AbstractModel):
    """ModifyWorkloadGroupStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message	
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message	
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class NetworkInfo(AbstractModel):
    """Network information

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _SubnetId: Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _SubnetIpNum: The number of available IP addresses in the current subnet
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetIpNum: int
        """
        self._Zone = None
        self._SubnetId = None
        self._SubnetIpNum = None

    @property
    def Zone(self):
        """Availability zone
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        """Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetIpNum(self):
        """The number of available IP addresses in the current subnet
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SubnetIpNum

    @SubnetIpNum.setter
    def SubnetIpNum(self, SubnetIpNum):
        self._SubnetIpNum = SubnetIpNum


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        self._SubnetIpNum = params.get("SubnetIpNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """NodeInfo

    """

    def __init__(self):
        r"""
        :param _Ip: User IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param _Status: Node status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _NodeName: Node role name
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeName: str
        :param _ComponentName: Component name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentName: str
        :param _NodeRole: Node role
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeRole: str
        :param _LastRestartTime: The time when the node was last restarted
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastRestartTime: str
        :param _Zone: The availability zone where the node is located
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        """
        self._Ip = None
        self._Status = None
        self._NodeName = None
        self._ComponentName = None
        self._NodeRole = None
        self._LastRestartTime = None
        self._Zone = None

    @property
    def Ip(self):
        """User IP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Status(self):
        """Node status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NodeName(self):
        """Node role name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def ComponentName(self):
        """Component name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def NodeRole(self):
        """Node role
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def LastRestartTime(self):
        """The time when the node was last restarted
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastRestartTime

    @LastRestartTime.setter
    def LastRestartTime(self, LastRestartTime):
        self._LastRestartTime = LastRestartTime

    @property
    def Zone(self):
        """The availability zone where the node is located
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Status = params.get("Status")
        self._NodeName = params.get("NodeName")
        self._ComponentName = params.get("ComponentName")
        self._NodeRole = params.get("NodeRole")
        self._LastRestartTime = params.get("LastRestartTime")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfos(AbstractModel):
    """Node information list

    """

    def __init__(self):
        r"""
        :param _NodeName: Node name
        :type NodeName: str
        :param _Status: Node status
        :type Status: int
        :param _Ip: Node IP
        :type Ip: str
        :param _NodeRole: Node role
        :type NodeRole: str
        :param _ComponentName: Component name
        :type ComponentName: str
        :param _LastRestartTime: Last restart time
        :type LastRestartTime: str
        """
        self._NodeName = None
        self._Status = None
        self._Ip = None
        self._NodeRole = None
        self._ComponentName = None
        self._LastRestartTime = None

    @property
    def NodeName(self):
        """Node name
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Status(self):
        """Node status
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ip(self):
        """Node IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def NodeRole(self):
        """Node role
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def ComponentName(self):
        """Component name
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def LastRestartTime(self):
        """Last restart time
        :rtype: str
        """
        return self._LastRestartTime

    @LastRestartTime.setter
    def LastRestartTime(self, LastRestartTime):
        self._LastRestartTime = LastRestartTime


    def _deserialize(self, params):
        self._NodeName = params.get("NodeName")
        self._Status = params.get("Status")
        self._Ip = params.get("Ip")
        self._NodeRole = params.get("NodeRole")
        self._ComponentName = params.get("ComponentName")
        self._LastRestartTime = params.get("LastRestartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodesSummary(AbstractModel):
    """Node role description information

    """

    def __init__(self):
        r"""
        :param _Spec: Model, such as S1
        :type Spec: str
        :param _NodeSize: Number of nodes
        :type NodeSize: int
        :param _Core: Number of CPU cores, in counts
        :type Core: int
        :param _Memory: Memory size, in GB
        :type Memory: int
        :param _Disk: Disk size, in GB
        :type Disk: int
        :param _DiskType: Disk type
        :type DiskType: str
        :param _DiskDesc: Disk description
        :type DiskDesc: str
        :param _AttachCBSSpec: Information of mounted cloud disks
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttachCBSSpec: :class:`tencentcloud.cdwdoris.v20211228.models.AttachCBSSpec`
        :param _SubProductType: Sub-product name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubProductType: str
        :param _SpecCore: Specified cores
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecCore: int
        :param _SpecMemory: Specified memory
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecMemory: int
        :param _DiskCount: Disk size
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskCount: int
        :param _Encrypt: Whether it is encrypted.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Encrypt: int
        :param _MaxDiskSize: Maximum disk
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxDiskSize: int
        """
        self._Spec = None
        self._NodeSize = None
        self._Core = None
        self._Memory = None
        self._Disk = None
        self._DiskType = None
        self._DiskDesc = None
        self._AttachCBSSpec = None
        self._SubProductType = None
        self._SpecCore = None
        self._SpecMemory = None
        self._DiskCount = None
        self._Encrypt = None
        self._MaxDiskSize = None

    @property
    def Spec(self):
        """Model, such as S1
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def NodeSize(self):
        """Number of nodes
        :rtype: int
        """
        return self._NodeSize

    @NodeSize.setter
    def NodeSize(self, NodeSize):
        self._NodeSize = NodeSize

    @property
    def Core(self):
        """Number of CPU cores, in counts
        :rtype: int
        """
        return self._Core

    @Core.setter
    def Core(self, Core):
        self._Core = Core

    @property
    def Memory(self):
        """Memory size, in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        """Disk size, in GB
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def DiskType(self):
        """Disk type
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        """Disk description
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def AttachCBSSpec(self):
        """Information of mounted cloud disks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.AttachCBSSpec`
        """
        return self._AttachCBSSpec

    @AttachCBSSpec.setter
    def AttachCBSSpec(self, AttachCBSSpec):
        self._AttachCBSSpec = AttachCBSSpec

    @property
    def SubProductType(self):
        """Sub-product name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubProductType

    @SubProductType.setter
    def SubProductType(self, SubProductType):
        self._SubProductType = SubProductType

    @property
    def SpecCore(self):
        """Specified cores
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SpecCore

    @SpecCore.setter
    def SpecCore(self, SpecCore):
        self._SpecCore = SpecCore

    @property
    def SpecMemory(self):
        """Specified memory
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SpecMemory

    @SpecMemory.setter
    def SpecMemory(self, SpecMemory):
        self._SpecMemory = SpecMemory

    @property
    def DiskCount(self):
        """Disk size
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def Encrypt(self):
        """Whether it is encrypted.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def MaxDiskSize(self):
        """Maximum disk
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._NodeSize = params.get("NodeSize")
        self._Core = params.get("Core")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._DiskType = params.get("DiskType")
        self._DiskDesc = params.get("DiskDesc")
        if params.get("AttachCBSSpec") is not None:
            self._AttachCBSSpec = AttachCBSSpec()
            self._AttachCBSSpec._deserialize(params.get("AttachCBSSpec"))
        self._SubProductType = params.get("SubProductType")
        self._SpecCore = params.get("SpecCore")
        self._SpecMemory = params.get("SpecMemory")
        self._DiskCount = params.get("DiskCount")
        self._Encrypt = params.get("Encrypt")
        self._MaxDiskSize = params.get("MaxDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenCoolDownPolicyRequest(AbstractModel):
    """OpenCoolDownPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DatabaseName: DB name
        :type DatabaseName: str
        :param _TableName: Table name
        :type TableName: str
        :param _OperationType: Operation type
        :type OperationType: str
        :param _BatchOpenCoolDownTables: Separate with commas. The DB name is required, for example, db1.tb1,db1.tb2,db2.tb1.
        :type BatchOpenCoolDownTables: str
        :param _PolicyName: Policy name required for binding
        :type PolicyName: str
        :param _BatchOpenCoolDownPartitions: Separate with commas, for example, p1,p2,p3.
        :type BatchOpenCoolDownPartitions: str
        """
        self._InstanceId = None
        self._DatabaseName = None
        self._TableName = None
        self._OperationType = None
        self._BatchOpenCoolDownTables = None
        self._PolicyName = None
        self._BatchOpenCoolDownPartitions = None

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
    def DatabaseName(self):
        """DB name
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        """Table name
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def OperationType(self):
        """Operation type
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def BatchOpenCoolDownTables(self):
        """Separate with commas. The DB name is required, for example, db1.tb1,db1.tb2,db2.tb1.
        :rtype: str
        """
        return self._BatchOpenCoolDownTables

    @BatchOpenCoolDownTables.setter
    def BatchOpenCoolDownTables(self, BatchOpenCoolDownTables):
        self._BatchOpenCoolDownTables = BatchOpenCoolDownTables

    @property
    def PolicyName(self):
        """Policy name required for binding
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def BatchOpenCoolDownPartitions(self):
        """Separate with commas, for example, p1,p2,p3.
        :rtype: str
        """
        return self._BatchOpenCoolDownPartitions

    @BatchOpenCoolDownPartitions.setter
    def BatchOpenCoolDownPartitions(self, BatchOpenCoolDownPartitions):
        self._BatchOpenCoolDownPartitions = BatchOpenCoolDownPartitions


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._OperationType = params.get("OperationType")
        self._BatchOpenCoolDownTables = params.get("BatchOpenCoolDownTables")
        self._PolicyName = params.get("PolicyName")
        self._BatchOpenCoolDownPartitions = params.get("BatchOpenCoolDownPartitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenCoolDownPolicyResponse(AbstractModel):
    """OpenCoolDownPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _QueryDocument: Returned information
        :type QueryDocument: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._QueryDocument = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def QueryDocument(self):
        """Returned information
        :rtype: str
        """
        return self._QueryDocument

    @QueryDocument.setter
    def QueryDocument(self, QueryDocument):
        self._QueryDocument = QueryDocument

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._QueryDocument = params.get("QueryDocument")
        self._RequestId = params.get("RequestId")


class OpenCoolDownRequest(AbstractModel):
    """OpenCoolDown request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Cluster ID
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
        


class OpenCoolDownResponse(AbstractModel):
    """OpenCoolDown response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class Partition(AbstractModel):
    """Partition information of the table

    """

    def __init__(self):
        r"""
        :param _PartitionType: Partition type:
●Range: The partition column is usually of time or integer type. Four writing methods are supported.
●List: The partition value is an enumeration value.

Note: This field may return null, indicating that no valid values can be obtained.
        :type PartitionType: str
        :param _AutoPartition: Whether to automatically partition

Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoPartition: bool
        :param _RangeInfos: Partition information when the partition type is Range

Note: This field may return null, indicating that no valid values can be obtained.
        :type RangeInfos: list of RangeInfo
        :param _ListInfos: Partition information when the partition type is List

Note: This field may return null, indicating that no valid values can be obtained.
        :type ListInfos: list of ListInfo
        """
        self._PartitionType = None
        self._AutoPartition = None
        self._RangeInfos = None
        self._ListInfos = None

    @property
    def PartitionType(self):
        """Partition type:
●Range: The partition column is usually of time or integer type. Four writing methods are supported.
●List: The partition value is an enumeration value.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def AutoPartition(self):
        """Whether to automatically partition

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._AutoPartition

    @AutoPartition.setter
    def AutoPartition(self, AutoPartition):
        self._AutoPartition = AutoPartition

    @property
    def RangeInfos(self):
        """Partition information when the partition type is Range

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RangeInfo
        """
        return self._RangeInfos

    @RangeInfos.setter
    def RangeInfos(self, RangeInfos):
        self._RangeInfos = RangeInfos

    @property
    def ListInfos(self):
        """Partition information when the partition type is List

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ListInfo
        """
        return self._ListInfos

    @ListInfos.setter
    def ListInfos(self, ListInfos):
        self._ListInfos = ListInfos


    def _deserialize(self, params):
        self._PartitionType = params.get("PartitionType")
        self._AutoPartition = params.get("AutoPartition")
        if params.get("RangeInfos") is not None:
            self._RangeInfos = []
            for item in params.get("RangeInfos"):
                obj = RangeInfo()
                obj._deserialize(item)
                self._RangeInfos.append(obj)
        if params.get("ListInfos") is not None:
            self._ListInfos = []
            for item in params.get("ListInfos"):
                obj = ListInfo()
                obj._deserialize(item)
                self._ListInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermissionHostInfo(AbstractModel):
    """Permission overview

    """

    def __init__(self):
        r"""
        :param _GlobalPermissions: A list of user permissions in the global scope, which can be applied to all databases and tables.

Note: This field may return null, indicating that no valid values can be obtained.
        :type GlobalPermissions: list of str
        :param _DatabasePermissions: The key is the database name, and the value is the permission list of the user on the database.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabasePermissions: list of DatabasePermissions
        :param _TablePermissions: The key is the full name of the table, and the value is the permission list of the user on the table.

Note: This field may return null, indicating that no valid values can be obtained.
        :type TablePermissions: list of TablePermissions
        :param _CatalogPermissions: The key is the full name of the catalog, and the value is the permission list of the user on the catalog.

Note: This field may return null, indicating that no valid values can be obtained.
        :type CatalogPermissions: list of CatalogPermission
        """
        self._GlobalPermissions = None
        self._DatabasePermissions = None
        self._TablePermissions = None
        self._CatalogPermissions = None

    @property
    def GlobalPermissions(self):
        """A list of user permissions in the global scope, which can be applied to all databases and tables.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._GlobalPermissions

    @GlobalPermissions.setter
    def GlobalPermissions(self, GlobalPermissions):
        self._GlobalPermissions = GlobalPermissions

    @property
    def DatabasePermissions(self):
        """The key is the database name, and the value is the permission list of the user on the database.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatabasePermissions
        """
        return self._DatabasePermissions

    @DatabasePermissions.setter
    def DatabasePermissions(self, DatabasePermissions):
        self._DatabasePermissions = DatabasePermissions

    @property
    def TablePermissions(self):
        """The key is the full name of the table, and the value is the permission list of the user on the table.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TablePermissions
        """
        return self._TablePermissions

    @TablePermissions.setter
    def TablePermissions(self, TablePermissions):
        self._TablePermissions = TablePermissions

    @property
    def CatalogPermissions(self):
        """The key is the full name of the catalog, and the value is the permission list of the user on the catalog.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CatalogPermission
        """
        return self._CatalogPermissions

    @CatalogPermissions.setter
    def CatalogPermissions(self, CatalogPermissions):
        self._CatalogPermissions = CatalogPermissions


    def _deserialize(self, params):
        self._GlobalPermissions = params.get("GlobalPermissions")
        if params.get("DatabasePermissions") is not None:
            self._DatabasePermissions = []
            for item in params.get("DatabasePermissions"):
                obj = DatabasePermissions()
                obj._deserialize(item)
                self._DatabasePermissions.append(obj)
        if params.get("TablePermissions") is not None:
            self._TablePermissions = []
            for item in params.get("TablePermissions"):
                obj = TablePermissions()
                obj._deserialize(item)
                self._TablePermissions.append(obj)
        if params.get("CatalogPermissions") is not None:
            self._CatalogPermissions = []
            for item in params.get("CatalogPermissions"):
                obj = CatalogPermission()
                obj._deserialize(item)
                self._CatalogPermissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PropertiesMap(AbstractModel):
    """Property attribute

    """

    def __init__(self):
        r"""
        :param _PropertyKey: key
Note: This field may return null, indicating that no valid values can be obtained.
        :type PropertyKey: str
        :param _PropertyValue: value
Note: This field may return null, indicating that no valid values can be obtained.
        :type PropertyValue: str
        """
        self._PropertyKey = None
        self._PropertyValue = None

    @property
    def PropertyKey(self):
        """key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PropertyKey

    @PropertyKey.setter
    def PropertyKey(self, PropertyKey):
        self._PropertyKey = PropertyKey

    @property
    def PropertyValue(self):
        """value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PropertyValue

    @PropertyValue.setter
    def PropertyValue(self, PropertyValue):
        self._PropertyValue = PropertyValue


    def _deserialize(self, params):
        self._PropertyKey = params.get("PropertyKey")
        self._PropertyValue = params.get("PropertyValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Property(AbstractModel):
    """Attribute information of databases, tables, indexes, etc.

    """

    def __init__(self):
        r"""
        :param _PropertyKey: Attribute key
Note: This field may return null, indicating that no valid values can be obtained.
        :type PropertyKey: str
        :param _PropertyValue: Attribute value
Note: This field may return null, indicating that no valid values can be obtained.
        :type PropertyValue: str
        """
        self._PropertyKey = None
        self._PropertyValue = None

    @property
    def PropertyKey(self):
        """Attribute key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PropertyKey

    @PropertyKey.setter
    def PropertyKey(self, PropertyKey):
        self._PropertyKey = PropertyKey

    @property
    def PropertyValue(self):
        """Attribute value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PropertyValue

    @PropertyValue.setter
    def PropertyValue(self, PropertyValue):
        self._PropertyValue = PropertyValue


    def _deserialize(self, params):
        self._PropertyKey = params.get("PropertyKey")
        self._PropertyValue = params.get("PropertyValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDetails(AbstractModel):
    """Query and analyze details

    """

    def __init__(self):
        r"""
        :param _Initiator: Initiating User
Note: This field may return null, indicating that no valid values can be obtained.
        :type Initiator: str
        :param _SourceAddress: Access source address

Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceAddress: str
        :param _InitialRequestId: Initial request ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InitialRequestId: str
        :param _Catalog: catalog name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Catalog: str
        :param _Database: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param _SQLType: SQL Type: 0 is non-query, 1 is query, -1 is unrestricted.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SQLType: str
        :param _SQLStatement: SQL statement
Note: This field may return null, indicating that no valid values can be obtained.
        :type SQLStatement: str
        :param _StartTime: Execution start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _Duration: Runtime (s)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Duration: int
        :param _RowsRead: The number of read rows
Note: This field may return null, indicating that no valid values can be obtained.
        :type RowsRead: int
        :param _DataRead: Read data volume (MB)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataRead: float
        :param _MemoryUsage: Memory usage (MB)
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemoryUsage: float
        """
        self._Initiator = None
        self._SourceAddress = None
        self._InitialRequestId = None
        self._Catalog = None
        self._Database = None
        self._SQLType = None
        self._SQLStatement = None
        self._StartTime = None
        self._Duration = None
        self._RowsRead = None
        self._DataRead = None
        self._MemoryUsage = None

    @property
    def Initiator(self):
        """Initiating User
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Initiator

    @Initiator.setter
    def Initiator(self, Initiator):
        self._Initiator = Initiator

    @property
    def SourceAddress(self):
        """Access source address

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceAddress

    @SourceAddress.setter
    def SourceAddress(self, SourceAddress):
        self._SourceAddress = SourceAddress

    @property
    def InitialRequestId(self):
        """Initial request ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InitialRequestId

    @InitialRequestId.setter
    def InitialRequestId(self, InitialRequestId):
        self._InitialRequestId = InitialRequestId

    @property
    def Catalog(self):
        """catalog name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Database(self):
        """Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def SQLType(self):
        """SQL Type: 0 is non-query, 1 is query, -1 is unrestricted.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SQLType

    @SQLType.setter
    def SQLType(self, SQLType):
        self._SQLType = SQLType

    @property
    def SQLStatement(self):
        """SQL statement
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SQLStatement

    @SQLStatement.setter
    def SQLStatement(self, SQLStatement):
        self._SQLStatement = SQLStatement

    @property
    def StartTime(self):
        """Execution start time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        """Runtime (s)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RowsRead(self):
        """The number of read rows
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RowsRead

    @RowsRead.setter
    def RowsRead(self, RowsRead):
        self._RowsRead = RowsRead

    @property
    def DataRead(self):
        """Read data volume (MB)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._DataRead

    @DataRead.setter
    def DataRead(self, DataRead):
        self._DataRead = DataRead

    @property
    def MemoryUsage(self):
        """Memory usage (MB)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage


    def _deserialize(self, params):
        self._Initiator = params.get("Initiator")
        self._SourceAddress = params.get("SourceAddress")
        self._InitialRequestId = params.get("InitialRequestId")
        self._Catalog = params.get("Catalog")
        self._Database = params.get("Database")
        self._SQLType = params.get("SQLType")
        self._SQLStatement = params.get("SQLStatement")
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        self._RowsRead = params.get("RowsRead")
        self._DataRead = params.get("DataRead")
        self._MemoryUsage = params.get("MemoryUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTableDataRequest(AbstractModel):
    """QueryTableData request structure.

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Table: Table name
        :type Table: str
        :param _InstanceId: InstanceId
        :type InstanceId: str
        :param _SelectedFields: Array of fields to be queried
        :type SelectedFields: list of str
        :param _PageNum: Page number, which is 1 by default.
        :type PageNum: int
        :param _PageSize: Number of records per page, which is 10 by default.
        :type PageSize: int
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _CatalogName: Catalog name, defaults to 'internal' if not specified.

        :type CatalogName: str
        """
        self._Database = None
        self._Table = None
        self._InstanceId = None
        self._SelectedFields = None
        self._PageNum = None
        self._PageSize = None
        self._UserName = None
        self._PassWord = None
        self._CatalogName = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """Table name
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def InstanceId(self):
        """InstanceId
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SelectedFields(self):
        """Array of fields to be queried
        :rtype: list of str
        """
        return self._SelectedFields

    @SelectedFields.setter
    def SelectedFields(self, SelectedFields):
        self._SelectedFields = SelectedFields

    @property
    def PageNum(self):
        """Page number, which is 1 by default.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Number of records per page, which is 10 by default.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def CatalogName(self):
        """Catalog name, defaults to 'internal' if not specified.

        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._InstanceId = params.get("InstanceId")
        self._SelectedFields = params.get("SelectedFields")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._CatalogName = params.get("CatalogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTableDataResponse(AbstractModel):
    """QueryTableData response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total records of query results
        :type TotalCount: int
        :param _Fields: Field name array of query results
        :type Fields: list of str
        :param _FieldTypes: Field type array of query results
        :type FieldTypes: list of str
        :param _Rows: Returned data record array. Each element is an array, containing the value of the corresponding field.
        :type Rows: list of Rows
        :param _Message: Error message
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Fields = None
        self._FieldTypes = None
        self._Rows = None
        self._Message = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total records of query results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Fields(self):
        """Field name array of query results
        :rtype: list of str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def FieldTypes(self):
        """Field type array of query results
        :rtype: list of str
        """
        return self._FieldTypes

    @FieldTypes.setter
    def FieldTypes(self, FieldTypes):
        self._FieldTypes = FieldTypes

    @property
    def Rows(self):
        """Returned data record array. Each element is an array, containing the value of the corresponding field.
        :rtype: list of Rows
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def Message(self):
        """Error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Fields = params.get("Fields")
        self._FieldTypes = params.get("FieldTypes")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = Rows()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class RangeInfo(AbstractModel):
    """Information of Range type partition

    """

    def __init__(self):
        r"""
        :param _RangeType: Range partition type:
●FIXED: Define the left closed and right open interval of the partition.
●LESS THAN: Only define the upper bound of the partition.
●BATCH RANGE: Batch create RANGE partitions of numeric and time types, define the left closed and right open intervals of the partitions, and set the step size.

Note: This field may return null, indicating that no valid values can be obtained.
        :type RangeType: str
        :param _PartitionName: Partition name
Note: This field may return null, indicating that no valid values can be obtained.
        :type PartitionName: str
        :param _Left: The left-closed interval of each partition column when RangeType is FIXED or BATCH RANGE

Note: This field may return null, indicating that no valid values can be obtained.
        :type Left: str
        :param _Right: The right open interval of each partition column when RangeType is FIXED or BATCH RANGE

Note: This field may return null, indicating that no valid values can be obtained.
        :type Right: str
        :param _Max: The upper bound of each partition column when RangeType is LESS THAN

Note: This field may return null, indicating that no valid values can be obtained.
        :type Max: str
        :param _StepLength: RangeType is the step size of BATCH RANGE

Note: This field may return null, indicating that no valid values can be obtained.
        :type StepLength: int
        :param _Unit: Fill it in when RangeType is BATCH RANGE or automatic partitioning. It indicates the step size unit when the partition column is of time type.
●YEAR: year
●MONTH: month
●WEEK: week
●DAY: day

Note: This field may return null, indicating that no valid values can be obtained.
        :type Unit: str
        """
        self._RangeType = None
        self._PartitionName = None
        self._Left = None
        self._Right = None
        self._Max = None
        self._StepLength = None
        self._Unit = None

    @property
    def RangeType(self):
        """Range partition type:
●FIXED: Define the left closed and right open interval of the partition.
●LESS THAN: Only define the upper bound of the partition.
●BATCH RANGE: Batch create RANGE partitions of numeric and time types, define the left closed and right open intervals of the partitions, and set the step size.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RangeType

    @RangeType.setter
    def RangeType(self, RangeType):
        self._RangeType = RangeType

    @property
    def PartitionName(self):
        """Partition name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PartitionName

    @PartitionName.setter
    def PartitionName(self, PartitionName):
        self._PartitionName = PartitionName

    @property
    def Left(self):
        """The left-closed interval of each partition column when RangeType is FIXED or BATCH RANGE

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Right(self):
        """The right open interval of each partition column when RangeType is FIXED or BATCH RANGE

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Right

    @Right.setter
    def Right(self, Right):
        self._Right = Right

    @property
    def Max(self):
        """The upper bound of each partition column when RangeType is LESS THAN

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def StepLength(self):
        """RangeType is the step size of BATCH RANGE

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepLength

    @StepLength.setter
    def StepLength(self, StepLength):
        self._StepLength = StepLength

    @property
    def Unit(self):
        """Fill it in when RangeType is BATCH RANGE or automatic partitioning. It indicates the step size unit when the partition column is of time type.
●YEAR: year
●MONTH: month
●WEEK: week
●DAY: day

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._RangeType = params.get("RangeType")
        self._PartitionName = params.get("PartitionName")
        self._Left = params.get("Left")
        self._Right = params.get("Right")
        self._Max = params.get("Max")
        self._StepLength = params.get("StepLength")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverBackUpJobRequest(AbstractModel):
    """RecoverBackUpJob request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _BackUpJobId: Task ID
        :type BackUpJobId: int
        :param _ReplicationNum: Number of new table replicas recovered
        :type ReplicationNum: int
        :param _ReserveSourceConfig: Whether to retain the configuration in the source table during recovery. 1 indicates that the configurations in the source table are retained.
        :type ReserveSourceConfig: int
        :param _RecoverType: 0: default; 1: cos recovery
        :type RecoverType: int
        :param _CosSourceInfo: CosSourceInfo object
        :type CosSourceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        :param _ScheduleType: 0: default; 1: regular execution
        :type ScheduleType: int
        :param _NextTime: YY-MM-DD Hour : Minute : Second
        :type NextTime: str
        :param _ScheduleName: Scheduling name
        :type ScheduleName: str
        :param _OperationType: create update
        :type OperationType: str
        :param _RecoverScope: Recovery granularity: All, Database, and Table
        :type RecoverScope: str
        :param _RecoverDatabase: Recover database: If you back up by database, this field is required. Use commas to separate databases.
        :type RecoverDatabase: str
        """
        self._InstanceId = None
        self._BackUpJobId = None
        self._ReplicationNum = None
        self._ReserveSourceConfig = None
        self._RecoverType = None
        self._CosSourceInfo = None
        self._ScheduleType = None
        self._NextTime = None
        self._ScheduleName = None
        self._OperationType = None
        self._RecoverScope = None
        self._RecoverDatabase = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackUpJobId(self):
        """Task ID
        :rtype: int
        """
        return self._BackUpJobId

    @BackUpJobId.setter
    def BackUpJobId(self, BackUpJobId):
        self._BackUpJobId = BackUpJobId

    @property
    def ReplicationNum(self):
        """Number of new table replicas recovered
        :rtype: int
        """
        return self._ReplicationNum

    @ReplicationNum.setter
    def ReplicationNum(self, ReplicationNum):
        self._ReplicationNum = ReplicationNum

    @property
    def ReserveSourceConfig(self):
        """Whether to retain the configuration in the source table during recovery. 1 indicates that the configurations in the source table are retained.
        :rtype: int
        """
        return self._ReserveSourceConfig

    @ReserveSourceConfig.setter
    def ReserveSourceConfig(self, ReserveSourceConfig):
        self._ReserveSourceConfig = ReserveSourceConfig

    @property
    def RecoverType(self):
        """0: default; 1: cos recovery
        :rtype: int
        """
        return self._RecoverType

    @RecoverType.setter
    def RecoverType(self, RecoverType):
        self._RecoverType = RecoverType

    @property
    def CosSourceInfo(self):
        """CosSourceInfo object
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CosSourceInfo`
        """
        return self._CosSourceInfo

    @CosSourceInfo.setter
    def CosSourceInfo(self, CosSourceInfo):
        self._CosSourceInfo = CosSourceInfo

    @property
    def ScheduleType(self):
        """0: default; 1: regular execution
        :rtype: int
        """
        return self._ScheduleType

    @ScheduleType.setter
    def ScheduleType(self, ScheduleType):
        self._ScheduleType = ScheduleType

    @property
    def NextTime(self):
        """YY-MM-DD Hour : Minute : Second
        :rtype: str
        """
        return self._NextTime

    @NextTime.setter
    def NextTime(self, NextTime):
        self._NextTime = NextTime

    @property
    def ScheduleName(self):
        """Scheduling name
        :rtype: str
        """
        return self._ScheduleName

    @ScheduleName.setter
    def ScheduleName(self, ScheduleName):
        self._ScheduleName = ScheduleName

    @property
    def OperationType(self):
        """create update
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def RecoverScope(self):
        """Recovery granularity: All, Database, and Table
        :rtype: str
        """
        return self._RecoverScope

    @RecoverScope.setter
    def RecoverScope(self, RecoverScope):
        self._RecoverScope = RecoverScope

    @property
    def RecoverDatabase(self):
        """Recover database: If you back up by database, this field is required. Use commas to separate databases.
        :rtype: str
        """
        return self._RecoverDatabase

    @RecoverDatabase.setter
    def RecoverDatabase(self, RecoverDatabase):
        self._RecoverDatabase = RecoverDatabase


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackUpJobId = params.get("BackUpJobId")
        self._ReplicationNum = params.get("ReplicationNum")
        self._ReserveSourceConfig = params.get("ReserveSourceConfig")
        self._RecoverType = params.get("RecoverType")
        if params.get("CosSourceInfo") is not None:
            self._CosSourceInfo = CosSourceInfo()
            self._CosSourceInfo._deserialize(params.get("CosSourceInfo"))
        self._ScheduleType = params.get("ScheduleType")
        self._NextTime = params.get("NextTime")
        self._ScheduleName = params.get("ScheduleName")
        self._OperationType = params.get("OperationType")
        self._RecoverScope = params.get("RecoverScope")
        self._RecoverDatabase = params.get("RecoverDatabase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverBackUpJobResponse(AbstractModel):
    """RecoverBackUpJob response structure.

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


class ReduceInstanceRequest(AbstractModel):
    """ReduceInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _DelHosts: Node list
        :type DelHosts: list of str
        :param _Type: Role (MATER/CORE), MASTER corresponds to FE, CORE corresponds to BE.
        :type Type: str
        :param _HaType: High availability cluster type after scale-in. 0: non-high availability; 1: read high availability; 2: read-write high availability
        :type HaType: int
        """
        self._InstanceId = None
        self._DelHosts = None
        self._Type = None
        self._HaType = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DelHosts(self):
        """Node list
        :rtype: list of str
        """
        return self._DelHosts

    @DelHosts.setter
    def DelHosts(self, DelHosts):
        self._DelHosts = DelHosts

    @property
    def Type(self):
        """Role (MATER/CORE), MASTER corresponds to FE, CORE corresponds to BE.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HaType(self):
        """High availability cluster type after scale-in. 0: non-high availability; 1: read high availability; 2: read-write high availability
        :rtype: int
        """
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DelHosts = params.get("DelHosts")
        self._Type = params.get("Type")
        self._HaType = params.get("HaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReduceInstanceResponse(AbstractModel):
    """ReduceInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID
        :type FlowId: str
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class RegionAreaInfo(AbstractModel):
    """Description of the region categories for availability zones

    """

    def __init__(self):
        r"""
        :param _Name: Region category information, such as south_china, east_china, etc.
        :type Name: str
        :param _Desc: Description of the corresponding Name, such as South China, East China, etc.
        :type Desc: str
        :param _Regions: Specific region list 1
        :type Regions: list of RegionInfo
        """
        self._Name = None
        self._Desc = None
        self._Regions = None

    @property
    def Name(self):
        """Region category information, such as south_china, east_china, etc.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        """Description of the corresponding Name, such as South China, East China, etc.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Regions(self):
        """Specific region list 1
        :rtype: list of RegionInfo
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._Regions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    """Region description information

    """

    def __init__(self):
        r"""
        :param _Name: Region name, such as ap-guangzhou
        :type Name: str
        :param _Desc: Region description, such as Guangzhou
        :type Desc: str
        :param _RegionId: Unique marker of region
        :type RegionId: int
        :param _Zones: List of all availability zones in the region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zones: list of ZoneInfo
        :param _Count: Number of clusters in the region
        :type Count: int
        :param _IsInternationalSite: 0 indicates the international site; 1 indicates not.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsInternationalSite: int
        :param _Bucket: Bucket
Note: This field may return null, indicating that no valid values can be obtained.
        :type Bucket: str
        """
        self._Name = None
        self._Desc = None
        self._RegionId = None
        self._Zones = None
        self._Count = None
        self._IsInternationalSite = None
        self._Bucket = None

    @property
    def Name(self):
        """Region name, such as ap-guangzhou
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        """Region description, such as Guangzhou
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def RegionId(self):
        """Unique marker of region
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Zones(self):
        """List of all availability zones in the region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ZoneInfo
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Count(self):
        """Number of clusters in the region
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def IsInternationalSite(self):
        """0 indicates the international site; 1 indicates not.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsInternationalSite

    @IsInternationalSite.setter
    def IsInternationalSite(self, IsInternationalSite):
        self._IsInternationalSite = IsInternationalSite

    @property
    def Bucket(self):
        """Bucket
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._RegionId = params.get("RegionId")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._Count = params.get("Count")
        self._IsInternationalSite = params.get("IsInternationalSite")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskRequest(AbstractModel):
    """ResizeDisk request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _Type: Role (MATER/CORE), MASTER corresponds to FE, CORE corresponds to BE.
        :type Type: str
        :param _DiskSize: Cloud disk size
        :type DiskSize: int
        """
        self._InstanceId = None
        self._Type = None
        self._DiskSize = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """Role (MATER/CORE), MASTER corresponds to FE, CORE corresponds to BE.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DiskSize(self):
        """Cloud disk size
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskResponse(AbstractModel):
    """ResizeDisk response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _FlowId: Process ID
        :type FlowId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._FlowId = None
        self._ErrorMsg = None
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
    def FlowId(self):
        """Process ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ResourceSpec(AbstractModel):
    """Resource specification description information

    """

    def __init__(self):
        r"""
        :param _Name: Specification name, such as SCH1
        :type Name: str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Mem: Memory size, in GB
        :type Mem: int
        :param _Type: Classification markers, STANDARD/BIGDATA/HIGHIO respectively represent standard type/big data type/high IO.
        :type Type: str
        :param _SystemDisk: System disk description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type SystemDisk: :class:`tencentcloud.cdwdoris.v20211228.models.DiskSpec`
        :param _DataDisk: Data disk description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataDisk: :class:`tencentcloud.cdwdoris.v20211228.models.DiskSpec`
        :param _MaxNodeSize: Limit of the maximum number of nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxNodeSize: int
        :param _Available: Whether it is available. False indicates sell-out.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Available: bool
        :param _ComputeSpecDesc: Specification description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComputeSpecDesc: str
        :param _InstanceQuota: CVM inventory
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceQuota: int
        """
        self._Name = None
        self._Cpu = None
        self._Mem = None
        self._Type = None
        self._SystemDisk = None
        self._DataDisk = None
        self._MaxNodeSize = None
        self._Available = None
        self._ComputeSpecDesc = None
        self._InstanceQuota = None

    @property
    def Name(self):
        """Specification name, such as SCH1
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Mem(self):
        """Memory size, in GB
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Type(self):
        """Classification markers, STANDARD/BIGDATA/HIGHIO respectively represent standard type/big data type/high IO.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SystemDisk(self):
        """System disk description information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DiskSpec`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisk(self):
        """Data disk description information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DiskSpec`
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def MaxNodeSize(self):
        """Limit of the maximum number of nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxNodeSize

    @MaxNodeSize.setter
    def MaxNodeSize(self, MaxNodeSize):
        self._MaxNodeSize = MaxNodeSize

    @property
    def Available(self):
        """Whether it is available. False indicates sell-out.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def ComputeSpecDesc(self):
        """Specification description information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ComputeSpecDesc

    @ComputeSpecDesc.setter
    def ComputeSpecDesc(self, ComputeSpecDesc):
        self._ComputeSpecDesc = ComputeSpecDesc

    @property
    def InstanceQuota(self):
        """CVM inventory
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InstanceQuota

    @InstanceQuota.setter
    def InstanceQuota(self, InstanceQuota):
        self._InstanceQuota = InstanceQuota


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Type = params.get("Type")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = DiskSpec()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisk") is not None:
            self._DataDisk = DiskSpec()
            self._DataDisk._deserialize(params.get("DataDisk"))
        self._MaxNodeSize = params.get("MaxNodeSize")
        self._Available = params.get("Available")
        self._ComputeSpecDesc = params.get("ComputeSpecDesc")
        self._InstanceQuota = params.get("InstanceQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterForConfigsRequest(AbstractModel):
    """RestartClusterForConfigs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID, such as cdwch-xxxx
        :type InstanceId: str
        :param _ConfigName: Configuration file's name
        :type ConfigName: str
        :param _OperationType: grace_restart is an elegant scrolling restart. If this parameter is not filled in, restart now by default.
        :type OperationType: str
        """
        self._InstanceId = None
        self._ConfigName = None
        self._OperationType = None

    @property
    def InstanceId(self):
        """Cluster ID, such as cdwch-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigName(self):
        """Configuration file's name
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def OperationType(self):
        """grace_restart is an elegant scrolling restart. If this parameter is not filled in, restart now by default.
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConfigName = params.get("ConfigName")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterForConfigsResponse(AbstractModel):
    """RestartClusterForConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process related information
        :type FlowId: int
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process related information
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class RestartClusterForNodeRequest(AbstractModel):
    """RestartClusterForNode request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID, such as cdwch-xxxx
        :type InstanceId: str
        :param _ConfigName: Configuration file's name
        :type ConfigName: str
        :param _BatchSize: Each batch of restarts
        :type BatchSize: int
        :param _NodeList: Restart node
        :type NodeList: list of str
        :param _RollingRestart: False means non-rolling restart, and true means rolling restart.
        :type RollingRestart: bool
        """
        self._InstanceId = None
        self._ConfigName = None
        self._BatchSize = None
        self._NodeList = None
        self._RollingRestart = None

    @property
    def InstanceId(self):
        """Cluster ID, such as cdwch-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigName(self):
        """Configuration file's name
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def BatchSize(self):
        """Each batch of restarts
        :rtype: int
        """
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def NodeList(self):
        """Restart node
        :rtype: list of str
        """
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def RollingRestart(self):
        """False means non-rolling restart, and true means rolling restart.
        :rtype: bool
        """
        return self._RollingRestart

    @RollingRestart.setter
    def RollingRestart(self, RollingRestart):
        self._RollingRestart = RollingRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConfigName = params.get("ConfigName")
        self._BatchSize = params.get("BatchSize")
        self._NodeList = params.get("NodeList")
        self._RollingRestart = params.get("RollingRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterForNodeResponse(AbstractModel):
    """RestartClusterForNode response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process related information
        :type FlowId: int
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process related information
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class RestoreStatus(AbstractModel):
    """Recover the task information

    """

    def __init__(self):
        r"""
        :param _JobId: Recover the task ID
        :type JobId: int
        :param _Label: Recover the task tag
        :type Label: str
        :param _Timestamp: Recover the task timestamp
        :type Timestamp: str
        :param _DbName: Recover the database where the task is located
        :type DbName: str
        :param _State: Recover the task status
        :type State: str
        :param _AllowLoad: Whether to allow import during recovery
        :type AllowLoad: bool
        :param _ReplicationNum: Number of replicas
        :type ReplicationNum: str
        :param _ReplicaAllocation: Number of replicas
        :type ReplicaAllocation: str
        :param _RestoreObjects: Recover object
        :type RestoreObjects: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _MetaPreparedTime: Metadata preparation time
        :type MetaPreparedTime: str
        :param _SnapshotFinishedTime: Snapshot end time
        :type SnapshotFinishedTime: str
        :param _DownloadFinishedTime: Download end time
        :type DownloadFinishedTime: str
        :param _FinishedTime: End time
        :type FinishedTime: str
        :param _UnfinishedTasks: Unfinished tasks
        :type UnfinishedTasks: str
        :param _Progress: Progress
        :type Progress: str
        :param _TaskErrMsg: Error message
        :type TaskErrMsg: str
        :param _Status: Status
        :type Status: str
        :param _Timeout: Operation timeout period
        :type Timeout: int
        :param _ReserveReplica: Whether to maintain the number of replicas in the source table
        :type ReserveReplica: bool
        :param _ReserveDynamicPartitionEnable: Whether to maintain dynamic partitions in the source table
        :type ReserveDynamicPartitionEnable: bool
        :param _BackupJobId: Backup instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupJobId: int
        :param _TaskId: ID of the snapshot corresponding to the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        """
        self._JobId = None
        self._Label = None
        self._Timestamp = None
        self._DbName = None
        self._State = None
        self._AllowLoad = None
        self._ReplicationNum = None
        self._ReplicaAllocation = None
        self._RestoreObjects = None
        self._CreateTime = None
        self._MetaPreparedTime = None
        self._SnapshotFinishedTime = None
        self._DownloadFinishedTime = None
        self._FinishedTime = None
        self._UnfinishedTasks = None
        self._Progress = None
        self._TaskErrMsg = None
        self._Status = None
        self._Timeout = None
        self._ReserveReplica = None
        self._ReserveDynamicPartitionEnable = None
        self._BackupJobId = None
        self._TaskId = None

    @property
    def JobId(self):
        """Recover the task ID
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Label(self):
        """Recover the task tag
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Timestamp(self):
        """Recover the task timestamp
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def DbName(self):
        """Recover the database where the task is located
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def State(self):
        """Recover the task status
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AllowLoad(self):
        """Whether to allow import during recovery
        :rtype: bool
        """
        return self._AllowLoad

    @AllowLoad.setter
    def AllowLoad(self, AllowLoad):
        self._AllowLoad = AllowLoad

    @property
    def ReplicationNum(self):
        """Number of replicas
        :rtype: str
        """
        return self._ReplicationNum

    @ReplicationNum.setter
    def ReplicationNum(self, ReplicationNum):
        self._ReplicationNum = ReplicationNum

    @property
    def ReplicaAllocation(self):
        """Number of replicas
        :rtype: str
        """
        return self._ReplicaAllocation

    @ReplicaAllocation.setter
    def ReplicaAllocation(self, ReplicaAllocation):
        self._ReplicaAllocation = ReplicaAllocation

    @property
    def RestoreObjects(self):
        """Recover object
        :rtype: str
        """
        return self._RestoreObjects

    @RestoreObjects.setter
    def RestoreObjects(self, RestoreObjects):
        self._RestoreObjects = RestoreObjects

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MetaPreparedTime(self):
        """Metadata preparation time
        :rtype: str
        """
        return self._MetaPreparedTime

    @MetaPreparedTime.setter
    def MetaPreparedTime(self, MetaPreparedTime):
        self._MetaPreparedTime = MetaPreparedTime

    @property
    def SnapshotFinishedTime(self):
        """Snapshot end time
        :rtype: str
        """
        return self._SnapshotFinishedTime

    @SnapshotFinishedTime.setter
    def SnapshotFinishedTime(self, SnapshotFinishedTime):
        self._SnapshotFinishedTime = SnapshotFinishedTime

    @property
    def DownloadFinishedTime(self):
        """Download end time
        :rtype: str
        """
        return self._DownloadFinishedTime

    @DownloadFinishedTime.setter
    def DownloadFinishedTime(self, DownloadFinishedTime):
        self._DownloadFinishedTime = DownloadFinishedTime

    @property
    def FinishedTime(self):
        """End time
        :rtype: str
        """
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def UnfinishedTasks(self):
        """Unfinished tasks
        :rtype: str
        """
        return self._UnfinishedTasks

    @UnfinishedTasks.setter
    def UnfinishedTasks(self, UnfinishedTasks):
        self._UnfinishedTasks = UnfinishedTasks

    @property
    def Progress(self):
        """Progress
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskErrMsg(self):
        """Error message
        :rtype: str
        """
        return self._TaskErrMsg

    @TaskErrMsg.setter
    def TaskErrMsg(self, TaskErrMsg):
        self._TaskErrMsg = TaskErrMsg

    @property
    def Status(self):
        """Status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Timeout(self):
        """Operation timeout period
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def ReserveReplica(self):
        """Whether to maintain the number of replicas in the source table
        :rtype: bool
        """
        return self._ReserveReplica

    @ReserveReplica.setter
    def ReserveReplica(self, ReserveReplica):
        self._ReserveReplica = ReserveReplica

    @property
    def ReserveDynamicPartitionEnable(self):
        """Whether to maintain dynamic partitions in the source table
        :rtype: bool
        """
        return self._ReserveDynamicPartitionEnable

    @ReserveDynamicPartitionEnable.setter
    def ReserveDynamicPartitionEnable(self, ReserveDynamicPartitionEnable):
        self._ReserveDynamicPartitionEnable = ReserveDynamicPartitionEnable

    @property
    def BackupJobId(self):
        """Backup instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupJobId

    @BackupJobId.setter
    def BackupJobId(self, BackupJobId):
        self._BackupJobId = BackupJobId

    @property
    def TaskId(self):
        """ID of the snapshot corresponding to the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Label = params.get("Label")
        self._Timestamp = params.get("Timestamp")
        self._DbName = params.get("DbName")
        self._State = params.get("State")
        self._AllowLoad = params.get("AllowLoad")
        self._ReplicationNum = params.get("ReplicationNum")
        self._ReplicaAllocation = params.get("ReplicaAllocation")
        self._RestoreObjects = params.get("RestoreObjects")
        self._CreateTime = params.get("CreateTime")
        self._MetaPreparedTime = params.get("MetaPreparedTime")
        self._SnapshotFinishedTime = params.get("SnapshotFinishedTime")
        self._DownloadFinishedTime = params.get("DownloadFinishedTime")
        self._FinishedTime = params.get("FinishedTime")
        self._UnfinishedTasks = params.get("UnfinishedTasks")
        self._Progress = params.get("Progress")
        self._TaskErrMsg = params.get("TaskErrMsg")
        self._Status = params.get("Status")
        self._Timeout = params.get("Timeout")
        self._ReserveReplica = params.get("ReserveReplica")
        self._ReserveDynamicPartitionEnable = params.get("ReserveDynamicPartitionEnable")
        self._BackupJobId = params.get("BackupJobId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rows(AbstractModel):
    """Multiple rows of data

    """

    def __init__(self):
        r"""
        :param _DataRow: A row of data
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataRow: list of str
        """
        self._DataRow = None

    @property
    def DataRow(self):
        """A row of data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DataRow

    @DataRow.setter
    def DataRow(self, DataRow):
        self._DataRow = DataRow


    def _deserialize(self, params):
        self._DataRow = params.get("DataRow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _Type: Role (MATER/CORE), MASTER corresponds to FE, CORE corresponds to BE.
        :type Type: str
        :param _NodeCount: Number of nodes
        :type NodeCount: int
        :param _HaType: Cluster high availability type after scaled out: 0 indicates non-high availability, 1 indicates read high availability, and 2 indicates read-write high availability.
        :type HaType: int
        """
        self._InstanceId = None
        self._Type = None
        self._NodeCount = None
        self._HaType = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """Role (MATER/CORE), MASTER corresponds to FE, CORE corresponds to BE.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NodeCount(self):
        """Number of nodes
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def HaType(self):
        """Cluster high availability type after scaled out: 0 indicates non-high availability, 1 indicates read high availability, and 2 indicates read-write high availability.
        :rtype: int
        """
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._NodeCount = params.get("NodeCount")
        self._HaType = params.get("HaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID
        :type FlowId: str
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ScaleUpInstanceRequest(AbstractModel):
    """ScaleUpInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _SpecName: Node specifications
        :type SpecName: str
        :param _Type: Role (MATER/CORE). MASTER corresponds to FE, and CORE corresponds to BE.
        :type Type: str
        """
        self._InstanceId = None
        self._SpecName = None
        self._Type = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpecName(self):
        """Node specifications
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Type(self):
        """Role (MATER/CORE). MASTER corresponds to FE, and CORE corresponds to BE.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpecName = params.get("SpecName")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpInstanceResponse(AbstractModel):
    """ScaleUpInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID
        :type FlowId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
    def ErrorMsg(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class SearchTags(AbstractModel):
    """The searched marker list on the list page

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        :param _AllValue: 1 means only the tag key is entered without a value, and 0 means both the key and the value are entered.
        :type AllValue: int
        """
        self._TagKey = None
        self._TagValue = None
        self._AllValue = None

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

    @property
    def AllValue(self):
        """1 means only the tag key is entered without a value, and 0 means both the key and the value are entered.
        :rtype: int
        """
        return self._AllValue

    @AllValue.setter
    def AllValue(self, AllValue):
        self._AllValue = AllValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._AllValue = params.get("AllValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowQueryRecord(AbstractModel):
    """Slow log records

    """

    def __init__(self):
        r"""
        :param _OsUser: User query 
        :type OsUser: str
        :param _InitialQueryId: ID query
        :type InitialQueryId: str
        :param _Sql: SQL statement
        :type Sql: str
        :param _QueryStartTime: Start time
        :type QueryStartTime: str
        :param _DurationMs: Execution duration
        :type DurationMs: int
        :param _ReadRows: The number of read rows
        :type ReadRows: int
        :param _ResultRows: Total number of read bytes
        :type ResultRows: int
        :param _ResultBytes: Result bytes
        :type ResultBytes: int
        :param _MemoryUsage: Memory
        :type MemoryUsage: int
        :param _InitialAddress: Initial query IP
        :type InitialAddress: str
        :param _DbName: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _IsQuery: Whether it is a query. 0 indicates no, and 1 indicates query statement.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsQuery: int
        :param _ResultBytesMB: MB format of ResultBytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultBytesMB: float
        :param _MemoryUsageMB: MemoryUsage, in MB
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemoryUsageMB: float
        :param _DurationSec: DurationMs, in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type DurationSec: float
        """
        self._OsUser = None
        self._InitialQueryId = None
        self._Sql = None
        self._QueryStartTime = None
        self._DurationMs = None
        self._ReadRows = None
        self._ResultRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._InitialAddress = None
        self._DbName = None
        self._IsQuery = None
        self._ResultBytesMB = None
        self._MemoryUsageMB = None
        self._DurationSec = None

    @property
    def OsUser(self):
        """User query 
        :rtype: str
        """
        return self._OsUser

    @OsUser.setter
    def OsUser(self, OsUser):
        self._OsUser = OsUser

    @property
    def InitialQueryId(self):
        """ID query
        :rtype: str
        """
        return self._InitialQueryId

    @InitialQueryId.setter
    def InitialQueryId(self, InitialQueryId):
        self._InitialQueryId = InitialQueryId

    @property
    def Sql(self):
        """SQL statement
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def QueryStartTime(self):
        """Start time
        :rtype: str
        """
        return self._QueryStartTime

    @QueryStartTime.setter
    def QueryStartTime(self, QueryStartTime):
        self._QueryStartTime = QueryStartTime

    @property
    def DurationMs(self):
        """Execution duration
        :rtype: int
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def ReadRows(self):
        """The number of read rows
        :rtype: int
        """
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultRows(self):
        """Total number of read bytes
        :rtype: int
        """
        return self._ResultRows

    @ResultRows.setter
    def ResultRows(self, ResultRows):
        self._ResultRows = ResultRows

    @property
    def ResultBytes(self):
        """Result bytes
        :rtype: int
        """
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        """Memory
        :rtype: int
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def InitialAddress(self):
        """Initial query IP
        :rtype: str
        """
        return self._InitialAddress

    @InitialAddress.setter
    def InitialAddress(self, InitialAddress):
        self._InitialAddress = InitialAddress

    @property
    def DbName(self):
        """Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def IsQuery(self):
        """Whether it is a query. 0 indicates no, and 1 indicates query statement.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def ResultBytesMB(self):
        """MB format of ResultBytes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._ResultBytesMB

    @ResultBytesMB.setter
    def ResultBytesMB(self, ResultBytesMB):
        self._ResultBytesMB = ResultBytesMB

    @property
    def MemoryUsageMB(self):
        """MemoryUsage, in MB
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._MemoryUsageMB

    @MemoryUsageMB.setter
    def MemoryUsageMB(self, MemoryUsageMB):
        self._MemoryUsageMB = MemoryUsageMB

    @property
    def DurationSec(self):
        """DurationMs, in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._DurationSec

    @DurationSec.setter
    def DurationSec(self, DurationSec):
        self._DurationSec = DurationSec


    def _deserialize(self, params):
        self._OsUser = params.get("OsUser")
        self._InitialQueryId = params.get("InitialQueryId")
        self._Sql = params.get("Sql")
        self._QueryStartTime = params.get("QueryStartTime")
        self._DurationMs = params.get("DurationMs")
        self._ReadRows = params.get("ReadRows")
        self._ResultRows = params.get("ResultRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._InitialAddress = params.get("InitialAddress")
        self._DbName = params.get("DbName")
        self._IsQuery = params.get("IsQuery")
        self._ResultBytesMB = params.get("ResultBytesMB")
        self._MemoryUsageMB = params.get("MemoryUsageMB")
        self._DurationSec = params.get("DurationSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePermissions(AbstractModel):
    """Table-level permissions

    """

    def __init__(self):
        r"""
        :param _TableName: Full name of the table
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _Permissions: Table permission
Note: This field may return null, indicating that no valid values can be obtained.
        :type Permissions: list of str
        """
        self._TableName = None
        self._Permissions = None

    @property
    def TableName(self):
        """Full name of the table
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Permissions(self):
        """Table permission
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._Permissions = params.get("Permissions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablesDDL(AbstractModel):
    """DDL information of the table

    """

    def __init__(self):
        r"""
        :param _TableName: Table name

Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _DDLInfo: DDL statement for creating a table

Note: This field may return null, indicating that no valid values can be obtained.
        :type DDLInfo: str
        """
        self._TableName = None
        self._DDLInfo = None

    @property
    def TableName(self):
        """Table name

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def DDLInfo(self):
        """DDL statement for creating a table

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DDLInfo

    @DDLInfo.setter
    def DDLInfo(self, DDLInfo):
        self._DDLInfo = DDLInfo


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._DDLInfo = params.get("DDLInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag description

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
        


class UpdateCoolDownRequest(AbstractModel):
    """UpdateCoolDown request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _Enable: Whether to enable. 0: disable; 1: enable.
        :type Enable: int
        :param _Bucket: Address of the COS bucket where the user stores layered hot and cold data
        :type Bucket: str
        """
        self._InstanceId = None
        self._Enable = None
        self._Bucket = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Enable(self):
        """Whether to enable. 0: disable; 1: enable.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Bucket(self):
        """Address of the COS bucket where the user stores layered hot and cold data
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Enable = params.get("Enable")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCoolDownResponse(AbstractModel):
    """UpdateCoolDown response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Error message

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class UpdateDatabaseRequest(AbstractModel):
    """UpdateDatabase request structure.

    """

    def __init__(self):
        r"""
        :param _DbName: The database name to be modified
        :type DbName: str
        :param _Operation: Modify the operation type, such as SET_QUOTA, RENAME, SET_REPLICA_QUOTA, and SET_PROPERTIES. Modify the operation type, such as SET_QUOTA, RENAME, SET_REPLICA_QUOTA, and SET_PROPERTIES.
        :type Operation: str
        :param _InstanceId: InstanceId
        :type InstanceId: str
        :param _Quota: Quota value, which is used to set the quota of data volume or replicas.
        :type Quota: str
        :param _NewDbName: New database name, used for renaming operation.
        :type NewDbName: str
        :param _Properties: Attribute key-value pair to be set
        :type Properties: list of PropertiesMap
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _CatalogName: The name of the catalog, if left unspecified, defaults to "internal".
        :type CatalogName: str
        """
        self._DbName = None
        self._Operation = None
        self._InstanceId = None
        self._Quota = None
        self._NewDbName = None
        self._Properties = None
        self._UserName = None
        self._PassWord = None
        self._CatalogName = None

    @property
    def DbName(self):
        """The database name to be modified
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Operation(self):
        """Modify the operation type, such as SET_QUOTA, RENAME, SET_REPLICA_QUOTA, and SET_PROPERTIES. Modify the operation type, such as SET_QUOTA, RENAME, SET_REPLICA_QUOTA, and SET_PROPERTIES.
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InstanceId(self):
        """InstanceId
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Quota(self):
        """Quota value, which is used to set the quota of data volume or replicas.
        :rtype: str
        """
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota

    @property
    def NewDbName(self):
        """New database name, used for renaming operation.
        :rtype: str
        """
        return self._NewDbName

    @NewDbName.setter
    def NewDbName(self, NewDbName):
        self._NewDbName = NewDbName

    @property
    def Properties(self):
        """Attribute key-value pair to be set
        :rtype: list of PropertiesMap
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def CatalogName(self):
        """The name of the catalog, if left unspecified, defaults to "internal".
        :rtype: str
        """
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._Operation = params.get("Operation")
        self._InstanceId = params.get("InstanceId")
        self._Quota = params.get("Quota")
        self._NewDbName = params.get("NewDbName")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = PropertiesMap()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._CatalogName = params.get("CatalogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDatabaseResponse(AbstractModel):
    """UpdateDatabase response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Whether the operation is successful
        :type Success: bool
        :param _Message: Message description of the operation result
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._Message = None
        self._RequestId = None

    @property
    def Success(self):
        """Whether the operation is successful
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def Message(self):
        """Message description of the operation result
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Success = params.get("Success")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class UpdateTableSchemaRequest(AbstractModel):
    """UpdateTableSchema request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Resource ID, which is the TCHouse-D resource ID used for table creation.
        :type InstanceId: str
        :param _DbName: Database name
        :type DbName: str
        :param _TableName: Table name
        :type TableName: str
        :param _Columns: Column
        :type Columns: list of Column
        :param _Distribution: Bucket information
        :type Distribution: :class:`tencentcloud.cdwdoris.v20211228.models.Distribution`
        :param _UserName: Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type UserName: str
        :param _PassWord: Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :type PassWord: str
        :param _IndexInfos: Index information. The inverted index and N-Gram index can be configured through this parameter. The Prefix index is related to the sort key and key column, and do not require additional configuration. Configure bloom_filter_columns in the table attribute when BloomFilter index is required.
        :type IndexInfos: list of IndexInfo
        :param _TableComment: Table description
        :type TableComment: str
        :param _Properties: Table attribute
        :type Properties: list of Property
        """
        self._InstanceId = None
        self._DbName = None
        self._TableName = None
        self._Columns = None
        self._Distribution = None
        self._UserName = None
        self._PassWord = None
        self._IndexInfos = None
        self._TableComment = None
        self._Properties = None

    @property
    def InstanceId(self):
        """Resource ID, which is the TCHouse-D resource ID used for table creation.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """Database name
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableName(self):
        """Table name
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Columns(self):
        """Column
        :rtype: list of Column
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Distribution(self):
        """Bucket information
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.Distribution`
        """
        return self._Distribution

    @Distribution.setter
    def Distribution(self, Distribution):
        self._Distribution = Distribution

    @property
    def UserName(self):
        """Use the user who has corresponding permissions for operations. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password corresponding to the user. If the TCHouse-D cluster uses a kernel account registered by a CAM user, you do not need to fill it in.
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def IndexInfos(self):
        """Index information. The inverted index and N-Gram index can be configured through this parameter. The Prefix index is related to the sort key and key column, and do not require additional configuration. Configure bloom_filter_columns in the table attribute when BloomFilter index is required.
        :rtype: list of IndexInfo
        """
        return self._IndexInfos

    @IndexInfos.setter
    def IndexInfos(self, IndexInfos):
        self._IndexInfos = IndexInfos

    @property
    def TableComment(self):
        """Table description
        :rtype: str
        """
        return self._TableComment

    @TableComment.setter
    def TableComment(self, TableComment):
        self._TableComment = TableComment

    @property
    def Properties(self):
        """Table attribute
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._TableName = params.get("TableName")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Distribution") is not None:
            self._Distribution = Distribution()
            self._Distribution._deserialize(params.get("Distribution"))
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        if params.get("IndexInfos") is not None:
            self._IndexInfos = []
            for item in params.get("IndexInfos"):
                obj = IndexInfo()
                obj._deserialize(item)
                self._IndexInfos.append(obj)
        self._TableComment = params.get("TableComment")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTableSchemaResponse(AbstractModel):
    """UpdateTableSchema response structure.

    """

    def __init__(self):
        r"""
        :param _Message: Error message
        :type Message: str
        :param _Success: Is it successful
        :type Success: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Message = None
        self._Success = None
        self._RequestId = None

    @property
    def Message(self):
        """Error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Success(self):
        """Is it successful
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

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
        self._Message = params.get("Message")
        self._Success = params.get("Success")
        self._RequestId = params.get("RequestId")


class UpdateUserPrivileges(AbstractModel):
    """Update user permission structure

    """

    def __init__(self):
        r"""
        :param _IsSetGlobalCatalog: Whether to set catalog permission
        :type IsSetGlobalCatalog: bool
        """
        self._IsSetGlobalCatalog = None

    @property
    def IsSetGlobalCatalog(self):
        """Whether to set catalog permission
        :rtype: bool
        """
        return self._IsSetGlobalCatalog

    @IsSetGlobalCatalog.setter
    def IsSetGlobalCatalog(self, IsSetGlobalCatalog):
        self._IsSetGlobalCatalog = IsSetGlobalCatalog


    def _deserialize(self, params):
        self._IsSetGlobalCatalog = params.get("IsSetGlobalCatalog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """Add or modify the user

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID.
        :type InstanceId: str
        :param _UserName: Username
        :type UserName: str
        :param _PassWord: Password
        :type PassWord: str
        :param _WhiteHost: The IP address of the user link
        :type WhiteHost: str
        :param _OldWhiteHost: IP address of the user link before modification
        :type OldWhiteHost: str
        :param _Describe: Description
        :type Describe: str
        :param _OldPwd: Original password
        :type OldPwd: str
        :param _CamUin: UIN of the bound sub-user
        :type CamUin: str
        :param _CamRangerGroupIds: Ranger group id list
        :type CamRangerGroupIds: list of int
        """
        self._InstanceId = None
        self._UserName = None
        self._PassWord = None
        self._WhiteHost = None
        self._OldWhiteHost = None
        self._Describe = None
        self._OldPwd = None
        self._CamUin = None
        self._CamRangerGroupIds = None

    @property
    def InstanceId(self):
        """Cluster instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def PassWord(self):
        """Password
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def WhiteHost(self):
        """The IP address of the user link
        :rtype: str
        """
        return self._WhiteHost

    @WhiteHost.setter
    def WhiteHost(self, WhiteHost):
        self._WhiteHost = WhiteHost

    @property
    def OldWhiteHost(self):
        """IP address of the user link before modification
        :rtype: str
        """
        return self._OldWhiteHost

    @OldWhiteHost.setter
    def OldWhiteHost(self, OldWhiteHost):
        self._OldWhiteHost = OldWhiteHost

    @property
    def Describe(self):
        """Description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def OldPwd(self):
        """Original password
        :rtype: str
        """
        return self._OldPwd

    @OldPwd.setter
    def OldPwd(self, OldPwd):
        self._OldPwd = OldPwd

    @property
    def CamUin(self):
        """UIN of the bound sub-user
        :rtype: str
        """
        return self._CamUin

    @CamUin.setter
    def CamUin(self, CamUin):
        self._CamUin = CamUin

    @property
    def CamRangerGroupIds(self):
        """Ranger group id list
        :rtype: list of int
        """
        return self._CamRangerGroupIds

    @CamRangerGroupIds.setter
    def CamRangerGroupIds(self, CamRangerGroupIds):
        self._CamRangerGroupIds = CamRangerGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        self._WhiteHost = params.get("WhiteHost")
        self._OldWhiteHost = params.get("OldWhiteHost")
        self._Describe = params.get("Describe")
        self._OldPwd = params.get("OldPwd")
        self._CamUin = params.get("CamUin")
        self._CamRangerGroupIds = params.get("CamRangerGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserWorkloadGroup(AbstractModel):
    """Resource group information bound to the user

    """

    def __init__(self):
        r"""
        :param _UserName: test
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _WorkloadGroupName: normal
Note: This field may return null, indicating that no valid values can be obtained.
        :type WorkloadGroupName: str
        """
        self._UserName = None
        self._WorkloadGroupName = None

    @property
    def UserName(self):
        """test
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def WorkloadGroupName(self):
        """normal
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WorkloadGroupName

    @WorkloadGroupName.setter
    def WorkloadGroupName(self, WorkloadGroupName):
        self._WorkloadGroupName = WorkloadGroupName


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._WorkloadGroupName = params.get("WorkloadGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadGroupConfig(AbstractModel):
    """Resource group configuration

    """

    def __init__(self):
        r"""
        :param _WorkloadGroupName: Resource group name
Note: This field may return null, indicating that no valid values can be obtained.
        :type WorkloadGroupName: str
        :param _CpuShare: CPU weight
Note: This field may return null, indicating that no valid values can be obtained.
        :type CpuShare: int
        :param _MemoryLimit: Memory limit. The sum of memory limit values of all resource groups should be less than or equal to 100.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemoryLimit: int
        :param _EnableMemoryOverCommit: Whether to allow over-allocation
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableMemoryOverCommit: bool
        :param _CpuHardLimit: CPU hard limit
Note: This field may return null, indicating that no valid values can be obtained.
        :type CpuHardLimit: str
        """
        self._WorkloadGroupName = None
        self._CpuShare = None
        self._MemoryLimit = None
        self._EnableMemoryOverCommit = None
        self._CpuHardLimit = None

    @property
    def WorkloadGroupName(self):
        """Resource group name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WorkloadGroupName

    @WorkloadGroupName.setter
    def WorkloadGroupName(self, WorkloadGroupName):
        self._WorkloadGroupName = WorkloadGroupName

    @property
    def CpuShare(self):
        """CPU weight
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CpuShare

    @CpuShare.setter
    def CpuShare(self, CpuShare):
        self._CpuShare = CpuShare

    @property
    def MemoryLimit(self):
        """Memory limit. The sum of memory limit values of all resource groups should be less than or equal to 100.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def EnableMemoryOverCommit(self):
        """Whether to allow over-allocation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableMemoryOverCommit

    @EnableMemoryOverCommit.setter
    def EnableMemoryOverCommit(self, EnableMemoryOverCommit):
        self._EnableMemoryOverCommit = EnableMemoryOverCommit

    @property
    def CpuHardLimit(self):
        """CPU hard limit
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CpuHardLimit

    @CpuHardLimit.setter
    def CpuHardLimit(self, CpuHardLimit):
        self._CpuHardLimit = CpuHardLimit


    def _deserialize(self, params):
        self._WorkloadGroupName = params.get("WorkloadGroupName")
        self._CpuShare = params.get("CpuShare")
        self._MemoryLimit = params.get("MemoryLimit")
        self._EnableMemoryOverCommit = params.get("EnableMemoryOverCommit")
        self._CpuHardLimit = params.get("CpuHardLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """Availability zone description

    """

    def __init__(self):
        r"""
        :param _Name: Availability zone name, such as ap-guangzhou-1
        :type Name: str
        :param _Desc: Availability zone description, such as Guangzhou region 1
        :type Desc: str
        :param _ZoneId: Unique tag of the availability zone
        :type ZoneId: int
        :param _Encrypt: Encryptid
Note: This field may return null, indicating that no valid values can be obtained.
        :type Encrypt: int
        """
        self._Name = None
        self._Desc = None
        self._ZoneId = None
        self._Encrypt = None

    @property
    def Name(self):
        """Availability zone name, such as ap-guangzhou-1
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        """Availability zone description, such as Guangzhou region 1
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ZoneId(self):
        """Unique tag of the availability zone
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Encrypt(self):
        """Encryptid
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._ZoneId = params.get("ZoneId")
        self._Encrypt = params.get("Encrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        