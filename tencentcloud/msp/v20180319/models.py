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


class DeregisterMigrationTaskRequest(AbstractModel):
    """DeregisterMigrationTask request structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterMigrationTaskResponse(AbstractModel):
    """DeregisterMigrationTask response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeMigrationTaskRequest(AbstractModel):
    """DescribeMigrationTask request structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID, such as msp-jitoh33n\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationTaskResponse(AbstractModel):
    """DescribeMigrationTask response structure.

    """

    def __init__(self):
        """
        :param TaskStatus: Migration details list\n        :type TaskStatus: list of TaskStatus\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Region: Migration destination region\n        :type Region: str\n        :param Ip: \n        :type Ip: str\n        :param Port: Migration destination port\n        :type Port: str\n        :param InstanceId: Migration destination instance ID\n        :type InstanceId: str\n        """
        self.Region = None
        self.Ip = None
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationProjectRequest(AbstractModel):
    """ListMigrationProject request structure.

    """

    def __init__(self):
        """
        :param Offset: The initial number of records, default value: 0\n        :type Offset: int\n        :param Limit: The number of records returned, default value: 500\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationProjectResponse(AbstractModel):
    """ListMigrationProject response structure.

    """

    def __init__(self):
        """
        :param Projects: Project list\n        :type Projects: list of Project\n        :param TotalCount: Total number of projects\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Offset: The initial number of records, default value: 0\n        :type Offset: int\n        :param Limit: Number of records, default value: 10\n        :type Limit: int\n        :param ProjectId: Project ID, the default value is empty.\n        :type ProjectId: int\n        """
        self.Offset = None
        self.Limit = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationTaskResponse(AbstractModel):
    """ListMigrationTask response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records\n        :type TotalCount: int\n        :param Tasks: Migration task list\n        :type Tasks: list of Task\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TaskId: Task ID, such as msp-jitoh33n\n        :type TaskId: str\n        :param ProjectId: Project ID, such as 10005\n        :type ProjectId: int\n        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationTaskBelongToProjectResponse(AbstractModel):
    """ModifyMigrationTaskBelongToProject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrationTaskStatusRequest(AbstractModel):
    """ModifyMigrationTaskStatus request structure.

    """

    def __init__(self):
        """
        :param Status: Task status, valid values include `unstart` (migration has not started), `migrating` (migration in progress), `finish` (migration completed) or `fail` (migration failed).\n        :type Status: str\n        :param TaskId: Task ID, such as msp-jitoh33n\n        :type TaskId: str\n        """
        self.Status = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationTaskStatusResponse(AbstractModel):
    """ModifyMigrationTaskStatus response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Project(AbstractModel):
    """List type

    """

    def __init__(self):
        """
        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param ProjectName: Project name\n        :type ProjectName: str\n        """
        self.ProjectId = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterMigrationTaskRequest(AbstractModel):
    """RegisterMigrationTask request structure.

    """

    def __init__(self):
        """
        :param TaskType: Task type, valid values include `database` (database migration), `file` (file migration) or `host` (host migration).\n        :type TaskType: str\n        :param TaskName: Task name\n        :type TaskName: str\n        :param ServiceSupplier: Service supplier name\n        :type ServiceSupplier: str\n        :param CreateTime: Migration task creation time\n        :type CreateTime: str\n        :param UpdateTime: Migration task update time\n        :type UpdateTime: str\n        :param MigrateClass: Migration type, for example `mysql:mysql` in database migration means migration from mysql to mysql and `oss:cos` in file migration means migration from Alibaba Cloud OSS to Tencent COS.\n        :type MigrateClass: str\n        :param SrcInfo: Migration task source information\n        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`\n        :param DstInfo: Migration task destination information\n        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`\n        :param SrcAccessType: Source instance access type. Valid values for database migration include `extranet` (public network), `cvm` (CVM-created instance), `dcg` (Direct Connect-enabled instance), `vpncloud` (Tencent Cloud VPN-enabled instance), `vpnselfbuild` (self-built VPN-enabled instance), `cdb` (TencentDB instance)\n        :type SrcAccessType: str\n        :param SrcDatabaseType: Database type of the source instance. Valid values for database migration: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`\n        :type SrcDatabaseType: str\n        :param DstAccessType: Target instance access type. Valid values for database migration include `extranet` (public network), `cvm` (CVM-created instance), `dcg` (Direct Connect-enabled instance), `vpncloud` (Tencent Cloud VPN-enabled instance), `vpnselfbuild` (self-built VPN-enabled instance), `cdb` (TencentDB instance)\n        :type DstAccessType: str\n        :param DstDatabaseType: Database type of the target instance. Valid values for database migration: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`\n        :type DstDatabaseType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterMigrationTaskResponse(AbstractModel):
    """RegisterMigrationTask response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Region: Migration source region\n        :type Region: str\n        :param Ip: \n        :type Ip: str\n        :param Port: Migration source port\n        :type Port: str\n        :param InstanceId: Migration source instance ID\n        :type InstanceId: str\n        """
        self.Region = None
        self.Ip = None
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """Migration task type

    """

    def __init__(self):
        """
        :param TaskId: Task ID\n        :type TaskId: str\n        :param TaskName: Task name\n        :type TaskName: str\n        :param MigrationType: Migration type\n        :type MigrationType: str\n        :param Status: Migration status\n        :type Status: str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param ProjectName: Project name\n        :type ProjectName: str\n        :param SrcInfo: Migration source information\n        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`\n        :param MigrationTimeLine: Migration time information\n        :type MigrationTimeLine: :class:`tencentcloud.msp.v20180319.models.TimeObj`\n        :param Updated: Status update time\n        :type Updated: str\n        :param DstInfo: Migration destination information\n        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatus(AbstractModel):
    """Migration details list

    """

    def __init__(self):
        """
        :param Status: Migration status\n        :type Status: str\n        :param Progress: Migration progress\n        :type Progress: str\n        :param UpdateTime: Migration date\n        :type UpdateTime: str\n        """
        self.Status = None
        self.Progress = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeObj(AbstractModel):
    """Time object

    """

    def __init__(self):
        """
        :param CreateTime: The creation time\n        :type CreateTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        """
        self.CreateTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        