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


class CancelTaskRequest(AbstractModel):
    """CancelTask request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Globally unique task ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Column(AbstractModel):
    """Column information of the data table.

    """

    def __init__(self):
        r"""
        :param Name: Column name, which is case-insensitive and can contain up to 25 characters.
        :type Name: str
        :param Type: Column type. Valid values:
string|tinyint|smallint|int|bigint|boolean|float|double|decimal|timestamp|date|binary|array<data_type>|map<primitive_type, data_type>|struct<col_name : data_type [COMMENT col_comment], ...>|uniontype<data_type, data_type, ...>.
        :type Type: str
        :param Comment: Class comment.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Comment: str
        :param Precision: Length of the entire numeric value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Precision: int
        :param Scale: Length of the decimal part
Note: This field may return null, indicating that no valid values can be obtained.
        :type Scale: int
        :param Nullable: Whether the column is null.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nullable: str
        :param Position: Field position
Note: This field may return null, indicating that no valid values can be obtained.
        :type Position: int
        :param CreateTime: Field creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param ModifiedTime: Field modification time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param IsPartition: Whether the column is the partition field.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsPartition: bool
        """
        self.Name = None
        self.Type = None
        self.Comment = None
        self.Precision = None
        self.Scale = None
        self.Nullable = None
        self.Position = None
        self.CreateTime = None
        self.ModifiedTime = None
        self.IsPartition = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        self.Precision = params.get("Precision")
        self.Scale = params.get("Scale")
        self.Nullable = params.get("Nullable")
        self.Position = params.get("Position")
        self.CreateTime = params.get("CreateTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.IsPartition = params.get("IsPartition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataEngineRequest(AbstractModel):
    """CreateDataEngine request structure.

    """

    def __init__(self):
        r"""
        :param EngineType: The engine type. Valid values: `spark` and `presto`.
        :type EngineType: str
        :param DataEngineName: The name of the virtual cluster.
        :type DataEngineName: str
        :param ClusterType: The cluster type. Valid values: `spark_private`, `presto_private`, `presto_cu`, and `spark_cu`.
        :type ClusterType: str
        :param Mode: The billing mode. Valid values: `0` (shared engine), `1` (pay-as-you-go), and `2` (monthly subscription).
        :type Mode: int
        :param AutoResume: Whether to automatically start the clusters.
        :type AutoResume: bool
        :param MinClusters: The minimum number of clusters.
        :type MinClusters: int
        :param MaxClusters: The maximum number of clusters.
        :type MaxClusters: int
        :param DefaultDataEngine: Whether the cluster is the default one.
        :type DefaultDataEngine: bool
        :param CidrBlock: The VPC CIDR block.
        :type CidrBlock: str
        :param Message: The description.
        :type Message: str
        :param Size: The cluster size.
        :type Size: int
        :param PayMode: The pay mode. Valid value: `0` (postpaid, default) and `1` (prepaid) (currently not available).
        :type PayMode: int
        :param TimeSpan: The resource period. For the postpaid mode, the value is 3600 (default); for the prepaid mode, the value must be in the range of 1–120, representing purchasing the resource for 1–120 months.
        :type TimeSpan: int
        :param TimeUnit: The unit of the resource period. Valid values: `s` (default) for the postpaid mode and `m` for the prepaid mode.
        :type TimeUnit: str
        :param AutoRenew: The auto-renewal status of the resource. For the postpaid mode, no renewal is required, and the value is fixed to `0`. For the prepaid mode, valid values are `0` (manual), `1` (auto), and `2` (no renewal). If this parameter is set to `0` for a key account in the prepaid mode, auto-renewal applies. It defaults to `0`.
        :type AutoRenew: int
        :param Tags: The tags to be set for the resource being created.
        :type Tags: list of TagInfo
        :param AutoSuspend: Whether to automatically suspend clusters. Valid values: `false` (default, no) and `true` (yes).
        :type AutoSuspend: bool
        :param CrontabResumeSuspend: Whether to enable scheduled start and suspension of clusters. Valid values: `0` (disable) and `1` (enable). Note: This policy and the auto-suspension policy are mutually exclusive.
        :type CrontabResumeSuspend: int
        :param CrontabResumeSuspendStrategy: The complex policy for scheduled start and suspension, including the start/suspension time and suspension policy.
        :type CrontabResumeSuspendStrategy: :class:`tencentcloud.dlc.v20210125.models.CrontabResumeSuspendStrategy`
        :param EngineExecType: The type of tasks to be executed by the engine, which defaults to SQL.
        :type EngineExecType: str
        :param MaxConcurrency: The max task concurrency of a cluster, which defaults to 5.
        :type MaxConcurrency: int
        :param TolerableQueueTime: The task queue time limit, which defaults to 0. When the actual queue time exceeds the value set here, scale-out may be triggered. Setting this parameter to 0 represents that scale-out may be triggered immediately after a task queues up.
        :type TolerableQueueTime: int
        :param AutoSuspendTime: The cluster auto-suspension time, which defaults to 10 min.
        :type AutoSuspendTime: int
        :param ResourceType: The resource type. Valid values: `Standard_CU` (standard) and `Memory_CU` (memory).
        :type ResourceType: str
        :param DataEngineConfigPairs: The advanced configurations of clusters.
        :type DataEngineConfigPairs: list of DataEngineConfigPair
        :param ImageVersionName: The version name of cluster image, such as SuperSQL-P 1.1 and SuperSQL-S 3.2. If no value is passed in, a cluster is created using the latest image version.
        :type ImageVersionName: str
        :param MainClusterName: The name of the primary cluster.
        :type MainClusterName: str
        :param ElasticSwitch: 
        :type ElasticSwitch: bool
        :param ElasticLimit: 
        :type ElasticLimit: int
        """
        self.EngineType = None
        self.DataEngineName = None
        self.ClusterType = None
        self.Mode = None
        self.AutoResume = None
        self.MinClusters = None
        self.MaxClusters = None
        self.DefaultDataEngine = None
        self.CidrBlock = None
        self.Message = None
        self.Size = None
        self.PayMode = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.AutoRenew = None
        self.Tags = None
        self.AutoSuspend = None
        self.CrontabResumeSuspend = None
        self.CrontabResumeSuspendStrategy = None
        self.EngineExecType = None
        self.MaxConcurrency = None
        self.TolerableQueueTime = None
        self.AutoSuspendTime = None
        self.ResourceType = None
        self.DataEngineConfigPairs = None
        self.ImageVersionName = None
        self.MainClusterName = None
        self.ElasticSwitch = None
        self.ElasticLimit = None


    def _deserialize(self, params):
        self.EngineType = params.get("EngineType")
        self.DataEngineName = params.get("DataEngineName")
        self.ClusterType = params.get("ClusterType")
        self.Mode = params.get("Mode")
        self.AutoResume = params.get("AutoResume")
        self.MinClusters = params.get("MinClusters")
        self.MaxClusters = params.get("MaxClusters")
        self.DefaultDataEngine = params.get("DefaultDataEngine")
        self.CidrBlock = params.get("CidrBlock")
        self.Message = params.get("Message")
        self.Size = params.get("Size")
        self.PayMode = params.get("PayMode")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoRenew = params.get("AutoRenew")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoSuspend = params.get("AutoSuspend")
        self.CrontabResumeSuspend = params.get("CrontabResumeSuspend")
        if params.get("CrontabResumeSuspendStrategy") is not None:
            self.CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy()
            self.CrontabResumeSuspendStrategy._deserialize(params.get("CrontabResumeSuspendStrategy"))
        self.EngineExecType = params.get("EngineExecType")
        self.MaxConcurrency = params.get("MaxConcurrency")
        self.TolerableQueueTime = params.get("TolerableQueueTime")
        self.AutoSuspendTime = params.get("AutoSuspendTime")
        self.ResourceType = params.get("ResourceType")
        if params.get("DataEngineConfigPairs") is not None:
            self.DataEngineConfigPairs = []
            for item in params.get("DataEngineConfigPairs"):
                obj = DataEngineConfigPair()
                obj._deserialize(item)
                self.DataEngineConfigPairs.append(obj)
        self.ImageVersionName = params.get("ImageVersionName")
        self.MainClusterName = params.get("MainClusterName")
        self.ElasticSwitch = params.get("ElasticSwitch")
        self.ElasticLimit = params.get("ElasticLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataEngineResponse(AbstractModel):
    """CreateDataEngine response structure.

    """

    def __init__(self):
        r"""
        :param DataEngineId: The ID of the virtual engine.
        :type DataEngineId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataEngineId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataEngineId = params.get("DataEngineId")
        self.RequestId = params.get("RequestId")


