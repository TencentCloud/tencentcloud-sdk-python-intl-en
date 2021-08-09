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


class ActivateSubscribeRequest(AbstractModel):
    """ActivateSubscribe request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Subscription instance ID.\n        :type SubscribeId: str\n        :param InstanceId: Database Instance ID\n        :type InstanceId: str\n        :param SubscribeObjectType: Data subscription type. 0: full instance subscription, 1: data subscription, 2: structure subscription, 3: data subscription and structure subscription\n        :type SubscribeObjectType: int\n        :param Objects: Subscription object\n        :type Objects: :class:`tencentcloud.dts.v20180330.models.SubscribeObject`\n        :param UniqSubnetId: Subnet of data subscription service, which is the subnet of the database instance by default.\n        :type UniqSubnetId: str\n        :param Vport: Subscription service port. Default value: 7507\n        :type Vport: int\n        """
        self.SubscribeId = None
        self.InstanceId = None
        self.SubscribeObjectType = None
        self.Objects = None
        self.UniqSubnetId = None
        self.Vport = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.InstanceId = params.get("InstanceId")
        self.SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self.Objects = SubscribeObject()
            self.Objects._deserialize(params.get("Objects"))
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateSubscribeResponse(AbstractModel):
    """ActivateSubscribe response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Data subscription configuration task ID.\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID\n        :type JobId: str\n        :param CompleteMode: The way to complete the task, which is supported only for legacy MySQL migration task. waitForSync: wait for the source-replica lag to become 0 before stopping; immediately: complete immediately without waiting for source-replica sync. Default value: waitForSync\n        :type CompleteMode: str\n        """
        self.JobId = None
        self.CompleteMode = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompleteMode = params.get("CompleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConsistencyParams(AbstractModel):
    """Sampling parameter for spot check

    """

    def __init__(self):
        """
        :param SelectRowsPerTable: Data content check parameter, which refers to the proportion of the rows selected for data comparison in all the rows of the table. Value: an integer between 1 and 100.\n        :type SelectRowsPerTable: int\n        :param TablesSelectAll: Data content check parameter, which refers to the proportion of the tables selected for data detection in all the tables. Value: an integer between 1 and 100.\n        :type TablesSelectAll: int\n        :param TablesSelectCount: Data quantity check parameter, which checks whether the numbers of rows are identical. It refers to the proportion of the tables selected for quantity check in all the tables. Value: an integer between 1 and 100.\n        :type TablesSelectCount: int\n        """
        self.SelectRowsPerTable = None
        self.TablesSelectAll = None
        self.TablesSelectCount = None


    def _deserialize(self, params):
        self.SelectRowsPerTable = params.get("SelectRowsPerTable")
        self.TablesSelectAll = params.get("TablesSelectAll")
        self.TablesSelectCount = params.get("TablesSelectCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMigrateJobRequest(AbstractModel):
    """CreateMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobName: Data migration task name\n        :type JobName: str\n        :param MigrateOption: Migration task configuration options\n        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`\n        :param SrcDatabaseType: Source instance database type, which currently supports MySQL, Redis, MongoDB, PostgreSQL, MariaDB, and Percona. For more information on the supported types in a specific region, see the migration task creation page in the console.\n        :type SrcDatabaseType: str\n        :param SrcAccessType: Source instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance), ccn (CCN instance)\n        :type SrcAccessType: str\n        :param SrcInfo: Source instance information, which is correlated with the migration task type\n        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`\n        :param DstDatabaseType: Target instance access type, which currently supports MySQL, Redis, MongoDB, PostgreSQL, MariaDB, and Percona. For more information on the supported types in a specific region, see the migration task creation page in the console.\n        :type DstDatabaseType: str\n        :param DstAccessType: Target instance access type, which currently only supports cdb (TencentDB instance)\n        :type DstAccessType: str\n        :param DstInfo: Destination instance information\n        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`\n        :param DatabaseInfo: Information of the source table to be migrated, which is described in JSON string format. It is required if MigrateOption.MigrateObject is 2 (migrating the specified table).
For databases with a database-table structure:
[{Database:db1,Table:[table1,table2]},{Database:db2}]
For databases with a database-schema-table structure:
[{Database:db1,Schema:s1
Table:[table1,table2]},{Database:db1,Schema:s2
Table:[table1,table2]},{Database:db2,Schema:s1
Table:[table1,table2]},{Database:db3},{Database:db4
Schema:s1}]\n        :type DatabaseInfo: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateJobResponse(AbstractModel):
    """CreateMigrateJob response structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID\n        :type JobId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe request structure.

    """

    def __init__(self):
        """
        :param Product: Subscribed database type. Currently, MySQL is supported\n        :type Product: str\n        :param PayType: Instance billing mode, which is always 1 (hourly billing),\n        :type PayType: int\n        :param Duration: Purchase duration in months, which is required if `PayType` is 0. Maximum value: 120 (this field is not required of global site users and is better to be hidden)\n        :type Duration: int\n        :param Count: Quantity. Default value: 1. Maximum value: 10\n        :type Count: int\n        :param AutoRenew: Whether to auto-renew. Default value: 0. This flag does not take effect for hourly billed instances (this field should be hidden from global site users)\n        :type AutoRenew: int\n        :param Tags: Instance resource tags\n        :type Tags: list of TagItem\n        """
        self.Product = None
        self.PayType = None
        self.Duration = None
        self.Count = None
        self.AutoRenew = None
        self.Tags = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.PayType = params.get("PayType")
        self.Duration = params.get("Duration")
        self.Count = params.get("Count")
        self.AutoRenew = params.get("AutoRenew")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe response structure.

    """

    def __init__(self):
        """
        :param SubscribeIds: Data subscription instance ID array
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubscribeIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SubscribeIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscribeIds = params.get("SubscribeIds")
        self.RequestId = params.get("RequestId")


class CreateSyncCheckJobRequest(AbstractModel):
    """CreateSyncCheckJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Disaster recovery sync task ID\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSyncCheckJobResponse(AbstractModel):
    """CreateSyncCheckJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSyncJobRequest(AbstractModel):
    """CreateSyncJob request structure.

    """

    def __init__(self):
        """
        :param JobName: Disaster recovery sync task name\n        :type JobName: str\n        :param SyncOption: Configuration options of a disaster recovery sync task\n        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`\n        :param SrcDatabaseType: Source instance database type, which currently only supports mysql\n        :type SrcDatabaseType: str\n        :param SrcAccessType: Source instance access type, which currently only supports cdb (TencentDB instances)\n        :type SrcAccessType: str\n        :param SrcInfo: Source instance information\n        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`\n        :param DstDatabaseType: Target instance access type, which currently only supports mysql\n        :type DstDatabaseType: str\n        :param DstAccessType: Target instance access type, which currently only supports cdb (TencentDB instances)\n        :type DstAccessType: str\n        :param DstInfo: Target instance information\n        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`\n        :param DatabaseInfo: Information of the source table to be synced, which is described in JSON string format.
For databases with a database-table structure:
[{Database:db1,Table:[table1,table2]},{Database:db2}]\n        :type DatabaseInfo: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSyncJobResponse(AbstractModel):
    """CreateSyncJob response structure.

    """

    def __init__(self):
        """
        :param JobId: Disaster recovery sync task ID\n        :type JobId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param JobId: Data migration task ID\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMigrateJobResponse(AbstractModel):
    """DeleteMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSyncJobRequest(AbstractModel):
    """DeleteSyncJob request structure.

    """

    def __init__(self):
        """
        :param JobId: ID of the disaster recovery sync task to be deleted\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSyncJobResponse(AbstractModel):
    """DeleteSyncJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Task ID\n        :type AsyncRequestId: str\n        """
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
        """
        :param Info: Task execution result information\n        :type Info: str\n        :param Status: Task execution status. Valid values: success, failed, running\n        :type Status: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Info = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Info = params.get("Info")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeMigrateCheckJobRequest(AbstractModel):
    """DescribeMigrateCheckJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateCheckJobResponse(AbstractModel):
    """DescribeMigrateCheckJob response structure.

    """

    def __init__(self):
        """
        :param Status: Check task status: unavailable, starting, running, finished\n        :type Status: str\n        :param ErrorCode: Task error code\n        :type ErrorCode: int\n        :param ErrorMessage: Task error message\n        :type ErrorMessage: str\n        :param Progress: Check task progress. For example, "30" means 30% completed\n        :type Progress: str\n        :param CheckFlag: Whether the check succeeds. 0: no; 1: yes; 3: not checked\n        :type CheckFlag: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param JobId: Data migration task ID\n        :type JobId: str\n        :param JobName: Data migration task name\n        :type JobName: str\n        :param Order: Sort by field. Value range: JobId, Status, JobName, MigrateType, RunMode, CreateTime\n        :type Order: str\n        :param OrderSeq: Sorting order. Value range: ASC (ascending), DESC (descending)\n        :type OrderSeq: str\n        :param Offset: Offset. Default value: 0\n        :type Offset: int\n        :param Limit: Number of the returned instances. Value range: [1, 100]. Default value: 20\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateJobsResponse(AbstractModel):
    """DescribeMigrateJobs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of tasks\n        :type TotalCount: int\n        :param JobList: Array of task details\n        :type JobList: list of MigrateJobInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeRegionConfRequest(AbstractModel):
    """DescribeRegionConf request structure.

    """


class DescribeRegionConfResponse(AbstractModel):
    """DescribeRegionConf response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of purchasable regions\n        :type TotalCount: int\n        :param Items: Purchasable region details\n        :type Items: list of SubscribeRegionConf\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SubscribeRegionConf()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubscribeConfRequest(AbstractModel):
    """DescribeSubscribeConf request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Subscription instance ID\n        :type SubscribeId: str\n        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeConfResponse(AbstractModel):
    """DescribeSubscribeConf response structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Subscription instance ID\n        :type SubscribeId: str\n        :param SubscribeName: Subscription instance name\n        :type SubscribeName: str\n        :param ChannelId: Subscription channel\n        :type ChannelId: str\n        :param Product: Subscribed database type\n        :type Product: str\n        :param InstanceId: Subscribed instance\n        :type InstanceId: str\n        :param InstanceStatus: Subscribed instance status. Valid values: running, offline, isolate\n        :type InstanceStatus: str\n        :param SubsStatus: Subscription instance status. Valid values: unconfigure, configuring, configured\n        :type SubsStatus: str\n        :param Status: Subscription instance lifecycle status. Valid values: normal, isolating, isolated, offlining\n        :type Status: str\n        :param CreateTime: Subscription instance creation time\n        :type CreateTime: str\n        :param IsolateTime: Subscription instance isolation time\n        :type IsolateTime: str\n        :param ExpireTime: Subscription instance expiration time\n        :type ExpireTime: str\n        :param OfflineTime: Subscription instance deactivation time\n        :type OfflineTime: str\n        :param ConsumeStartTime: Consumption starting time point of subscription instance\n        :type ConsumeStartTime: str\n        :param PayType: Subscription instance billing mode. 1: hourly billing\n        :type PayType: int\n        :param Vip: Subscription channel VIP\n        :type Vip: str\n        :param Vport: Subscription channel port\n        :type Vport: int\n        :param UniqVpcId: Subscription channel `VpcId`\n        :type UniqVpcId: str\n        :param UniqSubnetId: Subscription channel `SubnetId`\n        :type UniqSubnetId: str\n        :param SdkConsumedTime: Current SDK consumption time point\n        :type SdkConsumedTime: str\n        :param SdkHost: Subscription SDK IP address\n        :type SdkHost: str\n        :param SubscribeObjectType: Subscription object type. 0: full instance subscription, 1: DDL data subscription, 2: DML structure subscription, 3: DDL data subscription + DML structure subscription\n        :type SubscribeObjectType: int\n        :param SubscribeObjects: Subscription object, which is an empty array if `SubscribeObjectType` is 0\n        :type SubscribeObjects: list of SubscribeObject\n        :param ModifyTime: Modification time\n        :type ModifyTime: str\n        :param Region: Region\n        :type Region: str\n        :param Tags: Tags of the subscription
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Tags: list of TagItem\n        :param AutoRenewFlag: Whether auto-renewal is enabled. 0: do not enable, 1: enable
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AutoRenewFlag: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SubscribeId = None
        self.SubscribeName = None
        self.ChannelId = None
        self.Product = None
        self.InstanceId = None
        self.InstanceStatus = None
        self.SubsStatus = None
        self.Status = None
        self.CreateTime = None
        self.IsolateTime = None
        self.ExpireTime = None
        self.OfflineTime = None
        self.ConsumeStartTime = None
        self.PayType = None
        self.Vip = None
        self.Vport = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.SdkConsumedTime = None
        self.SdkHost = None
        self.SubscribeObjectType = None
        self.SubscribeObjects = None
        self.ModifyTime = None
        self.Region = None
        self.Tags = None
        self.AutoRenewFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        self.ChannelId = params.get("ChannelId")
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.SubsStatus = params.get("SubsStatus")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.IsolateTime = params.get("IsolateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.OfflineTime = params.get("OfflineTime")
        self.ConsumeStartTime = params.get("ConsumeStartTime")
        self.PayType = params.get("PayType")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.SdkConsumedTime = params.get("SdkConsumedTime")
        self.SdkHost = params.get("SdkHost")
        self.SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("SubscribeObjects") is not None:
            self.SubscribeObjects = []
            for item in params.get("SubscribeObjects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self.SubscribeObjects.append(obj)
        self.ModifyTime = params.get("ModifyTime")
        self.Region = params.get("Region")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.RequestId = params.get("RequestId")


class DescribeSubscribesRequest(AbstractModel):
    """DescribeSubscribes request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID\n        :type SubscribeId: str\n        :param SubscribeName: Data subscription instance name\n        :type SubscribeName: str\n        :param InstanceId: ID of bound database instance\n        :type InstanceId: str\n        :param ChannelId: Data subscription instance channel ID\n        :type ChannelId: str\n        :param PayType: Billing mode filter. Default value: 1 (pay-as-you-go)\n        :type PayType: str\n        :param Product: Subscribed database product, such as MySQL\n        :type Product: str\n        :param Status: Data subscription instance status. Valid values: creating, normal, isolating, isolated, offlining\n        :type Status: list of str\n        :param SubsStatus: Data subscription instance configuration status. Valid values: unconfigure, configuring, configured\n        :type SubsStatus: list of str\n        :param Offset: Starting offset of returned results\n        :type Offset: int\n        :param Limit: Number of results to be returned at a time\n        :type Limit: int\n        :param OrderDirection: Sorting order. Valid values: DESC, ASC. Default value: DESC, indicating descending by creation time\n        :type OrderDirection: str\n        :param TagFilters: Tag filtering condition\n        :type TagFilters: list of TagFilter\n        :param SubscribeVersion: Subscription instance edition. `txdts`: legacy data subscription; `kafka`: data subscription in Kafka edition\n        :type SubscribeVersion: str\n        """
        self.SubscribeId = None
        self.SubscribeName = None
        self.InstanceId = None
        self.ChannelId = None
        self.PayType = None
        self.Product = None
        self.Status = None
        self.SubsStatus = None
        self.Offset = None
        self.Limit = None
        self.OrderDirection = None
        self.TagFilters = None
        self.SubscribeVersion = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        self.InstanceId = params.get("InstanceId")
        self.ChannelId = params.get("ChannelId")
        self.PayType = params.get("PayType")
        self.Product = params.get("Product")
        self.Status = params.get("Status")
        self.SubsStatus = params.get("SubsStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderDirection = params.get("OrderDirection")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.SubscribeVersion = params.get("SubscribeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribesResponse(AbstractModel):
    """DescribeSubscribes response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param Items: Information list of data subscription instances\n        :type Items: list of SubscribeInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SubscribeInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSyncCheckJobRequest(AbstractModel):
    """DescribeSyncCheckJob request structure.

    """

    def __init__(self):
        """
        :param JobId: ID of the disaster recovery sync task to be queried\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSyncCheckJobResponse(AbstractModel):
    """DescribeSyncCheckJob response structure.

    """

    def __init__(self):
        """
        :param Status: Task check status: starting, running, finished\n        :type Status: str\n        :param ErrorCode: Code of the task check result\n        :type ErrorCode: int\n        :param ErrorMessage: Prompt message\n        :type ErrorMessage: str\n        :param StepInfo: Description of a task execution step\n        :type StepInfo: list of SyncCheckStepInfo\n        :param CheckFlag: Check flag. 0: checking; 1: successfully checked\n        :type CheckFlag: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param JobId: Disaster recovery sync task ID\n        :type JobId: str\n        :param JobName: Disaster recovery sync task name\n        :type JobName: str\n        :param Order: Sort by field. Value range: JobId, Status, JobName, CreateTime\n        :type Order: str\n        :param OrderSeq: Sorting order. Value range: ASC (ascending), DESC (descending)\n        :type OrderSeq: str\n        :param Offset: Offset. Default value: 0\n        :type Offset: int\n        :param Limit: Number of the returned instances. Value range: [1, 100]. Default value: 20\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSyncJobsResponse(AbstractModel):
    """DescribeSyncJobs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of tasks\n        :type TotalCount: int\n        :param JobList: Array of task details\n        :type JobList: list of SyncJobInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Target instance ID, such as cdb-jd92ijd8\n        :type InstanceId: str\n        :param Region: Target instance region, such as ap-guangzhou\n        :type Region: str\n        :param Ip: Target instance VIP, which has been disused and does not need to be entered\n        :type Ip: str\n        :param Port: Target instance Vport, which has been disused and does not need to be entered\n        :type Port: int\n        :param ReadOnly: Only valid for MySQL currently. For instance-level migration, the value range is: 1 (read-only), 0 (read/write)\n        :type ReadOnly: int\n        :param User: Target database account\n        :type User: str\n        :param Password: Target database password\n        :type Password: str\n        """
        self.InstanceId = None
        self.Region = None
        self.Ip = None
        self.Port = None
        self.ReadOnly = None
        self.User = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.ReadOnly = params.get("ReadOnly")
        self.User = params.get("User")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfo(AbstractModel):
    """Message and prompt for migration task error

    """

    def __init__(self):
        """
        :param ErrorLog: Specific error log, including error code and error message\n        :type ErrorLog: str\n        :param HelpDoc: Help document URL corresponding to error\n        :type HelpDoc: str\n        """
        self.ErrorLog = None
        self.HelpDoc = None


    def _deserialize(self, params):
        self.ErrorLog = params.get("ErrorLog")
        self.HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSubscribeRequest(AbstractModel):
    """IsolateSubscribe request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Subscription instance ID\n        :type SubscribeId: str\n        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSubscribeResponse(AbstractModel):
    """IsolateSubscribe response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MigrateDetailInfo(AbstractModel):
    """Describes the specific migration process

    """

    def __init__(self):
        """
        :param StepAll: Total number of steps\n        :type StepAll: int\n        :param StepNow: Current step\n        :type StepNow: int\n        :param Progress: Overall progress, such as "10"\n        :type Progress: str\n        :param CurrentStepProgress: Progress of current step, such as "1"\n        :type CurrentStepProgress: str\n        :param MasterSlaveDistance: Master/slave lag in MB, which is valid during incremental sync and currently supported by TencentDB for Redis and MySQL\n        :type MasterSlaveDistance: int\n        :param SecondsBehindMaster: Master/slave lag in seconds, which is valid during incremental sync and currently supported by TencentDB for MySQL\n        :type SecondsBehindMaster: int\n        :param StepInfo: Step information\n        :type StepInfo: list of MigrateStepDetailInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateJobInfo(AbstractModel):
    """Migration task details

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID\n        :type JobId: str\n        :param JobName: Data migration task name\n        :type JobName: str\n        :param MigrateOption: Migration task configuration options\n        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`\n        :param SrcDatabaseType: Source instance database type: MySQL, Redis, MongoDB, PostgreSQL, MariaDB, Percona\n        :type SrcDatabaseType: str\n        :param SrcAccessType: Source instance access type. Value range: extranet (public network), cvm (CVM-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance), ccn (CCN instances)\n        :type SrcAccessType: str\n        :param SrcInfo: Source instance information, which is correlated with the migration task type\n        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`\n        :param DstDatabaseType: Target instance access type: MySQL, Redis, MongoDB, PostgreSQL, MariaDB, Percona\n        :type DstDatabaseType: str\n        :param DstAccessType: Target instance access type, which currently only supports cdb (TencentDB instance)\n        :type DstAccessType: str\n        :param DstInfo: Target instance information\n        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`\n        :param DatabaseInfo: Information of the source table to be migrated. If the entire instance is to be migrated, this field should be []\n        :type DatabaseInfo: str\n        :param CreateTime: Task creation/submission time\n        :type CreateTime: str\n        :param StartTime: Task start time\n        :type StartTime: str\n        :param EndTime: Task end time\n        :type EndTime: str\n        :param Status: Task status. Value range: 1 (Creating), 3 (Checking), 4 (CheckPass), 5 (CheckNotPass), 7 (Running), 8 (ReadyComplete), 9 (Success), 10 (Failed), 11 (Stopping), 12 (Completing)\n        :type Status: int\n        :param Detail: Task details\n        :type Detail: :class:`tencentcloud.dts.v20180330.models.MigrateDetailInfo`\n        :param ErrorInfo: Prompt message for task error, which is not null or empty when an error occurs with the task\n        :type ErrorInfo: list of ErrorInfo\n        """
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
        self.ErrorInfo = None


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
        if params.get("ErrorInfo") is not None:
            self.ErrorInfo = []
            for item in params.get("ErrorInfo"):
                obj = ErrorInfo()
                obj._deserialize(item)
                self.ErrorInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOption(AbstractModel):
    """Migration task configuration options

    """

    def __init__(self):
        """
        :param RunMode: Task operation mode. Value range: 1 (immediate execution), 2 (scheduled execution)\n        :type RunMode: int\n        :param ExpectTime: Expected execution time in the format of yyyy-mm-dd hh:mm:ss. If runMode=2, this field is required\n        :type ExpectTime: str\n        :param MigrateType: Data migration type. Value range: 1 (structural migration), 2 (full migration), 3 (full + incremental migration)\n        :type MigrateType: int\n        :param MigrateObject: Migration subject. 1: entire instance; 2: specified table\n        :type MigrateObject: int\n        :param ConsistencyType: Parameter of spot data consistency check. 1: not configured; 2: full check; 3: spot check; 4: check inconsistent tables only; 5: no check\n        :type ConsistencyType: int\n        :param IsOverrideRoot: Whether to overwrite the target database with the root account of the source database. Value range: 0 (no), 1 (yes). This value should be 0 for table or structural migration\n        :type IsOverrideRoot: int\n        :param ExternParams: Additional parameters for different databases, which are described in JSON format. 
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
MySQL currently does not support configuring additional parameters.\n        :type ExternParams: str\n        :param ConsistencyParams: Only used for "spot data consistency check". It is required if ConsistencyType is spot check\n        :type ConsistencyParams: :class:`tencentcloud.dts.v20180330.models.ConsistencyParams`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateStepDetailInfo(AbstractModel):
    """Information of steps in migration

    """

    def __init__(self):
        """
        :param StepNo: Step number\n        :type StepNo: int\n        :param StepName: Step name\n        :type StepName: str\n        :param StepId: Step ID\n        :type StepId: str\n        :param Status: Step status. Value range: 0 (default), 1 (succeeded), 2 (failed), 3 (in progress), 4 (not started)\n        :type Status: int\n        :param StartTime: Start time of current step in the format of `yyyy-mm-dd hh:mm:ss`. This field is meaningless if it does not exist or is empty
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StartTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobRequest(AbstractModel):
    """ModifyMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: ID of the data migration task to be modified\n        :type JobId: str\n        :param JobName: Data migration task name\n        :type JobName: str\n        :param MigrateOption: Migration task configuration options\n        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`\n        :param SrcAccessType: Source instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance)\n        :type SrcAccessType: str\n        :param SrcInfo: Source instance information, which is correlated with the migration task type\n        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`\n        :param DstAccessType: Target instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance). Currently, only `cdb` is supported\n        :type DstAccessType: str\n        :param DstInfo: Target instance information. The region where the target instance is located cannot be modified.\n        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`\n        :param DatabaseInfo: When migrating the specified table, you need to set the information of the source database table to be migrated, which should be described in JSON string format. Below are examples.

For databases with a database-table structure:
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
For databases with a database-schema-table structure:
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]

This field does not need to be set when the entire instance is to be migrated\n        :type DatabaseInfo: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobResponse(AbstractModel):
    """ModifyMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscribeConsumeTimeRequest(AbstractModel):
    """ModifySubscribeConsumeTime request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID\n        :type SubscribeId: str\n        :param ConsumeStartTime: Consumption starting time point in the format of `Y-m-d h:m:s`, i.e., the starting time point for data subscription. Value range: within the last 24 hours\n        :type ConsumeStartTime: str\n        """
        self.SubscribeId = None
        self.ConsumeStartTime = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.ConsumeStartTime = params.get("ConsumeStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeConsumeTimeResponse(AbstractModel):
    """ModifySubscribeConsumeTime response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscribeNameRequest(AbstractModel):
    """ModifySubscribeName request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID\n        :type SubscribeId: str\n        :param SubscribeName: Data subscription instance name. Length limit: [1,60]\n        :type SubscribeName: str\n        """
        self.SubscribeId = None
        self.SubscribeName = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeNameResponse(AbstractModel):
    """ModifySubscribeName response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscribeObjectsRequest(AbstractModel):
    """ModifySubscribeObjects request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID\n        :type SubscribeId: str\n        :param SubscribeObjectType: Data subscription type. Valid values: 0 (full instance subscription), 1 (data subscription), 2 (structure subscription), 3 (data subscription + structure subscription)\n        :type SubscribeObjectType: int\n        :param Objects: Information of subscribed table\n        :type Objects: list of SubscribeObject\n        """
        self.SubscribeId = None
        self.SubscribeObjectType = None
        self.Objects = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self.Objects = []
            for item in params.get("Objects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self.Objects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeObjectsResponse(AbstractModel):
    """ModifySubscribeObjects response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task ID\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifySubscribeVipVportRequest(AbstractModel):
    """ModifySubscribeVipVport request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID\n        :type SubscribeId: str\n        :param DstUniqSubnetId: Specified destination subnet. If this parameter is passed in, `DstIp` must be in the destination subnet\n        :type DstUniqSubnetId: str\n        :param DstIp: Target IP. Either this field or `DstPort` must be passed in\n        :type DstIp: str\n        :param DstPort: Target port. Value range: [1025-65535]\n        :type DstPort: int\n        """
        self.SubscribeId = None
        self.DstUniqSubnetId = None
        self.DstIp = None
        self.DstPort = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.DstUniqSubnetId = params.get("DstUniqSubnetId")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeVipVportResponse(AbstractModel):
    """ModifySubscribeVipVport response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySyncJobRequest(AbstractModel):
    """ModifySyncJob request structure.

    """

    def __init__(self):
        """
        :param JobId: ID of the disaster recovery sync task to be modified\n        :type JobId: str\n        :param JobName: Name of the disaster recovery sync task\n        :type JobName: str\n        :param SyncOption: Configuration options of a disaster recovery sync task\n        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`\n        :param DatabaseInfo: When syncing the specified table, you need to set the information of the source table to be synced, which should be described in JSON string format. Below are examples.
For databases with a database-table structure:
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]\n        :type DatabaseInfo: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySyncJobResponse(AbstractModel):
    """ModifySyncJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OfflineIsolatedSubscribeRequest(AbstractModel):
    """OfflineIsolatedSubscribe request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID\n        :type SubscribeId: str\n        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineIsolatedSubscribeResponse(AbstractModel):
    """OfflineIsolatedSubscribe response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetSubscribeRequest(AbstractModel):
    """ResetSubscribe request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID\n        :type SubscribeId: str\n        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetSubscribeResponse(AbstractModel):
    """ResetSubscribe response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SrcInfo(AbstractModel):
    """Source instance information

    """

    def __init__(self):
        """
        :param AccessKey: Alibaba Cloud AccessKey, which is applicable if the source database is an Alibaba Cloud ApsaraDB for RDS 5.6 instance\n        :type AccessKey: str\n        :param Ip: Instance IP address\n        :type Ip: str\n        :param Port: Instance port\n        :type Port: int\n        :param User: Instance username\n        :type User: str\n        :param Password: Instance password\n        :type Password: str\n        :param RdsInstanceId: Alibaba Cloud ApsaraDB for RDS instance ID, which is applicable if the source database is an Alibaba Cloud ApsaraDB for RDS 5.6/5.7 instance\n        :type RdsInstanceId: str\n        :param CvmInstanceId: Short CVM instance ID in the format of `ins-olgl39y8`. It is the same as the instance ID displayed on the CVM Console page. For CVM-based self-created instances, this field needs to be passed in\n        :type CvmInstanceId: str\n        :param UniqDcgId: Direct Connect gateway ID in the format of dcg-0rxtqqxb\n        :type UniqDcgId: str\n        :param VpcId: VPC ID in the format of vpc-92jblxto\n        :type VpcId: str\n        :param SubnetId: VPC Subnet ID in the format of subnet-3paxmkdz\n        :type SubnetId: str\n        :param UniqVpnGwId: VPN gateway ID in the format of vpngw-9ghexg7q\n        :type UniqVpnGwId: str\n        :param InstanceId: Database instance ID in the format of cdb-powiqx8q\n        :type InstanceId: str\n        :param Region: Region name, such as ap-guangzhou\n        :type Region: str\n        :param Supplier: For Alibaba Cloud ApsaraDB for RDS instances, enter "aliyun"; otherwise, enter "others"\n        :type Supplier: str\n        :param CcnId: CCN instance ID, such as ccn-afp6kltc
