# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""Backing index metadata fields

    """

    def __init__(self):
        r"""
        :param _IndexName: Backing index name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexName: str
        :param _IndexStatus: Backing index status
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexStatus: str
        :param _IndexStorage: Backing index size
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexStorage: int
        :param _IndexPhrase: Current lifecycle phase of backing index
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexPhrase: str
        :param _IndexCreateTime: Backing index creation time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexCreateTime: str
        """
        self._IndexName = None
        self._IndexStatus = None
        self._IndexStorage = None
        self._IndexPhrase = None
        self._IndexCreateTime = None

    @property
    def IndexName(self):
        r"""Backing index name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexStatus(self):
        r"""Backing index status
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus

    @property
    def IndexStorage(self):
        r"""Backing index size
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._IndexStorage

    @IndexStorage.setter
    def IndexStorage(self, IndexStorage):
        self._IndexStorage = IndexStorage

    @property
    def IndexPhrase(self):
        r"""Current lifecycle phase of backing index
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IndexPhrase

    @IndexPhrase.setter
    def IndexPhrase(self, IndexPhrase):
        self._IndexPhrase = IndexPhrase

    @property
    def IndexCreateTime(self):
        r"""Backing index creation time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IndexCreateTime

    @IndexCreateTime.setter
    def IndexCreateTime(self, IndexCreateTime):
        self._IndexCreateTime = IndexCreateTime


    def _deserialize(self, params):
        self._IndexName = params.get("IndexName")
        self._IndexStatus = params.get("IndexStatus")
        self._IndexStorage = params.get("IndexStorage")
        self._IndexPhrase = params.get("IndexPhrase")
        self._IndexCreateTime = params.get("IndexCreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterView(AbstractModel):
    r"""Cluster view data

    """

    def __init__(self):
        r"""
        :param _Health: Cluster health status
        :type Health: float
        :param _Visible: Whether the cluster is visible
        :type Visible: float
        :param _Break: Whether the cluster encounters circuit breaking
        :type Break: float
        :param _AvgDiskUsage: Average disk usage
        :type AvgDiskUsage: float
        :param _AvgMemUsage: Average memory usage
        :type AvgMemUsage: float
        :param _AvgCpuUsage: Average CPU usage
        :type AvgCpuUsage: float
        :param _TotalDiskSize: Total disk size of the cluster
        :type TotalDiskSize: int
        :param _TargetNodeTypes: Types of nodes to receive client requests
        :type TargetNodeTypes: list of str
        :param _NodeNum: Number of online nodes
        :type NodeNum: int
        :param _TotalNodeNum: Total number of nodes
        :type TotalNodeNum: int
        :param _DataNodeNum: Number of data nodes
        :type DataNodeNum: int
        :param _IndexNum: Number of indices
        :type IndexNum: int
        :param _DocNum: Number of documents
        :type DocNum: int
        :param _DiskUsedInBytes: Used disk size (in bytes)
        :type DiskUsedInBytes: int
        :param _ShardNum: Number of shards
        :type ShardNum: int
        :param _PrimaryShardNum: Number of primary shards
        :type PrimaryShardNum: int
        :param _RelocatingShardNum: Number of relocating shards
        :type RelocatingShardNum: int
        :param _InitializingShardNum: Number of initializing shards
        :type InitializingShardNum: int
        :param _UnassignedShardNum: Number of unassigned shards
        :type UnassignedShardNum: int
        :param _TotalCosStorage: Total COS storage of an enterprise cluster, in GB
        :type TotalCosStorage: int
        :param _SearchableSnapshotCosBucket: Name of the COS bucket that stores searchable snapshots of an enterprise cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type SearchableSnapshotCosBucket: str
        :param _SearchableSnapshotCosAppId: COS app ID of the searchable snapshots of an enterprise cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type SearchableSnapshotCosAppId: str
        """
        self._Health = None
        self._Visible = None
        self._Break = None
        self._AvgDiskUsage = None
        self._AvgMemUsage = None
        self._AvgCpuUsage = None
        self._TotalDiskSize = None
        self._TargetNodeTypes = None
        self._NodeNum = None
        self._TotalNodeNum = None
        self._DataNodeNum = None
        self._IndexNum = None
        self._DocNum = None
        self._DiskUsedInBytes = None
        self._ShardNum = None
        self._PrimaryShardNum = None
        self._RelocatingShardNum = None
        self._InitializingShardNum = None
        self._UnassignedShardNum = None
        self._TotalCosStorage = None
        self._SearchableSnapshotCosBucket = None
        self._SearchableSnapshotCosAppId = None

    @property
    def Health(self):
        r"""Cluster health status
        :rtype: float
        """
        return self._Health

    @Health.setter
    def Health(self, Health):
        self._Health = Health

    @property
    def Visible(self):
        r"""Whether the cluster is visible
        :rtype: float
        """
        return self._Visible

    @Visible.setter
    def Visible(self, Visible):
        self._Visible = Visible

    @property
    def Break(self):
        r"""Whether the cluster encounters circuit breaking
        :rtype: float
        """
        return self._Break

    @Break.setter
    def Break(self, Break):
        self._Break = Break

    @property
    def AvgDiskUsage(self):
        r"""Average disk usage
        :rtype: float
        """
        return self._AvgDiskUsage

    @AvgDiskUsage.setter
    def AvgDiskUsage(self, AvgDiskUsage):
        self._AvgDiskUsage = AvgDiskUsage

    @property
    def AvgMemUsage(self):
        r"""Average memory usage
        :rtype: float
        """
        return self._AvgMemUsage

    @AvgMemUsage.setter
    def AvgMemUsage(self, AvgMemUsage):
        self._AvgMemUsage = AvgMemUsage

    @property
    def AvgCpuUsage(self):
        r"""Average CPU usage
        :rtype: float
        """
        return self._AvgCpuUsage

    @AvgCpuUsage.setter
    def AvgCpuUsage(self, AvgCpuUsage):
        self._AvgCpuUsage = AvgCpuUsage

    @property
    def TotalDiskSize(self):
        r"""Total disk size of the cluster
        :rtype: int
        """
        return self._TotalDiskSize

    @TotalDiskSize.setter
    def TotalDiskSize(self, TotalDiskSize):
        self._TotalDiskSize = TotalDiskSize

    @property
    def TargetNodeTypes(self):
        r"""Types of nodes to receive client requests
        :rtype: list of str
        """
        return self._TargetNodeTypes

    @TargetNodeTypes.setter
    def TargetNodeTypes(self, TargetNodeTypes):
        self._TargetNodeTypes = TargetNodeTypes

    @property
    def NodeNum(self):
        r"""Number of online nodes
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def TotalNodeNum(self):
        r"""Total number of nodes
        :rtype: int
        """
        return self._TotalNodeNum

    @TotalNodeNum.setter
    def TotalNodeNum(self, TotalNodeNum):
        self._TotalNodeNum = TotalNodeNum

    @property
    def DataNodeNum(self):
        r"""Number of data nodes
        :rtype: int
        """
        return self._DataNodeNum

    @DataNodeNum.setter
    def DataNodeNum(self, DataNodeNum):
        self._DataNodeNum = DataNodeNum

    @property
    def IndexNum(self):
        r"""Number of indices
        :rtype: int
        """
        return self._IndexNum

    @IndexNum.setter
    def IndexNum(self, IndexNum):
        self._IndexNum = IndexNum

    @property
    def DocNum(self):
        r"""Number of documents
        :rtype: int
        """
        return self._DocNum

    @DocNum.setter
    def DocNum(self, DocNum):
        self._DocNum = DocNum

    @property
    def DiskUsedInBytes(self):
        r"""Used disk size (in bytes)
        :rtype: int
        """
        return self._DiskUsedInBytes

    @DiskUsedInBytes.setter
    def DiskUsedInBytes(self, DiskUsedInBytes):
        self._DiskUsedInBytes = DiskUsedInBytes

    @property
    def ShardNum(self):
        r"""Number of shards
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def PrimaryShardNum(self):
        r"""Number of primary shards
        :rtype: int
        """
        return self._PrimaryShardNum

    @PrimaryShardNum.setter
    def PrimaryShardNum(self, PrimaryShardNum):
        self._PrimaryShardNum = PrimaryShardNum

    @property
    def RelocatingShardNum(self):
        r"""Number of relocating shards
        :rtype: int
        """
        return self._RelocatingShardNum

    @RelocatingShardNum.setter
    def RelocatingShardNum(self, RelocatingShardNum):
        self._RelocatingShardNum = RelocatingShardNum

    @property
    def InitializingShardNum(self):
        r"""Number of initializing shards
        :rtype: int
        """
        return self._InitializingShardNum

    @InitializingShardNum.setter
    def InitializingShardNum(self, InitializingShardNum):
        self._InitializingShardNum = InitializingShardNum

    @property
    def UnassignedShardNum(self):
        r"""Number of unassigned shards
        :rtype: int
        """
        return self._UnassignedShardNum

    @UnassignedShardNum.setter
    def UnassignedShardNum(self, UnassignedShardNum):
        self._UnassignedShardNum = UnassignedShardNum

    @property
    def TotalCosStorage(self):
        r"""Total COS storage of an enterprise cluster, in GB
        :rtype: int
        """
        return self._TotalCosStorage

    @TotalCosStorage.setter
    def TotalCosStorage(self, TotalCosStorage):
        self._TotalCosStorage = TotalCosStorage

    @property
    def SearchableSnapshotCosBucket(self):
        r"""Name of the COS bucket that stores searchable snapshots of an enterprise cluster
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SearchableSnapshotCosBucket

    @SearchableSnapshotCosBucket.setter
    def SearchableSnapshotCosBucket(self, SearchableSnapshotCosBucket):
        self._SearchableSnapshotCosBucket = SearchableSnapshotCosBucket

    @property
    def SearchableSnapshotCosAppId(self):
        r"""COS app ID of the searchable snapshots of an enterprise cluster
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SearchableSnapshotCosAppId

    @SearchableSnapshotCosAppId.setter
    def SearchableSnapshotCosAppId(self, SearchableSnapshotCosAppId):
        self._SearchableSnapshotCosAppId = SearchableSnapshotCosAppId


    def _deserialize(self, params):
        self._Health = params.get("Health")
        self._Visible = params.get("Visible")
        self._Break = params.get("Break")
        self._AvgDiskUsage = params.get("AvgDiskUsage")
        self._AvgMemUsage = params.get("AvgMemUsage")
        self._AvgCpuUsage = params.get("AvgCpuUsage")
        self._TotalDiskSize = params.get("TotalDiskSize")
        self._TargetNodeTypes = params.get("TargetNodeTypes")
        self._NodeNum = params.get("NodeNum")
        self._TotalNodeNum = params.get("TotalNodeNum")
        self._DataNodeNum = params.get("DataNodeNum")
        self._IndexNum = params.get("IndexNum")
        self._DocNum = params.get("DocNum")
        self._DiskUsedInBytes = params.get("DiskUsedInBytes")
        self._ShardNum = params.get("ShardNum")
        self._PrimaryShardNum = params.get("PrimaryShardNum")
        self._RelocatingShardNum = params.get("RelocatingShardNum")
        self._InitializingShardNum = params.get("InitializingShardNum")
        self._UnassignedShardNum = params.get("UnassignedShardNum")
        self._TotalCosStorage = params.get("TotalCosStorage")
        self._SearchableSnapshotCosBucket = params.get("SearchableSnapshotCosBucket")
        self._SearchableSnapshotCosAppId = params.get("SearchableSnapshotCosAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosBackup(AbstractModel):
    r"""Auto-backup to COS for ES

    """

    def __init__(self):
        r"""
        :param _IsAutoBackup: Whether to enable auto-backup to COS
        :type IsAutoBackup: bool
        :param _BackupTime: Auto-backup time (accurate down to the hour), such as "22:00"
        :type BackupTime: str
        """
        self._IsAutoBackup = None
        self._BackupTime = None

    @property
    def IsAutoBackup(self):
        r"""Whether to enable auto-backup to COS
        :rtype: bool
        """
        return self._IsAutoBackup

    @IsAutoBackup.setter
    def IsAutoBackup(self, IsAutoBackup):
        self._IsAutoBackup = IsAutoBackup

    @property
    def BackupTime(self):
        r"""Auto-backup time (accurate down to the hour), such as "22:00"
        :rtype: str
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime


    def _deserialize(self, params):
        self._IsAutoBackup = params.get("IsAutoBackup")
        self._BackupTime = params.get("BackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexRequest(AbstractModel):
    r"""CreateIndex request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES cluster ID
        :type InstanceId: str
        :param _IndexType: Type of the index to create. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param _IndexName: Name of the index to create
        :type IndexName: str
        :param _IndexMetaJson: JSON-formatted index metadata to create, such as `mappings` and `settings`
        :type IndexMetaJson: str
        :param _Username: Username for cluster access
        :type Username: str
        :param _Password: Password for cluster access
        :type Password: str
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._IndexMetaJson = None
        self._Username = None
        self._Password = None

    @property
    def InstanceId(self):
        r"""ES cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        r"""Type of the index to create. `auto`: Automated; `normal`: General.
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""Name of the index to create
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexMetaJson(self):
        r"""JSON-formatted index metadata to create, such as `mappings` and `settings`
        :rtype: str
        """
        return self._IndexMetaJson

    @IndexMetaJson.setter
    def IndexMetaJson(self, IndexMetaJson):
        self._IndexMetaJson = IndexMetaJson

    @property
    def Username(self):
        r"""Username for cluster access
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""Password for cluster access
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._IndexMetaJson = params.get("IndexMetaJson")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexResponse(AbstractModel):
    r"""CreateIndex response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    r"""CreateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Availability Zone
        :type Zone: str
        :param _EsVersion: Instance version. Valid values: `5.6.4`, `6.4.3`, `6.8.2`, `7.5.1`, `7.10.1`
        :type EsVersion: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _Password: Access password, which must contain 8 to 16 characters, and include at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]
        :type Password: str
        :param _InstanceName: Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)
        :type InstanceName: str
        :param _NodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2-50)
        :type NodeNum: int
        :param _ChargeType: Billing mode <li>POSTPAID_BY_HOUR: Pay-as-you-go hourly </li>Default value: POSTPAID_BY_HOUR
        :type ChargeType: str
        :param _ChargePeriod: This parameter is not used on the global website
        :type ChargePeriod: int
        :param _RenewFlag: This parameter is not used on the global website
        :type RenewFlag: str
        :param _NodeType: This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param _DiskType: This parameter has been disused. Please use `NodeInfoList`
Node storage type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: premium cloud storage </li>Default value: CLOUD_SSD
        :type DiskType: str
        :param _DiskSize: This parameter has been disused. Please use `NodeInfoList`
Node disk size in GB
        :type DiskSize: int
        :param _TimeUnit: This parameter is not used on the global website
        :type TimeUnit: str
        :param _AutoVoucher: Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0
        :type AutoVoucher: int
        :param _VoucherIds: List of voucher IDs (only one voucher can be specified at a time currently)
        :type VoucherIds: list of str
        :param _EnableDedicatedMaster: This parameter has been disused. Please use `NodeInfoList`
Whether to create a dedicated primary node <li>true: yes </li><li>false: no </li>Default value: false
        :type EnableDedicatedMaster: bool
        :param _MasterNodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of dedicated primary nodes (only 3 and 5 are supported. This value must be passed in if `EnableDedicatedMaster` is `true`)
        :type MasterNodeNum: int
        :param _MasterNodeType: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node type, which must be passed in if `EnableDedicatedMaster` is `true` <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :type MasterNodeType: str
        :param _MasterNodeDiskSize: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node disk size in GB, which is optional. If passed in, it can only be 50 and cannot be customized currently
        :type MasterNodeDiskSize: int
        :param _ClusterNameInConf: ClusterName in the cluster configuration file, which is the instance ID by default and currently cannot be customized
        :type ClusterNameInConf: str
        :param _DeployMode: Cluster deployment mode <li>0: single-AZ deployment </li><li>1: multi-AZ deployment </li>Default value: 0
        :type DeployMode: int
        :param _MultiZoneInfo: Details of AZs in multi-AZ deployment mode (which is required when DeployMode is 1)
        :type MultiZoneInfo: list of ZoneDetail
        :param _LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :type LicenseType: str
        :param _NodeInfoList: Node information list, which is used to describe the specification information of various types of nodes in the cluster, such as node type, node quantity, node specification, disk type, and disk size
        :type NodeInfoList: list of NodeInfo
        :param _TagList: Node tag information list
        :type TagList: list of TagInfo
        :param _BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :type BasicSecurityType: int
        :param _SceneType: Scenario template type. 0: not enabled; 1: general; 2: log; 3: search
        :type SceneType: int
        :param _WebNodeTypeInfo: Visual node configuration
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param _Protocol: Valid values: `https`, `http` (default)
        :type Protocol: str
        :param _OperationDuration: The maintenance time slot
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param _EnableHybridStorage: Whether to enable the storage-computing separation feature.
        :type EnableHybridStorage: bool
        :param _DiskEnhance: Whether to enable enhanced SSD
        :type DiskEnhance: int
        :param _EnableDiagnose: Whether to enable smart inspection.
        :type EnableDiagnose: bool
        """
        self._Zone = None
        self._EsVersion = None
        self._VpcId = None
        self._SubnetId = None
        self._Password = None
        self._InstanceName = None
        self._NodeNum = None
        self._ChargeType = None
        self._ChargePeriod = None
        self._RenewFlag = None
        self._NodeType = None
        self._DiskType = None
        self._DiskSize = None
        self._TimeUnit = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._EnableDedicatedMaster = None
        self._MasterNodeNum = None
        self._MasterNodeType = None
        self._MasterNodeDiskSize = None
        self._ClusterNameInConf = None
        self._DeployMode = None
        self._MultiZoneInfo = None
        self._LicenseType = None
        self._NodeInfoList = None
        self._TagList = None
        self._BasicSecurityType = None
        self._SceneType = None
        self._WebNodeTypeInfo = None
        self._Protocol = None
        self._OperationDuration = None
        self._EnableHybridStorage = None
        self._DiskEnhance = None
        self._EnableDiagnose = None

    @property
    def Zone(self):
        r"""Availability Zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def EsVersion(self):
        r"""Instance version. Valid values: `5.6.4`, `6.4.3`, `6.8.2`, `7.5.1`, `7.10.1`
        :rtype: str
        """
        return self._EsVersion

    @EsVersion.setter
    def EsVersion(self, EsVersion):
        self._EsVersion = EsVersion

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Password(self):
        r"""Access password, which must contain 8 to 16 characters, and include at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InstanceName(self):
        r"""Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NodeNum(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2-50)
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def ChargeType(self):
        r"""Billing mode <li>POSTPAID_BY_HOUR: Pay-as-you-go hourly </li>Default value: POSTPAID_BY_HOUR
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePeriod(self):
        r"""This parameter is not used on the global website
        :rtype: int
        """
        return self._ChargePeriod

    @ChargePeriod.setter
    def ChargePeriod(self, ChargePeriod):
        self._ChargePeriod = ChargePeriod

    @property
    def RenewFlag(self):
        r"""This parameter is not used on the global website
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def NodeType(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def DiskType(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Node storage type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: premium cloud storage </li>Default value: CLOUD_SSD
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Node disk size in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def TimeUnit(self):
        r"""This parameter is not used on the global website
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""List of voucher IDs (only one voucher can be specified at a time currently)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def EnableDedicatedMaster(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Whether to create a dedicated primary node <li>true: yes </li><li>false: no </li>Default value: false
        :rtype: bool
        """
        return self._EnableDedicatedMaster

    @EnableDedicatedMaster.setter
    def EnableDedicatedMaster(self, EnableDedicatedMaster):
        self._EnableDedicatedMaster = EnableDedicatedMaster

    @property
    def MasterNodeNum(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Number of dedicated primary nodes (only 3 and 5 are supported. This value must be passed in if `EnableDedicatedMaster` is `true`)
        :rtype: int
        """
        return self._MasterNodeNum

    @MasterNodeNum.setter
    def MasterNodeNum(self, MasterNodeNum):
        self._MasterNodeNum = MasterNodeNum

    @property
    def MasterNodeType(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node type, which must be passed in if `EnableDedicatedMaster` is `true` <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :rtype: str
        """
        return self._MasterNodeType

    @MasterNodeType.setter
    def MasterNodeType(self, MasterNodeType):
        self._MasterNodeType = MasterNodeType

    @property
    def MasterNodeDiskSize(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node disk size in GB, which is optional. If passed in, it can only be 50 and cannot be customized currently
        :rtype: int
        """
        return self._MasterNodeDiskSize

    @MasterNodeDiskSize.setter
    def MasterNodeDiskSize(self, MasterNodeDiskSize):
        self._MasterNodeDiskSize = MasterNodeDiskSize

    @property
    def ClusterNameInConf(self):
        r"""ClusterName in the cluster configuration file, which is the instance ID by default and currently cannot be customized
        :rtype: str
        """
        return self._ClusterNameInConf

    @ClusterNameInConf.setter
    def ClusterNameInConf(self, ClusterNameInConf):
        self._ClusterNameInConf = ClusterNameInConf

    @property
    def DeployMode(self):
        r"""Cluster deployment mode <li>0: single-AZ deployment </li><li>1: multi-AZ deployment </li>Default value: 0
        :rtype: int
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def MultiZoneInfo(self):
        r"""Details of AZs in multi-AZ deployment mode (which is required when DeployMode is 1)
        :rtype: list of ZoneDetail
        """
        return self._MultiZoneInfo

    @MultiZoneInfo.setter
    def MultiZoneInfo(self, MultiZoneInfo):
        self._MultiZoneInfo = MultiZoneInfo

    @property
    def LicenseType(self):
        r"""License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def NodeInfoList(self):
        r"""Node information list, which is used to describe the specification information of various types of nodes in the cluster, such as node type, node quantity, node specification, disk type, and disk size
        :rtype: list of NodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList

    @property
    def TagList(self):
        r"""Node tag information list
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def BasicSecurityType(self):
        r"""Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def SceneType(self):
        r"""Scenario template type. 0: not enabled; 1: general; 2: log; 3: search
        :rtype: int
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def WebNodeTypeInfo(self):
        r"""Visual node configuration
        :rtype: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        """
        return self._WebNodeTypeInfo

    @WebNodeTypeInfo.setter
    def WebNodeTypeInfo(self, WebNodeTypeInfo):
        self._WebNodeTypeInfo = WebNodeTypeInfo

    @property
    def Protocol(self):
        r"""Valid values: `https`, `http` (default)
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OperationDuration(self):
        r"""The maintenance time slot
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def EnableHybridStorage(self):
        r"""Whether to enable the storage-computing separation feature.
        :rtype: bool
        """
        return self._EnableHybridStorage

    @EnableHybridStorage.setter
    def EnableHybridStorage(self, EnableHybridStorage):
        self._EnableHybridStorage = EnableHybridStorage

    @property
    def DiskEnhance(self):
        r"""Whether to enable enhanced SSD
        :rtype: int
        """
        return self._DiskEnhance

    @DiskEnhance.setter
    def DiskEnhance(self, DiskEnhance):
        self._DiskEnhance = DiskEnhance

    @property
    def EnableDiagnose(self):
        r"""Whether to enable smart inspection.
        :rtype: bool
        """
        return self._EnableDiagnose

    @EnableDiagnose.setter
    def EnableDiagnose(self, EnableDiagnose):
        self._EnableDiagnose = EnableDiagnose


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._EsVersion = params.get("EsVersion")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Password = params.get("Password")
        self._InstanceName = params.get("InstanceName")
        self._NodeNum = params.get("NodeNum")
        self._ChargeType = params.get("ChargeType")
        self._ChargePeriod = params.get("ChargePeriod")
        self._RenewFlag = params.get("RenewFlag")
        self._NodeType = params.get("NodeType")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._TimeUnit = params.get("TimeUnit")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self._MasterNodeNum = params.get("MasterNodeNum")
        self._MasterNodeType = params.get("MasterNodeType")
        self._MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self._ClusterNameInConf = params.get("ClusterNameInConf")
        self._DeployMode = params.get("DeployMode")
        if params.get("MultiZoneInfo") is not None:
            self._MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self._MultiZoneInfo.append(obj)
        self._LicenseType = params.get("LicenseType")
        if params.get("NodeInfoList") is not None:
            self._NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfoList.append(obj)
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._BasicSecurityType = params.get("BasicSecurityType")
        self._SceneType = params.get("SceneType")
        if params.get("WebNodeTypeInfo") is not None:
            self._WebNodeTypeInfo = WebNodeTypeInfo()
            self._WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self._Protocol = params.get("Protocol")
        if params.get("OperationDuration") is not None:
            self._OperationDuration = OperationDuration()
            self._OperationDuration._deserialize(params.get("OperationDuration"))
        self._EnableHybridStorage = params.get("EnableHybridStorage")
        self._DiskEnhance = params.get("DiskEnhance")
        self._EnableDiagnose = params.get("EnableDiagnose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    r"""CreateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DealName: Order ID
Note: This field may return `null`, indicating that no valid value was found.
        :type DealName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._DealName = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealName(self):
        r"""Order ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class DeleteIndexRequest(AbstractModel):
    r"""DeleteIndex request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES cluster ID
        :type InstanceId: str
        :param _IndexType: Type of the index to delete. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param _IndexName: Name of the index to delete
        :type IndexName: str
        :param _Username: Username for cluster access
        :type Username: str
        :param _Password: Password for cluster access
        :type Password: str
        :param _BackingIndexName: Backing index name
        :type BackingIndexName: str
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._Username = None
        self._Password = None
        self._BackingIndexName = None

    @property
    def InstanceId(self):
        r"""ES cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        r"""Type of the index to delete. `auto`: Automated; `normal`: General.
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""Name of the index to delete
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Username(self):
        r"""Username for cluster access
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""Password for cluster access
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def BackingIndexName(self):
        r"""Backing index name
        :rtype: str
        """
        return self._BackingIndexName

    @BackingIndexName.setter
    def BackingIndexName(self, BackingIndexName):
        self._BackingIndexName = BackingIndexName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._BackingIndexName = params.get("BackingIndexName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIndexResponse(AbstractModel):
    r"""DeleteIndex response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    r"""DeleteInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    r"""DeleteInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeIndexListRequest(AbstractModel):
    r"""DescribeIndexList request structure.

    """

    def __init__(self):
        r"""
        :param _IndexType: Index type. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param _InstanceId: ES cluster ID
        :type InstanceId: str
        :param _IndexName: Index name. `null` indicates that all indexes are requested.
        :type IndexName: str
        :param _Username: Username for cluster access
        :type Username: str
        :param _Password: Password for cluster access
        :type Password: str
        :param _Offset: The starting position of paging
        :type Offset: int
        :param _Limit: The number of results per page
        :type Limit: int
        :param _OrderBy: Sorting condition field, which can be `IndexName`, `IndexStorage`, or `IndexCreateTime`.
        :type OrderBy: str
        :param _IndexStatusList: Filtering by index status
        :type IndexStatusList: list of str
        :param _Order: Sorting mode, which can be `asc` and `desc`.
        :type Order: str
        """
        self._IndexType = None
        self._InstanceId = None
        self._IndexName = None
        self._Username = None
        self._Password = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._IndexStatusList = None
        self._Order = None

    @property
    def IndexType(self):
        r"""Index type. `auto`: Automated; `normal`: General.
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def InstanceId(self):
        r"""ES cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexName(self):
        r"""Index name. `null` indicates that all indexes are requested.
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Username(self):
        r"""Username for cluster access
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""Password for cluster access
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Offset(self):
        r"""The starting position of paging
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""The number of results per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        r"""Sorting condition field, which can be `IndexName`, `IndexStorage`, or `IndexCreateTime`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def IndexStatusList(self):
        r"""Filtering by index status
        :rtype: list of str
        """
        return self._IndexStatusList

    @IndexStatusList.setter
    def IndexStatusList(self, IndexStatusList):
        self._IndexStatusList = IndexStatusList

    @property
    def Order(self):
        r"""Sorting mode, which can be `asc` and `desc`.
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._IndexType = params.get("IndexType")
        self._InstanceId = params.get("InstanceId")
        self._IndexName = params.get("IndexName")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._IndexStatusList = params.get("IndexStatusList")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexListResponse(AbstractModel):
    r"""DescribeIndexList response structure.

    """

    def __init__(self):
        r"""
        :param _IndexMetaFields: Index metadata field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexMetaFields: list of IndexMetaField
        :param _TotalCount: Total number of results
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IndexMetaFields = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def IndexMetaFields(self):
        r"""Index metadata field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of IndexMetaField
        """
        return self._IndexMetaFields

    @IndexMetaFields.setter
    def IndexMetaFields(self, IndexMetaFields):
        self._IndexMetaFields = IndexMetaFields

    @property
    def TotalCount(self):
        r"""Total number of results
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IndexMetaFields") is not None:
            self._IndexMetaFields = []
            for item in params.get("IndexMetaFields"):
                obj = IndexMetaField()
                obj._deserialize(item)
                self._IndexMetaFields.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIndexMetaRequest(AbstractModel):
    r"""DescribeIndexMeta request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES cluster ID
        :type InstanceId: str
        :param _IndexType: Index type. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param _IndexName: Index name. `null` indicates that all indexes are requested.
        :type IndexName: str
        :param _Username: Username for cluster access
        :type Username: str
        :param _Password: Password for cluster access
        :type Password: str
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._Username = None
        self._Password = None

    @property
    def InstanceId(self):
        r"""ES cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        r"""Index type. `auto`: Automated; `normal`: General.
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""Index name. `null` indicates that all indexes are requested.
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Username(self):
        r"""Username for cluster access
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""Password for cluster access
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexMetaResponse(AbstractModel):
    r"""DescribeIndexMeta response structure.

    """

    def __init__(self):
        r"""
        :param _IndexMetaField: Index metadata field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexMetaField: :class:`tencentcloud.es.v20180416.models.IndexMetaField`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IndexMetaField = None
        self._RequestId = None

    @property
    def IndexMetaField(self):
        r"""Index metadata field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexMetaField`
        """
        return self._IndexMetaField

    @IndexMetaField.setter
    def IndexMetaField(self, IndexMetaField):
        self._IndexMetaField = IndexMetaField

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IndexMetaField") is not None:
            self._IndexMetaField = IndexMetaField()
            self._IndexMetaField._deserialize(params.get("IndexMetaField"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    r"""DescribeInstanceLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        :param _LogType: Log type. Default value: 1
<li>1: primary log</li>
<li>2: search slow log</li>
<li>3: index slow log</li>
<li>4: GC log</li>
        :type LogType: int
        :param _SearchKey: Search keyword, which supports LUCENE syntax, such as `level:WARN`, `ip:1.1.1.1`, and `message:test-index`
        :type SearchKey: str
        :param _StartTime: Log start time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53
        :type StartTime: str
        :param _EndTime: Log end time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53
        :type EndTime: str
        :param _Offset: Pagination start value. Default value: 0
        :type Offset: int
        :param _Limit: Number of entries per page. Default value: 100. Maximum value: 100
        :type Limit: int
        :param _OrderByType: Time sorting order. Default value: 0
<li>0: descending</li>
<li>1: ascending</li>
        :type OrderByType: int
        """
        self._InstanceId = None
        self._LogType = None
        self._SearchKey = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        r"""Cluster instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogType(self):
        r"""Log type. Default value: 1
<li>1: primary log</li>
<li>2: search slow log</li>
<li>3: index slow log</li>
<li>4: GC log</li>
        :rtype: int
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def SearchKey(self):
        r"""Search keyword, which supports LUCENE syntax, such as `level:WARN`, `ip:1.1.1.1`, and `message:test-index`
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def StartTime(self):
        r"""Log start time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Log end time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""Pagination start value. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries per page. Default value: 100. Maximum value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByType(self):
        r"""Time sorting order. Default value: 0
<li>0: descending</li>
<li>1: ascending</li>
        :rtype: int
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogType = params.get("LogType")
        self._SearchKey = params.get("SearchKey")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogsResponse(AbstractModel):
    r"""DescribeInstanceLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of returned logs
        :type TotalCount: int
        :param _InstanceLogList: Log details list
        :type InstanceLogList: list of InstanceLog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceLogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of returned logs
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceLogList(self):
        r"""Log details list
        :rtype: list of InstanceLog
        """
        return self._InstanceLogList

    @InstanceLogList.setter
    def InstanceLogList(self, InstanceLogList):
        self._InstanceLogList = InstanceLogList

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceLogList") is not None:
            self._InstanceLogList = []
            for item in params.get("InstanceLogList"):
                obj = InstanceLog()
                obj._deserialize(item)
                self._InstanceLogList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    r"""DescribeInstanceOperations request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        :param _StartTime: Start time, such as "2019-03-07 16:30:39"
        :type StartTime: str
        :param _EndTime: End time, such as "2019-03-30 20:18:03"
        :type EndTime: str
        :param _Offset: Pagination start value
        :type Offset: int
        :param _Limit: Number of entries per page
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""Cluster instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Start time, such as "2019-03-07 16:30:39"
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time, such as "2019-03-30 20:18:03"
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""Pagination start value
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceOperationsResponse(AbstractModel):
    r"""DescribeInstanceOperations response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of operation records
        :type TotalCount: int
        :param _Operations: Operation history
        :type Operations: list of Operation
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Operations = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of operation records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Operations(self):
        r"""Operation history
        :rtype: list of Operation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self._Operations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ of the cluster instance. If this is not passed in, all AZs are used by default
        :type Zone: str
        :param _InstanceIds: List of cluster instance IDs
        :type InstanceIds: list of str
        :param _InstanceNames: List of cluster instance names
        :type InstanceNames: list of str
        :param _Offset: Pagination start value. Default value: 0
        :type Offset: int
        :param _Limit: Number of entries per page. Default value: 20
        :type Limit: int
        :param _OrderByKey: The sorting field. <li>1: Instance ID </li><li>2: Instance name </li><li>3: AZ </li><li>4: Creation time </li>If `OrderByKey` is not passed in, sorting is performed by creation time in descending order.
        :type OrderByKey: int
        :param _OrderByType: Sorting order <li>0: ascending </li><li>1: descending </li>If orderByKey is passed in but orderByType is not, ascending order is used by default
        :type OrderByType: int
        :param _TagList: Node tag information list
        :type TagList: list of TagInfo
        :param _IpList: VPC VIP list
        :type IpList: list of str
        :param _ZoneList: List of availability zones
        :type ZoneList: list of str
        :param _HealthStatus: The health status filter. Valid values: `0` (green), `1` (yellow), `2` (red), `-1` (unknown).
        :type HealthStatus: list of int
        :param _VpcIds: VPC IDs
        :type VpcIds: list of str
        """
        self._Zone = None
        self._InstanceIds = None
        self._InstanceNames = None
        self._Offset = None
        self._Limit = None
        self._OrderByKey = None
        self._OrderByType = None
        self._TagList = None
        self._IpList = None
        self._ZoneList = None
        self._HealthStatus = None
        self._VpcIds = None

    @property
    def Zone(self):
        r"""AZ of the cluster instance. If this is not passed in, all AZs are used by default
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceIds(self):
        r"""List of cluster instance IDs
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        r"""List of cluster instance names
        :rtype: list of str
        """
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def Offset(self):
        r"""Pagination start value. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries per page. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByKey(self):
        r"""The sorting field. <li>1: Instance ID </li><li>2: Instance name </li><li>3: AZ </li><li>4: Creation time </li>If `OrderByKey` is not passed in, sorting is performed by creation time in descending order.
        :rtype: int
        """
        return self._OrderByKey

    @OrderByKey.setter
    def OrderByKey(self, OrderByKey):
        self._OrderByKey = OrderByKey

    @property
    def OrderByType(self):
        r"""Sorting order <li>0: ascending </li><li>1: descending </li>If orderByKey is passed in but orderByType is not, ascending order is used by default
        :rtype: int
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def TagList(self):
        r"""Node tag information list
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def IpList(self):
        r"""VPC VIP list
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def ZoneList(self):
        r"""List of availability zones
        :rtype: list of str
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def HealthStatus(self):
        r"""The health status filter. Valid values: `0` (green), `1` (yellow), `2` (red), `-1` (unknown).
        :rtype: list of int
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def VpcIds(self):
        r"""VPC IDs
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByKey = params.get("OrderByKey")
        self._OrderByType = params.get("OrderByType")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._IpList = params.get("IpList")
        self._ZoneList = params.get("ZoneList")
        self._HealthStatus = params.get("HealthStatus")
        self._VpcIds = params.get("VpcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    r"""DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of returned instances
        :type TotalCount: int
        :param _InstanceList: List of instance details
        :type InstanceList: list of InstanceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of returned instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        r"""List of instance details
        :rtype: list of InstanceInfo
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeViewsRequest(AbstractModel):
    r"""DescribeViews request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Cluster instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeViewsResponse(AbstractModel):
    r"""DescribeViews response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterView: Cluster view
Note: This field may return `null`, indicating that no valid value was found.
        :type ClusterView: :class:`tencentcloud.es.v20180416.models.ClusterView`
        :param _NodesView: Node view
Note: This field may return `null`, indicating that no valid value was found.
        :type NodesView: list of NodeView
        :param _KibanasView: Kibana view
Note: This field may return `null`, indicating that no valid value was found.
        :type KibanasView: list of KibanaView
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterView = None
        self._NodesView = None
        self._KibanasView = None
        self._RequestId = None

    @property
    def ClusterView(self):
        r"""Cluster view
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: :class:`tencentcloud.es.v20180416.models.ClusterView`
        """
        return self._ClusterView

    @ClusterView.setter
    def ClusterView(self, ClusterView):
        self._ClusterView = ClusterView

    @property
    def NodesView(self):
        r"""Node view
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of NodeView
        """
        return self._NodesView

    @NodesView.setter
    def NodesView(self, NodesView):
        self._NodesView = NodesView

    @property
    def KibanasView(self):
        r"""Kibana view
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of KibanaView
        """
        return self._KibanasView

    @KibanasView.setter
    def KibanasView(self, KibanasView):
        self._KibanasView = KibanasView

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterView") is not None:
            self._ClusterView = ClusterView()
            self._ClusterView._deserialize(params.get("ClusterView"))
        if params.get("NodesView") is not None:
            self._NodesView = []
            for item in params.get("NodesView"):
                obj = NodeView()
                obj._deserialize(item)
                self._NodesView.append(obj)
        if params.get("KibanasView") is not None:
            self._KibanasView = []
            for item in params.get("KibanasView"):
                obj = KibanaView()
                obj._deserialize(item)
                self._KibanasView.append(obj)
        self._RequestId = params.get("RequestId")


class DictInfo(AbstractModel):
    r"""Information of the IK plugin dictionary

    """

    def __init__(self):
        r"""
        :param _Key: Dictionary key value
        :type Key: str
        :param _Name: Dictionary name
        :type Name: str
        :param _Size: Dictionary size in B
        :type Size: int
        """
        self._Key = None
        self._Name = None
        self._Size = None

    @property
    def Key(self):
        r"""Dictionary key value
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Name(self):
        r"""Dictionary name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        r"""Dictionary size in B
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsAcl(AbstractModel):
    r"""ES cluster configuration item

    """

    def __init__(self):
        r"""
        :param _BlackIpList: Kibana access blocklist
        :type BlackIpList: list of str
        :param _WhiteIpList: Kibana access allowlist
        :type WhiteIpList: list of str
        """
        self._BlackIpList = None
        self._WhiteIpList = None

    @property
    def BlackIpList(self):
        r"""Kibana access blocklist
        :rtype: list of str
        """
        return self._BlackIpList

    @BlackIpList.setter
    def BlackIpList(self, BlackIpList):
        self._BlackIpList = BlackIpList

    @property
    def WhiteIpList(self):
        r"""Kibana access allowlist
        :rtype: list of str
        """
        return self._WhiteIpList

    @WhiteIpList.setter
    def WhiteIpList(self, WhiteIpList):
        self._WhiteIpList = WhiteIpList


    def _deserialize(self, params):
        self._BlackIpList = params.get("BlackIpList")
        self._WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsConfigSetInfo(AbstractModel):
    r"""Configuration set information

    """

    def __init__(self):
        r"""
        :param _Type: Configuration set type, such as `LDAP` and `AD`.
        :type Type: str
        :param _EsConfig: "{\"order\":0,\"url\":\"ldap://10.0.1.72:389\",\"bind_dn\":\"cn=admin,dc=tencent,dc=com\",\"user_search.base_dn\":\"dc=tencent,dc=com\",\"user_search.filter\":\"(cn={0})\",\"group_search.base_dn\":\"dc=tencent,dc=com\"}"
        :type EsConfig: str
        """
        self._Type = None
        self._EsConfig = None

    @property
    def Type(self):
        r"""Configuration set type, such as `LDAP` and `AD`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EsConfig(self):
        r""""{\"order\":0,\"url\":\"ldap://10.0.1.72:389\",\"bind_dn\":\"cn=admin,dc=tencent,dc=com\",\"user_search.base_dn\":\"dc=tencent,dc=com\",\"user_search.filter\":\"(cn={0})\",\"group_search.base_dn\":\"dc=tencent,dc=com\"}"
        :rtype: str
        """
        return self._EsConfig

    @EsConfig.setter
    def EsConfig(self, EsConfig):
        self._EsConfig = EsConfig


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._EsConfig = params.get("EsConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsDictionaryInfo(AbstractModel):
    r"""ES dictionary information

    """

    def __init__(self):
        r"""
        :param _MainDict: List of non-stop words
        :type MainDict: list of DictInfo
        :param _Stopwords: List of stop words
        :type Stopwords: list of DictInfo
        :param _QQDict: QQ dictionary list
        :type QQDict: list of DictInfo
        :param _Synonym: Synonym dictionary list
        :type Synonym: list of DictInfo
        :param _UpdateType: Update dictionary type
        :type UpdateType: str
        """
        self._MainDict = None
        self._Stopwords = None
        self._QQDict = None
        self._Synonym = None
        self._UpdateType = None

    @property
    def MainDict(self):
        r"""List of non-stop words
        :rtype: list of DictInfo
        """
        return self._MainDict

    @MainDict.setter
    def MainDict(self, MainDict):
        self._MainDict = MainDict

    @property
    def Stopwords(self):
        r"""List of stop words
        :rtype: list of DictInfo
        """
        return self._Stopwords

    @Stopwords.setter
    def Stopwords(self, Stopwords):
        self._Stopwords = Stopwords

    @property
    def QQDict(self):
        r"""QQ dictionary list
        :rtype: list of DictInfo
        """
        return self._QQDict

    @QQDict.setter
    def QQDict(self, QQDict):
        self._QQDict = QQDict

    @property
    def Synonym(self):
        r"""Synonym dictionary list
        :rtype: list of DictInfo
        """
        return self._Synonym

    @Synonym.setter
    def Synonym(self, Synonym):
        self._Synonym = Synonym

    @property
    def UpdateType(self):
        r"""Update dictionary type
        :rtype: str
        """
        return self._UpdateType

    @UpdateType.setter
    def UpdateType(self, UpdateType):
        self._UpdateType = UpdateType


    def _deserialize(self, params):
        if params.get("MainDict") is not None:
            self._MainDict = []
            for item in params.get("MainDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self._MainDict.append(obj)
        if params.get("Stopwords") is not None:
            self._Stopwords = []
            for item in params.get("Stopwords"):
                obj = DictInfo()
                obj._deserialize(item)
                self._Stopwords.append(obj)
        if params.get("QQDict") is not None:
            self._QQDict = []
            for item in params.get("QQDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self._QQDict.append(obj)
        if params.get("Synonym") is not None:
            self._Synonym = []
            for item in params.get("Synonym"):
                obj = DictInfo()
                obj._deserialize(item)
                self._Synonym.append(obj)
        self._UpdateType = params.get("UpdateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsPublicAcl(AbstractModel):
    r"""Public network ACL information of ES

    """

    def __init__(self):
        r"""
        :param _BlackIpList: Access blocklist
        :type BlackIpList: list of str
        :param _WhiteIpList: Access allowlist
        :type WhiteIpList: list of str
        """
        self._BlackIpList = None
        self._WhiteIpList = None

    @property
    def BlackIpList(self):
        r"""Access blocklist
        :rtype: list of str
        """
        return self._BlackIpList

    @BlackIpList.setter
    def BlackIpList(self, BlackIpList):
        self._BlackIpList = BlackIpList

    @property
    def WhiteIpList(self):
        r"""Access allowlist
        :rtype: list of str
        """
        return self._WhiteIpList

    @WhiteIpList.setter
    def WhiteIpList(self, WhiteIpList):
        self._WhiteIpList = WhiteIpList


    def _deserialize(self, params):
        self._BlackIpList = params.get("BlackIpList")
        self._WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesRequest(AbstractModel):
    r"""GetRequestTargetNodeTypes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesResponse(AbstractModel):
    r"""GetRequestTargetNodeTypes response structure.

    """

    def __init__(self):
        r"""
        :param _TargetNodeTypes: A list of node types used to receive requests.
        :type TargetNodeTypes: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TargetNodeTypes = None
        self._RequestId = None

    @property
    def TargetNodeTypes(self):
        r"""A list of node types used to receive requests.
        :rtype: list of str
        """
        return self._TargetNodeTypes

    @TargetNodeTypes.setter
    def TargetNodeTypes(self, TargetNodeTypes):
        self._TargetNodeTypes = TargetNodeTypes

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TargetNodeTypes = params.get("TargetNodeTypes")
        self._RequestId = params.get("RequestId")


class IndexMetaField(AbstractModel):
    r"""Index metadata field

    """

    def __init__(self):
        r"""
        :param _IndexType: Index type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexType: str
        :param _IndexName: Index name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexName: str
        :param _IndexStatus: Index status
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexStatus: str
        :param _IndexStorage: Index size (in byte)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexStorage: int
        :param _IndexCreateTime: Index creation time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexCreateTime: str
        :param _BackingIndices: Backing index
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BackingIndices: list of BackingIndexMetaField
        :param _ClusterId: Cluster ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterId: str
        :param _ClusterName: Cluster name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterName: str
        :param _ClusterVersion: Cluster version
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterVersion: str
        :param _IndexPolicyField: Index lifecycle policy field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexPolicyField: :class:`tencentcloud.es.v20180416.models.IndexPolicyField`
        :param _IndexOptionsField: Index automation field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexOptionsField: :class:`tencentcloud.es.v20180416.models.IndexOptionsField`
        :param _IndexSettingsField: Index setting field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IndexSettingsField: :class:`tencentcloud.es.v20180416.models.IndexSettingsField`
        :param _AppId: Cluster APP ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AppId: int
        :param _IndexDocs: The number of index docs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndexDocs: int
        """
        self._IndexType = None
        self._IndexName = None
        self._IndexStatus = None
        self._IndexStorage = None
        self._IndexCreateTime = None
        self._BackingIndices = None
        self._ClusterId = None
        self._ClusterName = None
        self._ClusterVersion = None
        self._IndexPolicyField = None
        self._IndexOptionsField = None
        self._IndexSettingsField = None
        self._AppId = None
        self._IndexDocs = None

    @property
    def IndexType(self):
        r"""Index type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""Index name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexStatus(self):
        r"""Index status
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus

    @property
    def IndexStorage(self):
        r"""Index size (in byte)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._IndexStorage

    @IndexStorage.setter
    def IndexStorage(self, IndexStorage):
        self._IndexStorage = IndexStorage

    @property
    def IndexCreateTime(self):
        r"""Index creation time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IndexCreateTime

    @IndexCreateTime.setter
    def IndexCreateTime(self, IndexCreateTime):
        self._IndexCreateTime = IndexCreateTime

    @property
    def BackingIndices(self):
        r"""Backing index
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of BackingIndexMetaField
        """
        return self._BackingIndices

    @BackingIndices.setter
    def BackingIndices(self, BackingIndices):
        self._BackingIndices = BackingIndices

    @property
    def ClusterId(self):
        r"""Cluster ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""Cluster name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterVersion(self):
        r"""Cluster version
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def IndexPolicyField(self):
        r"""Index lifecycle policy field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexPolicyField`
        """
        return self._IndexPolicyField

    @IndexPolicyField.setter
    def IndexPolicyField(self, IndexPolicyField):
        self._IndexPolicyField = IndexPolicyField

    @property
    def IndexOptionsField(self):
        r"""Index automation field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexOptionsField`
        """
        return self._IndexOptionsField

    @IndexOptionsField.setter
    def IndexOptionsField(self, IndexOptionsField):
        self._IndexOptionsField = IndexOptionsField

    @property
    def IndexSettingsField(self):
        r"""Index setting field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexSettingsField`
        """
        return self._IndexSettingsField

    @IndexSettingsField.setter
    def IndexSettingsField(self, IndexSettingsField):
        self._IndexSettingsField = IndexSettingsField

    @property
    def AppId(self):
        r"""Cluster APP ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def IndexDocs(self):
        r"""The number of index docs.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IndexDocs

    @IndexDocs.setter
    def IndexDocs(self, IndexDocs):
        self._IndexDocs = IndexDocs


    def _deserialize(self, params):
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._IndexStatus = params.get("IndexStatus")
        self._IndexStorage = params.get("IndexStorage")
        self._IndexCreateTime = params.get("IndexCreateTime")
        if params.get("BackingIndices") is not None:
            self._BackingIndices = []
            for item in params.get("BackingIndices"):
                obj = BackingIndexMetaField()
                obj._deserialize(item)
                self._BackingIndices.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._ClusterVersion = params.get("ClusterVersion")
        if params.get("IndexPolicyField") is not None:
            self._IndexPolicyField = IndexPolicyField()
            self._IndexPolicyField._deserialize(params.get("IndexPolicyField"))
        if params.get("IndexOptionsField") is not None:
            self._IndexOptionsField = IndexOptionsField()
            self._IndexOptionsField._deserialize(params.get("IndexOptionsField"))
        if params.get("IndexSettingsField") is not None:
            self._IndexSettingsField = IndexSettingsField()
            self._IndexSettingsField._deserialize(params.get("IndexSettingsField"))
        self._AppId = params.get("AppId")
        self._IndexDocs = params.get("IndexDocs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexOptionsField(AbstractModel):
    r"""Index automation field

    """

    def __init__(self):
        r"""
        :param _ExpireMaxAge: Max age for expiry purpose
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireMaxAge: str
        :param _ExpireMaxSize: Max size for expiry purpose
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireMaxSize: str
        :param _RolloverMaxAge: Rollover cycle
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RolloverMaxAge: str
        :param _RolloverDynamic: Whether to enable the dynamic rollover
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RolloverDynamic: str
        :param _ShardNumDynamic: Whether to enable dynamic sharding
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ShardNumDynamic: str
        :param _TimestampField: Timestamp field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TimestampField: str
        :param _WriteMode: Write mode
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WriteMode: str
        """
        self._ExpireMaxAge = None
        self._ExpireMaxSize = None
        self._RolloverMaxAge = None
        self._RolloverDynamic = None
        self._ShardNumDynamic = None
        self._TimestampField = None
        self._WriteMode = None

    @property
    def ExpireMaxAge(self):
        r"""Max age for expiry purpose
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ExpireMaxAge

    @ExpireMaxAge.setter
    def ExpireMaxAge(self, ExpireMaxAge):
        self._ExpireMaxAge = ExpireMaxAge

    @property
    def ExpireMaxSize(self):
        r"""Max size for expiry purpose
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ExpireMaxSize

    @ExpireMaxSize.setter
    def ExpireMaxSize(self, ExpireMaxSize):
        self._ExpireMaxSize = ExpireMaxSize

    @property
    def RolloverMaxAge(self):
        r"""Rollover cycle
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RolloverMaxAge

    @RolloverMaxAge.setter
    def RolloverMaxAge(self, RolloverMaxAge):
        self._RolloverMaxAge = RolloverMaxAge

    @property
    def RolloverDynamic(self):
        r"""Whether to enable the dynamic rollover
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RolloverDynamic

    @RolloverDynamic.setter
    def RolloverDynamic(self, RolloverDynamic):
        self._RolloverDynamic = RolloverDynamic

    @property
    def ShardNumDynamic(self):
        r"""Whether to enable dynamic sharding
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ShardNumDynamic

    @ShardNumDynamic.setter
    def ShardNumDynamic(self, ShardNumDynamic):
        self._ShardNumDynamic = ShardNumDynamic

    @property
    def TimestampField(self):
        r"""Timestamp field
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._TimestampField

    @TimestampField.setter
    def TimestampField(self, TimestampField):
        self._TimestampField = TimestampField

    @property
    def WriteMode(self):
        r"""Write mode
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._WriteMode

    @WriteMode.setter
    def WriteMode(self, WriteMode):
        self._WriteMode = WriteMode


    def _deserialize(self, params):
        self._ExpireMaxAge = params.get("ExpireMaxAge")
        self._ExpireMaxSize = params.get("ExpireMaxSize")
        self._RolloverMaxAge = params.get("RolloverMaxAge")
        self._RolloverDynamic = params.get("RolloverDynamic")
        self._ShardNumDynamic = params.get("ShardNumDynamic")
        self._TimestampField = params.get("TimestampField")
        self._WriteMode = params.get("WriteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexPolicyField(AbstractModel):
    r"""Index lifecycle policy field

    """

    def __init__(self):
        r"""
        :param _WarmEnable: Whether to enable the warm phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WarmEnable: str
        :param _WarmMinAge: Min age before data transitions to the warm phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WarmMinAge: str
        :param _ColdEnable: Whether to enable the cold phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ColdEnable: str
        :param _ColdMinAge: Min age before data transitions to the cold phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ColdMinAge: str
        :param _FrozenEnable: Whether to enable the frozen phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FrozenEnable: str
        :param _FrozenMinAge: Min age before data transitions to the frozen phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FrozenMinAge: str
        :param _ColdAction: /
Note: This field may return null, indicating that no valid value can be obtained.
        :type ColdAction: str
        """
        self._WarmEnable = None
        self._WarmMinAge = None
        self._ColdEnable = None
        self._ColdMinAge = None
        self._FrozenEnable = None
        self._FrozenMinAge = None
        self._ColdAction = None

    @property
    def WarmEnable(self):
        r"""Whether to enable the warm phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._WarmEnable

    @WarmEnable.setter
    def WarmEnable(self, WarmEnable):
        self._WarmEnable = WarmEnable

    @property
    def WarmMinAge(self):
        r"""Min age before data transitions to the warm phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._WarmMinAge

    @WarmMinAge.setter
    def WarmMinAge(self, WarmMinAge):
        self._WarmMinAge = WarmMinAge

    @property
    def ColdEnable(self):
        r"""Whether to enable the cold phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ColdEnable

    @ColdEnable.setter
    def ColdEnable(self, ColdEnable):
        self._ColdEnable = ColdEnable

    @property
    def ColdMinAge(self):
        r"""Min age before data transitions to the cold phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ColdMinAge

    @ColdMinAge.setter
    def ColdMinAge(self, ColdMinAge):
        self._ColdMinAge = ColdMinAge

    @property
    def FrozenEnable(self):
        r"""Whether to enable the frozen phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._FrozenEnable

    @FrozenEnable.setter
    def FrozenEnable(self, FrozenEnable):
        self._FrozenEnable = FrozenEnable

    @property
    def FrozenMinAge(self):
        r"""Min age before data transitions to the frozen phase
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._FrozenMinAge

    @FrozenMinAge.setter
    def FrozenMinAge(self, FrozenMinAge):
        self._FrozenMinAge = FrozenMinAge

    @property
    def ColdAction(self):
        r"""/
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ColdAction

    @ColdAction.setter
    def ColdAction(self, ColdAction):
        self._ColdAction = ColdAction


    def _deserialize(self, params):
        self._WarmEnable = params.get("WarmEnable")
        self._WarmMinAge = params.get("WarmMinAge")
        self._ColdEnable = params.get("ColdEnable")
        self._ColdMinAge = params.get("ColdMinAge")
        self._FrozenEnable = params.get("FrozenEnable")
        self._FrozenMinAge = params.get("FrozenMinAge")
        self._ColdAction = params.get("ColdAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexSettingsField(AbstractModel):
    r"""Index configuration fields

    """

    def __init__(self):
        r"""
        :param _NumberOfShards: Number of primary shards
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NumberOfShards: str
        :param _NumberOfReplicas: Number of replica shards
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NumberOfReplicas: str
        :param _RefreshInterval: Index refresh interval
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RefreshInterval: str
        """
        self._NumberOfShards = None
        self._NumberOfReplicas = None
        self._RefreshInterval = None

    @property
    def NumberOfShards(self):
        r"""Number of primary shards
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._NumberOfShards

    @NumberOfShards.setter
    def NumberOfShards(self, NumberOfShards):
        self._NumberOfShards = NumberOfShards

    @property
    def NumberOfReplicas(self):
        r"""Number of replica shards
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._NumberOfReplicas

    @NumberOfReplicas.setter
    def NumberOfReplicas(self, NumberOfReplicas):
        self._NumberOfReplicas = NumberOfReplicas

    @property
    def RefreshInterval(self):
        r"""Index refresh interval
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RefreshInterval

    @RefreshInterval.setter
    def RefreshInterval(self, RefreshInterval):
        self._RefreshInterval = RefreshInterval


    def _deserialize(self, params):
        self._NumberOfShards = params.get("NumberOfShards")
        self._NumberOfReplicas = params.get("NumberOfReplicas")
        self._RefreshInterval = params.get("RefreshInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    r"""Instance details

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Region: Region
        :type Region: str
        :param _Zone: Availability Zone
        :type Zone: str
        :param _AppId: User ID
        :type AppId: int
        :param _Uin: User UIN
        :type Uin: str
        :param _VpcUid: UID of the VPC where the instance resides
        :type VpcUid: str
        :param _SubnetUid: UID of the subnet where the instance resides
        :type SubnetUid: str
        :param _Status: Instance status. `0`: Processing; `1`: Normal; `-1`: `Stopped`; `-2`: Being terminated; `-3`: Terminated; `2`: Initializing during the cluster creation.
        :type Status: int
        :param _RenewFlag: This parameter is not used on the global website
        :type RenewFlag: str
        :param _ChargeType: Instance billing method. Valid values: POSTPAID_BY_HOUR (pay-as-you-go hourly); CDHPAID (billed based on CDH, i.e., only CDH is billed but not the instances on CDH)
        :type ChargeType: str
        :param _ChargePeriod: This parameter is not used on the global website
        :type ChargePeriod: int
        :param _NodeType: Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param _NodeNum: Number of nodes
        :type NodeNum: int
        :param _CpuNum: Number of CPU cores of the node
        :type CpuNum: int
        :param _MemSize: Node memory size in GB
        :type MemSize: int
        :param _DiskType: Node disk type
        :type DiskType: str
        :param _DiskSize: Node disk size in GB
        :type DiskSize: int
        :param _EsDomain: ES domain name
        :type EsDomain: str
        :param _EsVip: ES VIP
        :type EsVip: str
        :param _EsPort: ES port
        :type EsPort: int
        :param _KibanaUrl: Kibana access URL
        :type KibanaUrl: str
        :param _EsVersion: ES version number
        :type EsVersion: str
        :param _EsConfig: ES configuration item
        :type EsConfig: str
        :param _EsAcl: Kibana access control configuration
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _CreateTime: Instance creation time
        :type CreateTime: str
        :param _UpdateTime: Last modified time of the instance
        :type UpdateTime: str
        :param _Deadline: This parameter is not used on the global website
        :type Deadline: str
        :param _InstanceType: Instance type (instance type identifier, which can be only 1 or 2 currently)
        :type InstanceType: int
        :param _IkConfig: IK analyzer configuration
        :type IkConfig: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        :param _MasterNodeInfo: Dedicated primary node configuration
        :type MasterNodeInfo: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        :param _CosBackup: Auto-backup to COS configuration
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param _AllowCosBackup: Whether to allow auto-backup to COS
        :type AllowCosBackup: bool
        :param _TagList: List of tags owned by the instance
        :type TagList: list of TagInfo
        :param _LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :type LicenseType: str
        :param _EnableHotWarmMode: Whether it is a hot/warm cluster <li>true: yes </li><li>false: no</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableHotWarmMode: bool
        :param _WarmNodeType: Warm node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmNodeType: str
        :param _WarmNodeNum: Number of warm nodes
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmNodeNum: int
        :param _WarmCpuNum: Number of warm node CPU cores
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmCpuNum: int
        :param _WarmMemSize: Warm node memory size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmMemSize: int
        :param _WarmDiskType: Warm node disk type
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmDiskType: str
        :param _WarmDiskSize: Warm node disk size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type WarmDiskSize: int
        :param _NodeInfoList: Cluster node information list
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeInfoList: list of NodeInfo
        :param _EsPublicUrl: ES public IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type EsPublicUrl: str
        :param _MultiZoneInfo: Multi-AZ network information
Note: This field may return null, indicating that no valid values can be obtained.
        :type MultiZoneInfo: list of ZoneDetail
        :param _DeployMode: Deployment mode <li>0: single-AZ </li><li>1: multi-AZ</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeployMode: int
        :param _PublicAccess: ES public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicAccess: str
        :param _EsPublicAcl: ES public access control configuration
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _KibanaPrivateUrl: Kibana private IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaPrivateUrl: str
        :param _KibanaPublicAccess: Kibana public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaPublicAccess: str
        :param _KibanaPrivateAccess: Kibana private access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaPrivateAccess: str
        :param _SecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityType: int
        :param _SceneType: Scenario template type. 0: not enabled; 1: general scenario; 2: log scenario; 3: search scenario
Note: this field may return null, indicating that no valid values can be obtained.
        :type SceneType: int
        :param _KibanaConfig: Kibana configuration item.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type KibanaConfig: str
        :param _KibanaNodeInfo: Kibana node information
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type KibanaNodeInfo: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`
        :param _WebNodeTypeInfo: Visual node configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param _Jdk: JDK type. Valid values: `oracle`, `kona`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Jdk: str
        :param _Protocol: Cluster network communication protocol
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _SecurityGroups: Security group ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroups: list of str
        :param _ColdNodeType: Cold node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdNodeType: str
        :param _ColdNodeNum: Number of cold nodes
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdNodeNum: int
        :param _ColdCpuNum: Number of cold node CPU cores
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdCpuNum: int
        :param _ColdMemSize: Cold node memory size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdMemSize: int
        :param _ColdDiskType: Cold node disk type
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdDiskType: str
        :param _ColdDiskSize: Cold node disk size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type ColdDiskSize: int
        :param _FrozenNodeType: Frozen node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenNodeType: str
        :param _FrozenNodeNum: Number of frozen nodes
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenNodeNum: int
        :param _FrozenCpuNum: Number of frozen node CPU cores
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenCpuNum: int
        :param _FrozenMemSize: Frozen node memory size (GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenMemSize: int
        :param _FrozenDiskType: Frozen node disk type
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenDiskType: str
        :param _FrozenDiskSize: Frozen node disk size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :type FrozenDiskSize: int
        :param _HealthStatus: Cluster health status. `-1`: Unknown; `0`: Green; `1`: Yellow; `2`: Red
Note: This field may return `null`, indicating that no valid value was found.
        :type HealthStatus: int
        :param _EsPrivateUrl: Private URL of the HTTPS cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type EsPrivateUrl: str
        :param _EsPrivateDomain: Private domain of the HTTPS cluster
Note: This field may return `null`, indicating that no valid value was found.
        :type EsPrivateDomain: str
        :param _EsConfigSets: Configuration set info of the cluster.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EsConfigSets: list of EsConfigSetInfo
        :param _OperationDuration: The maintenance time slot of the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param _OptionalWebServiceInfos: Web node list
Note: This field may return null, indicating that no valid values can be obtained.
        :type OptionalWebServiceInfos: list of OptionalWebServiceInfo
        :param _AutoIndexEnabled: Autonomous index option
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoIndexEnabled: bool
        :param _EnableHybridStorage: Whether the storage-computing separation feature is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableHybridStorage: bool
        :param _ProcessPercent: The process progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcessPercent: float
        :param _KibanaAlteringPublicAccess: The alerting policy of Kibana over the public network. <li>`OPEN`: Enable the policy;</li><li>`CLOSE`: Disable the policy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaAlteringPublicAccess: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._Zone = None
        self._AppId = None
        self._Uin = None
        self._VpcUid = None
        self._SubnetUid = None
        self._Status = None
        self._RenewFlag = None
        self._ChargeType = None
        self._ChargePeriod = None
        self._NodeType = None
        self._NodeNum = None
        self._CpuNum = None
        self._MemSize = None
        self._DiskType = None
        self._DiskSize = None
        self._EsDomain = None
        self._EsVip = None
        self._EsPort = None
        self._KibanaUrl = None
        self._EsVersion = None
        self._EsConfig = None
        self._EsAcl = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Deadline = None
        self._InstanceType = None
        self._IkConfig = None
        self._MasterNodeInfo = None
        self._CosBackup = None
        self._AllowCosBackup = None
        self._TagList = None
        self._LicenseType = None
        self._EnableHotWarmMode = None
        self._WarmNodeType = None
        self._WarmNodeNum = None
        self._WarmCpuNum = None
        self._WarmMemSize = None
        self._WarmDiskType = None
        self._WarmDiskSize = None
        self._NodeInfoList = None
        self._EsPublicUrl = None
        self._MultiZoneInfo = None
        self._DeployMode = None
        self._PublicAccess = None
        self._EsPublicAcl = None
        self._KibanaPrivateUrl = None
        self._KibanaPublicAccess = None
        self._KibanaPrivateAccess = None
        self._SecurityType = None
        self._SceneType = None
        self._KibanaConfig = None
        self._KibanaNodeInfo = None
        self._WebNodeTypeInfo = None
        self._Jdk = None
        self._Protocol = None
        self._SecurityGroups = None
        self._ColdNodeType = None
        self._ColdNodeNum = None
        self._ColdCpuNum = None
        self._ColdMemSize = None
        self._ColdDiskType = None
        self._ColdDiskSize = None
        self._FrozenNodeType = None
        self._FrozenNodeNum = None
        self._FrozenCpuNum = None
        self._FrozenMemSize = None
        self._FrozenDiskType = None
        self._FrozenDiskSize = None
        self._HealthStatus = None
        self._EsPrivateUrl = None
        self._EsPrivateDomain = None
        self._EsConfigSets = None
        self._OperationDuration = None
        self._OptionalWebServiceInfos = None
        self._AutoIndexEnabled = None
        self._EnableHybridStorage = None
        self._ProcessPercent = None
        self._KibanaAlteringPublicAccess = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        r"""Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""Availability Zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AppId(self):
        r"""User ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""User UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcUid(self):
        r"""UID of the VPC where the instance resides
        :rtype: str
        """
        return self._VpcUid

    @VpcUid.setter
    def VpcUid(self, VpcUid):
        self._VpcUid = VpcUid

    @property
    def SubnetUid(self):
        r"""UID of the subnet where the instance resides
        :rtype: str
        """
        return self._SubnetUid

    @SubnetUid.setter
    def SubnetUid(self, SubnetUid):
        self._SubnetUid = SubnetUid

    @property
    def Status(self):
        r"""Instance status. `0`: Processing; `1`: Normal; `-1`: `Stopped`; `-2`: Being terminated; `-3`: Terminated; `2`: Initializing during the cluster creation.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RenewFlag(self):
        r"""This parameter is not used on the global website
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ChargeType(self):
        r"""Instance billing method. Valid values: POSTPAID_BY_HOUR (pay-as-you-go hourly); CDHPAID (billed based on CDH, i.e., only CDH is billed but not the instances on CDH)
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePeriod(self):
        r"""This parameter is not used on the global website
        :rtype: int
        """
        return self._ChargePeriod

    @ChargePeriod.setter
    def ChargePeriod(self, ChargePeriod):
        self._ChargePeriod = ChargePeriod

    @property
    def NodeType(self):
        r"""Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeNum(self):
        r"""Number of nodes
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def CpuNum(self):
        r"""Number of CPU cores of the node
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MemSize(self):
        r"""Node memory size in GB
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def DiskType(self):
        r"""Node disk type
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""Node disk size in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def EsDomain(self):
        r"""ES domain name
        :rtype: str
        """
        return self._EsDomain

    @EsDomain.setter
    def EsDomain(self, EsDomain):
        self._EsDomain = EsDomain

    @property
    def EsVip(self):
        r"""ES VIP
        :rtype: str
        """
        return self._EsVip

    @EsVip.setter
    def EsVip(self, EsVip):
        self._EsVip = EsVip

    @property
    def EsPort(self):
        r"""ES port
        :rtype: int
        """
        return self._EsPort

    @EsPort.setter
    def EsPort(self, EsPort):
        self._EsPort = EsPort

    @property
    def KibanaUrl(self):
        r"""Kibana access URL
        :rtype: str
        """
        return self._KibanaUrl

    @KibanaUrl.setter
    def KibanaUrl(self, KibanaUrl):
        self._KibanaUrl = KibanaUrl

    @property
    def EsVersion(self):
        r"""ES version number
        :rtype: str
        """
        return self._EsVersion

    @EsVersion.setter
    def EsVersion(self, EsVersion):
        self._EsVersion = EsVersion

    @property
    def EsConfig(self):
        r"""ES configuration item
        :rtype: str
        """
        return self._EsConfig

    @EsConfig.setter
    def EsConfig(self, EsConfig):
        self._EsConfig = EsConfig

    @property
    def EsAcl(self):
        r"""Kibana access control configuration
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._EsAcl

    @EsAcl.setter
    def EsAcl(self, EsAcl):
        self._EsAcl = EsAcl

    @property
    def CreateTime(self):
        r"""Instance creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Last modified time of the instance
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Deadline(self):
        r"""This parameter is not used on the global website
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def InstanceType(self):
        r"""Instance type (instance type identifier, which can be only 1 or 2 currently)
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def IkConfig(self):
        r"""IK analyzer configuration
        :rtype: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        """
        return self._IkConfig

    @IkConfig.setter
    def IkConfig(self, IkConfig):
        self._IkConfig = IkConfig

    @property
    def MasterNodeInfo(self):
        r"""Dedicated primary node configuration
        :rtype: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        """
        return self._MasterNodeInfo

    @MasterNodeInfo.setter
    def MasterNodeInfo(self, MasterNodeInfo):
        self._MasterNodeInfo = MasterNodeInfo

    @property
    def CosBackup(self):
        r"""Auto-backup to COS configuration
        :rtype: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup

    @property
    def AllowCosBackup(self):
        r"""Whether to allow auto-backup to COS
        :rtype: bool
        """
        return self._AllowCosBackup

    @AllowCosBackup.setter
    def AllowCosBackup(self, AllowCosBackup):
        self._AllowCosBackup = AllowCosBackup

    @property
    def TagList(self):
        r"""List of tags owned by the instance
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def LicenseType(self):
        r"""License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def EnableHotWarmMode(self):
        r"""Whether it is a hot/warm cluster <li>true: yes </li><li>false: no</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableHotWarmMode

    @EnableHotWarmMode.setter
    def EnableHotWarmMode(self, EnableHotWarmMode):
        self._EnableHotWarmMode = EnableHotWarmMode

    @property
    def WarmNodeType(self):
        r"""Warm node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._WarmNodeType

    @WarmNodeType.setter
    def WarmNodeType(self, WarmNodeType):
        self._WarmNodeType = WarmNodeType

    @property
    def WarmNodeNum(self):
        r"""Number of warm nodes
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._WarmNodeNum

    @WarmNodeNum.setter
    def WarmNodeNum(self, WarmNodeNum):
        self._WarmNodeNum = WarmNodeNum

    @property
    def WarmCpuNum(self):
        r"""Number of warm node CPU cores
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._WarmCpuNum

    @WarmCpuNum.setter
    def WarmCpuNum(self, WarmCpuNum):
        self._WarmCpuNum = WarmCpuNum

    @property
    def WarmMemSize(self):
        r"""Warm node memory size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._WarmMemSize

    @WarmMemSize.setter
    def WarmMemSize(self, WarmMemSize):
        self._WarmMemSize = WarmMemSize

    @property
    def WarmDiskType(self):
        r"""Warm node disk type
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._WarmDiskType

    @WarmDiskType.setter
    def WarmDiskType(self, WarmDiskType):
        self._WarmDiskType = WarmDiskType

    @property
    def WarmDiskSize(self):
        r"""Warm node disk size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._WarmDiskSize

    @WarmDiskSize.setter
    def WarmDiskSize(self, WarmDiskSize):
        self._WarmDiskSize = WarmDiskSize

    @property
    def NodeInfoList(self):
        r"""Cluster node information list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of NodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList

    @property
    def EsPublicUrl(self):
        r"""ES public IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EsPublicUrl

    @EsPublicUrl.setter
    def EsPublicUrl(self, EsPublicUrl):
        self._EsPublicUrl = EsPublicUrl

    @property
    def MultiZoneInfo(self):
        r"""Multi-AZ network information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ZoneDetail
        """
        return self._MultiZoneInfo

    @MultiZoneInfo.setter
    def MultiZoneInfo(self, MultiZoneInfo):
        self._MultiZoneInfo = MultiZoneInfo

    @property
    def DeployMode(self):
        r"""Deployment mode <li>0: single-AZ </li><li>1: multi-AZ</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def PublicAccess(self):
        r"""ES public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def EsPublicAcl(self):
        r"""ES public access control configuration
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._EsPublicAcl

    @EsPublicAcl.setter
    def EsPublicAcl(self, EsPublicAcl):
        self._EsPublicAcl = EsPublicAcl

    @property
    def KibanaPrivateUrl(self):
        r"""Kibana private IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KibanaPrivateUrl

    @KibanaPrivateUrl.setter
    def KibanaPrivateUrl(self, KibanaPrivateUrl):
        self._KibanaPrivateUrl = KibanaPrivateUrl

    @property
    def KibanaPublicAccess(self):
        r"""Kibana public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KibanaPublicAccess

    @KibanaPublicAccess.setter
    def KibanaPublicAccess(self, KibanaPublicAccess):
        self._KibanaPublicAccess = KibanaPublicAccess

    @property
    def KibanaPrivateAccess(self):
        r"""Kibana private access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KibanaPrivateAccess

    @KibanaPrivateAccess.setter
    def KibanaPrivateAccess(self, KibanaPrivateAccess):
        self._KibanaPrivateAccess = KibanaPrivateAccess

    @property
    def SecurityType(self):
        r"""Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def SceneType(self):
        r"""Scenario template type. 0: not enabled; 1: general scenario; 2: log scenario; 3: search scenario
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def KibanaConfig(self):
        r"""Kibana configuration item.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KibanaConfig

    @KibanaConfig.setter
    def KibanaConfig(self, KibanaConfig):
        self._KibanaConfig = KibanaConfig

    @property
    def KibanaNodeInfo(self):
        r"""Kibana node information
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`
        """
        return self._KibanaNodeInfo

    @KibanaNodeInfo.setter
    def KibanaNodeInfo(self, KibanaNodeInfo):
        self._KibanaNodeInfo = KibanaNodeInfo

    @property
    def WebNodeTypeInfo(self):
        r"""Visual node configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        """
        return self._WebNodeTypeInfo

    @WebNodeTypeInfo.setter
    def WebNodeTypeInfo(self, WebNodeTypeInfo):
        self._WebNodeTypeInfo = WebNodeTypeInfo

    @property
    def Jdk(self):
        r"""JDK type. Valid values: `oracle`, `kona`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Jdk

    @Jdk.setter
    def Jdk(self, Jdk):
        self._Jdk = Jdk

    @property
    def Protocol(self):
        r"""Cluster network communication protocol
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SecurityGroups(self):
        r"""Security group ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def ColdNodeType(self):
        r"""Cold node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ColdNodeType

    @ColdNodeType.setter
    def ColdNodeType(self, ColdNodeType):
        self._ColdNodeType = ColdNodeType

    @property
    def ColdNodeNum(self):
        r"""Number of cold nodes
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._ColdNodeNum

    @ColdNodeNum.setter
    def ColdNodeNum(self, ColdNodeNum):
        self._ColdNodeNum = ColdNodeNum

    @property
    def ColdCpuNum(self):
        r"""Number of cold node CPU cores
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._ColdCpuNum

    @ColdCpuNum.setter
    def ColdCpuNum(self, ColdCpuNum):
        self._ColdCpuNum = ColdCpuNum

    @property
    def ColdMemSize(self):
        r"""Cold node memory size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._ColdMemSize

    @ColdMemSize.setter
    def ColdMemSize(self, ColdMemSize):
        self._ColdMemSize = ColdMemSize

    @property
    def ColdDiskType(self):
        r"""Cold node disk type
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ColdDiskType

    @ColdDiskType.setter
    def ColdDiskType(self, ColdDiskType):
        self._ColdDiskType = ColdDiskType

    @property
    def ColdDiskSize(self):
        r"""Cold node disk size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._ColdDiskSize

    @ColdDiskSize.setter
    def ColdDiskSize(self, ColdDiskSize):
        self._ColdDiskSize = ColdDiskSize

    @property
    def FrozenNodeType(self):
        r"""Frozen node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._FrozenNodeType

    @FrozenNodeType.setter
    def FrozenNodeType(self, FrozenNodeType):
        self._FrozenNodeType = FrozenNodeType

    @property
    def FrozenNodeNum(self):
        r"""Number of frozen nodes
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._FrozenNodeNum

    @FrozenNodeNum.setter
    def FrozenNodeNum(self, FrozenNodeNum):
        self._FrozenNodeNum = FrozenNodeNum

    @property
    def FrozenCpuNum(self):
        r"""Number of frozen node CPU cores
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._FrozenCpuNum

    @FrozenCpuNum.setter
    def FrozenCpuNum(self, FrozenCpuNum):
        self._FrozenCpuNum = FrozenCpuNum

    @property
    def FrozenMemSize(self):
        r"""Frozen node memory size (GB)
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._FrozenMemSize

    @FrozenMemSize.setter
    def FrozenMemSize(self, FrozenMemSize):
        self._FrozenMemSize = FrozenMemSize

    @property
    def FrozenDiskType(self):
        r"""Frozen node disk type
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._FrozenDiskType

    @FrozenDiskType.setter
    def FrozenDiskType(self, FrozenDiskType):
        self._FrozenDiskType = FrozenDiskType

    @property
    def FrozenDiskSize(self):
        r"""Frozen node disk size (in GB)
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._FrozenDiskSize

    @FrozenDiskSize.setter
    def FrozenDiskSize(self, FrozenDiskSize):
        self._FrozenDiskSize = FrozenDiskSize

    @property
    def HealthStatus(self):
        r"""Cluster health status. `-1`: Unknown; `0`: Green; `1`: Yellow; `2`: Red
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def EsPrivateUrl(self):
        r"""Private URL of the HTTPS cluster
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._EsPrivateUrl

    @EsPrivateUrl.setter
    def EsPrivateUrl(self, EsPrivateUrl):
        self._EsPrivateUrl = EsPrivateUrl

    @property
    def EsPrivateDomain(self):
        r"""Private domain of the HTTPS cluster
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._EsPrivateDomain

    @EsPrivateDomain.setter
    def EsPrivateDomain(self, EsPrivateDomain):
        self._EsPrivateDomain = EsPrivateDomain

    @property
    def EsConfigSets(self):
        r"""Configuration set info of the cluster.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of EsConfigSetInfo
        """
        return self._EsConfigSets

    @EsConfigSets.setter
    def EsConfigSets(self, EsConfigSets):
        self._EsConfigSets = EsConfigSets

    @property
    def OperationDuration(self):
        r"""The maintenance time slot of the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def OptionalWebServiceInfos(self):
        r"""Web node list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of OptionalWebServiceInfo
        """
        return self._OptionalWebServiceInfos

    @OptionalWebServiceInfos.setter
    def OptionalWebServiceInfos(self, OptionalWebServiceInfos):
        self._OptionalWebServiceInfos = OptionalWebServiceInfos

    @property
    def AutoIndexEnabled(self):
        r"""Autonomous index option
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._AutoIndexEnabled

    @AutoIndexEnabled.setter
    def AutoIndexEnabled(self, AutoIndexEnabled):
        self._AutoIndexEnabled = AutoIndexEnabled

    @property
    def EnableHybridStorage(self):
        r"""Whether the storage-computing separation feature is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableHybridStorage

    @EnableHybridStorage.setter
    def EnableHybridStorage(self, EnableHybridStorage):
        self._EnableHybridStorage = EnableHybridStorage

    @property
    def ProcessPercent(self):
        r"""The process progress
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._ProcessPercent

    @ProcessPercent.setter
    def ProcessPercent(self, ProcessPercent):
        self._ProcessPercent = ProcessPercent

    @property
    def KibanaAlteringPublicAccess(self):
        r"""The alerting policy of Kibana over the public network. <li>`OPEN`: Enable the policy;</li><li>`CLOSE`: Disable the policy.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KibanaAlteringPublicAccess

    @KibanaAlteringPublicAccess.setter
    def KibanaAlteringPublicAccess(self, KibanaAlteringPublicAccess):
        self._KibanaAlteringPublicAccess = KibanaAlteringPublicAccess


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._VpcUid = params.get("VpcUid")
        self._SubnetUid = params.get("SubnetUid")
        self._Status = params.get("Status")
        self._RenewFlag = params.get("RenewFlag")
        self._ChargeType = params.get("ChargeType")
        self._ChargePeriod = params.get("ChargePeriod")
        self._NodeType = params.get("NodeType")
        self._NodeNum = params.get("NodeNum")
        self._CpuNum = params.get("CpuNum")
        self._MemSize = params.get("MemSize")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._EsDomain = params.get("EsDomain")
        self._EsVip = params.get("EsVip")
        self._EsPort = params.get("EsPort")
        self._KibanaUrl = params.get("KibanaUrl")
        self._EsVersion = params.get("EsVersion")
        self._EsConfig = params.get("EsConfig")
        if params.get("EsAcl") is not None:
            self._EsAcl = EsAcl()
            self._EsAcl._deserialize(params.get("EsAcl"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Deadline = params.get("Deadline")
        self._InstanceType = params.get("InstanceType")
        if params.get("IkConfig") is not None:
            self._IkConfig = EsDictionaryInfo()
            self._IkConfig._deserialize(params.get("IkConfig"))
        if params.get("MasterNodeInfo") is not None:
            self._MasterNodeInfo = MasterNodeInfo()
            self._MasterNodeInfo._deserialize(params.get("MasterNodeInfo"))
        if params.get("CosBackup") is not None:
            self._CosBackup = CosBackup()
            self._CosBackup._deserialize(params.get("CosBackup"))
        self._AllowCosBackup = params.get("AllowCosBackup")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._LicenseType = params.get("LicenseType")
        self._EnableHotWarmMode = params.get("EnableHotWarmMode")
        self._WarmNodeType = params.get("WarmNodeType")
        self._WarmNodeNum = params.get("WarmNodeNum")
        self._WarmCpuNum = params.get("WarmCpuNum")
        self._WarmMemSize = params.get("WarmMemSize")
        self._WarmDiskType = params.get("WarmDiskType")
        self._WarmDiskSize = params.get("WarmDiskSize")
        if params.get("NodeInfoList") is not None:
            self._NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfoList.append(obj)
        self._EsPublicUrl = params.get("EsPublicUrl")
        if params.get("MultiZoneInfo") is not None:
            self._MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self._MultiZoneInfo.append(obj)
        self._DeployMode = params.get("DeployMode")
        self._PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self._EsPublicAcl = EsAcl()
            self._EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self._KibanaPrivateUrl = params.get("KibanaPrivateUrl")
        self._KibanaPublicAccess = params.get("KibanaPublicAccess")
        self._KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self._SecurityType = params.get("SecurityType")
        self._SceneType = params.get("SceneType")
        self._KibanaConfig = params.get("KibanaConfig")
        if params.get("KibanaNodeInfo") is not None:
            self._KibanaNodeInfo = KibanaNodeInfo()
            self._KibanaNodeInfo._deserialize(params.get("KibanaNodeInfo"))
        if params.get("WebNodeTypeInfo") is not None:
            self._WebNodeTypeInfo = WebNodeTypeInfo()
            self._WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self._Jdk = params.get("Jdk")
        self._Protocol = params.get("Protocol")
        self._SecurityGroups = params.get("SecurityGroups")
        self._ColdNodeType = params.get("ColdNodeType")
        self._ColdNodeNum = params.get("ColdNodeNum")
        self._ColdCpuNum = params.get("ColdCpuNum")
        self._ColdMemSize = params.get("ColdMemSize")
        self._ColdDiskType = params.get("ColdDiskType")
        self._ColdDiskSize = params.get("ColdDiskSize")
        self._FrozenNodeType = params.get("FrozenNodeType")
        self._FrozenNodeNum = params.get("FrozenNodeNum")
        self._FrozenCpuNum = params.get("FrozenCpuNum")
        self._FrozenMemSize = params.get("FrozenMemSize")
        self._FrozenDiskType = params.get("FrozenDiskType")
        self._FrozenDiskSize = params.get("FrozenDiskSize")
        self._HealthStatus = params.get("HealthStatus")
        self._EsPrivateUrl = params.get("EsPrivateUrl")
        self._EsPrivateDomain = params.get("EsPrivateDomain")
        if params.get("EsConfigSets") is not None:
            self._EsConfigSets = []
            for item in params.get("EsConfigSets"):
                obj = EsConfigSetInfo()
                obj._deserialize(item)
                self._EsConfigSets.append(obj)
        if params.get("OperationDuration") is not None:
            self._OperationDuration = OperationDuration()
            self._OperationDuration._deserialize(params.get("OperationDuration"))
        if params.get("OptionalWebServiceInfos") is not None:
            self._OptionalWebServiceInfos = []
            for item in params.get("OptionalWebServiceInfos"):
                obj = OptionalWebServiceInfo()
                obj._deserialize(item)
                self._OptionalWebServiceInfos.append(obj)
        self._AutoIndexEnabled = params.get("AutoIndexEnabled")
        self._EnableHybridStorage = params.get("EnableHybridStorage")
        self._ProcessPercent = params.get("ProcessPercent")
        self._KibanaAlteringPublicAccess = params.get("KibanaAlteringPublicAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceLog(AbstractModel):
    r"""ES cluster log details

    """

    def __init__(self):
        r"""
        :param _Time: Log time
        :type Time: str
        :param _Level: Log level
        :type Level: str
        :param _Ip: Cluster node IP
        :type Ip: str
        :param _Message: Log content
        :type Message: str
        """
        self._Time = None
        self._Level = None
        self._Ip = None
        self._Message = None

    @property
    def Time(self):
        r"""Log time
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Level(self):
        r"""Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Ip(self):
        r"""Cluster node IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Message(self):
        r"""Log content
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Level = params.get("Level")
        self._Ip = params.get("Ip")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    r"""`OperationDetail` uses an array of this structure to describe the old and new configuration information

    """

    def __init__(self):
        r"""
        :param _Key: Key
        :type Key: str
        :param _Value: Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KibanaNodeInfo(AbstractModel):
    r"""Kibana node information

    """

    def __init__(self):
        r"""
        :param _KibanaNodeType: Kibana node specification
        :type KibanaNodeType: str
        :param _KibanaNodeNum: Number of Kibana nodes
        :type KibanaNodeNum: int
        :param _KibanaNodeCpuNum: Number of Kibana node's CPUs
        :type KibanaNodeCpuNum: int
        :param _KibanaNodeMemSize: Kibana node's memory in GB
        :type KibanaNodeMemSize: int
        :param _KibanaNodeDiskType: Kibana node's disk type
        :type KibanaNodeDiskType: str
        :param _KibanaNodeDiskSize: Kibana node's disk size
        :type KibanaNodeDiskSize: int
        """
        self._KibanaNodeType = None
        self._KibanaNodeNum = None
        self._KibanaNodeCpuNum = None
        self._KibanaNodeMemSize = None
        self._KibanaNodeDiskType = None
        self._KibanaNodeDiskSize = None

    @property
    def KibanaNodeType(self):
        r"""Kibana node specification
        :rtype: str
        """
        return self._KibanaNodeType

    @KibanaNodeType.setter
    def KibanaNodeType(self, KibanaNodeType):
        self._KibanaNodeType = KibanaNodeType

    @property
    def KibanaNodeNum(self):
        r"""Number of Kibana nodes
        :rtype: int
        """
        return self._KibanaNodeNum

    @KibanaNodeNum.setter
    def KibanaNodeNum(self, KibanaNodeNum):
        self._KibanaNodeNum = KibanaNodeNum

    @property
    def KibanaNodeCpuNum(self):
        r"""Number of Kibana node's CPUs
        :rtype: int
        """
        return self._KibanaNodeCpuNum

    @KibanaNodeCpuNum.setter
    def KibanaNodeCpuNum(self, KibanaNodeCpuNum):
        self._KibanaNodeCpuNum = KibanaNodeCpuNum

    @property
    def KibanaNodeMemSize(self):
        r"""Kibana node's memory in GB
        :rtype: int
        """
        return self._KibanaNodeMemSize

    @KibanaNodeMemSize.setter
    def KibanaNodeMemSize(self, KibanaNodeMemSize):
        self._KibanaNodeMemSize = KibanaNodeMemSize

    @property
    def KibanaNodeDiskType(self):
        r"""Kibana node's disk type
        :rtype: str
        """
        return self._KibanaNodeDiskType

    @KibanaNodeDiskType.setter
    def KibanaNodeDiskType(self, KibanaNodeDiskType):
        self._KibanaNodeDiskType = KibanaNodeDiskType

    @property
    def KibanaNodeDiskSize(self):
        r"""Kibana node's disk size
        :rtype: int
        """
        return self._KibanaNodeDiskSize

    @KibanaNodeDiskSize.setter
    def KibanaNodeDiskSize(self, KibanaNodeDiskSize):
        self._KibanaNodeDiskSize = KibanaNodeDiskSize


    def _deserialize(self, params):
        self._KibanaNodeType = params.get("KibanaNodeType")
        self._KibanaNodeNum = params.get("KibanaNodeNum")
        self._KibanaNodeCpuNum = params.get("KibanaNodeCpuNum")
        self._KibanaNodeMemSize = params.get("KibanaNodeMemSize")
        self._KibanaNodeDiskType = params.get("KibanaNodeDiskType")
        self._KibanaNodeDiskSize = params.get("KibanaNodeDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KibanaView(AbstractModel):
    r"""Kibana view data

    """

    def __init__(self):
        r"""
        :param _Ip: Kibana node IP
        :type Ip: str
        :param _DiskSize: Node disk size
        :type DiskSize: int
        :param _DiskUsage: Disk usage
        :type DiskUsage: float
        :param _MemSize: Node memory size
        :type MemSize: int
        :param _MemUsage: Memory usage
        :type MemUsage: float
        :param _CpuNum: Number of node CPUs
        :type CpuNum: int
        :param _CpuUsage: CPU usage
        :type CpuUsage: float
        :param _Zone: Availability zone
        :type Zone: str
        """
        self._Ip = None
        self._DiskSize = None
        self._DiskUsage = None
        self._MemSize = None
        self._MemUsage = None
        self._CpuNum = None
        self._CpuUsage = None
        self._Zone = None

    @property
    def Ip(self):
        r"""Kibana node IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def DiskSize(self):
        r"""Node disk size
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskUsage(self):
        r"""Disk usage
        :rtype: float
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def MemSize(self):
        r"""Node memory size
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MemUsage(self):
        r"""Memory usage
        :rtype: float
        """
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def CpuNum(self):
        r"""Number of node CPUs
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def CpuUsage(self):
        r"""CPU usage
        :rtype: float
        """
        return self._CpuUsage

    @CpuUsage.setter
    def CpuUsage(self, CpuUsage):
        self._CpuUsage = CpuUsage

    @property
    def Zone(self):
        r"""Availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._DiskSize = params.get("DiskSize")
        self._DiskUsage = params.get("DiskUsage")
        self._MemSize = params.get("MemSize")
        self._MemUsage = params.get("MemUsage")
        self._CpuNum = params.get("CpuNum")
        self._CpuUsage = params.get("CpuUsage")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskInfo(AbstractModel):
    r"""Local disk information of node

    """

    def __init__(self):
        r"""
        :param _LocalDiskType: Local disk type <li>LOCAL_SATA: big data </li><li>NVME_SSD: high IO</li>
        :type LocalDiskType: str
        :param _LocalDiskSize: Size of a single local disk
        :type LocalDiskSize: int
        :param _LocalDiskCount: Number of local disks
        :type LocalDiskCount: int
        """
        self._LocalDiskType = None
        self._LocalDiskSize = None
        self._LocalDiskCount = None

    @property
    def LocalDiskType(self):
        r"""Local disk type <li>LOCAL_SATA: big data </li><li>NVME_SSD: high IO</li>
        :rtype: str
        """
        return self._LocalDiskType

    @LocalDiskType.setter
    def LocalDiskType(self, LocalDiskType):
        self._LocalDiskType = LocalDiskType

    @property
    def LocalDiskSize(self):
        r"""Size of a single local disk
        :rtype: int
        """
        return self._LocalDiskSize

    @LocalDiskSize.setter
    def LocalDiskSize(self, LocalDiskSize):
        self._LocalDiskSize = LocalDiskSize

    @property
    def LocalDiskCount(self):
        r"""Number of local disks
        :rtype: int
        """
        return self._LocalDiskCount

    @LocalDiskCount.setter
    def LocalDiskCount(self, LocalDiskCount):
        self._LocalDiskCount = LocalDiskCount


    def _deserialize(self, params):
        self._LocalDiskType = params.get("LocalDiskType")
        self._LocalDiskSize = params.get("LocalDiskSize")
        self._LocalDiskCount = params.get("LocalDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MasterNodeInfo(AbstractModel):
    r"""Information of the dedicated primary node in an instance

    """

    def __init__(self):
        r"""
        :param _EnableDedicatedMaster: Whether to enable the dedicated primary node
        :type EnableDedicatedMaster: bool
        :param _MasterNodeType: Dedicated primary node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :type MasterNodeType: str
        :param _MasterNodeNum: Number of dedicated primary nodes
        :type MasterNodeNum: int
        :param _MasterNodeCpuNum: Number of CPU cores of the dedicated primary node
        :type MasterNodeCpuNum: int
        :param _MasterNodeMemSize: Memory size of the dedicated primary node in GB
        :type MasterNodeMemSize: int
        :param _MasterNodeDiskSize: Disk size of the dedicated primary node in GB
        :type MasterNodeDiskSize: int
        :param _MasterNodeDiskType: Disk type of the dedicated primary node
        :type MasterNodeDiskType: str
        """
        self._EnableDedicatedMaster = None
        self._MasterNodeType = None
        self._MasterNodeNum = None
        self._MasterNodeCpuNum = None
        self._MasterNodeMemSize = None
        self._MasterNodeDiskSize = None
        self._MasterNodeDiskType = None

    @property
    def EnableDedicatedMaster(self):
        r"""Whether to enable the dedicated primary node
        :rtype: bool
        """
        return self._EnableDedicatedMaster

    @EnableDedicatedMaster.setter
    def EnableDedicatedMaster(self, EnableDedicatedMaster):
        self._EnableDedicatedMaster = EnableDedicatedMaster

    @property
    def MasterNodeType(self):
        r"""Dedicated primary node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :rtype: str
        """
        return self._MasterNodeType

    @MasterNodeType.setter
    def MasterNodeType(self, MasterNodeType):
        self._MasterNodeType = MasterNodeType

    @property
    def MasterNodeNum(self):
        r"""Number of dedicated primary nodes
        :rtype: int
        """
        return self._MasterNodeNum

    @MasterNodeNum.setter
    def MasterNodeNum(self, MasterNodeNum):
        self._MasterNodeNum = MasterNodeNum

    @property
    def MasterNodeCpuNum(self):
        r"""Number of CPU cores of the dedicated primary node
        :rtype: int
        """
        return self._MasterNodeCpuNum

    @MasterNodeCpuNum.setter
    def MasterNodeCpuNum(self, MasterNodeCpuNum):
        self._MasterNodeCpuNum = MasterNodeCpuNum

    @property
    def MasterNodeMemSize(self):
        r"""Memory size of the dedicated primary node in GB
        :rtype: int
        """
        return self._MasterNodeMemSize

    @MasterNodeMemSize.setter
    def MasterNodeMemSize(self, MasterNodeMemSize):
        self._MasterNodeMemSize = MasterNodeMemSize

    @property
    def MasterNodeDiskSize(self):
        r"""Disk size of the dedicated primary node in GB
        :rtype: int
        """
        return self._MasterNodeDiskSize

    @MasterNodeDiskSize.setter
    def MasterNodeDiskSize(self, MasterNodeDiskSize):
        self._MasterNodeDiskSize = MasterNodeDiskSize

    @property
    def MasterNodeDiskType(self):
        r"""Disk type of the dedicated primary node
        :rtype: str
        """
        return self._MasterNodeDiskType

    @MasterNodeDiskType.setter
    def MasterNodeDiskType(self, MasterNodeDiskType):
        self._MasterNodeDiskType = MasterNodeDiskType


    def _deserialize(self, params):
        self._EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self._MasterNodeType = params.get("MasterNodeType")
        self._MasterNodeNum = params.get("MasterNodeNum")
        self._MasterNodeCpuNum = params.get("MasterNodeCpuNum")
        self._MasterNodeMemSize = params.get("MasterNodeMemSize")
        self._MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self._MasterNodeDiskType = params.get("MasterNodeDiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    r"""Specification information of a node type in the cluster (such as hot data node, warm data node, or dedicated primary node), including node type, number of nodes, node specification, disk type, and disk size. If `Type` is not specified, it will be a hot data node by default; if the node is a primary node, then the `DiskType` and `DiskSize` parameters will be ignored (as a primary node has no data disks)

    """

    def __init__(self):
        r"""
        :param _NodeNum: Number of nodes
        :type NodeNum: int
        :param _NodeType: Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param _Type: Node type<li>`hotData`: hot data node</li>
<li>`warmData`: warm data node</li>
<li>`dedicatedMaster`: dedicated master node</li>
Default value: `hotData`
        :type Type: str
        :param _DiskType: Node disk type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: Premium cloud disk </li>Default value: CLOUD_SSD
        :type DiskType: str
        :param _DiskSize: Node disk size in GB
        :type DiskSize: int
        :param _LocalDiskInfo: Local disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :type LocalDiskInfo: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`
        :param _DiskCount: Number of node disks
        :type DiskCount: int
        :param _DiskEncrypt: Whether to encrypt node disk. 0: no (default); 1: yes.
        :type DiskEncrypt: int
        :param _CpuNum: CPU number
Note: This field may return null, indicating that no valid values can be obtained.
        :type CpuNum: int
        :param _MemSize: Memory size in GB
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param _DiskEnhance: /
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskEnhance: int
        """
        self._NodeNum = None
        self._NodeType = None
        self._Type = None
        self._DiskType = None
        self._DiskSize = None
        self._LocalDiskInfo = None
        self._DiskCount = None
        self._DiskEncrypt = None
        self._CpuNum = None
        self._MemSize = None
        self._DiskEnhance = None

    @property
    def NodeNum(self):
        r"""Number of nodes
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def NodeType(self):
        r"""Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def Type(self):
        r"""Node type<li>`hotData`: hot data node</li>
<li>`warmData`: warm data node</li>
<li>`dedicatedMaster`: dedicated master node</li>
Default value: `hotData`
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DiskType(self):
        r"""Node disk type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: Premium cloud disk </li>Default value: CLOUD_SSD
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""Node disk size in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def LocalDiskInfo(self):
        r"""Local disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`
        """
        return self._LocalDiskInfo

    @LocalDiskInfo.setter
    def LocalDiskInfo(self, LocalDiskInfo):
        self._LocalDiskInfo = LocalDiskInfo

    @property
    def DiskCount(self):
        r"""Number of node disks
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskEncrypt(self):
        r"""Whether to encrypt node disk. 0: no (default); 1: yes.
        :rtype: int
        """
        return self._DiskEncrypt

    @DiskEncrypt.setter
    def DiskEncrypt(self, DiskEncrypt):
        self._DiskEncrypt = DiskEncrypt

    @property
    def CpuNum(self):
        r"""CPU number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MemSize(self):
        r"""Memory size in GB
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def DiskEnhance(self):
        r"""/
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskEnhance

    @DiskEnhance.setter
    def DiskEnhance(self, DiskEnhance):
        self._DiskEnhance = DiskEnhance


    def _deserialize(self, params):
        self._NodeNum = params.get("NodeNum")
        self._NodeType = params.get("NodeType")
        self._Type = params.get("Type")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        if params.get("LocalDiskInfo") is not None:
            self._LocalDiskInfo = LocalDiskInfo()
            self._LocalDiskInfo._deserialize(params.get("LocalDiskInfo"))
        self._DiskCount = params.get("DiskCount")
        self._DiskEncrypt = params.get("DiskEncrypt")
        self._CpuNum = params.get("CpuNum")
        self._MemSize = params.get("MemSize")
        self._DiskEnhance = params.get("DiskEnhance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeView(AbstractModel):
    r"""Node view data

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID
        :type NodeId: str
        :param _NodeIp: Node IP
        :type NodeIp: str
        :param _Visible: Whether the node is visible
        :type Visible: float
        :param _Break: Whether the node encounters circuit breaking
        :type Break: float
        :param _DiskSize: Node disk size
        :type DiskSize: int
        :param _DiskUsage: Disk usage
        :type DiskUsage: float
        :param _MemSize: Node memory size (in GB)
        :type MemSize: int
        :param _MemUsage: Memory usage
        :type MemUsage: float
        :param _CpuNum: Number of node CPUs
        :type CpuNum: int
        :param _CpuUsage: CPU usage
        :type CpuUsage: float
        :param _Zone: Availability zone
        :type Zone: str
        :param _NodeRole: Node role
        :type NodeRole: str
        :param _NodeHttpIp: Node HTTP IP
        :type NodeHttpIp: str
        :param _JvmMemUsage: JVM memory usage
        :type JvmMemUsage: float
        :param _ShardNum: Number of node shards
        :type ShardNum: int
        :param _DiskIds: ID list of node disks
        :type DiskIds: list of str
        :param _Hidden: Whether a hidden availability zone
        :type Hidden: bool
        """
        self._NodeId = None
        self._NodeIp = None
        self._Visible = None
        self._Break = None
        self._DiskSize = None
        self._DiskUsage = None
        self._MemSize = None
        self._MemUsage = None
        self._CpuNum = None
        self._CpuUsage = None
        self._Zone = None
        self._NodeRole = None
        self._NodeHttpIp = None
        self._JvmMemUsage = None
        self._ShardNum = None
        self._DiskIds = None
        self._Hidden = None

    @property
    def NodeId(self):
        r"""Node ID
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeIp(self):
        r"""Node IP
        :rtype: str
        """
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp

    @property
    def Visible(self):
        r"""Whether the node is visible
        :rtype: float
        """
        return self._Visible

    @Visible.setter
    def Visible(self, Visible):
        self._Visible = Visible

    @property
    def Break(self):
        r"""Whether the node encounters circuit breaking
        :rtype: float
        """
        return self._Break

    @Break.setter
    def Break(self, Break):
        self._Break = Break

    @property
    def DiskSize(self):
        r"""Node disk size
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskUsage(self):
        r"""Disk usage
        :rtype: float
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def MemSize(self):
        r"""Node memory size (in GB)
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MemUsage(self):
        r"""Memory usage
        :rtype: float
        """
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def CpuNum(self):
        r"""Number of node CPUs
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def CpuUsage(self):
        r"""CPU usage
        :rtype: float
        """
        return self._CpuUsage

    @CpuUsage.setter
    def CpuUsage(self, CpuUsage):
        self._CpuUsage = CpuUsage

    @property
    def Zone(self):
        r"""Availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeRole(self):
        r"""Node role
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def NodeHttpIp(self):
        r"""Node HTTP IP
        :rtype: str
        """
        return self._NodeHttpIp

    @NodeHttpIp.setter
    def NodeHttpIp(self, NodeHttpIp):
        self._NodeHttpIp = NodeHttpIp

    @property
    def JvmMemUsage(self):
        r"""JVM memory usage
        :rtype: float
        """
        return self._JvmMemUsage

    @JvmMemUsage.setter
    def JvmMemUsage(self, JvmMemUsage):
        self._JvmMemUsage = JvmMemUsage

    @property
    def ShardNum(self):
        r"""Number of node shards
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def DiskIds(self):
        r"""ID list of node disks
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Hidden(self):
        r"""Whether a hidden availability zone
        :rtype: bool
        """
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeIp = params.get("NodeIp")
        self._Visible = params.get("Visible")
        self._Break = params.get("Break")
        self._DiskSize = params.get("DiskSize")
        self._DiskUsage = params.get("DiskUsage")
        self._MemSize = params.get("MemSize")
        self._MemUsage = params.get("MemUsage")
        self._CpuNum = params.get("CpuNum")
        self._CpuUsage = params.get("CpuUsage")
        self._Zone = params.get("Zone")
        self._NodeRole = params.get("NodeRole")
        self._NodeHttpIp = params.get("NodeHttpIp")
        self._JvmMemUsage = params.get("JvmMemUsage")
        self._ShardNum = params.get("ShardNum")
        self._DiskIds = params.get("DiskIds")
        self._Hidden = params.get("Hidden")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operation(AbstractModel):
    r"""ES cluster operation details

    """

    def __init__(self):
        r"""
        :param _Id: Unique operation ID
        :type Id: int
        :param _StartTime: Operation start time
        :type StartTime: str
        :param _Type: Operation type
        :type Type: str
        :param _Detail: Operation details
        :type Detail: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        :param _Result: Operation result
        :type Result: str
        :param _Tasks: Workflow task information
        :type Tasks: list of TaskDetail
        :param _Progress: Operation progress
        :type Progress: float
        """
        self._Id = None
        self._StartTime = None
        self._Type = None
        self._Detail = None
        self._Result = None
        self._Tasks = None
        self._Progress = None

    @property
    def Id(self):
        r"""Unique operation ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        r"""Operation start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""Operation type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Detail(self):
        r"""Operation details
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Result(self):
        r"""Operation result
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Tasks(self):
        r"""Workflow task information
        :rtype: list of TaskDetail
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Progress(self):
        r"""Operation progress
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        if params.get("Detail") is not None:
            self._Detail = OperationDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._Result = params.get("Result")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskDetail()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDetail(AbstractModel):
    r"""Operation details

    """

    def __init__(self):
        r"""
        :param _OldInfo: Original instance configuration information
        :type OldInfo: list of KeyValue
        :param _NewInfo: Updated instance configuration information
        :type NewInfo: list of KeyValue
        """
        self._OldInfo = None
        self._NewInfo = None

    @property
    def OldInfo(self):
        r"""Original instance configuration information
        :rtype: list of KeyValue
        """
        return self._OldInfo

    @OldInfo.setter
    def OldInfo(self, OldInfo):
        self._OldInfo = OldInfo

    @property
    def NewInfo(self):
        r"""Updated instance configuration information
        :rtype: list of KeyValue
        """
        return self._NewInfo

    @NewInfo.setter
    def NewInfo(self, NewInfo):
        self._NewInfo = NewInfo


    def _deserialize(self, params):
        if params.get("OldInfo") is not None:
            self._OldInfo = []
            for item in params.get("OldInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self._OldInfo.append(obj)
        if params.get("NewInfo") is not None:
            self._NewInfo = []
            for item in params.get("NewInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self._NewInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDuration(AbstractModel):
    r"""The maintenance time slot of the cluster

    """

    def __init__(self):
        r"""
        :param _Periods: Maintenance period, which can be one or more days from Monday to Sunday. Valid values: [0, 6].
Note: This field may return null, indicating that no valid values can be obtained.
        :type Periods: list of int non-negative
        :param _TimeStart: The maintenance start time
        :type TimeStart: str
        :param _TimeEnd: The maintenance end time
        :type TimeEnd: str
        :param _TimeZone: The time zone expressed in UTC.
        :type TimeZone: str
        """
        self._Periods = None
        self._TimeStart = None
        self._TimeEnd = None
        self._TimeZone = None

    @property
    def Periods(self):
        r"""Maintenance period, which can be one or more days from Monday to Sunday. Valid values: [0, 6].
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int non-negative
        """
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def TimeStart(self):
        r"""The maintenance start time
        :rtype: str
        """
        return self._TimeStart

    @TimeStart.setter
    def TimeStart(self, TimeStart):
        self._TimeStart = TimeStart

    @property
    def TimeEnd(self):
        r"""The maintenance end time
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def TimeZone(self):
        r"""The time zone expressed in UTC.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Periods = params.get("Periods")
        self._TimeStart = params.get("TimeStart")
        self._TimeEnd = params.get("TimeEnd")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDurationUpdated(AbstractModel):
    r"""The maintenance time slot of the cluster

    """

    def __init__(self):
        r"""
        :param _Periods: Maintenance period, which can be one or more days from Monday to Sunday. Valid values: [0, 6].
        :type Periods: list of int non-negative
        :param _TimeStart: The maintenance start time
        :type TimeStart: str
        :param _TimeEnd: The maintenance end time
        :type TimeEnd: str
        :param _TimeZone: The time zone expressed in UTC.
        :type TimeZone: str
        :param _MoreInstances: The array of ES cluster IDs
        :type MoreInstances: list of str
        """
        self._Periods = None
        self._TimeStart = None
        self._TimeEnd = None
        self._TimeZone = None
        self._MoreInstances = None

    @property
    def Periods(self):
        r"""Maintenance period, which can be one or more days from Monday to Sunday. Valid values: [0, 6].
        :rtype: list of int non-negative
        """
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def TimeStart(self):
        r"""The maintenance start time
        :rtype: str
        """
        return self._TimeStart

    @TimeStart.setter
    def TimeStart(self, TimeStart):
        self._TimeStart = TimeStart

    @property
    def TimeEnd(self):
        r"""The maintenance end time
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def TimeZone(self):
        r"""The time zone expressed in UTC.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def MoreInstances(self):
        r"""The array of ES cluster IDs
        :rtype: list of str
        """
        return self._MoreInstances

    @MoreInstances.setter
    def MoreInstances(self, MoreInstances):
        self._MoreInstances = MoreInstances


    def _deserialize(self, params):
        self._Periods = params.get("Periods")
        self._TimeStart = params.get("TimeStart")
        self._TimeEnd = params.get("TimeEnd")
        self._TimeZone = params.get("TimeZone")
        self._MoreInstances = params.get("MoreInstances")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OptionalWebServiceInfo(AbstractModel):
    r"""The information of optional web components

    """

    def __init__(self):
        r"""
        :param _Type: Type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Status: Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _PublicUrl: Public URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicUrl: str
        :param _PrivateUrl: Private URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateUrl: str
        :param _PublicAccess: Public network access
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicAccess: str
        :param _PrivateAccess: Private network access
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateAccess: str
        :param _Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        """
        self._Type = None
        self._Status = None
        self._PublicUrl = None
        self._PrivateUrl = None
        self._PublicAccess = None
        self._PrivateAccess = None
        self._Version = None

    @property
    def Type(self):
        r"""Type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""Status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PublicUrl(self):
        r"""Public URL
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicUrl

    @PublicUrl.setter
    def PublicUrl(self, PublicUrl):
        self._PublicUrl = PublicUrl

    @property
    def PrivateUrl(self):
        r"""Private URL
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateUrl

    @PrivateUrl.setter
    def PrivateUrl(self, PrivateUrl):
        self._PrivateUrl = PrivateUrl

    @property
    def PublicAccess(self):
        r"""Public network access
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def PrivateAccess(self):
        r"""Private network access
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateAccess

    @PrivateAccess.setter
    def PrivateAccess(self, PrivateAccess):
        self._PrivateAccess = PrivateAccess

    @property
    def Version(self):
        r"""Version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._PublicUrl = params.get("PublicUrl")
        self._PrivateUrl = params.get("PrivateUrl")
        self._PublicAccess = params.get("PublicAccess")
        self._PrivateAccess = params.get("PrivateAccess")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    r"""RestartInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ForceRestart: Whether to force restart <li>true: Yes </li><li>false: No </li>Default value: false
        :type ForceRestart: bool
        :param _RestartMode: Restart mode. `0`: rolling restart; `1`: full restart
        :type RestartMode: int
        """
        self._InstanceId = None
        self._ForceRestart = None
        self._RestartMode = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForceRestart(self):
        r"""Whether to force restart <li>true: Yes </li><li>false: No </li>Default value: false
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def RestartMode(self):
        r"""Restart mode. `0`: rolling restart; `1`: full restart
        :rtype: int
        """
        return self._RestartMode

    @RestartMode.setter
    def RestartMode(self, RestartMode):
        self._RestartMode = RestartMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ForceRestart = params.get("ForceRestart")
        self._RestartMode = params.get("RestartMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceResponse(AbstractModel):
    r"""RestartInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RestartKibanaRequest(AbstractModel):
    r"""RestartKibana request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""ES instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartKibanaResponse(AbstractModel):
    r"""RestartKibana response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RestartNodesRequest(AbstractModel):
    r"""RestartNodes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        :param _NodeNames: Node name list
        :type NodeNames: list of str
        :param _ForceRestart: Whether to force restart
        :type ForceRestart: bool
        :param _RestartMode: The restart mode. Valid values: `in-place` (default), `blue-green`.
        :type RestartMode: str
        :param _IsOffline: The node status, applicable in the blue/green mode. The blue/green restart is risky if the node is offline.
        :type IsOffline: bool
        """
        self._InstanceId = None
        self._NodeNames = None
        self._ForceRestart = None
        self._RestartMode = None
        self._IsOffline = None

    @property
    def InstanceId(self):
        r"""Cluster instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeNames(self):
        r"""Node name list
        :rtype: list of str
        """
        return self._NodeNames

    @NodeNames.setter
    def NodeNames(self, NodeNames):
        self._NodeNames = NodeNames

    @property
    def ForceRestart(self):
        r"""Whether to force restart
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def RestartMode(self):
        r"""The restart mode. Valid values: `in-place` (default), `blue-green`.
        :rtype: str
        """
        return self._RestartMode

    @RestartMode.setter
    def RestartMode(self, RestartMode):
        self._RestartMode = RestartMode

    @property
    def IsOffline(self):
        r"""The node status, applicable in the blue/green mode. The blue/green restart is risky if the node is offline.
        :rtype: bool
        """
        return self._IsOffline

    @IsOffline.setter
    def IsOffline(self, IsOffline):
        self._IsOffline = IsOffline


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeNames = params.get("NodeNames")
        self._ForceRestart = params.get("ForceRestart")
        self._RestartMode = params.get("RestartMode")
        self._IsOffline = params.get("IsOffline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartNodesResponse(AbstractModel):
    r"""RestartNodes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SubTaskDetail(AbstractModel):
    r"""Information of subtask in workflow task in the instance operation history (such as each check item in a upgrade check task)

    """

    def __init__(self):
        r"""
        :param _Name: Subtask name
        :type Name: str
        :param _Result: Subtask result
        :type Result: bool
        :param _ErrMsg: Subtask error message
        :type ErrMsg: str
        :param _Type: Subtask type
        :type Type: str
        :param _Status: Subtask status. 0: processing, 1: succeeded, -1: failed
        :type Status: int
        :param _FailedIndices: Name of the index for which the check for upgrade failed
        :type FailedIndices: list of str
        :param _FinishTime: Subtask end time
        :type FinishTime: str
        :param _Level: Subtask level. 1: warning, 2: failed
        :type Level: int
        """
        self._Name = None
        self._Result = None
        self._ErrMsg = None
        self._Type = None
        self._Status = None
        self._FailedIndices = None
        self._FinishTime = None
        self._Level = None

    @property
    def Name(self):
        r"""Subtask name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Result(self):
        r"""Subtask result
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrMsg(self):
        r"""Subtask error message
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Type(self):
        r"""Subtask type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""Subtask status. 0: processing, 1: succeeded, -1: failed
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailedIndices(self):
        r"""Name of the index for which the check for upgrade failed
        :rtype: list of str
        """
        return self._FailedIndices

    @FailedIndices.setter
    def FailedIndices(self, FailedIndices):
        self._FailedIndices = FailedIndices

    @property
    def FinishTime(self):
        r"""Subtask end time
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Level(self):
        r"""Subtask level. 1: warning, 2: failed
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Result = params.get("Result")
        self._ErrMsg = params.get("ErrMsg")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._FailedIndices = params.get("FailedIndices")
        self._FinishTime = params.get("FinishTime")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    r"""Instance tag information

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value
        :rtype: str
        """
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
        


class TaskDetail(AbstractModel):
    r"""Information of workflow task in instance operation history

    """

    def __init__(self):
        r"""
        :param _Name: Task name
        :type Name: str
        :param _Progress: Task progress
        :type Progress: float
        :param _FinishTime: Task completion time
        :type FinishTime: str
        :param _SubTasks: Subtask
        :type SubTasks: list of SubTaskDetail
        :param _ElapsedTime: The task time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ElapsedTime: int
        """
        self._Name = None
        self._Progress = None
        self._FinishTime = None
        self._SubTasks = None
        self._ElapsedTime = None

    @property
    def Name(self):
        r"""Task name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Progress(self):
        r"""Task progress
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def FinishTime(self):
        r"""Task completion time
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def SubTasks(self):
        r"""Subtask
        :rtype: list of SubTaskDetail
        """
        return self._SubTasks

    @SubTasks.setter
    def SubTasks(self, SubTasks):
        self._SubTasks = SubTasks

    @property
    def ElapsedTime(self):
        r"""The task time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ElapsedTime

    @ElapsedTime.setter
    def ElapsedTime(self, ElapsedTime):
        self._ElapsedTime = ElapsedTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Progress = params.get("Progress")
        self._FinishTime = params.get("FinishTime")
        if params.get("SubTasks") is not None:
            self._SubTasks = []
            for item in params.get("SubTasks"):
                obj = SubTaskDetail()
                obj._deserialize(item)
                self._SubTasks.append(obj)
        self._ElapsedTime = params.get("ElapsedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDictionariesRequest(AbstractModel):
    r"""UpdateDictionaries request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES instance ID
        :type InstanceId: str
        :param _IkMainDicts: COS address of the main dictionary for the IK analyzer
        :type IkMainDicts: list of str
        :param _IkStopwords: COS address of the stopword dictionary for the IK analyzer
        :type IkStopwords: list of str
        :param _Synonym: COS address of the synonym dictionary
        :type Synonym: list of str
        :param _QQDict: COS address of the QQ dictionary
        :type QQDict: list of str
        :param _UpdateType: `0` (default): Install, `1`: Delete
        :type UpdateType: int
        :param _ForceRestart: Whether to force restart the cluster. The default value is `false`.
        :type ForceRestart: bool
        """
        self._InstanceId = None
        self._IkMainDicts = None
        self._IkStopwords = None
        self._Synonym = None
        self._QQDict = None
        self._UpdateType = None
        self._ForceRestart = None

    @property
    def InstanceId(self):
        r"""ES instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IkMainDicts(self):
        r"""COS address of the main dictionary for the IK analyzer
        :rtype: list of str
        """
        return self._IkMainDicts

    @IkMainDicts.setter
    def IkMainDicts(self, IkMainDicts):
        self._IkMainDicts = IkMainDicts

    @property
    def IkStopwords(self):
        r"""COS address of the stopword dictionary for the IK analyzer
        :rtype: list of str
        """
        return self._IkStopwords

    @IkStopwords.setter
    def IkStopwords(self, IkStopwords):
        self._IkStopwords = IkStopwords

    @property
    def Synonym(self):
        r"""COS address of the synonym dictionary
        :rtype: list of str
        """
        return self._Synonym

    @Synonym.setter
    def Synonym(self, Synonym):
        self._Synonym = Synonym

    @property
    def QQDict(self):
        r"""COS address of the QQ dictionary
        :rtype: list of str
        """
        return self._QQDict

    @QQDict.setter
    def QQDict(self, QQDict):
        self._QQDict = QQDict

    @property
    def UpdateType(self):
        r"""`0` (default): Install, `1`: Delete
        :rtype: int
        """
        return self._UpdateType

    @UpdateType.setter
    def UpdateType(self, UpdateType):
        self._UpdateType = UpdateType

    @property
    def ForceRestart(self):
        r"""Whether to force restart the cluster. The default value is `false`.
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IkMainDicts = params.get("IkMainDicts")
        self._IkStopwords = params.get("IkStopwords")
        self._Synonym = params.get("Synonym")
        self._QQDict = params.get("QQDict")
        self._UpdateType = params.get("UpdateType")
        self._ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDictionariesResponse(AbstractModel):
    r"""UpdateDictionaries response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateIndexRequest(AbstractModel):
    r"""UpdateIndex request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES cluster ID
        :type InstanceId: str
        :param _IndexType: Type of the index to update. `auto`: Automated; `normal`: General.
        :type IndexType: str
        :param _IndexName: Name of the index to update
        :type IndexName: str
        :param _UpdateMetaJson: JSON-formatted index metadata to update, such as `mappings` and `settings`.
        :type UpdateMetaJson: str
        :param _Username: Username for cluster access
        :type Username: str
        :param _Password: Password for cluster access
        :type Password: str
        :param _RolloverBackingIndex: Whether to roll over the backup index
        :type RolloverBackingIndex: bool
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._UpdateMetaJson = None
        self._Username = None
        self._Password = None
        self._RolloverBackingIndex = None

    @property
    def InstanceId(self):
        r"""ES cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        r"""Type of the index to update. `auto`: Automated; `normal`: General.
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""Name of the index to update
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def UpdateMetaJson(self):
        r"""JSON-formatted index metadata to update, such as `mappings` and `settings`.
        :rtype: str
        """
        return self._UpdateMetaJson

    @UpdateMetaJson.setter
    def UpdateMetaJson(self, UpdateMetaJson):
        self._UpdateMetaJson = UpdateMetaJson

    @property
    def Username(self):
        r"""Username for cluster access
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""Password for cluster access
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RolloverBackingIndex(self):
        r"""Whether to roll over the backup index
        :rtype: bool
        """
        return self._RolloverBackingIndex

    @RolloverBackingIndex.setter
    def RolloverBackingIndex(self, RolloverBackingIndex):
        self._RolloverBackingIndex = RolloverBackingIndex


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._UpdateMetaJson = params.get("UpdateMetaJson")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._RolloverBackingIndex = params.get("RolloverBackingIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateIndexResponse(AbstractModel):
    r"""UpdateIndex response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateInstanceRequest(AbstractModel):
    r"""UpdateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)
        :type InstanceName: str
        :param _NodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2-50)
        :type NodeNum: int
        :param _EsConfig: ES configuration item (JSON string)
        :type EsConfig: str
        :param _Password: Password of the default user 'elastic', which must contain 8 to 16 characters, including at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]
        :type Password: str
        :param _EsAcl: The policy for visual component (Kibana and Cerebro) access over public network.
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _DiskSize: This parameter has been disused. Please use `NodeInfoList`
Disk size in GB
        :type DiskSize: int
        :param _NodeType: This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param _MasterNodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of dedicated primary nodes (only 3 and 5 are supported)
        :type MasterNodeNum: int
        :param _MasterNodeType: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :type MasterNodeType: str
        :param _MasterNodeDiskSize: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node disk size in GB. This is 50 GB by default and currently cannot be customized
        :type MasterNodeDiskSize: int
        :param _ForceRestart: Whether to force restart during configuration update <li>true: Yes </li><li>false: No </li>This needs to be set only for EsConfig. Default value: false
        :type ForceRestart: bool
        :param _CosBackup: Auto-backup to COS
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param _NodeInfoList: Node information list. You can pass in only the nodes to be updated and their corresponding specification information. Supported operations include: <li>modifying the number of nodes in the same type </li><li>modifying the specification and disk size of nodes in the same type </li><li>adding a node type (you must also specify the node type, quantity, specification, disk, etc.) </li>The above operations can only be performed one at a time, and the disk type cannot be modified
        :type NodeInfoList: list of NodeInfo
        :param _PublicAccess: The status of ES cluster access over public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type PublicAccess: str
        :param _EsPublicAcl: Public network ACL
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`
        :param _KibanaPublicAccess: The status of Kibana access over public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type KibanaPublicAccess: str
        :param _KibanaPrivateAccess: The status of Kibana access over private network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type KibanaPrivateAccess: str
        :param _BasicSecurityType: Enables or disables user authentication for ES Basic Edition v6.8 and above
        :type BasicSecurityType: int
        :param _KibanaPrivatePort: Kibana private port
        :type KibanaPrivatePort: int
        :param _ScaleType: 0: scaling in blue/green deployment mode without cluster restart (default); 1: scaling by unmounting disk with rolling cluster restart
        :type ScaleType: int
        :param _MultiZoneInfo: Multi-AZ deployment
        :type MultiZoneInfo: list of ZoneDetail
        :param _SceneType: Scenario template type. -1: not enabled; 1: general; 2: log; 3: search
        :type SceneType: int
        :param _KibanaConfig: Kibana configuration item (JSON string)
        :type KibanaConfig: str
        :param _WebNodeTypeInfo: Visual node configuration
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param _SwitchPrivateLink: Whether to switch to the new network architecture
        :type SwitchPrivateLink: str
        :param _EnableCerebro: Whether to enable Cerebro
        :type EnableCerebro: bool
        :param _CerebroPublicAccess: The status of Cerebro access over public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type CerebroPublicAccess: str
        :param _CerebroPrivateAccess: The status of Cerebro access over private network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type CerebroPrivateAccess: str
        :param _EsConfigSet: Added or modified configuration set information
        :type EsConfigSet: :class:`tencentcloud.es.v20180416.models.EsConfigSetInfo`
        :param _OperationDuration: The maintenance time slot
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        :param _KibanaAlteringPublicAccess: Whether to enable the option for sending alerting messages over the public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :type KibanaAlteringPublicAccess: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._NodeNum = None
        self._EsConfig = None
        self._Password = None
        self._EsAcl = None
        self._DiskSize = None
        self._NodeType = None
        self._MasterNodeNum = None
        self._MasterNodeType = None
        self._MasterNodeDiskSize = None
        self._ForceRestart = None
        self._CosBackup = None
        self._NodeInfoList = None
        self._PublicAccess = None
        self._EsPublicAcl = None
        self._KibanaPublicAccess = None
        self._KibanaPrivateAccess = None
        self._BasicSecurityType = None
        self._KibanaPrivatePort = None
        self._ScaleType = None
        self._MultiZoneInfo = None
        self._SceneType = None
        self._KibanaConfig = None
        self._WebNodeTypeInfo = None
        self._SwitchPrivateLink = None
        self._EnableCerebro = None
        self._CerebroPublicAccess = None
        self._CerebroPrivateAccess = None
        self._EsConfigSet = None
        self._OperationDuration = None
        self._KibanaAlteringPublicAccess = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NodeNum(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2-50)
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def EsConfig(self):
        r"""ES configuration item (JSON string)
        :rtype: str
        """
        return self._EsConfig

    @EsConfig.setter
    def EsConfig(self, EsConfig):
        self._EsConfig = EsConfig

    @property
    def Password(self):
        r"""Password of the default user 'elastic', which must contain 8 to 16 characters, including at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EsAcl(self):
        r"""The policy for visual component (Kibana and Cerebro) access over public network.
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._EsAcl

    @EsAcl.setter
    def EsAcl(self, EsAcl):
        self._EsAcl = EsAcl

    @property
    def DiskSize(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Disk size in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def NodeType(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def MasterNodeNum(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Number of dedicated primary nodes (only 3 and 5 are supported)
        :rtype: int
        """
        return self._MasterNodeNum

    @MasterNodeNum.setter
    def MasterNodeNum(self, MasterNodeNum):
        self._MasterNodeNum = MasterNodeNum

    @property
    def MasterNodeType(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :rtype: str
        """
        return self._MasterNodeType

    @MasterNodeType.setter
    def MasterNodeType(self, MasterNodeType):
        self._MasterNodeType = MasterNodeType

    @property
    def MasterNodeDiskSize(self):
        r"""This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node disk size in GB. This is 50 GB by default and currently cannot be customized
        :rtype: int
        """
        return self._MasterNodeDiskSize

    @MasterNodeDiskSize.setter
    def MasterNodeDiskSize(self, MasterNodeDiskSize):
        self._MasterNodeDiskSize = MasterNodeDiskSize

    @property
    def ForceRestart(self):
        r"""Whether to force restart during configuration update <li>true: Yes </li><li>false: No </li>This needs to be set only for EsConfig. Default value: false
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def CosBackup(self):
        r"""Auto-backup to COS
        :rtype: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup

    @property
    def NodeInfoList(self):
        r"""Node information list. You can pass in only the nodes to be updated and their corresponding specification information. Supported operations include: <li>modifying the number of nodes in the same type </li><li>modifying the specification and disk size of nodes in the same type </li><li>adding a node type (you must also specify the node type, quantity, specification, disk, etc.) </li>The above operations can only be performed one at a time, and the disk type cannot be modified
        :rtype: list of NodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList

    @property
    def PublicAccess(self):
        r"""The status of ES cluster access over public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :rtype: str
        """
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def EsPublicAcl(self):
        r"""Public network ACL
        :rtype: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`
        """
        return self._EsPublicAcl

    @EsPublicAcl.setter
    def EsPublicAcl(self, EsPublicAcl):
        self._EsPublicAcl = EsPublicAcl

    @property
    def KibanaPublicAccess(self):
        r"""The status of Kibana access over public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :rtype: str
        """
        return self._KibanaPublicAccess

    @KibanaPublicAccess.setter
    def KibanaPublicAccess(self, KibanaPublicAccess):
        self._KibanaPublicAccess = KibanaPublicAccess

    @property
    def KibanaPrivateAccess(self):
        r"""The status of Kibana access over private network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :rtype: str
        """
        return self._KibanaPrivateAccess

    @KibanaPrivateAccess.setter
    def KibanaPrivateAccess(self, KibanaPrivateAccess):
        self._KibanaPrivateAccess = KibanaPrivateAccess

    @property
    def BasicSecurityType(self):
        r"""Enables or disables user authentication for ES Basic Edition v6.8 and above
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def KibanaPrivatePort(self):
        r"""Kibana private port
        :rtype: int
        """
        return self._KibanaPrivatePort

    @KibanaPrivatePort.setter
    def KibanaPrivatePort(self, KibanaPrivatePort):
        self._KibanaPrivatePort = KibanaPrivatePort

    @property
    def ScaleType(self):
        r"""0: scaling in blue/green deployment mode without cluster restart (default); 1: scaling by unmounting disk with rolling cluster restart
        :rtype: int
        """
        return self._ScaleType

    @ScaleType.setter
    def ScaleType(self, ScaleType):
        self._ScaleType = ScaleType

    @property
    def MultiZoneInfo(self):
        r"""Multi-AZ deployment
        :rtype: list of ZoneDetail
        """
        return self._MultiZoneInfo

    @MultiZoneInfo.setter
    def MultiZoneInfo(self, MultiZoneInfo):
        self._MultiZoneInfo = MultiZoneInfo

    @property
    def SceneType(self):
        r"""Scenario template type. -1: not enabled; 1: general; 2: log; 3: search
        :rtype: int
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def KibanaConfig(self):
        r"""Kibana configuration item (JSON string)
        :rtype: str
        """
        return self._KibanaConfig

    @KibanaConfig.setter
    def KibanaConfig(self, KibanaConfig):
        self._KibanaConfig = KibanaConfig

    @property
    def WebNodeTypeInfo(self):
        r"""Visual node configuration
        :rtype: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        """
        return self._WebNodeTypeInfo

    @WebNodeTypeInfo.setter
    def WebNodeTypeInfo(self, WebNodeTypeInfo):
        self._WebNodeTypeInfo = WebNodeTypeInfo

    @property
    def SwitchPrivateLink(self):
        r"""Whether to switch to the new network architecture
        :rtype: str
        """
        return self._SwitchPrivateLink

    @SwitchPrivateLink.setter
    def SwitchPrivateLink(self, SwitchPrivateLink):
        self._SwitchPrivateLink = SwitchPrivateLink

    @property
    def EnableCerebro(self):
        r"""Whether to enable Cerebro
        :rtype: bool
        """
        return self._EnableCerebro

    @EnableCerebro.setter
    def EnableCerebro(self, EnableCerebro):
        self._EnableCerebro = EnableCerebro

    @property
    def CerebroPublicAccess(self):
        r"""The status of Cerebro access over public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :rtype: str
        """
        return self._CerebroPublicAccess

    @CerebroPublicAccess.setter
    def CerebroPublicAccess(self, CerebroPublicAccess):
        self._CerebroPublicAccess = CerebroPublicAccess

    @property
    def CerebroPrivateAccess(self):
        r"""The status of Cerebro access over private network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :rtype: str
        """
        return self._CerebroPrivateAccess

    @CerebroPrivateAccess.setter
    def CerebroPrivateAccess(self, CerebroPrivateAccess):
        self._CerebroPrivateAccess = CerebroPrivateAccess

    @property
    def EsConfigSet(self):
        r"""Added or modified configuration set information
        :rtype: :class:`tencentcloud.es.v20180416.models.EsConfigSetInfo`
        """
        return self._EsConfigSet

    @EsConfigSet.setter
    def EsConfigSet(self, EsConfigSet):
        self._EsConfigSet = EsConfigSet

    @property
    def OperationDuration(self):
        r"""The maintenance time slot
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def KibanaAlteringPublicAccess(self):
        r"""Whether to enable the option for sending alerting messages over the public network.
`OPEN`: Enabled.
`CLOSE`: Disabled.
        :rtype: str
        """
        return self._KibanaAlteringPublicAccess

    @KibanaAlteringPublicAccess.setter
    def KibanaAlteringPublicAccess(self, KibanaAlteringPublicAccess):
        self._KibanaAlteringPublicAccess = KibanaAlteringPublicAccess


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._NodeNum = params.get("NodeNum")
        self._EsConfig = params.get("EsConfig")
        self._Password = params.get("Password")
        if params.get("EsAcl") is not None:
            self._EsAcl = EsAcl()
            self._EsAcl._deserialize(params.get("EsAcl"))
        self._DiskSize = params.get("DiskSize")
        self._NodeType = params.get("NodeType")
        self._MasterNodeNum = params.get("MasterNodeNum")
        self._MasterNodeType = params.get("MasterNodeType")
        self._MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self._ForceRestart = params.get("ForceRestart")
        if params.get("CosBackup") is not None:
            self._CosBackup = CosBackup()
            self._CosBackup._deserialize(params.get("CosBackup"))
        if params.get("NodeInfoList") is not None:
            self._NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfoList.append(obj)
        self._PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self._EsPublicAcl = EsPublicAcl()
            self._EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self._KibanaPublicAccess = params.get("KibanaPublicAccess")
        self._KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self._BasicSecurityType = params.get("BasicSecurityType")
        self._KibanaPrivatePort = params.get("KibanaPrivatePort")
        self._ScaleType = params.get("ScaleType")
        if params.get("MultiZoneInfo") is not None:
            self._MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self._MultiZoneInfo.append(obj)
        self._SceneType = params.get("SceneType")
        self._KibanaConfig = params.get("KibanaConfig")
        if params.get("WebNodeTypeInfo") is not None:
            self._WebNodeTypeInfo = WebNodeTypeInfo()
            self._WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self._SwitchPrivateLink = params.get("SwitchPrivateLink")
        self._EnableCerebro = params.get("EnableCerebro")
        self._CerebroPublicAccess = params.get("CerebroPublicAccess")
        self._CerebroPrivateAccess = params.get("CerebroPrivateAccess")
        if params.get("EsConfigSet") is not None:
            self._EsConfigSet = EsConfigSetInfo()
            self._EsConfigSet._deserialize(params.get("EsConfigSet"))
        if params.get("OperationDuration") is not None:
            self._OperationDuration = OperationDurationUpdated()
            self._OperationDuration._deserialize(params.get("OperationDuration"))
        self._KibanaAlteringPublicAccess = params.get("KibanaAlteringPublicAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceResponse(AbstractModel):
    r"""UpdateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order ID
Note: This field may return `null`, indicating that no valid value was found.
        :type DealName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class UpdatePluginsRequest(AbstractModel):
    r"""UpdatePlugins request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstallPluginList: List of names of the plugins to be installed
        :type InstallPluginList: list of str
        :param _RemovePluginList: List of names of the plugins to be uninstalled
        :type RemovePluginList: list of str
        :param _ForceRestart: Whether to force restart the cluster. The default value is `false`.
        :type ForceRestart: bool
        :param _ForceUpdate: Whether to reinstall the cluster. The default value is `false`.
        :type ForceUpdate: bool
        :param _PluginType: 0: system plugin
        :type PluginType: int
        """
        self._InstanceId = None
        self._InstallPluginList = None
        self._RemovePluginList = None
        self._ForceRestart = None
        self._ForceUpdate = None
        self._PluginType = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstallPluginList(self):
        r"""List of names of the plugins to be installed
        :rtype: list of str
        """
        return self._InstallPluginList

    @InstallPluginList.setter
    def InstallPluginList(self, InstallPluginList):
        self._InstallPluginList = InstallPluginList

    @property
    def RemovePluginList(self):
        r"""List of names of the plugins to be uninstalled
        :rtype: list of str
        """
        return self._RemovePluginList

    @RemovePluginList.setter
    def RemovePluginList(self, RemovePluginList):
        self._RemovePluginList = RemovePluginList

    @property
    def ForceRestart(self):
        r"""Whether to force restart the cluster. The default value is `false`.
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def ForceUpdate(self):
        r"""Whether to reinstall the cluster. The default value is `false`.
        :rtype: bool
        """
        return self._ForceUpdate

    @ForceUpdate.setter
    def ForceUpdate(self, ForceUpdate):
        self._ForceUpdate = ForceUpdate

    @property
    def PluginType(self):
        r"""0: system plugin
        :rtype: int
        """
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstallPluginList = params.get("InstallPluginList")
        self._RemovePluginList = params.get("RemovePluginList")
        self._ForceRestart = params.get("ForceRestart")
        self._ForceUpdate = params.get("ForceUpdate")
        self._PluginType = params.get("PluginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePluginsResponse(AbstractModel):
    r"""UpdatePlugins response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateRequestTargetNodeTypesRequest(AbstractModel):
    r"""UpdateRequestTargetNodeTypes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _TargetNodeTypes: A list of node types used to receive requests.
        :type TargetNodeTypes: list of str
        """
        self._InstanceId = None
        self._TargetNodeTypes = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TargetNodeTypes(self):
        r"""A list of node types used to receive requests.
        :rtype: list of str
        """
        return self._TargetNodeTypes

    @TargetNodeTypes.setter
    def TargetNodeTypes(self, TargetNodeTypes):
        self._TargetNodeTypes = TargetNodeTypes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TargetNodeTypes = params.get("TargetNodeTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRequestTargetNodeTypesResponse(AbstractModel):
    r"""UpdateRequestTargetNodeTypes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpgradeInstanceRequest(AbstractModel):
    r"""UpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _EsVersion: Target ES version. Valid values: 6.4.3, 6.8.2, 7.5.1
        :type EsVersion: str
        :param _CheckOnly: Whether to check for upgrade only. Default value: false
        :type CheckOnly: bool
        :param _LicenseType: Target X-Pack edition: <li>OSS: Open-source Edition </li><li>basic: Basic Edition </li>Currently only used for v5.6.4 to v6.x upgrade. Default value: basic
        :type LicenseType: str
        :param _BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :type BasicSecurityType: int
        :param _UpgradeMode: Upgrade mode. <li>scale: blue/green deployment</li><li>restart: rolling restart</li>Default value: scale
        :type UpgradeMode: str
        :param _CosBackup: Whether to back up the cluster before version upgrade (no backup by default)
        :type CosBackup: bool
        :param _SkipCheckForceRestart: Whether to skip the check and perform a force restart in the rolling mode. Default value: `false`.
        :type SkipCheckForceRestart: bool
        """
        self._InstanceId = None
        self._EsVersion = None
        self._CheckOnly = None
        self._LicenseType = None
        self._BasicSecurityType = None
        self._UpgradeMode = None
        self._CosBackup = None
        self._SkipCheckForceRestart = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EsVersion(self):
        r"""Target ES version. Valid values: 6.4.3, 6.8.2, 7.5.1
        :rtype: str
        """
        return self._EsVersion

    @EsVersion.setter
    def EsVersion(self, EsVersion):
        self._EsVersion = EsVersion

    @property
    def CheckOnly(self):
        r"""Whether to check for upgrade only. Default value: false
        :rtype: bool
        """
        return self._CheckOnly

    @CheckOnly.setter
    def CheckOnly(self, CheckOnly):
        self._CheckOnly = CheckOnly

    @property
    def LicenseType(self):
        r"""Target X-Pack edition: <li>OSS: Open-source Edition </li><li>basic: Basic Edition </li>Currently only used for v5.6.4 to v6.x upgrade. Default value: basic
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def BasicSecurityType(self):
        r"""Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def UpgradeMode(self):
        r"""Upgrade mode. <li>scale: blue/green deployment</li><li>restart: rolling restart</li>Default value: scale
        :rtype: str
        """
        return self._UpgradeMode

    @UpgradeMode.setter
    def UpgradeMode(self, UpgradeMode):
        self._UpgradeMode = UpgradeMode

    @property
    def CosBackup(self):
        r"""Whether to back up the cluster before version upgrade (no backup by default)
        :rtype: bool
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup

    @property
    def SkipCheckForceRestart(self):
        r"""Whether to skip the check and perform a force restart in the rolling mode. Default value: `false`.
        :rtype: bool
        """
        return self._SkipCheckForceRestart

    @SkipCheckForceRestart.setter
    def SkipCheckForceRestart(self, SkipCheckForceRestart):
        self._SkipCheckForceRestart = SkipCheckForceRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EsVersion = params.get("EsVersion")
        self._CheckOnly = params.get("CheckOnly")
        self._LicenseType = params.get("LicenseType")
        self._BasicSecurityType = params.get("BasicSecurityType")
        self._UpgradeMode = params.get("UpgradeMode")
        self._CosBackup = params.get("CosBackup")
        self._SkipCheckForceRestart = params.get("SkipCheckForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    r"""UpgradeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpgradeLicenseRequest(AbstractModel):
    r"""UpgradeLicense request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :type LicenseType: str
        :param _AutoVoucher: Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0
        :type AutoVoucher: int
        :param _VoucherIds: List of voucher IDs (only one voucher can be specified at a time currently)
        :type VoucherIds: list of str
        :param _BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :type BasicSecurityType: int
        :param _ForceRestart: Whether to force restart <li>true: yes </li><li>false: no </li>Default value: false
        :type ForceRestart: bool
        """
        self._InstanceId = None
        self._LicenseType = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._BasicSecurityType = None
        self._ForceRestart = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LicenseType(self):
        r"""License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def AutoVoucher(self):
        r"""Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""List of voucher IDs (only one voucher can be specified at a time currently)
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def BasicSecurityType(self):
        r"""Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def ForceRestart(self):
        r"""Whether to force restart <li>true: yes </li><li>false: no </li>Default value: false
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LicenseType = params.get("LicenseType")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._BasicSecurityType = params.get("BasicSecurityType")
        self._ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLicenseResponse(AbstractModel):
    r"""UpgradeLicense response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order ID
Note: This field may return `null`, indicating that no valid value was found.
        :type DealName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        r"""The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class WebNodeTypeInfo(AbstractModel):
    r"""Visual node configuration

    """

    def __init__(self):
        r"""
        :param _NodeNum: Number of visual nodes. The value is always `1`.
        :type NodeNum: int
        :param _NodeType: Visual node specification
        :type NodeType: str
        """
        self._NodeNum = None
        self._NodeType = None

    @property
    def NodeNum(self):
        r"""Number of visual nodes. The value is always `1`.
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def NodeType(self):
        r"""Visual node specification
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType


    def _deserialize(self, params):
        self._NodeNum = params.get("NodeNum")
        self._NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDetail(AbstractModel):
    r"""Details of AZs in multi-AZ deployment mode

    """

    def __init__(self):
        r"""
        :param _Zone: AZ
        :type Zone: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        """
        self._Zone = None
        self._SubnetId = None

    @property
    def Zone(self):
        r"""AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        r"""Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        