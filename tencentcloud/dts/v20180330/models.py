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


class ActivateSubscribeRequest(AbstractModel):
    """ActivateSubscribe request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Subscription instance ID.
        :type SubscribeId: str
        :param InstanceId: Database Instance ID
        :type InstanceId: str
        :param SubscribeObjectType: Data subscription type. 0: full instance subscription, 1: data subscription, 2: structure subscription, 3: data subscription and structure subscription
        :type SubscribeObjectType: int
        :param Objects: Subscription object
        :type Objects: :class:`tencentcloud.dts.v20180330.models.SubscribeObject`
        :param UniqSubnetId: Subnet of data subscription service, which is the subnet of the database instance by default.
        :type UniqSubnetId: str
        :param Vport: Subscription service port. Default value: 7507
        :type Vport: int
        """
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


class ActivateSubscribeResponse(AbstractModel):
    """ActivateSubscribe response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Data subscription configuration task ID.
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe request structure.

    """

    def __init__(self):
        """
        :param Product: Subscribed database type. Currently, MySQL is supported
        :type Product: str
        :param PayType: Instance billing mode, which is always 1 (hourly billing),
        :type PayType: int
        :param Duration: Purchase duration in months, which is required if `PayType` is 0. Maximum value: 120 (this field is not required of global site users and is better to be hidden)
        :type Duration: int
        :param Count: Quantity. Default value: 1. Maximum value: 10
        :type Count: int
        :param AutoRenew: Whether to auto-renew. Default value: 0. This flag does not take effect for hourly billed instances (this field should be hidden from global site users)
        :type AutoRenew: int
        :param Tags: Instance resource tags
        :type Tags: list of TagItem
        """
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


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe response structure.

    """

    def __init__(self):
        """
        :param SubscribeIds: Data subscription instance ID array
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscribeIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Task ID
        :type AsyncRequestId: str
        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo response structure.

    """

    def __init__(self):
        """
        :param Info: Task execution result information
        :type Info: str
        :param Status: Task execution status. Valid values: success, failed, running
        :type Status: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DescribeRegionConfRequest(AbstractModel):
    """DescribeRegionConf request structure.

    """


class DescribeRegionConfResponse(AbstractModel):
    """DescribeRegionConf response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of purchasable regions
        :type TotalCount: int
        :param Items: Purchasable region details
        :type Items: list of SubscribeRegionConf
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
                obj = SubscribeRegionConf()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubscribeConfRequest(AbstractModel):
    """DescribeSubscribeConf request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Subscription instance ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")


class DescribeSubscribeConfResponse(AbstractModel):
    """DescribeSubscribeConf response structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Subscription instance ID
        :type SubscribeId: str
        :param SubscribeName: Subscription instance name
        :type SubscribeName: str
        :param ChannelId: Subscription channel
        :type ChannelId: str
        :param Product: Subscribed database type
        :type Product: str
        :param InstanceId: Subscribed instance
        :type InstanceId: str
        :param InstanceStatus: Subscribed instance status. Valid values: running, offline, isolate
        :type InstanceStatus: str
        :param SubsStatus: Subscription instance status. Valid values: unconfigure, configuring, configured
        :type SubsStatus: str
        :param Status: Subscription instance lifecycle status. Valid values: normal, isolating, isolated, offlining
        :type Status: str
        :param CreateTime: Subscription instance creation time
        :type CreateTime: str
        :param IsolateTime: Subscription instance isolation time
        :type IsolateTime: str
        :param ExpireTime: Subscription instance expiration time
        :type ExpireTime: str
        :param OfflineTime: Subscription instance deactivation time
        :type OfflineTime: str
        :param ConsumeStartTime: Consumption starting time point of subscription instance
        :type ConsumeStartTime: str
        :param PayType: Subscription instance billing mode. 1: hourly billing
        :type PayType: int
        :param Vip: Subscription channel VIP
        :type Vip: str
        :param Vport: Subscription channel port
        :type Vport: int
        :param UniqVpcId: Subscription channel `VpcId`
        :type UniqVpcId: str
        :param UniqSubnetId: Subscription channel `SubnetId`
        :type UniqSubnetId: str
        :param SdkConsumedTime: Current SDK consumption time point
        :type SdkConsumedTime: str
        :param SdkHost: Subscription SDK IP address
        :type SdkHost: str
        :param SubscribeObjectType: Subscription object type. 0: full instance subscription, 1: DDL data subscription, 2: DML structure subscription, 3: DDL data subscription + DML structure subscription
        :type SubscribeObjectType: int
        :param SubscribeObjects: Subscription object, which is an empty array if `SubscribeObjectType` is 0
        :type SubscribeObjects: list of SubscribeObject
        :param ModifyTime: Modification time
        :type ModifyTime: str
        :param Region: Region
        :type Region: str
        :param Tags: Tags of the subscription
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param AutoRenewFlag: Whether auto-renewal is enabled. 0: do not enable, 1: enable
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param SubscribeName: Data subscription instance name
        :type SubscribeName: str
        :param InstanceId: ID of bound database instance
        :type InstanceId: str
        :param ChannelId: Data subscription instance channel ID
        :type ChannelId: str
        :param PayType: Billing mode filter. Default value: 1 (pay-as-you-go)
        :type PayType: str
        :param Product: Subscribed database product, such as MySQL
        :type Product: str
        :param Status: Data subscription instance status. Valid values: creating, normal, isolating, isolated, offlining
        :type Status: list of str
        :param SubsStatus: Data subscription instance configuration status. Valid values: unconfigure, configuring, configured
        :type SubsStatus: list of str
        :param Offset: Starting offset of returned results
        :type Offset: int
        :param Limit: Number of results to be returned at a time
        :type Limit: int
        :param OrderDirection: Sorting order. Valid values: DESC, ASC. Default value: DESC, indicating descending by creation time
        :type OrderDirection: str
        :param TagFilters: Tag filtering condition
        :type TagFilters: list of TagFilter
        :param SubscribeVersion: Subscription instance edition. `txdts`: legacy data subscription; `kafka`: data subscription in Kafka edition
        :type SubscribeVersion: str
        """
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


