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


class AutoScaleDiskInfo(AbstractModel):
    r"""Auto capacity expansion parameter for cvm

    """

    def __init__(self):
        r"""
        :param _NodeType: Node type. Valid values: `hotData`, `warmData`.
        :type NodeType: str
        :param _ScaleType: 0: Percentage-based scale-out; 1: Absolute value-based scale-out
        :type ScaleType: int
        :param _Threshold: Trigger threshold. Unit: %. For example, 80%.
        :type Threshold: int
        :param _Duration: Trigger duration in minutes, for example, 60
        :type Duration: int
        :param _PercentSize: Expansion ratio per time, unit: %, for example, 20%
        :type PercentSize: int
        :param _FixSize: Absolute value-based scale-out, in GB, for example, 100 GB
        :type FixSize: int
        :param _MaxSize: Capacity limit for scale-out, in GB, for example, 500 GB
        :type MaxSize: int
        """
        self._NodeType = None
        self._ScaleType = None
        self._Threshold = None
        self._Duration = None
        self._PercentSize = None
        self._FixSize = None
        self._MaxSize = None

    @property
    def NodeType(self):
        r"""Node type. Valid values: `hotData`, `warmData`.
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ScaleType(self):
        r"""0: Percentage-based scale-out; 1: Absolute value-based scale-out
        :rtype: int
        """
        return self._ScaleType

    @ScaleType.setter
    def ScaleType(self, ScaleType):
        self._ScaleType = ScaleType

    @property
    def Threshold(self):
        r"""Trigger threshold. Unit: %. For example, 80%.
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Duration(self):
        r"""Trigger duration in minutes, for example, 60
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def PercentSize(self):
        r"""Expansion ratio per time, unit: %, for example, 20%
        :rtype: int
        """
        return self._PercentSize

    @PercentSize.setter
    def PercentSize(self, PercentSize):
        self._PercentSize = PercentSize

    @property
    def FixSize(self):
        r"""Absolute value-based scale-out, in GB, for example, 100 GB
        :rtype: int
        """
        return self._FixSize

    @FixSize.setter
    def FixSize(self, FixSize):
        self._FixSize = FixSize

    @property
    def MaxSize(self):
        r"""Capacity limit for scale-out, in GB, for example, 500 GB
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._ScaleType = params.get("ScaleType")
        self._Threshold = params.get("Threshold")
        self._Duration = params.get("Duration")
        self._PercentSize = params.get("PercentSize")
        self._FixSize = params.get("FixSize")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackingIndexMetaField(AbstractModel):
    r"""Backup index metadata field

    """

    def __init__(self):
        r"""
        :param _IndexName: <p>Backing index name</p>
        :type IndexName: str
        :param _IndexStatus: <p>Backup index status</p>
        :type IndexStatus: str
        :param _IndexStorage: <p>Backup index storage size</p>
        :type IndexStorage: int
        :param _IndexPhrase: <p>Backup index current lifecycle</p>
        :type IndexPhrase: str
        :param _IndexCreateTime: <p>Backup index creation time</p>
        :type IndexCreateTime: str
        :param _IndexUuid: <p>Index Uuid</p>
        :type IndexUuid: str
        """
        self._IndexName = None
        self._IndexStatus = None
        self._IndexStorage = None
        self._IndexPhrase = None
        self._IndexCreateTime = None
        self._IndexUuid = None

    @property
    def IndexName(self):
        r"""<p>Backing index name</p>
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexStatus(self):
        r"""<p>Backup index status</p>
        :rtype: str
        """
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus

    @property
    def IndexStorage(self):
        r"""<p>Backup index storage size</p>
        :rtype: int
        """
        return self._IndexStorage

    @IndexStorage.setter
    def IndexStorage(self, IndexStorage):
        self._IndexStorage = IndexStorage

    @property
    def IndexPhrase(self):
        r"""<p>Backup index current lifecycle</p>
        :rtype: str
        """
        return self._IndexPhrase

    @IndexPhrase.setter
    def IndexPhrase(self, IndexPhrase):
        self._IndexPhrase = IndexPhrase

    @property
    def IndexCreateTime(self):
        r"""<p>Backup index creation time</p>
        :rtype: str
        """
        return self._IndexCreateTime

    @IndexCreateTime.setter
    def IndexCreateTime(self, IndexCreateTime):
        self._IndexCreateTime = IndexCreateTime

    @property
    def IndexUuid(self):
        r"""<p>Index Uuid</p>
        :rtype: str
        """
        return self._IndexUuid

    @IndexUuid.setter
    def IndexUuid(self, IndexUuid):
        self._IndexUuid = IndexUuid


    def _deserialize(self, params):
        self._IndexName = params.get("IndexName")
        self._IndexStatus = params.get("IndexStatus")
        self._IndexStorage = params.get("IndexStorage")
        self._IndexPhrase = params.get("IndexPhrase")
        self._IndexCreateTime = params.get("IndexCreateTime")
        self._IndexUuid = params.get("IndexUuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterView(AbstractModel):
    r"""Cluster dimension view data

    """

    def __init__(self):
        r"""
        :param _Health: Cluster health status
        :type Health: float
        :param _Visible: Whether the cluster is visible
        :type Visible: float
        :param _Break: Whether to fuse the cluster
        :type Break: float
        :param _AvgDiskUsage: Average Disk Usage
        :type AvgDiskUsage: float
        :param _AvgMemUsage: Average memory utilization
        :type AvgMemUsage: float
        :param _AvgCpuUsage: Average CPU Usage
        :type AvgCpuUsage: float
        :param _TotalDiskSize: Total storage size of a cluster.
        :type TotalDiskSize: int
        :param _TargetNodeTypes: Client request node
        :type TargetNodeTypes: list of str
        :param _NodeNum: Number of online nodes
        :type NodeNum: int
        :param _TotalNodeNum: Total number of nodes
        :type TotalNodeNum: int
        :param _DataNodeNum: Number of Data Nodes
        :type DataNodeNum: int
        :param _IndexNum: Index count
        :type IndexNum: int
        :param _DocNum: Number of documents
        :type DocNum: int
        :param _DiskUsedInBytes: Used bytes of the disk
        :type DiskUsedInBytes: int
        :param _ShardNum: Number of shards
        :type ShardNum: int
        :param _PrimaryShardNum: Number of primary shards
        :type PrimaryShardNum: int
        :param _RelocatingShardNum: Number of migrating shards
        :type RelocatingShardNum: int
        :param _InitializingShardNum: Number of initializing shards.
        :type InitializingShardNum: int
        :param _UnassignedShardNum: Number of unassigned shards
        :type UnassignedShardNum: int
        :param _TotalCosStorage: Enterprise Edition COS storage capacity size in GB
        :type TotalCosStorage: int
        :param _SearchableSnapshotCosBucket: bucket name for storing cos searchable snapshots in the Enterprise Edition cluster
        :type SearchableSnapshotCosBucket: str
        :param _SearchableSnapshotCosAppId: App ID of the cos bucket for searchable snapshots in the Enterprise Edition cluster
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
        r"""Whether to fuse the cluster
        :rtype: float
        """
        return self._Break

    @Break.setter
    def Break(self, Break):
        self._Break = Break

    @property
    def AvgDiskUsage(self):
        r"""Average Disk Usage
        :rtype: float
        """
        return self._AvgDiskUsage

    @AvgDiskUsage.setter
    def AvgDiskUsage(self, AvgDiskUsage):
        self._AvgDiskUsage = AvgDiskUsage

    @property
    def AvgMemUsage(self):
        r"""Average memory utilization
        :rtype: float
        """
        return self._AvgMemUsage

    @AvgMemUsage.setter
    def AvgMemUsage(self, AvgMemUsage):
        self._AvgMemUsage = AvgMemUsage

    @property
    def AvgCpuUsage(self):
        r"""Average CPU Usage
        :rtype: float
        """
        return self._AvgCpuUsage

    @AvgCpuUsage.setter
    def AvgCpuUsage(self, AvgCpuUsage):
        self._AvgCpuUsage = AvgCpuUsage

    @property
    def TotalDiskSize(self):
        r"""Total storage size of a cluster.
        :rtype: int
        """
        return self._TotalDiskSize

    @TotalDiskSize.setter
    def TotalDiskSize(self, TotalDiskSize):
        self._TotalDiskSize = TotalDiskSize

    @property
    def TargetNodeTypes(self):
        r"""Client request node
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
        r"""Number of Data Nodes
        :rtype: int
        """
        return self._DataNodeNum

    @DataNodeNum.setter
    def DataNodeNum(self, DataNodeNum):
        self._DataNodeNum = DataNodeNum

    @property
    def IndexNum(self):
        r"""Index count
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
        r"""Used bytes of the disk
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
        r"""Number of migrating shards
        :rtype: int
        """
        return self._RelocatingShardNum

    @RelocatingShardNum.setter
    def RelocatingShardNum(self, RelocatingShardNum):
        self._RelocatingShardNum = RelocatingShardNum

    @property
    def InitializingShardNum(self):
        r"""Number of initializing shards.
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
        r"""Enterprise Edition COS storage capacity size in GB
        :rtype: int
        """
        return self._TotalCosStorage

    @TotalCosStorage.setter
    def TotalCosStorage(self, TotalCosStorage):
        self._TotalCosStorage = TotalCosStorage

    @property
    def SearchableSnapshotCosBucket(self):
        r"""bucket name for storing cos searchable snapshots in the Enterprise Edition cluster
        :rtype: str
        """
        return self._SearchableSnapshotCosBucket

    @SearchableSnapshotCosBucket.setter
    def SearchableSnapshotCosBucket(self, SearchableSnapshotCosBucket):
        self._SearchableSnapshotCosBucket = SearchableSnapshotCosBucket

    @property
    def SearchableSnapshotCosAppId(self):
        r"""App ID of the cos bucket for searchable snapshots in the Enterprise Edition cluster
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
    r"""ES cos auto backup information

    """

    def __init__(self):
        r"""
        :param _IsAutoBackup: <p>Whether to enable cos automatic backup</p>
        :type IsAutoBackup: bool
        :param _BackupTime: <p>Automatic backup execution time (accurate to the hour), e.g. "22:00"</p>
        :type BackupTime: str
        :param _SnapshotName: <p>Backup snapshot prefix</p>
        :type SnapshotName: str
        :param _EsRepositoryType: <p>0 (Tencent Cloud repository); 1 (customer repository)</p>
        :type EsRepositoryType: int
        :param _PaasEsRepository: <p>Managed snapshot repository name.</p>
        :type PaasEsRepository: str
        :param _UserEsRepository: <p>Customer snapshot repository name</p>
        :type UserEsRepository: str
        :param _CosBasePath: <p>cos storage folder directory</p>
        :type CosBasePath: str
        :param _StorageDuration: <p>Snapshot storage cycle in days</p>
        :type StorageDuration: int
        :param _AutoBackupInterval: <p>Auto backup frequency in hours.</p>
        :type AutoBackupInterval: int
        :param _CosRetention: <p>Backup lock. Valid values: 0 (not locked) and 1 (locked).</p>
        :type CosRetention: int
        :param _RetainUntilDate: <p>Lock expiration date, such as 2022-12-10T08:34:48.000Z.</p>
        :type RetainUntilDate: str
        :param _RetentionGraceTime: <p>Lock grace period</p>
        :type RetentionGraceTime: int
        :param _RemoteCos: <p>Cross-region backup. Valid values: 0 (disabled) and 1 (enabled).</p>
        :type RemoteCos: int
        :param _RemoteCosRegion: <p>Region name for cross-regional backup, such as ap-guangzhou.</p>
        :type RemoteCosRegion: str
        :param _StrategyName: <p>Policy name.</p>
        :type StrategyName: str
        :param _Indices: <p>Backup index list. If left empty, it means to back up all indexes.</p>
        :type Indices: str
        :param _MultiAz: <p>cos multi-AZ backup. 0: single AZ; 1: multi-AZ</p>
        :type MultiAz: int
        :param _MaxSnapshotPerSec: <p>Maximum speed of write to the repository per node max_snapshot_bytes_per_sec, default 40m</p>
        :type MaxSnapshotPerSec: str
        :param _MaxRestorePerSec: <p>Maximum speed of reading the repository per node max_restore_bytes_per_sec. Default is 40m before 710, and default unlimited from 710 onwards</p>
        :type MaxRestorePerSec: str
        :param _CreateTime: <p>Policy creation time</p>
        :type CreateTime: str
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        """
        self._IsAutoBackup = None
        self._BackupTime = None
        self._SnapshotName = None
        self._EsRepositoryType = None
        self._PaasEsRepository = None
        self._UserEsRepository = None
        self._CosBasePath = None
        self._StorageDuration = None
        self._AutoBackupInterval = None
        self._CosRetention = None
        self._RetainUntilDate = None
        self._RetentionGraceTime = None
        self._RemoteCos = None
        self._RemoteCosRegion = None
        self._StrategyName = None
        self._Indices = None
        self._MultiAz = None
        self._MaxSnapshotPerSec = None
        self._MaxRestorePerSec = None
        self._CreateTime = None
        self._InstanceId = None

    @property
    def IsAutoBackup(self):
        r"""<p>Whether to enable cos automatic backup</p>
        :rtype: bool
        """
        return self._IsAutoBackup

    @IsAutoBackup.setter
    def IsAutoBackup(self, IsAutoBackup):
        self._IsAutoBackup = IsAutoBackup

    @property
    def BackupTime(self):
        r"""<p>Automatic backup execution time (accurate to the hour), e.g. "22:00"</p>
        :rtype: str
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def SnapshotName(self):
        r"""<p>Backup snapshot prefix</p>
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def EsRepositoryType(self):
        r"""<p>0 (Tencent Cloud repository); 1 (customer repository)</p>
        :rtype: int
        """
        return self._EsRepositoryType

    @EsRepositoryType.setter
    def EsRepositoryType(self, EsRepositoryType):
        self._EsRepositoryType = EsRepositoryType

    @property
    def PaasEsRepository(self):
        r"""<p>Managed snapshot repository name.</p>
        :rtype: str
        """
        return self._PaasEsRepository

    @PaasEsRepository.setter
    def PaasEsRepository(self, PaasEsRepository):
        self._PaasEsRepository = PaasEsRepository

    @property
    def UserEsRepository(self):
        r"""<p>Customer snapshot repository name</p>
        :rtype: str
        """
        return self._UserEsRepository

    @UserEsRepository.setter
    def UserEsRepository(self, UserEsRepository):
        self._UserEsRepository = UserEsRepository

    @property
    def CosBasePath(self):
        r"""<p>cos storage folder directory</p>
        :rtype: str
        """
        return self._CosBasePath

    @CosBasePath.setter
    def CosBasePath(self, CosBasePath):
        self._CosBasePath = CosBasePath

    @property
    def StorageDuration(self):
        r"""<p>Snapshot storage cycle in days</p>
        :rtype: int
        """
        return self._StorageDuration

    @StorageDuration.setter
    def StorageDuration(self, StorageDuration):
        self._StorageDuration = StorageDuration

    @property
    def AutoBackupInterval(self):
        r"""<p>Auto backup frequency in hours.</p>
        :rtype: int
        """
        return self._AutoBackupInterval

    @AutoBackupInterval.setter
    def AutoBackupInterval(self, AutoBackupInterval):
        self._AutoBackupInterval = AutoBackupInterval

    @property
    def CosRetention(self):
        r"""<p>Backup lock. Valid values: 0 (not locked) and 1 (locked).</p>
        :rtype: int
        """
        return self._CosRetention

    @CosRetention.setter
    def CosRetention(self, CosRetention):
        self._CosRetention = CosRetention

    @property
    def RetainUntilDate(self):
        r"""<p>Lock expiration date, such as 2022-12-10T08:34:48.000Z.</p>
        :rtype: str
        """
        return self._RetainUntilDate

    @RetainUntilDate.setter
    def RetainUntilDate(self, RetainUntilDate):
        self._RetainUntilDate = RetainUntilDate

    @property
    def RetentionGraceTime(self):
        r"""<p>Lock grace period</p>
        :rtype: int
        """
        return self._RetentionGraceTime

    @RetentionGraceTime.setter
    def RetentionGraceTime(self, RetentionGraceTime):
        self._RetentionGraceTime = RetentionGraceTime

    @property
    def RemoteCos(self):
        r"""<p>Cross-region backup. Valid values: 0 (disabled) and 1 (enabled).</p>
        :rtype: int
        """
        return self._RemoteCos

    @RemoteCos.setter
    def RemoteCos(self, RemoteCos):
        self._RemoteCos = RemoteCos

    @property
    def RemoteCosRegion(self):
        r"""<p>Region name for cross-regional backup, such as ap-guangzhou.</p>
        :rtype: str
        """
        return self._RemoteCosRegion

    @RemoteCosRegion.setter
    def RemoteCosRegion(self, RemoteCosRegion):
        self._RemoteCosRegion = RemoteCosRegion

    @property
    def StrategyName(self):
        r"""<p>Policy name.</p>
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def Indices(self):
        r"""<p>Backup index list. If left empty, it means to back up all indexes.</p>
        :rtype: str
        """
        return self._Indices

    @Indices.setter
    def Indices(self, Indices):
        self._Indices = Indices

    @property
    def MultiAz(self):
        r"""<p>cos multi-AZ backup. 0: single AZ; 1: multi-AZ</p>
        :rtype: int
        """
        return self._MultiAz

    @MultiAz.setter
    def MultiAz(self, MultiAz):
        self._MultiAz = MultiAz

    @property
    def MaxSnapshotPerSec(self):
        r"""<p>Maximum speed of write to the repository per node max_snapshot_bytes_per_sec, default 40m</p>
        :rtype: str
        """
        return self._MaxSnapshotPerSec

    @MaxSnapshotPerSec.setter
    def MaxSnapshotPerSec(self, MaxSnapshotPerSec):
        self._MaxSnapshotPerSec = MaxSnapshotPerSec

    @property
    def MaxRestorePerSec(self):
        r"""<p>Maximum speed of reading the repository per node max_restore_bytes_per_sec. Default is 40m before 710, and default unlimited from 710 onwards</p>
        :rtype: str
        """
        return self._MaxRestorePerSec

    @MaxRestorePerSec.setter
    def MaxRestorePerSec(self, MaxRestorePerSec):
        self._MaxRestorePerSec = MaxRestorePerSec

    @property
    def CreateTime(self):
        r"""<p>Policy creation time</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._IsAutoBackup = params.get("IsAutoBackup")
        self._BackupTime = params.get("BackupTime")
        self._SnapshotName = params.get("SnapshotName")
        self._EsRepositoryType = params.get("EsRepositoryType")
        self._PaasEsRepository = params.get("PaasEsRepository")
        self._UserEsRepository = params.get("UserEsRepository")
        self._CosBasePath = params.get("CosBasePath")
        self._StorageDuration = params.get("StorageDuration")
        self._AutoBackupInterval = params.get("AutoBackupInterval")
        self._CosRetention = params.get("CosRetention")
        self._RetainUntilDate = params.get("RetainUntilDate")
        self._RetentionGraceTime = params.get("RetentionGraceTime")
        self._RemoteCos = params.get("RemoteCos")
        self._RemoteCosRegion = params.get("RemoteCosRegion")
        self._StrategyName = params.get("StrategyName")
        self._Indices = params.get("Indices")
        self._MultiAz = params.get("MultiAz")
        self._MaxSnapshotPerSec = params.get("MaxSnapshotPerSec")
        self._MaxRestorePerSec = params.get("MaxRestorePerSec")
        self._CreateTime = params.get("CreateTime")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoBackUpStrategyRequest(AbstractModel):
    r"""CreateAutoBackUpStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance name.
        :type InstanceId: str
        :param _CosBackup: Policy information.
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        self._InstanceId = None
        self._CosBackup = None

    @property
    def InstanceId(self):
        r"""Instance name.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CosBackup(self):
        r"""Policy information.
        :rtype: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("CosBackup") is not None:
            self._CosBackup = CosBackup()
            self._CosBackup._deserialize(params.get("CosBackup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoBackUpStrategyResponse(AbstractModel):
    r"""CreateAutoBackUpStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Valid values: true (success) and false (failure).
        :type Status: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Valid values: true (success) and false (failure).
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateIndexRequest(AbstractModel):
    r"""CreateIndex request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES cluster ID
        :type InstanceId: str
        :param _IndexType: Index type of the created index. auto: autonomous index; normal: general index
        :type IndexType: str
        :param _IndexName: Index name of the created index
        :type IndexName: str
        :param _IndexMetaJson: [Required] JSON-formatted index metadata created, such as mappings and settings
        :type IndexMetaJson: str
        :param _Username: Cluster access username.
        :type Username: str
        :param _Password: Cluster access password
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
        r"""Index type of the created index. auto: autonomous index; normal: general index
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""Index name of the created index
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexMetaJson(self):
        r"""[Required] JSON-formatted index metadata created, such as mappings and settings
        :rtype: str
        """
        return self._IndexMetaJson

    @IndexMetaJson.setter
    def IndexMetaJson(self, IndexMetaJson):
        self._IndexMetaJson = IndexMetaJson

    @property
    def Username(self):
        r"""Cluster access username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""Cluster access password
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
        :param _Zone: <p>AZ.</p>
        :type Zone: str
        :param _EsVersion: <p>Instance version (supported: "5.6.4", "6.4.3", "6.8.2", "7.5.1", "7.10.1")</p>
        :type EsVersion: str
        :param _VpcId: <p>VPC ID</p>
        :type VpcId: str
        :param _SubnetId: <p>Subnet ID.</p>
        :type SubnetId: str
        :param _Password: <p>Access password (8-16 characters, including at least two of the following: [a-z,A-Z], [0-9], and special characters in [-!@#$%&amp;^*+=_:;,.?])</p>
        :type Password: str
        :param _InstanceName: <p>Instance name (1-50 English letters, Chinese characters, digits, hyphens -, or underscores _)</p>
        :type InstanceName: str
        :param _NodeNum: <p>Abandoned. Please use NodeInfoList<br>Node quantity (2-50)</p>
        :type NodeNum: int
        :param _ChargeType: <p>Billing type<li>PREPAID: prepaid, i.e., monthly subscription</li><li>POSTPAID_BY_HOUR: pay-as-you-go by hour</li>Default value: POSTPAID_BY_HOUR</p>
        :type ChargeType: str
        :param _ChargePeriod: <p>Annual and monthly subscription duration (unit determined by the TimeUnit parameter)</p>
        :type ChargePeriod: int
        :param _RenewFlag: <p>Auto-renewal flag<li>RENEW_FLAG_AUTO: auto renewal</li><li>RENEW_FLAG_MANUAL: no auto-renewal, user renews manually</li>This needs to be set when ChargeType is PREPAID. If this parameter is not passed, no automatic renewal by default for general users, and auto renewal for SVIP users</p>
        :type RenewFlag: str
        :param _NodeType: <p>Abandoned. Please use NodeInfoList<br>Node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :type NodeType: str
        :param _DiskType: <p>Abandoned. Please use NodeInfoList<br>Node disk type<li>CLOUD_SSD: ssd cloud disk</li><li>CLOUD_PREMIUM: high-performance cloud block storage</li><li>CLOUD_HSSD: enhanced SSD cloud disk</li><li>CLOUD_BSSD: universal type SSD cloud disk</li>Default value: CLOUD_SSD</p>
        :type DiskType: str
        :param _DiskSize: <p>Abandoned. Please use NodeInfoList<br>Node disk capacity (unit: GB)</p>
        :type DiskSize: int
        :param _TimeUnit: <p>Billing duration unit (needs to be set when ChargeType is PREPAID. Default value: "m", which means month. Currently only support "m")</p>
        :type TimeUnit: str
        :param _AutoVoucher: <p>Indicates whether to use vouchers automatically<li>0: Do not use automatically.</li><li>1: Use automatically.</li>Default value: 0.</p>
        :type AutoVoucher: int
        :param _VoucherIds: <p>Voucher ID list. Only one voucher can be specified.</p>
        :type VoucherIds: list of str
        :param _EnableDedicatedMaster: <p>Abandoned. Please use NodeInfoList<br>Whether to create a dedicated master node<li>true: enable a dedicated master node</li><li>false: disable a dedicated master node</li>Default value: false</p>
        :type EnableDedicatedMaster: bool
        :param _MasterNodeNum: <p>Abandoned. Please use NodeInfoList<br>Number of dedicated primary nodes (supports only 3 or 5. Required if EnableDedicatedMaster is true)</p>
        :type MasterNodeNum: int
        :param _MasterNodeType: <p>Abandoned. Please use NodeInfoList<br>Dedicated primary node type (required if EnableDedicatedMaster is true)<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :type MasterNodeType: str
        :param _MasterNodeDiskSize: <p>Abandoned. Please use NodeInfoList<br>Dedicated primary node disk size (in GB, optional; if transmitted, it must be 50. Customization is not supported temporarily)</p>
        :type MasterNodeDiskSize: int
        :param _ClusterNameInConf: <p>ClusterName in the cluster configuration file (system default configuration is the instance ID, customization is not supported temporarily)</p>
        :type ClusterNameInConf: str
        :param _DeployMode: <p>Cluster deployment method<li>0: single-AZ deployment</li><li>1: multi-AZ deployment, Beijing, Shanghai, Shanghai Finance, Guangzhou, Nanjing, Hong Kong, Singapore, Frankfurt (allowlist control)</li>Default value: 0</p>
        :type DeployMode: int
        :param _MultiZoneInfo: <p>Detailed information of availability zones in multi-AZ deployment (required when DeployMode is 1)</p>
        :type MultiZoneInfo: list of ZoneDetail
        :param _LicenseType: <p>License type<li>oss: open source edition</li><li>basic: basic version</li><li>platinum: platinum version</li>Default value: platinum</p>
        :type LicenseType: str
        :param _NodeInfoList: <p>Node information list, for description of the specification information of various types of nodes in the cluster, such as node type, number of nodes, node specification, disk type, and disk size</p>
        :type NodeInfoList: list of NodeInfo
        :param _TagList: <p>Node tag information list</p>
        :type TagList: list of TagInfo
        :param _BasicSecurityType: <p>Whether xpack security authentication is enabled for basic version 6.8 (and above versions)<li>1: not enabled</li><li>2: enabled</li></p>
        :type BasicSecurityType: int
        :param _SceneType: <p>Scenario template type 0: disabled 1: common 2: log 3: search</p>
        :type SceneType: int
        :param _WebNodeTypeInfo: <p>Visualize node configuration</p>
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param _Protocol: <p>Create an https cluster. http is selected by default.</p>
        :type Protocol: str
        :param _OperationDuration: <p>Maintenance time slot</p>
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param _EnableHybridStorage: <p>Whether storage-compute separation is enabled</p>
        :type EnableHybridStorage: bool
        :param _DiskEnhance: <p>Additional hard disk performance</p>
        :type DiskEnhance: int
        :param _EnableDiagnose: <p>Whether intelligent check is enabled</p>
        :type EnableDiagnose: bool
        :param _EnableCosBackup: <p>Whether to enable automatic backup</p>
        :type EnableCosBackup: bool
        :param _CdcId: <p>cdcId, pass it when using a CDC subnet</p>
        :type CdcId: str
        :param _DisasterRecoverGroupAffinity: <p>Placement group affinity. Value range: [0,10]. 0 indicates disabled.</p>
        :type DisasterRecoverGroupAffinity: int
        :param _SubProductCode: <p>Enumeration values of sub-product ID: open source edition: "sp_es_io2", basic version: "sp_es_basic", platinum version: "sp_es_platinum", enterprise edition: "sp_es_enterprise", CDC platinum version: "sp_es_CDC_platinum", Log Enhancement Edition: "sp_es_enlogging", tsearch: "sp_tsearch_io2", logstash: "sp_es_logstash". It can be empty. When it is empty, the backend maps this field based on LicenseType.</p>
        :type SubProductCode: str
        :param _ReadWriteMode: <p>Read-write separation mode: 0: not enabled; 1: local read/write separation; 2: remote read/write separation.</p>
        :type ReadWriteMode: int
        :param _EnableScheduleRecoverGroup: <p>Whether the placement group has asynchronous tasks enabled</p>
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: <p>Maintenance time slot for enabling async tasks in a placement group</p>
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        :param _AutoScaleDiskInfoList: <p>Auto capacity expansion parameter list</p>
        :type AutoScaleDiskInfoList: list of AutoScaleDiskInfo
        :param _EnableKibanaPublicAccess: <p>Whether to enable public network access to kibana. Enabled by default if not passed</p>
        :type EnableKibanaPublicAccess: str
        :param _AlarmPolicyIds: <p>Existing cloud monitoring and alarm policy ID</p>
        :type AlarmPolicyIds: list of str
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
        self._EnableCosBackup = None
        self._CdcId = None
        self._DisasterRecoverGroupAffinity = None
        self._SubProductCode = None
        self._ReadWriteMode = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None
        self._AutoScaleDiskInfoList = None
        self._EnableKibanaPublicAccess = None
        self._AlarmPolicyIds = None

    @property
    def Zone(self):
        r"""<p>AZ.</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def EsVersion(self):
        r"""<p>Instance version (supported: "5.6.4", "6.4.3", "6.8.2", "7.5.1", "7.10.1")</p>
        :rtype: str
        """
        return self._EsVersion

    @EsVersion.setter
    def EsVersion(self, EsVersion):
        self._EsVersion = EsVersion

    @property
    def VpcId(self):
        r"""<p>VPC ID</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>Subnet ID.</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Password(self):
        r"""<p>Access password (8-16 characters, including at least two of the following: [a-z,A-Z], [0-9], and special characters in [-!@#$%&amp;^*+=_:;,.?])</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InstanceName(self):
        r"""<p>Instance name (1-50 English letters, Chinese characters, digits, hyphens -, or underscores _)</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NodeNum(self):
        r"""<p>Abandoned. Please use NodeInfoList<br>Node quantity (2-50)</p>
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def ChargeType(self):
        r"""<p>Billing type<li>PREPAID: prepaid, i.e., monthly subscription</li><li>POSTPAID_BY_HOUR: pay-as-you-go by hour</li>Default value: POSTPAID_BY_HOUR</p>
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePeriod(self):
        r"""<p>Annual and monthly subscription duration (unit determined by the TimeUnit parameter)</p>
        :rtype: int
        """
        return self._ChargePeriod

    @ChargePeriod.setter
    def ChargePeriod(self, ChargePeriod):
        self._ChargePeriod = ChargePeriod

    @property
    def RenewFlag(self):
        r"""<p>Auto-renewal flag<li>RENEW_FLAG_AUTO: auto renewal</li><li>RENEW_FLAG_MANUAL: no auto-renewal, user renews manually</li>This needs to be set when ChargeType is PREPAID. If this parameter is not passed, no automatic renewal by default for general users, and auto renewal for SVIP users</p>
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def NodeType(self):
        r"""<p>Abandoned. Please use NodeInfoList<br>Node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def DiskType(self):
        r"""<p>Abandoned. Please use NodeInfoList<br>Node disk type<li>CLOUD_SSD: ssd cloud disk</li><li>CLOUD_PREMIUM: high-performance cloud block storage</li><li>CLOUD_HSSD: enhanced SSD cloud disk</li><li>CLOUD_BSSD: universal type SSD cloud disk</li>Default value: CLOUD_SSD</p>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""<p>Abandoned. Please use NodeInfoList<br>Node disk capacity (unit: GB)</p>
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def TimeUnit(self):
        r"""<p>Billing duration unit (needs to be set when ChargeType is PREPAID. Default value: "m", which means month. Currently only support "m")</p>
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def AutoVoucher(self):
        r"""<p>Indicates whether to use vouchers automatically<li>0: Do not use automatically.</li><li>1: Use automatically.</li>Default value: 0.</p>
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""<p>Voucher ID list. Only one voucher can be specified.</p>
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def EnableDedicatedMaster(self):
        r"""<p>Abandoned. Please use NodeInfoList<br>Whether to create a dedicated master node<li>true: enable a dedicated master node</li><li>false: disable a dedicated master node</li>Default value: false</p>
        :rtype: bool
        """
        return self._EnableDedicatedMaster

    @EnableDedicatedMaster.setter
    def EnableDedicatedMaster(self, EnableDedicatedMaster):
        self._EnableDedicatedMaster = EnableDedicatedMaster

    @property
    def MasterNodeNum(self):
        r"""<p>Abandoned. Please use NodeInfoList<br>Number of dedicated primary nodes (supports only 3 or 5. Required if EnableDedicatedMaster is true)</p>
        :rtype: int
        """
        return self._MasterNodeNum

    @MasterNodeNum.setter
    def MasterNodeNum(self, MasterNodeNum):
        self._MasterNodeNum = MasterNodeNum

    @property
    def MasterNodeType(self):
        r"""<p>Abandoned. Please use NodeInfoList<br>Dedicated primary node type (required if EnableDedicatedMaster is true)<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :rtype: str
        """
        return self._MasterNodeType

    @MasterNodeType.setter
    def MasterNodeType(self, MasterNodeType):
        self._MasterNodeType = MasterNodeType

    @property
    def MasterNodeDiskSize(self):
        r"""<p>Abandoned. Please use NodeInfoList<br>Dedicated primary node disk size (in GB, optional; if transmitted, it must be 50. Customization is not supported temporarily)</p>
        :rtype: int
        """
        return self._MasterNodeDiskSize

    @MasterNodeDiskSize.setter
    def MasterNodeDiskSize(self, MasterNodeDiskSize):
        self._MasterNodeDiskSize = MasterNodeDiskSize

    @property
    def ClusterNameInConf(self):
        r"""<p>ClusterName in the cluster configuration file (system default configuration is the instance ID, customization is not supported temporarily)</p>
        :rtype: str
        """
        return self._ClusterNameInConf

    @ClusterNameInConf.setter
    def ClusterNameInConf(self, ClusterNameInConf):
        self._ClusterNameInConf = ClusterNameInConf

    @property
    def DeployMode(self):
        r"""<p>Cluster deployment method<li>0: single-AZ deployment</li><li>1: multi-AZ deployment, Beijing, Shanghai, Shanghai Finance, Guangzhou, Nanjing, Hong Kong, Singapore, Frankfurt (allowlist control)</li>Default value: 0</p>
        :rtype: int
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def MultiZoneInfo(self):
        r"""<p>Detailed information of availability zones in multi-AZ deployment (required when DeployMode is 1)</p>
        :rtype: list of ZoneDetail
        """
        return self._MultiZoneInfo

    @MultiZoneInfo.setter
    def MultiZoneInfo(self, MultiZoneInfo):
        self._MultiZoneInfo = MultiZoneInfo

    @property
    def LicenseType(self):
        r"""<p>License type<li>oss: open source edition</li><li>basic: basic version</li><li>platinum: platinum version</li>Default value: platinum</p>
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def NodeInfoList(self):
        r"""<p>Node information list, for description of the specification information of various types of nodes in the cluster, such as node type, number of nodes, node specification, disk type, and disk size</p>
        :rtype: list of NodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList

    @property
    def TagList(self):
        r"""<p>Node tag information list</p>
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def BasicSecurityType(self):
        r"""<p>Whether xpack security authentication is enabled for basic version 6.8 (and above versions)<li>1: not enabled</li><li>2: enabled</li></p>
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def SceneType(self):
        r"""<p>Scenario template type 0: disabled 1: common 2: log 3: search</p>
        :rtype: int
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def WebNodeTypeInfo(self):
        r"""<p>Visualize node configuration</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        """
        return self._WebNodeTypeInfo

    @WebNodeTypeInfo.setter
    def WebNodeTypeInfo(self, WebNodeTypeInfo):
        self._WebNodeTypeInfo = WebNodeTypeInfo

    @property
    def Protocol(self):
        r"""<p>Create an https cluster. http is selected by default.</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OperationDuration(self):
        r"""<p>Maintenance time slot</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def EnableHybridStorage(self):
        r"""<p>Whether storage-compute separation is enabled</p>
        :rtype: bool
        """
        return self._EnableHybridStorage

    @EnableHybridStorage.setter
    def EnableHybridStorage(self, EnableHybridStorage):
        self._EnableHybridStorage = EnableHybridStorage

    @property
    def DiskEnhance(self):
        r"""<p>Additional hard disk performance</p>
        :rtype: int
        """
        return self._DiskEnhance

    @DiskEnhance.setter
    def DiskEnhance(self, DiskEnhance):
        self._DiskEnhance = DiskEnhance

    @property
    def EnableDiagnose(self):
        r"""<p>Whether intelligent check is enabled</p>
        :rtype: bool
        """
        return self._EnableDiagnose

    @EnableDiagnose.setter
    def EnableDiagnose(self, EnableDiagnose):
        self._EnableDiagnose = EnableDiagnose

    @property
    def EnableCosBackup(self):
        r"""<p>Whether to enable automatic backup</p>
        :rtype: bool
        """
        return self._EnableCosBackup

    @EnableCosBackup.setter
    def EnableCosBackup(self, EnableCosBackup):
        self._EnableCosBackup = EnableCosBackup

    @property
    def CdcId(self):
        r"""<p>cdcId, pass it when using a CDC subnet</p>
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def DisasterRecoverGroupAffinity(self):
        r"""<p>Placement group affinity. Value range: [0,10]. 0 indicates disabled.</p>
        :rtype: int
        """
        return self._DisasterRecoverGroupAffinity

    @DisasterRecoverGroupAffinity.setter
    def DisasterRecoverGroupAffinity(self, DisasterRecoverGroupAffinity):
        self._DisasterRecoverGroupAffinity = DisasterRecoverGroupAffinity

    @property
    def SubProductCode(self):
        r"""<p>Enumeration values of sub-product ID: open source edition: "sp_es_io2", basic version: "sp_es_basic", platinum version: "sp_es_platinum", enterprise edition: "sp_es_enterprise", CDC platinum version: "sp_es_CDC_platinum", Log Enhancement Edition: "sp_es_enlogging", tsearch: "sp_tsearch_io2", logstash: "sp_es_logstash". It can be empty. When it is empty, the backend maps this field based on LicenseType.</p>
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def ReadWriteMode(self):
        r"""<p>Read-write separation mode: 0: not enabled; 1: local read/write separation; 2: remote read/write separation.</p>
        :rtype: int
        """
        return self._ReadWriteMode

    @ReadWriteMode.setter
    def ReadWriteMode(self, ReadWriteMode):
        self._ReadWriteMode = ReadWriteMode

    @property
    def EnableScheduleRecoverGroup(self):
        r"""<p>Whether the placement group has asynchronous tasks enabled</p>
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        r"""<p>Maintenance time slot for enabling async tasks in a placement group</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration

    @property
    def AutoScaleDiskInfoList(self):
        r"""<p>Auto capacity expansion parameter list</p>
        :rtype: list of AutoScaleDiskInfo
        """
        return self._AutoScaleDiskInfoList

    @AutoScaleDiskInfoList.setter
    def AutoScaleDiskInfoList(self, AutoScaleDiskInfoList):
        self._AutoScaleDiskInfoList = AutoScaleDiskInfoList

    @property
    def EnableKibanaPublicAccess(self):
        r"""<p>Whether to enable public network access to kibana. Enabled by default if not passed</p>
        :rtype: str
        """
        return self._EnableKibanaPublicAccess

    @EnableKibanaPublicAccess.setter
    def EnableKibanaPublicAccess(self, EnableKibanaPublicAccess):
        self._EnableKibanaPublicAccess = EnableKibanaPublicAccess

    @property
    def AlarmPolicyIds(self):
        r"""<p>Existing cloud monitoring and alarm policy ID</p>
        :rtype: list of str
        """
        return self._AlarmPolicyIds

    @AlarmPolicyIds.setter
    def AlarmPolicyIds(self, AlarmPolicyIds):
        self._AlarmPolicyIds = AlarmPolicyIds


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
        self._EnableCosBackup = params.get("EnableCosBackup")
        self._CdcId = params.get("CdcId")
        self._DisasterRecoverGroupAffinity = params.get("DisasterRecoverGroupAffinity")
        self._SubProductCode = params.get("SubProductCode")
        self._ReadWriteMode = params.get("ReadWriteMode")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
        if params.get("AutoScaleDiskInfoList") is not None:
            self._AutoScaleDiskInfoList = []
            for item in params.get("AutoScaleDiskInfoList"):
                obj = AutoScaleDiskInfo()
                obj._deserialize(item)
                self._AutoScaleDiskInfoList.append(obj)
        self._EnableKibanaPublicAccess = params.get("EnableKibanaPublicAccess")
        self._AlarmPolicyIds = params.get("AlarmPolicyIds")
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
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _DealName: <p>Order ID.</p>
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._DealName = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealName(self):
        r"""<p>Order ID.</p>
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._InstanceId = params.get("InstanceId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class DeleteAutoBackUpStrategyRequest(AbstractModel):
    r"""DeleteAutoBackUpStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance name.
        :type InstanceId: str
        :param _StrategyName: Policy name.
        :type StrategyName: list of str
        """
        self._InstanceId = None
        self._StrategyName = None

    @property
    def InstanceId(self):
        r"""Instance name.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StrategyName(self):
        r"""Policy name.
        :rtype: list of str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StrategyName = params.get("StrategyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoBackUpStrategyResponse(AbstractModel):
    r"""DeleteAutoBackUpStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Valid values: true (success) and false (failure).
        :type Status: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Valid values: true (success) and false (failure).
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteIndexRequest(AbstractModel):
    r"""DeleteIndex request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>ES cluster ID</p>
        :type InstanceId: str
        :param _IndexType: <p>Deleted index type. auto: autonomous index; normal: general index</p>
        :type IndexType: str
        :param _IndexName: <p>Name of the deleted index</p>
        :type IndexName: str
        :param _Username: <p>Cluster access username.</p>
        :type Username: str
        :param _Password: <p>Cluster access password</p>
        :type Password: str
        :param _BackingIndexName: <p>Backing index name</p>
        :type BackingIndexName: str
        :param _IndexPhrase: <p>Index life cycle</p>
        :type IndexPhrase: str
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._Username = None
        self._Password = None
        self._BackingIndexName = None
        self._IndexPhrase = None

    @property
    def InstanceId(self):
        r"""<p>ES cluster ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        r"""<p>Deleted index type. auto: autonomous index; normal: general index</p>
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""<p>Name of the deleted index</p>
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Username(self):
        r"""<p>Cluster access username.</p>
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""<p>Cluster access password</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def BackingIndexName(self):
        r"""<p>Backing index name</p>
        :rtype: str
        """
        return self._BackingIndexName

    @BackingIndexName.setter
    def BackingIndexName(self, BackingIndexName):
        self._BackingIndexName = BackingIndexName

    @property
    def IndexPhrase(self):
        r"""<p>Index life cycle</p>
        :rtype: str
        """
        return self._IndexPhrase

    @IndexPhrase.setter
    def IndexPhrase(self, IndexPhrase):
        self._IndexPhrase = IndexPhrase


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._BackingIndexName = params.get("BackingIndexName")
        self._IndexPhrase = params.get("IndexPhrase")
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
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _LockEnabled: <p>Recycle bin lock settings. If true, it cannot be manually terminated and will be automatically destroyed after the preset time.</p><p>Default value: false</p>
        :type LockEnabled: bool
        :param _LockDuration: <p>Lock time after being put into the recycle bin</p><p>Value range: [1, 7]</p><p>Unit: day</p><p>Default value: 1</p>
        :type LockDuration: int
        """
        self._InstanceId = None
        self._LockEnabled = None
        self._LockDuration = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LockEnabled(self):
        r"""<p>Recycle bin lock settings. If true, it cannot be manually terminated and will be automatically destroyed after the preset time.</p><p>Default value: false</p>
        :rtype: bool
        """
        return self._LockEnabled

    @LockEnabled.setter
    def LockEnabled(self, LockEnabled):
        self._LockEnabled = LockEnabled

    @property
    def LockDuration(self):
        r"""<p>Lock time after being put into the recycle bin</p><p>Value range: [1, 7]</p><p>Unit: day</p><p>Default value: 1</p>
        :rtype: int
        """
        return self._LockDuration

    @LockDuration.setter
    def LockDuration(self, LockDuration):
        self._LockDuration = LockDuration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LockEnabled = params.get("LockEnabled")
        self._LockDuration = params.get("LockDuration")
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


class DescribeAutoBackUpStrategyRequest(AbstractModel):
    r"""DescribeAutoBackUpStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance name.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance name.
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
        


class DescribeAutoBackUpStrategyResponse(AbstractModel):
    r"""DescribeAutoBackUpStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _CosBackupList: Policy information.
        :type CosBackupList: list of CosBackup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CosBackupList = None
        self._RequestId = None

    @property
    def CosBackupList(self):
        r"""Policy information.
        :rtype: list of CosBackup
        """
        return self._CosBackupList

    @CosBackupList.setter
    def CosBackupList(self, CosBackupList):
        self._CosBackupList = CosBackupList

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
        if params.get("CosBackupList") is not None:
            self._CosBackupList = []
            for item in params.get("CosBackupList"):
                obj = CosBackup()
                obj._deserialize(item)
                self._CosBackupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIndexListRequest(AbstractModel):
    r"""DescribeIndexList request structure.

    """

    def __init__(self):
        r"""
        :param _IndexType: Index type. auto: autonomous index; normal: general index
        :type IndexType: str
        :param _InstanceId: ES cluster ID
        :type InstanceId: str
        :param _IndexName: Index name. If this parameter is left empty, all indexes are obtained.
        :type IndexName: str
        :param _Username: Cluster access username.
        :type Username: str
        :param _Password: Cluster access password
        :type Password: str
        :param _Offset: Paging start position
        :type Offset: int
        :param _Limit: Number of items displayed per page
        :type Limit: int
        :param _OrderBy: Sorting fields, which support the following index names: IndexName, IndexStorage, and IndexCreateTime.
        :type OrderBy: str
        :param _IndexStatusList: Filter by index status
        :type IndexStatusList: list of str
        :param _Order: Sort order. Supports asc and desc. Defaults to desc. Data format: "asc", "desc"
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
        r"""Index type. auto: autonomous index; normal: general index
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
        r"""Index name. If this parameter is left empty, all indexes are obtained.
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Username(self):
        r"""Cluster access username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""Cluster access password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Offset(self):
        r"""Paging start position
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of items displayed per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        r"""Sorting fields, which support the following index names: IndexName, IndexStorage, and IndexCreateTime.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def IndexStatusList(self):
        r"""Filter by index status
        :rtype: list of str
        """
        return self._IndexStatusList

    @IndexStatusList.setter
    def IndexStatusList(self, IndexStatusList):
        self._IndexStatusList = IndexStatusList

    @property
    def Order(self):
        r"""Sort order. Supports asc and desc. Defaults to desc. Data format: "asc", "desc"
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
        :type IndexMetaFields: list of IndexMetaField
        :param _TotalCount: Total query count
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IndexMetaFields = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def IndexMetaFields(self):
        r"""Index metadata field
        :rtype: list of IndexMetaField
        """
        return self._IndexMetaFields

    @IndexMetaFields.setter
    def IndexMetaFields(self, IndexMetaFields):
        self._IndexMetaFields = IndexMetaFields

    @property
    def TotalCount(self):
        r"""Total query count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        :param _IndexType: Index type. auto: autonomous index; normal: general index
        :type IndexType: str
        :param _IndexName: Index name. If this parameter is left empty, all indexes are obtained.
        :type IndexName: str
        :param _Username: Cluster access username.
        :type Username: str
        :param _Password: Cluster access password
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
        r"""Index type. auto: autonomous index; normal: general index
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""Index name. If this parameter is left empty, all indexes are obtained.
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Username(self):
        r"""Cluster access username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""Cluster access password
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
        :type IndexMetaField: :class:`tencentcloud.es.v20180416.models.IndexMetaField`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IndexMetaField = None
        self._RequestId = None

    @property
    def IndexMetaField(self):
        r"""Index metadata field
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexMetaField`
        """
        return self._IndexMetaField

    @IndexMetaField.setter
    def IndexMetaField(self, IndexMetaField):
        self._IndexMetaField = IndexMetaField

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
        if params.get("IndexMetaField") is not None:
            self._IndexMetaField = IndexMetaField()
            self._IndexMetaField._deserialize(params.get("IndexMetaField"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    r"""DescribeInstanceLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID.
        :type InstanceId: str
        :param _LogType: Log type. Default value: 1.
<li>1, master log</li>
<li>2. Search slow logs</li>
<li>3. Index slow log</li>
<li>4. GC log</li>
        :type LogType: int
        :param _SearchKey: Search term. LUCENE grammar is supported, for example, level:WARN, ip:1.1.1.1, message:test-index
        :type SearchKey: str
        :param _StartTime: Log start time in the format of YYYY-MM-DD HH:MM:SS, for example, 2019-01-22 20:15:53
        :type StartTime: str
        :param _EndTime: Log end time in the format of YYYY-MM-DD HH:MM:SS, for example, 2019-01-22 20:15:53
        :type EndTime: str
        :param _Offset: Pagination starting value. Default value: 0.
        :type Offset: int
        :param _Limit: Pagination size. Default value: 100. Maximum value: 100.
        :type Limit: int
        :param _OrderByType: Time sort method. Default value: 0.
<li>0: descending order</li>
<li>1, ascending</li>
        :type OrderByType: int
        :param _LogLevels: Log level
        :type LogLevels: list of str
        :param _NodeIds: Node ID.
        :type NodeIds: list of str
        :param _IndexName: Slow log index name
        :type IndexName: str
        :param _ShardId: Slow log index shards
        :type ShardId: str
        :param _QueryCost: Slow log query time
        :type QueryCost: int
        """
        self._InstanceId = None
        self._LogType = None
        self._SearchKey = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._OrderByType = None
        self._LogLevels = None
        self._NodeIds = None
        self._IndexName = None
        self._ShardId = None
        self._QueryCost = None

    @property
    def InstanceId(self):
        r"""Cluster instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogType(self):
        r"""Log type. Default value: 1.
<li>1, master log</li>
<li>2. Search slow logs</li>
<li>3. Index slow log</li>
<li>4. GC log</li>
        :rtype: int
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def SearchKey(self):
        r"""Search term. LUCENE grammar is supported, for example, level:WARN, ip:1.1.1.1, message:test-index
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def StartTime(self):
        r"""Log start time in the format of YYYY-MM-DD HH:MM:SS, for example, 2019-01-22 20:15:53
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Log end time in the format of YYYY-MM-DD HH:MM:SS, for example, 2019-01-22 20:15:53
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""Pagination starting value. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination size. Default value: 100. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByType(self):
        r"""Time sort method. Default value: 0.
<li>0: descending order</li>
<li>1, ascending</li>
        :rtype: int
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def LogLevels(self):
        r"""Log level
        :rtype: list of str
        """
        return self._LogLevels

    @LogLevels.setter
    def LogLevels(self, LogLevels):
        self._LogLevels = LogLevels

    @property
    def NodeIds(self):
        r"""Node ID.
        :rtype: list of str
        """
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds

    @property
    def IndexName(self):
        r"""Slow log index name
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def ShardId(self):
        r"""Slow log index shards
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def QueryCost(self):
        r"""Slow log query time
        :rtype: int
        """
        return self._QueryCost

    @QueryCost.setter
    def QueryCost(self, QueryCost):
        self._QueryCost = QueryCost


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogType = params.get("LogType")
        self._SearchKey = params.get("SearchKey")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByType = params.get("OrderByType")
        self._LogLevels = params.get("LogLevels")
        self._NodeIds = params.get("NodeIds")
        self._IndexName = params.get("IndexName")
        self._ShardId = params.get("ShardId")
        self._QueryCost = params.get("QueryCost")
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
        :param _TotalCount: Number of returned log entries
        :type TotalCount: int
        :param _InstanceLogList: List of log details
        :type InstanceLogList: list of InstanceLog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceLogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of returned log entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceLogList(self):
        r"""List of log details
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
        :param _InstanceId: Cluster instance ID.
        :type InstanceId: str
        :param _StartTime: Start time, e.g., "2019-03-07 16:30:39"
        :type StartTime: str
        :param _EndTime: End time, e.g., "2019-03-30 20:18:03"
        :type EndTime: str
        :param _Offset: Paging Starting Value
        :type Offset: int
        :param _Limit: Pagination size.
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""Cluster instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Start time, e.g., "2019-03-07 16:30:39"
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time, e.g., "2019-03-30 20:18:03"
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""Paging Starting Value
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination size.
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
        :param _Operations: Operation record
        :type Operations: list of Operation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        r"""Operation record
        :rtype: list of Operation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

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
        :param _Zone: <p>AZ to which the cluster instance belongs. All AZs are selected by default if this parameter is not specified.</p>
        :type Zone: str
        :param _InstanceIds: <p>Cluster instance ID list</p>
        :type InstanceIds: list of str
        :param _InstanceNames: <p>Cluster instance name list.</p>
        :type InstanceNames: list of str
        :param _Offset: <p>Pagination starting value. Default value: 0</p>
        :type Offset: int
        :param _Limit: <p>Page size. Default value: 20</p>
        :type Limit: int
        :param _OrderByKey: <p>Sorting field<li>1: Instance ID</li><li>2: Instance name</li><li>3: Availability zone</li><li>4: Creation time</li>If orderByKey is not transmitted, sort by creation time in descending order</p>
        :type OrderByKey: int
        :param _OrderByType: <p>Sorting method<li>0: ascending</li><li>1: descending</li>If orderByKey is passed but orderByType is not, ascending by default</p>
        :type OrderByType: int
        :param _TagList: <p>Node tag information list</p>
        :type TagList: list of TagInfo
        :param _IpList: <p>Private network vip list</p>
        :type IpList: list of str
        :param _NodeIps: <p>IP list of cluster nodes</p>
        :type NodeIps: list of str
        :param _ZoneList: <p>Availability zone list</p>
        :type ZoneList: list of str
        :param _HealthStatus: <p>Health status filter list: 0 represents green, 1 represents yellow, 2 represents red, -1 represents unknown</p>
        :type HealthStatus: list of int
        :param _VpcIds: <p>Vpc list filter item</p>
        :type VpcIds: list of str
        :param _CdcId: <p>cdc cluster id</p>
        :type CdcId: str
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
        self._NodeIps = None
        self._ZoneList = None
        self._HealthStatus = None
        self._VpcIds = None
        self._CdcId = None

    @property
    def Zone(self):
        r"""<p>AZ to which the cluster instance belongs. All AZs are selected by default if this parameter is not specified.</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceIds(self):
        r"""<p>Cluster instance ID list</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        r"""<p>Cluster instance name list.</p>
        :rtype: list of str
        """
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def Offset(self):
        r"""<p>Pagination starting value. Default value: 0</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Page size. Default value: 20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByKey(self):
        r"""<p>Sorting field<li>1: Instance ID</li><li>2: Instance name</li><li>3: Availability zone</li><li>4: Creation time</li>If orderByKey is not transmitted, sort by creation time in descending order</p>
        :rtype: int
        """
        return self._OrderByKey

    @OrderByKey.setter
    def OrderByKey(self, OrderByKey):
        self._OrderByKey = OrderByKey

    @property
    def OrderByType(self):
        r"""<p>Sorting method<li>0: ascending</li><li>1: descending</li>If orderByKey is passed but orderByType is not, ascending by default</p>
        :rtype: int
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def TagList(self):
        r"""<p>Node tag information list</p>
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def IpList(self):
        r"""<p>Private network vip list</p>
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def NodeIps(self):
        r"""<p>IP list of cluster nodes</p>
        :rtype: list of str
        """
        return self._NodeIps

    @NodeIps.setter
    def NodeIps(self, NodeIps):
        self._NodeIps = NodeIps

    @property
    def ZoneList(self):
        r"""<p>Availability zone list</p>
        :rtype: list of str
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def HealthStatus(self):
        r"""<p>Health status filter list: 0 represents green, 1 represents yellow, 2 represents red, -1 represents unknown</p>
        :rtype: list of int
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def VpcIds(self):
        r"""<p>Vpc list filter item</p>
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def CdcId(self):
        r"""<p>cdc cluster id</p>
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


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
        self._NodeIps = params.get("NodeIps")
        self._ZoneList = params.get("ZoneList")
        self._HealthStatus = params.get("HealthStatus")
        self._VpcIds = params.get("VpcIds")
        self._CdcId = params.get("CdcId")
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
        :param _TotalCount: <p>Number of returned instances</p>
        :type TotalCount: int
        :param _InstanceList: <p>Instance detail list</p>
        :type InstanceList: list of InstanceInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>Number of returned instances</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        r"""<p>Instance detail list</p>
        :rtype: list of InstanceInfo
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

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
        :param _InstanceId: Cluster instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Cluster instance ID.
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
        :param _ClusterView: Cluster dimension view
        :type ClusterView: :class:`tencentcloud.es.v20180416.models.ClusterView`
        :param _NodesView: Node dimension view
        :type NodesView: list of NodeView
        :param _KibanasView: Kibana dimensional view
        :type KibanasView: list of KibanaView
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterView = None
        self._NodesView = None
        self._KibanasView = None
        self._RequestId = None

    @property
    def ClusterView(self):
        r"""Cluster dimension view
        :rtype: :class:`tencentcloud.es.v20180416.models.ClusterView`
        """
        return self._ClusterView

    @ClusterView.setter
    def ClusterView(self, ClusterView):
        self._ClusterView = ClusterView

    @property
    def NodesView(self):
        r"""Node dimension view
        :rtype: list of NodeView
        """
        return self._NodesView

    @NodesView.setter
    def NodesView(self, NodesView):
        self._NodesView = NodesView

    @property
    def KibanasView(self):
        r"""Kibana dimensional view
        :rtype: list of KibanaView
        """
        return self._KibanasView

    @KibanasView.setter
    def KibanasView(self, KibanasView):
        self._KibanasView = KibanasView

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
    r"""ik plug-in dictionary information

    """

    def __init__(self):
        r"""
        :param _Key: Dictionary key-value
        :type Key: str
        :param _Name: Dictionary name
        :type Name: str
        :param _Size: Dictionary size. Unit: B.
        :type Size: int
        """
        self._Key = None
        self._Name = None
        self._Size = None

    @property
    def Key(self):
        r"""Dictionary key-value
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
        r"""Dictionary size. Unit: B.
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
        


class EnableScheduleOperationDuration(AbstractModel):
    r"""Placement group async task maintenance time period

    """

    def __init__(self):
        r"""
        :param _Periods: Date when enabling an asynchronous task is supported
        :type Periods: list of str
        :param _TimeStart: Enable async start time
        :type TimeStart: str
        :param _TimeEnd: Supports enabling asynchronous termination time
        :type TimeEnd: str
        :param _TimeZone: Enable async time zone
        :type TimeZone: str
        """
        self._Periods = None
        self._TimeStart = None
        self._TimeEnd = None
        self._TimeZone = None

    @property
    def Periods(self):
        r"""Date when enabling an asynchronous task is supported
        :rtype: list of str
        """
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def TimeStart(self):
        r"""Enable async start time
        :rtype: str
        """
        return self._TimeStart

    @TimeStart.setter
    def TimeStart(self, TimeStart):
        self._TimeStart = TimeStart

    @property
    def TimeEnd(self):
        r"""Supports enabling asynchronous termination time
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def TimeZone(self):
        r"""Enable async time zone
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
        


class EsAcl(AbstractModel):
    r"""ES cluster configuration item

    """

    def __init__(self):
        r"""
        :param _BlackIpList: kibana access blocklist
        :type BlackIpList: list of str
        :param _WhiteIpList: kibana access allowlist
        :type WhiteIpList: list of str
        """
        self._BlackIpList = None
        self._WhiteIpList = None

    @property
    def BlackIpList(self):
        r"""kibana access blocklist
        :rtype: list of str
        """
        return self._BlackIpList

    @BlackIpList.setter
    def BlackIpList(self, BlackIpList):
        self._BlackIpList = BlackIpList

    @property
    def WhiteIpList(self):
        r"""kibana access allowlist
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
    r"""Configuration group information

    """

    def __init__(self):
        r"""
        :param _Type: Configuration group type, for example, ldap and ad
        :type Type: str
        :param _EsConfig: "{\"order\":0,\"url\":\"ldap://10.0.1.72:389\",\"bind_dn\":\"cn=admin,dc=tencent,dc=com\",\"user_search.base_dn\":\"dc=tencent,dc=com\",\"user_search.filter\":\"(cn={0})\",\"group_search.base_dn\":\"dc=tencent,dc=com\"}"
        :type EsConfig: str
        """
        self._Type = None
        self._EsConfig = None

    @property
    def Type(self):
        r"""Configuration group type, for example, ldap and ad
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
    r"""ES library information

    """

    def __init__(self):
        r"""
        :param _MainDict: List of enabled word dictionaries
        :type MainDict: list of DictInfo
        :param _Stopwords: List of stopword dictionaries
        :type Stopwords: list of DictInfo
        :param _QQDict: List of QQ word segmentation dictionaries
        :type QQDict: list of DictInfo
        :param _Synonym: List of synonym dictionaries
        :type Synonym: list of DictInfo
        :param _UpdateType: Update the dictionary type
        :type UpdateType: str
        :param _AnsjMain: List of ansj enabled word dictionaries
        :type AnsjMain: list of DictInfo
        :param _AnsjStop: List of ansj stopword dictionaries
        :type AnsjStop: list of DictInfo
        :param _AnsjAmbiguity: List of ansj ambiguity lexicons
        :type AnsjAmbiguity: list of DictInfo
        :param _AnsjSynonyms: List of ansj synonym dictionaries
        :type AnsjSynonyms: list of DictInfo
        """
        self._MainDict = None
        self._Stopwords = None
        self._QQDict = None
        self._Synonym = None
        self._UpdateType = None
        self._AnsjMain = None
        self._AnsjStop = None
        self._AnsjAmbiguity = None
        self._AnsjSynonyms = None

    @property
    def MainDict(self):
        r"""List of enabled word dictionaries
        :rtype: list of DictInfo
        """
        return self._MainDict

    @MainDict.setter
    def MainDict(self, MainDict):
        self._MainDict = MainDict

    @property
    def Stopwords(self):
        r"""List of stopword dictionaries
        :rtype: list of DictInfo
        """
        return self._Stopwords

    @Stopwords.setter
    def Stopwords(self, Stopwords):
        self._Stopwords = Stopwords

    @property
    def QQDict(self):
        r"""List of QQ word segmentation dictionaries
        :rtype: list of DictInfo
        """
        return self._QQDict

    @QQDict.setter
    def QQDict(self, QQDict):
        self._QQDict = QQDict

    @property
    def Synonym(self):
        r"""List of synonym dictionaries
        :rtype: list of DictInfo
        """
        return self._Synonym

    @Synonym.setter
    def Synonym(self, Synonym):
        self._Synonym = Synonym

    @property
    def UpdateType(self):
        r"""Update the dictionary type
        :rtype: str
        """
        return self._UpdateType

    @UpdateType.setter
    def UpdateType(self, UpdateType):
        self._UpdateType = UpdateType

    @property
    def AnsjMain(self):
        r"""List of ansj enabled word dictionaries
        :rtype: list of DictInfo
        """
        return self._AnsjMain

    @AnsjMain.setter
    def AnsjMain(self, AnsjMain):
        self._AnsjMain = AnsjMain

    @property
    def AnsjStop(self):
        r"""List of ansj stopword dictionaries
        :rtype: list of DictInfo
        """
        return self._AnsjStop

    @AnsjStop.setter
    def AnsjStop(self, AnsjStop):
        self._AnsjStop = AnsjStop

    @property
    def AnsjAmbiguity(self):
        r"""List of ansj ambiguity lexicons
        :rtype: list of DictInfo
        """
        return self._AnsjAmbiguity

    @AnsjAmbiguity.setter
    def AnsjAmbiguity(self, AnsjAmbiguity):
        self._AnsjAmbiguity = AnsjAmbiguity

    @property
    def AnsjSynonyms(self):
        r"""List of ansj synonym dictionaries
        :rtype: list of DictInfo
        """
        return self._AnsjSynonyms

    @AnsjSynonyms.setter
    def AnsjSynonyms(self, AnsjSynonyms):
        self._AnsjSynonyms = AnsjSynonyms


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
        if params.get("AnsjMain") is not None:
            self._AnsjMain = []
            for item in params.get("AnsjMain"):
                obj = DictInfo()
                obj._deserialize(item)
                self._AnsjMain.append(obj)
        if params.get("AnsjStop") is not None:
            self._AnsjStop = []
            for item in params.get("AnsjStop"):
                obj = DictInfo()
                obj._deserialize(item)
                self._AnsjStop.append(obj)
        if params.get("AnsjAmbiguity") is not None:
            self._AnsjAmbiguity = []
            for item in params.get("AnsjAmbiguity"):
                obj = DictInfo()
                obj._deserialize(item)
                self._AnsjAmbiguity.append(obj)
        if params.get("AnsjSynonyms") is not None:
            self._AnsjSynonyms = []
            for item in params.get("AnsjSynonyms"):
                obj = DictInfo()
                obj._deserialize(item)
                self._AnsjSynonyms.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsPublicAcl(AbstractModel):
    r"""ES public network access control information

    """

    def __init__(self):
        r"""
        :param _BlackIpList: Access the blocklist
        :type BlackIpList: list of str
        :param _WhiteIpList: Access allowlist
        :type WhiteIpList: list of str
        """
        self._BlackIpList = None
        self._WhiteIpList = None

    @property
    def BlackIpList(self):
        r"""Access the blocklist
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
        


class GetRequestTargetNodeTypesResponse(AbstractModel):
    r"""GetRequestTargetNodeTypes response structure.

    """

    def __init__(self):
        r"""
        :param _TargetNodeTypes: List of target node types that receive requests
        :type TargetNodeTypes: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TargetNodeTypes = None
        self._RequestId = None

    @property
    def TargetNodeTypes(self):
        r"""List of target node types that receive requests
        :rtype: list of str
        """
        return self._TargetNodeTypes

    @TargetNodeTypes.setter
    def TargetNodeTypes(self, TargetNodeTypes):
        self._TargetNodeTypes = TargetNodeTypes

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
        self._TargetNodeTypes = params.get("TargetNodeTypes")
        self._RequestId = params.get("RequestId")


class GpuInfo(AbstractModel):
    r"""Gpu information of the node

    """

    def __init__(self):
        r"""
        :param _GpuCount: Number of Gpu blocks
        :type GpuCount: int
        :param _GpuType: GPU type.
        :type GpuType: str
        """
        self._GpuCount = None
        self._GpuType = None

    @property
    def GpuCount(self):
        r"""Number of Gpu blocks
        :rtype: int
        """
        return self._GpuCount

    @GpuCount.setter
    def GpuCount(self, GpuCount):
        self._GpuCount = GpuCount

    @property
    def GpuType(self):
        r"""GPU type.
        :rtype: str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType


    def _deserialize(self, params):
        self._GpuCount = params.get("GpuCount")
        self._GpuType = params.get("GpuType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexMetaField(AbstractModel):
    r"""Index metadata field

    """

    def __init__(self):
        r"""
        :param _IndexType: Index type
        :type IndexType: str
        :param _IndexName: Index name
        :type IndexName: str
        :param _IndexMetaJson: JSON-formatted index metadata
        :type IndexMetaJson: str
        :param _IndexStatus: Index status
        :type IndexStatus: str
        :param _IndexStorage: Index storage size in bytes
        :type IndexStorage: int
        :param _IndexCreateTime: Index creation time
        :type IndexCreateTime: str
        :param _BackingIndices: Backup index
        :type BackingIndices: list of BackingIndexMetaField
        :param _ClusterId: Cluster ID of the index
        :type ClusterId: str
        :param _ClusterName: Cluster name of the index
        :type ClusterName: str
        :param _ClusterVersion: Version number of the cluster to which the index belongs
        :type ClusterVersion: str
        :param _IndexPolicyField: Index lifecycle field
        :type IndexPolicyField: :class:`tencentcloud.es.v20180416.models.IndexPolicyField`
        :param _IndexOptionsField: Index autonomous field
        :type IndexOptionsField: :class:`tencentcloud.es.v20180416.models.IndexOptionsField`
        :param _IndexSettingsField: Index configuration field
        :type IndexSettingsField: :class:`tencentcloud.es.v20180416.models.IndexSettingsField`
        :param _IndexAliasesField: Index alias field
        :type IndexAliasesField: list of str
        :param _AppId: APP ID of the cluster to which the index belongs
        :type AppId: int
        :param _IndexDocs: Number of indexed documents
        :type IndexDocs: int
        """
        self._IndexType = None
        self._IndexName = None
        self._IndexMetaJson = None
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
        self._IndexAliasesField = None
        self._AppId = None
        self._IndexDocs = None

    @property
    def IndexType(self):
        r"""Index type
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""Index name
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexMetaJson(self):
        r"""JSON-formatted index metadata
        :rtype: str
        """
        return self._IndexMetaJson

    @IndexMetaJson.setter
    def IndexMetaJson(self, IndexMetaJson):
        self._IndexMetaJson = IndexMetaJson

    @property
    def IndexStatus(self):
        r"""Index status
        :rtype: str
        """
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus

    @property
    def IndexStorage(self):
        r"""Index storage size in bytes
        :rtype: int
        """
        return self._IndexStorage

    @IndexStorage.setter
    def IndexStorage(self, IndexStorage):
        self._IndexStorage = IndexStorage

    @property
    def IndexCreateTime(self):
        r"""Index creation time
        :rtype: str
        """
        return self._IndexCreateTime

    @IndexCreateTime.setter
    def IndexCreateTime(self, IndexCreateTime):
        self._IndexCreateTime = IndexCreateTime

    @property
    def BackingIndices(self):
        r"""Backup index
        :rtype: list of BackingIndexMetaField
        """
        return self._BackingIndices

    @BackingIndices.setter
    def BackingIndices(self, BackingIndices):
        self._BackingIndices = BackingIndices

    @property
    def ClusterId(self):
        r"""Cluster ID of the index
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""Cluster name of the index
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterVersion(self):
        r"""Version number of the cluster to which the index belongs
        :rtype: str
        """
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def IndexPolicyField(self):
        r"""Index lifecycle field
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexPolicyField`
        """
        return self._IndexPolicyField

    @IndexPolicyField.setter
    def IndexPolicyField(self, IndexPolicyField):
        self._IndexPolicyField = IndexPolicyField

    @property
    def IndexOptionsField(self):
        r"""Index autonomous field
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexOptionsField`
        """
        return self._IndexOptionsField

    @IndexOptionsField.setter
    def IndexOptionsField(self, IndexOptionsField):
        self._IndexOptionsField = IndexOptionsField

    @property
    def IndexSettingsField(self):
        r"""Index configuration field
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexSettingsField`
        """
        return self._IndexSettingsField

    @IndexSettingsField.setter
    def IndexSettingsField(self, IndexSettingsField):
        self._IndexSettingsField = IndexSettingsField

    @property
    def IndexAliasesField(self):
        r"""Index alias field
        :rtype: list of str
        """
        return self._IndexAliasesField

    @IndexAliasesField.setter
    def IndexAliasesField(self, IndexAliasesField):
        self._IndexAliasesField = IndexAliasesField

    @property
    def AppId(self):
        r"""APP ID of the cluster to which the index belongs
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def IndexDocs(self):
        r"""Number of indexed documents
        :rtype: int
        """
        return self._IndexDocs

    @IndexDocs.setter
    def IndexDocs(self, IndexDocs):
        self._IndexDocs = IndexDocs


    def _deserialize(self, params):
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._IndexMetaJson = params.get("IndexMetaJson")
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
        self._IndexAliasesField = params.get("IndexAliasesField")
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
    r"""Index autonomous field

    """

    def __init__(self):
        r"""
        :param _ExpireMaxAge: <p>Expiration time.</p>
        :type ExpireMaxAge: str
        :param _ExpireMaxSize: <p>Expiration size</p>
        :type ExpireMaxSize: str
        :param _RolloverMaxAge: <p>Rollover period</p>
        :type RolloverMaxAge: str
        :param _RolloverDynamic: <p>Whether to enable dynamic scrolling</p>
        :type RolloverDynamic: str
        :param _ShardNumDynamic: <p>Whether to enable dynamic sharding</p>
        :type ShardNumDynamic: str
        :param _TimestampField: <p>Time partition field</p>
        :type TimestampField: str
        :param _WriteMode: <p>Write mode</p>
        :type WriteMode: str
        :param _FullOffloadedEnable: <p>Whether to enable complete uninstallation</p><p>Enumeration values:</p><ul><li>true: enable complete uninstallation</li><li>false: disable complete uninstallation</li></ul>
        :type FullOffloadedEnable: str
        :param _FullOffloadedMaxAge: <p>Full uninstall lifecycle</p>
        :type FullOffloadedMaxAge: str
        :param _FullOffloadedRetrieveMaxAge: <p>Completely uninstall the lifecycle after backup index retrieval</p>
        :type FullOffloadedRetrieveMaxAge: str
        """
        self._ExpireMaxAge = None
        self._ExpireMaxSize = None
        self._RolloverMaxAge = None
        self._RolloverDynamic = None
        self._ShardNumDynamic = None
        self._TimestampField = None
        self._WriteMode = None
        self._FullOffloadedEnable = None
        self._FullOffloadedMaxAge = None
        self._FullOffloadedRetrieveMaxAge = None

    @property
    def ExpireMaxAge(self):
        r"""<p>Expiration time.</p>
        :rtype: str
        """
        return self._ExpireMaxAge

    @ExpireMaxAge.setter
    def ExpireMaxAge(self, ExpireMaxAge):
        self._ExpireMaxAge = ExpireMaxAge

    @property
    def ExpireMaxSize(self):
        r"""<p>Expiration size</p>
        :rtype: str
        """
        return self._ExpireMaxSize

    @ExpireMaxSize.setter
    def ExpireMaxSize(self, ExpireMaxSize):
        self._ExpireMaxSize = ExpireMaxSize

    @property
    def RolloverMaxAge(self):
        r"""<p>Rollover period</p>
        :rtype: str
        """
        return self._RolloverMaxAge

    @RolloverMaxAge.setter
    def RolloverMaxAge(self, RolloverMaxAge):
        self._RolloverMaxAge = RolloverMaxAge

    @property
    def RolloverDynamic(self):
        r"""<p>Whether to enable dynamic scrolling</p>
        :rtype: str
        """
        return self._RolloverDynamic

    @RolloverDynamic.setter
    def RolloverDynamic(self, RolloverDynamic):
        self._RolloverDynamic = RolloverDynamic

    @property
    def ShardNumDynamic(self):
        r"""<p>Whether to enable dynamic sharding</p>
        :rtype: str
        """
        return self._ShardNumDynamic

    @ShardNumDynamic.setter
    def ShardNumDynamic(self, ShardNumDynamic):
        self._ShardNumDynamic = ShardNumDynamic

    @property
    def TimestampField(self):
        r"""<p>Time partition field</p>
        :rtype: str
        """
        return self._TimestampField

    @TimestampField.setter
    def TimestampField(self, TimestampField):
        self._TimestampField = TimestampField

    @property
    def WriteMode(self):
        r"""<p>Write mode</p>
        :rtype: str
        """
        return self._WriteMode

    @WriteMode.setter
    def WriteMode(self, WriteMode):
        self._WriteMode = WriteMode

    @property
    def FullOffloadedEnable(self):
        r"""<p>Whether to enable complete uninstallation</p><p>Enumeration values:</p><ul><li>true: enable complete uninstallation</li><li>false: disable complete uninstallation</li></ul>
        :rtype: str
        """
        return self._FullOffloadedEnable

    @FullOffloadedEnable.setter
    def FullOffloadedEnable(self, FullOffloadedEnable):
        self._FullOffloadedEnable = FullOffloadedEnable

    @property
    def FullOffloadedMaxAge(self):
        r"""<p>Full uninstall lifecycle</p>
        :rtype: str
        """
        return self._FullOffloadedMaxAge

    @FullOffloadedMaxAge.setter
    def FullOffloadedMaxAge(self, FullOffloadedMaxAge):
        self._FullOffloadedMaxAge = FullOffloadedMaxAge

    @property
    def FullOffloadedRetrieveMaxAge(self):
        r"""<p>Completely uninstall the lifecycle after backup index retrieval</p>
        :rtype: str
        """
        return self._FullOffloadedRetrieveMaxAge

    @FullOffloadedRetrieveMaxAge.setter
    def FullOffloadedRetrieveMaxAge(self, FullOffloadedRetrieveMaxAge):
        self._FullOffloadedRetrieveMaxAge = FullOffloadedRetrieveMaxAge


    def _deserialize(self, params):
        self._ExpireMaxAge = params.get("ExpireMaxAge")
        self._ExpireMaxSize = params.get("ExpireMaxSize")
        self._RolloverMaxAge = params.get("RolloverMaxAge")
        self._RolloverDynamic = params.get("RolloverDynamic")
        self._ShardNumDynamic = params.get("ShardNumDynamic")
        self._TimestampField = params.get("TimestampField")
        self._WriteMode = params.get("WriteMode")
        self._FullOffloadedEnable = params.get("FullOffloadedEnable")
        self._FullOffloadedMaxAge = params.get("FullOffloadedMaxAge")
        self._FullOffloadedRetrieveMaxAge = params.get("FullOffloadedRetrieveMaxAge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexPolicyField(AbstractModel):
    r"""Index lifecycle field

    """

    def __init__(self):
        r"""
        :param _WarmEnable: Whether the warm phase is enabled
        :type WarmEnable: str
        :param _WarmMinAge: Transfer time to the warm phase
        :type WarmMinAge: str
        :param _ColdEnable: Whether the cold phase is enabled
        :type ColdEnable: str
        :param _ColdMinAge: Transfer time to the cold phase
        :type ColdMinAge: str
        :param _FrozenEnable: Whether the frozen phase is enabled
        :type FrozenEnable: str
        :param _FrozenMinAge: Time of transfer to the frozen stage
        :type FrozenMinAge: str
        :param _ColdAction: /
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
        r"""Whether the warm phase is enabled
        :rtype: str
        """
        return self._WarmEnable

    @WarmEnable.setter
    def WarmEnable(self, WarmEnable):
        self._WarmEnable = WarmEnable

    @property
    def WarmMinAge(self):
        r"""Transfer time to the warm phase
        :rtype: str
        """
        return self._WarmMinAge

    @WarmMinAge.setter
    def WarmMinAge(self, WarmMinAge):
        self._WarmMinAge = WarmMinAge

    @property
    def ColdEnable(self):
        r"""Whether the cold phase is enabled
        :rtype: str
        """
        return self._ColdEnable

    @ColdEnable.setter
    def ColdEnable(self, ColdEnable):
        self._ColdEnable = ColdEnable

    @property
    def ColdMinAge(self):
        r"""Transfer time to the cold phase
        :rtype: str
        """
        return self._ColdMinAge

    @ColdMinAge.setter
    def ColdMinAge(self, ColdMinAge):
        self._ColdMinAge = ColdMinAge

    @property
    def FrozenEnable(self):
        r"""Whether the frozen phase is enabled
        :rtype: str
        """
        return self._FrozenEnable

    @FrozenEnable.setter
    def FrozenEnable(self, FrozenEnable):
        self._FrozenEnable = FrozenEnable

    @property
    def FrozenMinAge(self):
        r"""Time of transfer to the frozen stage
        :rtype: str
        """
        return self._FrozenMinAge

    @FrozenMinAge.setter
    def FrozenMinAge(self, FrozenMinAge):
        self._FrozenMinAge = FrozenMinAge

    @property
    def ColdAction(self):
        r"""/
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
    r"""Index configuration field

    """

    def __init__(self):
        r"""
        :param _NumberOfShards: Number of index primary shards
        :type NumberOfShards: str
        :param _NumberOfReplicas: Replica shard count of an index
        :type NumberOfReplicas: str
        :param _RefreshInterval: Index refresh frequency
        :type RefreshInterval: str
        """
        self._NumberOfShards = None
        self._NumberOfReplicas = None
        self._RefreshInterval = None

    @property
    def NumberOfShards(self):
        r"""Number of index primary shards
        :rtype: str
        """
        return self._NumberOfShards

    @NumberOfShards.setter
    def NumberOfShards(self, NumberOfShards):
        self._NumberOfShards = NumberOfShards

    @property
    def NumberOfReplicas(self):
        r"""Replica shard count of an index
        :rtype: str
        """
        return self._NumberOfReplicas

    @NumberOfReplicas.setter
    def NumberOfReplicas(self, NumberOfReplicas):
        self._NumberOfReplicas = NumberOfReplicas

    @property
    def RefreshInterval(self):
        r"""Index refresh frequency
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
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _InstanceName: <p>Instance name.</p>
        :type InstanceName: str
        :param _Region: <p>Region.</p>
        :type Region: str
        :param _Zone: <p>AZ.</p>
        :type Zone: str
        :param _AppId: <p>uid</p>
        :type AppId: int
        :param _Uin: <p>User UIN.</p>
        :type Uin: str
        :param _VpcUid: <p>UID of the VPC to which the instance belongs</p>
        :type VpcUid: str
        :param _SubnetUid: <p>UID of the subnet to which the instance belongs</p>
        :type SubnetUid: str
        :param _Status: <p>Instance status. 0: processing, 1: normal, -1: stopped, -2: being destroyed, -3: terminated, -4: isolated, 2: initializing when creating a cluster</p>
        :type Status: int
        :param _RenewFlag: <p>Auto-renewal flag. Value range: <br>RENEW_FLAG_AUTO: auto renewal<br>RENEW_FLAG_MANUAL: no auto-renewal<br>Default value: <br>RENEW_FLAG_DEFAULT: no auto-renewal<br>If this parameter is set to RENEW_FLAG_AUTO, the instance will automatically renew on a monthly basis after expiration if the account balance is sufficient.</p>
        :type RenewFlag: str
        :param _ChargeType: <p>Instance billing mode. Value ranges: PREPAID: prepaid mode, i.e., monthly subscription. POSTPAID_BY_HOUR: postpaid, i.e., pay-as-you-go. CDHPAID: CDH-paid mode, i.e., only charges for CDH, without charging for instances on CDH.</p>
        :type ChargeType: str
        :param _ChargePeriod: <p>Annual and monthly subscription duration, unit: month</p>
        :type ChargePeriod: int
        :param _NodeType: <p>Node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :type NodeType: str
        :param _NodeNum: <p>Number of nodes</p>
        :type NodeNum: int
        :param _CpuNum: <p>Number of node CPU cores.</p>
        :type CpuNum: int
        :param _MemSize: <p>Node memory size (GB).</p>
        :type MemSize: int
        :param _DiskType: <p>Node disk type</p>
        :type DiskType: str
        :param _DiskSize: <p>Node disk size (GB).</p>
        :type DiskSize: int
        :param _EsDomain: <p>ES domain name</p>
        :type EsDomain: str
        :param _EsVip: <p>ES VIP</p>
        :type EsVip: str
        :param _EsPort: <p>ES port</p>
        :type EsPort: int
        :param _KibanaUrl: <p>Kibana access url</p>
        :type KibanaUrl: str
        :param _EsVersion: <p>ES version number</p>
        :type EsVersion: str
        :param _EsConfig: <p>ES configuration item</p>
        :type EsConfig: str
        :param _EsAcl: <p>Kibana Access Control Configuration</p>
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _CreateTime: <p>Instance creation time</p>
        :type CreateTime: str
        :param _UpdateTime: <p>Last modification time of the instance</p>
        :type UpdateTime: str
        :param _Deadline: <p>Instance expiration time</p>
        :type Deadline: str
        :param _InstanceType: <p>Instance type (instance type flag, currently only 1 and 2)</p>
        :type InstanceType: int
        :param _IkConfig: <p>Ik analyzer configuration</p>
        :type IkConfig: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        :param _MasterNodeInfo: <p>Dedicated master node configuration</p>
        :type MasterNodeInfo: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        :param _CosBackup: <p>cos automatic backup configuration</p>
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param _AllowCosBackup: <p>Whether cos automatic backup is allowed</p>
        :type AllowCosBackup: bool
        :param _TagList: <p>Tag list of the instance</p>
        :type TagList: list of TagInfo
        :param _LicenseType: <p>License type<li>oss: open source edition</li><li>basic: basic version</li><li>platinum: platinum version</li>Default value: platinum</p>
        :type LicenseType: str
        :param _RealLicenseType: <p>License type<li>oss: open source edition</li><li>basic: basic version</li><li>platinum: platinum version</li><li>enterprise: enterprise edition</li>Default value: platinum</p>
        :type RealLicenseType: str
        :param _EnableHotWarmMode: <p>Whether it is a hot-cold cluster<li>true: Hot-cold cluster</li><li>false: Non-hot-cold cluster</li></p>
        :type EnableHotWarmMode: bool
        :param _WarmNodeType: <p>Warm node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :type WarmNodeType: str
        :param _WarmNodeNum: <p>Number of warm nodes</p>
        :type WarmNodeNum: int
        :param _WarmCpuNum: <p>Warm node CPU cores</p>
        :type WarmCpuNum: int
        :param _WarmMemSize: <p>Warm node memory size (GB).</p>
        :type WarmMemSize: int
        :param _WarmDiskType: <p>Warm node disk type</p>
        :type WarmDiskType: str
        :param _WarmDiskSize: <p>Warm node disk size (GB).</p>
        :type WarmDiskSize: int
        :param _NodeInfoList: <p>Cluster node information list</p>
        :type NodeInfoList: list of NodeInfo
        :param _EsPublicUrl: <p>Es public network address</p>
        :type EsPublicUrl: str
        :param _MultiZoneInfo: <p>Multi-AZ network info</p>
        :type MultiZoneInfo: list of ZoneDetail
        :param _DeployMode: <p>Deployment mode<li>0: single availability zone</li><li>1: multi-availability zone, Beijing, Shanghai, Shanghai Finance, Guangzhou, Nanjing, Hong Kong, Singapore, Frankfurt (allowlist control)</li></p>
        :type DeployMode: int
        :param _PublicAccess: <p>ES public access status<li>OPEN: enable</li><li>CLOSE: disable</li></p>
        :type PublicAccess: str
        :param _EsPublicAcl: <p>ES public network access control configuration</p>
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _KibanaPrivateUrl: <p>Kibana private network address</p>
        :type KibanaPrivateUrl: str
        :param _KibanaPublicAccess: <p>Kibana public access status<li>OPEN: enabled</li><li>CLOSE: disabled</li></p>
        :type KibanaPublicAccess: str
        :param _KibanaPrivateAccess: <p>Kibana internal access status<li>OPEN: enable</li><li>CLOSE: disable</li></p>
        :type KibanaPrivateAccess: str
        :param _SecurityType: <p>Whether xpack security authentication is enabled for basic version 6.8 (and above versions)<li>1: not enabled</li><li>2: enabled</li></p>
        :type SecurityType: int
        :param _SceneType: <p>Scenario template type: 0, not enabled; 1, common scenarios; 2, log scenario; 3, search scenario</p>
        :type SceneType: int
        :param _KibanaConfig: <p>Kibana configuration item</p>
        :type KibanaConfig: str
        :param _KibanaNodeInfo: <p>Kibana node information</p>
        :type KibanaNodeInfo: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`
        :param _WebNodeTypeInfo: <p>Visualize node configuration</p>
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param _Jdk: <p>JDK type. Valid values: oracle, kona</p>
        :type Jdk: str
        :param _Protocol: <p>Cluster network communication protocol</p>
        :type Protocol: str
        :param _SecurityGroups: <p>Security group id</p>
        :type SecurityGroups: list of str
        :param _ColdNodeType: <p>Cold node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :type ColdNodeType: str
        :param _ColdNodeNum: <p>Number of cold nodes</p>
        :type ColdNodeNum: int
        :param _ColdCpuNum: <p>Cold node CPU cores</p>
        :type ColdCpuNum: int
        :param _ColdMemSize: <p>Cold node memory size (GB).</p>
        :type ColdMemSize: int
        :param _ColdDiskType: <p>Cold node disk type</p>
        :type ColdDiskType: str
        :param _ColdDiskSize: <p>Cold node disk size (GB).</p>
        :type ColdDiskSize: int
        :param _FrozenNodeType: <p>Frozen node specification<li>ES.S1.SMALL2: 1-core 2GB</li><li>ES.S1.MEDIUM4: 2-core 4GB</li><li>ES.S1.MEDIUM8: 2-core 8GB</li><li>ES.S1.LARGE16: 4-core 16GB</li><li>ES.S1.2XLARGE32: 8-core 32GB</li><li>ES.S1.4XLARGE32: 16-core 32GB</li><li>ES.S1.4XLARGE64: 16-core 64GB</li></p>
        :type FrozenNodeType: str
        :param _FrozenNodeNum: <p>Number of frozen nodes</p>
        :type FrozenNodeNum: int
        :param _FrozenCpuNum: <p>Frozen node CPU cores</p>
        :type FrozenCpuNum: int
        :param _FrozenMemSize: <p>Frozen node memory size (GB).</p>
        :type FrozenMemSize: int
        :param _FrozenDiskType: <p>Frozen node disk type</p>
        :type FrozenDiskType: str
        :param _FrozenDiskSize: <p>Frozen node disk size (GB).</p>
        :type FrozenDiskSize: int
        :param _HealthStatus: <p>Cluster health status: -1 unknown; 0 Green; 1 Yellow; 2 Red</p>
        :type HealthStatus: int
        :param _EsPrivateUrl: <p>Intracluster network url for https.</p>
        :type EsPrivateUrl: str
        :param _EsPrivateDomain: <p>https cluster private network domain name</p>
        :type EsPrivateDomain: str
        :param _EsConfigSets: <p>Cluster configuration group information.</p>
        :type EsConfigSets: list of EsConfigSetInfo
        :param _OperationDuration: <p>Cluster maintenance time slot</p>
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param _OptionalWebServiceInfos: <p>web node list</p>
        :type OptionalWebServiceInfos: list of OptionalWebServiceInfo
        :param _AutoIndexEnabled: <p>Autonomous index switch</p>
        :type AutoIndexEnabled: bool
        :param _EnableHybridStorage: <p>Whether storage and computation separation is supported.</p>
        :type EnableHybridStorage: bool
        :param _ProcessPercent: <p>Process progress.</p>
        :type ProcessPercent: float
        :param _KibanaAlteringPublicAccess: <p>Kibana alerting public network alert policy<li>OPEN: enable</li><li>CLOSE: disable</li></p>
        :type KibanaAlteringPublicAccess: str
        :param _HasKernelUpgrade: <p>Whether there is a kernel update this month: false (no) and true (yes).</p>
        :type HasKernelUpgrade: bool
        :param _CdcId: <p>cdcId, pass it when using a CDC subnet</p>
        :type CdcId: str
        :param _KibanaPrivateVip: <p>kibana intranet vip</p>
        :type KibanaPrivateVip: str
        :param _CustomKibanaPrivateUrl: <p>Customize the private network url of kibana</p>
        :type CustomKibanaPrivateUrl: str
        :param _OutboundPublicAcls: <p>Node outbound access detailed information.</p>
        :type OutboundPublicAcls: list of OutboundPublicAcl
        :param _NetConnectScheme: <p>Network connection solution</p>
        :type NetConnectScheme: str
        :param _DisasterRecoverGroupAffinity: <p>Placement group related parameters</p>
        :type DisasterRecoverGroupAffinity: int
        :param _SubProductCode: <p>Sub-product ID enumeration values: open source edition: "sp_es_io2", basic version: "sp_es_basic", platinum version: "sp_es_platinum", AI Search Enhancement Edition: "sp_es_aisearch", enterprise edition: "sp_es_enterprise", CDC platinum version: "sp_es_CDC_platinum", Log Enhancement Edition: "sp_es_enlogging", tsearch: "sp_tsearch_io2", logstash: "sp_es_logstash". It can be empty. When it is empty, the backend maps this field based on LicenseType.</p>
        :type SubProductCode: str
        :param _CosBucketStorageSize: <p>Storage-compute separation cos usage, Unit: M</p>
        :type CosBucketStorageSize: int
        :param _ReadWriteMode: <p>Read-write separation mode: 0: not enabled; 1: local read/write separation; 2: remote read/write separation.</p>
        :type ReadWriteMode: int
        :param _EnableScheduleRecoverGroup: <p>Whether there is an asynchronous task scheduling for placement groups</p>
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: <p>The time when an asynchronous task is scheduled</p>
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        :param _EnableDestroyProtection: <p>Cluster protection: OPEN: enable, CLOSE: disable</p>
        :type EnableDestroyProtection: str
        :param _ShowKibanaIpPort: <p>kibana intranet access address</p>
        :type ShowKibanaIpPort: str
        :param _IsCdzLite: <p>Whether it is a CDZLite availability zone</p>
        :type IsCdzLite: bool
        :param _EsPrivateTcpUrl: <p>Cluster private network tcp address</p>
        :type EsPrivateTcpUrl: str
        :param _IsInRecycleBin: <p>Whether it is in the recycle bin</p><p>Default value: false</p>
        :type IsInRecycleBin: bool
        :param _RecycleLockEnabled: <p>Is locked in the recycle bin</p><p>Default value: false</p>
        :type RecycleLockEnabled: bool
        :param _MayDestroyPoint: <p>The time when termination is expected</p><p>Parameter format: YYYY-MM-DD hh:mm:ss</p>
        :type MayDestroyPoint: str
        :param _DelayDestroyInterval: <p>The time when termination is delayed</p><p>Unit: day</p>
        :type DelayDestroyInterval: int
        :param _EnableAutoReplace: <p>Enable automatic replacement of unhealthy nodes. 0: disable, 1: enable</p>
        :type EnableAutoReplace: int
        :param _OpenMTLS: <p>Enable mtls. 0: disable, 1: enable</p>
        :type OpenMTLS: int
        :param _ServerCertSource: <p>Certificate type</p>
        :type ServerCertSource: str
        :param _OldEsVip: <p>VIP pending migration for the cluster</p>
        :type OldEsVip: str
        :param _OldEsPrivateTcpUrl: <p>Cluster TCP address to be migrated</p>
        :type OldEsPrivateTcpUrl: str
        :param _NeedOfflineOldNodesNotify: <p>Whether to take old nodes offline from the VIP</p>
        :type NeedOfflineOldNodesNotify: bool
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
        self._RealLicenseType = None
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
        self._HasKernelUpgrade = None
        self._CdcId = None
        self._KibanaPrivateVip = None
        self._CustomKibanaPrivateUrl = None
        self._OutboundPublicAcls = None
        self._NetConnectScheme = None
        self._DisasterRecoverGroupAffinity = None
        self._SubProductCode = None
        self._CosBucketStorageSize = None
        self._ReadWriteMode = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None
        self._EnableDestroyProtection = None
        self._ShowKibanaIpPort = None
        self._IsCdzLite = None
        self._EsPrivateTcpUrl = None
        self._IsInRecycleBin = None
        self._RecycleLockEnabled = None
        self._MayDestroyPoint = None
        self._DelayDestroyInterval = None
        self._EnableAutoReplace = None
        self._OpenMTLS = None
        self._ServerCertSource = None
        self._OldEsVip = None
        self._OldEsPrivateTcpUrl = None
        self._NeedOfflineOldNodesNotify = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""<p>Instance name.</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        r"""<p>Region.</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""<p>AZ.</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AppId(self):
        r"""<p>uid</p>
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""<p>User UIN.</p>
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcUid(self):
        r"""<p>UID of the VPC to which the instance belongs</p>
        :rtype: str
        """
        return self._VpcUid

    @VpcUid.setter
    def VpcUid(self, VpcUid):
        self._VpcUid = VpcUid

    @property
    def SubnetUid(self):
        r"""<p>UID of the subnet to which the instance belongs</p>
        :rtype: str
        """
        return self._SubnetUid

    @SubnetUid.setter
    def SubnetUid(self, SubnetUid):
        self._SubnetUid = SubnetUid

    @property
    def Status(self):
        r"""<p>Instance status. 0: processing, 1: normal, -1: stopped, -2: being destroyed, -3: terminated, -4: isolated, 2: initializing when creating a cluster</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RenewFlag(self):
        r"""<p>Auto-renewal flag. Value range: <br>RENEW_FLAG_AUTO: auto renewal<br>RENEW_FLAG_MANUAL: no auto-renewal<br>Default value: <br>RENEW_FLAG_DEFAULT: no auto-renewal<br>If this parameter is set to RENEW_FLAG_AUTO, the instance will automatically renew on a monthly basis after expiration if the account balance is sufficient.</p>
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ChargeType(self):
        r"""<p>Instance billing mode. Value ranges: PREPAID: prepaid mode, i.e., monthly subscription. POSTPAID_BY_HOUR: postpaid, i.e., pay-as-you-go. CDHPAID: CDH-paid mode, i.e., only charges for CDH, without charging for instances on CDH.</p>
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePeriod(self):
        r"""<p>Annual and monthly subscription duration, unit: month</p>
        :rtype: int
        """
        return self._ChargePeriod

    @ChargePeriod.setter
    def ChargePeriod(self, ChargePeriod):
        self._ChargePeriod = ChargePeriod

    @property
    def NodeType(self):
        r"""<p>Node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeNum(self):
        r"""<p>Number of nodes</p>
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def CpuNum(self):
        r"""<p>Number of node CPU cores.</p>
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MemSize(self):
        r"""<p>Node memory size (GB).</p>
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def DiskType(self):
        r"""<p>Node disk type</p>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""<p>Node disk size (GB).</p>
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def EsDomain(self):
        r"""<p>ES domain name</p>
        :rtype: str
        """
        return self._EsDomain

    @EsDomain.setter
    def EsDomain(self, EsDomain):
        self._EsDomain = EsDomain

    @property
    def EsVip(self):
        r"""<p>ES VIP</p>
        :rtype: str
        """
        return self._EsVip

    @EsVip.setter
    def EsVip(self, EsVip):
        self._EsVip = EsVip

    @property
    def EsPort(self):
        r"""<p>ES port</p>
        :rtype: int
        """
        return self._EsPort

    @EsPort.setter
    def EsPort(self, EsPort):
        self._EsPort = EsPort

    @property
    def KibanaUrl(self):
        r"""<p>Kibana access url</p>
        :rtype: str
        """
        return self._KibanaUrl

    @KibanaUrl.setter
    def KibanaUrl(self, KibanaUrl):
        self._KibanaUrl = KibanaUrl

    @property
    def EsVersion(self):
        r"""<p>ES version number</p>
        :rtype: str
        """
        return self._EsVersion

    @EsVersion.setter
    def EsVersion(self, EsVersion):
        self._EsVersion = EsVersion

    @property
    def EsConfig(self):
        r"""<p>ES configuration item</p>
        :rtype: str
        """
        return self._EsConfig

    @EsConfig.setter
    def EsConfig(self, EsConfig):
        self._EsConfig = EsConfig

    @property
    def EsAcl(self):
        r"""<p>Kibana Access Control Configuration</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._EsAcl

    @EsAcl.setter
    def EsAcl(self, EsAcl):
        self._EsAcl = EsAcl

    @property
    def CreateTime(self):
        r"""<p>Instance creation time</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>Last modification time of the instance</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Deadline(self):
        r"""<p>Instance expiration time</p>
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def InstanceType(self):
        r"""<p>Instance type (instance type flag, currently only 1 and 2)</p>
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def IkConfig(self):
        r"""<p>Ik analyzer configuration</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        """
        return self._IkConfig

    @IkConfig.setter
    def IkConfig(self, IkConfig):
        self._IkConfig = IkConfig

    @property
    def MasterNodeInfo(self):
        r"""<p>Dedicated master node configuration</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        """
        return self._MasterNodeInfo

    @MasterNodeInfo.setter
    def MasterNodeInfo(self, MasterNodeInfo):
        self._MasterNodeInfo = MasterNodeInfo

    @property
    def CosBackup(self):
        r"""<p>cos automatic backup configuration</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup

    @property
    def AllowCosBackup(self):
        r"""<p>Whether cos automatic backup is allowed</p>
        :rtype: bool
        """
        return self._AllowCosBackup

    @AllowCosBackup.setter
    def AllowCosBackup(self, AllowCosBackup):
        self._AllowCosBackup = AllowCosBackup

    @property
    def TagList(self):
        r"""<p>Tag list of the instance</p>
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def LicenseType(self):
        r"""<p>License type<li>oss: open source edition</li><li>basic: basic version</li><li>platinum: platinum version</li>Default value: platinum</p>
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def RealLicenseType(self):
        r"""<p>License type<li>oss: open source edition</li><li>basic: basic version</li><li>platinum: platinum version</li><li>enterprise: enterprise edition</li>Default value: platinum</p>
        :rtype: str
        """
        return self._RealLicenseType

    @RealLicenseType.setter
    def RealLicenseType(self, RealLicenseType):
        self._RealLicenseType = RealLicenseType

    @property
    def EnableHotWarmMode(self):
        r"""<p>Whether it is a hot-cold cluster<li>true: Hot-cold cluster</li><li>false: Non-hot-cold cluster</li></p>
        :rtype: bool
        """
        return self._EnableHotWarmMode

    @EnableHotWarmMode.setter
    def EnableHotWarmMode(self, EnableHotWarmMode):
        self._EnableHotWarmMode = EnableHotWarmMode

    @property
    def WarmNodeType(self):
        r"""<p>Warm node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :rtype: str
        """
        return self._WarmNodeType

    @WarmNodeType.setter
    def WarmNodeType(self, WarmNodeType):
        self._WarmNodeType = WarmNodeType

    @property
    def WarmNodeNum(self):
        r"""<p>Number of warm nodes</p>
        :rtype: int
        """
        return self._WarmNodeNum

    @WarmNodeNum.setter
    def WarmNodeNum(self, WarmNodeNum):
        self._WarmNodeNum = WarmNodeNum

    @property
    def WarmCpuNum(self):
        r"""<p>Warm node CPU cores</p>
        :rtype: int
        """
        return self._WarmCpuNum

    @WarmCpuNum.setter
    def WarmCpuNum(self, WarmCpuNum):
        self._WarmCpuNum = WarmCpuNum

    @property
    def WarmMemSize(self):
        r"""<p>Warm node memory size (GB).</p>
        :rtype: int
        """
        return self._WarmMemSize

    @WarmMemSize.setter
    def WarmMemSize(self, WarmMemSize):
        self._WarmMemSize = WarmMemSize

    @property
    def WarmDiskType(self):
        r"""<p>Warm node disk type</p>
        :rtype: str
        """
        return self._WarmDiskType

    @WarmDiskType.setter
    def WarmDiskType(self, WarmDiskType):
        self._WarmDiskType = WarmDiskType

    @property
    def WarmDiskSize(self):
        r"""<p>Warm node disk size (GB).</p>
        :rtype: int
        """
        return self._WarmDiskSize

    @WarmDiskSize.setter
    def WarmDiskSize(self, WarmDiskSize):
        self._WarmDiskSize = WarmDiskSize

    @property
    def NodeInfoList(self):
        r"""<p>Cluster node information list</p>
        :rtype: list of NodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList

    @property
    def EsPublicUrl(self):
        r"""<p>Es public network address</p>
        :rtype: str
        """
        return self._EsPublicUrl

    @EsPublicUrl.setter
    def EsPublicUrl(self, EsPublicUrl):
        self._EsPublicUrl = EsPublicUrl

    @property
    def MultiZoneInfo(self):
        r"""<p>Multi-AZ network info</p>
        :rtype: list of ZoneDetail
        """
        return self._MultiZoneInfo

    @MultiZoneInfo.setter
    def MultiZoneInfo(self, MultiZoneInfo):
        self._MultiZoneInfo = MultiZoneInfo

    @property
    def DeployMode(self):
        r"""<p>Deployment mode<li>0: single availability zone</li><li>1: multi-availability zone, Beijing, Shanghai, Shanghai Finance, Guangzhou, Nanjing, Hong Kong, Singapore, Frankfurt (allowlist control)</li></p>
        :rtype: int
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def PublicAccess(self):
        r"""<p>ES public access status<li>OPEN: enable</li><li>CLOSE: disable</li></p>
        :rtype: str
        """
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def EsPublicAcl(self):
        r"""<p>ES public network access control configuration</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._EsPublicAcl

    @EsPublicAcl.setter
    def EsPublicAcl(self, EsPublicAcl):
        self._EsPublicAcl = EsPublicAcl

    @property
    def KibanaPrivateUrl(self):
        r"""<p>Kibana private network address</p>
        :rtype: str
        """
        return self._KibanaPrivateUrl

    @KibanaPrivateUrl.setter
    def KibanaPrivateUrl(self, KibanaPrivateUrl):
        self._KibanaPrivateUrl = KibanaPrivateUrl

    @property
    def KibanaPublicAccess(self):
        r"""<p>Kibana public access status<li>OPEN: enabled</li><li>CLOSE: disabled</li></p>
        :rtype: str
        """
        return self._KibanaPublicAccess

    @KibanaPublicAccess.setter
    def KibanaPublicAccess(self, KibanaPublicAccess):
        self._KibanaPublicAccess = KibanaPublicAccess

    @property
    def KibanaPrivateAccess(self):
        r"""<p>Kibana internal access status<li>OPEN: enable</li><li>CLOSE: disable</li></p>
        :rtype: str
        """
        return self._KibanaPrivateAccess

    @KibanaPrivateAccess.setter
    def KibanaPrivateAccess(self, KibanaPrivateAccess):
        self._KibanaPrivateAccess = KibanaPrivateAccess

    @property
    def SecurityType(self):
        r"""<p>Whether xpack security authentication is enabled for basic version 6.8 (and above versions)<li>1: not enabled</li><li>2: enabled</li></p>
        :rtype: int
        """
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def SceneType(self):
        r"""<p>Scenario template type: 0, not enabled; 1, common scenarios; 2, log scenario; 3, search scenario</p>
        :rtype: int
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def KibanaConfig(self):
        r"""<p>Kibana configuration item</p>
        :rtype: str
        """
        return self._KibanaConfig

    @KibanaConfig.setter
    def KibanaConfig(self, KibanaConfig):
        self._KibanaConfig = KibanaConfig

    @property
    def KibanaNodeInfo(self):
        r"""<p>Kibana node information</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`
        """
        return self._KibanaNodeInfo

    @KibanaNodeInfo.setter
    def KibanaNodeInfo(self, KibanaNodeInfo):
        self._KibanaNodeInfo = KibanaNodeInfo

    @property
    def WebNodeTypeInfo(self):
        r"""<p>Visualize node configuration</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        """
        return self._WebNodeTypeInfo

    @WebNodeTypeInfo.setter
    def WebNodeTypeInfo(self, WebNodeTypeInfo):
        self._WebNodeTypeInfo = WebNodeTypeInfo

    @property
    def Jdk(self):
        r"""<p>JDK type. Valid values: oracle, kona</p>
        :rtype: str
        """
        return self._Jdk

    @Jdk.setter
    def Jdk(self, Jdk):
        self._Jdk = Jdk

    @property
    def Protocol(self):
        r"""<p>Cluster network communication protocol</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SecurityGroups(self):
        r"""<p>Security group id</p>
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def ColdNodeType(self):
        r"""<p>Cold node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :rtype: str
        """
        return self._ColdNodeType

    @ColdNodeType.setter
    def ColdNodeType(self, ColdNodeType):
        self._ColdNodeType = ColdNodeType

    @property
    def ColdNodeNum(self):
        r"""<p>Number of cold nodes</p>
        :rtype: int
        """
        return self._ColdNodeNum

    @ColdNodeNum.setter
    def ColdNodeNum(self, ColdNodeNum):
        self._ColdNodeNum = ColdNodeNum

    @property
    def ColdCpuNum(self):
        r"""<p>Cold node CPU cores</p>
        :rtype: int
        """
        return self._ColdCpuNum

    @ColdCpuNum.setter
    def ColdCpuNum(self, ColdCpuNum):
        self._ColdCpuNum = ColdCpuNum

    @property
    def ColdMemSize(self):
        r"""<p>Cold node memory size (GB).</p>
        :rtype: int
        """
        return self._ColdMemSize

    @ColdMemSize.setter
    def ColdMemSize(self, ColdMemSize):
        self._ColdMemSize = ColdMemSize

    @property
    def ColdDiskType(self):
        r"""<p>Cold node disk type</p>
        :rtype: str
        """
        return self._ColdDiskType

    @ColdDiskType.setter
    def ColdDiskType(self, ColdDiskType):
        self._ColdDiskType = ColdDiskType

    @property
    def ColdDiskSize(self):
        r"""<p>Cold node disk size (GB).</p>
        :rtype: int
        """
        return self._ColdDiskSize

    @ColdDiskSize.setter
    def ColdDiskSize(self, ColdDiskSize):
        self._ColdDiskSize = ColdDiskSize

    @property
    def FrozenNodeType(self):
        r"""<p>Frozen node specification<li>ES.S1.SMALL2: 1-core 2GB</li><li>ES.S1.MEDIUM4: 2-core 4GB</li><li>ES.S1.MEDIUM8: 2-core 8GB</li><li>ES.S1.LARGE16: 4-core 16GB</li><li>ES.S1.2XLARGE32: 8-core 32GB</li><li>ES.S1.4XLARGE32: 16-core 32GB</li><li>ES.S1.4XLARGE64: 16-core 64GB</li></p>
        :rtype: str
        """
        return self._FrozenNodeType

    @FrozenNodeType.setter
    def FrozenNodeType(self, FrozenNodeType):
        self._FrozenNodeType = FrozenNodeType

    @property
    def FrozenNodeNum(self):
        r"""<p>Number of frozen nodes</p>
        :rtype: int
        """
        return self._FrozenNodeNum

    @FrozenNodeNum.setter
    def FrozenNodeNum(self, FrozenNodeNum):
        self._FrozenNodeNum = FrozenNodeNum

    @property
    def FrozenCpuNum(self):
        r"""<p>Frozen node CPU cores</p>
        :rtype: int
        """
        return self._FrozenCpuNum

    @FrozenCpuNum.setter
    def FrozenCpuNum(self, FrozenCpuNum):
        self._FrozenCpuNum = FrozenCpuNum

    @property
    def FrozenMemSize(self):
        r"""<p>Frozen node memory size (GB).</p>
        :rtype: int
        """
        return self._FrozenMemSize

    @FrozenMemSize.setter
    def FrozenMemSize(self, FrozenMemSize):
        self._FrozenMemSize = FrozenMemSize

    @property
    def FrozenDiskType(self):
        r"""<p>Frozen node disk type</p>
        :rtype: str
        """
        return self._FrozenDiskType

    @FrozenDiskType.setter
    def FrozenDiskType(self, FrozenDiskType):
        self._FrozenDiskType = FrozenDiskType

    @property
    def FrozenDiskSize(self):
        r"""<p>Frozen node disk size (GB).</p>
        :rtype: int
        """
        return self._FrozenDiskSize

    @FrozenDiskSize.setter
    def FrozenDiskSize(self, FrozenDiskSize):
        self._FrozenDiskSize = FrozenDiskSize

    @property
    def HealthStatus(self):
        r"""<p>Cluster health status: -1 unknown; 0 Green; 1 Yellow; 2 Red</p>
        :rtype: int
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def EsPrivateUrl(self):
        r"""<p>Intracluster network url for https.</p>
        :rtype: str
        """
        return self._EsPrivateUrl

    @EsPrivateUrl.setter
    def EsPrivateUrl(self, EsPrivateUrl):
        self._EsPrivateUrl = EsPrivateUrl

    @property
    def EsPrivateDomain(self):
        r"""<p>https cluster private network domain name</p>
        :rtype: str
        """
        return self._EsPrivateDomain

    @EsPrivateDomain.setter
    def EsPrivateDomain(self, EsPrivateDomain):
        self._EsPrivateDomain = EsPrivateDomain

    @property
    def EsConfigSets(self):
        r"""<p>Cluster configuration group information.</p>
        :rtype: list of EsConfigSetInfo
        """
        return self._EsConfigSets

    @EsConfigSets.setter
    def EsConfigSets(self, EsConfigSets):
        self._EsConfigSets = EsConfigSets

    @property
    def OperationDuration(self):
        r"""<p>Cluster maintenance time slot</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def OptionalWebServiceInfos(self):
        r"""<p>web node list</p>
        :rtype: list of OptionalWebServiceInfo
        """
        return self._OptionalWebServiceInfos

    @OptionalWebServiceInfos.setter
    def OptionalWebServiceInfos(self, OptionalWebServiceInfos):
        self._OptionalWebServiceInfos = OptionalWebServiceInfos

    @property
    def AutoIndexEnabled(self):
        r"""<p>Autonomous index switch</p>
        :rtype: bool
        """
        return self._AutoIndexEnabled

    @AutoIndexEnabled.setter
    def AutoIndexEnabled(self, AutoIndexEnabled):
        self._AutoIndexEnabled = AutoIndexEnabled

    @property
    def EnableHybridStorage(self):
        r"""<p>Whether storage and computation separation is supported.</p>
        :rtype: bool
        """
        return self._EnableHybridStorage

    @EnableHybridStorage.setter
    def EnableHybridStorage(self, EnableHybridStorage):
        self._EnableHybridStorage = EnableHybridStorage

    @property
    def ProcessPercent(self):
        r"""<p>Process progress.</p>
        :rtype: float
        """
        return self._ProcessPercent

    @ProcessPercent.setter
    def ProcessPercent(self, ProcessPercent):
        self._ProcessPercent = ProcessPercent

    @property
    def KibanaAlteringPublicAccess(self):
        r"""<p>Kibana alerting public network alert policy<li>OPEN: enable</li><li>CLOSE: disable</li></p>
        :rtype: str
        """
        return self._KibanaAlteringPublicAccess

    @KibanaAlteringPublicAccess.setter
    def KibanaAlteringPublicAccess(self, KibanaAlteringPublicAccess):
        self._KibanaAlteringPublicAccess = KibanaAlteringPublicAccess

    @property
    def HasKernelUpgrade(self):
        r"""<p>Whether there is a kernel update this month: false (no) and true (yes).</p>
        :rtype: bool
        """
        return self._HasKernelUpgrade

    @HasKernelUpgrade.setter
    def HasKernelUpgrade(self, HasKernelUpgrade):
        self._HasKernelUpgrade = HasKernelUpgrade

    @property
    def CdcId(self):
        r"""<p>cdcId, pass it when using a CDC subnet</p>
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def KibanaPrivateVip(self):
        r"""<p>kibana intranet vip</p>
        :rtype: str
        """
        return self._KibanaPrivateVip

    @KibanaPrivateVip.setter
    def KibanaPrivateVip(self, KibanaPrivateVip):
        self._KibanaPrivateVip = KibanaPrivateVip

    @property
    def CustomKibanaPrivateUrl(self):
        r"""<p>Customize the private network url of kibana</p>
        :rtype: str
        """
        return self._CustomKibanaPrivateUrl

    @CustomKibanaPrivateUrl.setter
    def CustomKibanaPrivateUrl(self, CustomKibanaPrivateUrl):
        self._CustomKibanaPrivateUrl = CustomKibanaPrivateUrl

    @property
    def OutboundPublicAcls(self):
        r"""<p>Node outbound access detailed information.</p>
        :rtype: list of OutboundPublicAcl
        """
        return self._OutboundPublicAcls

    @OutboundPublicAcls.setter
    def OutboundPublicAcls(self, OutboundPublicAcls):
        self._OutboundPublicAcls = OutboundPublicAcls

    @property
    def NetConnectScheme(self):
        r"""<p>Network connection solution</p>
        :rtype: str
        """
        return self._NetConnectScheme

    @NetConnectScheme.setter
    def NetConnectScheme(self, NetConnectScheme):
        self._NetConnectScheme = NetConnectScheme

    @property
    def DisasterRecoverGroupAffinity(self):
        r"""<p>Placement group related parameters</p>
        :rtype: int
        """
        return self._DisasterRecoverGroupAffinity

    @DisasterRecoverGroupAffinity.setter
    def DisasterRecoverGroupAffinity(self, DisasterRecoverGroupAffinity):
        self._DisasterRecoverGroupAffinity = DisasterRecoverGroupAffinity

    @property
    def SubProductCode(self):
        r"""<p>Sub-product ID enumeration values: open source edition: "sp_es_io2", basic version: "sp_es_basic", platinum version: "sp_es_platinum", AI Search Enhancement Edition: "sp_es_aisearch", enterprise edition: "sp_es_enterprise", CDC platinum version: "sp_es_CDC_platinum", Log Enhancement Edition: "sp_es_enlogging", tsearch: "sp_tsearch_io2", logstash: "sp_es_logstash". It can be empty. When it is empty, the backend maps this field based on LicenseType.</p>
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def CosBucketStorageSize(self):
        r"""<p>Storage-compute separation cos usage, Unit: M</p>
        :rtype: int
        """
        return self._CosBucketStorageSize

    @CosBucketStorageSize.setter
    def CosBucketStorageSize(self, CosBucketStorageSize):
        self._CosBucketStorageSize = CosBucketStorageSize

    @property
    def ReadWriteMode(self):
        r"""<p>Read-write separation mode: 0: not enabled; 1: local read/write separation; 2: remote read/write separation.</p>
        :rtype: int
        """
        return self._ReadWriteMode

    @ReadWriteMode.setter
    def ReadWriteMode(self, ReadWriteMode):
        self._ReadWriteMode = ReadWriteMode

    @property
    def EnableScheduleRecoverGroup(self):
        r"""<p>Whether there is an asynchronous task scheduling for placement groups</p>
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        r"""<p>The time when an asynchronous task is scheduled</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration

    @property
    def EnableDestroyProtection(self):
        r"""<p>Cluster protection: OPEN: enable, CLOSE: disable</p>
        :rtype: str
        """
        return self._EnableDestroyProtection

    @EnableDestroyProtection.setter
    def EnableDestroyProtection(self, EnableDestroyProtection):
        self._EnableDestroyProtection = EnableDestroyProtection

    @property
    def ShowKibanaIpPort(self):
        r"""<p>kibana intranet access address</p>
        :rtype: str
        """
        return self._ShowKibanaIpPort

    @ShowKibanaIpPort.setter
    def ShowKibanaIpPort(self, ShowKibanaIpPort):
        self._ShowKibanaIpPort = ShowKibanaIpPort

    @property
    def IsCdzLite(self):
        r"""<p>Whether it is a CDZLite availability zone</p>
        :rtype: bool
        """
        return self._IsCdzLite

    @IsCdzLite.setter
    def IsCdzLite(self, IsCdzLite):
        self._IsCdzLite = IsCdzLite

    @property
    def EsPrivateTcpUrl(self):
        r"""<p>Cluster private network tcp address</p>
        :rtype: str
        """
        return self._EsPrivateTcpUrl

    @EsPrivateTcpUrl.setter
    def EsPrivateTcpUrl(self, EsPrivateTcpUrl):
        self._EsPrivateTcpUrl = EsPrivateTcpUrl

    @property
    def IsInRecycleBin(self):
        r"""<p>Whether it is in the recycle bin</p><p>Default value: false</p>
        :rtype: bool
        """
        return self._IsInRecycleBin

    @IsInRecycleBin.setter
    def IsInRecycleBin(self, IsInRecycleBin):
        self._IsInRecycleBin = IsInRecycleBin

    @property
    def RecycleLockEnabled(self):
        r"""<p>Is locked in the recycle bin</p><p>Default value: false</p>
        :rtype: bool
        """
        return self._RecycleLockEnabled

    @RecycleLockEnabled.setter
    def RecycleLockEnabled(self, RecycleLockEnabled):
        self._RecycleLockEnabled = RecycleLockEnabled

    @property
    def MayDestroyPoint(self):
        r"""<p>The time when termination is expected</p><p>Parameter format: YYYY-MM-DD hh:mm:ss</p>
        :rtype: str
        """
        return self._MayDestroyPoint

    @MayDestroyPoint.setter
    def MayDestroyPoint(self, MayDestroyPoint):
        self._MayDestroyPoint = MayDestroyPoint

    @property
    def DelayDestroyInterval(self):
        r"""<p>The time when termination is delayed</p><p>Unit: day</p>
        :rtype: int
        """
        return self._DelayDestroyInterval

    @DelayDestroyInterval.setter
    def DelayDestroyInterval(self, DelayDestroyInterval):
        self._DelayDestroyInterval = DelayDestroyInterval

    @property
    def EnableAutoReplace(self):
        r"""<p>Enable automatic replacement of unhealthy nodes. 0: disable, 1: enable</p>
        :rtype: int
        """
        return self._EnableAutoReplace

    @EnableAutoReplace.setter
    def EnableAutoReplace(self, EnableAutoReplace):
        self._EnableAutoReplace = EnableAutoReplace

    @property
    def OpenMTLS(self):
        r"""<p>Enable mtls. 0: disable, 1: enable</p>
        :rtype: int
        """
        return self._OpenMTLS

    @OpenMTLS.setter
    def OpenMTLS(self, OpenMTLS):
        self._OpenMTLS = OpenMTLS

    @property
    def ServerCertSource(self):
        r"""<p>Certificate type</p>
        :rtype: str
        """
        return self._ServerCertSource

    @ServerCertSource.setter
    def ServerCertSource(self, ServerCertSource):
        self._ServerCertSource = ServerCertSource

    @property
    def OldEsVip(self):
        r"""<p>VIP pending migration for the cluster</p>
        :rtype: str
        """
        return self._OldEsVip

    @OldEsVip.setter
    def OldEsVip(self, OldEsVip):
        self._OldEsVip = OldEsVip

    @property
    def OldEsPrivateTcpUrl(self):
        r"""<p>Cluster TCP address to be migrated</p>
        :rtype: str
        """
        return self._OldEsPrivateTcpUrl

    @OldEsPrivateTcpUrl.setter
    def OldEsPrivateTcpUrl(self, OldEsPrivateTcpUrl):
        self._OldEsPrivateTcpUrl = OldEsPrivateTcpUrl

    @property
    def NeedOfflineOldNodesNotify(self):
        r"""<p>Whether to take old nodes offline from the VIP</p>
        :rtype: bool
        """
        return self._NeedOfflineOldNodesNotify

    @NeedOfflineOldNodesNotify.setter
    def NeedOfflineOldNodesNotify(self, NeedOfflineOldNodesNotify):
        self._NeedOfflineOldNodesNotify = NeedOfflineOldNodesNotify


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
        self._RealLicenseType = params.get("RealLicenseType")
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
        self._HasKernelUpgrade = params.get("HasKernelUpgrade")
        self._CdcId = params.get("CdcId")
        self._KibanaPrivateVip = params.get("KibanaPrivateVip")
        self._CustomKibanaPrivateUrl = params.get("CustomKibanaPrivateUrl")
        if params.get("OutboundPublicAcls") is not None:
            self._OutboundPublicAcls = []
            for item in params.get("OutboundPublicAcls"):
                obj = OutboundPublicAcl()
                obj._deserialize(item)
                self._OutboundPublicAcls.append(obj)
        self._NetConnectScheme = params.get("NetConnectScheme")
        self._DisasterRecoverGroupAffinity = params.get("DisasterRecoverGroupAffinity")
        self._SubProductCode = params.get("SubProductCode")
        self._CosBucketStorageSize = params.get("CosBucketStorageSize")
        self._ReadWriteMode = params.get("ReadWriteMode")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
        self._EnableDestroyProtection = params.get("EnableDestroyProtection")
        self._ShowKibanaIpPort = params.get("ShowKibanaIpPort")
        self._IsCdzLite = params.get("IsCdzLite")
        self._EsPrivateTcpUrl = params.get("EsPrivateTcpUrl")
        self._IsInRecycleBin = params.get("IsInRecycleBin")
        self._RecycleLockEnabled = params.get("RecycleLockEnabled")
        self._MayDestroyPoint = params.get("MayDestroyPoint")
        self._DelayDestroyInterval = params.get("DelayDestroyInterval")
        self._EnableAutoReplace = params.get("EnableAutoReplace")
        self._OpenMTLS = params.get("OpenMTLS")
        self._ServerCertSource = params.get("ServerCertSource")
        self._OldEsVip = params.get("OldEsVip")
        self._OldEsPrivateTcpUrl = params.get("OldEsPrivateTcpUrl")
        self._NeedOfflineOldNodesNotify = params.get("NeedOfflineOldNodesNotify")
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
        :param _Ip: Cluster node IP address.
        :type Ip: str
        :param _Message: Log content
        :type Message: str
        :param _NodeID: Cluster node ID.
        :type NodeID: str
        :param _IndexName: Slow log index name
        :type IndexName: str
        :param _Shard: Slow log index shards
        :type Shard: str
        :param _QueryCost: Slow log index query time
        :type QueryCost: str
        """
        self._Time = None
        self._Level = None
        self._Ip = None
        self._Message = None
        self._NodeID = None
        self._IndexName = None
        self._Shard = None
        self._QueryCost = None

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
        r"""Cluster node IP address.
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

    @property
    def NodeID(self):
        r"""Cluster node ID.
        :rtype: str
        """
        return self._NodeID

    @NodeID.setter
    def NodeID(self, NodeID):
        self._NodeID = NodeID

    @property
    def IndexName(self):
        r"""Slow log index name
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Shard(self):
        r"""Slow log index shards
        :rtype: str
        """
        return self._Shard

    @Shard.setter
    def Shard(self, Shard):
        self._Shard = Shard

    @property
    def QueryCost(self):
        r"""Slow log index query time
        :rtype: str
        """
        return self._QueryCost

    @QueryCost.setter
    def QueryCost(self, QueryCost):
        self._QueryCost = QueryCost


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Level = params.get("Level")
        self._Ip = params.get("Ip")
        self._Message = params.get("Message")
        self._NodeID = params.get("NodeID")
        self._IndexName = params.get("IndexName")
        self._Shard = params.get("Shard")
        self._QueryCost = params.get("QueryCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    r"""OperationDetail uses an array of this structure to describe the old and new configuration

    """

    def __init__(self):
        r"""
        :param _Key: Key.
        :type Key: str
        :param _Value: Value.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value.
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
    r"""Kibana node-related information of the instance

    """

    def __init__(self):
        r"""
        :param _KibanaNodeType: Kibana node specification
        :type KibanaNodeType: str
        :param _KibanaNodeNum: Number of Kibana nodes
        :type KibanaNodeNum: int
        :param _KibanaNodeCpuNum: Number of CPUs of the Kibana node
        :type KibanaNodeCpuNum: int
        :param _KibanaNodeMemSize: Kibana node memory in GB
        :type KibanaNodeMemSize: int
        :param _KibanaNodeDiskType: Kibana node disk type
        :type KibanaNodeDiskType: str
        :param _KibanaNodeDiskSize: Kibana node disk size
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
        r"""Number of CPUs of the Kibana node
        :rtype: int
        """
        return self._KibanaNodeCpuNum

    @KibanaNodeCpuNum.setter
    def KibanaNodeCpuNum(self, KibanaNodeCpuNum):
        self._KibanaNodeCpuNum = KibanaNodeCpuNum

    @property
    def KibanaNodeMemSize(self):
        r"""Kibana node memory in GB
        :rtype: int
        """
        return self._KibanaNodeMemSize

    @KibanaNodeMemSize.setter
    def KibanaNodeMemSize(self, KibanaNodeMemSize):
        self._KibanaNodeMemSize = KibanaNodeMemSize

    @property
    def KibanaNodeDiskType(self):
        r"""Kibana node disk type
        :rtype: str
        """
        return self._KibanaNodeDiskType

    @KibanaNodeDiskType.setter
    def KibanaNodeDiskType(self, KibanaNodeDiskType):
        self._KibanaNodeDiskType = KibanaNodeDiskType

    @property
    def KibanaNodeDiskSize(self):
        r"""Kibana node disk size
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
        :param _Ip: <p>Kibana node IP</p>
        :type Ip: str
        :param _DiskSize: <p>Total node disk size</p>
        :type DiskSize: int
        :param _DiskUsage: <p>Disk utilization rate</p>
        :type DiskUsage: float
        :param _MemSize: <p>Node memory size</p>
        :type MemSize: int
        :param _MemUsage: <p>Memory usage rate</p>
        :type MemUsage: float
        :param _CpuNum: <p>Number of CPUs on the node</p>
        :type CpuNum: int
        :param _CpuUsage: <p>cpu utilization</p>
        :type CpuUsage: float
        :param _Zone: <p>AZ.</p>
        :type Zone: str
        :param _NodeId: <p>ts-0noqayxu-az6-hot-03222010-0</p>
        :type NodeId: str
        :param _UserIp: <p>Client-side Ip info</p>
        :type UserIp: str
        """
        self._Ip = None
        self._DiskSize = None
        self._DiskUsage = None
        self._MemSize = None
        self._MemUsage = None
        self._CpuNum = None
        self._CpuUsage = None
        self._Zone = None
        self._NodeId = None
        self._UserIp = None

    @property
    def Ip(self):
        r"""<p>Kibana node IP</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def DiskSize(self):
        r"""<p>Total node disk size</p>
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskUsage(self):
        r"""<p>Disk utilization rate</p>
        :rtype: float
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def MemSize(self):
        r"""<p>Node memory size</p>
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MemUsage(self):
        r"""<p>Memory usage rate</p>
        :rtype: float
        """
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def CpuNum(self):
        r"""<p>Number of CPUs on the node</p>
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def CpuUsage(self):
        r"""<p>cpu utilization</p>
        :rtype: float
        """
        return self._CpuUsage

    @CpuUsage.setter
    def CpuUsage(self, CpuUsage):
        self._CpuUsage = CpuUsage

    @property
    def Zone(self):
        r"""<p>AZ.</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeId(self):
        r"""<p>ts-0noqayxu-az6-hot-03222010-0</p>
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def UserIp(self):
        r"""<p>Client-side Ip info</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._DiskSize = params.get("DiskSize")
        self._DiskUsage = params.get("DiskUsage")
        self._MemSize = params.get("MemSize")
        self._MemUsage = params.get("MemUsage")
        self._CpuNum = params.get("CpuNum")
        self._CpuUsage = params.get("CpuUsage")
        self._Zone = params.get("Zone")
        self._NodeId = params.get("NodeId")
        self._UserIp = params.get("UserIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskInfo(AbstractModel):
    r"""Local disk information of the node

    """

    def __init__(self):
        r"""
        :param _LocalDiskType: Local disk type<li>LOCAL_SATA: big data type</li><li>NVME_SSD: high IO type</li>
        :type LocalDiskType: str
        :param _LocalDiskSize: Single local disk size
        :type LocalDiskSize: int
        :param _LocalDiskCount: Number of local disk blocks
        :type LocalDiskCount: int
        """
        self._LocalDiskType = None
        self._LocalDiskSize = None
        self._LocalDiskCount = None

    @property
    def LocalDiskType(self):
        r"""Local disk type<li>LOCAL_SATA: big data type</li><li>NVME_SSD: high IO type</li>
        :rtype: str
        """
        return self._LocalDiskType

    @LocalDiskType.setter
    def LocalDiskType(self, LocalDiskType):
        self._LocalDiskType = LocalDiskType

    @property
    def LocalDiskSize(self):
        r"""Single local disk size
        :rtype: int
        """
        return self._LocalDiskSize

    @LocalDiskSize.setter
    def LocalDiskSize(self, LocalDiskSize):
        self._LocalDiskSize = LocalDiskSize

    @property
    def LocalDiskCount(self):
        r"""Number of local disk blocks
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
    r"""Instance-dedicated primary node-related information

    """

    def __init__(self):
        r"""
        :param _EnableDedicatedMaster: Whether the dedicated master node is enabled or not
        :type EnableDedicatedMaster: bool
        :param _MasterNodeType: Dedicated primary node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li>
        :type MasterNodeType: str
        :param _MasterNodeNum: Number of dedicated primary nodes
        :type MasterNodeNum: int
        :param _MasterNodeCpuNum: Number of CPU cores of the dedicated master node
        :type MasterNodeCpuNum: int
        :param _MasterNodeMemSize: Dedicated primary node memory size, in GB.
        :type MasterNodeMemSize: int
        :param _MasterNodeDiskSize: Dedicated primary node disk size in GB
        :type MasterNodeDiskSize: int
        :param _MasterNodeDiskType: Dedicated primary node disk type
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
        r"""Whether the dedicated master node is enabled or not
        :rtype: bool
        """
        return self._EnableDedicatedMaster

    @EnableDedicatedMaster.setter
    def EnableDedicatedMaster(self, EnableDedicatedMaster):
        self._EnableDedicatedMaster = EnableDedicatedMaster

    @property
    def MasterNodeType(self):
        r"""Dedicated primary node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li>
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
        r"""Number of CPU cores of the dedicated master node
        :rtype: int
        """
        return self._MasterNodeCpuNum

    @MasterNodeCpuNum.setter
    def MasterNodeCpuNum(self, MasterNodeCpuNum):
        self._MasterNodeCpuNum = MasterNodeCpuNum

    @property
    def MasterNodeMemSize(self):
        r"""Dedicated primary node memory size, in GB.
        :rtype: int
        """
        return self._MasterNodeMemSize

    @MasterNodeMemSize.setter
    def MasterNodeMemSize(self, MasterNodeMemSize):
        self._MasterNodeMemSize = MasterNodeMemSize

    @property
    def MasterNodeDiskSize(self):
        r"""Dedicated primary node disk size in GB
        :rtype: int
        """
        return self._MasterNodeDiskSize

    @MasterNodeDiskSize.setter
    def MasterNodeDiskSize(self, MasterNodeDiskSize):
        self._MasterNodeDiskSize = MasterNodeDiskSize

    @property
    def MasterNodeDiskType(self):
        r"""Dedicated primary node disk type
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
        


class ModifyAutoBackUpCommonInfoRequest(AbstractModel):
    r"""ModifyAutoBackUpCommonInfo request structure.

    """


class ModifyAutoBackUpCommonInfoResponse(AbstractModel):
    r"""ModifyAutoBackUpCommonInfo response structure.

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


class ModifyAutoBackUpStrategyRequest(AbstractModel):
    r"""ModifyAutoBackUpStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance name.
        :type InstanceId: str
        :param _StrategyName: Current policy name.
        :type StrategyName: str
        :param _CosBackup: Policy information.
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        self._InstanceId = None
        self._StrategyName = None
        self._CosBackup = None

    @property
    def InstanceId(self):
        r"""Instance name.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StrategyName(self):
        r"""Current policy name.
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def CosBackup(self):
        r"""Policy information.
        :rtype: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StrategyName = params.get("StrategyName")
        if params.get("CosBackup") is not None:
            self._CosBackup = CosBackup()
            self._CosBackup._deserialize(params.get("CosBackup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackUpStrategyResponse(AbstractModel):
    r"""ModifyAutoBackUpStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Valid values: true (success) and false (failure).
        :type Status: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Valid values: true (success) and false (failure).
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class NodeInfo(AbstractModel):
    r"""Specification description information of a node type in the cluster (such as hot data node, cold data node, dedicated master node), including node type, number of nodes, node specification, disk type, and disk size. If Type is not specified, it defaults to hot data node. If the node is a master node, the DiskType and DiskSize parameters will be ignored (the primary node has no data disk).

    """

    def __init__(self):
        r"""
        :param _NodeNum: <p>Number of nodes.</p>
        :type NodeNum: int
        :param _NodeType: <p>Node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :type NodeType: str
        :param _Type: <p>Node type</p><p>Enumeration values:</p><ul><li>hotData: hot data node</li><li>warmData: cold data node</li><li>dedicatedMaster: dedicated master node</li><li>dedicatedCoordinating: dedicated coordinator node</li><li>dedicatedMl: dedicated Machine Learning node</li></ul>
        :type Type: str
        :param _DiskType: <p>Node disk type<li>CLOUD_SSD: ssd cloud disk</li><li>CLOUD_PREMIUM: high-performance cloud disk</li>Default value: CLOUD_SSD</p>
        :type DiskType: str
        :param _DiskSize: <p>Node disk capacity (GB)</p>
        :type DiskSize: int
        :param _LocalDiskInfo: <p>Node local disk information.</p>
        :type LocalDiskInfo: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`
        :param _DiskCount: <p>Number of node disk blocks</p>
        :type DiskCount: int
        :param _DiskEncrypt: <p>Whether the node disk is encrypted. 0: no encryption; 1: encryption; not encrypted by default</p>
        :type DiskEncrypt: int
        :param _KmsKeyId: <p>Custom encryption key id</p>
        :type KmsKeyId: str
        :param _KmsKeyName: <p>Custom encryption key name</p>
        :type KmsKeyName: str
        :param _CpuNum: <p>Number of CPUs</p>
        :type CpuNum: int
        :param _MemSize: <p>Memory size, in GB.</p>
        :type MemSize: int
        :param _DiskEnhance: <p>Additional hard disk performance</p>
        :type DiskEnhance: int
        :param _GpuInfo: <p>Gpu information of the node</p>
        :type GpuInfo: :class:`tencentcloud.es.v20180416.models.GpuInfo`
        """
        self._NodeNum = None
        self._NodeType = None
        self._Type = None
        self._DiskType = None
        self._DiskSize = None
        self._LocalDiskInfo = None
        self._DiskCount = None
        self._DiskEncrypt = None
        self._KmsKeyId = None
        self._KmsKeyName = None
        self._CpuNum = None
        self._MemSize = None
        self._DiskEnhance = None
        self._GpuInfo = None

    @property
    def NodeNum(self):
        r"""<p>Number of nodes.</p>
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def NodeType(self):
        r"""<p>Node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li></p>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def Type(self):
        r"""<p>Node type</p><p>Enumeration values:</p><ul><li>hotData: hot data node</li><li>warmData: cold data node</li><li>dedicatedMaster: dedicated master node</li><li>dedicatedCoordinating: dedicated coordinator node</li><li>dedicatedMl: dedicated Machine Learning node</li></ul>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DiskType(self):
        r"""<p>Node disk type<li>CLOUD_SSD: ssd cloud disk</li><li>CLOUD_PREMIUM: high-performance cloud disk</li>Default value: CLOUD_SSD</p>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""<p>Node disk capacity (GB)</p>
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def LocalDiskInfo(self):
        r"""<p>Node local disk information.</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`
        """
        return self._LocalDiskInfo

    @LocalDiskInfo.setter
    def LocalDiskInfo(self, LocalDiskInfo):
        self._LocalDiskInfo = LocalDiskInfo

    @property
    def DiskCount(self):
        r"""<p>Number of node disk blocks</p>
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskEncrypt(self):
        r"""<p>Whether the node disk is encrypted. 0: no encryption; 1: encryption; not encrypted by default</p>
        :rtype: int
        """
        return self._DiskEncrypt

    @DiskEncrypt.setter
    def DiskEncrypt(self, DiskEncrypt):
        self._DiskEncrypt = DiskEncrypt

    @property
    def KmsKeyId(self):
        r"""<p>Custom encryption key id</p>
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def KmsKeyName(self):
        r"""<p>Custom encryption key name</p>
        :rtype: str
        """
        return self._KmsKeyName

    @KmsKeyName.setter
    def KmsKeyName(self, KmsKeyName):
        self._KmsKeyName = KmsKeyName

    @property
    def CpuNum(self):
        r"""<p>Number of CPUs</p>
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MemSize(self):
        r"""<p>Memory size, in GB.</p>
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def DiskEnhance(self):
        r"""<p>Additional hard disk performance</p>
        :rtype: int
        """
        return self._DiskEnhance

    @DiskEnhance.setter
    def DiskEnhance(self, DiskEnhance):
        self._DiskEnhance = DiskEnhance

    @property
    def GpuInfo(self):
        r"""<p>Gpu information of the node</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.GpuInfo`
        """
        return self._GpuInfo

    @GpuInfo.setter
    def GpuInfo(self, GpuInfo):
        self._GpuInfo = GpuInfo


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
        self._KmsKeyId = params.get("KmsKeyId")
        self._KmsKeyName = params.get("KmsKeyName")
        self._CpuNum = params.get("CpuNum")
        self._MemSize = params.get("MemSize")
        self._DiskEnhance = params.get("DiskEnhance")
        if params.get("GpuInfo") is not None:
            self._GpuInfo = GpuInfo()
            self._GpuInfo._deserialize(params.get("GpuInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeView(AbstractModel):
    r"""Node dimension view data

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID.
        :type NodeId: str
        :param _NodeIp: Node IP
        :type NodeIp: str
        :param _Visible: Whether the node is visible
        :type Visible: float
        :param _Break: Whether to fuse
        :type Break: float
        :param _DiskSize: Total node disk size
        :type DiskSize: int
        :param _DiskUsage: Disk utilization rate
        :type DiskUsage: float
        :param _MemSize: Node memory size (unit: GB)
        :type MemSize: int
        :param _MemUsage: Memory usage rate
        :type MemUsage: float
        :param _CpuNum: Number of CPUs on the node
        :type CpuNum: int
        :param _CpuUsage: CPU utilization
        :type CpuUsage: float
        :param _Zone: AZ.
        :type Zone: str
        :param _NodeRole: Node role
        :type NodeRole: str
        :param _NodeHttpIp: Node HTTP IP
        :type NodeHttpIp: str
        :param _JvmMemUsage: JVM memory usage rate
        :type JvmMemUsage: float
        :param _ShardNum: Number of shards per node
        :type ShardNum: int
        :param _DiskIds: Disk ID list on node
        :type DiskIds: list of str
        :param _Hidden: Whether it is a hidden AZ
        :type Hidden: bool
        :param _IsCoordinationNode: Whether to act as the coordination node role
        :type IsCoordinationNode: bool
        :param _CVMStatus: CVM running state
        :type CVMStatus: str
        :param _CVMDisasterRecoverGroupId: id of the placement group bound to the cvm
        :type CVMDisasterRecoverGroupId: str
        :param _CVMDisasterRecoverGroupStatus: Status of the placement group bound to the cvm. 2: Bound; 1: Binding; 0: Not enabled
        :type CVMDisasterRecoverGroupStatus: int
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
        self._IsCoordinationNode = None
        self._CVMStatus = None
        self._CVMDisasterRecoverGroupId = None
        self._CVMDisasterRecoverGroupStatus = None

    @property
    def NodeId(self):
        r"""Node ID.
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
        r"""Whether to fuse
        :rtype: float
        """
        return self._Break

    @Break.setter
    def Break(self, Break):
        self._Break = Break

    @property
    def DiskSize(self):
        r"""Total node disk size
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskUsage(self):
        r"""Disk utilization rate
        :rtype: float
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def MemSize(self):
        r"""Node memory size (unit: GB)
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MemUsage(self):
        r"""Memory usage rate
        :rtype: float
        """
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def CpuNum(self):
        r"""Number of CPUs on the node
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def CpuUsage(self):
        r"""CPU utilization
        :rtype: float
        """
        return self._CpuUsage

    @CpuUsage.setter
    def CpuUsage(self, CpuUsage):
        self._CpuUsage = CpuUsage

    @property
    def Zone(self):
        r"""AZ.
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
        r"""JVM memory usage rate
        :rtype: float
        """
        return self._JvmMemUsage

    @JvmMemUsage.setter
    def JvmMemUsage(self, JvmMemUsage):
        self._JvmMemUsage = JvmMemUsage

    @property
    def ShardNum(self):
        r"""Number of shards per node
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def DiskIds(self):
        r"""Disk ID list on node
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Hidden(self):
        r"""Whether it is a hidden AZ
        :rtype: bool
        """
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden

    @property
    def IsCoordinationNode(self):
        r"""Whether to act as the coordination node role
        :rtype: bool
        """
        return self._IsCoordinationNode

    @IsCoordinationNode.setter
    def IsCoordinationNode(self, IsCoordinationNode):
        self._IsCoordinationNode = IsCoordinationNode

    @property
    def CVMStatus(self):
        r"""CVM running state
        :rtype: str
        """
        return self._CVMStatus

    @CVMStatus.setter
    def CVMStatus(self, CVMStatus):
        self._CVMStatus = CVMStatus

    @property
    def CVMDisasterRecoverGroupId(self):
        r"""id of the placement group bound to the cvm
        :rtype: str
        """
        return self._CVMDisasterRecoverGroupId

    @CVMDisasterRecoverGroupId.setter
    def CVMDisasterRecoverGroupId(self, CVMDisasterRecoverGroupId):
        self._CVMDisasterRecoverGroupId = CVMDisasterRecoverGroupId

    @property
    def CVMDisasterRecoverGroupStatus(self):
        r"""Status of the placement group bound to the cvm. 2: Bound; 1: Binding; 0: Not enabled
        :rtype: int
        """
        return self._CVMDisasterRecoverGroupStatus

    @CVMDisasterRecoverGroupStatus.setter
    def CVMDisasterRecoverGroupStatus(self, CVMDisasterRecoverGroupStatus):
        self._CVMDisasterRecoverGroupStatus = CVMDisasterRecoverGroupStatus


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
        self._IsCoordinationNode = params.get("IsCoordinationNode")
        self._CVMStatus = params.get("CVMStatus")
        self._CVMDisasterRecoverGroupId = params.get("CVMDisasterRecoverGroupId")
        self._CVMDisasterRecoverGroupStatus = params.get("CVMDisasterRecoverGroupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operation(AbstractModel):
    r"""Detailed ES cluster operation information

    """

    def __init__(self):
        r"""
        :param _Id: <p>Unique id of the operation</p>
        :type Id: int
        :param _StartTime: <p>Operation start time.</p>
        :type StartTime: str
        :param _Type: <p>Operation type.</p>
        :type Type: str
        :param _Detail: <p>Operation details.</p>
        :type Detail: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        :param _Result: <p>Operation result.</p>
        :type Result: str
        :param _Tasks: <p>Process task info</p>
        :type Tasks: list of TaskDetail
        :param _Progress: <p>Operation progress.</p>
        :type Progress: float
        :param _RollbackTag: <p>Rollback tag. 0: not rolled back, 1: rolling back, 2: rolled back</p>
        :type RollbackTag: int
        :param _SubAccountUin: <p>Operator Uin</p>
        :type SubAccountUin: str
        :param _AutoScaleTag: <p>Auto scaling flag. Valid values: 0 (non-auto) and 1 (auto).</p>
        :type AutoScaleTag: int
        :param _SuspendedReason: <p>Process exception cause</p>
        :type SuspendedReason: str
        """
        self._Id = None
        self._StartTime = None
        self._Type = None
        self._Detail = None
        self._Result = None
        self._Tasks = None
        self._Progress = None
        self._RollbackTag = None
        self._SubAccountUin = None
        self._AutoScaleTag = None
        self._SuspendedReason = None

    @property
    def Id(self):
        r"""<p>Unique id of the operation</p>
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        r"""<p>Operation start time.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""<p>Operation type.</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Detail(self):
        r"""<p>Operation details.</p>
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Result(self):
        r"""<p>Operation result.</p>
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Tasks(self):
        r"""<p>Process task info</p>
        :rtype: list of TaskDetail
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Progress(self):
        r"""<p>Operation progress.</p>
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RollbackTag(self):
        r"""<p>Rollback tag. 0: not rolled back, 1: rolling back, 2: rolled back</p>
        :rtype: int
        """
        return self._RollbackTag

    @RollbackTag.setter
    def RollbackTag(self, RollbackTag):
        self._RollbackTag = RollbackTag

    @property
    def SubAccountUin(self):
        r"""<p>Operator Uin</p>
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def AutoScaleTag(self):
        r"""<p>Auto scaling flag. Valid values: 0 (non-auto) and 1 (auto).</p>
        :rtype: int
        """
        return self._AutoScaleTag

    @AutoScaleTag.setter
    def AutoScaleTag(self, AutoScaleTag):
        self._AutoScaleTag = AutoScaleTag

    @property
    def SuspendedReason(self):
        r"""<p>Process exception cause</p>
        :rtype: str
        """
        return self._SuspendedReason

    @SuspendedReason.setter
    def SuspendedReason(self, SuspendedReason):
        self._SuspendedReason = SuspendedReason


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
        self._RollbackTag = params.get("RollbackTag")
        self._SubAccountUin = params.get("SubAccountUin")
        self._AutoScaleTag = params.get("AutoScaleTag")
        self._SuspendedReason = params.get("SuspendedReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDetail(AbstractModel):
    r"""Operation details.

    """

    def __init__(self):
        r"""
        :param _OldInfo: Original configuration message of the instance
        :type OldInfo: list of KeyValue
        :param _NewInfo: Configuration message after the instance update
        :type NewInfo: list of KeyValue
        """
        self._OldInfo = None
        self._NewInfo = None

    @property
    def OldInfo(self):
        r"""Original configuration message of the instance
        :rtype: list of KeyValue
        """
        return self._OldInfo

    @OldInfo.setter
    def OldInfo(self, OldInfo):
        self._OldInfo = OldInfo

    @property
    def NewInfo(self):
        r"""Configuration message after the instance update
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
    r"""Cluster maintainability time

    """

    def __init__(self):
        r"""
        :param _Periods: Maintenance period, which refers to Monday to Sunday. Valid values: [0, 6].
        :type Periods: list of int non-negative
        :param _TimeStart: Maintenance start time
        :type TimeStart: str
        :param _TimeEnd: Maintenance end time.
        :type TimeEnd: str
        :param _TimeZone: Time zone in UTC format
        :type TimeZone: str
        """
        self._Periods = None
        self._TimeStart = None
        self._TimeEnd = None
        self._TimeZone = None

    @property
    def Periods(self):
        r"""Maintenance period, which refers to Monday to Sunday. Valid values: [0, 6].
        :rtype: list of int non-negative
        """
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def TimeStart(self):
        r"""Maintenance start time
        :rtype: str
        """
        return self._TimeStart

    @TimeStart.setter
    def TimeStart(self, TimeStart):
        self._TimeStart = TimeStart

    @property
    def TimeEnd(self):
        r"""Maintenance end time.
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def TimeZone(self):
        r"""Time zone in UTC format
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
    r"""Cluster maintainability time

    """

    def __init__(self):
        r"""
        :param _Periods: Maintenance period, which refers to Monday to Sunday. Valid values: [0, 6].
        :type Periods: list of int non-negative
        :param _TimeStart: Maintenance start time
        :type TimeStart: str
        :param _TimeEnd: Maintenance end time.
        :type TimeEnd: str
        :param _TimeZone: Time zone in UTC format
        :type TimeZone: str
        :param _MoreInstances: ES cluster ID array
        :type MoreInstances: list of str
        """
        self._Periods = None
        self._TimeStart = None
        self._TimeEnd = None
        self._TimeZone = None
        self._MoreInstances = None

    @property
    def Periods(self):
        r"""Maintenance period, which refers to Monday to Sunday. Valid values: [0, 6].
        :rtype: list of int non-negative
        """
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def TimeStart(self):
        r"""Maintenance start time
        :rtype: str
        """
        return self._TimeStart

    @TimeStart.setter
    def TimeStart(self, TimeStart):
        self._TimeStart = TimeStart

    @property
    def TimeEnd(self):
        r"""Maintenance end time.
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def TimeZone(self):
        r"""Time zone in UTC format
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def MoreInstances(self):
        r"""ES cluster ID array
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
    r"""Optional web component information

    """

    def __init__(self):
        r"""
        :param _Type: Type.
        :type Type: str
        :param _Status: Status.
        :type Status: int
        :param _PublicUrl: Public url
        :type PublicUrl: str
        :param _PrivateUrl: Private network url
        :type PrivateUrl: str
        :param _PublicAccess: Public access permissions
        :type PublicAccess: str
        :param _PrivateAccess: Private network access permission
        :type PrivateAccess: str
        :param _Version: Version
        :type Version: str
        :param _PrivateVip: Intranet vip of the web service
        :type PrivateVip: str
        :param _CustomPrivateUrl: Custom url of cerebro on the private network
        :type CustomPrivateUrl: str
        """
        self._Type = None
        self._Status = None
        self._PublicUrl = None
        self._PrivateUrl = None
        self._PublicAccess = None
        self._PrivateAccess = None
        self._Version = None
        self._PrivateVip = None
        self._CustomPrivateUrl = None

    @property
    def Type(self):
        r"""Type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""Status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PublicUrl(self):
        r"""Public url
        :rtype: str
        """
        return self._PublicUrl

    @PublicUrl.setter
    def PublicUrl(self, PublicUrl):
        self._PublicUrl = PublicUrl

    @property
    def PrivateUrl(self):
        r"""Private network url
        :rtype: str
        """
        return self._PrivateUrl

    @PrivateUrl.setter
    def PrivateUrl(self, PrivateUrl):
        self._PrivateUrl = PrivateUrl

    @property
    def PublicAccess(self):
        r"""Public access permissions
        :rtype: str
        """
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def PrivateAccess(self):
        r"""Private network access permission
        :rtype: str
        """
        return self._PrivateAccess

    @PrivateAccess.setter
    def PrivateAccess(self, PrivateAccess):
        self._PrivateAccess = PrivateAccess

    @property
    def Version(self):
        r"""Version
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def PrivateVip(self):
        r"""Intranet vip of the web service
        :rtype: str
        """
        return self._PrivateVip

    @PrivateVip.setter
    def PrivateVip(self, PrivateVip):
        self._PrivateVip = PrivateVip

    @property
    def CustomPrivateUrl(self):
        r"""Custom url of cerebro on the private network
        :rtype: str
        """
        return self._CustomPrivateUrl

    @CustomPrivateUrl.setter
    def CustomPrivateUrl(self, CustomPrivateUrl):
        self._CustomPrivateUrl = CustomPrivateUrl


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._PublicUrl = params.get("PublicUrl")
        self._PrivateUrl = params.get("PrivateUrl")
        self._PublicAccess = params.get("PublicAccess")
        self._PrivateAccess = params.get("PrivateAccess")
        self._Version = params.get("Version")
        self._PrivateVip = params.get("PrivateVip")
        self._CustomPrivateUrl = params.get("CustomPrivateUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherConfig(AbstractModel):
    r"""Additional EsConfig and JvmHeapConfig used by updateInstance

    """

    def __init__(self):
        r"""
        :param _EsConfig: Additional yml configuration for es
        :type EsConfig: str
        :param _JvmHeapConfig: jvm heap configuration of es
        :type JvmHeapConfig: str
        """
        self._EsConfig = None
        self._JvmHeapConfig = None

    @property
    def EsConfig(self):
        r"""Additional yml configuration for es
        :rtype: str
        """
        return self._EsConfig

    @EsConfig.setter
    def EsConfig(self, EsConfig):
        self._EsConfig = EsConfig

    @property
    def JvmHeapConfig(self):
        r"""jvm heap configuration of es
        :rtype: str
        """
        return self._JvmHeapConfig

    @JvmHeapConfig.setter
    def JvmHeapConfig(self, JvmHeapConfig):
        self._JvmHeapConfig = JvmHeapConfig


    def _deserialize(self, params):
        self._EsConfig = params.get("EsConfig")
        self._JvmHeapConfig = params.get("JvmHeapConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutboundPublicAcl(AbstractModel):
    r"""Node outbound access information

    """

    def __init__(self):
        r"""
        :param _NodeType: Node types with permission for node outbound access
        :type NodeType: str
        :param _WhiteHostList: Allowlist for outbound access from nodes
        :type WhiteHostList: list of str
        """
        self._NodeType = None
        self._WhiteHostList = None

    @property
    def NodeType(self):
        r"""Node types with permission for node outbound access
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def WhiteHostList(self):
        r"""Allowlist for outbound access from nodes
        :rtype: list of str
        """
        return self._WhiteHostList

    @WhiteHostList.setter
    def WhiteHostList(self, WhiteHostList):
        self._WhiteHostList = WhiteHostList


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._WhiteHostList = params.get("WhiteHostList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessDetail(AbstractModel):
    r"""Task progress details

    """

    def __init__(self):
        r"""
        :param _Completed: <p>Number of completed</p>
        :type Completed: int
        :param _Remain: <p>Remaining quantity</p>
        :type Remain: int
        :param _Total: <p>Total quantity.</p>
        :type Total: int
        :param _TaskType: <p>Task type:<br>60: Restart task<br>70: Shard migration task<br>80: Node configuration modification task</p>
        :type TaskType: int
        :param _EstimatedTimeRemaining: <p>Estimated remaining time</p><p>Unit: seconds</p>
        :type EstimatedTimeRemaining: int
        """
        self._Completed = None
        self._Remain = None
        self._Total = None
        self._TaskType = None
        self._EstimatedTimeRemaining = None

    @property
    def Completed(self):
        r"""<p>Number of completed</p>
        :rtype: int
        """
        return self._Completed

    @Completed.setter
    def Completed(self, Completed):
        self._Completed = Completed

    @property
    def Remain(self):
        r"""<p>Remaining quantity</p>
        :rtype: int
        """
        return self._Remain

    @Remain.setter
    def Remain(self, Remain):
        self._Remain = Remain

    @property
    def Total(self):
        r"""<p>Total quantity.</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TaskType(self):
        r"""<p>Task type:<br>60: Restart task<br>70: Shard migration task<br>80: Node configuration modification task</p>
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def EstimatedTimeRemaining(self):
        r"""<p>Estimated remaining time</p><p>Unit: seconds</p>
        :rtype: int
        """
        return self._EstimatedTimeRemaining

    @EstimatedTimeRemaining.setter
    def EstimatedTimeRemaining(self, EstimatedTimeRemaining):
        self._EstimatedTimeRemaining = EstimatedTimeRemaining


    def _deserialize(self, params):
        self._Completed = params.get("Completed")
        self._Remain = params.get("Remain")
        self._Total = params.get("Total")
        self._TaskType = params.get("TaskType")
        self._EstimatedTimeRemaining = params.get("EstimatedTimeRemaining")
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
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _ForceRestart: <p>Whether to force restart<li>true: force restart</li><li>false: do not force restart</li>Default value: false</p>
        :type ForceRestart: bool
        :param _RestartMode: <p>Restart mode: 0 rolling restart; 1 full restart</p>
        :type RestartMode: int
        :param _UpgradeKernel: <p>Select whether to upgrade the kernel patch version upon restart</p>
        :type UpgradeKernel: bool
        """
        self._InstanceId = None
        self._ForceRestart = None
        self._RestartMode = None
        self._UpgradeKernel = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForceRestart(self):
        r"""<p>Whether to force restart<li>true: force restart</li><li>false: do not force restart</li>Default value: false</p>
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def RestartMode(self):
        r"""<p>Restart mode: 0 rolling restart; 1 full restart</p>
        :rtype: int
        """
        return self._RestartMode

    @RestartMode.setter
    def RestartMode(self, RestartMode):
        self._RestartMode = RestartMode

    @property
    def UpgradeKernel(self):
        r"""<p>Select whether to upgrade the kernel patch version upon restart</p>
        :rtype: bool
        """
        return self._UpgradeKernel

    @UpgradeKernel.setter
    def UpgradeKernel(self, UpgradeKernel):
        self._UpgradeKernel = UpgradeKernel


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ForceRestart = params.get("ForceRestart")
        self._RestartMode = params.get("RestartMode")
        self._UpgradeKernel = params.get("UpgradeKernel")
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


class RestartKibanaRequest(AbstractModel):
    r"""RestartKibana request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""ES instance ID.
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


class RestartNodesRequest(AbstractModel):
    r"""RestartNodes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID.
        :type InstanceId: str
        :param _NodeNames: Node name list
        :type NodeNames: list of str
        :param _ForceRestart: Whether to perform forced reboot.
        :type ForceRestart: bool
        :param _RestartMode: Optional restart mode. `in-place`: restart; `blue-green`: blue-green restart. Default value: `in-place`.
        :type RestartMode: str
        :param _IsOffline: Node status, for use in blue-green mode; offline node blue/green at risk
        :type IsOffline: bool
        :param _CvmDelayOnlineTime: cvm delay listing time
        :type CvmDelayOnlineTime: int
        :param _ShardAllocationConcurrents: Number of concurrent shard migrations
        :type ShardAllocationConcurrents: int
        :param _ShardAllocationBytes: Shard migration concurrency speed
        :type ShardAllocationBytes: int
        :param _EnableScheduleRecoverGroup: Whether to enable the placement group asynchronous task
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: Time period of the async task for the placement group
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        :param _EventTypeIds: Event ID list.
        :type EventTypeIds: list of str
        """
        self._InstanceId = None
        self._NodeNames = None
        self._ForceRestart = None
        self._RestartMode = None
        self._IsOffline = None
        self._CvmDelayOnlineTime = None
        self._ShardAllocationConcurrents = None
        self._ShardAllocationBytes = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None
        self._EventTypeIds = None

    @property
    def InstanceId(self):
        r"""Cluster instance ID.
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
        r"""Whether to perform forced reboot.
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def RestartMode(self):
        r"""Optional restart mode. `in-place`: restart; `blue-green`: blue-green restart. Default value: `in-place`.
        :rtype: str
        """
        return self._RestartMode

    @RestartMode.setter
    def RestartMode(self, RestartMode):
        self._RestartMode = RestartMode

    @property
    def IsOffline(self):
        r"""Node status, for use in blue-green mode; offline node blue/green at risk
        :rtype: bool
        """
        return self._IsOffline

    @IsOffline.setter
    def IsOffline(self, IsOffline):
        self._IsOffline = IsOffline

    @property
    def CvmDelayOnlineTime(self):
        r"""cvm delay listing time
        :rtype: int
        """
        return self._CvmDelayOnlineTime

    @CvmDelayOnlineTime.setter
    def CvmDelayOnlineTime(self, CvmDelayOnlineTime):
        self._CvmDelayOnlineTime = CvmDelayOnlineTime

    @property
    def ShardAllocationConcurrents(self):
        r"""Number of concurrent shard migrations
        :rtype: int
        """
        return self._ShardAllocationConcurrents

    @ShardAllocationConcurrents.setter
    def ShardAllocationConcurrents(self, ShardAllocationConcurrents):
        self._ShardAllocationConcurrents = ShardAllocationConcurrents

    @property
    def ShardAllocationBytes(self):
        r"""Shard migration concurrency speed
        :rtype: int
        """
        return self._ShardAllocationBytes

    @ShardAllocationBytes.setter
    def ShardAllocationBytes(self, ShardAllocationBytes):
        self._ShardAllocationBytes = ShardAllocationBytes

    @property
    def EnableScheduleRecoverGroup(self):
        r"""Whether to enable the placement group asynchronous task
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        r"""Time period of the async task for the placement group
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration

    @property
    def EventTypeIds(self):
        r"""Event ID list.
        :rtype: list of str
        """
        return self._EventTypeIds

    @EventTypeIds.setter
    def EventTypeIds(self, EventTypeIds):
        self._EventTypeIds = EventTypeIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeNames = params.get("NodeNames")
        self._ForceRestart = params.get("ForceRestart")
        self._RestartMode = params.get("RestartMode")
        self._IsOffline = params.get("IsOffline")
        self._CvmDelayOnlineTime = params.get("CvmDelayOnlineTime")
        self._ShardAllocationConcurrents = params.get("ShardAllocationConcurrents")
        self._ShardAllocationBytes = params.get("ShardAllocationBytes")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
        self._EventTypeIds = params.get("EventTypeIds")
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


class SubTaskDetail(AbstractModel):
    r"""Subtask information in the process task of the instance operation record (for example, each check item in the upgrade check task)

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
        :param _Status: Subtask status. 0: processing, 1: success, -1: failure
        :type Status: int
        :param _FailedIndices: Index name that failed the upgrade check
        :type FailedIndices: list of str
        :param _FinishTime: Subtask end time
        :type FinishTime: str
        :param _Level: Subtask level. 1: warning; 2: failure
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
        r"""Subtask status. 0: processing, 1: success, -1: failure
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailedIndices(self):
        r"""Index name that failed the upgrade check
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
        r"""Subtask level. 1: warning; 2: failure
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
    r"""Instance tag information.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value.
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
    r"""Process task information in the instance operation record

    """

    def __init__(self):
        r"""
        :param _Name: Task Name
        :type Name: str
        :param _Progress: Task progress
        :type Progress: float
        :param _FinishTime: Task completion time
        :type FinishTime: str
        :param _SubTasks: Subtask
        :type SubTasks: list of SubTaskDetail
        :param _ElapsedTime: Time taken by the task
        :type ElapsedTime: int
        :param _ProcessInfo: Task progress details
        :type ProcessInfo: :class:`tencentcloud.es.v20180416.models.ProcessDetail`
        """
        self._Name = None
        self._Progress = None
        self._FinishTime = None
        self._SubTasks = None
        self._ElapsedTime = None
        self._ProcessInfo = None

    @property
    def Name(self):
        r"""Task Name
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
        r"""Time taken by the task
        :rtype: int
        """
        return self._ElapsedTime

    @ElapsedTime.setter
    def ElapsedTime(self, ElapsedTime):
        self._ElapsedTime = ElapsedTime

    @property
    def ProcessInfo(self):
        r"""Task progress details
        :rtype: :class:`tencentcloud.es.v20180416.models.ProcessDetail`
        """
        return self._ProcessInfo

    @ProcessInfo.setter
    def ProcessInfo(self, ProcessInfo):
        self._ProcessInfo = ProcessInfo


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
        if params.get("ProcessInfo") is not None:
            self._ProcessInfo = ProcessDetail()
            self._ProcessInfo._deserialize(params.get("ProcessInfo"))
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
        :param _InstanceId: ES instance ID.
        :type InstanceId: str
        :param _IkMainDicts: Address of the COS main dictionary for IK word segmentation entered during installation, and the dictionary name such as test.dic entered during deletion.
        :type IkMainDicts: list of str
        :param _IkStopwords: Address of the COS stopword dictionary for IK word segmentation during installation. When deleting, enter the dictionary name, for example, test.dic.
        :type IkStopwords: list of str
        :param _Synonym: Address of the synonym dictionary COS during installation, and the dictionary name such as test.dic when deleting.
        :type Synonym: list of str
        :param _QQDict: Address of the COS QQ tokenizer dictionary during installation, and the dictionary name such as test.dic during deletion.
        :type QQDict: list of str
        :param _UpdateType: 0: installation; 1: deletion. Default value: 0
        :type UpdateType: int
        :param _ForceRestart: Whether to force restart the cluster. Default value: false
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
        r"""ES instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IkMainDicts(self):
        r"""Address of the COS main dictionary for IK word segmentation entered during installation, and the dictionary name such as test.dic entered during deletion.
        :rtype: list of str
        """
        return self._IkMainDicts

    @IkMainDicts.setter
    def IkMainDicts(self, IkMainDicts):
        self._IkMainDicts = IkMainDicts

    @property
    def IkStopwords(self):
        r"""Address of the COS stopword dictionary for IK word segmentation during installation. When deleting, enter the dictionary name, for example, test.dic.
        :rtype: list of str
        """
        return self._IkStopwords

    @IkStopwords.setter
    def IkStopwords(self, IkStopwords):
        self._IkStopwords = IkStopwords

    @property
    def Synonym(self):
        r"""Address of the synonym dictionary COS during installation, and the dictionary name such as test.dic when deleting.
        :rtype: list of str
        """
        return self._Synonym

    @Synonym.setter
    def Synonym(self, Synonym):
        self._Synonym = Synonym

    @property
    def QQDict(self):
        r"""Address of the COS QQ tokenizer dictionary during installation, and the dictionary name such as test.dic during deletion.
        :rtype: list of str
        """
        return self._QQDict

    @QQDict.setter
    def QQDict(self, QQDict):
        self._QQDict = QQDict

    @property
    def UpdateType(self):
        r"""0: installation; 1: deletion. Default value: 0
        :rtype: int
        """
        return self._UpdateType

    @UpdateType.setter
    def UpdateType(self, UpdateType):
        self._UpdateType = UpdateType

    @property
    def ForceRestart(self):
        r"""Whether to force restart the cluster. Default value: false
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


class UpdateIndexRequest(AbstractModel):
    r"""UpdateIndex request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>ES cluster ID</p>
        :type InstanceId: str
        :param _IndexType: <p>Updated index type. auto: autonomous index; normal: general index</p>
        :type IndexType: str
        :param _IndexName: <p>Updated index name</p>
        :type IndexName: str
        :param _UpdateMetaJson: <p>Updated JSON-formatted index metadata, such as mappings and settings</p>
        :type UpdateMetaJson: str
        :param _Username: <p>Cluster access username.</p>
        :type Username: str
        :param _Password: <p>Cluster access password</p>
        :type Password: str
        :param _RolloverBackingIndex: <p>Whether to scroll the backup index</p>
        :type RolloverBackingIndex: bool
        :param _MountIndex: <p>Whether to retrieve the full uninstall index</p>
        :type MountIndex: bool
        :param _IndexUuid: <p>Index Uuid</p>
        :type IndexUuid: str
        :param _BackingIndexName: <p>Backing index name</p>
        :type BackingIndexName: str
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._UpdateMetaJson = None
        self._Username = None
        self._Password = None
        self._RolloverBackingIndex = None
        self._MountIndex = None
        self._IndexUuid = None
        self._BackingIndexName = None

    @property
    def InstanceId(self):
        r"""<p>ES cluster ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        r"""<p>Updated index type. auto: autonomous index; normal: general index</p>
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        r"""<p>Updated index name</p>
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def UpdateMetaJson(self):
        r"""<p>Updated JSON-formatted index metadata, such as mappings and settings</p>
        :rtype: str
        """
        return self._UpdateMetaJson

    @UpdateMetaJson.setter
    def UpdateMetaJson(self, UpdateMetaJson):
        self._UpdateMetaJson = UpdateMetaJson

    @property
    def Username(self):
        r"""<p>Cluster access username.</p>
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""<p>Cluster access password</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RolloverBackingIndex(self):
        r"""<p>Whether to scroll the backup index</p>
        :rtype: bool
        """
        return self._RolloverBackingIndex

    @RolloverBackingIndex.setter
    def RolloverBackingIndex(self, RolloverBackingIndex):
        self._RolloverBackingIndex = RolloverBackingIndex

    @property
    def MountIndex(self):
        r"""<p>Whether to retrieve the full uninstall index</p>
        :rtype: bool
        """
        return self._MountIndex

    @MountIndex.setter
    def MountIndex(self, MountIndex):
        self._MountIndex = MountIndex

    @property
    def IndexUuid(self):
        r"""<p>Index Uuid</p>
        :rtype: str
        """
        return self._IndexUuid

    @IndexUuid.setter
    def IndexUuid(self, IndexUuid):
        self._IndexUuid = IndexUuid

    @property
    def BackingIndexName(self):
        r"""<p>Backing index name</p>
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
        self._UpdateMetaJson = params.get("UpdateMetaJson")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._RolloverBackingIndex = params.get("RolloverBackingIndex")
        self._MountIndex = params.get("MountIndex")
        self._IndexUuid = params.get("IndexUuid")
        self._BackingIndexName = params.get("BackingIndexName")
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


class UpdateInstanceRequest(AbstractModel):
    r"""UpdateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name (1-50 English letters, Chinese characters, digits, hyphens -, or underscores _)
        :type InstanceName: str
        :param _NodeNum: Abandoned. Please use NodeInfoList.
Number of nodes (2-50).
        :type NodeNum: int
        :param _EsConfig: ES configuration item (JSON format string)
        :type EsConfig: str
        :param _Password: Password of the default user elastic (8–16 characters, including at least two of the following: [a-z,A-Z], [0-9], and special characters [-!@#$%&^*+=_:;,.?])
        :type Password: str
        :param _EsAcl: Public access policy for visualization components (Kibana and Cerebro)
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _DiskSize: Abandoned. Please use NodeInfoList.
Disk size in GB
        :type DiskSize: int
        :param _NodeType: Abandoned. Please use NodeInfoList.
Node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li>
        :type NodeType: str
        :param _MasterNodeNum: Abandoned. Please use NodeInfoList.
Number of dedicated primary nodes (supports only 3 or 5)
        :type MasterNodeNum: int
        :param _MasterNodeType: Abandoned. Please use NodeInfoList.
Dedicated primary node specification<li>ES.S1.SMALL2: 1-core 2GB</li><li>ES.S1.MEDIUM4: 2-core 4GB</li><li>ES.S1.MEDIUM8: 2-core 8GB</li><li>ES.S1.LARGE16: 4-core 16GB</li><li>ES.S1.2XLARGE32: 8-core 32GB</li><li>ES.S1.4XLARGE32: 16-core 32GB</li><li>ES.S1.4XLARGE64: 16-core 64GB</li>
        :type MasterNodeType: str
        :param _MasterNodeDiskSize: Abandoned. Please use NodeInfoList.
Dedicated primary node disk size (in GB. The system default configuration is 50 GB. Customization is temporarily not supported.)
        :type MasterNodeDiskSize: int
        :param _ForceRestart: Whether to force restart when updating the configuration <li>true: force restart</li><li>false: do not force restart</li>Currently, this needs to be set only when updating EsConfig. The default value is false.
        :type ForceRestart: bool
        :param _CosBackup: COS auto backup information
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param _NodeInfoList: Node information list. You can transmit only the node to be updated and its corresponding specification information. Supported operations include <li>modifying the count of a node type</li><li>modifying the node specification and disk size of a node type</li><li>adding a node type (you need to simultaneously specify the node type, count, specification, disk, and other information)</li>. You can perform only one of the above operations at a time, and the disk type cannot be modified.
        :type NodeInfoList: list of NodeInfo
        :param _PublicAccess: Public access status of the ES cluster
OPEN: enabled.
-CLOSE: disabled.
        :type PublicAccess: str
        :param _EsPublicAcl: Public network access control list
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`
        :param _KibanaPublicAccess: Kibana public access status
OPEN: enabled.
-CLOSE: disabled.
        :type KibanaPublicAccess: str
        :param _KibanaPrivateAccess: Kibana internal access status
OPEN: enabled.
-CLOSE: disabled.
        :type KibanaPrivateAccess: str
        :param _BasicSecurityType: Turn on or off user authentication for the basic version of ES 6.8 and above
        :type BasicSecurityType: int
        :param _KibanaPrivatePort: Kibana private network port
        :type KibanaPrivatePort: int
        :param _ScaleType: 0: Scale out via blue-green change without restarting the cluster (default) 1: Scale out by unmounting disks with a cluster rolling restart
        :type ScaleType: int
        :param _MultiZoneInfo: Multi-AZ deployment
        :type MultiZoneInfo: list of ZoneDetail
        :param _SceneType: Scenario template type. -1: not enabled. 1: common. 2: log. 3: search
        :type SceneType: int
        :param _KibanaConfig: Kibana configuration item (JSON format string)
        :type KibanaConfig: str
        :param _WebNodeTypeInfo: Visualize node configuration
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param _SwitchPrivateLink: Switch to the new network architecture
        :type SwitchPrivateLink: str
        :param _EnableCerebro: Enable Cerebro
        :type EnableCerebro: bool
        :param _CerebroPublicAccess: Cerebro public access status
OPEN: enabled.
-CLOSE: disabled.
        :type CerebroPublicAccess: str
        :param _CerebroPrivateAccess: Cerebro private network access status
OPEN: enabled.
-CLOSE: disabled.
        :type CerebroPrivateAccess: str
        :param _EsConfigSet: Newly-added or modified configuration group information
        :type EsConfigSet: :class:`tencentcloud.es.v20180416.models.EsConfigSetInfo`
        :param _OperationDuration: Maintenance time slot.
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        :param _KibanaAlteringPublicAccess: Whether Alerting public network alert output is enabled:
OPEN: enabled.
-CLOSE: disabled.
        :type KibanaAlteringPublicAccess: str
        :param _KibanaPrivateDomain: Custom domain name of kibana on the private network
        :type KibanaPrivateDomain: str
        :param _CerebroPrivateDomain: Custom domain name of cerebro on the private network
        :type CerebroPrivateDomain: str
        :param _Protocol: Change to an https cluster. http is selected by default.
        :type Protocol: str
        :param _OutboundPublicAcls: Outbound access details of the node

        :type OutboundPublicAcls: list of OutboundPublicAcl
        :param _OutboundPublicAccess: Outbound access operations of the node
OPEN
-CLOSE: disabled.
        :type OutboundPublicAccess: str
        :param _CvmDelayOnlineTime: Parameter for delayed cvm launch
        :type CvmDelayOnlineTime: int
        :param _ShardAllocationConcurrents: Number of concurrent shard migrations
        :type ShardAllocationConcurrents: int
        :param _ShardAllocationBytes: Shard migration concurrency speed
        :type ShardAllocationBytes: int
        :param _ReadWriteMode: Read-write separation mode: -1: not enabled; 1: local read/write separation; 2: remote read/write separation.
        :type ReadWriteMode: int
        :param _EnableScheduleRecoverGroup: Whether to enable the placement group async task
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: Placement group async task maintenance time slot
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        :param _EnableDestroyProtection: Cluster protection: OPEN: enable, CLOSE: disable
        :type EnableDestroyProtection: str
        :param _AutoScaleDiskInfoList: Auto capacity expansion parameter
        :type AutoScaleDiskInfoList: list of AutoScaleDiskInfo
        :param _AutoScaleDiskDeleteNodeTypeList: Auto-expansion delete parameter
        :type AutoScaleDiskDeleteNodeTypeList: list of str
        :param _OtherConfig: Other additional configuration, jvm or yml.
        :type OtherConfig: :class:`tencentcloud.es.v20180416.models.OtherConfig`
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
        self._KibanaPrivateDomain = None
        self._CerebroPrivateDomain = None
        self._Protocol = None
        self._OutboundPublicAcls = None
        self._OutboundPublicAccess = None
        self._CvmDelayOnlineTime = None
        self._ShardAllocationConcurrents = None
        self._ShardAllocationBytes = None
        self._ReadWriteMode = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None
        self._EnableDestroyProtection = None
        self._AutoScaleDiskInfoList = None
        self._AutoScaleDiskDeleteNodeTypeList = None
        self._OtherConfig = None

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
        r"""Instance name (1-50 English letters, Chinese characters, digits, hyphens -, or underscores _)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NodeNum(self):
        r"""Abandoned. Please use NodeInfoList.
Number of nodes (2-50).
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def EsConfig(self):
        r"""ES configuration item (JSON format string)
        :rtype: str
        """
        return self._EsConfig

    @EsConfig.setter
    def EsConfig(self, EsConfig):
        self._EsConfig = EsConfig

    @property
    def Password(self):
        r"""Password of the default user elastic (8–16 characters, including at least two of the following: [a-z,A-Z], [0-9], and special characters [-!@#$%&^*+=_:;,.?])
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EsAcl(self):
        r"""Public access policy for visualization components (Kibana and Cerebro)
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._EsAcl

    @EsAcl.setter
    def EsAcl(self, EsAcl):
        self._EsAcl = EsAcl

    @property
    def DiskSize(self):
        r"""Abandoned. Please use NodeInfoList.
Disk size in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def NodeType(self):
        r"""Abandoned. Please use NodeInfoList.
Node specification<li>ES.S1.SMALL2: 1-core 2G</li><li>ES.S1.MEDIUM4: 2-core 4G</li><li>ES.S1.MEDIUM8: 2-core 8G</li><li>ES.S1.LARGE16: 4-core 16G</li><li>ES.S1.2XLARGE32: 8-core 32G</li><li>ES.S1.4XLARGE32: 16-core 32G</li><li>ES.S1.4XLARGE64: 16-core 64G</li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def MasterNodeNum(self):
        r"""Abandoned. Please use NodeInfoList.
Number of dedicated primary nodes (supports only 3 or 5)
        :rtype: int
        """
        return self._MasterNodeNum

    @MasterNodeNum.setter
    def MasterNodeNum(self, MasterNodeNum):
        self._MasterNodeNum = MasterNodeNum

    @property
    def MasterNodeType(self):
        r"""Abandoned. Please use NodeInfoList.
Dedicated primary node specification<li>ES.S1.SMALL2: 1-core 2GB</li><li>ES.S1.MEDIUM4: 2-core 4GB</li><li>ES.S1.MEDIUM8: 2-core 8GB</li><li>ES.S1.LARGE16: 4-core 16GB</li><li>ES.S1.2XLARGE32: 8-core 32GB</li><li>ES.S1.4XLARGE32: 16-core 32GB</li><li>ES.S1.4XLARGE64: 16-core 64GB</li>
        :rtype: str
        """
        return self._MasterNodeType

    @MasterNodeType.setter
    def MasterNodeType(self, MasterNodeType):
        self._MasterNodeType = MasterNodeType

    @property
    def MasterNodeDiskSize(self):
        r"""Abandoned. Please use NodeInfoList.
Dedicated primary node disk size (in GB. The system default configuration is 50 GB. Customization is temporarily not supported.)
        :rtype: int
        """
        return self._MasterNodeDiskSize

    @MasterNodeDiskSize.setter
    def MasterNodeDiskSize(self, MasterNodeDiskSize):
        self._MasterNodeDiskSize = MasterNodeDiskSize

    @property
    def ForceRestart(self):
        r"""Whether to force restart when updating the configuration <li>true: force restart</li><li>false: do not force restart</li>Currently, this needs to be set only when updating EsConfig. The default value is false.
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def CosBackup(self):
        r"""COS auto backup information
        :rtype: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup

    @property
    def NodeInfoList(self):
        r"""Node information list. You can transmit only the node to be updated and its corresponding specification information. Supported operations include <li>modifying the count of a node type</li><li>modifying the node specification and disk size of a node type</li><li>adding a node type (you need to simultaneously specify the node type, count, specification, disk, and other information)</li>. You can perform only one of the above operations at a time, and the disk type cannot be modified.
        :rtype: list of NodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList

    @property
    def PublicAccess(self):
        r"""Public access status of the ES cluster
OPEN: enabled.
-CLOSE: disabled.
        :rtype: str
        """
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def EsPublicAcl(self):
        r"""Public network access control list
        :rtype: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`
        """
        return self._EsPublicAcl

    @EsPublicAcl.setter
    def EsPublicAcl(self, EsPublicAcl):
        self._EsPublicAcl = EsPublicAcl

    @property
    def KibanaPublicAccess(self):
        r"""Kibana public access status
OPEN: enabled.
-CLOSE: disabled.
        :rtype: str
        """
        return self._KibanaPublicAccess

    @KibanaPublicAccess.setter
    def KibanaPublicAccess(self, KibanaPublicAccess):
        self._KibanaPublicAccess = KibanaPublicAccess

    @property
    def KibanaPrivateAccess(self):
        r"""Kibana internal access status
OPEN: enabled.
-CLOSE: disabled.
        :rtype: str
        """
        return self._KibanaPrivateAccess

    @KibanaPrivateAccess.setter
    def KibanaPrivateAccess(self, KibanaPrivateAccess):
        self._KibanaPrivateAccess = KibanaPrivateAccess

    @property
    def BasicSecurityType(self):
        r"""Turn on or off user authentication for the basic version of ES 6.8 and above
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def KibanaPrivatePort(self):
        r"""Kibana private network port
        :rtype: int
        """
        return self._KibanaPrivatePort

    @KibanaPrivatePort.setter
    def KibanaPrivatePort(self, KibanaPrivatePort):
        self._KibanaPrivatePort = KibanaPrivatePort

    @property
    def ScaleType(self):
        r"""0: Scale out via blue-green change without restarting the cluster (default) 1: Scale out by unmounting disks with a cluster rolling restart
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
        r"""Scenario template type. -1: not enabled. 1: common. 2: log. 3: search
        :rtype: int
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def KibanaConfig(self):
        r"""Kibana configuration item (JSON format string)
        :rtype: str
        """
        return self._KibanaConfig

    @KibanaConfig.setter
    def KibanaConfig(self, KibanaConfig):
        self._KibanaConfig = KibanaConfig

    @property
    def WebNodeTypeInfo(self):
        r"""Visualize node configuration
        :rtype: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        """
        return self._WebNodeTypeInfo

    @WebNodeTypeInfo.setter
    def WebNodeTypeInfo(self, WebNodeTypeInfo):
        self._WebNodeTypeInfo = WebNodeTypeInfo

    @property
    def SwitchPrivateLink(self):
        r"""Switch to the new network architecture
        :rtype: str
        """
        return self._SwitchPrivateLink

    @SwitchPrivateLink.setter
    def SwitchPrivateLink(self, SwitchPrivateLink):
        self._SwitchPrivateLink = SwitchPrivateLink

    @property
    def EnableCerebro(self):
        r"""Enable Cerebro
        :rtype: bool
        """
        return self._EnableCerebro

    @EnableCerebro.setter
    def EnableCerebro(self, EnableCerebro):
        self._EnableCerebro = EnableCerebro

    @property
    def CerebroPublicAccess(self):
        r"""Cerebro public access status
OPEN: enabled.
-CLOSE: disabled.
        :rtype: str
        """
        return self._CerebroPublicAccess

    @CerebroPublicAccess.setter
    def CerebroPublicAccess(self, CerebroPublicAccess):
        self._CerebroPublicAccess = CerebroPublicAccess

    @property
    def CerebroPrivateAccess(self):
        r"""Cerebro private network access status
OPEN: enabled.
-CLOSE: disabled.
        :rtype: str
        """
        return self._CerebroPrivateAccess

    @CerebroPrivateAccess.setter
    def CerebroPrivateAccess(self, CerebroPrivateAccess):
        self._CerebroPrivateAccess = CerebroPrivateAccess

    @property
    def EsConfigSet(self):
        r"""Newly-added or modified configuration group information
        :rtype: :class:`tencentcloud.es.v20180416.models.EsConfigSetInfo`
        """
        return self._EsConfigSet

    @EsConfigSet.setter
    def EsConfigSet(self, EsConfigSet):
        self._EsConfigSet = EsConfigSet

    @property
    def OperationDuration(self):
        r"""Maintenance time slot.
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def KibanaAlteringPublicAccess(self):
        r"""Whether Alerting public network alert output is enabled:
OPEN: enabled.
-CLOSE: disabled.
        :rtype: str
        """
        return self._KibanaAlteringPublicAccess

    @KibanaAlteringPublicAccess.setter
    def KibanaAlteringPublicAccess(self, KibanaAlteringPublicAccess):
        self._KibanaAlteringPublicAccess = KibanaAlteringPublicAccess

    @property
    def KibanaPrivateDomain(self):
        r"""Custom domain name of kibana on the private network
        :rtype: str
        """
        return self._KibanaPrivateDomain

    @KibanaPrivateDomain.setter
    def KibanaPrivateDomain(self, KibanaPrivateDomain):
        self._KibanaPrivateDomain = KibanaPrivateDomain

    @property
    def CerebroPrivateDomain(self):
        r"""Custom domain name of cerebro on the private network
        :rtype: str
        """
        return self._CerebroPrivateDomain

    @CerebroPrivateDomain.setter
    def CerebroPrivateDomain(self, CerebroPrivateDomain):
        self._CerebroPrivateDomain = CerebroPrivateDomain

    @property
    def Protocol(self):
        r"""Change to an https cluster. http is selected by default.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OutboundPublicAcls(self):
        r"""Outbound access details of the node

        :rtype: list of OutboundPublicAcl
        """
        return self._OutboundPublicAcls

    @OutboundPublicAcls.setter
    def OutboundPublicAcls(self, OutboundPublicAcls):
        self._OutboundPublicAcls = OutboundPublicAcls

    @property
    def OutboundPublicAccess(self):
        r"""Outbound access operations of the node
OPEN
-CLOSE: disabled.
        :rtype: str
        """
        return self._OutboundPublicAccess

    @OutboundPublicAccess.setter
    def OutboundPublicAccess(self, OutboundPublicAccess):
        self._OutboundPublicAccess = OutboundPublicAccess

    @property
    def CvmDelayOnlineTime(self):
        r"""Parameter for delayed cvm launch
        :rtype: int
        """
        return self._CvmDelayOnlineTime

    @CvmDelayOnlineTime.setter
    def CvmDelayOnlineTime(self, CvmDelayOnlineTime):
        self._CvmDelayOnlineTime = CvmDelayOnlineTime

    @property
    def ShardAllocationConcurrents(self):
        r"""Number of concurrent shard migrations
        :rtype: int
        """
        return self._ShardAllocationConcurrents

    @ShardAllocationConcurrents.setter
    def ShardAllocationConcurrents(self, ShardAllocationConcurrents):
        self._ShardAllocationConcurrents = ShardAllocationConcurrents

    @property
    def ShardAllocationBytes(self):
        r"""Shard migration concurrency speed
        :rtype: int
        """
        return self._ShardAllocationBytes

    @ShardAllocationBytes.setter
    def ShardAllocationBytes(self, ShardAllocationBytes):
        self._ShardAllocationBytes = ShardAllocationBytes

    @property
    def ReadWriteMode(self):
        r"""Read-write separation mode: -1: not enabled; 1: local read/write separation; 2: remote read/write separation.
        :rtype: int
        """
        return self._ReadWriteMode

    @ReadWriteMode.setter
    def ReadWriteMode(self, ReadWriteMode):
        self._ReadWriteMode = ReadWriteMode

    @property
    def EnableScheduleRecoverGroup(self):
        r"""Whether to enable the placement group async task
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        r"""Placement group async task maintenance time slot
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration

    @property
    def EnableDestroyProtection(self):
        r"""Cluster protection: OPEN: enable, CLOSE: disable
        :rtype: str
        """
        return self._EnableDestroyProtection

    @EnableDestroyProtection.setter
    def EnableDestroyProtection(self, EnableDestroyProtection):
        self._EnableDestroyProtection = EnableDestroyProtection

    @property
    def AutoScaleDiskInfoList(self):
        r"""Auto capacity expansion parameter
        :rtype: list of AutoScaleDiskInfo
        """
        return self._AutoScaleDiskInfoList

    @AutoScaleDiskInfoList.setter
    def AutoScaleDiskInfoList(self, AutoScaleDiskInfoList):
        self._AutoScaleDiskInfoList = AutoScaleDiskInfoList

    @property
    def AutoScaleDiskDeleteNodeTypeList(self):
        r"""Auto-expansion delete parameter
        :rtype: list of str
        """
        return self._AutoScaleDiskDeleteNodeTypeList

    @AutoScaleDiskDeleteNodeTypeList.setter
    def AutoScaleDiskDeleteNodeTypeList(self, AutoScaleDiskDeleteNodeTypeList):
        self._AutoScaleDiskDeleteNodeTypeList = AutoScaleDiskDeleteNodeTypeList

    @property
    def OtherConfig(self):
        r"""Other additional configuration, jvm or yml.
        :rtype: :class:`tencentcloud.es.v20180416.models.OtherConfig`
        """
        return self._OtherConfig

    @OtherConfig.setter
    def OtherConfig(self, OtherConfig):
        self._OtherConfig = OtherConfig


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
        self._KibanaPrivateDomain = params.get("KibanaPrivateDomain")
        self._CerebroPrivateDomain = params.get("CerebroPrivateDomain")
        self._Protocol = params.get("Protocol")
        if params.get("OutboundPublicAcls") is not None:
            self._OutboundPublicAcls = []
            for item in params.get("OutboundPublicAcls"):
                obj = OutboundPublicAcl()
                obj._deserialize(item)
                self._OutboundPublicAcls.append(obj)
        self._OutboundPublicAccess = params.get("OutboundPublicAccess")
        self._CvmDelayOnlineTime = params.get("CvmDelayOnlineTime")
        self._ShardAllocationConcurrents = params.get("ShardAllocationConcurrents")
        self._ShardAllocationBytes = params.get("ShardAllocationBytes")
        self._ReadWriteMode = params.get("ReadWriteMode")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
        self._EnableDestroyProtection = params.get("EnableDestroyProtection")
        if params.get("AutoScaleDiskInfoList") is not None:
            self._AutoScaleDiskInfoList = []
            for item in params.get("AutoScaleDiskInfoList"):
                obj = AutoScaleDiskInfo()
                obj._deserialize(item)
                self._AutoScaleDiskInfoList.append(obj)
        self._AutoScaleDiskDeleteNodeTypeList = params.get("AutoScaleDiskDeleteNodeTypeList")
        if params.get("OtherConfig") is not None:
            self._OtherConfig = OtherConfig()
            self._OtherConfig._deserialize(params.get("OtherConfig"))
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
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order ID
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class UpdatePluginsRequest(AbstractModel):
    r"""UpdatePlugins request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstallPluginList: Name list of plug-ins that needs to be installed
        :type InstallPluginList: list of str
        :param _RemovePluginList: List of plug-in names to uninstall
        :type RemovePluginList: list of str
        :param _ForceRestart: Whether to force restart. Default value: false
        :type ForceRestart: bool
        :param _ForceUpdate: Whether to reinstall. Default value: false
        :type ForceUpdate: bool
        :param _PluginType: 0: System plugin
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
        r"""Name list of plug-ins that needs to be installed
        :rtype: list of str
        """
        return self._InstallPluginList

    @InstallPluginList.setter
    def InstallPluginList(self, InstallPluginList):
        self._InstallPluginList = InstallPluginList

    @property
    def RemovePluginList(self):
        r"""List of plug-in names to uninstall
        :rtype: list of str
        """
        return self._RemovePluginList

    @RemovePluginList.setter
    def RemovePluginList(self, RemovePluginList):
        self._RemovePluginList = RemovePluginList

    @property
    def ForceRestart(self):
        r"""Whether to force restart. Default value: false
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def ForceUpdate(self):
        r"""Whether to reinstall. Default value: false
        :rtype: bool
        """
        return self._ForceUpdate

    @ForceUpdate.setter
    def ForceUpdate(self, ForceUpdate):
        self._ForceUpdate = ForceUpdate

    @property
    def PluginType(self):
        r"""0: System plugin
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


class UpdateRequestTargetNodeTypesRequest(AbstractModel):
    r"""UpdateRequestTargetNodeTypes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TargetNodeTypes: List of target node types that receive requests
        :type TargetNodeTypes: list of str
        """
        self._InstanceId = None
        self._TargetNodeTypes = None

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
    def TargetNodeTypes(self):
        r"""List of target node types that receive requests
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


class UpgradeInstanceRequest(AbstractModel):
    r"""UpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _EsVersion: Target ES version. Valid values: "6.4.3", "6.8.2", "7.5.1", "7.10.1", and "7.14.2".
        :type EsVersion: str
        :param _CheckOnly: Whether to perform an upgrade check only. Default value: false.
        :type CheckOnly: bool
        :param _LicenseType: Target business feature version: <li>oss open source edition</li><li>basic edition</li>Currently used only when upgrading from 5.6.4 to 6.x. Default value: basic
        :type LicenseType: str
        :param _BasicSecurityType: Whether xpack security authentication is enabled for basic version 6.8 (and above versions)<li>1: not enabled</li><li>2: enabled</li>
        :type BasicSecurityType: int
        :param _UpgradeMode: Upgrade method: <li>scale blue-green change</li><li>restart rolling restart</li>Default value: scale
        :type UpgradeMode: str
        :param _CosBackup: Whether to back up the cluster before upgrading the version. By default, no backup is performed.
        :type CosBackup: bool
        :param _SkipCheckForceRestart: In rolling mode, whether to skip the check and perform a forced reboot. Default value: false
        :type SkipCheckForceRestart: bool
        :param _CvmDelayOnlineTime: Parameter for delayed cvm launch
        :type CvmDelayOnlineTime: int
        :param _ShardAllocationConcurrents: Number of concurrent shard migrations
        :type ShardAllocationConcurrents: int
        :param _ShardAllocationBytes: Shard migration concurrency speed
        :type ShardAllocationBytes: int
        :param _EnableScheduleRecoverGroup: Whether to enable the placement group asynchronous task
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: Time period of the async task for the placement group
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        self._InstanceId = None
        self._EsVersion = None
        self._CheckOnly = None
        self._LicenseType = None
        self._BasicSecurityType = None
        self._UpgradeMode = None
        self._CosBackup = None
        self._SkipCheckForceRestart = None
        self._CvmDelayOnlineTime = None
        self._ShardAllocationConcurrents = None
        self._ShardAllocationBytes = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None

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
        r"""Target ES version. Valid values: "6.4.3", "6.8.2", "7.5.1", "7.10.1", and "7.14.2".
        :rtype: str
        """
        return self._EsVersion

    @EsVersion.setter
    def EsVersion(self, EsVersion):
        self._EsVersion = EsVersion

    @property
    def CheckOnly(self):
        r"""Whether to perform an upgrade check only. Default value: false.
        :rtype: bool
        """
        return self._CheckOnly

    @CheckOnly.setter
    def CheckOnly(self, CheckOnly):
        self._CheckOnly = CheckOnly

    @property
    def LicenseType(self):
        r"""Target business feature version: <li>oss open source edition</li><li>basic edition</li>Currently used only when upgrading from 5.6.4 to 6.x. Default value: basic
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def BasicSecurityType(self):
        r"""Whether xpack security authentication is enabled for basic version 6.8 (and above versions)<li>1: not enabled</li><li>2: enabled</li>
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def UpgradeMode(self):
        r"""Upgrade method: <li>scale blue-green change</li><li>restart rolling restart</li>Default value: scale
        :rtype: str
        """
        return self._UpgradeMode

    @UpgradeMode.setter
    def UpgradeMode(self, UpgradeMode):
        self._UpgradeMode = UpgradeMode

    @property
    def CosBackup(self):
        r"""Whether to back up the cluster before upgrading the version. By default, no backup is performed.
        :rtype: bool
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup

    @property
    def SkipCheckForceRestart(self):
        r"""In rolling mode, whether to skip the check and perform a forced reboot. Default value: false
        :rtype: bool
        """
        return self._SkipCheckForceRestart

    @SkipCheckForceRestart.setter
    def SkipCheckForceRestart(self, SkipCheckForceRestart):
        self._SkipCheckForceRestart = SkipCheckForceRestart

    @property
    def CvmDelayOnlineTime(self):
        r"""Parameter for delayed cvm launch
        :rtype: int
        """
        return self._CvmDelayOnlineTime

    @CvmDelayOnlineTime.setter
    def CvmDelayOnlineTime(self, CvmDelayOnlineTime):
        self._CvmDelayOnlineTime = CvmDelayOnlineTime

    @property
    def ShardAllocationConcurrents(self):
        r"""Number of concurrent shard migrations
        :rtype: int
        """
        return self._ShardAllocationConcurrents

    @ShardAllocationConcurrents.setter
    def ShardAllocationConcurrents(self, ShardAllocationConcurrents):
        self._ShardAllocationConcurrents = ShardAllocationConcurrents

    @property
    def ShardAllocationBytes(self):
        r"""Shard migration concurrency speed
        :rtype: int
        """
        return self._ShardAllocationBytes

    @ShardAllocationBytes.setter
    def ShardAllocationBytes(self, ShardAllocationBytes):
        self._ShardAllocationBytes = ShardAllocationBytes

    @property
    def EnableScheduleRecoverGroup(self):
        r"""Whether to enable the placement group asynchronous task
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        r"""Time period of the async task for the placement group
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EsVersion = params.get("EsVersion")
        self._CheckOnly = params.get("CheckOnly")
        self._LicenseType = params.get("LicenseType")
        self._BasicSecurityType = params.get("BasicSecurityType")
        self._UpgradeMode = params.get("UpgradeMode")
        self._CosBackup = params.get("CosBackup")
        self._SkipCheckForceRestart = params.get("SkipCheckForceRestart")
        self._CvmDelayOnlineTime = params.get("CvmDelayOnlineTime")
        self._ShardAllocationConcurrents = params.get("ShardAllocationConcurrents")
        self._ShardAllocationBytes = params.get("ShardAllocationBytes")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
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


class UpgradeLicenseRequest(AbstractModel):
    r"""UpgradeLicense request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _LicenseType: License type<li>oss: open source edition</li><li>basic: basic version</li><li>platinum: platinum version</li>Default value: platinum
        :type LicenseType: str
        :param _AutoVoucher: Indicates whether to use vouchers automatically<li>0: Do not use automatically.</li><li>1: Use automatically.</li>Default value: 0.
        :type AutoVoucher: int
        :param _VoucherIds: Voucher ID list. Only one voucher can be specified.
        :type VoucherIds: list of str
        :param _BasicSecurityType: Whether xpack security authentication is enabled for basic version 6.8 (and above versions)<li>1: not enabled</li><li>2: enabled</li><li>If no parameter is passed, the original status is maintained by default. When passing a parameter, note that it can only change from not enabled to enabled, and cannot change from enabled to not enabled</li>
        :type BasicSecurityType: int
        :param _ForceRestart: Whether to force restart <li>true: force restart</li><li>false: do not force restart</li> Default value: false
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
        r"""License type<li>oss: open source edition</li><li>basic: basic version</li><li>platinum: platinum version</li>Default value: platinum
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def AutoVoucher(self):
        r"""Indicates whether to use vouchers automatically<li>0: Do not use automatically.</li><li>1: Use automatically.</li>Default value: 0.
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""Voucher ID list. Only one voucher can be specified.
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def BasicSecurityType(self):
        r"""Whether xpack security authentication is enabled for basic version 6.8 (and above versions)<li>1: not enabled</li><li>2: enabled</li><li>If no parameter is passed, the original status is maintained by default. When passing a parameter, note that it can only change from not enabled to enabled, and cannot change from enabled to not enabled</li>
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def ForceRestart(self):
        r"""Whether to force restart <li>true: force restart</li><li>false: do not force restart</li> Default value: false
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
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        r"""Order ID
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class WebNodeTypeInfo(AbstractModel):
    r"""Visualize node configuration

    """

    def __init__(self):
        r"""
        :param _NodeNum: Number of nodes to visualize, fixed as 1
        :type NodeNum: int
        :param _NodeType: Visualize node specifications
        :type NodeType: str
        """
        self._NodeNum = None
        self._NodeType = None

    @property
    def NodeNum(self):
        r"""Number of nodes to visualize, fixed as 1
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def NodeType(self):
        r"""Visualize node specifications
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
    r"""Detailed information of availability zones in multi-AZ deployment

    """

    def __init__(self):
        r"""
        :param _Zone: AZ.
        :type Zone: str
        :param _SubnetId: Subnet ID.
        :type SubnetId: str
        :param _Hidden: Whether it is a hidden AZ
        :type Hidden: bool
        """
        self._Zone = None
        self._SubnetId = None
        self._Hidden = None

    @property
    def Zone(self):
        r"""AZ.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        r"""Subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Hidden(self):
        r"""Whether it is a hidden AZ
        :rtype: bool
        """
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        self._Hidden = params.get("Hidden")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        