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


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConsistencyParams(AbstractModel):
    """Sampling parameter for spot check

    """

    def __init__(self):
        """
        :param SelectRowsPerTable: Data content check parameter, which refers to the proportion of the rows selected for data comparison in all the rows of the table. Value: an integer between 1 and 100.
        :type SelectRowsPerTable: int
        :param TablesSelectAll: Data content check parameter, which refers to the proportion of the tables selected for data detection in all the tables. Value: an integer between 1 and 100.
        :type TablesSelectAll: int
        :param TablesSelectCount: Data quantity check parameter, which checks whether the numbers of rows are identical. It refers to the proportion of the tables selected for quantity check in all the tables. Value: an integer between 1 and 100.
        :type TablesSelectCount: int
        """
        self.SelectRowsPerTable = None
        self.TablesSelectAll = None
        self.TablesSelectCount = None


    def _deserialize(self, params):
        self.SelectRowsPerTable = params.get("SelectRowsPerTable")
        self.TablesSelectAll = params.get("TablesSelectAll")
        self.TablesSelectCount = params.get("TablesSelectCount")


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMigrateJobRequest(AbstractModel):
    """CreateMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobName: Data migration task name
        :type JobName: str
        :param MigrateOption: Migration task configuration options
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcDatabaseType: Source instance database type, which currently supports MySQL, Redis, MongoDB, PostgreSQL, MariaDB, and Percona. For more information on the supported types in a specific region, see the migration task creation page in the console.
        :type SrcDatabaseType: str
        :param SrcAccessType: Source instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance), ccn (CCN instance)
        :type SrcAccessType: str
        :param SrcInfo: Source instance information, which is correlated with the migration task type
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: Target instance access type, which currently supports MySQL, Redis, MongoDB, PostgreSQL, MariaDB, and Percona. For more information on the supported types in a specific region, see the migration task creation page in the console.
        :type DstDatabaseType: str
        :param DstAccessType: Target instance access type, which currently only supports cdb (TencentDB instance)
        :type DstAccessType: str
        :param DstInfo: Destination instance information
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: Information of the source table to be migrated, which is described in JSON string format. It is required if MigrateOption.MigrateObject is 2 (migrating the specified table).
For databases with a database-table structure:
[{Database:db1,Table:[table1,table2]},{Database:db2}]
For databases with a database-schema-table structure:
[{Database:db1,Schema:s1
Table:[table1,table2]},{Database:db1,Schema:s2
Table:[table1,table2]},{Database:db2,Schema:s1
Table:[table1,table2]},{Database:db3},{Database:db4
Schema:s1}]
        :type DatabaseInfo: str
        """
        self.JobName = None
        self.MigrateOption = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class CreateMigrateJobResponse(AbstractModel):
    """CreateMigrateJob response structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID
        :type JobId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateSyncCheckJobRequest(AbstractModel):
    """CreateSyncCheckJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Disaster recovery sync task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CreateSyncCheckJobResponse(AbstractModel):
    """CreateSyncCheckJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSyncJobRequest(AbstractModel):
    """CreateSyncJob request structure.

    """

    def __init__(self):
        """
        :param JobName: Disaster recovery sync task name
        :type JobName: str
        :param SyncOption: Configuration options of a disaster recovery sync task
        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`
        :param SrcDatabaseType: Source instance database type, which currently only supports mysql
        :type SrcDatabaseType: str
        :param SrcAccessType: Source instance access type, which currently only supports cdb (TencentDB instances)
        :type SrcAccessType: str
        :param SrcInfo: Source instance information
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DstDatabaseType: Target instance access type, which currently only supports mysql
        :type DstDatabaseType: str
        :param DstAccessType: Target instance access type, which currently only supports cdb (TencentDB instances)
        :type DstAccessType: str
        :param DstInfo: Target instance information
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DatabaseInfo: Information of the source table to be synced, which is described in JSON string format.
For databases with a database-table structure:
[{Database:db1,Table:[table1,table2]},{Database:db2}]
        :type DatabaseInfo: str
        """
        self.JobName = None
        self.SyncOption = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        if params.get("SyncOption") is not None:
            self.SyncOption = SyncOption()
            self.SyncOption._deserialize(params.get("SyncOption"))
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SyncInstanceInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class CreateSyncJobResponse(AbstractModel):
    """CreateSyncJob response structure.

    """

    def __init__(self):
        """
        :param JobId: Disaster recovery sync task ID
        :type JobId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class DeleteMigrateJobRequest(AbstractModel):
    """DeleteMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DeleteMigrateJobResponse(AbstractModel):
    """DeleteMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSyncJobRequest(AbstractModel):
    """DeleteSyncJob request structure.

    """

    def __init__(self):
        """
        :param JobId: ID of the disaster recovery sync task to be deleted
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DeleteSyncJobResponse(AbstractModel):
    """DeleteSyncJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeMigrateCheckJobRequest(AbstractModel):
    """DescribeMigrateCheckJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeMigrateCheckJobResponse(AbstractModel):
    """DescribeMigrateCheckJob response structure.

    """

    def __init__(self):
        """
        :param Status: Check task status: unavailable, starting, running, finished
        :type Status: str
        :param ErrorCode: Task error code
        :type ErrorCode: int
        :param ErrorMessage: Task error message
        :type ErrorMessage: str
        :param Progress: Check task progress. For example, "30" means 30% completed
        :type Progress: str
        :param CheckFlag: Whether the check succeeds. 0: no; 1: yes; 3: not checked
        :type CheckFlag: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.ErrorCode = None
        self.ErrorMessage = None
        self.Progress = None
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        self.Progress = params.get("Progress")
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class DescribeMigrateJobsRequest(AbstractModel):
    """DescribeMigrateJobs request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID
        :type JobId: str
        :param JobName: Data migration task name
        :type JobName: str
        :param Order: Sort by field. Value range: JobId, Status, JobName, MigrateType, RunMode, CreateTime
        :type Order: str
        :param OrderSeq: Sorting order. Value range: ASC (ascending), DESC (descending)
        :type OrderSeq: str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Number of the returned instances. Value range: [1, 100]. Default value: 20
        :type Limit: int
        """
        self.JobId = None
        self.JobName = None
        self.Order = None
        self.OrderSeq = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Order = params.get("Order")
        self.OrderSeq = params.get("OrderSeq")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMigrateJobsResponse(AbstractModel):
    """DescribeMigrateJobs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of tasks
        :type TotalCount: int
        :param JobList: Array of task details
        :type JobList: list of MigrateJobInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = MigrateJobInfo()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSyncCheckJobRequest(AbstractModel):
    """DescribeSyncCheckJob request structure.

    """

    def __init__(self):
        """
        :param JobId: ID of the disaster recovery sync task to be queried
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeSyncCheckJobResponse(AbstractModel):
    """DescribeSyncCheckJob response structure.

    """

    def __init__(self):
        """
        :param Status: Task check status: starting, running, finished
        :type Status: str
        :param ErrorCode: Code of the task check result
        :type ErrorCode: int
        :param ErrorMessage: Prompt message
        :type ErrorMessage: str
        :param StepInfo: Description of a task execution step
        :type StepInfo: list of SyncCheckStepInfo
        :param CheckFlag: Check flag. 0: checking; 1: successfully checked
        :type CheckFlag: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.ErrorCode = None
        self.ErrorMessage = None
        self.StepInfo = None
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = SyncCheckStepInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class DescribeSyncJobsRequest(AbstractModel):
    """DescribeSyncJobs request structure.

    """

    def __init__(self):
        """
        :param JobId: Disaster recovery sync task ID
        :type JobId: str
        :param JobName: Disaster recovery sync task name
        :type JobName: str
        :param Order: Sort by field. Value range: JobId, Status, JobName, CreateTime
        :type Order: str
        :param OrderSeq: Sorting order. Value range: ASC (ascending), DESC (descending)
        :type OrderSeq: str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Number of the returned instances. Value range: [1, 100]. Default value: 20
        :type Limit: int
        """
        self.JobId = None
        self.JobName = None
        self.Order = None
        self.OrderSeq = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Order = params.get("Order")
        self.OrderSeq = params.get("OrderSeq")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSyncJobsResponse(AbstractModel):
    """DescribeSyncJobs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of tasks
        :type TotalCount: int
        :param JobList: Array of task details
        :type JobList: list of SyncJobInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = SyncJobInfo()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """Target instance information, which is correlated with the migration task type

    """

    def __init__(self):
        """
        :param InstanceId: Target instance ID, such as cdb-jd92ijd8
        :type InstanceId: str
        :param Region: Target instance region, such as ap-guangzhou
        :type Region: str
        :param Ip: Target instance VIP, which has been disused and does not need to be entered
        :type Ip: str
        :param Port: Target instance Vport, which has been disused and does not need to be entered
        :type Port: int
        :param ReadOnly: Only valid for MySQL currently. For instance-level migration, the value range is: 1 (read-only), 0 (read/write)
        :type ReadOnly: int
        """
        self.InstanceId = None
        self.Region = None
        self.Ip = None
        self.Port = None
        self.ReadOnly = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.ReadOnly = params.get("ReadOnly")


class MigrateDetailInfo(AbstractModel):
    """Describes the specific migration process

    """

    def __init__(self):
        """
        :param StepAll: Total number of steps
        :type StepAll: int
        :param StepNow: Current step
        :type StepNow: int
        :param Progress: Overall progress, such as:
        :type Progress: str
        :param CurrentStepProgress: Progress of the current step, such as:
        :type CurrentStepProgress: str
        :param MasterSlaveDistance: Master/slave lag in MB, which is valid during incremental sync and currently supported by TencentDB for Redis and MySQL
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: Master/slave lag in seconds, which is valid during incremental sync and currently supported by TencentDB for MySQL
        :type SecondsBehindMaster: int
        :param StepInfo: Step information
        :type StepInfo: list of MigrateStepDetailInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.CurrentStepProgress = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        self.CurrentStepProgress = params.get("CurrentStepProgress")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = MigrateStepDetailInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)


class MigrateJobInfo(AbstractModel):
    """Migration task details

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID
        :type JobId: str
        :param JobName: Data migration task name
        :type JobName: str
        :param MigrateOption: Migration task configuration options
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcDatabaseType: Source instance database type: MySQL, Redis, MongoDB, PostgreSQL, MariaDB, Percona
        :type SrcDatabaseType: str
        :param SrcAccessType: Source instance access type. Value range: extranet (public network), cvm (CVM-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance), ccn (CCN instances)
        :type SrcAccessType: str
        :param SrcInfo: Source instance information, which is correlated with the migration task type
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: Target instance access type: MySQL, Redis, MongoDB, PostgreSQL, MariaDB, Percona
        :type DstDatabaseType: str
        :param DstAccessType: Target instance access type, which currently only supports cdb (TencentDB instance)
        :type DstAccessType: str
        :param DstInfo: Target instance information
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: Information of the source table to be migrated. If the entire instance is to be migrated, this field should be []
        :type DatabaseInfo: str
        :param CreateTime: Task creation/submission time
        :type CreateTime: str
        :param StartTime: Task start time
        :type StartTime: str
        :param EndTime: Task end time
        :type EndTime: str
        :param Status: Task status. Value range: 1 (Creating), 3 (Checking), 4 (CheckPass), 5 (CheckNotPass), 7 (Running), 8 (ReadyComplete), 9 (Success), 10 (Failed), 11 (Stopping), 12 (Completing)
        :type Status: int
        :param Detail: Task details
        :type Detail: :class:`tencentcloud.dts.v20180330.models.MigrateDetailInfo`
        """
        self.JobId = None
        self.JobName = None
        self.MigrateOption = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Detail = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        if params.get("Detail") is not None:
            self.Detail = MigrateDetailInfo()
            self.Detail._deserialize(params.get("Detail"))


class MigrateOption(AbstractModel):
    """Migration task configuration options

    """

    def __init__(self):
        """
        :param RunMode: Task operation mode. Value range: 1 (immediate execution), 2 (scheduled execution)
        :type RunMode: int
        :param ExpectTime: Expected execution time in the format of yyyy-mm-dd hh:mm:ss. If runMode=2, this field is required
        :type ExpectTime: str
        :param MigrateType: Data migration type. Value range: 1 (structural migration), 2 (full migration), 3 (full + incremental migration)
        :type MigrateType: int
        :param MigrateObject: Migration subject. 1: entire instance; 2: specified table
        :type MigrateObject: int
        :param ConsistencyType: Parameter of spot data consistency check. 1: not configured; 2: full check; 3: spot check; 4: check inconsistent tables only; 5: no check
        :type ConsistencyType: int
        :param IsOverrideRoot: Whether to overwrite the target database with the root account of the source database. Value range: 0 (no), 1 (yes). This value should be 0 for table or structural migration
        :type IsOverrideRoot: int
        :param ExternParams: Additional parameters for different databases, which are described in JSON format. 
The following parameters can be defined for Redis: 
{ 
	"ClientOutputBufferHardLimit":512, 	Hard capacity limit of slave buffer (MB) 
	"ClientOutputBufferSoftLimit":512, 	Soft capacity limit of slave buffer (MB) 
	"ClientOutputBufferPersistTime":60, Soft limit duration of slave buffer (s) 
	"ReplBacklogSize":512, 	Circular buffer capacity limit (MB) 
	"ReplTimeout":120, 		Replication timeout period (s) 
}
The following parameters can be defined for MongoDB: 
{
	'SrcAuthDatabase':'admin', 
	'SrcAuthFlag': "1", 
	'SrcAuthMechanism':"SCRAM-SHA-1"
}
MySQL currently does not support configuring additional parameters.
        :type ExternParams: str
        :param ConsistencyParams: Only used for "spot data consistency check". It is required if ConsistencyType is spot check
        :type ConsistencyParams: :class:`tencentcloud.dts.v20180330.models.ConsistencyParams`
        """
        self.RunMode = None
        self.ExpectTime = None
        self.MigrateType = None
        self.MigrateObject = None
        self.ConsistencyType = None
        self.IsOverrideRoot = None
        self.ExternParams = None
        self.ConsistencyParams = None


    def _deserialize(self, params):
        self.RunMode = params.get("RunMode")
        self.ExpectTime = params.get("ExpectTime")
        self.MigrateType = params.get("MigrateType")
        self.MigrateObject = params.get("MigrateObject")
        self.ConsistencyType = params.get("ConsistencyType")
        self.IsOverrideRoot = params.get("IsOverrideRoot")
        self.ExternParams = params.get("ExternParams")
        if params.get("ConsistencyParams") is not None:
            self.ConsistencyParams = ConsistencyParams()
            self.ConsistencyParams._deserialize(params.get("ConsistencyParams"))


class MigrateStepDetailInfo(AbstractModel):
    """Information of steps in migration

    """

    def __init__(self):
        """
        :param StepNo: Step number
        :type StepNo: int
        :param StepName: Step name
        :type StepName: str
        :param StepId: Step ID
        :type StepId: str
        :param Status: Step status. Value range: 0 (default), 1 (succeeded), 2 (failed), 3 (in progress), 4 (not started)
        :type Status: int
        :param StartTime: Start time of current step in the format of `yyyy-mm-dd hh:mm:ss`. This field is meaningless if it does not exist or is empty
Note: this field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None
        self.StartTime = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")


class ModifyMigrateJobRequest(AbstractModel):
    """ModifyMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: ID of the data migration task to be modified
        :type JobId: str
        :param JobName: Data migration task name
        :type JobName: str
        :param MigrateOption: Migration task configuration options
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcAccessType: Source instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance)
        :type SrcAccessType: str
        :param SrcInfo: Source instance information, which is correlated with the migration task type
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstAccessType: Target instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance). Currently, only `cdb` is supported
        :type DstAccessType: str
        :param DstInfo: Target instance information. The region where the target instance is located cannot be modified.
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: When migrating the specified table, you need to set the information of the source database table to be migrated, which should be described in JSON string format. Below are examples.

For databases with a database-table structure:
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
For databases with a database-schema-table structure:
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]

This field does not need to be set when the entire instance is to be migrated
        :type DatabaseInfo: str
        """
        self.JobId = None
        self.JobName = None
        self.MigrateOption = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class ModifyMigrateJobResponse(AbstractModel):
    """ModifyMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySyncJobRequest(AbstractModel):
    """ModifySyncJob request structure.

    """

    def __init__(self):
        """
        :param JobId: ID of the disaster recovery sync task to be modified
        :type JobId: str
        :param JobName: Name of the disaster recovery sync task
        :type JobName: str
        :param SyncOption: Configuration options of a disaster recovery sync task
        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`
        :param DatabaseInfo: When syncing the specified table, you need to set the information of the source table to be synced, which should be described in JSON string format. Below are examples.
