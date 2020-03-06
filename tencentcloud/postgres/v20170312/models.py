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


class AccountInfo(AbstractModel):
    """Account information

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-lnp6j617
        :type DBInstanceId: str
        :param UserName: Account
        :type UserName: str
        :param Remark: Account remarks
        :type Remark: str
        :param Status: Account status. 1: creating, 2: normal, 3: modifying, 4: resetting password, -1: deleting
        :type Status: int
        :param CreateTime: Account creation time
        :type CreateTime: str
        :param UpdateTime: Account last modified time
        :type UpdateTime: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Remark = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-6r233v55
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DBBackup(AbstractModel):
    """Database backup information

    """

    def __init__(self):
        """
        :param Id: Unique backup file ID
        :type Id: int
        :param StartTime: File generation start time
        :type StartTime: str
        :param EndTime: File generation end time
        :type EndTime: str
        :param Size: File size in KB
        :type Size: int
        :param Strategy: Policy (0: instance backup, 1: multi-database backup)
        :type Strategy: int
        :param Way: Type (0: scheduled)
        :type Way: int
        :param Type: Backup mode (1: full)
        :type Type: int
        :param Status: Status (1: creating, 2: success, 3: failure)
        :type Status: int
        :param DbList: DB list
        :type DbList: list of str
        :param InternalAddr: Download address on private network
        :type InternalAddr: str
        :param ExternalAddr: Download address on public network
        :type ExternalAddr: str
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Strategy = None
        self.Way = None
        self.Type = None
        self.Status = None
        self.DbList = None
        self.InternalAddr = None
        self.ExternalAddr = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Strategy = params.get("Strategy")
        self.Way = params.get("Way")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.DbList = params.get("DbList")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")


class DBInstance(AbstractModel):
    """Instance details

    """

    def __init__(self):
        """
        :param Region: Instance region such as ap-guangzhou, which corresponds to the `Region` field of `RegionSet`
        :type Region: str
        :param Zone: Instance AZ such as ap-guangzhou-3, which corresponds to the `Zone` field of `ZoneSet`
        :type Zone: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: SubnetId
        :type SubnetId: str
        :param DBInstanceId: Instance ID
        :type DBInstanceId: str
        :param DBInstanceName: Instance name
        :type DBInstanceName: str
        :param DBInstanceStatus: Instance status
        :type DBInstanceStatus: str
        :param DBInstanceMemory: Assigned instance memory size in GB
        :type DBInstanceMemory: int
        :param DBInstanceStorage: Assigned instance storage capacity in GB
        :type DBInstanceStorage: int
        :param DBInstanceCpu: Number of assigned CPUs
        :type DBInstanceCpu: int
        :param DBInstanceClass: Purchasable specification ID
        :type DBInstanceClass: str
        :param DBInstanceType: Instance type. 1: primary (master instance), 2: readonly (read-only instance), 3: guard (disaster recovery instance), 4: temp (temp instance)
        :type DBInstanceType: str
        :param DBInstanceVersion: Instance edition. Currently, only `standard` edition (dual-server high-availability one-master-one-slave edition) is supported
        :type DBInstanceVersion: str
        :param DBCharset: Instance database character set
        :type DBCharset: str
        :param DBVersion: PostgreSQL kernel version
        :type DBVersion: str
        :param CreateTime: Instance creation time
        :type CreateTime: str
        :param UpdateTime: Instance last modified time
        :type UpdateTime: str
        :param ExpireTime: Instance expiration time
        :type ExpireTime: str
        :param IsolatedTime: Instance isolation time
        :type IsolatedTime: str
        :param PayType: Billing mode. postpaid: pay-as-you-go
        :type PayType: str
        :param AutoRenew: Whether to renew automatically. 1: yes, 0: no
        :type AutoRenew: int
        :param DBInstanceNetInfo: Instance network connection information
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        :param Type: Machine type
        :type Type: str
        """
        self.Region = None
        self.Zone = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DBInstanceId = None
        self.DBInstanceName = None
        self.DBInstanceStatus = None
        self.DBInstanceMemory = None
        self.DBInstanceStorage = None
        self.DBInstanceCpu = None
        self.DBInstanceClass = None
        self.DBInstanceType = None
        self.DBInstanceVersion = None
        self.DBCharset = None
        self.DBVersion = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.PayType = None
        self.AutoRenew = None
        self.DBInstanceNetInfo = None
        self.Type = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceStatus = params.get("DBInstanceStatus")
        self.DBInstanceMemory = params.get("DBInstanceMemory")
        self.DBInstanceStorage = params.get("DBInstanceStorage")
        self.DBInstanceCpu = params.get("DBInstanceCpu")
        self.DBInstanceClass = params.get("DBInstanceClass")
        self.DBInstanceType = params.get("DBInstanceType")
        self.DBInstanceVersion = params.get("DBInstanceVersion")
        self.DBCharset = params.get("DBCharset")
        self.DBVersion = params.get("DBVersion")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.PayType = params.get("PayType")
        self.AutoRenew = params.get("AutoRenew")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)
        self.Type = params.get("Type")