class DescribeSubscribesResponse(AbstractModel):
    """DescribeSubscribes response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param Items: Information list of data subscription instances
        :type Items: list of SubscribeInfo
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
                obj = SubscribeInfo()
                obj._deserialize(item)
                self.Items.append(obj)
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
        :param User: Target database account
        :type User: str
        :param Password: Target database password
        :type Password: str
        """
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


class ErrorInfo(AbstractModel):
    """Message and prompt for migration task error

    """

    def __init__(self):
        """
        :param ErrorLog: Specific error log, including error code and error message
        :type ErrorLog: str
        :param HelpDoc: Help document URL corresponding to error
        :type HelpDoc: str
        """
        self.ErrorLog = None
        self.HelpDoc = None


    def _deserialize(self, params):
        self.ErrorLog = params.get("ErrorLog")
        self.HelpDoc = params.get("HelpDoc")


class IsolateSubscribeRequest(AbstractModel):
    """IsolateSubscribe request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Subscription instance ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")


class IsolateSubscribeResponse(AbstractModel):
    """IsolateSubscribe response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MigrateDetailInfo(AbstractModel):
    """Describes the specific migration process

    """

    def __init__(self):
        """
        :param StepAll: Total number of steps
        :type StepAll: int
        :param StepNow: Current step
        :type StepNow: int
        :param Progress: Overall progress, such as "10"
        :type Progress: str
        :param CurrentStepProgress: Progress of current step, such as "1"
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
        :param ErrorInfo: Prompt message for task error, which is not null or empty when an error occurs with the task
        :type ErrorInfo: list of ErrorInfo
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


class ModifySubscribeConsumeTimeRequest(AbstractModel):
    """ModifySubscribeConsumeTime request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param ConsumeStartTime: Consumption starting time point in the format of `Y-m-d h:m:s`, i.e., the starting time point for data subscription. Value range: within the last 24 hours
        :type ConsumeStartTime: str
        """
        self.SubscribeId = None
        self.ConsumeStartTime = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.ConsumeStartTime = params.get("ConsumeStartTime")


class ModifySubscribeConsumeTimeResponse(AbstractModel):
    """ModifySubscribeConsumeTime response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscribeNameRequest(AbstractModel):
    """ModifySubscribeName request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param SubscribeName: Data subscription instance name. Length limit: [1,60]
        :type SubscribeName: str
        """
        self.SubscribeId = None
        self.SubscribeName = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")


class ModifySubscribeNameResponse(AbstractModel):
    """ModifySubscribeName response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscribeObjectsRequest(AbstractModel):
    """ModifySubscribeObjects request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param SubscribeObjectType: Data subscription type. Valid values: 0 (full instance subscription), 1 (data subscription), 2 (structure subscription), 3 (data subscription + structure subscription)
        :type SubscribeObjectType: int
        :param Objects: Information of subscribed table
        :type Objects: list of SubscribeObject
        """
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


class ModifySubscribeObjectsResponse(AbstractModel):
    """ModifySubscribeObjects response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Async task ID
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param DstUniqSubnetId: Specified destination subnet. If this parameter is passed in, `DstIp` must be in the destination subnet
        :type DstUniqSubnetId: str
        :param DstIp: Target IP. Either this field or `DstPort` must be passed in
        :type DstIp: str
        :param DstPort: Target port. Value range: [1025-65535]
        :type DstPort: int
        """
        self.SubscribeId = None
        self.DstUniqSubnetId = None
        self.DstIp = None
        self.DstPort = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.DstUniqSubnetId = params.get("DstUniqSubnetId")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")


class ModifySubscribeVipVportResponse(AbstractModel):
    """ModifySubscribeVipVport response structure.

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