Note: This field may return null, indicating that no valid values can be obtained.\n        :type CcnId: str\n        :param EngineVersion: Database version. This parameter is valid only when the instance is an RDS instance. Value: 5.6 or 5.7. Default value: 5.6\n        :type EngineVersion: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartSyncJobRequest(AbstractModel):
    """StartSyncJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Disaster recovery sync task ID\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartSyncJobResponse(AbstractModel):
    """StartSyncJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Data migration task ID\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubscribeInfo(AbstractModel):
    """Subscription instance information

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID\n        :type SubscribeId: str\n        :param SubscribeName: Data subscription instance name\n        :type SubscribeName: str\n        :param ChannelId: ID of channel bound to data subscription instance\n        :type ChannelId: str\n        :param Product: Name of product bound to data subscription instance\n        :type Product: str\n        :param InstanceId: ID of database instance bound to data subscription instance\n        :type InstanceId: str\n        :param InstanceStatus: Status of database instance bound to data subscription instance\n        :type InstanceStatus: str\n        :param SubsStatus: Data subscription instance configuration status. Valid values: unconfigure, configuring, configured\n        :type SubsStatus: str\n        :param ModifyTime: Last modified time\n        :type ModifyTime: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param IsolateTime: Isolation time\n        :type IsolateTime: str\n        :param ExpireTime: Expiration time\n        :type ExpireTime: str\n        :param OfflineTime: Deactivation time\n        :type OfflineTime: str\n        :param ConsumeStartTime: Last modified consumption starting time point. If it has never been modified, this field is 0\n        :type ConsumeStartTime: str\n        :param Region: Data subscription instance region\n        :type Region: str\n        :param PayType: Billing mode. 1: pay-as-you-go\n        :type PayType: int\n        :param Vip: Data subscription instance VIP\n        :type Vip: str\n        :param Vport: Data subscription instance Vport\n        :type Vport: int\n        :param UniqVpcId: Unique ID of the VPC where the data subscription instance VIP resides\n        :type UniqVpcId: str\n        :param UniqSubnetId: Unique ID of the subnet where the data subscription instance VIP resides\n        :type UniqSubnetId: str\n        :param Status: Data subscription instance status. Valid values: creating, normal, isolating, isolated, offlining, offline\n        :type Status: str\n        :param SdkConsumedTime: Timestamp of the last message confirmed by the SDK. If the SDK keeps consuming, this field can also be used as the current consumption time point of the SDK\n        :type SdkConsumedTime: str\n        :param Tags: Tag
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Tags: list of TagItem\n        :param AutoRenewFlag: Whether auto-renewal is enabled. 0: do not enable; 1: enable
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AutoRenewFlag: int\n        :param SubscribeVersion: Subscription instance edition. ·`txdts`: legacy data subscription; `kafka`: data subscription in Kafka edition
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SubscribeVersion: str\n        """
        self.SubscribeId = None
        self.SubscribeName = None
        self.ChannelId = None
        self.Product = None
        self.InstanceId = None
        self.InstanceStatus = None
        self.SubsStatus = None
        self.ModifyTime = None
        self.CreateTime = None
        self.IsolateTime = None
        self.ExpireTime = None
        self.OfflineTime = None
        self.ConsumeStartTime = None
        self.Region = None
        self.PayType = None
        self.Vip = None
        self.Vport = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.Status = None
        self.SdkConsumedTime = None
        self.Tags = None
        self.AutoRenewFlag = None
        self.SubscribeVersion = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        self.ChannelId = params.get("ChannelId")
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.SubsStatus = params.get("SubsStatus")
        self.ModifyTime = params.get("ModifyTime")
        self.CreateTime = params.get("CreateTime")
        self.IsolateTime = params.get("IsolateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.OfflineTime = params.get("OfflineTime")
        self.ConsumeStartTime = params.get("ConsumeStartTime")
        self.Region = params.get("Region")
        self.PayType = params.get("PayType")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.Status = params.get("Status")
        self.SdkConsumedTime = params.get("SdkConsumedTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.SubscribeVersion = params.get("SubscribeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeObject(AbstractModel):
    """Data subscription object

    """

    def __init__(self):
        """
        :param ObjectsType: Data subscription object type. 0: database, 1: database table
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ObjectsType: int\n        :param DatabaseName: Name of subscribed database
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DatabaseName: str\n        :param TableNames: Array of table names in subscribed database
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableNames: list of str\n        """
        self.ObjectsType = None
        self.DatabaseName = None
        self.TableNames = None


    def _deserialize(self, params):
        self.ObjectsType = params.get("ObjectsType")
        self.DatabaseName = params.get("DatabaseName")
        self.TableNames = params.get("TableNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeRegionConf(AbstractModel):
    """Sale information of data subscription region

    """

    def __init__(self):
        """
        :param RegionName: Region name, such as Guangzhou
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RegionName: str\n        :param Region: Region ID, such as ap-guangzhou
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Region: str\n        :param Area: Region name, such as South China
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Area: str\n        :param IsDefaultRegion: Whether it is the default region. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDefaultRegion: int\n        :param Status: Purchasable status of current region. 1: normal, 2: beta test, 3: not purchasable
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        """
        self.RegionName = None
        self.Region = None
        self.Area = None
        self.IsDefaultRegion = None
        self.Status = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.Region = params.get("Region")
        self.Area = params.get("Area")
        self.IsDefaultRegion = params.get("IsDefaultRegion")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDrToMasterRequest(AbstractModel):
    """SwitchDrToMaster request structure.

    """

    def __init__(self):
        """
        :param DstInfo: Disaster recovery instance information\n        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`\n        :param DatabaseType: Database type (such as MySQL)\n        :type DatabaseType: str\n        """
        self.DstInfo = None
        self.DatabaseType = None


    def _deserialize(self, params):
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseType = params.get("DatabaseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDrToMasterResponse(AbstractModel):
    """SwitchDrToMaster response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Backend async task request ID\n        :type AsyncRequestId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SyncCheckStepInfo(AbstractModel):
    """Check steps for a disaster recovery task

    """

    def __init__(self):
        """
        :param StepNo: Step number\n        :type StepNo: int\n        :param StepName: Step name\n        :type StepName: str\n        :param StepCode: Code of the step execution result\n        :type StepCode: int\n        :param StepMessage: Message about the step execution result\n        :type StepMessage: str\n        """
        self.StepNo = None
        self.StepName = None
        self.StepCode = None
        self.StepMessage = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepCode = params.get("StepCode")
        self.StepMessage = params.get("StepMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDetailInfo(AbstractModel):
    """Describes the specific process of the sync task.

    """

    def __init__(self):
        """
        :param StepAll: Total number of steps\n        :type StepAll: int\n        :param StepNow: Current step\n        :type StepNow: int\n        :param Progress: Overall progress\n        :type Progress: str\n        :param CurrentStepProgress: Progress of the current step\n        :type CurrentStepProgress: str\n        :param MasterSlaveDistance: Master/slave delay in MB\n        :type MasterSlaveDistance: int\n        :param SecondsBehindMaster: Master/slave delay in seconds\n        :type SecondsBehindMaster: int\n        :param StepInfo: Step information\n        :type StepInfo: list of SyncStepDetailInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncInstanceInfo(AbstractModel):
    """Instance information of disaster recovery sync, which records the information of the master instance or disaster recovery instance

    """

    def __init__(self):
        """
        :param Region: Region name, such as ap-guangzhou\n        :type Region: str\n        :param InstanceId: Short instance ID\n        :type InstanceId: str\n        """
        self.Region = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncJobInfo(AbstractModel):
    """Disaster recovery sync task information

    """

    def __init__(self):
        """
        :param JobId: Disaster recovery task ID\n        :type JobId: str\n        :param JobName: Disaster recovery task name\n        :type JobName: str\n        :param SyncOption: Task sync\n        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`\n        :param SrcAccessType: Source access type\n        :type SrcAccessType: str\n        :param SrcDatabaseType: Source data type\n        :type SrcDatabaseType: str\n        :param SrcInfo: Source instance information\n        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`\n        :param DstAccessType: Disaster recovery access type\n        :type DstAccessType: str\n        :param DstDatabaseType: Disaster recovery data type\n        :type DstDatabaseType: str\n        :param DstInfo: Disaster recovery instance information\n        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`\n        :param Detail: Task information\n        :type Detail: :class:`tencentcloud.dts.v20180330.models.SyncDetailInfo`\n        :param Status: Task status\n        :type Status: int\n        :param DatabaseInfo: Table to be migrated\n        :type DatabaseInfo: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncOption(AbstractModel):
    """Configuration options of a disaster recovery sync task

    """

    def __init__(self):
        """
        :param SyncObject: Sync object. 1: entire instance; 2: specified table\n        :type SyncObject: int\n        :param RunMode: Sync start configuration. 1: start immediately\n        :type RunMode: int\n        :param SyncType: Sync mode. 3: full + incremental sync\n        :type SyncType: int\n        :param ConsistencyType: Data consistency check. 1: no configuration required\n        :type ConsistencyType: int\n        """
        self.SyncObject = None
        self.RunMode = None
        self.SyncType = None
        self.ConsistencyType = None


    def _deserialize(self, params):
        self.SyncObject = params.get("SyncObject")
        self.RunMode = params.get("RunMode")
        self.SyncType = params.get("SyncType")
        self.ConsistencyType = params.get("ConsistencyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncStepDetailInfo(AbstractModel):
    """Sync task progress

    """

    def __init__(self):
        """
        :param StepNo: Step number\n        :type StepNo: int\n        :param StepName: Step name\n        :type StepName: str\n        :param CanStop: Whether it can be stopped\n        :type CanStop: int\n        :param StepId: Step ID\n        :type StepId: int\n        """
        self.StepNo = None
        self.StepName = None
        self.CanStop = None
        self.StepId = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.CanStop = params.get("CanStop")
        self.StepId = params.get("StepId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """Tag filtering

    """

    def __init__(self):
        """
        :param TagKey: Tag key value\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: list of str\n        """
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
        


class TagItem(AbstractModel):
    """Tag

    """

    def __init__(self):
        """
        :param TagKey: Tag key value\n        :type TagKey: str\n        :param TagValue: Tag value
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TagValue: str\n        """
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
        