class DBInstanceNetInfo(AbstractModel):
    """Instance network connection information

    """

    def __init__(self):
        """
        :param Address: DNS domain name
        :type Address: str
        :param Ip: Ip
        :type Ip: str
        :param Port: Connection port address
        :type Port: int
        :param NetType: Network type. 1: inner (private network address), 2: public (public network address)
        :type NetType: str
        :param Status: Network connection status
        :type Status: str
        """
        self.Address = None
        self.Ip = None
        self.Port = None
        self.NetType = None
        self.Status = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.NetType = params.get("NetType")
        self.Status = params.get("Status")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-6fego161
        :type DBInstanceId: str
        :param Limit: Number of entries returned per page. Default value: 20. Value range: 1–100.
        :type Limit: int
        :param Offset: Page number for data return in paged query. Pagination starts from 0
        :type Offset: int
        :param OrderBy: Whether to sort by creation time or username. Valid values: `createTime` (sort by creation time), `name` (sort by username)
        :type OrderBy: str
        :param OrderByType: Whether returns are sorted in ascending or descending order. Valid values: `desc` (descending), `asc` (ascending)
        :type OrderByType: str
        """
        self.DBInstanceId = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of date entries returned for this API call.
        :type TotalCount: int
        :param Details: Account list details.
        :type Details: list of AccountInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = AccountInfo()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-4wdeb0zv.
        :type DBInstanceId: str
        :param Type: Backup mode (1: full). Currently, only full backup is supported. The value is 1.
        :type Type: int
        :param StartTime: Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago
        :type StartTime: str
        :param EndTime: Query end time in the format of 2018-06-10 17:06:38
        :type EndTime: str
        :param Limit: Number of entries returned per page for backup list. Default value: 20. Minimum value: 1. Maximum value: 100.
        :type Limit: int
        :param Offset: Page number for data return in paged query. Pagination starts from 0. Default value: 0.
        :type Offset: int
        """
        self.DBInstanceId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDBBackupsResponse(AbstractModel):
    """DescribeDBBackups response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of backup files in the returned backup list
        :type TotalCount: int
        :param BackupList: Backup list
        :type BackupList: list of DBBackup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = DBBackup()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBErrlogsRequest(AbstractModel):
    """DescribeDBErrlogs request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-5bq3wfjd
        :type DBInstanceId: str
        :param StartTime: Query start time in the format of 2018-01-01 00:00:00, which cannot be more than 7 days ago
        :type StartTime: str
        :param EndTime: Query end time in the format of 2018-01-01 00:00:00
        :type EndTime: str
        :param DatabaseName: Database name
        :type DatabaseName: str
        :param SearchKeys: Search keyword
        :type SearchKeys: list of str
        :param Limit: Number of entries returned per page. Value range: 1–100
        :type Limit: int
        :param Offset: Page number for data return in paged query. Pagination starts from 0
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.SearchKeys = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.SearchKeys = params.get("SearchKeys")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDBErrlogsResponse(AbstractModel):
    """DescribeDBErrlogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of date entries returned for this call
        :type TotalCount: int
        :param Details: Error log list
        :type Details: list of ErrLogDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ErrLogDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceAttributeRequest(AbstractModel):
    """DescribeDBInstanceAttribute request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class DescribeDBInstanceAttributeResponse(AbstractModel):
    """DescribeDBInstanceAttribute response structure.

    """

    def __init__(self):
        """
        :param DBInstance: Instance details.
        :type DBInstance: :class:`tencentcloud.postgres.v20170312.models.DBInstance`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DBInstance = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DBInstance") is not None:
            self.DBInstance = DBInstance()
            self.DBInstance._deserialize(params.get("DBInstance"))
        self.RequestId = params.get("RequestId")


class DescribeDBSlowlogsRequest(AbstractModel):
    """DescribeDBSlowlogs request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-lnp6j617
        :type DBInstanceId: str
        :param StartTime: Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago
        :type StartTime: str
        :param EndTime: Query end time in the format of 2018-06-10 17:06:38
        :type EndTime: str
        :param DatabaseName: Database name
        :type DatabaseName: str
        :param OrderBy: Metric for sorting. Valid values: `sum_calls` (total number of calls), `sum_cost_time` (total time consumed)
        :type OrderBy: str
        :param OrderByType: Sorting order. desc: descending, asc: ascending
        :type OrderByType: str
        :param Limit: Number of entries returned per page. Value range: 1–100. Default value: 20.
        :type Limit: int
        :param Offset: Page number for data return in paged query. Pagination starts from 0
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.OrderBy = None
        self.OrderByType = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDBSlowlogsResponse(AbstractModel):
    """DescribeDBSlowlogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of date entries returned this time
        :type TotalCount: int
        :param Detail: Slow query log details
        :type Detail: :class:`tencentcloud.postgres.v20170312.models.SlowlogDetail`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Detail") is not None:
            self.Detail = SlowlogDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeDBXlogsRequest(AbstractModel):
    """DescribeDBXlogs request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-4wdeb0zv.
        :type DBInstanceId: str
        :param StartTime: Query start time in the format of 2018-06-10 17:06:38, which cannot be more than 7 days ago
        :type StartTime: str
        :param EndTime: Query end time in the format of 2018-06-10 17:06:38
        :type EndTime: str
        :param Offset: Page number for data return in paged query. Pagination starts from 0
        :type Offset: int
        :param Limit: Number of entries returned per page in paged query. Value range: 1–100.
        :type Limit: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDBXlogsResponse(AbstractModel):
    """DescribeDBXlogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of date entries returned this time.
        :type TotalCount: int
        :param XlogList: Xlog list
        :type XlogList: list of Xlog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.XlogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("XlogList") is not None:
            self.XlogList = []
            for item in params.get("XlogList"):
                obj = Xlog()
                obj._deserialize(item)
                self.XlogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders request structure.

    """

    def __init__(self):
        """
        :param DealNames: Order name set
        :type DealNames: list of str
        """
        self.DealNames = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of orders
        :type TotalCount: int
        :param Deals: Order array
        :type Deals: list of PgDeal
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Deals = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = PgDeal()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig request structure.

    """

    def __init__(self):
        """
        :param Zone: AZ name
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")