class CreateInternalTableRequest(AbstractModel):
    """CreateInternalTable request structure.

    """

    def __init__(self):
        r"""
        :param TableBaseInfo: The basic table information.
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param Columns: The table fields.
        :type Columns: list of TColumn
        :param Partitions: The table partitions.
        :type Partitions: list of TPartition
        :param Properties: The table properties.
        :type Properties: list of Property
        """
        self.TableBaseInfo = None
        self.Columns = None
        self.Partitions = None
        self.Properties = None


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self.TableBaseInfo = TableBaseInfo()
            self.TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = TColumn()
                obj._deserialize(item)
                self.Columns.append(obj)
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = TPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self.Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInternalTableResponse(AbstractModel):
    """CreateInternalTable response structure.

    """

    def __init__(self):
        r"""
        :param Execution: The SQL statements for creating the managed internal table.
        :type Execution: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Execution = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Execution = params.get("Execution")
        self.RequestId = params.get("RequestId")


class CreateResultDownloadRequest(AbstractModel):
    """CreateResultDownload request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The result query task ID.
        :type TaskId: str
        :param Format: The result format.
        :type Format: str
        :param Force: Whether to re-generate a file to download. This parameter applies only when the last task is `timeout` or `error`.
        :type Force: bool
        """
        self.TaskId = None
        self.Format = None
        self.Force = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Format = params.get("Format")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResultDownloadResponse(AbstractModel):
    """CreateResultDownload response structure.

    """

    def __init__(self):
        r"""
        :param DownloadId: The download task ID.
        :type DownloadId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DownloadId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadId = params.get("DownloadId")
        self.RequestId = params.get("RequestId")


