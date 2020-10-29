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


class DeregisterMigrationTaskRequest(AbstractModel):
    """DeregisterMigrationTask request structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DeregisterMigrationTaskResponse(AbstractModel):
    """DeregisterMigrationTask response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeMigrationTaskRequest(AbstractModel):
    """DescribeMigrationTask request structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID, such as msp-jitoh33n
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeMigrationTaskResponse(AbstractModel):
    """DescribeMigrationTask response structure.

    """

    def __init__(self):
        """
        :param TaskStatus: Migration details list
        :type TaskStatus: list of TaskStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskStatus") is not None:
            self.TaskStatus = []
            for item in params.get("TaskStatus"):
                obj = TaskStatus()
                obj._deserialize(item)
                self.TaskStatus.append(obj)
        self.RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """Migration destination information

    """

    def __init__(self):
        """
        :param Region: Migration destination region
        :type Region: str
        :param Ip: 
        :type Ip: str
        :param Port: Migration destination port
        :type Port: str
        :param InstanceId: Migration destination instance ID
        :type InstanceId: str
        """
        self.Region = None
        self.Ip = None
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")


class ListMigrationProjectRequest(AbstractModel):
    """ListMigrationProject request structure.

    """

    def __init__(self):
        """
        :param Offset: The initial number of records, default value: 0
        :type Offset: int
        :param Limit: The number of records returned, default value: 500
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class ListMigrationProjectResponse(AbstractModel):
    """ListMigrationProject response structure.

    """

    def __init__(self):
        """
        :param Projects: Project list
        :type Projects: list of Project
        :param TotalCount: Total number of projects
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Projects = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListMigrationTaskRequest(AbstractModel):
    """ListMigrationTask request structure.

    """

    def __init__(self):
        """
        :param Offset: The initial number of records, default value: 0
        :type Offset: int
        :param Limit: Number of records, default value: 10
        :type Limit: int
        :param ProjectId: Project ID, the default value is empty.
        :type ProjectId: int
        """
        self.Offset = None
        self.Limit = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")


class ListMigrationTaskResponse(AbstractModel):
    """ListMigrationTask response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records
        :type TotalCount: int
        :param Tasks: Migration task list
        :type Tasks: list of Task
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
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyMigrationTaskBelongToProjectRequest(AbstractModel):
    """ModifyMigrationTaskBelongToProject request structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID, such as msp-jitoh33n
        :type TaskId: str
        :param ProjectId: Project ID, such as 10005
        :type ProjectId: int
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")


class ModifyMigrationTaskBelongToProjectResponse(AbstractModel):
    """ModifyMigrationTaskBelongToProject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrationTaskStatusRequest(AbstractModel):
    """ModifyMigrationTaskStatus request structure.

    """

    def __init__(self):
        """
        :param Status: Task status, valid values include `unstart` (migration has not started), `migrating` (migration in progress), `finish` (migration completed) or `fail` (migration failed).
        :type Status: str
        :param TaskId: Task ID, such as msp-jitoh33n
        :type TaskId: str
        """
        self.Status = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")


class ModifyMigrationTaskStatusResponse(AbstractModel):
    """ModifyMigrationTaskStatus response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Project(AbstractModel):
    """List type

    """

    def __init__(self):
        """
        :param ProjectId: Project ID
        :type ProjectId: int
        :param ProjectName: Project name
        :type ProjectName: str
        """
        self.ProjectId = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")