class DescribeProductConfigResponse(AbstractModel):
    """DescribeProductConfig response structure.

    """

    def __init__(self):
        """
        :param SpecInfoList: Purchasable specification list.
        :type SpecInfoList: list of SpecInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of returned results.
        :type TotalCount: int
        :param RegionSet: Region information set.
        :type RegionSet: list of RegionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of returned results.
        :type TotalCount: int
        :param ZoneSet: AZ information set.
        :type ZoneSet: list of ZoneInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class ErrLogDetail(AbstractModel):
    """Error log details

    """

    def __init__(self):
        """
        :param UserName: Username
        :type UserName: str
        :param Database: Database name
        :type Database: str
        :param ErrTime: Error occurrence time
        :type ErrTime: str
        :param ErrMsg: Error message
        :type ErrMsg: str
        """
        self.UserName = None
        self.Database = None
        self.ErrTime = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Database = params.get("Database")
        self.ErrTime = params.get("ErrTime")
        self.ErrMsg = params.get("ErrMsg")


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances request structure.

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: Instance ID set.
        :type DBInstanceIdSet: list of str
        :param AdminName: Instance admin account username.
        :type AdminName: str
        :param AdminPassword: Password corresponding to instance root account username.
        :type AdminPassword: str
        :param Charset: Instance character set. Valid values: UTF8, LATIN1.
        :type Charset: str
        """
        self.DBInstanceIdSet = None
        self.AdminName = None
        self.AdminPassword = None
        self.Charset = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.AdminName = params.get("AdminName")
        self.AdminPassword = params.get("AdminPassword")
        self.Charset = params.get("Charset")


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances response structure.

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: Instance ID set.
        :type DBInstanceIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeDBInstance request structure.

    """

    def __init__(self):
        """
        :param Storage: Instance disk size in GB
        :type Storage: int
        :param Memory: Instance memory size in GB
        :type Memory: int
        :param DBInstanceId: Instance ID in the format of postgres-hez4fh0v
        :type DBInstanceId: str
        :param InstanceChargeType: Instance billing type. Valid value: `POSTPAID_BY_HOUR` (pay-as-you-go hourly)
        :type InstanceChargeType: str
        """
        self.Storage = None
        self.Memory = None
        self.DBInstanceId = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.Storage = params.get("Storage")
        self.Memory = params.get("Memory")
        self.DBInstanceId = params.get("DBInstanceId")
        self.InstanceChargeType = params.get("InstanceChargeType")


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance response structure.

    """

    def __init__(self):
        """
        :param OriginalPrice: Total cost before discount.
        :type OriginalPrice: int
        :param Price: Actual amount payable
        :type Price: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class ModifyAccountRemarkRequest(AbstractModel):
    """ModifyAccountRemark request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-4wdeb0zv
        :type DBInstanceId: str
        :param UserName: Instance username
        :type UserName: str
        :param Remark: New remarks corresponding to user `UserName`
        :type Remark: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Remark = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")