class CreateSparkAppRequest(AbstractModel):
    """CreateSparkApp request structure.

    """

    def __init__(self):
        r"""
        :param AppName: Spark application name
        :type AppName: str
        :param AppType: 1: Spark JAR application; 2: Spark streaming application
        :type AppType: int
        :param DataEngine: The data engine executing the Spark job
        :type DataEngine: str
        :param AppFile: Execution entry of the Spark application
        :type AppFile: str
        :param RoleArn: Execution role ID of the Spark job
        :type RoleArn: int
        :param AppDriverSize: Driver resource specification of the Spark job. Valid values: `small`, `medium`, `large`, `xlarge`.
        :type AppDriverSize: str
        :param AppExecutorSize: Executor resource specification of the Spark job. Valid values: `small`, `medium`, `large`, `xlarge`.
        :type AppExecutorSize: str
        :param AppExecutorNums: Number of Spark job executors
        :type AppExecutorNums: int
        :param Eni: This field has been disused. Use the `Datasource` field instead.
        :type Eni: str
        :param IsLocal: Whether it is upload locally. Valid values: `cos`, `lakefs`.
        :type IsLocal: str
        :param MainClass: Main class of the Spark JAR job during execution
        :type MainClass: str
        :param AppConf: Spark configurations separated by line break
        :type AppConf: str
        :param IsLocalJars: Whether it is upload locally. Valid values: `cos`, `lakefs`.
        :type IsLocalJars: str
        :param AppJars: Dependency JAR packages of the Spark JAR job separated by comma
        :type AppJars: str
        :param IsLocalFiles: Whether it is upload locally. Valid values: `cos`, `lakefs`.
        :type IsLocalFiles: str
        :param AppFiles: Dependency resources of the Spark job separated by comma
        :type AppFiles: str
        :param CmdArgs: Command line parameters of the Spark job
        :type CmdArgs: str
        :param MaxRetries: This parameter takes effect only for Spark flow tasks.
        :type MaxRetries: int
        :param DataSource: Data source name
        :type DataSource: str
        :param IsLocalPythonFiles: PySpark: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalPythonFiles: str
        :param AppPythonFiles: PySpark: Python dependency, which can be in .py, .zip, or .egg format. Multiple files should be separated by comma.
        :type AppPythonFiles: str
        :param IsLocalArchives: Archives: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalArchives: str
        :param AppArchives: Archives: Dependency resources
        :type AppArchives: str
        :param SparkImage: The Spark image version.
        :type SparkImage: str
        :param SparkImageVersion: The Spark image version name.
        :type SparkImageVersion: str
        :param AppExecutorMaxNumbers: The specified executor count (max), which defaults to 1. This parameter applies if the "Dynamic" mode is selected. If the "Dynamic" mode is not selected, the executor count is equal to `AppExecutorNums`.
        :type AppExecutorMaxNumbers: int
        """
        self.AppName = None
        self.AppType = None
        self.DataEngine = None
        self.AppFile = None
        self.RoleArn = None
        self.AppDriverSize = None
        self.AppExecutorSize = None
        self.AppExecutorNums = None
        self.Eni = None
        self.IsLocal = None
        self.MainClass = None
        self.AppConf = None
        self.IsLocalJars = None
        self.AppJars = None
        self.IsLocalFiles = None
        self.AppFiles = None
        self.CmdArgs = None
        self.MaxRetries = None
        self.DataSource = None
        self.IsLocalPythonFiles = None
        self.AppPythonFiles = None
        self.IsLocalArchives = None
        self.AppArchives = None
        self.SparkImage = None
        self.SparkImageVersion = None
        self.AppExecutorMaxNumbers = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.AppType = params.get("AppType")
        self.DataEngine = params.get("DataEngine")
        self.AppFile = params.get("AppFile")
        self.RoleArn = params.get("RoleArn")
        self.AppDriverSize = params.get("AppDriverSize")
        self.AppExecutorSize = params.get("AppExecutorSize")
        self.AppExecutorNums = params.get("AppExecutorNums")
        self.Eni = params.get("Eni")
        self.IsLocal = params.get("IsLocal")
        self.MainClass = params.get("MainClass")
        self.AppConf = params.get("AppConf")
        self.IsLocalJars = params.get("IsLocalJars")
        self.AppJars = params.get("AppJars")
        self.IsLocalFiles = params.get("IsLocalFiles")
        self.AppFiles = params.get("AppFiles")
        self.CmdArgs = params.get("CmdArgs")
        self.MaxRetries = params.get("MaxRetries")
        self.DataSource = params.get("DataSource")
        self.IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self.AppPythonFiles = params.get("AppPythonFiles")
        self.IsLocalArchives = params.get("IsLocalArchives")
        self.AppArchives = params.get("AppArchives")
        self.SparkImage = params.get("SparkImage")
        self.SparkImageVersion = params.get("SparkImageVersion")
        self.AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkAppResponse(AbstractModel):
    """CreateSparkApp response structure.

    """

    def __init__(self):
        r"""
        :param SparkAppId: The unique ID of the application.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkAppId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SparkAppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SparkAppId = params.get("SparkAppId")
        self.RequestId = params.get("RequestId")


class CreateSparkAppTaskRequest(AbstractModel):
    """CreateSparkAppTask request structure.

    """

    def __init__(self):
        r"""
        :param JobName: Spark job name
        :type JobName: str
        :param CmdArgs: Command line parameters of the Spark job separated by space. They are generally used for periodic calls.
        :type CmdArgs: str
        """
        self.JobName = None
        self.CmdArgs = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        self.CmdArgs = params.get("CmdArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkAppTaskResponse(AbstractModel):
    """CreateSparkAppTask response structure.

    """

    def __init__(self):
        r"""
        :param BatchId: Batch ID
        :type BatchId: str
        :param TaskId: Task ID
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BatchId = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask request structure.

    """

    def __init__(self):
        r"""
        :param Task: Computing task. This parameter contains the task type and related configuration information.
        :type Task: :class:`tencentcloud.dlc.v20210125.models.Task`
        :param DatabaseName: Database name. If there is a database name in the SQL statement, the database in the SQL statement will be used first; otherwise, the database specified by this parameter will be used (note: when submitting the database creation SQL statement, passed in an empty string for this field).
        :type DatabaseName: str
        :param DatasourceConnectionName: Name of the default data source
        :type DatasourceConnectionName: str
        :param DataEngineName: Data engine name. If this parameter is not specified, the task will be submitted to the default engine.
        :type DataEngineName: str
        """
        self.Task = None
        self.DatabaseName = None
        self.DatasourceConnectionName = None
        self.DataEngineName = None


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self.Task = Task()
            self.Task._deserialize(params.get("Task"))
        self.DatabaseName = params.get("DatabaseName")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.DataEngineName = params.get("DataEngineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    """CreateTask response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateTasksRequest(AbstractModel):
    """CreateTasks request structure.

    """

    def __init__(self):
        r"""
        :param DatabaseName: Database name. If there is a database name in the SQL statement, the database in the SQL statement will be used first; otherwise, the database specified by this parameter will be used (note: when submitting the database creation SQL statement, passed in an empty string for this field).
        :type DatabaseName: str
        :param Tasks: SQL task information
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TasksInfo`
        :param DatasourceConnectionName: Data source name. Default value: DataLakeCatalog.
        :type DatasourceConnectionName: str
        :param DataEngineName: Compute engine name. If this parameter is not specified, the task will be submitted to the default engine.
        :type DataEngineName: str
        """
        self.DatabaseName = None
        self.Tasks = None
        self.DatasourceConnectionName = None
        self.DataEngineName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        if params.get("Tasks") is not None:
            self.Tasks = TasksInfo()
            self.Tasks._deserialize(params.get("Tasks"))
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.DataEngineName = params.get("DataEngineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTasksResponse(AbstractModel):
    """CreateTasks response structure.

    """

    def __init__(self):
        r"""
        :param BatchId: ID of the current batch of submitted tasks
        :type BatchId: str
        :param TaskIdSet: Collection of task IDs arranged in order of execution
        :type TaskIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BatchId = None
        self.TaskIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.TaskIdSet = params.get("TaskIdSet")
        self.RequestId = params.get("RequestId")


class CrontabResumeSuspendStrategy(AbstractModel):
    """Scheduled start and suspension information

    """

    def __init__(self):
        r"""
        :param ResumeTime: The scheduled start time, such as 8:00 AM every Monday.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResumeTime: str
        :param SuspendTime: The scheduled suspension time, such as 8:00 PM every Monday.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SuspendTime: str
        :param SuspendStrategy: The suspension setting. Valid values: `0` (suspension after task end, default) and `1` (force suspension).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SuspendStrategy: int
        """
        self.ResumeTime = None
        self.SuspendTime = None
        self.SuspendStrategy = None


    def _deserialize(self, params):
        self.ResumeTime = params.get("ResumeTime")
        self.SuspendTime = params.get("SuspendTime")
        self.SuspendStrategy = params.get("SuspendStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineConfigPair(AbstractModel):
    """Engine configurations

    """


class DataGovernPolicy(AbstractModel):
    """The data governance rules.

    """


class DeleteSparkAppRequest(AbstractModel):
    """DeleteSparkApp request structure.

    """

    def __init__(self):
        r"""
        :param AppName: Spark application name
        :type AppName: str
        """
        self.AppName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSparkAppResponse(AbstractModel):
    """DeleteSparkApp response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeEngineUsageInfoRequest(AbstractModel):
    """DescribeEngineUsageInfo request structure.

    """

    def __init__(self):
        r"""
        :param DataEngineId: The house ID.
        :type DataEngineId: str
        """
        self.DataEngineId = None


    def _deserialize(self, params):
        self.DataEngineId = params.get("DataEngineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEngineUsageInfoResponse(AbstractModel):
    """DescribeEngineUsageInfo response structure.

    """

    def __init__(self):
        r"""
        :param Total: The total cluster spec.
        :type Total: int
        :param Used: The used cluster spec.
        :type Used: int
        :param Available: The available cluster spec.
        :type Available: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Used = None
        self.Available = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        self.Available = params.get("Available")
        self.RequestId = params.get("RequestId")


class DescribeForbiddenTableProRequest(AbstractModel):
    """DescribeForbiddenTablePro request structure.

    """


class DescribeForbiddenTableProResponse(AbstractModel):
    """DescribeForbiddenTablePro response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeLakeFsDirSummaryRequest(AbstractModel):
    """DescribeLakeFsDirSummary request structure.

    """


class DescribeLakeFsDirSummaryResponse(AbstractModel):
    """DescribeLakeFsDirSummary response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeLakeFsInfoRequest(AbstractModel):
    """DescribeLakeFsInfo request structure.

    """


class DescribeLakeFsInfoResponse(AbstractModel):
    """DescribeLakeFsInfo response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeResultDownloadRequest(AbstractModel):
    """DescribeResultDownload request structure.

    """

    def __init__(self):
        r"""
        :param DownloadId: The query task ID.
        :type DownloadId: str
        """
        self.DownloadId = None


    def _deserialize(self, params):
        self.DownloadId = params.get("DownloadId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResultDownloadResponse(AbstractModel):
    """DescribeResultDownload response structure.

    """

    def __init__(self):
        r"""
        :param Path: The file save path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param Status: The task status. Valid values: `init`, `queue`, `format`, `compress`, `success`, `timeout`, and `error`.
        :type Status: str
        :param Reason: The task exception cause.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        :param SecretId: The temporary secret ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecretId: str
        :param SecretKey: The temporary secret key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param Token: The temporary token.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Token: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Path = None
        self.Status = None
        self.Reason = None
        self.SecretId = None
        self.SecretKey = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class DescribeSparkAppJobRequest(AbstractModel):
    """DescribeSparkAppJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Spark job ID. If it co-exists with `JobName`, `JobName` will become invalid.
        :type JobId: str
        :param JobName: Spark job name
        :type JobName: str
        """
        self.JobId = None
        self.JobName = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkAppJobResponse(AbstractModel):
    """DescribeSparkAppJob response structure.

    """

    def __init__(self):
        r"""
        :param Job: Spark job details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Job: :class:`tencentcloud.dlc.v20210125.models.SparkJobInfo`
        :param IsExists: Whether the queried Spark job exists
        :type IsExists: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Job = None
        self.IsExists = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = SparkJobInfo()
            self.Job._deserialize(params.get("Job"))
        self.IsExists = params.get("IsExists")
        self.RequestId = params.get("RequestId")


class DescribeSparkAppJobsRequest(AbstractModel):
    """DescribeSparkAppJobs request structure.

    """

    def __init__(self):
        r"""
        :param SortBy: The returned results are sorted by this field.
        :type SortBy: str
        :param Sorting: Descending or ascending order, such as `desc`.
        :type Sorting: str
        :param Filters: Filter by this parameter, which can be `spark-job-name`.
        :type Filters: list of Filter
        :param StartTime: Update start time
        :type StartTime: str
        :param EndTime: Update end time
        :type EndTime: str
        :param Offset: Query list offset
        :type Offset: int
        :param Limit: Query list limit
        :type Limit: int
        """
        self.SortBy = None
        self.Sorting = None
        self.Filters = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SortBy = params.get("SortBy")
        self.Sorting = params.get("Sorting")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
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
        


class DescribeSparkAppJobsResponse(AbstractModel):
    """DescribeSparkAppJobs response structure.

    """

    def __init__(self):
        r"""
        :param SparkAppJobs: Detailed list of Spark jobs
        :type SparkAppJobs: list of SparkJobInfo
        :param TotalCount: Total number of Spark jobs
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SparkAppJobs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SparkAppJobs") is not None:
            self.SparkAppJobs = []
            for item in params.get("SparkAppJobs"):
                obj = SparkJobInfo()
                obj._deserialize(item)
                self.SparkAppJobs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSparkAppTasksRequest(AbstractModel):
    """DescribeSparkAppTasks request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Spark job ID
        :type JobId: str
        :param Offset: Paginated query offset
        :type Offset: int
        :param Limit: Paginated query limit
        :type Limit: int
        :param TaskId: Execution instance ID
        :type TaskId: str
        :param StartTime: Update start time
        :type StartTime: str
        :param EndTime: Update end time
        :type EndTime: str
        :param Filters: Filter by this parameter, which can be `task-state`.
        :type Filters: list of Filter
        """
        self.JobId = None
        self.Offset = None
        self.Limit = None
        self.TaskId = None
        self.StartTime = None
        self.EndTime = None
        self.Filters = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TaskId = params.get("TaskId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkAppTasksResponse(AbstractModel):
    """DescribeSparkAppTasks response structure.

    """

    def __init__(self):
        r"""
        :param Tasks: Task result (this field has been disused)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TaskResponseInfo`
        :param TotalCount: Total number of tasks
        :type TotalCount: int
        :param SparkAppTasks: List of task results
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkAppTasks: list of TaskResponseInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Tasks = None
        self.TotalCount = None
        self.SparkAppTasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = TaskResponseInfo()
            self.Tasks._deserialize(params.get("Tasks"))
        self.TotalCount = params.get("TotalCount")
        if params.get("SparkAppTasks") is not None:
            self.SparkAppTasks = []
            for item in params.get("SparkAppTasks"):
                obj = TaskResponseInfo()
                obj._deserialize(item)
                self.SparkAppTasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Unique task ID
        :type TaskId: str
        :param NextToken: The pagination information returned by the last response. This parameter can be omitted for the first response, where the data will be returned from the beginning. The data with a volume set by the `MaxResults` field is returned each time.
        :type NextToken: str
        :param MaxResults: Maximum number of returned rows. Value range: 0–1,000. Default value: 1,000.
        :type MaxResults: int
        """
        self.TaskId = None
        self.NextToken = None
        self.MaxResults = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.NextToken = params.get("NextToken")
        self.MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult response structure.

    """

    def __init__(self):
        r"""
        :param TaskInfo: The queried task information. If the returned value is empty, the task with the entered task ID does not exist. The task result will be returned only if the task status is `2` (succeeded).
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskInfo: :class:`tencentcloud.dlc.v20210125.models.TaskResultInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self.TaskInfo = TaskResultInfo()
            self.TaskInfo._deserialize(params.get("TaskInfo"))
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of returned results. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter. The following filters are supported, and the `Name` input parameter must be one of them. Up to 50 `task-id` values can be filtered, while up to 5 other parameters can be filtered in total.
task-id - String - (filter by task ID). `task-id` format: e386471f-139a-4e59-877f-50ece8135b99.
task-state - String - (filter exactly by task status). Valid values: `0` (initial), `1` (running), `2` (succeeded), `-1` (failed).
task-sql-keyword - String - (filter fuzzily by SQL statement keyword, such as `DROP TABLE`).
task-operator- string (filter by sub-UIN)
task-kind - string (filter by task type)
        :type Filters: list of Filter
        :param SortBy: Sorting field. Valid values: `create-time` (default value), `update-time`.
        :type SortBy: str
        :param Sorting: Sorting order. Valid values: `asc` (ascending order), `desc` (descending order). Default value: `asc`.
        :type Sorting: str
        :param StartTime: Start time in the format of `yyyy-mm-dd HH:MM:SS`, which is the current time seven days ago by default.
        :type StartTime: str
        :param EndTime: End time in the format of `yyyy-mm-dd HH:MM:SS`, which is the current time by default. The time span is (0, 30] days. Data in the last 45 days can be queried.
        :type EndTime: str
        :param DataEngineName: Filter by compute resource name
        :type DataEngineName: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.SortBy = None
        self.Sorting = None
        self.StartTime = None
        self.EndTime = None
        self.DataEngineName = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortBy = params.get("SortBy")
        self.Sorting = params.get("Sorting")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DataEngineName = params.get("DataEngineName")
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
        :param TaskList: List of task objects.
        :type TaskList: list of TaskResponseInfo
        :param TotalCount: Total number of instances
        :type TotalCount: int
        :param TasksOverview: The task overview.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TasksOverview: :class:`tencentcloud.dlc.v20210125.models.TasksOverview`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskList = None
        self.TotalCount = None
        self.TasksOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskList") is not None:
            self.TaskList = []
            for item in params.get("TaskList"):
                obj = TaskResponseInfo()
                obj._deserialize(item)
                self.TaskList.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("TasksOverview") is not None:
            self.TasksOverview = TasksOverview()
            self.TasksOverview._deserialize(params.get("TasksOverview"))
        self.RequestId = params.get("RequestId")


class Execution(AbstractModel):
    """SQL statement objects

    """

    def __init__(self):
        r"""
        :param SQL: The automatically generated SQL statements.
        :type SQL: str
        """
        self.SQL = None


    def _deserialize(self, params):
        self.SQL = params.get("SQL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Query list filter parameter

    """

    def __init__(self):
        r"""
        :param Name: Attribute name. If more than one filter exists, the logical relationship between these filters is `OR`.
        :type Name: str
        :param Values: Attribute value. If multiple values exist in one filter, the logical relationship between these values is `OR`.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateCreateMangedTableSqlRequest(AbstractModel):
    """GenerateCreateMangedTableSql request structure.

    """

    def __init__(self):
        r"""
        :param TableBaseInfo: The basic table information.
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param Columns: The table fields.
        :type Columns: list of TColumn
        :param Partitions: The table partitions.
        :type Partitions: list of TPartition
        :param Properties: The table properties.
        :type Properties: list of Property
        """
        self.TableBaseInfo = None
        self.Columns = None
        self.Partitions = None
        self.Properties = None


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self.TableBaseInfo = TableBaseInfo()
            self.TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = TColumn()
                obj._deserialize(item)
                self.Columns.append(obj)
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = TPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self.Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateCreateMangedTableSqlResponse(AbstractModel):
    """GenerateCreateMangedTableSql response structure.

    """

    def __init__(self):
        r"""
        :param Execution: The SQL statements for creating the managed internal table.
        :type Execution: :class:`tencentcloud.dlc.v20210125.models.Execution`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Execution = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Execution") is not None:
            self.Execution = Execution()
            self.Execution._deserialize(params.get("Execution"))
        self.RequestId = params.get("RequestId")


class KVPair(AbstractModel):
    """Configuration format

    """

    def __init__(self):
        r"""
        :param Key: Configured key
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param Value: Configured value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGovernEventRuleRequest(AbstractModel):
    """ModifyGovernEventRule request structure.

    """


class ModifyGovernEventRuleResponse(AbstractModel):
    """ModifyGovernEventRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySparkAppRequest(AbstractModel):
    """ModifySparkApp request structure.

    """

    def __init__(self):
        r"""
        :param AppName: Spark application name
        :type AppName: str
        :param AppType: 1: Spark JAR application; 2: Spark streaming application
        :type AppType: int
        :param DataEngine: The data engine executing the Spark job
        :type DataEngine: str
        :param AppFile: Execution entry of the Spark application
        :type AppFile: str
        :param RoleArn: Execution role ID of the Spark job
        :type RoleArn: int
        :param AppDriverSize: Driver resource specification of the Spark job. Valid values: `small`, `medium`, `large`, `xlarge`.
        :type AppDriverSize: str
        :param AppExecutorSize: Executor resource specification of the Spark job. Valid values: `small`, `medium`, `large`, `xlarge`.
        :type AppExecutorSize: str
        :param AppExecutorNums: Number of Spark job executors
        :type AppExecutorNums: int
        :param SparkAppId: Spark application ID
        :type SparkAppId: str
        :param Eni: This field has been disused. Use the `Datasource` field instead.
        :type Eni: str
        :param IsLocal: Whether it is uploaded locally. Valid values: `cos`, `lakefs`.
        :type IsLocal: str
        :param MainClass: Main class of the Spark JAR job during execution
        :type MainClass: str
        :param AppConf: Spark configurations separated by line break
        :type AppConf: str
        :param IsLocalJars: JAR resource dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalJars: str
        :param AppJars: Dependency JAR packages of the Spark JAR job separated by comma
        :type AppJars: str
        :param IsLocalFiles: File resource dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalFiles: str
        :param AppFiles: Dependency resources of the Spark job separated by comma
        :type AppFiles: str
        :param IsLocalPythonFiles: PySpark: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalPythonFiles: str
        :param AppPythonFiles: PySpark: Python dependency, which can be in .py, .zip, or .egg format. Multiple files should be separated by comma.
        :type AppPythonFiles: str
        :param CmdArgs: Command line parameters of the Spark job
        :type CmdArgs: str
        :param MaxRetries: This parameter takes effect only for Spark flow tasks.
        :type MaxRetries: int
        :param DataSource: Data source name
        :type DataSource: str
        :param IsLocalArchives: Archives: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalArchives: str
        :param AppArchives: Archives: Dependency resources
        :type AppArchives: str
        :param SparkImage: The Spark image version.
        :type SparkImage: str
        :param SparkImageVersion: The Spark image version name.
        :type SparkImageVersion: str
        :param AppExecutorMaxNumbers: The specified executor count (max), which defaults to 1. This parameter applies if the "Dynamic" mode is selected. If the "Dynamic" mode is not selected, the executor count is equal to `AppExecutorNums`.
        :type AppExecutorMaxNumbers: int
        """
        self.AppName = None
        self.AppType = None
        self.DataEngine = None
        self.AppFile = None
        self.RoleArn = None
        self.AppDriverSize = None
        self.AppExecutorSize = None
        self.AppExecutorNums = None
        self.SparkAppId = None
        self.Eni = None
        self.IsLocal = None
        self.MainClass = None
        self.AppConf = None
        self.IsLocalJars = None
        self.AppJars = None
        self.IsLocalFiles = None
        self.AppFiles = None
        self.IsLocalPythonFiles = None
        self.AppPythonFiles = None
        self.CmdArgs = None
        self.MaxRetries = None
        self.DataSource = None
        self.IsLocalArchives = None
        self.AppArchives = None
        self.SparkImage = None
        self.SparkImageVersion = None
        self.AppExecutorMaxNumbers = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.AppType = params.get("AppType")
        self.DataEngine = params.get("DataEngine")
        self.AppFile = params.get("AppFile")
        self.RoleArn = params.get("RoleArn")
        self.AppDriverSize = params.get("AppDriverSize")
        self.AppExecutorSize = params.get("AppExecutorSize")
        self.AppExecutorNums = params.get("AppExecutorNums")
        self.SparkAppId = params.get("SparkAppId")
        self.Eni = params.get("Eni")
        self.IsLocal = params.get("IsLocal")
        self.MainClass = params.get("MainClass")
        self.AppConf = params.get("AppConf")
        self.IsLocalJars = params.get("IsLocalJars")
        self.AppJars = params.get("AppJars")
        self.IsLocalFiles = params.get("IsLocalFiles")
        self.AppFiles = params.get("AppFiles")
        self.IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self.AppPythonFiles = params.get("AppPythonFiles")
        self.CmdArgs = params.get("CmdArgs")
        self.MaxRetries = params.get("MaxRetries")
        self.DataSource = params.get("DataSource")
        self.IsLocalArchives = params.get("IsLocalArchives")
        self.AppArchives = params.get("AppArchives")
        self.SparkImage = params.get("SparkImage")
        self.SparkImageVersion = params.get("SparkImageVersion")
        self.AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySparkAppResponse(AbstractModel):
    """ModifySparkApp response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Policy(AbstractModel):
    """Permission objects

    """

    def __init__(self):
        r"""
        :param Database: The name of the target database. `*` represents all databases in the current catalog. To grant admin permissions, it must be `*`; to grant data connection permissions, it must be null; to grant other permissions, it can be any database.
        :type Database: str
        :param Catalog: The name of the target data source. To grant admin permission, it must be `*` (all resources at this level); to grant data source and database permissions, it must be `COSDataCatalog` or `*`; to grant table permissions, it can be a custom data source; if it is left empty, `DataLakeCatalog` is used. Note: To grant permissions on a custom data source, the permissions that can be managed in the Data Lake Compute console are subsets of the account permissions granted when you connect the data source to the console.
        :type Catalog: str
        :param Table: The name of the target table. `*` represents all tables in the current database. To grant admin permissions, it must be `*`; to grant data connection and database permissions, it must be null; to grant other permissions, it can be any table.
        :type Table: str
        :param Operation: The target permissions, which vary by permission level. Admin: `ALL` (default); data connection: `CREATE`; database: `ALL`, `CREATE`, `ALTER`, and `DROP`; table: `ALL`, `SELECT`, `INSERT`, `ALTER`, `DELETE`, `DROP`, and `UPDATE`. Note: For table permissions, if a data source other than `COSDataCatalog` is specified, only the `SELECT` permission can be granted here.
        :type Operation: str
        :param PolicyType: The permission type. Valid values: `ADMIN`, `DATASOURCE`, `DATABASE`, `TABLE`, `VIEW`, `FUNCTION`, `COLUMN`, and `ENGINE`. Note: If it is left empty, `ADMIN` is used.
        :type PolicyType: str
        :param Function: The name of the target function. `*` represents all functions in the current catalog. To grant admin permissions, it must be `*`; to grant data connection permissions, it must be null; to grant other permissions, it can be any function.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Function: str
        :param View: The name of the target view. `*` represents all views in the current database. To grant admin permissions, it must be `*`; to grant data connection and database permissions, it must be null; to grant other permissions, it can be any view.
Note: This field may return null, indicating that no valid values can be obtained.
        :type View: str
        :param Column: The name of the target column. `*` represents all columns. To grant admin permissions, it must be `*`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Column: str
        :param DataEngine: The name of the target data engine. `*` represents all engines. To grant admin permissions, it must be `*`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngine: str
        :param ReAuth: Whether the grantee is allowed to further grant the permissions. Valid values: `false` (default) and `true` (the grantee can grant permissions gained here to other sub-users).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReAuth: bool
        :param Source: The permission source, which is not required when input parameters are passed in. Valid values: `USER` (from the user) and `WORKGROUP` (from one or more associated work groups).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Source: str
        :param Mode: The grant mode, which is not required as an input parameter. Valid values: `COMMON` and `SENIOR`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mode: str
        :param Operator: The operator, which is not required as an input parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operator: str
        :param CreateTime: The permission policy creation time, which is not required as an input parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param SourceId: The ID of the work group, which applies only when the value of the `Source` field is `WORKGROUP`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceId: int
        :param SourceName: The name of the work group, which applies only when the value of the `Source` field is `WORKGROUP`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceName: str
        :param Id: The policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        """
        self.Database = None
        self.Catalog = None
        self.Table = None
        self.Operation = None
        self.PolicyType = None
        self.Function = None
        self.View = None
        self.Column = None
        self.DataEngine = None
        self.ReAuth = None
        self.Source = None
        self.Mode = None
        self.Operator = None
        self.CreateTime = None
        self.SourceId = None
        self.SourceName = None
        self.Id = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Catalog = params.get("Catalog")
        self.Table = params.get("Table")
        self.Operation = params.get("Operation")
        self.PolicyType = params.get("PolicyType")
        self.Function = params.get("Function")
        self.View = params.get("View")
        self.Column = params.get("Column")
        self.DataEngine = params.get("DataEngine")
        self.ReAuth = params.get("ReAuth")
        self.Source = params.get("Source")
        self.Mode = params.get("Mode")
        self.Operator = params.get("Operator")
        self.CreateTime = params.get("CreateTime")
        self.SourceId = params.get("SourceId")
        self.SourceName = params.get("SourceName")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Property(AbstractModel):
    """Properties of database and table

    """

    def __init__(self):
        r"""
        :param Key: The property key name.
        :type Key: str
        :param Value: The property value.
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLTask(AbstractModel):
    """SQL query task

    """

    def __init__(self):
        r"""
        :param SQL: Base64-encrypted SQL statement
        :type SQL: str
        :param Config: Task configuration information
        :type Config: list of KVPair
        """
        self.SQL = None
        self.Config = None


    def _deserialize(self, params):
        self.SQL = params.get("SQL")
        if params.get("Config") is not None:
            self.Config = []
            for item in params.get("Config"):
                obj = KVPair()
                obj._deserialize(item)
                self.Config.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkJobInfo(AbstractModel):
    """Spark job details

    """

    def __init__(self):
        r"""
        :param JobId: Spark job ID
        :type JobId: str
        :param JobName: Spark job name
        :type JobName: str
        :param JobType: Spark job type. Valid values: `1` (batch job), `2` (streaming job).
        :type JobType: int
        :param DataEngine: Engine name
        :type DataEngine: str
        :param Eni: This field has been disused. Use the `Datasource` field instead.
        :type Eni: str
        :param IsLocal: Whether the program package is uploaded locally. Valid values: `cos`, `lakefs`.
        :type IsLocal: str
        :param JobFile: Program package path
        :type JobFile: str
        :param RoleArn: Role ID
        :type RoleArn: int
        :param MainClass: Main class of Spark job execution
        :type MainClass: str
        :param CmdArgs: Command line parameters of the Spark job separated by space
        :type CmdArgs: str
        :param JobConf: Native Spark configurations separated by line break
        :type JobConf: str
        :param IsLocalJars: Whether the dependency JAR packages are uploaded locally. Valid values: `cos`, `lakefs`.
        :type IsLocalJars: str
        :param JobJars: Dependency JAR packages of the Spark job separated by comma
        :type JobJars: str
        :param IsLocalFiles: Whether the dependency file is uploaded locally. Valid values: `cos`, `lakefs`.
        :type IsLocalFiles: str
        :param JobFiles: Dependency files of the Spark job separated by comma
        :type JobFiles: str
        :param JobDriverSize: Driver resource size of the Spark job
        :type JobDriverSize: str
        :param JobExecutorSize: Executor resource size of the Spark job
        :type JobExecutorSize: str
        :param JobExecutorNums: Number of Spark job executors
        :type JobExecutorNums: int
        :param JobMaxAttempts: Maximum number of retries of the Spark flow task
        :type JobMaxAttempts: int
        :param JobCreator: Spark job creator
        :type JobCreator: str
        :param JobCreateTime: Spark job creation time
        :type JobCreateTime: int
        :param JobUpdateTime: Spark job update time
        :type JobUpdateTime: int
        :param CurrentTaskId: Last task ID of the Spark job
        :type CurrentTaskId: str
        :param JobStatus: Last status of the Spark job
        :type JobStatus: int
        :param StreamingStat: Spark streaming job statistics
Note: This field may return null, indicating that no valid values can be obtained.
        :type StreamingStat: :class:`tencentcloud.dlc.v20210125.models.StreamingStatistics`
        :param DataSource: Data source name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        :param IsLocalPythonFiles: PySpark: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsLocalPythonFiles: str
        :param AppPythonFiles: Note: This returned value has been disused.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppPythonFiles: str
        :param IsLocalArchives: Archives: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsLocalArchives: str
        :param JobArchives: Archives: Dependency resources
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobArchives: str
        :param SparkImage: The Spark image version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkImage: str
        :param JobPythonFiles: PySpark: Python dependency, which can be in .py, .zip, or .egg format. Multiple files should be separated by comma.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobPythonFiles: str
        :param TaskNum: Number of tasks running or ready to run under the current job
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskNum: int
        :param DataEngineStatus: Engine status. -100 (default value): unknown; -2–11: normal.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngineStatus: int
        :param JobExecutorMaxNumbers: The specified executor count (max), which defaults to 1. This parameter applies if the "Dynamic" mode is selected. If the "Dynamic" mode is not selected, the executor count is equal to `JobExecutorNums`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobExecutorMaxNumbers: int
        :param SparkImageVersion: The image version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkImageVersion: str
        """
        self.JobId = None
        self.JobName = None
        self.JobType = None
        self.DataEngine = None
        self.Eni = None
        self.IsLocal = None
        self.JobFile = None
        self.RoleArn = None
        self.MainClass = None
        self.CmdArgs = None
        self.JobConf = None
        self.IsLocalJars = None
        self.JobJars = None
        self.IsLocalFiles = None
        self.JobFiles = None
        self.JobDriverSize = None
        self.JobExecutorSize = None
        self.JobExecutorNums = None
        self.JobMaxAttempts = None
        self.JobCreator = None
        self.JobCreateTime = None
        self.JobUpdateTime = None
        self.CurrentTaskId = None
        self.JobStatus = None
        self.StreamingStat = None
        self.DataSource = None
        self.IsLocalPythonFiles = None
        self.AppPythonFiles = None
        self.IsLocalArchives = None
        self.JobArchives = None
        self.SparkImage = None
        self.JobPythonFiles = None
        self.TaskNum = None
        self.DataEngineStatus = None
        self.JobExecutorMaxNumbers = None
        self.SparkImageVersion = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.JobType = params.get("JobType")
        self.DataEngine = params.get("DataEngine")
        self.Eni = params.get("Eni")
        self.IsLocal = params.get("IsLocal")
        self.JobFile = params.get("JobFile")
        self.RoleArn = params.get("RoleArn")
        self.MainClass = params.get("MainClass")
        self.CmdArgs = params.get("CmdArgs")
        self.JobConf = params.get("JobConf")
        self.IsLocalJars = params.get("IsLocalJars")
        self.JobJars = params.get("JobJars")
        self.IsLocalFiles = params.get("IsLocalFiles")
        self.JobFiles = params.get("JobFiles")
        self.JobDriverSize = params.get("JobDriverSize")
        self.JobExecutorSize = params.get("JobExecutorSize")
        self.JobExecutorNums = params.get("JobExecutorNums")
        self.JobMaxAttempts = params.get("JobMaxAttempts")
        self.JobCreator = params.get("JobCreator")
        self.JobCreateTime = params.get("JobCreateTime")
        self.JobUpdateTime = params.get("JobUpdateTime")
        self.CurrentTaskId = params.get("CurrentTaskId")
        self.JobStatus = params.get("JobStatus")
        if params.get("StreamingStat") is not None:
            self.StreamingStat = StreamingStatistics()
            self.StreamingStat._deserialize(params.get("StreamingStat"))
        self.DataSource = params.get("DataSource")
        self.IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self.AppPythonFiles = params.get("AppPythonFiles")
        self.IsLocalArchives = params.get("IsLocalArchives")
        self.JobArchives = params.get("JobArchives")
        self.SparkImage = params.get("SparkImage")
        self.JobPythonFiles = params.get("JobPythonFiles")
        self.TaskNum = params.get("TaskNum")
        self.DataEngineStatus = params.get("DataEngineStatus")
        self.JobExecutorMaxNumbers = params.get("JobExecutorMaxNumbers")
        self.SparkImageVersion = params.get("SparkImageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamingStatistics(AbstractModel):
    """Statistics of the Spark flow task

    """

    def __init__(self):
        r"""
        :param StartTime: Task start time
        :type StartTime: str
        :param Receivers: Number of data receivers
        :type Receivers: int
        :param NumActiveReceivers: Number of receivers in service
        :type NumActiveReceivers: int
        :param NumInactiveReceivers: Number of inactive receivers
        :type NumInactiveReceivers: int
        :param NumActiveBatches: Number of running batches
        :type NumActiveBatches: int
        :param NumRetainedCompletedBatches: Number of batches to be processed
        :type NumRetainedCompletedBatches: int
        :param NumTotalCompletedBatches: Number of completed batches
        :type NumTotalCompletedBatches: int
        :param AverageInputRate: Average input speed
        :type AverageInputRate: float
        :param AverageSchedulingDelay: Average queue time
        :type AverageSchedulingDelay: float
        :param AverageProcessingTime: Average processing time
        :type AverageProcessingTime: float
        :param AverageTotalDelay: Average latency
        :type AverageTotalDelay: float
        """
        self.StartTime = None
        self.Receivers = None
        self.NumActiveReceivers = None
        self.NumInactiveReceivers = None
        self.NumActiveBatches = None
        self.NumRetainedCompletedBatches = None
        self.NumTotalCompletedBatches = None
        self.AverageInputRate = None
        self.AverageSchedulingDelay = None
        self.AverageProcessingTime = None
        self.AverageTotalDelay = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Receivers = params.get("Receivers")
        self.NumActiveReceivers = params.get("NumActiveReceivers")
        self.NumInactiveReceivers = params.get("NumInactiveReceivers")
        self.NumActiveBatches = params.get("NumActiveBatches")
        self.NumRetainedCompletedBatches = params.get("NumRetainedCompletedBatches")
        self.NumTotalCompletedBatches = params.get("NumTotalCompletedBatches")
        self.AverageInputRate = params.get("AverageInputRate")
        self.AverageSchedulingDelay = params.get("AverageSchedulingDelay")
        self.AverageProcessingTime = params.get("AverageProcessingTime")
        self.AverageTotalDelay = params.get("AverageTotalDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendResumeDataEngineRequest(AbstractModel):
    """SuspendResumeDataEngine request structure.

    """

    def __init__(self):
        r"""
        :param DataEngineName: The name of a virtual cluster.
        :type DataEngineName: str
        :param Operate: The operation type: `suspend` or `resume`.
        :type Operate: str
        """
        self.DataEngineName = None
        self.Operate = None


    def _deserialize(self, params):
        self.DataEngineName = params.get("DataEngineName")
        self.Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendResumeDataEngineResponse(AbstractModel):
    """SuspendResumeDataEngine response structure.

    """

    def __init__(self):
        r"""
        :param DataEngineName: The details of the virtual cluster.
        :type DataEngineName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataEngineName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataEngineName = params.get("DataEngineName")
        self.RequestId = params.get("RequestId")


class SwitchDataEngineRequest(AbstractModel):
    """SwitchDataEngine request structure.

    """

    def __init__(self):
        r"""
        :param DataEngineName: The name of the primary cluster.
        :type DataEngineName: str
        :param StartStandbyCluster: Whether to start the standby cluster.
        :type StartStandbyCluster: bool
        """
        self.DataEngineName = None
        self.StartStandbyCluster = None


    def _deserialize(self, params):
        self.DataEngineName = params.get("DataEngineName")
        self.StartStandbyCluster = params.get("StartStandbyCluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDataEngineResponse(AbstractModel):
    """SwitchDataEngine response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TColumn(AbstractModel):
    """Table field information

    """

    def __init__(self):
        r"""
        :param Name: The field name.
        :type Name: str
        :param Type: The field type.
        :type Type: str
        :param Comment: The field description.
        :type Comment: str
        :param Default: The default field value.
        :type Default: str
        :param NotNull: Whether the field is not null.
        :type NotNull: bool
        """
        self.Name = None
        self.Type = None
        self.Comment = None
        self.Default = None
        self.NotNull = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        self.Default = params.get("Default")
        self.NotNull = params.get("NotNull")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TPartition(AbstractModel):
    """Table partition information

    """

    def __init__(self):
        r"""
        :param Name: The field name.
        :type Name: str
        :param Type: The field type.
        :type Type: str
        :param Comment: The field description.
        :type Comment: str
        :param PartitionType: The partition type.
        :type PartitionType: str
        :param PartitionFormat: The partition format.
        :type PartitionFormat: str
        :param PartitionDot: The separator count of the partition conversion policy.
        :type PartitionDot: int
        :param Transform: The partition conversion policy.
        :type Transform: str
        :param TransformArgs: The policy parameters.
        :type TransformArgs: list of str
        """
        self.Name = None
        self.Type = None
        self.Comment = None
        self.PartitionType = None
        self.PartitionFormat = None
        self.PartitionDot = None
        self.Transform = None
        self.TransformArgs = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        self.PartitionType = params.get("PartitionType")
        self.PartitionFormat = params.get("PartitionFormat")
        self.PartitionDot = params.get("PartitionDot")
        self.Transform = params.get("Transform")
        self.TransformArgs = params.get("TransformArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableBaseInfo(AbstractModel):
    """Table configurations

    """

    def __init__(self):
        r"""
        :param DatabaseName: The database name.
        :type DatabaseName: str
        :param TableName: The table name.
        :type TableName: str
        :param DatasourceConnectionName: The data source name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatasourceConnectionName: str
        :param TableComment: The table remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableComment: str
        :param Type: The specific type: `table` or `view`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param TableFormat: The data format type, such as `hive` and `iceberg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableFormat: str
        :param UserAlias: The table creator name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserAlias: str
        :param UserSubUin: The table creator ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserSubUin: str
        :param GovernPolicy: The data governance configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GovernPolicy: :class:`tencentcloud.dlc.v20210125.models.DataGovernPolicy`
        """
        self.DatabaseName = None
        self.TableName = None
        self.DatasourceConnectionName = None
        self.TableComment = None
        self.Type = None
        self.TableFormat = None
        self.UserAlias = None
        self.UserSubUin = None
        self.GovernPolicy = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.TableName = params.get("TableName")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.TableComment = params.get("TableComment")
        self.Type = params.get("Type")
        self.TableFormat = params.get("TableFormat")
        self.UserAlias = params.get("UserAlias")
        self.UserSubUin = params.get("UserSubUin")
        if params.get("GovernPolicy") is not None:
            self.GovernPolicy = DataGovernPolicy()
            self.GovernPolicy._deserialize(params.get("GovernPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Tag pair info

    """

    def __init__(self):
        r"""
        :param TagKey: The tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: The tag value.
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class Task(AbstractModel):
    """Task type, such as SQL query.

    """

    def __init__(self):
        r"""
        :param SQLTask: SQL query task
        :type SQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`
        :param SparkSQLTask: Spark SQL query task
        :type SparkSQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`
        """
        self.SQLTask = None
        self.SparkSQLTask = None


    def _deserialize(self, params):
        if params.get("SQLTask") is not None:
            self.SQLTask = SQLTask()
            self.SQLTask._deserialize(params.get("SQLTask"))
        if params.get("SparkSQLTask") is not None:
            self.SparkSQLTask = SQLTask()
            self.SparkSQLTask._deserialize(params.get("SparkSQLTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResponseInfo(AbstractModel):
    """The task instance.

    """

    def __init__(self):
        r"""
        :param DatabaseName: Database name of the task
        :type DatabaseName: str
        :param DataAmount: Data volume of the task
        :type DataAmount: int
        :param Id: Task ID
        :type Id: str
        :param UsedTime: The compute time in ms.
        :type UsedTime: int
        :param OutputPath: Task output path
        :type OutputPath: str
        :param CreateTime: Task creation time
        :type CreateTime: str
        :param State: Task status. Valid values: `0` (initial), `1` (executing), `2` (executed successfully), `-1` (failed to execute), `-3` (canceled).
        :type State: int
        :param SQLType: SQL statement type of the task, such as DDL and DML.
        :type SQLType: str
        :param SQL: SQL statement of the task
        :type SQL: str
        :param ResultExpired: Whether the result has expired
        :type ResultExpired: bool
        :param RowAffectInfo: Number of affected data rows
        :type RowAffectInfo: str
        :param DataSet: Dataset of task results
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataSet: str
        :param Error: Failure information, such as `errorMessage`. This field has been disused.
        :type Error: str
        :param Percentage: Task progress (%)
        :type Percentage: int
        :param OutputMessage: Output information of task execution
        :type OutputMessage: str
        :param TaskType: Type of the engine executing the SQL statement
        :type TaskType: str
        :param ProgressDetail: Task progress details
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProgressDetail: str
        :param UpdateTime: Task end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param DataEngineId: Compute resource ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngineId: str
        :param OperateUin: Sub-UIN that executes the SQL statement
Note: This field may return null, indicating that no valid values can be obtained.
        :type OperateUin: str
        :param DataEngineName: Compute resource name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngineName: str
        :param InputType: Whether the import type is local import or COS
Note: This field may return null, indicating that no valid values can be obtained.
        :type InputType: str
        :param InputConf: Import configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type InputConf: str
        :param DataNumber: Number of data entries
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataNumber: int
        :param CanDownload: Whether the data can be downloaded
Note: This field may return null, indicating that no valid values can be obtained.
        :type CanDownload: bool
        :param UserAlias: User alias
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserAlias: str
        :param SparkJobName: Spark application job name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkJobName: str
        :param SparkJobId: Spark application job ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkJobId: str
        :param SparkJobFile: JAR file of the Spark application entry
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkJobFile: str
        :param UiUrl: Spark UI URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type UiUrl: str
        :param TotalTime: The task time in ms.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalTime: int
        :param CmdArgs: The program entry parameter for running a task under a Spark job.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CmdArgs: str
        """
        self.DatabaseName = None
        self.DataAmount = None
        self.Id = None
        self.UsedTime = None
        self.OutputPath = None
        self.CreateTime = None
        self.State = None
        self.SQLType = None
        self.SQL = None
        self.ResultExpired = None
        self.RowAffectInfo = None
        self.DataSet = None
        self.Error = None
        self.Percentage = None
        self.OutputMessage = None
        self.TaskType = None
        self.ProgressDetail = None
        self.UpdateTime = None
        self.DataEngineId = None
        self.OperateUin = None
        self.DataEngineName = None
        self.InputType = None
        self.InputConf = None
        self.DataNumber = None
        self.CanDownload = None
        self.UserAlias = None
        self.SparkJobName = None
        self.SparkJobId = None
        self.SparkJobFile = None
        self.UiUrl = None
        self.TotalTime = None
        self.CmdArgs = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.DataAmount = params.get("DataAmount")
        self.Id = params.get("Id")
        self.UsedTime = params.get("UsedTime")
        self.OutputPath = params.get("OutputPath")
        self.CreateTime = params.get("CreateTime")
        self.State = params.get("State")
        self.SQLType = params.get("SQLType")
        self.SQL = params.get("SQL")
        self.ResultExpired = params.get("ResultExpired")
        self.RowAffectInfo = params.get("RowAffectInfo")
        self.DataSet = params.get("DataSet")
        self.Error = params.get("Error")
        self.Percentage = params.get("Percentage")
        self.OutputMessage = params.get("OutputMessage")
        self.TaskType = params.get("TaskType")
        self.ProgressDetail = params.get("ProgressDetail")
        self.UpdateTime = params.get("UpdateTime")
        self.DataEngineId = params.get("DataEngineId")
        self.OperateUin = params.get("OperateUin")
        self.DataEngineName = params.get("DataEngineName")
        self.InputType = params.get("InputType")
        self.InputConf = params.get("InputConf")
        self.DataNumber = params.get("DataNumber")
        self.CanDownload = params.get("CanDownload")
        self.UserAlias = params.get("UserAlias")
        self.SparkJobName = params.get("SparkJobName")
        self.SparkJobId = params.get("SparkJobId")
        self.SparkJobFile = params.get("SparkJobFile")
        self.UiUrl = params.get("UiUrl")
        self.TotalTime = params.get("TotalTime")
        self.CmdArgs = params.get("CmdArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResultInfo(AbstractModel):
    """The task result information.

    """

    def __init__(self):
        r"""
        :param TaskId: Unique task ID
        :type TaskId: str
        :param DatasourceConnectionName: Name of the default selected data source when the current job is executed
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatasourceConnectionName: str
        :param DatabaseName: Name of the default selected database when the current job is executed
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param SQL: The currently executed SQL statement. Each task contains one SQL statement.
        :type SQL: str
        :param SQLType: Type of the executed task. Valid values: `DDL`, `DML`, `DQL`.
        :type SQLType: str
        :param State: Current status of the task. `0`: initial; `1`: task running; `2`: task execution succeeded; `-1`: task execution failed; `-3`: task terminated manually by the user. The task execution result will be returned only if task execution succeeds.
        :type State: int
        :param DataAmount: Amount of the data scanned in bytes
        :type DataAmount: int
        :param UsedTime: The compute time in ms.
        :type UsedTime: int
        :param OutputPath: Address of the COS bucket for storing the task result
        :type OutputPath: str
        :param CreateTime: Task creation timestamp
        :type CreateTime: str
        :param OutputMessage: Task execution information. `success` will be returned if the task succeeds; otherwise, the failure cause will be returned.
        :type OutputMessage: str
        :param RowAffectInfo: Number of affected rows
        :type RowAffectInfo: str
        :param ResultSchema: Schema information of the result
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultSchema: list of Column
        :param ResultSet: Result information. After it is unescaped, each element of the outer array is a data row.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultSet: str
        :param NextToken: Pagination information. If there is no more result data, `nextToken` will be empty.
        :type NextToken: str
        :param Percentage: Task progress (%)
        :type Percentage: int
        :param ProgressDetail: Task progress details
        :type ProgressDetail: str
        :param DisplayFormat: Console display format. Valid values: `table`, `text`.
        :type DisplayFormat: str
        :param TotalTime: The task time in ms.
        :type TotalTime: int
        """
        self.TaskId = None
        self.DatasourceConnectionName = None
        self.DatabaseName = None
        self.SQL = None
        self.SQLType = None
        self.State = None
        self.DataAmount = None
        self.UsedTime = None
        self.OutputPath = None
        self.CreateTime = None
        self.OutputMessage = None
        self.RowAffectInfo = None
        self.ResultSchema = None
        self.ResultSet = None
        self.NextToken = None
        self.Percentage = None
        self.ProgressDetail = None
        self.DisplayFormat = None
        self.TotalTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.DatabaseName = params.get("DatabaseName")
        self.SQL = params.get("SQL")
        self.SQLType = params.get("SQLType")
        self.State = params.get("State")
        self.DataAmount = params.get("DataAmount")
        self.UsedTime = params.get("UsedTime")
        self.OutputPath = params.get("OutputPath")
        self.CreateTime = params.get("CreateTime")
        self.OutputMessage = params.get("OutputMessage")
        self.RowAffectInfo = params.get("RowAffectInfo")
        if params.get("ResultSchema") is not None:
            self.ResultSchema = []
            for item in params.get("ResultSchema"):
                obj = Column()
                obj._deserialize(item)
                self.ResultSchema.append(obj)
        self.ResultSet = params.get("ResultSet")
        self.NextToken = params.get("NextToken")
        self.Percentage = params.get("Percentage")
        self.ProgressDetail = params.get("ProgressDetail")
        self.DisplayFormat = params.get("DisplayFormat")
        self.TotalTime = params.get("TotalTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TasksInfo(AbstractModel):
    """Collection of tasks executed sequentially in batches

    """

    def __init__(self):
        r"""
        :param TaskType: Task type. Valid values: `SQLTask` (SQL query task), `SparkSQLTask` (Spark SQL query task).
        :type TaskType: str
        :param FailureTolerance: Fault tolerance policy. `Proceed`: continues to execute subsequent tasks after the current task fails or is canceled. `Terminate`: terminates the execution of subsequent tasks after the current task fails or is canceled, and marks all subsequent tasks as canceled.
        :type FailureTolerance: str
        :param SQL: Base64-encrypted SQL statements separated by ";". Up to 50 tasks can be submitted at a time, and they will be executed strictly in sequence.
        :type SQL: str
        :param Config: Configuration information of the task. Currently, only `SparkSQLTask` tasks are supported.
        :type Config: list of KVPair
        :param Params: User-defined parameters of the task
        :type Params: list of KVPair
        """
        self.TaskType = None
        self.FailureTolerance = None
        self.SQL = None
        self.Config = None
        self.Params = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.FailureTolerance = params.get("FailureTolerance")
        self.SQL = params.get("SQL")
        if params.get("Config") is not None:
            self.Config = []
            for item in params.get("Config"):
                obj = KVPair()
                obj._deserialize(item)
                self.Config.append(obj)
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self.Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TasksOverview(AbstractModel):
    """The task overview.

    """

    def __init__(self):
        r"""
        :param TaskQueuedCount: The number of tasks in queue.
        :type TaskQueuedCount: int
        :param TaskInitCount: The number of initialized tasks.
        :type TaskInitCount: int
        :param TaskRunningCount: The number of tasks in progress.
        :type TaskRunningCount: int
        :param TotalTaskCount: The total number of tasks in this time range.
        :type TotalTaskCount: int
        """
        self.TaskQueuedCount = None
        self.TaskInitCount = None
        self.TaskRunningCount = None
        self.TotalTaskCount = None


    def _deserialize(self, params):
        self.TaskQueuedCount = params.get("TaskQueuedCount")
        self.TaskInitCount = params.get("TaskInitCount")
        self.TaskRunningCount = params.get("TaskRunningCount")
        self.TotalTaskCount = params.get("TotalTaskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRowFilterRequest(AbstractModel):
    """UpdateRowFilter request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: The ID of the row filter policy, which can be obtained using the `DescribeUserInfo` or `DescribeWorkGroupInfo` API.
        :type PolicyId: int
        :param Policy: The new filter policy.
        :type Policy: :class:`tencentcloud.dlc.v20210125.models.Policy`
        """
        self.PolicyId = None
        self.Policy = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        if params.get("Policy") is not None:
            self.Policy = Policy()
            self.Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRowFilterResponse(AbstractModel):
    """UpdateRowFilter response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")