class RegisterMigrationTaskRequest(AbstractModel):
    """RegisterMigrationTask request structure.

    """

    def __init__(self):
        """
        :param TaskType: Task type, valid values include `database` (database migration), `file` (file migration) or `host` (host migration).
        :type TaskType: str
        :param TaskName: Task name
        :type TaskName: str
        :param ServiceSupplier: Service supplier name
        :type ServiceSupplier: str
        :param CreateTime: Migration task creation time
        :type CreateTime: str
        :param UpdateTime: Migration task update time
        :type UpdateTime: str
        :param MigrateClass: Migration type, for example `mysql:mysql` in database migration means migration from mysql to mysql and `oss:cos` in file migration means migration from Alibaba Cloud OSS to Tencent COS.
        :type MigrateClass: str
        :param SrcInfo: Migration task source information
        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`
        :param DstInfo: Migration task destination information
        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`
        :param SrcAccessType: Source instance access type. Valid values for database migration include `extranet` (public network), `cvm` (CVM-created instance), `dcg` (Direct Connect-enabled instance), `vpncloud` (Tencent Cloud VPN-enabled instance), `vpnselfbuild` (self-built VPN-enabled instance), `cdb` (TencentDB instance)
        :type SrcAccessType: str
        :param SrcDatabaseType: Database type of the source instance. Valid values for database migration: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`
        :type SrcDatabaseType: str
        :param DstAccessType: Target instance access type. Valid values for database migration include `extranet` (public network), `cvm` (CVM-created instance), `dcg` (Direct Connect-enabled instance), `vpncloud` (Tencent Cloud VPN-enabled instance), `vpnselfbuild` (self-built VPN-enabled instance), `cdb` (TencentDB instance)
        :type DstAccessType: str
        :param DstDatabaseType: Database type of the target instance. Valid values for database migration: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`
        :type DstDatabaseType: str
        """
        self.TaskType = None
        self.TaskName = None
        self.ServiceSupplier = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MigrateClass = None
        self.SrcInfo = None
        self.DstInfo = None
        self.SrcAccessType = None
        self.SrcDatabaseType = None
        self.DstAccessType = None
        self.DstDatabaseType = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.TaskName = params.get("TaskName")
        self.ServiceSupplier = params.get("ServiceSupplier")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MigrateClass = params.get("MigrateClass")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.SrcAccessType = params.get("SrcAccessType")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        self.DstDatabaseType = params.get("DstDatabaseType")


class RegisterMigrationTaskResponse(AbstractModel):
    """RegisterMigrationTask response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SrcInfo(AbstractModel):
    """Migration source information

    """

    def __init__(self):
        """
        :param Region: Migration source region
        :type Region: str
        :param Ip: 
        :type Ip: str
        :param Port: Migration source port
        :type Port: str
        :param InstanceId: Migration source instance ID
        :type InstanceId: str
        """
        self.Region = None
        self.Ip = None
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")


class Task(AbstractModel):
    """Migration task type

    """

    def __init__(self):
        """
        :param TaskId: Task ID
        :type TaskId: str
        :param TaskName: Task name
        :type TaskName: str
        :param MigrationType: Migration type
        :type MigrationType: str
        :param Status: Migration status
        :type Status: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param ProjectName: Project name
        :type ProjectName: str
        :param SrcInfo: Migration source information
        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`
        :param MigrationTimeLine: Migration time information
        :type MigrationTimeLine: :class:`tencentcloud.msp.v20180319.models.TimeObj`
        :param Updated: Status update time
        :type Updated: str
        :param DstInfo: Migration destination information
        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`
        """
        self.TaskId = None
        self.TaskName = None
        self.MigrationType = None
        self.Status = None
        self.ProjectId = None
        self.ProjectName = None
        self.SrcInfo = None
        self.MigrationTimeLine = None
        self.Updated = None
        self.DstInfo = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.MigrationType = params.get("MigrationType")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("MigrationTimeLine") is not None:
            self.MigrationTimeLine = TimeObj()
            self.MigrationTimeLine._deserialize(params.get("MigrationTimeLine"))
        self.Updated = params.get("Updated")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))


class TaskStatus(AbstractModel):
    """Migration details list

    """

    def __init__(self):
        """
        :param Status: Migration status
        :type Status: str
        :param Progress: Migration progress
        :type Progress: str
        :param UpdateTime: Migration date
        :type UpdateTime: str
        """
        self.Status = None
        self.Progress = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.UpdateTime = params.get("UpdateTime")


class TimeObj(AbstractModel):
    """Time object

    """

    def __init__(self):
        """
        :param CreateTime: The creation time
        :type CreateTime: str
        :param EndTime: End time
        :type EndTime: str
        """
        self.CreateTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")