For databases with a database-table structure:
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
        :type DatabaseInfo: str
        """
        self.JobId = None
        self.JobName = None
        self.SyncOption = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("SyncOption") is not None:
            self.SyncOption = SyncOption()
            self.SyncOption._deserialize(params.get("SyncOption"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class ModifySyncJobResponse(AbstractModel):
    """ModifySyncJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SrcInfo(AbstractModel):
    """Source instance information

    """

    def __init__(self):
        """
        :param AccessKey: Alibaba Cloud AccessKey, which is applicable if the source database is an Alibaba Cloud ApsaraDB for RDS 5.6 instance
        :type AccessKey: str
        :param Ip: Instance IP address
        :type Ip: str
        :param Port: Instance port
        :type Port: int
        :param User: Instance username
        :type User: str
        :param Password: Instance password
        :type Password: str
        :param RdsInstanceId: Alibaba Cloud ApsaraDB for RDS instance ID, which is applicable if the source database is an Alibaba Cloud ApsaraDB for RDS 5.6/5.7 instance
        :type RdsInstanceId: str
        :param CvmInstanceId: Short CVM instance ID in the format of `ins-olgl39y8`. It is the same as the instance ID displayed on the CVM Console page. For CVM-based self-created instances, this field needs to be passed in
        :type CvmInstanceId: str
        :param UniqDcgId: Direct Connect gateway ID in the format of dcg-0rxtqqxb
        :type UniqDcgId: str
        :param VpcId: VPC ID in the format of vpc-92jblxto
        :type VpcId: str
        :param SubnetId: VPC Subnet ID in the format of subnet-3paxmkdz
        :type SubnetId: str
        :param UniqVpnGwId: VPN gateway ID in the format of vpngw-9ghexg7q
        :type UniqVpnGwId: str
        :param InstanceId: Database instance ID in the format of cdb-powiqx8q
        :type InstanceId: str
        :param Region: Region name, such as ap-guangzhou
        :type Region: str
        :param Supplier: For Alibaba Cloud ApsaraDB for RDS instances, enter "aliyun"; otherwise, enter "others"
        :type Supplier: str
        :param CcnId: CCN instance ID, such as ccn-afp6kltc
Note: This field may return null, indicating that no valid values can be obtained.
        :type CcnId: str
        :param EngineVersion: Database version. This parameter is valid only when the instance is an RDS instance. Value: 5.6 or 5.7. Default value: 5.6
        :type EngineVersion: str
        """
        self.AccessKey = None
        self.Ip = None
        self.Port = None
        self.User = None
        self.Password = None
        self.RdsInstanceId = None
        self.CvmInstanceId = None
        self.UniqDcgId = None
        self.VpcId = None
        self.SubnetId = None
        self.UniqVpnGwId = None
        self.InstanceId = None
        self.Region = None
        self.Supplier = None
        self.CcnId = None
        self.EngineVersion = None


    def _deserialize(self, params):
        self.AccessKey = params.get("AccessKey")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.RdsInstanceId = params.get("RdsInstanceId")
        self.CvmInstanceId = params.get("CvmInstanceId")
        self.UniqDcgId = params.get("UniqDcgId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.UniqVpnGwId = params.get("UniqVpnGwId")
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.Supplier = params.get("Supplier")
        self.CcnId = params.get("CcnId")
        self.EngineVersion = params.get("EngineVersion")


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartSyncJobRequest(AbstractModel):
    """StartSyncJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Disaster recovery sync task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class StartSyncJobResponse(AbstractModel):
    """StartSyncJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SyncCheckStepInfo(AbstractModel):
    """Check steps for a disaster recovery task

    """

    def __init__(self):
        """
        :param StepNo: Step number
        :type StepNo: int
        :param StepName: Step name
        :type StepName: str
        :param StepCode: Code of the step execution result
        :type StepCode: int
        :param StepMessage: Message about the step execution result
        :type StepMessage: str
        """
        self.StepNo = None
        self.StepName = None
        self.StepCode = None
        self.StepMessage = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepCode = params.get("StepCode")
        self.StepMessage = params.get("StepMessage")


class SyncDetailInfo(AbstractModel):
    """Describes the specific process of the sync task.

    """

    def __init__(self):
        """
        :param StepAll: Total number of steps
        :type StepAll: int
        :param StepNow: Current step
        :type StepNow: int
        :param Progress: Overall progress
        :type Progress: str
        :param CurrentStepProgress: Progress of the current step
        :type CurrentStepProgress: str
        :param MasterSlaveDistance: Master/slave delay in MB
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: Master/slave delay in seconds
        :type SecondsBehindMaster: int
        :param StepInfo: Step information
        :type StepInfo: list of SyncStepDetailInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.CurrentStepProgress = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        self.CurrentStepProgress = params.get("CurrentStepProgress")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = SyncStepDetailInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)


class SyncInstanceInfo(AbstractModel):
    """Instance information of disaster recovery sync, which records the information of the master instance or disaster recovery instance

    """

    def __init__(self):
        """
        :param Region: Region name, such as ap-guangzhou
        :type Region: str
        :param InstanceId: Short instance ID
        :type InstanceId: str
        """
        self.Region = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")


class SyncJobInfo(AbstractModel):
    """Disaster recovery sync task information

    """

    def __init__(self):
        """
        :param JobId: Disaster recovery task ID
        :type JobId: str
        :param JobName: Disaster recovery task name
        :type JobName: str
        :param SyncOption: Task sync
        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`
        :param SrcAccessType: Source access type
        :type SrcAccessType: str
        :param SrcDatabaseType: Source data type
        :type SrcDatabaseType: str
        :param SrcInfo: Source instance information
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DstAccessType: Disaster recovery access type
        :type DstAccessType: str
        :param DstDatabaseType: Disaster recovery data type
        :type DstDatabaseType: str
        :param DstInfo: Disaster recovery instance information
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param Detail: Task information
        :type Detail: :class:`tencentcloud.dts.v20180330.models.SyncDetailInfo`
        :param Status: Task status
        :type Status: int
        :param DatabaseInfo: Table to be migrated
        :type DatabaseInfo: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        """
        self.JobId = None
        self.JobName = None
        self.SyncOption = None
        self.SrcAccessType = None
        self.SrcDatabaseType = None
        self.SrcInfo = None
        self.DstAccessType = None
        self.DstDatabaseType = None
        self.DstInfo = None
        self.Detail = None
        self.Status = None
        self.DatabaseInfo = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("SyncOption") is not None:
            self.SyncOption = SyncOption()
            self.SyncOption._deserialize(params.get("SyncOption"))
        self.SrcAccessType = params.get("SrcAccessType")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SyncInstanceInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstAccessType = params.get("DstAccessType")
        self.DstDatabaseType = params.get("DstDatabaseType")
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        if params.get("Detail") is not None:
            self.Detail = SyncDetailInfo()
            self.Detail._deserialize(params.get("Detail"))
        self.Status = params.get("Status")
        self.DatabaseInfo = params.get("DatabaseInfo")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class SyncOption(AbstractModel):
    """Configuration options of a disaster recovery sync task

    """

    def __init__(self):
        """
        :param SyncObject: Sync object. 1: entire instance; 2: specified table
        :type SyncObject: int
        :param RunMode: Sync start configuration. 1: start immediately
        :type RunMode: int
        :param SyncType: Sync mode. 3: full + incremental sync
        :type SyncType: int
        :param ConsistencyType: Data consistency check. 1: no configuration required
        :type ConsistencyType: int
        """
        self.SyncObject = None
        self.RunMode = None
        self.SyncType = None
        self.ConsistencyType = None


    def _deserialize(self, params):
        self.SyncObject = params.get("SyncObject")
        self.RunMode = params.get("RunMode")
        self.SyncType = params.get("SyncType")
        self.ConsistencyType = params.get("ConsistencyType")


class SyncStepDetailInfo(AbstractModel):
    """Sync task progress

    """

    def __init__(self):
        """
        :param StepNo: Step number
        :type StepNo: int
        :param StepName: Step name
        :type StepName: str
        :param CanStop: Whether it can be stopped
        :type CanStop: int
        :param StepId: Step ID
        :type StepId: int
        """
        self.StepNo = None
        self.StepName = None
        self.CanStop = None
        self.StepId = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.CanStop = params.get("CanStop")
        self.StepId = params.get("StepId")