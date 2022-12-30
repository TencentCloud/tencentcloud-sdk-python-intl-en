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


class BackingIndexMetaField(AbstractModel):
    """Backing index metadata fields

    """

    def __init__(self):
        r"""
        :param IndexName: Backing index name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexName: str
        :param IndexStatus: Backing index status
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexStatus: str
        :param IndexStorage: Backing index size
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexStorage: int
        :param IndexPhrase: Current lifecycle phase of backing index
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexPhrase: str
        :param IndexCreateTime: Backing index creation time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexCreateTime: str
        """
        self.IndexName = None
        self.IndexStatus = None
        self.IndexStorage = None
        self.IndexPhrase = None
        self.IndexCreateTime = None


    def _deserialize(self, params):
        self.IndexName = params.get("IndexName")
        self.IndexStatus = params.get("IndexStatus")
        self.IndexStorage = params.get("IndexStorage")
        self.IndexPhrase = params.get("IndexPhrase")
        self.IndexCreateTime = params.get("IndexCreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterView(AbstractModel):
    """Cluster view data

    """

    def __init__(self):
        r"""
        :param Health: Cluster health status
        :type Health: float
        :param Visible: Whether the cluster is visible
        :type Visible: float
        :param Break: Whether the cluster encounters circuit breaking
        :type Break: float
        :param AvgDiskUsage: Average disk usage
        :type AvgDiskUsage: float
        :param AvgMemUsage: Average memory usage
        :type AvgMemUsage: float
        :param AvgCpuUsage: Average CPU usage
        :type AvgCpuUsage: float
        :param TotalDiskSize: Total disk size of the cluster
        :type TotalDiskSize: int
        :param TargetNodeTypes: Types of nodes to receive client requests
        :type TargetNodeTypes: list of str
        :param NodeNum: Number of online nodes
        :type NodeNum: int
        :param TotalNodeNum: Total number of nodes
        :type TotalNodeNum: int
        :param DataNodeNum: Number of data nodes
        :type DataNodeNum: int
        :param IndexNum: Number of indices
        :type IndexNum: int
        :param DocNum: Number of documents
        :type DocNum: int
        :param DiskUsedInBytes: Used disk size (in bytes)
        :type DiskUsedInBytes: int
        :param ShardNum: Number of shards
        :type ShardNum: int
        :param PrimaryShardNum: Number of primary shards
        :type PrimaryShardNum: int
        :param RelocatingShardNum: Number of relocating shards
        :type RelocatingShardNum: int
        :param InitializingShardNum: Number of initializing shards
        :type InitializingShardNum: int
        :param UnassignedShardNum: Number of unassigned shards
        :type UnassignedShardNum: int
        :param TotalCosStorage: Total COS storage of an enterprise cluster, in GB
        :type TotalCosStorage: int
        :param SearchableSnapshotCosBucket: Name of the COS bucket that stores searchable snapshots of an enterprise cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type SearchableSnapshotCosBucket: str
        :param SearchableSnapshotCosAppId: COS app ID of the searchable snapshots of an enterprise cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type SearchableSnapshotCosAppId: str
        """
        self.Health = None
        self.Visible = None
        self.Break = None
        self.AvgDiskUsage = None
        self.AvgMemUsage = None
        self.AvgCpuUsage = None
        self.TotalDiskSize = None
        self.TargetNodeTypes = None
        self.NodeNum = None
        self.TotalNodeNum = None
        self.DataNodeNum = None
        self.IndexNum = None
        self.DocNum = None
        self.DiskUsedInBytes = None
        self.ShardNum = None
        self.PrimaryShardNum = None
        self.RelocatingShardNum = None
        self.InitializingShardNum = None
        self.UnassignedShardNum = None
        self.TotalCosStorage = None
        self.SearchableSnapshotCosBucket = None
        self.SearchableSnapshotCosAppId = None


    def _deserialize(self, params):
        self.Health = params.get("Health")
        self.Visible = params.get("Visible")
        self.Break = params.get("Break")
        self.AvgDiskUsage = params.get("AvgDiskUsage")
        self.AvgMemUsage = params.get("AvgMemUsage")
        self.AvgCpuUsage = params.get("AvgCpuUsage")
        self.TotalDiskSize = params.get("TotalDiskSize")
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        self.NodeNum = params.get("NodeNum")
        self.TotalNodeNum = params.get("TotalNodeNum")
        self.DataNodeNum = params.get("DataNodeNum")
        self.IndexNum = params.get("IndexNum")
        self.DocNum = params.get("DocNum")
        self.DiskUsedInBytes = params.get("DiskUsedInBytes")
        self.ShardNum = params.get("ShardNum")
        self.PrimaryShardNum = params.get("PrimaryShardNum")
        self.RelocatingShardNum = params.get("RelocatingShardNum")
        self.InitializingShardNum = params.get("InitializingShardNum")
        self.UnassignedShardNum = params.get("UnassignedShardNum")
        self.TotalCosStorage = params.get("TotalCosStorage")
        self.SearchableSnapshotCosBucket = params.get("SearchableSnapshotCosBucket")
        self.SearchableSnapshotCosAppId = params.get("SearchableSnapshotCosAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosBackup(AbstractModel):
    """Auto-backup to COS for ES

    """

    def __init__(self):
        r"""
        :param IsAutoBackup: Whether to enable auto-backup to COS
        :type IsAutoBackup: bool
        :param BackupTime: Auto-backup time (accurate down to the hour), such as "22:00"
        :type BackupTime: str
        """
        self.IsAutoBackup = None
        self.BackupTime = None


    def _deserialize(self, params):
        self.IsAutoBackup = params.get("IsAutoBackup")
        self.BackupTime = params.get("BackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexRequest(AbstractModel):
    """CreateIndex request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ES cluster ID
        :type InstanceId: str
        :param IndexType: Type of the index to create. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param IndexName: Name of the index to create
        :type IndexName: str
        :param IndexMetaJson: JSON-formatted index metadata to create, such as `mappings` and `settings`
        :type IndexMetaJson: str
        :param Username: Username for cluster access
        :type Username: str
        :param Password: Password for cluster access
        :type Password: str
        """
        self.InstanceId = None
        self.IndexType = None
        self.IndexName = None
        self.IndexMetaJson = None
        self.Username = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.IndexMetaJson = params.get("IndexMetaJson")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexResponse(AbstractModel):
    """CreateIndex response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance request structure.

    """

    def __init__(self):
        r"""
        :param Zone: Availability Zone
        :type Zone: str
        :param EsVersion: Instance version. Valid values: `5.6.4`, `6.4.3`, `6.8.2`, `7.5.1`, `7.10.1`
        :type EsVersion: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param Password: Access password, which must contain 8 to 16 characters, and include at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]
        :type Password: str
        :param InstanceName: Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)
        :type InstanceName: str
        :param NodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2-50)
        :type NodeNum: int
        :param ChargeType: Billing mode <li>POSTPAID_BY_HOUR: Pay-as-you-go hourly </li>Default value: POSTPAID_BY_HOUR
        :type ChargeType: str
        :param ChargePeriod: This parameter is not used on the global website
        :type ChargePeriod: int
        :param RenewFlag: This parameter is not used on the global website
        :type RenewFlag: str
        :param NodeType: This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param DiskType: This parameter has been disused. Please use `NodeInfoList`
Node storage type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: premium cloud storage </li>Default value: CLOUD_SSD
        :type DiskType: str
        :param DiskSize: This parameter has been disused. Please use `NodeInfoList`
Node disk size in GB
        :type DiskSize: int
        :param TimeUnit: This parameter is not used on the global website
        :type TimeUnit: str
        :param AutoVoucher: Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0
        :type AutoVoucher: int
        :param VoucherIds: List of voucher IDs (only one voucher can be specified at a time currently)
        :type VoucherIds: list of str
        :param EnableDedicatedMaster: This parameter has been disused. Please use `NodeInfoList`
Whether to create a dedicated primary node <li>true: yes </li><li>false: no </li>Default value: false
        :type EnableDedicatedMaster: bool
        :param MasterNodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of dedicated primary nodes (only 3 and 5 are supported. This value must be passed in if `EnableDedicatedMaster` is `true`)
        :type MasterNodeNum: int
        :param MasterNodeType: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node type, which must be passed in if `EnableDedicatedMaster` is `true` <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :type MasterNodeType: str
        :param MasterNodeDiskSize: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node disk size in GB, which is optional. If passed in, it can only be 50 and cannot be customized currently
        :type MasterNodeDiskSize: int
        :param ClusterNameInConf: ClusterName in the cluster configuration file, which is the instance ID by default and currently cannot be customized
        :type ClusterNameInConf: str
        :param DeployMode: Cluster deployment mode <li>0: single-AZ deployment </li><li>1: multi-AZ deployment </li>Default value: 0
        :type DeployMode: int
        :param MultiZoneInfo: Details of AZs in multi-AZ deployment mode (which is required when DeployMode is 1)
        :type MultiZoneInfo: list of ZoneDetail
        :param LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :type LicenseType: str
        :param NodeInfoList: Node information list, which is used to describe the specification information of various types of nodes in the cluster, such as node type, node quantity, node specification, disk type, and disk size
        :type NodeInfoList: list of NodeInfo
        :param TagList: Node tag information list
        :type TagList: list of TagInfo
        :param BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :type BasicSecurityType: int
        :param SceneType: Scenario template type. 0: not enabled; 1: general; 2: log; 3: search
        :type SceneType: int
        :param WebNodeTypeInfo: Visual node configuration
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param Protocol: Valid values: `https`, `http` (default)
        :type Protocol: str
        :param OperationDuration: The maintenance time slot
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param EnableHybridStorage: Whether to enable the storage-computing separation feature.
        :type EnableHybridStorage: bool
        :param DiskEnhance: Whether to enable enhanced SSD
        :type DiskEnhance: int
        """
        self.Zone = None
        self.EsVersion = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.InstanceName = None
        self.NodeNum = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.DiskType = None
        self.DiskSize = None
        self.TimeUnit = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.EnableDedicatedMaster = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ClusterNameInConf = None
        self.DeployMode = None
        self.MultiZoneInfo = None
        self.LicenseType = None
        self.NodeInfoList = None
        self.TagList = None
        self.BasicSecurityType = None
        self.SceneType = None
        self.WebNodeTypeInfo = None
        self.Protocol = None
        self.OperationDuration = None
        self.EnableHybridStorage = None
        self.DiskEnhance = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.EsVersion = params.get("EsVersion")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ClusterNameInConf = params.get("ClusterNameInConf")
        self.DeployMode = params.get("DeployMode")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.LicenseType = params.get("LicenseType")
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.SceneType = params.get("SceneType")
        if params.get("WebNodeTypeInfo") is not None:
            self.WebNodeTypeInfo = WebNodeTypeInfo()
            self.WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self.Protocol = params.get("Protocol")
        if params.get("OperationDuration") is not None:
            self.OperationDuration = OperationDuration()
            self.OperationDuration._deserialize(params.get("OperationDuration"))
        self.EnableHybridStorage = params.get("EnableHybridStorage")
        self.DiskEnhance = params.get("DiskEnhance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance response structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DealName: Order ID
Note: This field may return `null`, indicating that no valid value was found.
        :type DealName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class DeleteIndexRequest(AbstractModel):
    """DeleteIndex request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ES cluster ID
        :type InstanceId: str
        :param IndexType: Type of the index to delete. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param IndexName: Name of the index to delete
        :type IndexName: str
        :param Username: Username for cluster access
        :type Username: str
        :param Password: Password for cluster access
        :type Password: str
        :param BackingIndexName: Backing index name
        :type BackingIndexName: str
        """
        self.InstanceId = None
        self.IndexType = None
        self.IndexName = None
        self.Username = None
        self.Password = None
        self.BackingIndexName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.BackingIndexName = params.get("BackingIndexName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIndexResponse(AbstractModel):
    """DeleteIndex response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeIndexListRequest(AbstractModel):
    """DescribeIndexList request structure.

    """

    def __init__(self):
        r"""
        :param IndexType: Index type. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param InstanceId: ES cluster ID
        :type InstanceId: str
        :param IndexName: Index name. `null` indicates that all indexes are requested.
        :type IndexName: str
        :param Username: Username for cluster access
        :type Username: str
        :param Password: Password for cluster access
        :type Password: str
        :param Offset: The starting position of paging
        :type Offset: int
        :param Limit: The number of results per page
        :type Limit: int
        :param OrderBy: Sorting condition field, which can be `IndexName`, `IndexStorage`, or `IndexCreateTime`.
        :type OrderBy: str
        :param IndexStatusList: Filtering by index status
        :type IndexStatusList: list of str
        :param Order: Sorting mode, which can be `asc` and `desc`.
        :type Order: str
        """
        self.IndexType = None
        self.InstanceId = None
        self.IndexName = None
        self.Username = None
        self.Password = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.IndexStatusList = None
        self.Order = None


    def _deserialize(self, params):
        self.IndexType = params.get("IndexType")
        self.InstanceId = params.get("InstanceId")
        self.IndexName = params.get("IndexName")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.IndexStatusList = params.get("IndexStatusList")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexListResponse(AbstractModel):
    """DescribeIndexList response structure.

    """

    def __init__(self):
        r"""
        :param IndexMetaFields: Index metadata field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexMetaFields: list of IndexMetaField
        :param TotalCount: Total number of results
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IndexMetaFields = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IndexMetaFields") is not None:
            self.IndexMetaFields = []
            for item in params.get("IndexMetaFields"):
                obj = IndexMetaField()
                obj._deserialize(item)
                self.IndexMetaFields.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIndexMetaRequest(AbstractModel):
    """DescribeIndexMeta request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ES cluster ID
        :type InstanceId: str
        :param IndexType: Index type. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param IndexName: Index name. `null` indicates that all indexes are requested.
        :type IndexName: str
        :param Username: Username for cluster access
        :type Username: str
        :param Password: Password for cluster access
        :type Password: str
        """
        self.InstanceId = None
        self.IndexType = None
        self.IndexName = None
        self.Username = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexMetaResponse(AbstractModel):
    """DescribeIndexMeta response structure.

    """

    def __init__(self):
        r"""
        :param IndexMetaField: Index metadata field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexMetaField: :class:`tencentcloud.es.v20180416.models.IndexMetaField`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IndexMetaField = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IndexMetaField") is not None:
            self.IndexMetaField = IndexMetaField()
            self.IndexMetaField._deserialize(params.get("IndexMetaField"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    """DescribeInstanceLogs request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Cluster instance ID
        :type InstanceId: str
        :param LogType: Log type. Default value: 1
<li>1: primary log</li>
<li>2: search slow log</li>
<li>3: index slow log</li>
<li>4: GC log</li>
        :type LogType: int
        :param SearchKey: Search keyword, which supports LUCENE syntax, such as `level:WARN`, `ip:1.1.1.1`, and `message:test-index`
        :type SearchKey: str
        :param StartTime: Log start time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53
        :type StartTime: str
        :param EndTime: Log end time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53
        :type EndTime: str
        :param Offset: Pagination start value. Default value: 0
        :type Offset: int
        :param Limit: Number of entries per page. Default value: 100. Maximum value: 100
        :type Limit: int
        :param OrderByType: Time sorting order. Default value: 0
<li>0: descending</li>
<li>1: ascending</li>
        :type OrderByType: int
        """
        self.InstanceId = None
        self.LogType = None
        self.SearchKey = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LogType = params.get("LogType")
        self.SearchKey = params.get("SearchKey")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogsResponse(AbstractModel):
    """DescribeInstanceLogs response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of returned logs
        :type TotalCount: int
        :param InstanceLogList: Log details list
        :type InstanceLogList: list of InstanceLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceLogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceLogList") is not None:
            self.InstanceLogList = []
            for item in params.get("InstanceLogList"):
                obj = InstanceLog()
                obj._deserialize(item)
                self.InstanceLogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    """DescribeInstanceOperations request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Cluster instance ID
        :type InstanceId: str
        :param StartTime: Start time, such as "2019-03-07 16:30:39"
        :type StartTime: str
        :param EndTime: End time, such as "2019-03-30 20:18:03"
        :type EndTime: str
        :param Offset: Pagination start value
        :type Offset: int
        :param Limit: Number of entries per page
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
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
        


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of operation records
        :type TotalCount: int
        :param Operations: Operation history
        :type Operations: list of Operation
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Operations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self.Operations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param Zone: AZ of the cluster instance. If this is not passed in, all AZs are used by default
        :type Zone: str
        :param InstanceIds: List of cluster instance IDs
        :type InstanceIds: list of str
        :param InstanceNames: List of cluster instance names
        :type InstanceNames: list of str
        :param Offset: Pagination start value. Default value: 0
        :type Offset: int
        :param Limit: Number of entries per page. Default value: 20
        :type Limit: int
        :param OrderByKey: The sorting field. <li>1: Instance ID </li><li>2: Instance name </li><li>3: AZ </li><li>4: Creation time </li>If `OrderByKey` is not passed in, sorting is performed by creation time in descending order.
        :type OrderByKey: int
        :param OrderByType: Sorting order <li>0: ascending </li><li>1: descending </li>If orderByKey is passed in but orderByType is not, ascending order is used by default
        :type OrderByType: int
        :param TagList: Node tag information list
        :type TagList: list of TagInfo
        :param IpList: VPC VIP list
        :type IpList: list of str
        :param ZoneList: List of availability zones
        :type ZoneList: list of str
        :param HealthStatus: The health status filter. Valid values: `0` (green), `1` (yellow), `2` (red), `-1` (unknown).
        :type HealthStatus: list of int
        :param VpcIds: VPC IDs
        :type VpcIds: list of str
        """
        self.Zone = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.Offset = None
        self.Limit = None
        self.OrderByKey = None
        self.OrderByType = None
        self.TagList = None
        self.IpList = None
        self.ZoneList = None
        self.HealthStatus = None
        self.VpcIds = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByKey = params.get("OrderByKey")
        self.OrderByType = params.get("OrderByType")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.IpList = params.get("IpList")
        self.ZoneList = params.get("ZoneList")
        self.HealthStatus = params.get("HealthStatus")
        self.VpcIds = params.get("VpcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of returned instances
        :type TotalCount: int
        :param InstanceList: List of instance details
        :type InstanceList: list of InstanceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeViewsRequest(AbstractModel):
    """DescribeViews request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Cluster instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeViewsResponse(AbstractModel):
    """DescribeViews response structure.

    """

    def __init__(self):
        r"""
        :param ClusterView: Cluster view
Note: This field may return `null`, indicating that no valid value was found.
        :type ClusterView: :class:`tencentcloud.es.v20180416.models.ClusterView`
        :param NodesView: Node view
Note: This field may return `null`, indicating that no valid value was found.
        :type NodesView: list of NodeView
        :param KibanasView: Kibana view
Note: This field may return `null`, indicating that no valid value was found.
        :type KibanasView: list of KibanaView
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterView = None
        self.NodesView = None
        self.KibanasView = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterView") is not None:
            self.ClusterView = ClusterView()
            self.ClusterView._deserialize(params.get("ClusterView"))
        if params.get("NodesView") is not None:
            self.NodesView = []
            for item in params.get("NodesView"):
                obj = NodeView()
                obj._deserialize(item)
                self.NodesView.append(obj)
        if params.get("KibanasView") is not None:
            self.KibanasView = []
            for item in params.get("KibanasView"):
                obj = KibanaView()
                obj._deserialize(item)
                self.KibanasView.append(obj)
        self.RequestId = params.get("RequestId")


class DictInfo(AbstractModel):
    """Information of the IK plugin dictionary

    """

    def __init__(self):
        r"""
        :param Key: Dictionary key value
        :type Key: str
        :param Name: Dictionary name
        :type Name: str
        :param Size: Dictionary size in B
        :type Size: int
        """
        self.Key = None
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsAcl(AbstractModel):
    """ES cluster configuration item

    """

    def __init__(self):
        r"""
        :param BlackIpList: Kibana access blocklist
        :type BlackIpList: list of str
        :param WhiteIpList: Kibana access allowlist
        :type WhiteIpList: list of str
        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsConfigSetInfo(AbstractModel):
    """Configuration set information

    """

    def __init__(self):
        r"""
        :param Type: Configuration set type, such as `LDAP` and `AD`.
        :type Type: str
        :param EsConfig: "{\"order\":0,\"url\":\"ldap://10.0.1.72:389\",\"bind_dn\":\"cn=admin,dc=tencent,dc=com\",\"user_search.base_dn\":\"dc=tencent,dc=com\",\"user_search.filter\":\"(cn={0})\",\"group_search.base_dn\":\"dc=tencent,dc=com\"}"
        :type EsConfig: str
        """
        self.Type = None
        self.EsConfig = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.EsConfig = params.get("EsConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsDictionaryInfo(AbstractModel):
    """ES dictionary information

    """

    def __init__(self):
        r"""
        :param MainDict: List of non-stop words
        :type MainDict: list of DictInfo
        :param Stopwords: List of stop words
        :type Stopwords: list of DictInfo
        :param QQDict: QQ dictionary list
        :type QQDict: list of DictInfo
        :param Synonym: Synonym dictionary list
        :type Synonym: list of DictInfo
        :param UpdateType: Update dictionary type
        :type UpdateType: str
        """
        self.MainDict = None
        self.Stopwords = None
        self.QQDict = None
        self.Synonym = None
        self.UpdateType = None


    def _deserialize(self, params):
        if params.get("MainDict") is not None:
            self.MainDict = []
            for item in params.get("MainDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self.MainDict.append(obj)
        if params.get("Stopwords") is not None:
            self.Stopwords = []
            for item in params.get("Stopwords"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Stopwords.append(obj)
        if params.get("QQDict") is not None:
            self.QQDict = []
            for item in params.get("QQDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self.QQDict.append(obj)
        if params.get("Synonym") is not None:
            self.Synonym = []
            for item in params.get("Synonym"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Synonym.append(obj)
        self.UpdateType = params.get("UpdateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsPublicAcl(AbstractModel):
    """Public network ACL information of ES

    """

    def __init__(self):
        r"""
        :param BlackIpList: Access blocklist
        :type BlackIpList: list of str
        :param WhiteIpList: Access allowlist
        :type WhiteIpList: list of str
        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesRequest(AbstractModel):
    """GetRequestTargetNodeTypes request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesResponse(AbstractModel):
    """GetRequestTargetNodeTypes response structure.

    """

    def __init__(self):
        r"""
        :param TargetNodeTypes: A list of node types used to receive requests.
        :type TargetNodeTypes: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TargetNodeTypes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        self.RequestId = params.get("RequestId")


class IndexMetaField(AbstractModel):
    """Index metadata field

    """

    def __init__(self):
        r"""
        :param IndexType: Index type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexType: str
        :param IndexName: Index name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexName: str
        :param IndexStatus: Index status
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexStatus: str
        :param IndexStorage: Index size (in byte)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexStorage: int
        :param IndexCreateTime: Index creation time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexCreateTime: str
        :param BackingIndices: Backing index
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BackingIndices: list of BackingIndexMetaField
        :param ClusterId: Cluster ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterId: str
        :param ClusterName: Cluster name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterName: str
        :param ClusterVersion: Cluster version
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterVersion: str
        :param IndexPolicyField: Index lifecycle policy field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexPolicyField: :class:`tencentcloud.es.v20180416.models.IndexPolicyField`
        :param IndexOptionsField: Index automation field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexOptionsField: :class:`tencentcloud.es.v20180416.models.IndexOptionsField`
        :param IndexSettingsField: Index setting field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexSettingsField: :class:`tencentcloud.es.v20180416.models.IndexSettingsField`
        :param AppId: Cluster APP ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AppId: int
        :param IndexDocs: The number of index docs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndexDocs: int
        """
        self.IndexType = None
        self.IndexName = None
        self.IndexStatus = None
        self.IndexStorage = None
        self.IndexCreateTime = None
        self.BackingIndices = None
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterVersion = None
        self.IndexPolicyField = None
        self.IndexOptionsField = None
        self.IndexSettingsField = None
        self.AppId = None
        self.IndexDocs = None


    def _deserialize(self, params):
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.IndexStatus = params.get("IndexStatus")
        self.IndexStorage = params.get("IndexStorage")
        self.IndexCreateTime = params.get("IndexCreateTime")
        if params.get("BackingIndices") is not None:
            self.BackingIndices = []
            for item in params.get("BackingIndices"):
                obj = BackingIndexMetaField()
                obj._deserialize(item)
                self.BackingIndices.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterVersion = params.get("ClusterVersion")
        if params.get("IndexPolicyField") is not None:
            self.IndexPolicyField = IndexPolicyField()
            self.IndexPolicyField._deserialize(params.get("IndexPolicyField"))
        if params.get("IndexOptionsField") is not None:
            self.IndexOptionsField = IndexOptionsField()
            self.IndexOptionsField._deserialize(params.get("IndexOptionsField"))
        if params.get("IndexSettingsField") is not None:
            self.IndexSettingsField = IndexSettingsField()
            self.IndexSettingsField._deserialize(params.get("IndexSettingsField"))
        self.AppId = params.get("AppId")
        self.IndexDocs = params.get("IndexDocs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexOptionsField(AbstractModel):
    """Index automation field

    """

    def __init__(self):
        r"""
        :param ExpireMaxAge: Max age for expiry purpose
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireMaxAge: str
        :param ExpireMaxSize: Max size for expiry purpose
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireMaxSize: str
        :param RolloverMaxAge: Rollover cycle
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RolloverMaxAge: str
        :param RolloverDynamic: Whether to enable the dynamic rollover
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RolloverDynamic: str
        :param ShardNumDynamic: Whether to enable dynamic sharding
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ShardNumDynamic: str
        :param TimestampField: Timestamp field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TimestampField: str
        :param WriteMode: Write mode
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WriteMode: str
        """
        self.ExpireMaxAge = None
        self.ExpireMaxSize = None
        self.RolloverMaxAge = None
        self.RolloverDynamic = None
        self.ShardNumDynamic = None
        self.TimestampField = None
        self.WriteMode = None


    def _deserialize(self, params):
        self.ExpireMaxAge = params.get("ExpireMaxAge")
        self.ExpireMaxSize = params.get("ExpireMaxSize")
        self.RolloverMaxAge = params.get("RolloverMaxAge")
        self.RolloverDynamic = params.get("RolloverDynamic")
        self.ShardNumDynamic = params.get("ShardNumDynamic")
        self.TimestampField = params.get("TimestampField")
        self.WriteMode = params.get("WriteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexPolicyField(AbstractModel):
    """Index lifecycle policy field

    """

    def __init__(self):
        r"""
        :param WarmEnable: Whether to enable the warm phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WarmEnable: str
        :param WarmMinAge: Min age before data transitions to the warm phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WarmMinAge: str
        :param ColdEnable: Whether to enable the cold phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ColdEnable: str
        :param ColdMinAge: Min age before data transitions to the cold phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ColdMinAge: str
        :param FrozenEnable: Whether to enable the frozen phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FrozenEnable: str
        :param FrozenMinAge: Min age before data transitions to the frozen phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FrozenMinAge: str
        :param ColdAction: /
Note: This field may return null, indicating that no valid value can be obtained.
        :type ColdAction: str
        """
        self.WarmEnable = None
        self.WarmMinAge = None
        self.ColdEnable = None
        self.ColdMinAge = None
        self.FrozenEnable = None
        self.FrozenMinAge = None
        self.ColdAction = None


    def _deserialize(self, params):
        self.WarmEnable = params.get("WarmEnable")
        self.WarmMinAge = params.get("WarmMinAge")
        self.ColdEnable = params.get("ColdEnable")
        self.ColdMinAge = params.get("ColdMinAge")
        self.FrozenEnable = params.get("FrozenEnable")
        self.FrozenMinAge = params.get("FrozenMinAge")
        self.ColdAction = params.get("ColdAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexSettingsField(AbstractModel):
    """Index configuration fields

    """

    def __init__(self):
        r"""
        :param NumberOfShards: Number of primary shards
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NumberOfShards: str
        :param NumberOfReplicas: Number of replica shards
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NumberOfReplicas: str
        :param RefreshInterval: Index refresh interval
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RefreshInterval: str
        """
        self.NumberOfShards = None
        self.NumberOfReplicas = None
        self.RefreshInterval = None


    def _deserialize(self, params):
        self.NumberOfShards = params.get("NumberOfShards")
        self.NumberOfReplicas = params.get("NumberOfReplicas")
        self.RefreshInterval = params.get("RefreshInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """Instance details

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param Region: Region
        :type Region: str
        :param Zone: Availability Zone
        :type Zone: str
        :param AppId: User ID
        :type AppId: int
        :param Uin: User UIN
        :type Uin: str
        :param VpcUid: UID of the VPC where the instance resides
        :type VpcUid: str
        :param SubnetUid: UID of the subnet where the instance resides
        :type SubnetUid: str
        :param Status: Instance status. `0`: Processing; `1`: Normal; `-1`: `Stopped`; `-2`: Being terminated; `-3`: Terminated; `2`: Initializing during the cluster creation.
        :type Status: int
        :param RenewFlag: This parameter is not used on the global website
        :type RenewFlag: str
        :param ChargeType: Instance billing method. Valid values: POSTPAID_BY_HOUR (pay-as-you-go hourly); CDHPAID (billed based on CDH, i.e., only CDH is billed but not the instances on CDH)
        :type ChargeType: str
        :param ChargePeriod: This parameter is not used on the global website
        :type ChargePeriod: int
        :param NodeType: Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param NodeNum: Number of nodes
        :type NodeNum: int
        :param CpuNum: Number of CPU cores of the node
        :type CpuNum: int
        :param MemSize: Node memory size in GB
        :type MemSize: int
        :param DiskType: Node disk type
        :type DiskType: str
        :param DiskSize: Node disk size in GB
        :type DiskSize: int
        :param EsDomain: ES domain name
        :type EsDomain: str
        :param EsVip: ES VIP
        :type EsVip: str
        :param EsPort: ES port
        :type EsPort: int
        :param KibanaUrl: Kibana access URL
        :type KibanaUrl: str
        :param EsVersion: ES version number
        :type EsVersion: str
        :param EsConfig: ES configuration item
        :type EsConfig: str
        :param EsAcl: Kibana access control configuration
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param CreateTime: Instance creation time
        :type CreateTime: str
        :param UpdateTime: Last modified time of the instance
        :type UpdateTime: str
        :param Deadline: This parameter is not used on the global website
        :type Deadline: str
        :param InstanceType: Instance type (instance type identifier, which can be only 1 or 2 currently)
        :type InstanceType: int
        :param IkConfig: IK analyzer configuration
        :type IkConfig: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        :param MasterNodeInfo: Dedicated primary node configuration
        :type MasterNodeInfo: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        :param CosBackup: Auto-backup to COS configuration
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param AllowCosBackup: Whether to allow auto-backup to COS
        :type AllowCosBackup: bool
        :param TagList: List of tags owned by the instance
        :type TagList: list of TagInfo
        :param LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :type LicenseType: str
        :param EnableHotWarmMode: Whether it is a hot/warm cluster <li>true: yes </li><li>false: no</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableHotWarmMode: bool
        :param WarmNodeType: Warm node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmNodeType: str
        :param WarmNodeNum: Number of warm nodes
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmNodeNum: int
        :param WarmCpuNum: Number of warm node CPU cores
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmCpuNum: int
        :param WarmMemSize: Warm node memory size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmMemSize: int
        :param WarmDiskType: Warm node disk type
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmDiskType: str
        :param WarmDiskSize: Warm node disk size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmDiskSize: int
        :param NodeInfoList: Cluster node information list
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeInfoList: list of NodeInfo
        :param EsPublicUrl: ES public IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type EsPublicUrl: str
        :param MultiZoneInfo: Multi-AZ network information
Note: This field may return null, indicating that no valid values can be obtained.
        :type MultiZoneInfo: list of ZoneDetail
        :param DeployMode: Deployment mode <li>0: single-AZ </li><li>1: multi-AZ</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeployMode: int
        :param PublicAccess: ES public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicAccess: str
        :param EsPublicAcl: ES public access control configuration
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param KibanaPrivateUrl: Kibana private IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaPrivateUrl: str
        :param KibanaPublicAccess: Kibana public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaPublicAccess: str
        :param KibanaPrivateAccess: Kibana private access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaPrivateAccess: str
        :param SecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityType: int
        :param SceneType: Scenario template type. 0: not enabled; 1: general scenario; 2: log scenario; 3: search scenario
Note: this field may return null, indicating that no valid values can be obtained.
        :type SceneType: int
        :param KibanaConfig: Kibana configuration item.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type KibanaConfig: str
        :param KibanaNodeInfo: Kibana node information
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type KibanaNodeInfo: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`
        :param WebNodeTypeInfo: Visual node configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param Jdk: JDK type. Valid values: `oracle`, `kona`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Jdk: str
        :param Protocol: Cluster network communication protocol
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Protocol: str
        :param SecurityGroups: Security group ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroups: list of str
        :param ColdNodeType: Cold node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdNodeType: str
        :param ColdNodeNum: Number of cold nodes
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdNodeNum: int
        :param ColdCpuNum: Number of cold node CPU cores
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdCpuNum: int
        :param ColdMemSize: Cold node memory size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdMemSize: int
        :param ColdDiskType: Cold node disk type
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdDiskType: str
        :param ColdDiskSize: Cold node disk size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdDiskSize: int
        :param FrozenNodeType: Frozen node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenNodeType: str
        :param FrozenNodeNum: Number of frozen nodes
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenNodeNum: int
        :param FrozenCpuNum: Number of frozen node CPU cores
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenCpuNum: int
        :param FrozenMemSize: Frozen node memory size (GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenMemSize: int
        :param FrozenDiskType: Frozen node disk type
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenDiskType: str
        :param FrozenDiskSize: Frozen node disk size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenDiskSize: int
        :param HealthStatus: Cluster health status. `-1`: Unknown; `0`: Green; `1`: Yellow; `2`: Red
Note: This field may return `null`, indicating that no valid value was found.
        :type HealthStatus: int
        :param EsPrivateUrl: Private URL of the HTTPS cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type EsPrivateUrl: str
        :param EsPrivateDomain: Private domain of the HTTPS cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type EsPrivateDomain: str
        :param EsConfigSets: Configuration set info of the cluster.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EsConfigSets: list of EsConfigSetInfo
        :param OperationDuration: The maintenance time slot of the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param OptionalWebServiceInfos: Web node list
Note: This field may return null, indicating that no valid values can be obtained.
        :type OptionalWebServiceInfos: list of OptionalWebServiceInfo
        :param AutoIndexEnabled: Autonomous index option
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoIndexEnabled: bool
        :param EnableHybridStorage: Whether the storage-computing separation feature is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableHybridStorage: bool
        :param ProcessPercent: The process progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcessPercent: float
        :param KibanaAlteringPublicAccess: The alerting policy of Kibana over the public network. <li>`OPEN`: Enable the policy;</li><li>`CLOSE`: Disable the policy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaAlteringPublicAccess: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.AppId = None
        self.Uin = None
        self.VpcUid = None
        self.SubnetUid = None
        self.Status = None
        self.RenewFlag = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.NodeType = None
        self.NodeNum = None
        self.CpuNum = None
        self.MemSize = None
        self.DiskType = None
        self.DiskSize = None
        self.EsDomain = None
        self.EsVip = None
        self.EsPort = None
        self.KibanaUrl = None
        self.EsVersion = None
        self.EsConfig = None
        self.EsAcl = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Deadline = None
        self.InstanceType = None
        self.IkConfig = None
        self.MasterNodeInfo = None
        self.CosBackup = None
        self.AllowCosBackup = None
        self.TagList = None
        self.LicenseType = None
        self.EnableHotWarmMode = None
        self.WarmNodeType = None
        self.WarmNodeNum = None
        self.WarmCpuNum = None
        self.WarmMemSize = None
        self.WarmDiskType = None
        self.WarmDiskSize = None
        self.NodeInfoList = None
        self.EsPublicUrl = None
        self.MultiZoneInfo = None
        self.DeployMode = None
        self.PublicAccess = None
        self.EsPublicAcl = None
        self.KibanaPrivateUrl = None
        self.KibanaPublicAccess = None
        self.KibanaPrivateAccess = None
        self.SecurityType = None
        self.SceneType = None
        self.KibanaConfig = None
        self.KibanaNodeInfo = None
        self.WebNodeTypeInfo = None
        self.Jdk = None
        self.Protocol = None
        self.SecurityGroups = None
        self.ColdNodeType = None
        self.ColdNodeNum = None
        self.ColdCpuNum = None
        self.ColdMemSize = None
        self.ColdDiskType = None
        self.ColdDiskSize = None
        self.FrozenNodeType = None
        self.FrozenNodeNum = None
        self.FrozenCpuNum = None
        self.FrozenMemSize = None
        self.FrozenDiskType = None
        self.FrozenDiskSize = None
        self.HealthStatus = None
        self.EsPrivateUrl = None
        self.EsPrivateDomain = None
        self.EsConfigSets = None
        self.OperationDuration = None
        self.OptionalWebServiceInfos = None
        self.AutoIndexEnabled = None
        self.EnableHybridStorage = None
        self.ProcessPercent = None
        self.KibanaAlteringPublicAccess = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.VpcUid = params.get("VpcUid")
        self.SubnetUid = params.get("SubnetUid")
        self.Status = params.get("Status")
        self.RenewFlag = params.get("RenewFlag")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.NodeType = params.get("NodeType")
        self.NodeNum = params.get("NodeNum")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.EsDomain = params.get("EsDomain")
        self.EsVip = params.get("EsVip")
        self.EsPort = params.get("EsPort")
        self.KibanaUrl = params.get("KibanaUrl")
        self.EsVersion = params.get("EsVersion")
        self.EsConfig = params.get("EsConfig")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Deadline = params.get("Deadline")
        self.InstanceType = params.get("InstanceType")
        if params.get("IkConfig") is not None:
            self.IkConfig = EsDictionaryInfo()
            self.IkConfig._deserialize(params.get("IkConfig"))
        if params.get("MasterNodeInfo") is not None:
            self.MasterNodeInfo = MasterNodeInfo()
            self.MasterNodeInfo._deserialize(params.get("MasterNodeInfo"))
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))
        self.AllowCosBackup = params.get("AllowCosBackup")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.LicenseType = params.get("LicenseType")
        self.EnableHotWarmMode = params.get("EnableHotWarmMode")
        self.WarmNodeType = params.get("WarmNodeType")
        self.WarmNodeNum = params.get("WarmNodeNum")
        self.WarmCpuNum = params.get("WarmCpuNum")
        self.WarmMemSize = params.get("WarmMemSize")
        self.WarmDiskType = params.get("WarmDiskType")
        self.WarmDiskSize = params.get("WarmDiskSize")
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        self.EsPublicUrl = params.get("EsPublicUrl")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.DeployMode = params.get("DeployMode")
        self.PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self.EsPublicAcl = EsAcl()
            self.EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self.KibanaPrivateUrl = params.get("KibanaPrivateUrl")
        self.KibanaPublicAccess = params.get("KibanaPublicAccess")
        self.KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self.SecurityType = params.get("SecurityType")
        self.SceneType = params.get("SceneType")
        self.KibanaConfig = params.get("KibanaConfig")
        if params.get("KibanaNodeInfo") is not None:
            self.KibanaNodeInfo = KibanaNodeInfo()
            self.KibanaNodeInfo._deserialize(params.get("KibanaNodeInfo"))
        if params.get("WebNodeTypeInfo") is not None:
            self.WebNodeTypeInfo = WebNodeTypeInfo()
            self.WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self.Jdk = params.get("Jdk")
        self.Protocol = params.get("Protocol")
        self.SecurityGroups = params.get("SecurityGroups")
        self.ColdNodeType = params.get("ColdNodeType")
        self.ColdNodeNum = params.get("ColdNodeNum")
        self.ColdCpuNum = params.get("ColdCpuNum")
        self.ColdMemSize = params.get("ColdMemSize")
        self.ColdDiskType = params.get("ColdDiskType")
        self.ColdDiskSize = params.get("ColdDiskSize")
        self.FrozenNodeType = params.get("FrozenNodeType")
        self.FrozenNodeNum = params.get("FrozenNodeNum")
        self.FrozenCpuNum = params.get("FrozenCpuNum")
        self.FrozenMemSize = params.get("FrozenMemSize")
        self.FrozenDiskType = params.get("FrozenDiskType")
        self.FrozenDiskSize = params.get("FrozenDiskSize")
        self.HealthStatus = params.get("HealthStatus")
        self.EsPrivateUrl = params.get("EsPrivateUrl")
        self.EsPrivateDomain = params.get("EsPrivateDomain")
        if params.get("EsConfigSets") is not None:
            self.EsConfigSets = []
            for item in params.get("EsConfigSets"):
                obj = EsConfigSetInfo()
                obj._deserialize(item)
                self.EsConfigSets.append(obj)
        if params.get("OperationDuration") is not None:
            self.OperationDuration = OperationDuration()
            self.OperationDuration._deserialize(params.get("OperationDuration"))
        if params.get("OptionalWebServiceInfos") is not None:
            self.OptionalWebServiceInfos = []
            for item in params.get("OptionalWebServiceInfos"):
                obj = OptionalWebServiceInfo()
                obj._deserialize(item)
                self.OptionalWebServiceInfos.append(obj)
        self.AutoIndexEnabled = params.get("AutoIndexEnabled")
        self.EnableHybridStorage = params.get("EnableHybridStorage")
        self.ProcessPercent = params.get("ProcessPercent")
        self.KibanaAlteringPublicAccess = params.get("KibanaAlteringPublicAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceLog(AbstractModel):
    """ES cluster log details

    """

    def __init__(self):
        r"""
        :param Time: Log time
        :type Time: str
        :param Level: Log level
        :type Level: str
        :param Ip: Cluster node IP
        :type Ip: str
        :param Message: Log content
        :type Message: str
        """
        self.Time = None
        self.Level = None
        self.Ip = None
        self.Message = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Level = params.get("Level")
        self.Ip = params.get("Ip")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """`OperationDetail` uses an array of this structure to describe the old and new configuration information

    """

    def __init__(self):
        r"""
        :param Key: Key
        :type Key: str
        :param Value: Value
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
        


class KibanaNodeInfo(AbstractModel):
    """Kibana node information

    """

    def __init__(self):
        r"""
        :param KibanaNodeType: Kibana node specification
        :type KibanaNodeType: str
        :param KibanaNodeNum: Number of Kibana nodes
        :type KibanaNodeNum: int
        :param KibanaNodeCpuNum: Number of Kibana node's CPUs
        :type KibanaNodeCpuNum: int
        :param KibanaNodeMemSize: Kibana node's memory in GB
        :type KibanaNodeMemSize: int
        :param KibanaNodeDiskType: Kibana node's disk type
        :type KibanaNodeDiskType: str
        :param KibanaNodeDiskSize: Kibana node's disk size
        :type KibanaNodeDiskSize: int
        """
        self.KibanaNodeType = None
        self.KibanaNodeNum = None
        self.KibanaNodeCpuNum = None
        self.KibanaNodeMemSize = None
        self.KibanaNodeDiskType = None
        self.KibanaNodeDiskSize = None


    def _deserialize(self, params):
        self.KibanaNodeType = params.get("KibanaNodeType")
        self.KibanaNodeNum = params.get("KibanaNodeNum")
        self.KibanaNodeCpuNum = params.get("KibanaNodeCpuNum")
        self.KibanaNodeMemSize = params.get("KibanaNodeMemSize")
        self.KibanaNodeDiskType = params.get("KibanaNodeDiskType")
        self.KibanaNodeDiskSize = params.get("KibanaNodeDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KibanaView(AbstractModel):
    """Kibana view data

    """

    def __init__(self):
        r"""
        :param Ip: Kibana node IP
        :type Ip: str
        :param DiskSize: Node disk size
        :type DiskSize: int
        :param DiskUsage: Disk usage
        :type DiskUsage: float
        :param MemSize: Node memory size
        :type MemSize: int
        :param MemUsage: Memory usage
        :type MemUsage: float
        :param CpuNum: Number of node CPUs
        :type CpuNum: int
        :param CpuUsage: CPU usage
        :type CpuUsage: float
        :param Zone: Availability zone
        :type Zone: str
        """
        self.Ip = None
        self.DiskSize = None
        self.DiskUsage = None
        self.MemSize = None
        self.MemUsage = None
        self.CpuNum = None
        self.CpuUsage = None
        self.Zone = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.DiskSize = params.get("DiskSize")
        self.DiskUsage = params.get("DiskUsage")
        self.MemSize = params.get("MemSize")
        self.MemUsage = params.get("MemUsage")
        self.CpuNum = params.get("CpuNum")
        self.CpuUsage = params.get("CpuUsage")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskInfo(AbstractModel):
    """Local disk information of node

    """

    def __init__(self):
        r"""
        :param LocalDiskType: Local disk type <li>LOCAL_SATA: big data </li><li>NVME_SSD: high IO</li>
        :type LocalDiskType: str
        :param LocalDiskSize: Size of a single local disk
        :type LocalDiskSize: int
        :param LocalDiskCount: Number of local disks
        :type LocalDiskCount: int
        """
        self.LocalDiskType = None
        self.LocalDiskSize = None
        self.LocalDiskCount = None


    def _deserialize(self, params):
        self.LocalDiskType = params.get("LocalDiskType")
        self.LocalDiskSize = params.get("LocalDiskSize")
        self.LocalDiskCount = params.get("LocalDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MasterNodeInfo(AbstractModel):
    """Information of the dedicated primary node in an instance

    """

    def __init__(self):
        r"""
        :param EnableDedicatedMaster: Whether to enable the dedicated primary node
        :type EnableDedicatedMaster: bool
        :param MasterNodeType: Dedicated primary node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :type MasterNodeType: str
        :param MasterNodeNum: Number of dedicated primary nodes
        :type MasterNodeNum: int
        :param MasterNodeCpuNum: Number of CPU cores of the dedicated primary node
        :type MasterNodeCpuNum: int
        :param MasterNodeMemSize: Memory size of the dedicated primary node in GB
        :type MasterNodeMemSize: int
        :param MasterNodeDiskSize: Disk size of the dedicated primary node in GB
        :type MasterNodeDiskSize: int
        :param MasterNodeDiskType: Disk type of the dedicated primary node
        :type MasterNodeDiskType: str
        """
        self.EnableDedicatedMaster = None
        self.MasterNodeType = None
        self.MasterNodeNum = None
        self.MasterNodeCpuNum = None
        self.MasterNodeMemSize = None
        self.MasterNodeDiskSize = None
        self.MasterNodeDiskType = None


    def _deserialize(self, params):
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeCpuNum = params.get("MasterNodeCpuNum")
        self.MasterNodeMemSize = params.get("MasterNodeMemSize")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.MasterNodeDiskType = params.get("MasterNodeDiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """Specification information of a node type in the cluster (such as hot data node, warm data node, or dedicated primary node), including node type, number of nodes, node specification, disk type, and disk size. If `Type` is not specified, it will be a hot data node by default; if the node is a primary node, then the `DiskType` and `DiskSize` parameters will be ignored (as a primary node has no data disks)

    """

    def __init__(self):
        r"""
        :param NodeNum: Number of nodes
        :type NodeNum: int
        :param NodeType: Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param Type: Node type<li>`hotData`: hot data node</li>
<li>`warmData`: warm data node</li>
<li>`dedicatedMaster`: dedicated master node</li>
Default value: `hotData`
        :type Type: str
        :param DiskType: Node disk type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: Premium cloud disk </li>Default value: CLOUD_SSD
        :type DiskType: str
        :param DiskSize: Node disk size in GB
        :type DiskSize: int
        :param LocalDiskInfo: Local disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :type LocalDiskInfo: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`
        :param DiskCount: Number of node disks
        :type DiskCount: int
        :param DiskEncrypt: Whether to encrypt node disk. 0: no (default); 1: yes.
        :type DiskEncrypt: int
        :param CpuNum: CPU number
Note: This field may return null, indicating that no valid values can be obtained.
        :type CpuNum: int
        :param MemSize: Memory size in GB
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param DiskEnhance: /
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskEnhance: int
        """
        self.NodeNum = None
        self.NodeType = None
        self.Type = None
        self.DiskType = None
        self.DiskSize = None
        self.LocalDiskInfo = None
        self.DiskCount = None
        self.DiskEncrypt = None
        self.CpuNum = None
        self.MemSize = None
        self.DiskEnhance = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.NodeType = params.get("NodeType")
        self.Type = params.get("Type")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        if params.get("LocalDiskInfo") is not None:
            self.LocalDiskInfo = LocalDiskInfo()
            self.LocalDiskInfo._deserialize(params.get("LocalDiskInfo"))
        self.DiskCount = params.get("DiskCount")
        self.DiskEncrypt = params.get("DiskEncrypt")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.DiskEnhance = params.get("DiskEnhance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeView(AbstractModel):
    """Node view data

    """

    def __init__(self):
        r"""
        :param NodeId: Node ID
        :type NodeId: str
        :param NodeIp: Node IP
        :type NodeIp: str
        :param Visible: Whether the node is visible
        :type Visible: float
        :param Break: Whether the node encounters circuit breaking
        :type Break: float
        :param DiskSize: Node disk size
        :type DiskSize: int
        :param DiskUsage: Disk usage
        :type DiskUsage: float
        :param MemSize: Node memory size (in GB)
        :type MemSize: int
        :param MemUsage: Memory usage
        :type MemUsage: float
        :param CpuNum: Number of node CPUs
        :type CpuNum: int
        :param CpuUsage: CPU usage
        :type CpuUsage: float
        :param Zone: Availability zone
        :type Zone: str
        :param NodeRole: Node role
        :type NodeRole: str
        :param NodeHttpIp: Node HTTP IP
        :type NodeHttpIp: str
        :param JvmMemUsage: JVM memory usage
        :type JvmMemUsage: float
        :param ShardNum: Number of node shards
        :type ShardNum: int
        :param DiskIds: ID list of node disks
        :type DiskIds: list of str
        :param Hidden: Whether a hidden availability zone
        :type Hidden: bool
        """
        self.NodeId = None
        self.NodeIp = None
        self.Visible = None
        self.Break = None
        self.DiskSize = None
        self.DiskUsage = None
        self.MemSize = None
        self.MemUsage = None
        self.CpuNum = None
        self.CpuUsage = None
        self.Zone = None
        self.NodeRole = None
        self.NodeHttpIp = None
        self.JvmMemUsage = None
        self.ShardNum = None
        self.DiskIds = None
        self.Hidden = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeIp = params.get("NodeIp")
        self.Visible = params.get("Visible")
        self.Break = params.get("Break")
        self.DiskSize = params.get("DiskSize")
        self.DiskUsage = params.get("DiskUsage")
        self.MemSize = params.get("MemSize")
        self.MemUsage = params.get("MemUsage")
        self.CpuNum = params.get("CpuNum")
        self.CpuUsage = params.get("CpuUsage")
        self.Zone = params.get("Zone")
        self.NodeRole = params.get("NodeRole")
        self.NodeHttpIp = params.get("NodeHttpIp")
        self.JvmMemUsage = params.get("JvmMemUsage")
        self.ShardNum = params.get("ShardNum")
        self.DiskIds = params.get("DiskIds")
        self.Hidden = params.get("Hidden")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operation(AbstractModel):
    """ES cluster operation details

    """

    def __init__(self):
        r"""
        :param Id: Unique operation ID
        :type Id: int
        :param StartTime: Operation start time
        :type StartTime: str
        :param Type: Operation type
        :type Type: str
        :param Detail: Operation details
        :type Detail: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        :param Result: Operation result
        :type Result: str
        :param Tasks: Workflow task information
        :type Tasks: list of TaskDetail
        :param Progress: Operation progress
        :type Progress: float
        """
        self.Id = None
        self.StartTime = None
        self.Type = None
        self.Detail = None
        self.Result = None
        self.Tasks = None
        self.Progress = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        if params.get("Detail") is not None:
            self.Detail = OperationDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.Result = params.get("Result")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDetail(AbstractModel):
    """Operation details

    """

    def __init__(self):
        r"""
        :param OldInfo: Original instance configuration information
        :type OldInfo: list of KeyValue
        :param NewInfo: Updated instance configuration information
        :type NewInfo: list of KeyValue
        """
        self.OldInfo = None
        self.NewInfo = None


    def _deserialize(self, params):
        if params.get("OldInfo") is not None:
            self.OldInfo = []
            for item in params.get("OldInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.OldInfo.append(obj)
        if params.get("NewInfo") is not None:
            self.NewInfo = []
            for item in params.get("NewInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.NewInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDuration(AbstractModel):
    """The maintenance time slot of the cluster

    """

    def __init__(self):
        r"""
        :param Periods: Maintenance period, which can be one or more days from Monday to Sunday. Valid values: [0, 6].
Note: This field may return null, indicating that no valid values can be obtained.
        :type Periods: list of int non-negative
        :param TimeStart: The maintenance start time
        :type TimeStart: str
        :param TimeEnd: The maintenance end time
        :type TimeEnd: str
        :param TimeZone: The time zone expressed in UTC.
        :type TimeZone: str
        """
        self.Periods = None
        self.TimeStart = None
        self.TimeEnd = None
        self.TimeZone = None


    def _deserialize(self, params):
        self.Periods = params.get("Periods")
        self.TimeStart = params.get("TimeStart")
        self.TimeEnd = params.get("TimeEnd")
        self.TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDurationUpdated(AbstractModel):
    """The maintenance time slot of the cluster

    """

    def __init__(self):
        r"""
        :param Periods: Maintenance period, which can be one or more days from Monday to Sunday. Valid values: [0, 6].
        :type Periods: list of int non-negative
        :param TimeStart: The maintenance start time
        :type TimeStart: str
        :param TimeEnd: The maintenance end time
        :type TimeEnd: str
        :param TimeZone: The time zone expressed in UTC.
        :type TimeZone: str
        :param MoreInstances: The array of ES cluster IDs
        :type MoreInstances: list of str
        """
        self.Periods = None
        self.TimeStart = None
        self.TimeEnd = None
        self.TimeZone = None
        self.MoreInstances = None


    def _deserialize(self, params):
        self.Periods = params.get("Periods")
        self.TimeStart = params.get("TimeStart")
        self.TimeEnd = params.get("TimeEnd")
        self.TimeZone = params.get("TimeZone")
        self.MoreInstances = params.get("MoreInstances")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OptionalWebServiceInfo(AbstractModel):
    """The information of optional web components

    """

    def __init__(self):
        r"""
        :param Type: Type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param Status: Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param PublicUrl: Public URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicUrl: str
        :param PrivateUrl: Private URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateUrl: str
        :param PublicAccess: Public network access
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicAccess: str
        :param PrivateAccess: Private network access
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateAccess: str
        :param Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        """
        self.Type = None
        self.Status = None
        self.PublicUrl = None
        self.PrivateUrl = None
        self.PublicAccess = None
        self.PrivateAccess = None
        self.Version = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.PublicUrl = params.get("PublicUrl")
        self.PrivateUrl = params.get("PrivateUrl")
        self.PublicAccess = params.get("PublicAccess")
        self.PrivateAccess = params.get("PrivateAccess")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    """RestartInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ForceRestart: Whether to force restart <li>true: Yes </li><li>false: No </li>Default value: false
        :type ForceRestart: bool
        :param RestartMode: Restart mode. `0`: rolling restart; `1`: full restart
        :type RestartMode: int
        """
        self.InstanceId = None
        self.ForceRestart = None
        self.RestartMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ForceRestart = params.get("ForceRestart")
        self.RestartMode = params.get("RestartMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartKibanaRequest(AbstractModel):
    """RestartKibana request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ES instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartKibanaResponse(AbstractModel):
    """RestartKibana response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartNodesRequest(AbstractModel):
    """RestartNodes request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Cluster instance ID
        :type InstanceId: str
        :param NodeNames: Node name list
        :type NodeNames: list of str
        :param ForceRestart: Whether to force restart
        :type ForceRestart: bool
        :param RestartMode: The restart mode. Valid values: `in-place` (default), `blue-green`.
        :type RestartMode: str
        :param IsOffline: The node status, applicable in the blue/green mode. The blue/green restart is risky if the node is offline.
        :type IsOffline: bool
        """
        self.InstanceId = None
        self.NodeNames = None
        self.ForceRestart = None
        self.RestartMode = None
        self.IsOffline = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeNames = params.get("NodeNames")
        self.ForceRestart = params.get("ForceRestart")
        self.RestartMode = params.get("RestartMode")
        self.IsOffline = params.get("IsOffline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartNodesResponse(AbstractModel):
    """RestartNodes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubTaskDetail(AbstractModel):
    """Information of subtask in workflow task in the instance operation history (such as each check item in a upgrade check task)

    """

    def __init__(self):
        r"""
        :param Name: Subtask name
        :type Name: str
        :param Result: Subtask result
        :type Result: bool
        :param ErrMsg: Subtask error message
        :type ErrMsg: str
        :param Type: Subtask type
        :type Type: str
        :param Status: Subtask status. 0: processing, 1: succeeded, -1: failed
        :type Status: int
        :param FailedIndices: Name of the index for which the check for upgrade failed
        :type FailedIndices: list of str
        :param FinishTime: Subtask end time
        :type FinishTime: str
        :param Level: Subtask level. 1: warning, 2: failed
        :type Level: int
        """
        self.Name = None
        self.Result = None
        self.ErrMsg = None
        self.Type = None
        self.Status = None
        self.FailedIndices = None
        self.FinishTime = None
        self.Level = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.FailedIndices = params.get("FailedIndices")
        self.FinishTime = params.get("FinishTime")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Instance tag information

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
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
        


class TaskDetail(AbstractModel):
    """Information of workflow task in instance operation history

    """

    def __init__(self):
        r"""
        :param Name: Task name
        :type Name: str
        :param Progress: Task progress
        :type Progress: float
        :param FinishTime: Task completion time
        :type FinishTime: str
        :param SubTasks: Subtask
        :type SubTasks: list of SubTaskDetail
        :param ElapsedTime: The task time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ElapsedTime: int
        """
        self.Name = None
        self.Progress = None
        self.FinishTime = None
        self.SubTasks = None
        self.ElapsedTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Progress = params.get("Progress")
        self.FinishTime = params.get("FinishTime")
        if params.get("SubTasks") is not None:
            self.SubTasks = []
            for item in params.get("SubTasks"):
                obj = SubTaskDetail()
                obj._deserialize(item)
                self.SubTasks.append(obj)
        self.ElapsedTime = params.get("ElapsedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDictionariesRequest(AbstractModel):
    """UpdateDictionaries request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ES instance ID
        :type InstanceId: str
        :param IkMainDicts: COS address of the main dictionary for the IK analyzer
        :type IkMainDicts: list of str
        :param IkStopwords: COS address of the stopword dictionary for the IK analyzer
        :type IkStopwords: list of str
        :param Synonym: COS address of the synonym dictionary
        :type Synonym: list of str
        :param QQDict: COS address of the QQ dictionary
        :type QQDict: list of str
        :param UpdateType: `0` (default): Install, `1`: Delete
        :type UpdateType: int
        :param ForceRestart: Whether to force restart the cluster. The default value is `false`.
        :type ForceRestart: bool
        """
        self.InstanceId = None
        self.IkMainDicts = None
        self.IkStopwords = None
        self.Synonym = None
        self.QQDict = None
        self.UpdateType = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IkMainDicts = params.get("IkMainDicts")
        self.IkStopwords = params.get("IkStopwords")
        self.Synonym = params.get("Synonym")
        self.QQDict = params.get("QQDict")
        self.UpdateType = params.get("UpdateType")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDictionariesResponse(AbstractModel):
    """UpdateDictionaries response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateIndexRequest(AbstractModel):
    """UpdateIndex request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ES cluster ID
        :type InstanceId: str
        :param IndexType: Type of the index to update. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param IndexName: Name of the index to update
        :type IndexName: str
        :param UpdateMetaJson: JSON-formatted index metadata to update, such as `mappings` and `settings`.
        :type UpdateMetaJson: str
        :param Username: Username for cluster access
        :type Username: str
        :param Password: Password for cluster access
        :type Password: str
        :param RolloverBackingIndex: Whether to roll over the backup index
        :type RolloverBackingIndex: bool
        """
        self.InstanceId = None
        self.IndexType = None
        self.IndexName = None
        self.UpdateMetaJson = None
        self.Username = None
        self.Password = None
        self.RolloverBackingIndex = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.UpdateMetaJson = params.get("UpdateMetaJson")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.RolloverBackingIndex = params.get("RolloverBackingIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateIndexResponse(AbstractModel):
    """UpdateIndex response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateInstanceRequest(AbstractModel):
    """UpdateInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)
        :type InstanceName: str
        :param NodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2-50)
        :type NodeNum: int
        :param EsConfig: ES configuration item (JSON string)
        :type EsConfig: str
        :param Password: Password of the default user 'elastic', which must contain 8 to 16 characters, including at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]
        :type Password: str
        :param EsAcl: The policy for visual component (Kibana and Cerebro) access over public network.
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param DiskSize: This parameter has been disused. Please use `NodeInfoList`
Disk size in GB
        :type DiskSize: int
        :param NodeType: This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param MasterNodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of dedicated primary nodes (only 3 and 5 are supported)
        :type MasterNodeNum: int
        :param MasterNodeType: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :type MasterNodeType: str
        :param MasterNodeDiskSize: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node disk size in GB. This is 50 GB by default and currently cannot be customized
        :type MasterNodeDiskSize: int
        :param ForceRestart: Whether to force restart during configuration update <li>true: Yes </li><li>false: No </li>This needs to be set only for EsConfig. Default value: false
        :type ForceRestart: bool
        :param CosBackup: Auto-backup to COS
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param NodeInfoList: Node information list. You can pass in only the nodes to be updated and their corresponding specification information. Supported operations include: <li>modifying the number of nodes in the same type </li><li>modifying the specification and disk size of nodes in the same type </li><li>adding a node type (you must also specify the node type, quantity, specification, disk, etc.) </li>The above operations can only be performed one at a time, and the disk type cannot be modified
        :type NodeInfoList: list of NodeInfo
        :param PublicAccess: The status of ES cluster access over public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type PublicAccess: str
        :param EsPublicAcl: Public network ACL
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`
        :param KibanaPublicAccess: The status of Kibana access over public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type KibanaPublicAccess: str
        :param KibanaPrivateAccess: The status of Kibana access over private network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type KibanaPrivateAccess: str
        :param BasicSecurityType: Enables or disables user authentication for ES Basic Edition v6.8 and above
        :type BasicSecurityType: int
        :param KibanaPrivatePort: Kibana private port
        :type KibanaPrivatePort: int
        :param ScaleType: 0: scaling in blue/green deployment mode without cluster restart (default); 1: scaling by unmounting disk with rolling cluster restart
        :type ScaleType: int
        :param MultiZoneInfo: Multi-AZ deployment
        :type MultiZoneInfo: list of ZoneDetail
        :param SceneType: Scenario template type. -1: not enabled; 1: general; 2: log; 3: search
        :type SceneType: int
        :param KibanaConfig: Kibana configuration item (JSON string)
        :type KibanaConfig: str
        :param WebNodeTypeInfo: Visual node configuration
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param SwitchPrivateLink: Whether to switch to the new network architecture
        :type SwitchPrivateLink: str
        :param EnableCerebro: Whether to enable Cerebro
        :type EnableCerebro: bool
        :param CerebroPublicAccess: The status of Cerebro access over public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type CerebroPublicAccess: str
        :param CerebroPrivateAccess: The status of Cerebro access over private network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type CerebroPrivateAccess: str
        :param EsConfigSet: Added or modified configuration set information
        :type EsConfigSet: :class:`tencentcloud.es.v20180416.models.EsConfigSetInfo`
        :param OperationDuration: The maintenance time slot
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        :param KibanaAlteringPublicAccess: Whether to enable the option for sending alerting messages over the public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type KibanaAlteringPublicAccess: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.NodeNum = None
        self.EsConfig = None
        self.Password = None
        self.EsAcl = None
        self.DiskSize = None
        self.NodeType = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ForceRestart = None
        self.CosBackup = None
        self.NodeInfoList = None
        self.PublicAccess = None
        self.EsPublicAcl = None
        self.KibanaPublicAccess = None
        self.KibanaPrivateAccess = None
        self.BasicSecurityType = None
        self.KibanaPrivatePort = None
        self.ScaleType = None
        self.MultiZoneInfo = None
        self.SceneType = None
        self.KibanaConfig = None
        self.WebNodeTypeInfo = None
        self.SwitchPrivateLink = None
        self.EnableCerebro = None
        self.CerebroPublicAccess = None
        self.CerebroPrivateAccess = None
        self.EsConfigSet = None
        self.OperationDuration = None
        self.KibanaAlteringPublicAccess = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.EsConfig = params.get("EsConfig")
        self.Password = params.get("Password")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.DiskSize = params.get("DiskSize")
        self.NodeType = params.get("NodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ForceRestart = params.get("ForceRestart")
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        self.PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self.EsPublicAcl = EsPublicAcl()
            self.EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self.KibanaPublicAccess = params.get("KibanaPublicAccess")
        self.KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.KibanaPrivatePort = params.get("KibanaPrivatePort")
        self.ScaleType = params.get("ScaleType")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.SceneType = params.get("SceneType")
        self.KibanaConfig = params.get("KibanaConfig")
        if params.get("WebNodeTypeInfo") is not None:
            self.WebNodeTypeInfo = WebNodeTypeInfo()
            self.WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self.SwitchPrivateLink = params.get("SwitchPrivateLink")
        self.EnableCerebro = params.get("EnableCerebro")
        self.CerebroPublicAccess = params.get("CerebroPublicAccess")
        self.CerebroPrivateAccess = params.get("CerebroPrivateAccess")
        if params.get("EsConfigSet") is not None:
            self.EsConfigSet = EsConfigSetInfo()
            self.EsConfigSet._deserialize(params.get("EsConfigSet"))
        if params.get("OperationDuration") is not None:
            self.OperationDuration = OperationDurationUpdated()
            self.OperationDuration._deserialize(params.get("OperationDuration"))
        self.KibanaAlteringPublicAccess = params.get("KibanaAlteringPublicAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceResponse(AbstractModel):
    """UpdateInstance response structure.

    """

    def __init__(self):
        r"""
        :param DealName: Order ID
Note: This field may return `null`, indicating that no valid value was found.
        :type DealName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class UpdatePluginsRequest(AbstractModel):
    """UpdatePlugins request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstallPluginList: List of names of the plugins to be installed
        :type InstallPluginList: list of str
        :param RemovePluginList: List of names of the plugins to be uninstalled
        :type RemovePluginList: list of str
        :param ForceRestart: Whether to force restart the cluster. The default value is `false`.
        :type ForceRestart: bool
        :param ForceUpdate: Whether to reinstall the cluster. The default value is `false`.
        :type ForceUpdate: bool
        :param PluginType: 0: system plugin
        :type PluginType: int
        """
        self.InstanceId = None
        self.InstallPluginList = None
        self.RemovePluginList = None
        self.ForceRestart = None
        self.ForceUpdate = None
        self.PluginType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstallPluginList = params.get("InstallPluginList")
        self.RemovePluginList = params.get("RemovePluginList")
        self.ForceRestart = params.get("ForceRestart")
        self.ForceUpdate = params.get("ForceUpdate")
        self.PluginType = params.get("PluginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePluginsResponse(AbstractModel):
    """UpdatePlugins response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRequestTargetNodeTypesRequest(AbstractModel):
    """UpdateRequestTargetNodeTypes request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param TargetNodeTypes: A list of node types used to receive requests.
        :type TargetNodeTypes: list of str
        """
        self.InstanceId = None
        self.TargetNodeTypes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRequestTargetNodeTypesResponse(AbstractModel):
    """UpdateRequestTargetNodeTypes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param EsVersion: Target ES version. Valid values: 6.4.3, 6.8.2, 7.5.1
        :type EsVersion: str
        :param CheckOnly: Whether to check for upgrade only. Default value: false
        :type CheckOnly: bool
        :param LicenseType: Target X-Pack edition: <li>OSS: Open-source Edition </li><li>basic: Basic Edition </li>Currently only used for v5.6.4 to v6.x upgrade. Default value: basic
        :type LicenseType: str
        :param BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :type BasicSecurityType: int
        :param UpgradeMode: Upgrade mode. <li>scale: blue/green deployment</li><li>restart: rolling restart</li>Default value: scale
        :type UpgradeMode: str
        :param CosBackup: Whether to back up the cluster before version upgrade (no backup by default)
        :type CosBackup: bool
        :param SkipCheckForceRestart: Whether to skip the check and perform a force restart in the rolling mode. Default value: `false`.
        :type SkipCheckForceRestart: bool
        """
        self.InstanceId = None
        self.EsVersion = None
        self.CheckOnly = None
        self.LicenseType = None
        self.BasicSecurityType = None
        self.UpgradeMode = None
        self.CosBackup = None
        self.SkipCheckForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EsVersion = params.get("EsVersion")
        self.CheckOnly = params.get("CheckOnly")
        self.LicenseType = params.get("LicenseType")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.UpgradeMode = params.get("UpgradeMode")
        self.CosBackup = params.get("CosBackup")
        self.SkipCheckForceRestart = params.get("SkipCheckForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeLicenseRequest(AbstractModel):
    """UpgradeLicense request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :type LicenseType: str
        :param AutoVoucher: Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0
        :type AutoVoucher: int
        :param VoucherIds: List of voucher IDs (only one voucher can be specified at a time currently)
        :type VoucherIds: list of str
        :param BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :type BasicSecurityType: int
        :param ForceRestart: Whether to force restart <li>true: yes </li><li>false: no </li>Default value: false
        :type ForceRestart: bool
        """
        self.InstanceId = None
        self.LicenseType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.BasicSecurityType = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LicenseType = params.get("LicenseType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLicenseResponse(AbstractModel):
    """UpgradeLicense response structure.

    """

    def __init__(self):
        r"""
        :param DealName: Order ID
Note: This field may return `null`, indicating that no valid value was found.
        :type DealName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class WebNodeTypeInfo(AbstractModel):
    """Visual node configuration

    """

    def __init__(self):
        r"""
        :param NodeNum: Number of visual nodes. The value is always `1`.
        :type NodeNum: int
        :param NodeType: Visual node specification
        :type NodeType: str
        """
        self.NodeNum = None
        self.NodeType = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDetail(AbstractModel):
    """Details of AZs in multi-AZ deployment mode

    """

    def __init__(self):
        r"""
        :param Zone: AZ
        :type Zone: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        """
        self.Zone = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        