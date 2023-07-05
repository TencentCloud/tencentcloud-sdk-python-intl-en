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
        r"""
        :param _SubscribeId: Subscription instance ID.
        :type SubscribeId: str
        :param _InstanceId: Database Instance ID
        :type InstanceId: str
        :param _SubscribeObjectType: Data subscription type. 0: full instance subscription, 1: data subscription, 2: structure subscription, 3: data subscription and structure subscription
        :type SubscribeObjectType: int
        :param _Objects: Subscription object
        :type Objects: :class:`tencentcloud.dts.v20180330.models.SubscribeObject`
        :param _UniqSubnetId: Subnet of data subscription service, which is the subnet of the database instance by default.
        :type UniqSubnetId: str
        :param _Vport: Subscription service port. Default value: 7507
        :type Vport: int
        """
        self._SubscribeId = None
        self._InstanceId = None
        self._SubscribeObjectType = None
        self._Objects = None
        self._UniqSubnetId = None
        self._Vport = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SubscribeObjectType(self):
        return self._SubscribeObjectType

    @SubscribeObjectType.setter
    def SubscribeObjectType(self, SubscribeObjectType):
        self._SubscribeObjectType = SubscribeObjectType

    @property
    def Objects(self):
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._InstanceId = params.get("InstanceId")
        self._SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self._Objects = SubscribeObject()
            self._Objects._deserialize(params.get("Objects"))
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateSubscribeResponse(AbstractModel):
    """ActivateSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Data subscription configuration task ID.
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


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        :param _CompleteMode: The way to complete the task, which is supported only for legacy MySQL migration task. waitForSync: wait for the source-replica lag to become 0 before stopping; immediately: complete immediately without waiting for source-replica sync. Default value: waitForSync
        :type CompleteMode: str
        """
        self._JobId = None
        self._CompleteMode = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompleteMode(self):
        return self._CompleteMode

    @CompleteMode.setter
    def CompleteMode(self, CompleteMode):
        self._CompleteMode = CompleteMode


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompleteMode = params.get("CompleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob response structure.

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


class ConsistencyParams(AbstractModel):
    """Sampling parameter for spot check

    """

    def __init__(self):
        r"""
        :param _SelectRowsPerTable: Data content check parameter, which refers to the proportion of the rows selected for data comparison in all the rows of the table. Value: an integer between 1 and 100.
        :type SelectRowsPerTable: int
        :param _TablesSelectAll: Data content check parameter, which refers to the proportion of the tables selected for data detection in all the tables. Value: an integer between 1 and 100.
        :type TablesSelectAll: int
        :param _TablesSelectCount: Data quantity check parameter, which checks whether the numbers of rows are identical. It refers to the proportion of the tables selected for quantity check in all the tables. Value: an integer between 1 and 100.
        :type TablesSelectCount: int
        """
        self._SelectRowsPerTable = None
        self._TablesSelectAll = None
        self._TablesSelectCount = None

    @property
    def SelectRowsPerTable(self):
        return self._SelectRowsPerTable

    @SelectRowsPerTable.setter
    def SelectRowsPerTable(self, SelectRowsPerTable):
        self._SelectRowsPerTable = SelectRowsPerTable

    @property
    def TablesSelectAll(self):
        return self._TablesSelectAll

    @TablesSelectAll.setter
    def TablesSelectAll(self, TablesSelectAll):
        self._TablesSelectAll = TablesSelectAll

    @property
    def TablesSelectCount(self):
        return self._TablesSelectCount

    @TablesSelectCount.setter
    def TablesSelectCount(self, TablesSelectCount):
        self._TablesSelectCount = TablesSelectCount


    def _deserialize(self, params):
        self._SelectRowsPerTable = params.get("SelectRowsPerTable")
        self._TablesSelectAll = params.get("TablesSelectAll")
        self._TablesSelectCount = params.get("TablesSelectCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob response structure.

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


class CreateMigrateJobRequest(AbstractModel):
    """CreateMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobName: Data migration task name
        :type JobName: str
        :param _MigrateOption: Migration task configuration options
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param _SrcDatabaseType: Source instance database type, which currently supports MySQL, Redis, MongoDB, PostgreSQL, MariaDB, Percona, and SQL Server. For more information on the supported types in a specific region, see the migration task creation page in the console.
        :type SrcDatabaseType: str
        :param _SrcAccessType: Source instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance), ccn (CCN instance)
        :type SrcAccessType: str
        :param _SrcInfo: Source instance information, which is correlated with the migration task type
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param _DstDatabaseType: Target instance access type, which currently supports MySQL, Redis, MongoDB, PostgreSQL, MariaDB, and Percona, SQL Server, and TDSQL-C for MySQL. For more information on the supported types in a specific region, see the migration task creation page in the console.
        :type DstDatabaseType: str
        :param _DstAccessType: Target instance access type, which currently only supports cdb (TencentDB instance)
        :type DstAccessType: str
        :param _DstInfo: Destination instance information
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param _DatabaseInfo: Information of the source table to be migrated, which is described in JSON string format. It is required if MigrateOption.MigrateObject is 2 (migrating the specified table).
For databases with a database-table structure:
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
For databases with a database-schema-table structure:
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]
        :type DatabaseInfo: str
        :param _Tags: Tag of the instance to be migrated.
        :type Tags: list of TagItem
        :param _SrcNodeType: Source instance type. `simple`: Primary/Secondary node; `cluster`: Cluster node. If this field is left empty, the value defaults to primary/secondary node.
        :type SrcNodeType: str
        :param _SrcInfoMulti: Source instance information, which is correlated with the migration task type.
        :type SrcInfoMulti: list of SrcInfo
        """
        self._JobName = None
        self._MigrateOption = None
        self._SrcDatabaseType = None
        self._SrcAccessType = None
        self._SrcInfo = None
        self._DstDatabaseType = None
        self._DstAccessType = None
        self._DstInfo = None
        self._DatabaseInfo = None
        self._Tags = None
        self._SrcNodeType = None
        self._SrcInfoMulti = None

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def MigrateOption(self):
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def SrcDatabaseType(self):
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstDatabaseType(self):
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DatabaseInfo(self):
        return self._DatabaseInfo

    @DatabaseInfo.setter
    def DatabaseInfo(self, DatabaseInfo):
        self._DatabaseInfo = DatabaseInfo

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SrcNodeType(self):
        return self._SrcNodeType

    @SrcNodeType.setter
    def SrcNodeType(self, SrcNodeType):
        self._SrcNodeType = SrcNodeType

    @property
    def SrcInfoMulti(self):
        return self._SrcInfoMulti

    @SrcInfoMulti.setter
    def SrcInfoMulti(self, SrcInfoMulti):
        self._SrcInfoMulti = SrcInfoMulti


    def _deserialize(self, params):
        self._JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._DatabaseInfo = params.get("DatabaseInfo")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SrcNodeType = params.get("SrcNodeType")
        if params.get("SrcInfoMulti") is not None:
            self._SrcInfoMulti = []
            for item in params.get("SrcInfoMulti"):
                obj = SrcInfo()
                obj._deserialize(item)
                self._SrcInfoMulti.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateJobResponse(AbstractModel):
    """CreateMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Subscribed database type. Currently, MySQL is supported
        :type Product: str
        :param _PayType: Instance billing mode, which is always 1 (hourly billing),
        :type PayType: int
        :param _Duration: Purchase duration in months, which is required if `PayType` is 0. Maximum value: 120 (this field is not required of global site users and is better to be hidden)
        :type Duration: int
        :param _Count: Quantity. Default value: 1. Maximum value: 10
        :type Count: int
        :param _AutoRenew: Whether to auto-renew. Default value: 0. This flag does not take effect for hourly billed instances (this field should be hidden from global site users)
        :type AutoRenew: int
        :param _Tags: Instance resource tags
        :type Tags: list of TagItem
        :param _Name: A custom instance name.
        :type Name: str
        """
        self._Product = None
        self._PayType = None
        self._Duration = None
        self._Count = None
        self._AutoRenew = None
        self._Tags = None
        self._Name = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._PayType = params.get("PayType")
        self._Duration = params.get("Duration")
        self._Count = params.get("Count")
        self._AutoRenew = params.get("AutoRenew")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeIds: Data subscription instance ID array
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscribeIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SubscribeIds = None
        self._RequestId = None

    @property
    def SubscribeIds(self):
        return self._SubscribeIds

    @SubscribeIds.setter
    def SubscribeIds(self, SubscribeIds):
        self._SubscribeIds = SubscribeIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscribeIds = params.get("SubscribeIds")
        self._RequestId = params.get("RequestId")


class DeleteMigrateJobRequest(AbstractModel):
    """DeleteMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMigrateJobResponse(AbstractModel):
    """DeleteMigrateJob response structure.

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


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Task ID
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
        :param _Info: Task execution result information
        :type Info: str
        :param _Status: Task execution status. Valid values: success, failed, running
        :type Status: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._Status = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        self._Info = params.get("Info")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeMigrateCheckJobRequest(AbstractModel):
    """DescribeMigrateCheckJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateCheckJobResponse(AbstractModel):
    """DescribeMigrateCheckJob response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Check task status: unavailable, starting, running, finished
        :type Status: str
        :param _ErrorCode: Task error code
        :type ErrorCode: int
        :param _ErrorMessage: Task error message
        :type ErrorMessage: str
        :param _Progress: Check task progress. For example, "30" means 30% completed
        :type Progress: str
        :param _CheckFlag: Whether the check succeeds. 0: no; 1: yes; 3: not checked
        :type CheckFlag: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._Progress = None
        self._CheckFlag = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CheckFlag(self):
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._Progress = params.get("Progress")
        self._CheckFlag = params.get("CheckFlag")
        self._RequestId = params.get("RequestId")


class DescribeMigrateJobsRequest(AbstractModel):
    """DescribeMigrateJobs request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        :param _JobName: Data migration task name
        :type JobName: str
        :param _Order: Sort by field. Value range: JobId, Status, JobName, MigrateType, RunMode, CreateTime
        :type Order: str
        :param _OrderSeq: Sorting order. Value range: ASC (ascending), DESC (descending)
        :type OrderSeq: str
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Number of the returned instances. Value range: [1, 100]. Default value: 20
        :type Limit: int
        :param _TagFilters: Tag filter.
        :type TagFilters: list of TagFilter
        """
        self._JobId = None
        self._JobName = None
        self._Order = None
        self._OrderSeq = None
        self._Offset = None
        self._Limit = None
        self._TagFilters = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderSeq(self):
        return self._OrderSeq

    @OrderSeq.setter
    def OrderSeq(self, OrderSeq):
        self._OrderSeq = OrderSeq

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
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Order = params.get("Order")
        self._OrderSeq = params.get("OrderSeq")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateJobsResponse(AbstractModel):
    """DescribeMigrateJobs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of tasks
        :type TotalCount: int
        :param _JobList: Array of task details
        :type JobList: list of MigrateJobInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobList(self):
        return self._JobList

    @JobList.setter
    def JobList(self, JobList):
        self._JobList = JobList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self._JobList = []
            for item in params.get("JobList"):
                obj = MigrateJobInfo()
                obj._deserialize(item)
                self._JobList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionConfRequest(AbstractModel):
    """DescribeRegionConf request structure.

    """


class DescribeRegionConfResponse(AbstractModel):
    """DescribeRegionConf response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of purchasable regions
        :type TotalCount: int
        :param _Items: Purchasable region details
        :type Items: list of SubscribeRegionConf
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SubscribeRegionConf()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeConfRequest(AbstractModel):
    """DescribeSubscribeConf request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeConfResponse(AbstractModel):
    """DescribeSubscribeConf response structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        :param _SubscribeName: Subscription instance name
        :type SubscribeName: str
        :param _ChannelId: Subscription channel
        :type ChannelId: str
        :param _Product: Subscribed database type
        :type Product: str
        :param _InstanceId: Subscribed instance
        :type InstanceId: str
        :param _InstanceStatus: Subscribed instance status. Valid values: running, offline, isolate
        :type InstanceStatus: str
        :param _SubsStatus: Subscription instance status. Valid values: unconfigure, configuring, configured
        :type SubsStatus: str
        :param _Status: Subscription instance lifecycle status. Valid values: normal, isolating, isolated, offlining
        :type Status: str
        :param _CreateTime: Subscription instance creation time
        :type CreateTime: str
        :param _IsolateTime: Subscription instance isolation time
        :type IsolateTime: str
        :param _ExpireTime: Subscription instance expiration time
        :type ExpireTime: str
        :param _OfflineTime: Subscription instance deactivation time
        :type OfflineTime: str
        :param _ConsumeStartTime: Consumption starting time point of subscription instance
        :type ConsumeStartTime: str
        :param _PayType: Subscription instance billing mode. 1: hourly billing
        :type PayType: int
        :param _Vip: Subscription channel VIP
        :type Vip: str
        :param _Vport: Subscription channel port
        :type Vport: int
        :param _UniqVpcId: Subscription channel `VpcId`
        :type UniqVpcId: str
        :param _UniqSubnetId: Subscription channel `SubnetId`
        :type UniqSubnetId: str
        :param _SdkConsumedTime: Current SDK consumption time point
        :type SdkConsumedTime: str
        :param _SdkHost: Subscription SDK IP address
        :type SdkHost: str
        :param _SubscribeObjectType: Subscription object type. 0: full instance subscription, 1: DDL data subscription, 2: DML structure subscription, 3: DDL data subscription + DML structure subscription
        :type SubscribeObjectType: int
        :param _SubscribeObjects: Subscription object, which is an empty array if `SubscribeObjectType` is 0
        :type SubscribeObjects: list of SubscribeObject
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        :param _Region: Region
        :type Region: str
        :param _Tags: Tags of the subscription
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param _AutoRenewFlag: Whether auto-renewal is enabled. 0: do not enable, 1: enable
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param _SubscribeVersion: Data subscription edition. `txdts`: Legacy edition; `kafka`: Kafka edition.
        :type SubscribeVersion: str
        :param _Errors: Error message.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Errors: list of SubsErr
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._ChannelId = None
        self._Product = None
        self._InstanceId = None
        self._InstanceStatus = None
        self._SubsStatus = None
        self._Status = None
        self._CreateTime = None
        self._IsolateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._ConsumeStartTime = None
        self._PayType = None
        self._Vip = None
        self._Vport = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._SdkConsumedTime = None
        self._SdkHost = None
        self._SubscribeObjectType = None
        self._SubscribeObjects = None
        self._ModifyTime = None
        self._Region = None
        self._Tags = None
        self._AutoRenewFlag = None
        self._SubscribeVersion = None
        self._Errors = None
        self._RequestId = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SubsStatus(self):
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def ConsumeStartTime(self):
        return self._ConsumeStartTime

    @ConsumeStartTime.setter
    def ConsumeStartTime(self, ConsumeStartTime):
        self._ConsumeStartTime = ConsumeStartTime

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

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
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def SdkConsumedTime(self):
        return self._SdkConsumedTime

    @SdkConsumedTime.setter
    def SdkConsumedTime(self, SdkConsumedTime):
        self._SdkConsumedTime = SdkConsumedTime

    @property
    def SdkHost(self):
        return self._SdkHost

    @SdkHost.setter
    def SdkHost(self, SdkHost):
        self._SdkHost = SdkHost

    @property
    def SubscribeObjectType(self):
        return self._SubscribeObjectType

    @SubscribeObjectType.setter
    def SubscribeObjectType(self, SubscribeObjectType):
        self._SubscribeObjectType = SubscribeObjectType

    @property
    def SubscribeObjects(self):
        return self._SubscribeObjects

    @SubscribeObjects.setter
    def SubscribeObjects(self, SubscribeObjects):
        self._SubscribeObjects = SubscribeObjects

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

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
    def SubscribeVersion(self):
        return self._SubscribeVersion

    @SubscribeVersion.setter
    def SubscribeVersion(self, SubscribeVersion):
        self._SubscribeVersion = SubscribeVersion

    @property
    def Errors(self):
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._ChannelId = params.get("ChannelId")
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._SubsStatus = params.get("SubsStatus")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._IsolateTime = params.get("IsolateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._ConsumeStartTime = params.get("ConsumeStartTime")
        self._PayType = params.get("PayType")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._SdkConsumedTime = params.get("SdkConsumedTime")
        self._SdkHost = params.get("SdkHost")
        self._SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("SubscribeObjects") is not None:
            self._SubscribeObjects = []
            for item in params.get("SubscribeObjects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self._SubscribeObjects.append(obj)
        self._ModifyTime = params.get("ModifyTime")
        self._Region = params.get("Region")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SubscribeVersion = params.get("SubscribeVersion")
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SubsErr()
                obj._deserialize(item)
                self._Errors.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribesRequest(AbstractModel):
    """DescribeSubscribes request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _SubscribeName: Data subscription instance name
        :type SubscribeName: str
        :param _InstanceId: ID of bound database instance
        :type InstanceId: str
        :param _ChannelId: Data subscription instance channel ID
        :type ChannelId: str
        :param _PayType: Billing mode filter. Default value: 1 (pay-as-you-go)
        :type PayType: str
        :param _Product: Subscribed database product, such as MySQL
        :type Product: str
        :param _Status: Data subscription instance status. Valid values: creating, normal, isolating, isolated, offlining
        :type Status: list of str
        :param _SubsStatus: Data subscription instance configuration status. Valid values: unconfigure, configuring, configured
        :type SubsStatus: list of str
        :param _Offset: Starting offset of returned results
        :type Offset: int
        :param _Limit: Number of results to be returned at a time
        :type Limit: int
        :param _OrderDirection: Sorting order. Valid values: DESC, ASC. Default value: DESC, indicating descending by creation time
        :type OrderDirection: str
        :param _TagFilters: Tag filtering condition
        :type TagFilters: list of TagFilter
        :param _SubscribeVersion: Subscription instance edition. `txdts`: legacy data subscription; `kafka`: data subscription in Kafka edition
        :type SubscribeVersion: str
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._InstanceId = None
        self._ChannelId = None
        self._PayType = None
        self._Product = None
        self._Status = None
        self._SubsStatus = None
        self._Offset = None
        self._Limit = None
        self._OrderDirection = None
        self._TagFilters = None
        self._SubscribeVersion = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubsStatus(self):
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

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
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def SubscribeVersion(self):
        return self._SubscribeVersion

    @SubscribeVersion.setter
    def SubscribeVersion(self, SubscribeVersion):
        self._SubscribeVersion = SubscribeVersion


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._InstanceId = params.get("InstanceId")
        self._ChannelId = params.get("ChannelId")
        self._PayType = params.get("PayType")
        self._Product = params.get("Product")
        self._Status = params.get("Status")
        self._SubsStatus = params.get("SubsStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderDirection = params.get("OrderDirection")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._SubscribeVersion = params.get("SubscribeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribesResponse(AbstractModel):
    """DescribeSubscribes response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _Items: Information list of data subscription instances
        :type Items: list of SubscribeInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SubscribeInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """Target instance information, which is correlated with the migration task type

    """

    def __init__(self):
        r"""
        :param _InstanceId: Target instance ID, such as cdb-jd92ijd8
        :type InstanceId: str
        :param _Region: Target instance region, such as ap-guangzhou
        :type Region: str
        :param _Ip: Target instance VIP, which has been disused and does not need to be entered
        :type Ip: str
        :param _Port: Target instance Vport, which has been disused and does not need to be entered
        :type Port: int
        :param _ReadOnly: Only valid for MySQL currently. For instance-level migration, the value range is: 1 (read-only), 0 (read/write)
        :type ReadOnly: int
        :param _User: Target database account
        :type User: str
        :param _Password: Target database password
        :type Password: str
        """
        self._InstanceId = None
        self._Region = None
        self._Ip = None
        self._Port = None
        self._ReadOnly = None
        self._User = None
        self._Password = None

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

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._ReadOnly = params.get("ReadOnly")
        self._User = params.get("User")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfo(AbstractModel):
    """Message and prompt for migration task error

    """

    def __init__(self):
        r"""
        :param _ErrorLog: Specific error log, including error code and error message
        :type ErrorLog: str
        :param _HelpDoc: Help document URL corresponding to error
        :type HelpDoc: str
        """
        self._ErrorLog = None
        self._HelpDoc = None

    @property
    def ErrorLog(self):
        return self._ErrorLog

    @ErrorLog.setter
    def ErrorLog(self, ErrorLog):
        self._ErrorLog = ErrorLog

    @property
    def HelpDoc(self):
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc


    def _deserialize(self, params):
        self._ErrorLog = params.get("ErrorLog")
        self._HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSubscribeRequest(AbstractModel):
    """IsolateSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSubscribeResponse(AbstractModel):
    """IsolateSubscribe response structure.

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


class MigrateDetailInfo(AbstractModel):
    """Describes the specific migration process

    """

    def __init__(self):
        r"""
        :param _StepAll: Total number of steps
        :type StepAll: int
        :param _StepNow: Current step
        :type StepNow: int
        :param _Progress: Overall progress, such as "10"
        :type Progress: str
        :param _CurrentStepProgress: Progress of current step, such as "1"
        :type CurrentStepProgress: str
        :param _MasterSlaveDistance: Master/slave lag in MB, which is valid during incremental sync and currently supported by TencentDB for Redis and MySQL
        :type MasterSlaveDistance: int
        :param _SecondsBehindMaster: Master/slave lag in seconds, which is valid during incremental sync and currently supported by TencentDB for MySQL
        :type SecondsBehindMaster: int
        :param _StepInfo: Step information
        :type StepInfo: list of MigrateStepDetailInfo
        """
        self._StepAll = None
        self._StepNow = None
        self._Progress = None
        self._CurrentStepProgress = None
        self._MasterSlaveDistance = None
        self._SecondsBehindMaster = None
        self._StepInfo = None

    @property
    def StepAll(self):
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CurrentStepProgress(self):
        return self._CurrentStepProgress

    @CurrentStepProgress.setter
    def CurrentStepProgress(self, CurrentStepProgress):
        self._CurrentStepProgress = CurrentStepProgress

    @property
    def MasterSlaveDistance(self):
        return self._MasterSlaveDistance

    @MasterSlaveDistance.setter
    def MasterSlaveDistance(self, MasterSlaveDistance):
        self._MasterSlaveDistance = MasterSlaveDistance

    @property
    def SecondsBehindMaster(self):
        return self._SecondsBehindMaster

    @SecondsBehindMaster.setter
    def SecondsBehindMaster(self, SecondsBehindMaster):
        self._SecondsBehindMaster = SecondsBehindMaster

    @property
    def StepInfo(self):
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo


    def _deserialize(self, params):
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._Progress = params.get("Progress")
        self._CurrentStepProgress = params.get("CurrentStepProgress")
        self._MasterSlaveDistance = params.get("MasterSlaveDistance")
        self._SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self._StepInfo = []
            for item in params.get("StepInfo"):
                obj = MigrateStepDetailInfo()
                obj._deserialize(item)
                self._StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateJobInfo(AbstractModel):
    """Migration task details

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        :param _JobName: Data migration task name
        :type JobName: str
        :param _MigrateOption: Migration task configuration options
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param _SrcDatabaseType: Source instance database type: MySQL, Redis, MongoDB, PostgreSQL, MariaDB, Percona
        :type SrcDatabaseType: str
        :param _SrcAccessType: Source instance access type. Value range: extranet (public network), cvm (CVM-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance), ccn (CCN instances)
        :type SrcAccessType: str
        :param _SrcInfo: Source instance information, which is correlated with the migration task type
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param _DstDatabaseType: Target instance access type: MySQL, Redis, MongoDB, PostgreSQL, MariaDB, Percona
        :type DstDatabaseType: str
        :param _DstAccessType: Target instance access type, which currently only supports cdb (TencentDB instance)
        :type DstAccessType: str
        :param _DstInfo: Target instance information
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param _DatabaseInfo: Information of the source table to be migrated. If the entire instance is to be migrated, this field should be []
        :type DatabaseInfo: str
        :param _CreateTime: Task creation/submission time
        :type CreateTime: str
        :param _StartTime: Task start time
        :type StartTime: str
        :param _EndTime: Task end time
        :type EndTime: str
        :param _Status: Task status. Value range: 1 (Creating), 3 (Checking), 4 (CheckPass), 5 (CheckNotPass), 7 (Running), 8 (ReadyComplete), 9 (Success), 10 (Failed), 11 (Stopping), 12 (Completing)
        :type Status: int
        :param _Detail: Task details
        :type Detail: :class:`tencentcloud.dts.v20180330.models.MigrateDetailInfo`
        :param _ErrorInfo: Prompt message for task error, which is not null or empty when an error occurs with the task
        :type ErrorInfo: list of ErrorInfo
        :param _Tags: Tag
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param _SrcInfoMulti: Information of the source instance, a cluster edition instance whose access type is not `cdb`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SrcInfoMulti: list of SrcInfo
        """
        self._JobId = None
        self._JobName = None
        self._MigrateOption = None
        self._SrcDatabaseType = None
        self._SrcAccessType = None
        self._SrcInfo = None
        self._DstDatabaseType = None
        self._DstAccessType = None
        self._DstInfo = None
        self._DatabaseInfo = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Detail = None
        self._ErrorInfo = None
        self._Tags = None
        self._SrcInfoMulti = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def MigrateOption(self):
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def SrcDatabaseType(self):
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstDatabaseType(self):
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DatabaseInfo(self):
        return self._DatabaseInfo

    @DatabaseInfo.setter
    def DatabaseInfo(self, DatabaseInfo):
        self._DatabaseInfo = DatabaseInfo

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SrcInfoMulti(self):
        return self._SrcInfoMulti

    @SrcInfoMulti.setter
    def SrcInfoMulti(self, SrcInfoMulti):
        self._SrcInfoMulti = SrcInfoMulti


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._DatabaseInfo = params.get("DatabaseInfo")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        if params.get("Detail") is not None:
            self._Detail = MigrateDetailInfo()
            self._Detail._deserialize(params.get("Detail"))
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = []
            for item in params.get("ErrorInfo"):
                obj = ErrorInfo()
                obj._deserialize(item)
                self._ErrorInfo.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("SrcInfoMulti") is not None:
            self._SrcInfoMulti = []
            for item in params.get("SrcInfoMulti"):
                obj = SrcInfo()
                obj._deserialize(item)
                self._SrcInfoMulti.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOption(AbstractModel):
    """Migration task configuration options

    """

    def __init__(self):
        r"""
        :param _RunMode: Task operation mode. Value range: 1 (immediate execution), 2 (scheduled execution)
        :type RunMode: int
        :param _ExpectTime: Expected execution time in the format of yyyy-mm-dd hh:mm:ss. If runMode=2, this field is required
        :type ExpectTime: str
        :param _MigrateType: Data migration type. Value range: 1 (structural migration), 2 (full migration), 3 (full + incremental migration)
        :type MigrateType: int
        :param _MigrateObject: Migration subject. 1: entire instance; 2: specified table
        :type MigrateObject: int
        :param _ConsistencyType: Parameter of spot data consistency check. 1: not configured; 2: full check; 3: spot check; 4: check inconsistent tables only; 5: no check
        :type ConsistencyType: int
        :param _IsOverrideRoot: Whether to overwrite the target database with the root account of the source database. Value range: 0 (no), 1 (yes). This value should be 0 for table or structural migration
        :type IsOverrideRoot: int
        :param _ExternParams: Additional parameters for different databases, which are described in JSON format. 
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
        :param _ConsistencyParams: Only used for "spot data consistency check". It is required if ConsistencyType is spot check
        :type ConsistencyParams: :class:`tencentcloud.dts.v20180330.models.ConsistencyParams`
        """
        self._RunMode = None
        self._ExpectTime = None
        self._MigrateType = None
        self._MigrateObject = None
        self._ConsistencyType = None
        self._IsOverrideRoot = None
        self._ExternParams = None
        self._ConsistencyParams = None

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectTime(self):
        return self._ExpectTime

    @ExpectTime.setter
    def ExpectTime(self, ExpectTime):
        self._ExpectTime = ExpectTime

    @property
    def MigrateType(self):
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def MigrateObject(self):
        return self._MigrateObject

    @MigrateObject.setter
    def MigrateObject(self, MigrateObject):
        self._MigrateObject = MigrateObject

    @property
    def ConsistencyType(self):
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def IsOverrideRoot(self):
        return self._IsOverrideRoot

    @IsOverrideRoot.setter
    def IsOverrideRoot(self, IsOverrideRoot):
        self._IsOverrideRoot = IsOverrideRoot

    @property
    def ExternParams(self):
        return self._ExternParams

    @ExternParams.setter
    def ExternParams(self, ExternParams):
        self._ExternParams = ExternParams

    @property
    def ConsistencyParams(self):
        return self._ConsistencyParams

    @ConsistencyParams.setter
    def ConsistencyParams(self, ConsistencyParams):
        self._ConsistencyParams = ConsistencyParams


    def _deserialize(self, params):
        self._RunMode = params.get("RunMode")
        self._ExpectTime = params.get("ExpectTime")
        self._MigrateType = params.get("MigrateType")
        self._MigrateObject = params.get("MigrateObject")
        self._ConsistencyType = params.get("ConsistencyType")
        self._IsOverrideRoot = params.get("IsOverrideRoot")
        self._ExternParams = params.get("ExternParams")
        if params.get("ConsistencyParams") is not None:
            self._ConsistencyParams = ConsistencyParams()
            self._ConsistencyParams._deserialize(params.get("ConsistencyParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateStepDetailInfo(AbstractModel):
    """Information of steps in migration

    """

    def __init__(self):
        r"""
        :param _StepNo: Step number
        :type StepNo: int
        :param _StepName: Step name
        :type StepName: str
        :param _StepId: Step ID
        :type StepId: str
        :param _Status: Step status. Value range: 0 (default), 1 (succeeded), 2 (failed), 3 (in progress), 4 (not started)
        :type Status: int
        :param _StartTime: Start time of current step in the format of `yyyy-mm-dd hh:mm:ss`. This field is meaningless if it does not exist or is empty
Note: this field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        """
        self._StepNo = None
        self._StepName = None
        self._StepId = None
        self._Status = None
        self._StartTime = None

    @property
    def StepNo(self):
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobRequest(AbstractModel):
    """ModifyMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: ID of the data migration task to be modified
        :type JobId: str
        :param _JobName: Data migration task name
        :type JobName: str
        :param _MigrateOption: Migration task configuration options
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param _SrcAccessType: Source instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance)
        :type SrcAccessType: str
        :param _SrcInfo: Source instance information, which is correlated with the migration task type
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param _DstAccessType: Target instance access type. Valid values: extranet (public network), cvm (CVM-based self-created instance), dcg (Direct Connect-enabled instance), vpncloud (Tencent Cloud VPN-enabled instance), cdb (TencentDB instance). Currently, only `cdb` is supported
        :type DstAccessType: str
        :param _DstInfo: Target instance information. The region where the target instance is located cannot be modified.
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param _DatabaseInfo: When migrating the specified table, you need to set the information of the source database table to be migrated, which should be described in JSON string format. Below are examples.

For databases with a database-table structure:
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
For databases with a database-schema-table structure:
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]

This field does not need to be set when the entire instance is to be migrated
        :type DatabaseInfo: str
        :param _SrcNodeType: Source instance type. `simple`: Primary/Secondary node; `cluster`: Cluster node. If this field is left empty, the value defaults to primary/secondary node.
        :type SrcNodeType: str
        :param _SrcInfoMulti: Source instance information, which is correlated with the migration task type.
        :type SrcInfoMulti: list of SrcInfo
        """
        self._JobId = None
        self._JobName = None
        self._MigrateOption = None
        self._SrcAccessType = None
        self._SrcInfo = None
        self._DstAccessType = None
        self._DstInfo = None
        self._DatabaseInfo = None
        self._SrcNodeType = None
        self._SrcInfoMulti = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def MigrateOption(self):
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def SrcAccessType(self):
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstAccessType(self):
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DatabaseInfo(self):
        return self._DatabaseInfo

    @DatabaseInfo.setter
    def DatabaseInfo(self, DatabaseInfo):
        self._DatabaseInfo = DatabaseInfo

    @property
    def SrcNodeType(self):
        return self._SrcNodeType

    @SrcNodeType.setter
    def SrcNodeType(self, SrcNodeType):
        self._SrcNodeType = SrcNodeType

    @property
    def SrcInfoMulti(self):
        return self._SrcInfoMulti

    @SrcInfoMulti.setter
    def SrcInfoMulti(self, SrcInfoMulti):
        self._SrcInfoMulti = SrcInfoMulti


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        self._SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        self._DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._DatabaseInfo = params.get("DatabaseInfo")
        self._SrcNodeType = params.get("SrcNodeType")
        if params.get("SrcInfoMulti") is not None:
            self._SrcInfoMulti = []
            for item in params.get("SrcInfoMulti"):
                obj = SrcInfo()
                obj._deserialize(item)
                self._SrcInfoMulti.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobResponse(AbstractModel):
    """ModifyMigrateJob response structure.

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


class ModifySubscribeConsumeTimeRequest(AbstractModel):
    """ModifySubscribeConsumeTime request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _ConsumeStartTime: Consumption starting time point in the format of `Y-m-d h:m:s`, i.e., the starting time point for data subscription. Value range: within the last 24 hours
        :type ConsumeStartTime: str
        """
        self._SubscribeId = None
        self._ConsumeStartTime = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def ConsumeStartTime(self):
        return self._ConsumeStartTime

    @ConsumeStartTime.setter
    def ConsumeStartTime(self, ConsumeStartTime):
        self._ConsumeStartTime = ConsumeStartTime


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._ConsumeStartTime = params.get("ConsumeStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeConsumeTimeResponse(AbstractModel):
    """ModifySubscribeConsumeTime response structure.

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


class ModifySubscribeNameRequest(AbstractModel):
    """ModifySubscribeName request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _SubscribeName: Data subscription instance name. Length limit: [1,60]
        :type SubscribeName: str
        """
        self._SubscribeId = None
        self._SubscribeName = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeNameResponse(AbstractModel):
    """ModifySubscribeName response structure.

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


class ModifySubscribeObjectsRequest(AbstractModel):
    """ModifySubscribeObjects request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _SubscribeObjectType: Data subscription type. Valid values: 0 (full instance subscription), 1 (data subscription), 2 (structure subscription), 3 (data subscription + structure subscription)
        :type SubscribeObjectType: int
        :param _Objects: Information of subscribed table
        :type Objects: list of SubscribeObject
        """
        self._SubscribeId = None
        self._SubscribeObjectType = None
        self._Objects = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeObjectType(self):
        return self._SubscribeObjectType

    @SubscribeObjectType.setter
    def SubscribeObjectType(self, SubscribeObjectType):
        self._SubscribeObjectType = SubscribeObjectType

    @property
    def Objects(self):
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self._Objects = []
            for item in params.get("Objects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self._Objects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeObjectsResponse(AbstractModel):
    """ModifySubscribeObjects response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID
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


class ModifySubscribeVipVportRequest(AbstractModel):
    """ModifySubscribeVipVport request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _DstUniqSubnetId: Specified destination subnet. If this parameter is passed in, `DstIp` must be in the destination subnet
        :type DstUniqSubnetId: str
        :param _DstIp: Target IP. Either this field or `DstPort` must be passed in
        :type DstIp: str
        :param _DstPort: Target port. Value range: [1025-65535]
        :type DstPort: int
        """
        self._SubscribeId = None
        self._DstUniqSubnetId = None
        self._DstIp = None
        self._DstPort = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def DstUniqSubnetId(self):
        return self._DstUniqSubnetId

    @DstUniqSubnetId.setter
    def DstUniqSubnetId(self, DstUniqSubnetId):
        self._DstUniqSubnetId = DstUniqSubnetId

    @property
    def DstIp(self):
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def DstPort(self):
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._DstUniqSubnetId = params.get("DstUniqSubnetId")
        self._DstIp = params.get("DstIp")
        self._DstPort = params.get("DstPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeVipVportResponse(AbstractModel):
    """ModifySubscribeVipVport response structure.

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


class OfflineIsolatedSubscribeRequest(AbstractModel):
    """OfflineIsolatedSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineIsolatedSubscribeResponse(AbstractModel):
    """OfflineIsolatedSubscribe response structure.

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


class ResetSubscribeRequest(AbstractModel):
    """ResetSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetSubscribeResponse(AbstractModel):
    """ResetSubscribe response structure.

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


class SrcInfo(AbstractModel):
    """Source instance information

    """

    def __init__(self):
        r"""
        :param _AccessKey: Alibaba Cloud AccessKey, which is applicable if the source database is an Alibaba Cloud ApsaraDB for RDS 5.6 instance
        :type AccessKey: str
        :param _Ip: Instance IP address
        :type Ip: str
        :param _Port: Instance port
        :type Port: int
        :param _User: Instance username
        :type User: str
        :param _Password: Instance password
        :type Password: str
        :param _RdsInstanceId: Alibaba Cloud ApsaraDB for RDS instance ID, which is applicable if the source database is an Alibaba Cloud ApsaraDB for RDS 5.6/5.7 instance
        :type RdsInstanceId: str
        :param _CvmInstanceId: Short CVM instance ID in the format of `ins-olgl39y8`. It is the same as the instance ID displayed on the CVM Console page. For CVM-based self-created instances, this field needs to be passed in
        :type CvmInstanceId: str
        :param _UniqDcgId: Direct Connect gateway ID in the format of dcg-0rxtqqxb
        :type UniqDcgId: str
        :param _VpcId: VPC ID in the format of vpc-92jblxto
        :type VpcId: str
        :param _SubnetId: VPC Subnet ID in the format of subnet-3paxmkdz
        :type SubnetId: str
        :param _UniqVpnGwId: VPN gateway ID in the format of vpngw-9ghexg7q
        :type UniqVpnGwId: str
        :param _InstanceId: Database instance ID in the format of cdb-powiqx8q
        :type InstanceId: str
        :param _Region: Region name, such as ap-guangzhou
        :type Region: str
        :param _Supplier: For Alibaba Cloud ApsaraDB for RDS instances, enter "aliyun"; otherwise, enter "others"
        :type Supplier: str
        :param _CcnId: CCN instance ID, such as ccn-afp6kltc
Note: This field may return null, indicating that no valid values can be obtained.
        :type CcnId: str
        :param _EngineVersion: Database version. This parameter is valid only when the instance is an RDS instance. Value: 5.6 or 5.7. Default value: 5.6
        :type EngineVersion: str
        """
        self._AccessKey = None
        self._Ip = None
        self._Port = None
        self._User = None
        self._Password = None
        self._RdsInstanceId = None
        self._CvmInstanceId = None
        self._UniqDcgId = None
        self._VpcId = None
        self._SubnetId = None
        self._UniqVpnGwId = None
        self._InstanceId = None
        self._Region = None
        self._Supplier = None
        self._CcnId = None
        self._EngineVersion = None

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RdsInstanceId(self):
        return self._RdsInstanceId

    @RdsInstanceId.setter
    def RdsInstanceId(self, RdsInstanceId):
        self._RdsInstanceId = RdsInstanceId

    @property
    def CvmInstanceId(self):
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqDcgId(self):
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

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
    def UniqVpnGwId(self):
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

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

    @property
    def Supplier(self):
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion


    def _deserialize(self, params):
        self._AccessKey = params.get("AccessKey")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._RdsInstanceId = params.get("RdsInstanceId")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        self._Supplier = params.get("Supplier")
        self._CcnId = params.get("CcnId")
        self._EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob response structure.

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


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob response structure.

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


class SubsErr(AbstractModel):
    """Error message displayed when the subscription configuration was queried.

    """

    def __init__(self):
        r"""
        :param _Message: Error message.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Message: str
        """
        self._Message = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeInfo(AbstractModel):
    """Subscription instance information

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _SubscribeName: Data subscription instance name
        :type SubscribeName: str
        :param _ChannelId: ID of channel bound to data subscription instance
        :type ChannelId: str
        :param _Product: Name of product bound to data subscription instance
        :type Product: str
        :param _InstanceId: ID of database instance bound to data subscription instance
        :type InstanceId: str
        :param _InstanceStatus: Status of database instance bound to data subscription instance
        :type InstanceStatus: str
        :param _SubsStatus: Data subscription instance configuration status. Valid values: unconfigure, configuring, configured
        :type SubsStatus: str
        :param _ModifyTime: Last modified time
        :type ModifyTime: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _IsolateTime: Isolation time
        :type IsolateTime: str
        :param _ExpireTime: Expiration time
        :type ExpireTime: str
        :param _OfflineTime: Deactivation time
        :type OfflineTime: str
        :param _ConsumeStartTime: Last modified consumption starting time point. If it has never been modified, this field is 0
        :type ConsumeStartTime: str
        :param _Region: Data subscription instance region
        :type Region: str
        :param _PayType: Billing mode. 1: pay-as-you-go
        :type PayType: int
        :param _Vip: Data subscription instance VIP
        :type Vip: str
        :param _Vport: Data subscription instance Vport
        :type Vport: int
        :param _UniqVpcId: Unique ID of the VPC where the data subscription instance VIP resides
        :type UniqVpcId: str
        :param _UniqSubnetId: Unique ID of the subnet where the data subscription instance VIP resides
        :type UniqSubnetId: str
        :param _Status: Data subscription instance status. Valid values: creating, normal, isolating, isolated, offlining, offline
        :type Status: str
        :param _SdkConsumedTime: Timestamp of the last message confirmed by the SDK. If the SDK keeps consuming, this field can also be used as the current consumption time point of the SDK
        :type SdkConsumedTime: str
        :param _Tags: Tag
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param _AutoRenewFlag: Whether auto-renewal is enabled. 0: do not enable; 1: enable
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param _SubscribeVersion: Subscription instance edition. ·`txdts`: legacy data subscription; `kafka`: data subscription in Kafka edition
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SubscribeVersion: str
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._ChannelId = None
        self._Product = None
        self._InstanceId = None
        self._InstanceStatus = None
        self._SubsStatus = None
        self._ModifyTime = None
        self._CreateTime = None
        self._IsolateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._ConsumeStartTime = None
        self._Region = None
        self._PayType = None
        self._Vip = None
        self._Vport = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Status = None
        self._SdkConsumedTime = None
        self._Tags = None
        self._AutoRenewFlag = None
        self._SubscribeVersion = None

    @property
    def SubscribeId(self):
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SubsStatus(self):
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def ConsumeStartTime(self):
        return self._ConsumeStartTime

    @ConsumeStartTime.setter
    def ConsumeStartTime(self, ConsumeStartTime):
        self._ConsumeStartTime = ConsumeStartTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

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
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SdkConsumedTime(self):
        return self._SdkConsumedTime

    @SdkConsumedTime.setter
    def SdkConsumedTime(self, SdkConsumedTime):
        self._SdkConsumedTime = SdkConsumedTime

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
    def SubscribeVersion(self):
        return self._SubscribeVersion

    @SubscribeVersion.setter
    def SubscribeVersion(self, SubscribeVersion):
        self._SubscribeVersion = SubscribeVersion


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._ChannelId = params.get("ChannelId")
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._SubsStatus = params.get("SubsStatus")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._IsolateTime = params.get("IsolateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._ConsumeStartTime = params.get("ConsumeStartTime")
        self._Region = params.get("Region")
        self._PayType = params.get("PayType")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Status = params.get("Status")
        self._SdkConsumedTime = params.get("SdkConsumedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SubscribeVersion = params.get("SubscribeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeObject(AbstractModel):
    """Data subscription object

    """

    def __init__(self):
        r"""
        :param _ObjectsType: Data subscription object type. 0: database, 1: database table
Note: this field may return null, indicating that no valid values can be obtained.
        :type ObjectsType: int
        :param _DatabaseName: Name of subscribed database
Note: this field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param _TableNames: Array of table names in subscribed database
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableNames: list of str
        """
        self._ObjectsType = None
        self._DatabaseName = None
        self._TableNames = None

    @property
    def ObjectsType(self):
        return self._ObjectsType

    @ObjectsType.setter
    def ObjectsType(self, ObjectsType):
        self._ObjectsType = ObjectsType

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableNames(self):
        return self._TableNames

    @TableNames.setter
    def TableNames(self, TableNames):
        self._TableNames = TableNames


    def _deserialize(self, params):
        self._ObjectsType = params.get("ObjectsType")
        self._DatabaseName = params.get("DatabaseName")
        self._TableNames = params.get("TableNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeRegionConf(AbstractModel):
    """Sale information of data subscription region

    """

    def __init__(self):
        r"""
        :param _RegionName: Region name, such as Guangzhou
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionName: str
        :param _Region: Region ID, such as ap-guangzhou
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Area: Region name, such as South China
Note: this field may return null, indicating that no valid values can be obtained.
        :type Area: str
        :param _IsDefaultRegion: Whether it is the default region. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDefaultRegion: int
        :param _Status: Purchasable status of current region. 1: normal, 2: beta test, 3: not purchasable
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._RegionName = None
        self._Region = None
        self._Area = None
        self._IsDefaultRegion = None
        self._Status = None

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def IsDefaultRegion(self):
        return self._IsDefaultRegion

    @IsDefaultRegion.setter
    def IsDefaultRegion(self, IsDefaultRegion):
        self._IsDefaultRegion = IsDefaultRegion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RegionName = params.get("RegionName")
        self._Region = params.get("Region")
        self._Area = params.get("Area")
        self._IsDefaultRegion = params.get("IsDefaultRegion")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """Tag filtering

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key value
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: list of str
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
        


class TagItem(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key value
        :type TagKey: str
        :param _TagValue: Tag value
Note: this field may return `null`, indicating that no valid values can be obtained.
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
        