class ModifyAccountRemarkResponse(AbstractModel):
    """ModifyAccountRemark response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Database instance ID in the format of postgres-6fego161
        :type DBInstanceId: str
        :param InstanceName: New name of database instance
        :type InstanceName: str
        """
        self.DBInstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.InstanceName = params.get("InstanceName")


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject request structure.

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: TencentDB for PostgreSQL instance ID array
        :type DBInstanceIdSet: list of str
        :param ProjectId: New project ID of TencentDB for PostgreSQL instance
        :type ProjectId: str
        """
        self.DBInstanceIdSet = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.ProjectId = params.get("ProjectId")


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject response structure.

    """

    def __init__(self):
        """
        :param Count: Number of successfully transferred instances
        :type Count: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class NormalQueryItem(AbstractModel):
    """Information of one SlowQuery

    """

    def __init__(self):
        """
        :param UserName: Username
        :type UserName: str
        :param Calls: Number of calls
        :type Calls: int
        :param CallsGrids: Granularity
        :type CallsGrids: list of int
        :param CostTime: Total time consumed
        :type CostTime: float
        :param Rows: Number of affected rows
        :type Rows: int
        :param MinCostTime: Minimum time consumed
        :type MinCostTime: float
        :param MaxCostTime: Maximum time consumed
        :type MaxCostTime: float
        :param FirstTime: Time of the earliest slow SQL statement
        :type FirstTime: str
        :param LastTime: Time of the latest slow SQL statement
        :type LastTime: str
        :param SharedReadBlks: Shared memory blocks for reads
        :type SharedReadBlks: int
        :param SharedWriteBlks: Shared memory blocks for writes
        :type SharedWriteBlks: int
        :param ReadCostTime: Total IO read time
        :type ReadCostTime: int
        :param WriteCostTime: Total IO write time
        :type WriteCostTime: int
        :param DatabaseName: Database name
        :type DatabaseName: str
        :param NormalQuery: Slow SQL statement after desensitization
        :type NormalQuery: str
        """
        self.UserName = None
        self.Calls = None
        self.CallsGrids = None
        self.CostTime = None
        self.Rows = None
        self.MinCostTime = None
        self.MaxCostTime = None
        self.FirstTime = None
        self.LastTime = None
        self.SharedReadBlks = None
        self.SharedWriteBlks = None
        self.ReadCostTime = None
        self.WriteCostTime = None
        self.DatabaseName = None
        self.NormalQuery = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Calls = params.get("Calls")
        self.CallsGrids = params.get("CallsGrids")
        self.CostTime = params.get("CostTime")
        self.Rows = params.get("Rows")
        self.MinCostTime = params.get("MinCostTime")
        self.MaxCostTime = params.get("MaxCostTime")
        self.FirstTime = params.get("FirstTime")
        self.LastTime = params.get("LastTime")
        self.SharedReadBlks = params.get("SharedReadBlks")
        self.SharedWriteBlks = params.get("SharedWriteBlks")
        self.ReadCostTime = params.get("ReadCostTime")
        self.WriteCostTime = params.get("WriteCostTime")
        self.DatabaseName = params.get("DatabaseName")
        self.NormalQuery = params.get("NormalQuery")


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-hez4fh0v
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class PgDeal(AbstractModel):
    """Order details

    """

    def __init__(self):
        """
        :param DealName: Order name
        :type DealName: str
        :param OwnerUin: User
        :type OwnerUin: str
        :param Count: Number of instances involved in order
        :type Count: int
        :param PayMode: Billing mode. 0: pay-as-you-go
        :type PayMode: int
        :param FlowId: Async task flow ID
        :type FlowId: int
        :param DBInstanceIdSet: Instance ID array
        :type DBInstanceIdSet: list of str
        """
        self.DealName = None
        self.OwnerUin = None
        self.Count = None
        self.PayMode = None
        self.FlowId = None
        self.DBInstanceIdSet = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.OwnerUin = params.get("OwnerUin")
        self.Count = params.get("Count")
        self.PayMode = params.get("PayMode")
        self.FlowId = params.get("FlowId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")


class RegionInfo(AbstractModel):
    """Region information such as number and status

    """

    def __init__(self):
        """
        :param Region: Region abbreviation
        :type Region: str
        :param RegionName: Region name
        :type RegionName: str
        :param RegionId: Region number
        :type RegionId: int
        :param RegionState: Availability status. UNAVAILABLE: unavailable, AVAILABLE: available
        :type RegionState: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionState = params.get("RegionState")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-4wdeb0zv
        :type DBInstanceId: str
        :param UserName: Instance account name
        :type UserName: str
        :param Password: New password corresponding to `UserName` account
        :type Password: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance request structure.

    """

    def __init__(self):
        """
        :param DBInstanceId: Instance ID in the format of postgres-6r233v55
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class RestartDBInstanceResponse(AbstractModel):
    """RestartDBInstance response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class SlowlogDetail(AbstractModel):
    """Slow query details

    """

    def __init__(self):
        """
        :param TotalTime: Total time consumed
        :type TotalTime: float
        :param TotalCalls: Total number of calls
        :type TotalCalls: int
        :param NormalQueries: List of slow SQL statements after desensitization
        :type NormalQueries: list of NormalQueryItem
        """
        self.TotalTime = None
        self.TotalCalls = None
        self.NormalQueries = None


    def _deserialize(self, params):
        self.TotalTime = params.get("TotalTime")
        self.TotalCalls = params.get("TotalCalls")
        if params.get("NormalQueries") is not None:
            self.NormalQueries = []
            for item in params.get("NormalQueries"):
                obj = NormalQueryItem()
                obj._deserialize(item)
                self.NormalQueries.append(obj)


class SpecInfo(AbstractModel):
    """Purchasable specification details in an AZ in a region.

    """

    def __init__(self):
        """
        :param Region: Region abbreviation, which corresponds to the `Region` field of `RegionSet`
        :type Region: str
        :param Zone: AZ abbreviate, which corresponds to the `Zone` field of `ZoneSet`
        :type Zone: str
        :param SpecItemInfoList: Specification details list
        :type SpecItemInfoList: list of SpecItemInfo
        """
        self.Region = None
        self.Zone = None
        self.SpecItemInfoList = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItemInfoList") is not None:
            self.SpecItemInfoList = []
            for item in params.get("SpecItemInfoList"):
                obj = SpecItemInfo()
                obj._deserialize(item)
                self.SpecItemInfoList.append(obj)


class SpecItemInfo(AbstractModel):
    """Specification information

    """

    def __init__(self):
        """
        :param SpecCode: Specification ID
        :type SpecCode: str
        :param Version: PostgreSQL kernel version number
        :type Version: str
        :param VersionName: Full version name corresponding to kernel number
        :type VersionName: str
        :param Cpu: Number of CPU cores
        :type Cpu: int
        :param Memory: Memory size in MB
        :type Memory: int
        :param MaxStorage: Maximum storage capacity in GB supported by this specification
        :type MaxStorage: int
        :param MinStorage: Minimum storage capacity in GB supported by this specification
        :type MinStorage: int
        :param Qps: Estimated QPS for this specification
        :type Qps: int
        :param Pid: Billing ID for this specification
        :type Pid: int
        :param Type: Machine type
        :type Type: str
        """
        self.SpecCode = None
        self.Version = None
        self.VersionName = None
        self.Cpu = None
        self.Memory = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Pid = None
        self.Type = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Version = params.get("Version")
        self.VersionName = params.get("VersionName")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Pid = params.get("Pid")
        self.Type = params.get("Type")


class Xlog(AbstractModel):
    """Database Xlog information

    """

    def __init__(self):
        """
        :param Id: Unique backup file ID
        :type Id: int
        :param StartTime: File generation start time
        :type StartTime: str
        :param EndTime: File generation end time
        :type EndTime: str
        :param InternalAddr: Download address on private network
        :type InternalAddr: str
        :param ExternalAddr: Download address on public network
        :type ExternalAddr: str
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.InternalAddr = None
        self.ExternalAddr = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")


class ZoneInfo(AbstractModel):
    """AZ information such as number and status

    """

    def __init__(self):
        """
        :param Zone: AZ abbreviation
        :type Zone: str
        :param ZoneName: AZ name
        :type ZoneName: str
        :param ZoneId: AZ number
        :type ZoneId: int
        :param ZoneState: Availability status. UNAVAILABLE: unavailable, AVAILABLE: available
        :type ZoneState: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.ZoneState = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")