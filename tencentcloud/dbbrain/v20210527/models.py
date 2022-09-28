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


class CreateProxySessionKillTaskRequest(AbstractModel):
    """CreateProxySessionKillTask request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param Product: Service type. Valid value: `redis` (TencentDB for Redis).
        :type Product: str
        """
        self.InstanceId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxySessionKillTaskResponse(AbstractModel):
    """CreateProxySessionKillTask response structure.

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task ID that is returned after the session killing task is created.
        :type AsyncRequestId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class DescribeDBDiagEventsRequest(AbstractModel):
    """DescribeDBDiagEvents request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time in the format of “2021-05-27 00:00:00”. The earliest time that can be queried is 30 days before the current time.
        :type StartTime: str
        :param EndTime: End time in the format of "2021-05-27 01:00:00". The interval between the end time and the start time can be up to 7 days.
        :type EndTime: str
        :param Severities: Risk level list. Valid values in descending order of severity: `1` (critical), `2` (serious), `3` (alarm), `4` (warning), `5` (healthy).
        :type Severities: list of int
        :param InstanceIds: Instance ID list.
        :type InstanceIds: list of str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 50.
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Severities = None
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Severities = params.get("Severities")
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventsResponse(AbstractModel):
    """DescribeDBDiagEvents response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of diagnosis events.
        :type TotalCount: int
        :param Items: Diagnosis event list.
        :type Items: list of DiagHistoryEventItem
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
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiagDBInstancesRequest(AbstractModel):
    """DescribeDiagDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param IsSupported: Whether it is an instance supported by DBbrain. It is fixed to `true`.
        :type IsSupported: bool
        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.
        :type Product: str
        :param Offset: Pagination parameter indicating the offset.
        :type Offset: int
        :param Limit: Pagination parameter. Maximum value: 100.
        :type Limit: int
        :param InstanceNames: Query by instance name.
        :type InstanceNames: list of str
        :param InstanceIds: Query by instance ID.
        :type InstanceIds: list of str
        :param Regions: Query by region.
        :type Regions: list of str
        """
        self.IsSupported = None
        self.Product = None
        self.Offset = None
        self.Limit = None
        self.InstanceNames = None
        self.InstanceIds = None
        self.Regions = None


    def _deserialize(self, params):
        self.IsSupported = params.get("IsSupported")
        self.Product = params.get("Product")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceNames = params.get("InstanceNames")
        self.InstanceIds = params.get("InstanceIds")
        self.Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagDBInstancesResponse(AbstractModel):
    """DescribeDiagDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of instances.
        :type TotalCount: int
        :param DbScanStatus: Status of all instance inspection. 0: all instance inspection enabled, 1: all instance inspection disabled.
        :type DbScanStatus: int
        :param Items: Instance information.
        :type Items: list of InstanceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DbScanStatus = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.DbScanStatus = params.get("DbScanStatus")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMySqlProcessListRequest(AbstractModel):
    """DescribeMySqlProcessList request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param ID: Thread ID, which is used to filter the thread list.
        :type ID: int
        :param User: Thread operation account name, which is used to filter the thread list.
        :type User: str
        :param Host: Thread operation host address, which is used to filter the thread list.
        :type Host: str
        :param DB: Thread operation database, which is used to filter the thread list.
        :type DB: str
        :param State: Thread operation status, which is used to filter the thread list.
        :type State: str
        :param Command: Thread execution type, which is used to filter the thread list.
        :type Command: str
        :param Time: Minimum operation duration of the thread in seconds, which is used to filter the list of threads whose operation duration is greater than this value.
        :type Time: int
        :param Info: Thread operation statement, which is used to filter the thread list.
        :type Info: str
        :param Limit: Number of returned results. Default value: 20.
        :type Limit: int
        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.
        :type Product: str
        """
        self.InstanceId = None
        self.ID = None
        self.User = None
        self.Host = None
        self.DB = None
        self.State = None
        self.Command = None
        self.Time = None
        self.Info = None
        self.Limit = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ID = params.get("ID")
        self.User = params.get("User")
        self.Host = params.get("Host")
        self.DB = params.get("DB")
        self.State = params.get("State")
        self.Command = params.get("Command")
        self.Time = params.get("Time")
        self.Info = params.get("Info")
        self.Limit = params.get("Limit")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMySqlProcessListResponse(AbstractModel):
    """DescribeMySqlProcessList response structure.

    """

    def __init__(self):
        r"""
        :param ProcessList: List of real-time threads.
        :type ProcessList: list of MySqlProcess
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProcessList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProcessList") is not None:
            self.ProcessList = []
            for item in params.get("ProcessList"):
                obj = MySqlProcess()
                obj._deserialize(item)
                self.ProcessList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxySessionKillTasksRequest(AbstractModel):
    """DescribeProxySessionKillTasks request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param AsyncRequestIds: The async session killing task ID, which is obtained after the API `CreateProxySessionKillTask` is successfully called.
        :type AsyncRequestIds: list of int
        :param Product: Service type. Valid value: `redis` (TencentDB for Redis).
        :type Product: str
        """
        self.InstanceId = None
        self.AsyncRequestIds = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySessionKillTasksResponse(AbstractModel):
    """DescribeProxySessionKillTasks response structure.

    """

    def __init__(self):
        r"""
        :param Tasks: Session killing task details.
        :type Tasks: list of TaskInfo
        :param TotalCount: Total number of tasks.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Tasks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRedisTopKeyPrefixListRequest(AbstractModel):
    """DescribeRedisTopKeyPrefixList request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Date: Date for query, such as `2021-05-27`. You can select a date as early as in the last 30 days for query.
        :type Date: str
        :param Product: Service type. Valid value: `redis` (TencentDB for Redis).
        :type Product: str
        :param Limit: The number of queried items. Default value: `20`. Max value: `100`.
        :type Limit: int
        """
        self.InstanceId = None
        self.Date = None
        self.Product = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        self.Product = params.get("Product")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisTopKeyPrefixListResponse(AbstractModel):
    """DescribeRedisTopKeyPrefixList response structure.

    """

    def __init__(self):
        r"""
        :param Items: List of top key prefixes
        :type Items: list of RedisPreKeySpaceData
        :param Timestamp: Data collection timestamp in seconds
        :type Timestamp: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Items = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RedisPreKeySpaceData()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Timestamp = params.get("Timestamp")
        self.RequestId = params.get("RequestId")


class DescribeSlowLogUserHostStatsRequest(AbstractModel):
    """DescribeSlowLogUserHostStats request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param StartTime: Start time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.
        :type StartTime: str
        :param EndTime: End time of the time range in the format of yyyy-MM-dd HH:mm:ss, such as 2019-09-10 12:13:14.
        :type EndTime: str
        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.
        :type Product: str
        :param Md5: MD5 value of SOL template
        :type Md5: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None
        self.Md5 = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")
        self.Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogUserHostStatsResponse(AbstractModel):
    """DescribeSlowLogUserHostStats response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of source addresses.
        :type TotalCount: int
        :param Items: Detailed list of the proportion of slow logs from each source address.
        :type Items: list of SlowLogHost
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
                obj = SlowLogHost()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceSchemasRequest(AbstractModel):
    """DescribeTopSpaceSchemas request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param Limit: Number of returned top databases. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param SortBy: Field used to sort top databases. Valid values: DataLength, IndexLength, TotalLength, DataFree, FragRatio, TableRows, PhysicalFileSize (supported only by TencentDB for MySQL instances). For TencentDB for MySQL instances, the default value is `PhysicalFileSize`. For other database instances, the default value is `TotalLength`.
        :type SortBy: str
        :param Product: Service type. Valid values: mysql (TencentDB for MySQL), cynosdb (TDSQL-C for MySQL). Default value: mysql.
        :type Product: str
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemasResponse(AbstractModel):
    """DescribeTopSpaceSchemas response structure.

    """

    def __init__(self):
        r"""
        :param TopSpaceSchemas: List of the returned space statistics of top databases.
        :type TopSpaceSchemas: list of SchemaSpaceData
        :param Timestamp: Timestamp (in seconds) of database space data collection points
        :type Timestamp: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopSpaceSchemas = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceSchemas") is not None:
            self.TopSpaceSchemas = []
            for item in params.get("TopSpaceSchemas"):
                obj = SchemaSpaceData()
                obj._deserialize(item)
                self.TopSpaceSchemas.append(obj)
        self.Timestamp = params.get("Timestamp")
        self.RequestId = params.get("RequestId")


class DescribeUserSqlAdviceRequest(AbstractModel):
    """DescribeUserSqlAdvice request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param SqlText: SQL statement.
        :type SqlText: str
        :param Schema: Database name.
        :type Schema: str
        :param Product: Service type. Valid values: `mysql` (TencentDB for MySQL), `cynosdb` (TDSQL-C for MySQL), `dbbrain-mysql` (self-built MySQL). Default value: `mysql`.
        :type Product: str
        """
        self.InstanceId = None
        self.SqlText = None
        self.Schema = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserSqlAdviceResponse(AbstractModel):
    """DescribeUserSqlAdvice response structure.

    """

    def __init__(self):
        r"""
        :param Advices: SQL statement optimization suggestions, which can be parsed into JSON arrays. If there is no need for optimization, the output will be empty.
        :type Advices: str
        :param Comments: Notes of SQL statement optimization suggestions, which can be parsed into String arrays. If there is no need for optimization, the output will be empty.
        :type Comments: str
        :param SqlText: SQL statement.
        :type SqlText: str
        :param Schema: Database name.
        :type Schema: str
        :param Tables: DDL information of related tables, which can be parsed into JSON arrays.
        :type Tables: str
        :param SqlPlan: SQL execution plan, which can be parsed into JSON arrays. If there is no need for optimization, the output will be empty.
        :type SqlPlan: str
        :param Cost: Cost saving details after SQL statement optimization, which can be parsed into JSON arrays. If there is no need for optimization, the output will be empty.
        :type Cost: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Advices = None
        self.Comments = None
        self.SqlText = None
        self.Schema = None
        self.Tables = None
        self.SqlPlan = None
        self.Cost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Advices = params.get("Advices")
        self.Comments = params.get("Comments")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        self.Tables = params.get("Tables")
        self.SqlPlan = params.get("SqlPlan")
        self.Cost = params.get("Cost")
        self.RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """Instance diagnosis event

    """

    def __init__(self):
        r"""
        :param DiagType: Diagnosis type.
        :type DiagType: str
        :param EndTime: End time.
        :type EndTime: str
        :param StartTime: Start time.
        :type StartTime: str
        :param EventId: Unique event ID.
        :type EventId: int
        :param Severity: Severity, which can be divided into 5 levels: 1: fatal, 2: severe, 3: warning, 4: notice, 5: healthy.
        :type Severity: int
        :param Outline: Diagnosis summary.
        :type Outline: str
        :param DiagItem: Diagnosis item description.
        :type DiagItem: str
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param Metric: Reserved field.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Metric: str
        :param Region: Region.
        :type Region: str
        """
        self.DiagType = None
        self.EndTime = None
        self.StartTime = None
        self.EventId = None
        self.Severity = None
        self.Outline = None
        self.DiagItem = None
        self.InstanceId = None
        self.Metric = None
        self.Region = None


    def _deserialize(self, params):
        self.DiagType = params.get("DiagType")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.EventId = params.get("EventId")
        self.Severity = params.get("Severity")
        self.Outline = params.get("Outline")
        self.DiagItem = params.get("DiagItem")
        self.InstanceId = params.get("InstanceId")
        self.Metric = params.get("Metric")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfs(AbstractModel):
    """Instance configuration.

    """

    def __init__(self):
        r"""
        :param DailyInspection: Whether to enable database inspection. Valid values: Yes, No.
        :type DailyInspection: str
        :param OverviewDisplay: Whether to enable instance overview. Valid values: Yes, No.
        :type OverviewDisplay: str
        """
        self.DailyInspection = None
        self.OverviewDisplay = None


    def _deserialize(self, params):
        self.DailyInspection = params.get("DailyInspection")
        self.OverviewDisplay = params.get("OverviewDisplay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """Queries the list of instances and returns their information.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param InstanceName: Instance name.
        :type InstanceName: str
        :param Region: Instance region.
        :type Region: str
        :param HealthScore: Health score.
        :type HealthScore: int
        :param Product: Service.
        :type Product: str
        :param EventCount: Number of exceptions.
        :type EventCount: int
        :param InstanceType: Instance type. Valid values: 1 (MASTER), 2 (DR), 3 (RO), 4 (SDR)
        :type InstanceType: int
        :param Cpu: Number of cores.
        :type Cpu: int
        :param Memory: Memory in MB.
        :type Memory: int
        :param Volume: Disk storage in GB.
        :type Volume: int
        :param EngineVersion: Database version.
        :type EngineVersion: str
        :param Vip: Private network address.
        :type Vip: str
        :param Vport: Private network port.
        :type Vport: int
        :param Source: Access source.
        :type Source: str
        :param GroupId: Group ID.
        :type GroupId: str
        :param GroupName: Group name.
        :type GroupName: str
        :param Status: Instance status. Valid values: 0 (delivering), 1 (running), 4 (terminating), 5 (isolated)
        :type Status: int
        :param UniqSubnetId: Unified subnet ID.
        :type UniqSubnetId: str
        :param DeployMode: TencentDB instance type.
        :type DeployMode: str
        :param InitFlag: TencentDB instance initialization flag. Valid values: 0 (not initialized), 1 (initialized).
        :type InitFlag: int
        :param TaskStatus: Task status.
        :type TaskStatus: int
        :param UniqVpcId: Unified VPC ID.
        :type UniqVpcId: str
        :param InstanceConf: Instance inspection/overview status.
        :type InstanceConf: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`
        :param DeadlineTime: Resource expiration time.
        :type DeadlineTime: str
        :param IsSupported: Whether it is an instance supported by DBbrain.
        :type IsSupported: bool
        :param SecAuditStatus: Status of instance security audit log. Valid values: ON (enabled), OFF (disabled).
        :type SecAuditStatus: str
        :param AuditPolicyStatus: Status of instance audit log. Valid values: ALL_AUDIT (full audit is enabled), RULE_AUDIT (rule audit is enabled), UNBOUND (audit is disabled).
        :type AuditPolicyStatus: str
        :param AuditRunningStatus: Running status of instance audit log. Valid values: normal (running), paused (suspension due to overdue payment).
        :type AuditRunningStatus: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.HealthScore = None
        self.Product = None
        self.EventCount = None
        self.InstanceType = None
        self.Cpu = None
        self.Memory = None
        self.Volume = None
        self.EngineVersion = None
        self.Vip = None
        self.Vport = None
        self.Source = None
        self.GroupId = None
        self.GroupName = None
        self.Status = None
        self.UniqSubnetId = None
        self.DeployMode = None
        self.InitFlag = None
        self.TaskStatus = None
        self.UniqVpcId = None
        self.InstanceConf = None
        self.DeadlineTime = None
        self.IsSupported = None
        self.SecAuditStatus = None
        self.AuditPolicyStatus = None
        self.AuditRunningStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.HealthScore = params.get("HealthScore")
        self.Product = params.get("Product")
        self.EventCount = params.get("EventCount")
        self.InstanceType = params.get("InstanceType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.EngineVersion = params.get("EngineVersion")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Source = params.get("Source")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Status = params.get("Status")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.DeployMode = params.get("DeployMode")
        self.InitFlag = params.get("InitFlag")
        self.TaskStatus = params.get("TaskStatus")
        self.UniqVpcId = params.get("UniqVpcId")
        if params.get("InstanceConf") is not None:
            self.InstanceConf = InstanceConfs()
            self.InstanceConf._deserialize(params.get("InstanceConf"))
        self.DeadlineTime = params.get("DeadlineTime")
        self.IsSupported = params.get("IsSupported")
        self.SecAuditStatus = params.get("SecAuditStatus")
        self.AuditPolicyStatus = params.get("AuditPolicyStatus")
        self.AuditRunningStatus = params.get("AuditRunningStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySqlProcess(AbstractModel):
    """Relational database thread

    """

    def __init__(self):
        r"""
        :param ID: Thread ID.
        :type ID: str
        :param User: Thread operation account name.
        :type User: str
        :param Host: Thread operation host address.
        :type Host: str
        :param DB: Thread operation database.
        :type DB: str
        :param State: Thread operation status.
        :type State: str
        :param Command: Thread execution type.
        :type Command: str
        :param Time: Thread operation duration in seconds.
        :type Time: str
        :param Info: Thread operation statement.
        :type Info: str
        """
        self.ID = None
        self.User = None
        self.Host = None
        self.DB = None
        self.State = None
        self.Command = None
        self.Time = None
        self.Info = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.User = params.get("User")
        self.Host = params.get("Host")
        self.DB = params.get("DB")
        self.State = params.get("State")
        self.Command = params.get("Command")
        self.Time = params.get("Time")
        self.Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisPreKeySpaceData(AbstractModel):
    """Space information of Redis key prefixes

    """

    def __init__(self):
        r"""
        :param AveElementSize: Average element length
        :type AveElementSize: int
        :param Length: Total memory usage in bytes
        :type Length: int
        :param KeyPreIndex: Key prefix
        :type KeyPreIndex: str
        :param ItemCount: The number of elements
        :type ItemCount: int
        :param Count: The number of keys
        :type Count: int
        :param MaxElementSize: The max element length
        :type MaxElementSize: int
        """
        self.AveElementSize = None
        self.Length = None
        self.KeyPreIndex = None
        self.ItemCount = None
        self.Count = None
        self.MaxElementSize = None


    def _deserialize(self, params):
        self.AveElementSize = params.get("AveElementSize")
        self.Length = params.get("Length")
        self.KeyPreIndex = params.get("KeyPreIndex")
        self.ItemCount = params.get("ItemCount")
        self.Count = params.get("Count")
        self.MaxElementSize = params.get("MaxElementSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceData(AbstractModel):
    """Database space statistics.

    """

    def __init__(self):
        r"""
        :param TableSchema: Database name.
        :type TableSchema: str
        :param DataLength: Data space in MB.
        :type DataLength: float
        :param IndexLength: Index space in MB.
        :type IndexLength: float
        :param DataFree: Fragmented space in MB.
        :type DataFree: float
        :param TotalLength: Total space usage in MB.
        :type TotalLength: float
        :param FragRatio: Fragmentation rate in %.
        :type FragRatio: float
        :param TableRows: Number of rows.
        :type TableRows: int
        :param PhysicalFileSize: Total size in MB of physical files exclusive to all tables in the database.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhysicalFileSize: float
        """
        self.TableSchema = None
        self.DataLength = None
        self.IndexLength = None
        self.DataFree = None
        self.TotalLength = None
        self.FragRatio = None
        self.TableRows = None
        self.PhysicalFileSize = None


    def _deserialize(self, params):
        self.TableSchema = params.get("TableSchema")
        self.DataLength = params.get("DataLength")
        self.IndexLength = params.get("IndexLength")
        self.DataFree = params.get("DataFree")
        self.TotalLength = params.get("TotalLength")
        self.FragRatio = params.get("FragRatio")
        self.TableRows = params.get("TableRows")
        self.PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogHost(AbstractModel):
    """Details of slow log source addresses.

    """

    def __init__(self):
        r"""
        :param UserHost: Source addresses.
        :type UserHost: str
        :param Ratio: Proportion (in %) of slow logs from this source address to the total number of slow logs.
        :type Ratio: float
        :param Count: Number of slow logs from this source address.
        :type Count: int
        """
        self.UserHost = None
        self.Ratio = None
        self.Count = None


    def _deserialize(self, params):
        self.UserHost = params.get("UserHost")
        self.Ratio = params.get("Ratio")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    """Information about Redis session killing task status

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: Async task ID.
        :type AsyncRequestId: int
        :param InstProxyList: List of all proxies of the current instance.
        :type InstProxyList: list of str
        :param InstProxyCount: Total number of proxies of the current instance.
        :type InstProxyCount: int
        :param CreateTime: Task creation time.
        :type CreateTime: str
        :param StartTime: Task start time.
        :type StartTime: str
        :param TaskStatus: Task status. Valid values: `created` (create), `chosen` (to be executed), `running` (being executed), `failed` (failed), and `finished` (completed).
        :type TaskStatus: str
        :param FinishedProxyList: IDs of the proxies that have completed the session killing tasks.
        :type FinishedProxyList: list of str
        :param FailedProxyList: IDs of the proxies that failed to execute the session killing tasks.
        :type FailedProxyList: list of str
        :param EndTime: Task end time.
        :type EndTime: str
        :param Progress: Task progress.
        :type Progress: int
        :param InstanceId: Instance ID.
        :type InstanceId: str
        """
        self.AsyncRequestId = None
        self.InstProxyList = None
        self.InstProxyCount = None
        self.CreateTime = None
        self.StartTime = None
        self.TaskStatus = None
        self.FinishedProxyList = None
        self.FailedProxyList = None
        self.EndTime = None
        self.Progress = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.InstProxyList = params.get("InstProxyList")
        self.InstProxyCount = params.get("InstProxyCount")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.TaskStatus = params.get("TaskStatus")
        self.FinishedProxyList = params.get("FinishedProxyList")
        self.FailedProxyList = params.get("FailedProxyList")
        self.EndTime = params.get("EndTime")
        self.Progress = params.get("Progress")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        