class OfflineIsolatedSubscribeRequest(AbstractModel):
    """OfflineIsolatedSubscribe request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")


class OfflineIsolatedSubscribeResponse(AbstractModel):
    """OfflineIsolatedSubscribe response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetSubscribeRequest(AbstractModel):
    """ResetSubscribe request structure.

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")


class ResetSubscribeResponse(AbstractModel):
    """ResetSubscribe response structure.

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


class SubscribeInfo(AbstractModel):
    """Subscription instance information

    """

    def __init__(self):
        """
        :param SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param SubscribeName: Data subscription instance name
        :type SubscribeName: str
        :param ChannelId: ID of channel bound to data subscription instance
        :type ChannelId: str
        :param Product: Name of product bound to data subscription instance
        :type Product: str
        :param InstanceId: ID of database instance bound to data subscription instance
        :type InstanceId: str
        :param InstanceStatus: Status of database instance bound to data subscription instance
        :type InstanceStatus: str
        :param SubsStatus: Data subscription instance configuration status. Valid values: unconfigure, configuring, configured
        :type SubsStatus: str
        :param ModifyTime: Last modified time
        :type ModifyTime: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param IsolateTime: Isolation time
        :type IsolateTime: str
        :param ExpireTime: Expiration time
        :type ExpireTime: str
        :param OfflineTime: Deactivation time
        :type OfflineTime: str
        :param ConsumeStartTime: Last modified consumption starting time point. If it has never been modified, this field is 0
        :type ConsumeStartTime: str
        :param Region: Data subscription instance region
        :type Region: str
        :param PayType: Billing mode. 1: pay-as-you-go
        :type PayType: int
        :param Vip: Data subscription instance VIP
        :type Vip: str
        :param Vport: Data subscription instance Vport
        :type Vport: int
        :param UniqVpcId: Unique ID of the VPC where the data subscription instance VIP resides
        :type UniqVpcId: str
        :param UniqSubnetId: Unique ID of the subnet where the data subscription instance VIP resides
        :type UniqSubnetId: str
        :param Status: Data subscription instance status. Valid values: creating, normal, isolating, isolated, offlining, offline
        :type Status: str
        :param SdkConsumedTime: Timestamp of the last message confirmed by the SDK. If the SDK keeps consuming, this field can also be used as the current consumption time point of the SDK
        :type SdkConsumedTime: str
        :param Tags: Tag
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param AutoRenewFlag: Whether auto-renewal is enabled. 0: do not enable; 1: enable
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param SubscribeVersion: Subscription instance edition. ·`txdts`: legacy data subscription; `kafka`: data subscription in Kafka edition
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SubscribeVersion: str
        """
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


class SubscribeObject(AbstractModel):
    """Data subscription object

    """

    def __init__(self):
        """
        :param ObjectsType: Data subscription object type. 0: database, 1: database table
Note: this field may return null, indicating that no valid values can be obtained.
        :type ObjectsType: int
        :param DatabaseName: Name of subscribed database
Note: this field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param TableNames: Array of table names in subscribed database
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableNames: list of str
        """
        self.ObjectsType = None
        self.DatabaseName = None
        self.TableNames = None


    def _deserialize(self, params):
        self.ObjectsType = params.get("ObjectsType")
        self.DatabaseName = params.get("DatabaseName")
        self.TableNames = params.get("TableNames")


class SubscribeRegionConf(AbstractModel):
    """Sale information of data subscription region

    """

    def __init__(self):
        """
        :param RegionName: Region name, such as Guangzhou
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionName: str
        :param Region: Region ID, such as ap-guangzhou
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param Area: Region name, such as South China
Note: this field may return null, indicating that no valid values can be obtained.
        :type Area: str
        :param IsDefaultRegion: Whether it is the default region. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDefaultRegion: int
        :param Status: Purchasable status of current region. 1: normal, 2: beta test, 3: not purchasable
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
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


class SwitchDrToMasterRequest(AbstractModel):
    """SwitchDrToMaster request structure.

    """

    def __init__(self):
        """
        :param DstInfo: Disaster recovery instance information
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DatabaseType: Database type (such as MySQL)
        :type DatabaseType: str
        """
        self.DstInfo = None
        self.DatabaseType = None


    def _deserialize(self, params):
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseType = params.get("DatabaseType")


class SwitchDrToMasterResponse(AbstractModel):
    """SwitchDrToMaster response structure.

    """

    def __init__(self):
        """
        :param AsyncRequestId: Backend async task request ID
        :type AsyncRequestId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class TagFilter(AbstractModel):
    """Tag filtering

    """

    def __init__(self):
        """
        :param TagKey: Tag key value
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: list of str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TagItem(AbstractModel):
    """Tag

    """

    def __init__(self):
        """
        :param TagKey: Tag key value
        :type TagKey: str
        :param TagValue: Tag value
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")