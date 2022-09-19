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


class ApplyResult(AbstractModel):
    """Application update results

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param ApplicationType: Application type
        :type ApplicationType: int
        :param ApplicationStatus: Status. Valid values: `0` (pending approval), `1` (application approved and task submitted), `2` (rejected)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplicationStatus: int
        :param TaskId: ID of the submitted task
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskId: str
        :param Error: Error information
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self.ApplicationId = None
        self.ApplicationType = None
        self.ApplicationStatus = None
        self.TaskId = None
        self.Error = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationType = params.get("ApplicationType")
        self.ApplicationStatus = params.get("ApplicationStatus")
        self.TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyStatus(AbstractModel):
    """Application ID and status

    """

    def __init__(self):
        r"""
        :param ApplicationId: Value format: cluster ID-application ID
        :type ApplicationId: str
        :param ApplicationStatus: Status. Valid values: `-1` (canceled), `0` (pending approval), `1` (application approved and task submitted), `2` (rejected). Only applications in the pending approval status can be updated.
        :type ApplicationStatus: int
        :param ApplicationType: Application type
        :type ApplicationType: int
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ApplicationId = None
        self.ApplicationStatus = None
        self.ApplicationType = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationStatus = params.get("ApplicationStatus")
        self.ApplicationType = params.get("ApplicationType")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearTablesRequest(AbstractModel):
    """ClearTables request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster instance where a table resides
        :type ClusterId: str
        :param SelectedTables: List of information of tables to be cleared
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearTablesResponse(AbstractModel):
    """ClearTables response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of cleared tables
        :type TotalCount: int
        :param TableResults: List of table clearing results
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ClusterInfo(AbstractModel):
    """Cluster details

    """

    def __init__(self):
        r"""
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Region: Cluster region
        :type Region: str
        :param IdlType: Cluster data description language type, such as `PROTO`, `TDR`, or `MIX`
        :type IdlType: str
        :param NetworkType: Network type
        :type NetworkType: str
        :param VpcId: ID of the VPC instance with which a cluster is associated
        :type VpcId: str
        :param SubnetId: ID of the subnet instance with which a cluster is associated
        :type SubnetId: str
        :param CreatedTime: Creation time
        :type CreatedTime: str
        :param Password: Cluster password
        :type Password: str
        :param PasswordStatus: Password status
        :type PasswordStatus: str
        :param ApiAccessId: TcaplusDB SDK connection parameter: access ID
        :type ApiAccessId: str
        :param ApiAccessIp: TcaplusDB SDK connection parameter: access address
        :type ApiAccessIp: str
        :param ApiAccessPort: TcaplusDB SDK connection parameter: access port
        :type ApiAccessPort: int
        :param OldPasswordExpireTime: If `PasswordStatus` is `unmodifiable`, the old password has not expired, and this field will display its expiration time; otherwise, this field will be empty
Note: this field may return null, indicating that no valid values can be obtained.
        :type OldPasswordExpireTime: str
        :param ApiAccessIpv6: TcaplusDB SDK connection parameter for accessing IPv6 addresses
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAccessIpv6: str
        :param ClusterType: Cluster type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClusterType: int
        :param ClusterStatus: Cluster status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClusterStatus: int
        :param ReadCapacityUnit: Read CU
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReadCapacityUnit: int
        :param WriteCapacityUnit: Write CU
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WriteCapacityUnit: int
        :param DiskVolume: Disk capacity
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiskVolume: int
        :param ServerList: Information of the machine at the storage layer (tcapsvr) in a dedicated cluster
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ServerList: list of ServerDetailInfo
        :param ProxyList: Information of the machine at the access layer (tcaproxy) in a dedicated cluster
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProxyList: list of ProxyDetailInfo
        :param Censorship: Whether the cluster operation approval feature is enabled. Valid values: `0` (disabled), `1` (enabled)
        :type Censorship: int
        :param DbaUins: Approver UIN list
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type DbaUins: list of str
        :param DataFlowStatus: Whether data subscription is enabled
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DataFlowStatus: int
        :param KafkaInfo: CKafka information when data subscription is enabled
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type KafkaInfo: :class:`tencentcloud.tcaplusdb.v20190823.models.KafkaInfo`
        :param TxhBackupExpireDay: The number of days after which the cluster Txh backup file will expire and be deleted.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TxhBackupExpireDay: int
        :param UlogBackupExpireDay: The number of days after which the cluster Ulog backup file will expire and be deleted.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UlogBackupExpireDay: int
        :param IsReadOnlyUlogBackupExpireDay: Whether the expiration policy of cluster Ulog backup file is read-only. `0`: Yes; `1`: No.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsReadOnlyUlogBackupExpireDay: int
        """
        self.ClusterName = None
        self.ClusterId = None
        self.Region = None
        self.IdlType = None
        self.NetworkType = None
        self.VpcId = None
        self.SubnetId = None
        self.CreatedTime = None
        self.Password = None
        self.PasswordStatus = None
        self.ApiAccessId = None
        self.ApiAccessIp = None
        self.ApiAccessPort = None
        self.OldPasswordExpireTime = None
        self.ApiAccessIpv6 = None
        self.ClusterType = None
        self.ClusterStatus = None
        self.ReadCapacityUnit = None
        self.WriteCapacityUnit = None
        self.DiskVolume = None
        self.ServerList = None
        self.ProxyList = None
        self.Censorship = None
        self.DbaUins = None
        self.DataFlowStatus = None
        self.KafkaInfo = None
        self.TxhBackupExpireDay = None
        self.UlogBackupExpireDay = None
        self.IsReadOnlyUlogBackupExpireDay = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.ClusterId = params.get("ClusterId")
        self.Region = params.get("Region")
        self.IdlType = params.get("IdlType")
        self.NetworkType = params.get("NetworkType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CreatedTime = params.get("CreatedTime")
        self.Password = params.get("Password")
        self.PasswordStatus = params.get("PasswordStatus")
        self.ApiAccessId = params.get("ApiAccessId")
        self.ApiAccessIp = params.get("ApiAccessIp")
        self.ApiAccessPort = params.get("ApiAccessPort")
        self.OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self.ApiAccessIpv6 = params.get("ApiAccessIpv6")
        self.ClusterType = params.get("ClusterType")
        self.ClusterStatus = params.get("ClusterStatus")
        self.ReadCapacityUnit = params.get("ReadCapacityUnit")
        self.WriteCapacityUnit = params.get("WriteCapacityUnit")
        self.DiskVolume = params.get("DiskVolume")
        if params.get("ServerList") is not None:
            self.ServerList = []
            for item in params.get("ServerList"):
                obj = ServerDetailInfo()
                obj._deserialize(item)
                self.ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyDetailInfo()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        self.Censorship = params.get("Censorship")
        self.DbaUins = params.get("DbaUins")
        self.DataFlowStatus = params.get("DataFlowStatus")
        if params.get("KafkaInfo") is not None:
            self.KafkaInfo = KafkaInfo()
            self.KafkaInfo._deserialize(params.get("KafkaInfo"))
        self.TxhBackupExpireDay = params.get("TxhBackupExpireDay")
        self.UlogBackupExpireDay = params.get("UlogBackupExpireDay")
        self.IsReadOnlyUlogBackupExpireDay = params.get("IsReadOnlyUlogBackupExpireDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareIdlFilesRequest(AbstractModel):
    """CompareIdlFiles request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table to be modified resides
        :type ClusterId: str
        :param SelectedTables: List of tables to be modified
        :type SelectedTables: list of SelectedTableInfoNew
        :param ExistingIdlFiles: Selected list of uploaded IDL files. Either this parameter or `NewIdlFiles` must be selected
        :type ExistingIdlFiles: list of IdlFileInfo
        :param NewIdlFiles: List of IDL files to be uploaded. Either this parameter or `ExistingIdlFiles` must be selected
        :type NewIdlFiles: list of IdlFileInfo
        """
        self.ClusterId = None
        self.SelectedTables = None
        self.ExistingIdlFiles = None
        self.NewIdlFiles = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        if params.get("ExistingIdlFiles") is not None:
            self.ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self.NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.NewIdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareIdlFilesResponse(AbstractModel):
    """CompareIdlFiles response structure.

    """

    def __init__(self):
        r"""
        :param IdlFiles: Information list of all IDL files uploaded and verified in this request
        :type IdlFiles: list of IdlFileInfo
        :param TotalCount: Number of tables verified to be valid in this request
        :type TotalCount: int
        :param TableInfos: Verification result parsed from the selected table after the IDL description file is read
        :type TableInfos: list of ParsedTableInfoNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IdlFiles = None
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class CompareTablesInfo(AbstractModel):
    """Compare the meta information of two tables

    """

    def __init__(self):
        r"""
        :param SrcTableClusterId: Cluster ID of the source table
        :type SrcTableClusterId: str
        :param SrcTableGroupId: Table group ID of the source table
        :type SrcTableGroupId: str
        :param SrcTableName: Source table name
        :type SrcTableName: str
        :param DstTableClusterId: Cluster ID of the target table
        :type DstTableClusterId: str
        :param DstTableGroupId: Table group ID of the target table
        :type DstTableGroupId: str
        :param DstTableName: Target table name
        :type DstTableName: str
        :param SrcTableInstanceId: Source table ID
        :type SrcTableInstanceId: str
        :param DstTableInstanceId: Target table ID
        :type DstTableInstanceId: str
        """
        self.SrcTableClusterId = None
        self.SrcTableGroupId = None
        self.SrcTableName = None
        self.DstTableClusterId = None
        self.DstTableGroupId = None
        self.DstTableName = None
        self.SrcTableInstanceId = None
        self.DstTableInstanceId = None


    def _deserialize(self, params):
        self.SrcTableClusterId = params.get("SrcTableClusterId")
        self.SrcTableGroupId = params.get("SrcTableGroupId")
        self.SrcTableName = params.get("SrcTableName")
        self.DstTableClusterId = params.get("DstTableClusterId")
        self.DstTableGroupId = params.get("DstTableGroupId")
        self.DstTableName = params.get("DstTableName")
        self.SrcTableInstanceId = params.get("SrcTableInstanceId")
        self.DstTableInstanceId = params.get("DstTableInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table to be backed up resides
        :type ClusterId: str
        :param SelectedTables: Information list of tables to be backed up
        :type SelectedTables: list of SelectedTableInfoNew
        :param Remark: Remarks
        :type Remark: str
        """
        self.ClusterId = None
        self.SelectedTables = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup response structure.

    """

    def __init__(self):
        r"""
        :param TaskIds: List of backup creation task IDs
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskIds: list of str
        :param ApplicationIds: List of backup creation application IDs
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplicationIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskIds = None
        self.ApplicationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.ApplicationIds = params.get("ApplicationIds")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster request structure.

    """

    def __init__(self):
        r"""
        :param IdlType: Cluster data description language type, such as `PROTO`, `TDR`, or `MIX`
        :type IdlType: str
        :param ClusterName: Cluster name, which can contain up to 32 letters and digits
        :type ClusterName: str
        :param VpcId: ID of the VPC instance bound to a cluster in the format of `vpc-f49l6u0z`
        :type VpcId: str
        :param SubnetId: ID of the subnet instance bound to a cluster in the format of `subnet-pxir56ns`
        :type SubnetId: str
        :param Password: Cluster access password, which must contain lowercase letters (a-z), uppercase letters (A-Z), and digits (0-9).
        :type Password: str
        :param ResourceTags: Cluster tag list
        :type ResourceTags: list of TagInfoUnit
        :param Ipv6Enable: Whether to enable IPv6 address access for clusters
        :type Ipv6Enable: int
        :param ServerList: Information of the machine at the storage layer (tcapsvr) in a dedicated cluster
        :type ServerList: list of MachineInfo
        :param ProxyList: Information of the machine at the access layer (tcaproxy) in a dedicated cluster
        :type ProxyList: list of MachineInfo
        :param ClusterType: Cluster type. Valid values: `1` (standard), `2` (dedicated)
        :type ClusterType: int
        :param AuthType: Authentication type. Valid values: `0` (static password), `1` (signature)
        :type AuthType: int
        """
        self.IdlType = None
        self.ClusterName = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.ResourceTags = None
        self.Ipv6Enable = None
        self.ServerList = None
        self.ProxyList = None
        self.ClusterType = None
        self.AuthType = None


    def _deserialize(self, params):
        self.IdlType = params.get("IdlType")
        self.ClusterName = params.get("ClusterName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.Ipv6Enable = params.get("Ipv6Enable")
        if params.get("ServerList") is not None:
            self.ServerList = []
            for item in params.get("ServerList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        self.ClusterType = params.get("ClusterType")
        self.AuthType = params.get("AuthType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateSnapshotsRequest(AbstractModel):
    """CreateSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where the table resides
        :type ClusterId: str
        :param SelectedTables: Snapshot list
        :type SelectedTables: list of SnapshotInfo
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotsResponse(AbstractModel):
    """CreateSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of snapshots created in batches
        :type TotalCount: int
        :param TableResults: The result list of snapshots created in batches
        :type TableResults: list of SnapshotResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class CreateTableGroupRequest(AbstractModel):
    """CreateTableGroup request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where a table group resides
        :type ClusterId: str
        :param TableGroupName: Table group name, which can contain up to 32 letters and digits
        :type TableGroupName: str
        :param TableGroupId: Table group ID, which can be customized but must be unique in one cluster. If it is not specified, the auto-increment mode will be used.
        :type TableGroupId: str
        :param ResourceTags: Table group tag list
        :type ResourceTags: list of TagInfoUnit
        """
        self.ClusterId = None
        self.TableGroupName = None
        self.TableGroupId = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupName = params.get("TableGroupName")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTableGroupResponse(AbstractModel):
    """CreateTableGroup response structure.

    """

    def __init__(self):
        r"""
        :param TableGroupId: ID of table group successfully created
        :type TableGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TableGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.RequestId = params.get("RequestId")


class CreateTablesRequest(AbstractModel):
    """CreateTables request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where to create a table
        :type ClusterId: str
        :param IdlFiles: Table creation IDL file list selected by user
        :type IdlFiles: list of IdlFileInfo
        :param SelectedTables: Information list of tables to be created
        :type SelectedTables: list of SelectedTableInfoNew
        :param ResourceTags: Table tag list
        :type ResourceTags: list of TagInfoUnit
        """
        self.ClusterId = None
        self.IdlFiles = None
        self.SelectedTables = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTablesResponse(AbstractModel):
    """CreateTables response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of tables created in batches
        :type TotalCount: int
        :param TableResults: List of tables created in batches
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of cluster to be deleted
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID generated by cluster deletion
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteIdlFilesRequest(AbstractModel):
    """DeleteIdlFiles request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where IDL resides
        :type ClusterId: str
        :param IdlFiles: List of information of IDL files to be deleted
        :type IdlFiles: list of IdlFileInfo
        """
        self.ClusterId = None
        self.IdlFiles = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIdlFilesResponse(AbstractModel):
    """DeleteIdlFiles response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of returned results
        :type TotalCount: int
        :param IdlFileInfos: Deletion result
        :type IdlFileInfos: list of IdlFileInfoWithoutContent
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.IdlFileInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("IdlFileInfos") is not None:
            self.IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfoWithoutContent()
                obj._deserialize(item)
                self.IdlFileInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where the table resides
        :type ClusterId: str
        :param SelectedTables: The list of snapshots to delete
        :type SelectedTables: list of SnapshotInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of snapshots deleted in batches
        :type TotalCount: int
        :param TableResults: The result list of snapshots deleted in batches
        :type TableResults: list of SnapshotResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteTableDataFlowRequest(AbstractModel):
    """DeleteTableDataFlow request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where the tables reside
        :type ClusterId: str
        :param SelectedTables: The list of tables for which data subscription will be disabled
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableDataFlowResponse(AbstractModel):
    """DeleteTableDataFlow response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of tables for which data subscription has been disabled
        :type TotalCount: int
        :param TableResults: The result list of tables for which data subscription has been disabled
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteTableGroupRequest(AbstractModel):
    """DeleteTableGroup request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where a table group resides
        :type ClusterId: str
        :param TableGroupId: Table group ID
        :type TableGroupId: str
        """
        self.ClusterId = None
        self.TableGroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableGroupResponse(AbstractModel):
    """DeleteTableGroup response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID generated by table group deletion
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteTableIndexRequest(AbstractModel):
    """DeleteTableIndex request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table resides
        :type ClusterId: str
        :param SelectedTables: The list of tables whose global indexes need to be deleted
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableIndexResponse(AbstractModel):
    """DeleteTableIndex response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of tables whose global indexes are deleted
        :type TotalCount: int
        :param TableResults: The list of global index deletion results
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteTablesRequest(AbstractModel):
    """DeleteTables request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table to be dropped resides
        :type ClusterId: str
        :param SelectedTables: List of information of tables to be dropped
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTablesResponse(AbstractModel):
    """DeleteTables response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of dropped tables
        :type TotalCount: int
        :param TableResults: List of details of dropped tables
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterTagsRequest(AbstractModel):
    """DescribeClusterTags request structure.

    """

    def __init__(self):
        r"""
        :param ClusterIds: The list of cluster IDs
        :type ClusterIds: list of str
        """
        self.ClusterIds = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterTagsResponse(AbstractModel):
    """DescribeClusterTags response structure.

    """

    def __init__(self):
        r"""
        :param Rows: The information list of cluster tags
        :type Rows: list of TagsInfoOfCluster
        :param TotalCount: The number of returned results
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rows = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfCluster()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        r"""
        :param ClusterIds: List of IDs of clusters to be queried
        :type ClusterIds: list of str
        :param Filters: Query filter
        :type Filters: list of Filter
        :param Offset: Query list offset
        :type Offset: int
        :param Limit: Number of returned results in query list. Default value: 20
        :type Limit: int
        :param Ipv6Enable: Whether to enable IPv6 address access
        :type Ipv6Enable: int
        """
        self.ClusterIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Ipv6Enable = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of cluster instances
        :type TotalCount: int
        :param Clusters: Cluster instance list
        :type Clusters: list of ClusterInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Clusters = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIdlFileInfosRequest(AbstractModel):
    """DescribeIdlFileInfos request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where a file resides
        :type ClusterId: str
        :param TableGroupIds: ID of the table group where a file resides
        :type TableGroupIds: list of str
        :param IdlFileIds: File ID list
        :type IdlFileIds: list of str
        :param Offset: Query list offset
        :type Offset: int
        :param Limit: Number of returned results in query list
        :type Limit: int
        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.IdlFileIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        self.IdlFileIds = params.get("IdlFileIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdlFileInfosResponse(AbstractModel):
    """DescribeIdlFileInfos response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of files
        :type TotalCount: int
        :param IdlFileInfos: List of file details
        :type IdlFileInfos: list of IdlFileInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.IdlFileInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("IdlFileInfos") is not None:
            self.IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFileInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineRequest(AbstractModel):
    """DescribeMachine request structure.

    """

    def __init__(self):
        r"""
        :param Ipv6Enable: If this parameter is not `0`, machines supporting IPv6 will be queried.
        :type Ipv6Enable: int
        """
        self.Ipv6Enable = None


    def _deserialize(self, params):
        self.Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineResponse(AbstractModel):
    """DescribeMachine response structure.

    """

    def __init__(self):
        r"""
        :param PoolList: The list of dedicated machine resources
        :type PoolList: list of PoolInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PoolList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PoolList") is not None:
            self.PoolList = []
            for item in params.get("PoolList"):
                obj = PoolInfo()
                obj._deserialize(item)
                self.PoolList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of queried AZs
        :type TotalCount: int
        :param RegionInfos: List of AZ query results
        :type RegionInfos: list of RegionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionInfos") is not None:
            self.RegionInfos = []
            for item in params.get("RegionInfos"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where the table resides
        :type ClusterId: str
        :param TableGroupId: The ID of the table group where the table resides
        :type TableGroupId: str
        :param TableName: Table name
        :type TableName: str
        :param SnapshotName: Snapshot name
        :type SnapshotName: str
        """
        self.ClusterId = None
        self.TableGroupId = None
        self.TableName = None
        self.SnapshotName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of snapshots
        :type TotalCount: int
        :param TableResults: The result list of snapshots
        :type TableResults: list of SnapshotResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableGroupTagsRequest(AbstractModel):
    """DescribeTableGroupTags request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where table group tags need to be queried
        :type ClusterId: str
        :param TableGroupIds: The list of IDs of the table groups whose tags need to be queried
        :type TableGroupIds: list of str
        """
        self.ClusterId = None
        self.TableGroupIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableGroupTagsResponse(AbstractModel):
    """DescribeTableGroupTags response structure.

    """

    def __init__(self):
        r"""
        :param Rows: The information list of table group tags
        :type Rows: list of TagsInfoOfTableGroup
        :param TotalCount: The number of returned results
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rows = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfTableGroup()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTableGroupsRequest(AbstractModel):
    """DescribeTableGroups request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where a table group resides
        :type ClusterId: str
        :param TableGroupIds: Table group ID list
        :type TableGroupIds: list of str
        :param Filters: Filter. Valid values: TableGroupName, TableGroupId
        :type Filters: list of Filter
        :param Offset: Query list offset
        :type Offset: int
        :param Limit: Number of returned results in query list
        :type Limit: int
        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableGroupsResponse(AbstractModel):
    """DescribeTableGroups response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of table groups
        :type TotalCount: int
        :param TableGroups: Table group information list
        :type TableGroups: list of TableGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableGroups") is not None:
            self.TableGroups = []
            for item in params.get("TableGroups"):
                obj = TableGroupInfo()
                obj._deserialize(item)
                self.TableGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableTagsRequest(AbstractModel):
    """DescribeTableTags request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where a table resides
        :type ClusterId: str
        :param SelectedTables: Table list
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableTagsResponse(AbstractModel):
    """DescribeTableTags response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The total number of returned results
        :type TotalCount: int
        :param Rows: The information list of table tags
        :type Rows: list of TagsInfoOfTable
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfTable()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesInRecycleRequest(AbstractModel):
    """DescribeTablesInRecycle request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table to be queried resides
        :type ClusterId: str
        :param TableGroupIds: List of IDs of the table groups where the table to be queried resides
        :type TableGroupIds: list of str
        :param Filters: Filter. Valid values: TableName, TableInstanceId
        :type Filters: list of Filter
        :param Offset: Query result offset
        :type Offset: int
        :param Limit: Number of returned query results
        :type Limit: int
        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesInRecycleResponse(AbstractModel):
    """DescribeTablesInRecycle response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of tables
        :type TotalCount: int
        :param TableInfos: Table details result list
        :type TableInfos: list of TableInfoNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table to be queried resides
        :type ClusterId: str
        :param TableGroupIds: List of IDs of the table groups where the table to be queried resides
        :type TableGroupIds: list of str
        :param SelectedTables: Information list of tables to be queried
        :type SelectedTables: list of SelectedTableInfoNew
        :param Filters: Filter. Valid values: TableName, TableInstanceId
        :type Filters: list of Filter
        :param Offset: Query result offset
        :type Offset: int
        :param Limit: Number of returned query results
        :type Limit: int
        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.SelectedTables = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of tables
        :type TotalCount: int
        :param TableInfos: Table details result list
        :type TableInfos: list of TableInfoNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks request structure.

    """

    def __init__(self):
        r"""
        :param ClusterIds: List of IDs of clusters where the tasks to be queried reside
        :type ClusterIds: list of str
        :param TaskIds: List of IDs of tasks to be queried
        :type TaskIds: list of str
        :param Filters: Filter. Valid values: Content, TaskType, Operator, Time
        :type Filters: list of Filter
        :param Offset: Query list offset
        :type Offset: int
        :param Limit: Number of returned results in query list
        :type Limit: int
        """
        self.ClusterIds = None
        self.TaskIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        self.TaskIds = params.get("TaskIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        :param TotalCount: Number of tasks
        :type TotalCount: int
        :param TaskInfos: List of details of queried tasks
        :type TaskInfos: list of TaskInfoNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = TaskInfoNew()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUinInWhitelistRequest(AbstractModel):
    """DescribeUinInWhitelist request structure.

    """


class DescribeUinInWhitelistResponse(AbstractModel):
    """DescribeUinInWhitelist response structure.

    """

    def __init__(self):
        r"""
        :param Result: Query result. FALSE: yes, TRUE: no
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableRestProxyRequest(AbstractModel):
    """DisableRestProxy request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The value is the same as `appid`.
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRestProxyResponse(AbstractModel):
    """DisableRestProxy response structure.

    """

    def __init__(self):
        r"""
        :param RestProxyStatus: RestProxy status. Valid values: 0 (disabled), 1 (enabling), 2 (enabled), 3 (disabling).
        :type RestProxyStatus: int
        :param TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, used to identify tasks of different clusters.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RestProxyStatus = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RestProxyStatus = params.get("RestProxyStatus")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EnableRestProxyRequest(AbstractModel):
    """EnableRestProxy request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The value is the same as `appid`.
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRestProxyResponse(AbstractModel):
    """EnableRestProxy response structure.

    """

    def __init__(self):
        r"""
        :param RestProxyStatus: RestProxy status. Valid values: 0 (disabled), 1 (enabling), 2 (enabled), 3 (disabling).
        :type RestProxyStatus: int
        :param TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, used to identify tasks of different clusters.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RestProxyStatus = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RestProxyStatus = params.get("RestProxyStatus")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ErrorInfo(AbstractModel):
    """Describes the details of errors that may occur during the processing of each instance (application, region, or table).

    """

    def __init__(self):
        r"""
        :param Code: Error code
        :type Code: str
        :param Message: Error message
        :type Message: str
        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FieldInfo(AbstractModel):
    """The list of table field information

    """

    def __init__(self):
        r"""
        :param FieldName: Table field name
        :type FieldName: str
        :param IsPrimaryKey: Whether it is a primary key field
        :type IsPrimaryKey: str
        :param FieldType: Field type
        :type FieldType: str
        :param FieldSize: Field length
        :type FieldSize: int
        """
        self.FieldName = None
        self.IsPrimaryKey = None
        self.FieldType = None
        self.FieldSize = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.IsPrimaryKey = params.get("IsPrimaryKey")
        self.FieldType = params.get("FieldType")
        self.FieldSize = params.get("FieldSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        r"""
        :param Name: Filter field name
        :type Name: str
        :param Value: Filter field value
        :type Value: str
        :param Values: Filter field value
        :type Values: list of str
        """
        self.Name = None
        self.Value = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdlFileInfo(AbstractModel):
    """Table definition file details, including file content

    """

    def __init__(self):
        r"""
        :param FileName: Filename excluding extension
        :type FileName: str
        :param FileType: Data interface description language (IDL) type
        :type FileType: str
        :param FileExtType: File extension
        :type FileExtType: str
        :param FileSize: File size in bytes
        :type FileSize: int
        :param FileId: File ID, which is meaningful for files already uploaded
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileId: int
        :param FileContent: File content, which is meaningful for files to be uploaded in this request
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileContent: str
        """
        self.FileName = None
        self.FileType = None
        self.FileExtType = None
        self.FileSize = None
        self.FileId = None
        self.FileContent = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.FileExtType = params.get("FileExtType")
        self.FileSize = params.get("FileSize")
        self.FileId = params.get("FileId")
        self.FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdlFileInfoWithoutContent(AbstractModel):
    """Table definition file details, excluding file content

    """

    def __init__(self):
        r"""
        :param FileName: Filename excluding extension
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileName: str
        :param FileType: Data interface description language (IDL) type
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileType: str
        :param FileExtType: File extension
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileExtType: str
        :param FileSize: File size in bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileSize: int
        :param FileId: File ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileId: int
        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self.FileName = None
        self.FileType = None
        self.FileExtType = None
        self.FileSize = None
        self.FileId = None
        self.Error = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.FileExtType = params.get("FileExtType")
        self.FileSize = params.get("FileSize")
        self.FileId = params.get("FileId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSnapshotsRequest(AbstractModel):
    """ImportSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where the original table (from which the snapshot was created) resides
        :type ClusterId: str
        :param Snapshots: The information of the snapshot to import
        :type Snapshots: :class:`tencentcloud.tcaplusdb.v20190823.models.SnapshotInfo`
        :param ImportSpecialKey: Whether to import partial data of the snapshot. Valid values: `TRUE` (import partial data), `FALSE` (import all data).
        :type ImportSpecialKey: str
        :param ImportOriginTable: Whether to import to the original table. Valid values: `TRUE` (import to the original table), `FALSE` (import to a new table).
        :type ImportOriginTable: str
        :param KeyFile: The file of the keys of the partial data
        :type KeyFile: :class:`tencentcloud.tcaplusdb.v20190823.models.KeyFile`
        :param NewTableGroupId: The ID of the table group where the new table resides, which is valid only when `ImportOriginTable` is set to `FALSE`
        :type NewTableGroupId: str
        :param NewTableName: The name of the new table, which is valid only when `ImportOriginTable` is set to `FALSE`. TcaplusDB will automatically create a table named `NewTableName` of the same structure as that of the original table.
        :type NewTableName: str
        """
        self.ClusterId = None
        self.Snapshots = None
        self.ImportSpecialKey = None
        self.ImportOriginTable = None
        self.KeyFile = None
        self.NewTableGroupId = None
        self.NewTableName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Snapshots") is not None:
            self.Snapshots = SnapshotInfo()
            self.Snapshots._deserialize(params.get("Snapshots"))
        self.ImportSpecialKey = params.get("ImportSpecialKey")
        self.ImportOriginTable = params.get("ImportOriginTable")
        if params.get("KeyFile") is not None:
            self.KeyFile = KeyFile()
            self.KeyFile._deserialize(params.get("KeyFile"))
        self.NewTableGroupId = params.get("NewTableGroupId")
        self.NewTableName = params.get("NewTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSnapshotsResponse(AbstractModel):
    """ImportSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, used to identify tasks of different clusters.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class KafkaInfo(AbstractModel):
    """CKafka address

    """

    def __init__(self):
        r"""
        :param Address: CKafka address
        :type Address: str
        :param Topic: CKafka topic
        :type Topic: str
        :param User: CKafka username
        :type User: str
        :param Password: CKafka password
        :type Password: str
        :param Instance: CKafka instance
        :type Instance: str
        :param IsVpc: Whether VPC access is enabled
        :type IsVpc: int
        """
        self.Address = None
        self.Topic = None
        self.User = None
        self.Password = None
        self.Instance = None
        self.IsVpc = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Topic = params.get("Topic")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.Instance = params.get("Instance")
        self.IsVpc = params.get("IsVpc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyFile(AbstractModel):
    """The file of keys used to import partial snapshot data

    """

    def __init__(self):
        r"""
        :param FileName: Key file name
        :type FileName: str
        :param FileExtType: Key file extension
        :type FileExtType: str
        :param FileContent: Key file content
        :type FileContent: str
        :param FileSize: Key file size
        :type FileSize: int
        """
        self.FileName = None
        self.FileExtType = None
        self.FileContent = None
        self.FileSize = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileExtType = params.get("FileExtType")
        self.FileContent = params.get("FileContent")
        self.FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineInfo(AbstractModel):
    """Machine type and quantity

    """

    def __init__(self):
        r"""
        :param MachineType: Machine type
        :type MachineType: str
        :param MachineNum: Machine quantity
        :type MachineNum: int
        """
        self.MachineType = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTableResult(AbstractModel):
    """Table merging results

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskId: str
        :param Error: If table merging is successful, `null` will be returned
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param Table: Comparison results of tables
        :type Table: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`
        :param ApplicationId: Application ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplicationId: str
        """
        self.TaskId = None
        self.Error = None
        self.Table = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        if params.get("Table") is not None:
            self.Table = CompareTablesInfo()
            self.Table._deserialize(params.get("Table"))
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTablesDataRequest(AbstractModel):
    """MergeTablesData request structure.

    """

    def __init__(self):
        r"""
        :param SelectedTables: Tables to be merged
        :type SelectedTables: list of MergeTablesInfo
        :param IsOnlyCompare: Valid values: `true` (only compare), `false` (compare and merge)
        :type IsOnlyCompare: bool
        """
        self.SelectedTables = None
        self.IsOnlyCompare = None


    def _deserialize(self, params):
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = MergeTablesInfo()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        self.IsOnlyCompare = params.get("IsOnlyCompare")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTablesDataResponse(AbstractModel):
    """MergeTablesData response structure.

    """

    def __init__(self):
        r"""
        :param Results: Table merging results
        :type Results: list of MergeTableResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = MergeTableResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class MergeTablesInfo(AbstractModel):
    """Request parameters used to merge tables

    """

    def __init__(self):
        r"""
        :param MergeTables: Information of tables to be merged
        :type MergeTables: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`
        :param CheckIndex: Whether to check indexes
        :type CheckIndex: bool
        """
        self.MergeTables = None
        self.CheckIndex = None


    def _deserialize(self, params):
        if params.get("MergeTables") is not None:
            self.MergeTables = CompareTablesInfo()
            self.MergeTables._deserialize(params.get("MergeTables"))
        self.CheckIndex = params.get("CheckIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCensorshipRequest(AbstractModel):
    """ModifyCensorship request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Censorship: Whether to enable the operation approval feature for this cluster. Valid values: `0` (disable), `1` (enable)
        :type Censorship: int
        :param Uins: Approver UIN list
        :type Uins: list of str
        """
        self.ClusterId = None
        self.Censorship = None
        self.Uins = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Censorship = params.get("Censorship")
        self.Uins = params.get("Uins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCensorshipResponse(AbstractModel):
    """ModifyCensorship response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Uins: Approver UIN list
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Uins: list of str
        :param Censorship: Whether the operation approval feature is enabled for this cluster. Valid values: `0` (disabled), `1` (enabled)
        :type Censorship: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.Uins = None
        self.Censorship = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Uins = params.get("Uins")
        self.Censorship = params.get("Censorship")
        self.RequestId = params.get("RequestId")


class ModifyClusterMachineRequest(AbstractModel):
    """ModifyClusterMachine request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ServerList: Information of the machines at the storage layer (tcapsvr)
        :type ServerList: list of MachineInfo
        :param ProxyList: Information of the machines at the access layer (tcaproxy)
        :type ProxyList: list of MachineInfo
        :param ClusterType: Cluster type. Valid values: `1` (standard), `2` (dedicated)
        :type ClusterType: int
        """
        self.ClusterId = None
        self.ServerList = None
        self.ProxyList = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ServerList") is not None:
            self.ServerList = []
            for item in params.get("ServerList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        self.ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterMachineResponse(AbstractModel):
    """ModifyClusterMachine response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster to be renamed
        :type ClusterId: str
        :param ClusterName: Cluster name to be changed to, which can contain up to 32 letters and digits
        :type ClusterName: str
        """
        self.ClusterId = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterPasswordRequest(AbstractModel):
    """ModifyClusterPassword request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster for which to modify the password
        :type ClusterId: str
        :param OldPassword: Old cluster password
        :type OldPassword: str
        :param OldPasswordExpireTime: Expected expiration time of old cluster password
        :type OldPasswordExpireTime: str
        :param NewPassword: New cluster password, which must contain lowercase letters (a-z), uppercase letters (A-Z), and digits (0-9).
        :type NewPassword: str
        :param Mode: Update mode. 1: updates password, 2: updates old password expiration time. Default value: 1
        :type Mode: str
        """
        self.ClusterId = None
        self.OldPassword = None
        self.OldPasswordExpireTime = None
        self.NewPassword = None
        self.Mode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.OldPassword = params.get("OldPassword")
        self.OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self.NewPassword = params.get("NewPassword")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterPasswordResponse(AbstractModel):
    """ModifyClusterPassword response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterTagsRequest(AbstractModel):
    """ModifyClusterTags request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster whose tags need to be modified
        :type ClusterId: str
        :param ReplaceTags: The list of tags to add or modify
        :type ReplaceTags: list of TagInfoUnit
        :param DeleteTags: Tags to delete
        :type DeleteTags: list of TagInfoUnit
        """
        self.ClusterId = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterTagsResponse(AbstractModel):
    """ModifyClusterTags response structure.

    """

    def __init__(self):
        r"""
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


class ModifySnapshotsRequest(AbstractModel):
    """ModifySnapshots request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where the table resides
        :type ClusterId: str
        :param SelectedTables: Snapshot list
        :type SelectedTables: list of SnapshotInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotsResponse(AbstractModel):
    """ModifySnapshots response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of snapshots modified in batches
        :type TotalCount: int
        :param TableResults: The result list of snapshots modified in batches
        :type TableResults: list of SnapshotResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTableGroupNameRequest(AbstractModel):
    """ModifyTableGroupName request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where a table group resides
        :type ClusterId: str
        :param TableGroupId: ID of the table group to be renamed
        :type TableGroupId: str
        :param TableGroupName: New table group name, which can contain letters and symbols
        :type TableGroupName: str
        """
        self.ClusterId = None
        self.TableGroupId = None
        self.TableGroupName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableGroupNameResponse(AbstractModel):
    """ModifyTableGroupName response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTableGroupTagsRequest(AbstractModel):
    """ModifyTableGroupTags request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where table group tags need to be modified
        :type ClusterId: str
        :param TableGroupId: The ID of the table group whose tags need to be modified
        :type TableGroupId: str
        :param ReplaceTags: The list of tags to add or modify
        :type ReplaceTags: list of TagInfoUnit
        :param DeleteTags: Tags to delete
        :type DeleteTags: list of TagInfoUnit
        """
        self.ClusterId = None
        self.TableGroupId = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableGroupTagsResponse(AbstractModel):
    """ModifyTableGroupTags response structure.

    """

    def __init__(self):
        r"""
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


class ModifyTableMemosRequest(AbstractModel):
    """ModifyTableMemos request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster instance where a table resides
        :type ClusterId: str
        :param TableMemos: List of details of selected tables
        :type TableMemos: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.TableMemos = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("TableMemos") is not None:
            self.TableMemos = []
            for item in params.get("TableMemos"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.TableMemos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableMemosResponse(AbstractModel):
    """ModifyTableMemos response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of tables modified for remarks
        :type TotalCount: int
        :param TableResults: List of table remarks modification results
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTableQuotasRequest(AbstractModel):
    """ModifyTableQuotas request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table to be scaled resides
        :type ClusterId: str
        :param TableQuotas: List of quotas of tables selected for modification
        :type TableQuotas: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.TableQuotas = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("TableQuotas") is not None:
            self.TableQuotas = []
            for item in params.get("TableQuotas"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.TableQuotas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableQuotasResponse(AbstractModel):
    """ModifyTableQuotas response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of scaled tables
        :type TotalCount: int
        :param TableResults: List of table scaling results
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTableTagsRequest(AbstractModel):
    """ModifyTableTags request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where table tags need to be modified
        :type ClusterId: str
        :param SelectedTables: The list of tables whose tags need to be modified
        :type SelectedTables: list of SelectedTableInfoNew
        :param ReplaceTags: The list of tags to add or modify
        :type ReplaceTags: list of TagInfoUnit
        :param DeleteTags: The list of tags to delete
        :type DeleteTags: list of TagInfoUnit
        """
        self.ClusterId = None
        self.SelectedTables = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableTagsResponse(AbstractModel):
    """ModifyTableTags response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The total number of returned results
        :type TotalCount: int
        :param TableResults: Returned results
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTablesRequest(AbstractModel):
    """ModifyTables request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table to be modified resides
        :type ClusterId: str
        :param IdlFiles: Selected table modification IDL files
        :type IdlFiles: list of IdlFileInfo
        :param SelectedTables: List of tables to be modified
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.IdlFiles = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTablesResponse(AbstractModel):
    """ModifyTables response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of modified tables
        :type TotalCount: int
        :param TableResults: List of table modification results
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ParsedTableInfoNew(AbstractModel):
    """Table information parsed from IDL table description file

    """

    def __init__(self):
        r"""
        :param TableIdlType: Table description language type. Valid values: PROTO, TDR
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableIdlType: str
        :param TableInstanceId: Table instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableInstanceId: str
        :param TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param TableType: Table data structure type. Valid values: GENERIC, LIST
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableType: str
        :param KeyFields: Primary key field information
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyFields: str
        :param OldKeyFields: Old primary key field information, which is valid during verification of table modification
Note: this field may return null, indicating that no valid values can be obtained.
        :type OldKeyFields: str
        :param ValueFields: Non-primary key field information
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValueFields: str
        :param OldValueFields: Old non-primary key field information, which is valid during verification of table modification
Note: this field may return null, indicating that no valid values can be obtained.
        :type OldValueFields: str
        :param TableGroupId: Table group ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param SumKeyFieldSize: Total size of primary key field
Note: this field may return null, indicating that no valid values can be obtained.
        :type SumKeyFieldSize: int
        :param SumValueFieldSize: Total size of non-primary key fields
Note: this field may return null, indicating that no valid values can be obtained.
        :type SumValueFieldSize: int
        :param IndexKeySet: Index key set
Note: this field may return null, indicating that no valid values can be obtained.
        :type IndexKeySet: str
        :param ShardingKeySet: Shardkey set
Note: this field may return null, indicating that no valid values can be obtained.
        :type ShardingKeySet: str
        :param TdrVersion: TDR version number
Note: this field may return null, indicating that no valid values can be obtained.
        :type TdrVersion: int
        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param ListElementNum: Number of LIST-type table elements
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListElementNum: int
        :param SortFieldNum: Number of SORTLIST-type table sort fields
Note: this field may return null, indicating that no valid values can be obtained.
        :type SortFieldNum: int
        :param SortRule: Sort order of SORTLIST-type tables
Note: this field may return null, indicating that no valid values can be obtained.
        :type SortRule: int
        """
        self.TableIdlType = None
        self.TableInstanceId = None
        self.TableName = None
        self.TableType = None
        self.KeyFields = None
        self.OldKeyFields = None
        self.ValueFields = None
        self.OldValueFields = None
        self.TableGroupId = None
        self.SumKeyFieldSize = None
        self.SumValueFieldSize = None
        self.IndexKeySet = None
        self.ShardingKeySet = None
        self.TdrVersion = None
        self.Error = None
        self.ListElementNum = None
        self.SortFieldNum = None
        self.SortRule = None


    def _deserialize(self, params):
        self.TableIdlType = params.get("TableIdlType")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.KeyFields = params.get("KeyFields")
        self.OldKeyFields = params.get("OldKeyFields")
        self.ValueFields = params.get("ValueFields")
        self.OldValueFields = params.get("OldValueFields")
        self.TableGroupId = params.get("TableGroupId")
        self.SumKeyFieldSize = params.get("SumKeyFieldSize")
        self.SumValueFieldSize = params.get("SumValueFieldSize")
        self.IndexKeySet = params.get("IndexKeySet")
        self.ShardingKeySet = params.get("ShardingKeySet")
        self.TdrVersion = params.get("TdrVersion")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.ListElementNum = params.get("ListElementNum")
        self.SortFieldNum = params.get("SortFieldNum")
        self.SortRule = params.get("SortRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoolInfo(AbstractModel):
    """Information of the machines in the resource pool

    """

    def __init__(self):
        r"""
        :param PoolUid: Unique ID
        :type PoolUid: int
        :param Ipv6Enable: Whether IPv6 is supported
        :type Ipv6Enable: int
        :param AvailableAppCount: Remaining available cluster resources
        :type AvailableAppCount: int
        :param ServerList: The list of machines at the storage layer (tcapsvr)
        :type ServerList: list of ServerMachineInfo
        :param ProxyList: The list of machines at the access layer (tcaproxy)
        :type ProxyList: list of ProxyMachineInfo
        """
        self.PoolUid = None
        self.Ipv6Enable = None
        self.AvailableAppCount = None
        self.ServerList = None
        self.ProxyList = None


    def _deserialize(self, params):
        self.PoolUid = params.get("PoolUid")
        self.Ipv6Enable = params.get("Ipv6Enable")
        self.AvailableAppCount = params.get("AvailableAppCount")
        if params.get("ServerList") is not None:
            self.ServerList = []
            for item in params.get("ServerList"):
                obj = ServerMachineInfo()
                obj._deserialize(item)
                self.ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyMachineInfo()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyDetailInfo(AbstractModel):
    """Information of the machine at the access layer (tcaproxy) in a dedicated cluster

    """

    def __init__(self):
        r"""
        :param ProxyUid: The unique ID of the access layer (tcaproxy)
        :type ProxyUid: str
        :param MachineType: Machine type
        :type MachineType: str
        :param ProcessSpeed: The speed of processing request packets
        :type ProcessSpeed: int
        :param AverageProcessDelay: Request packet delay
        :type AverageProcessDelay: int
        :param SlowProcessSpeed: The speed of processing delayed request packets
        :type SlowProcessSpeed: int
        """
        self.ProxyUid = None
        self.MachineType = None
        self.ProcessSpeed = None
        self.AverageProcessDelay = None
        self.SlowProcessSpeed = None


    def _deserialize(self, params):
        self.ProxyUid = params.get("ProxyUid")
        self.MachineType = params.get("MachineType")
        self.ProcessSpeed = params.get("ProcessSpeed")
        self.AverageProcessDelay = params.get("AverageProcessDelay")
        self.SlowProcessSpeed = params.get("SlowProcessSpeed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyMachineInfo(AbstractModel):
    """Information of the machine at the access layer (tcaproxy)

    """

    def __init__(self):
        r"""
        :param ProxyUid: Unique ID
        :type ProxyUid: str
        :param MachineType: Machine type
        :type MachineType: str
        :param AvailableCount: The number of proxy resources to be assigned
        :type AvailableCount: int
        """
        self.ProxyUid = None
        self.MachineType = None
        self.AvailableCount = None


    def _deserialize(self, params):
        self.ProxyUid = params.get("ProxyUid")
        self.MachineType = params.get("MachineType")
        self.AvailableCount = params.get("AvailableCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverRecycleTablesRequest(AbstractModel):
    """RecoverRecycleTables request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where a table resides
        :type ClusterId: str
        :param SelectedTables: Information of tables to be recovered
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverRecycleTablesResponse(AbstractModel):
    """RecoverRecycleTables response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of recovered tables
        :type TotalCount: int
        :param TableResults: List of information of recovered tables
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """TcaplusDB service region details

    """

    def __init__(self):
        r"""
        :param RegionName: Region `Ap-code`
        :type RegionName: str
        :param RegionAbbr: Region abbreviation
        :type RegionAbbr: str
        :param RegionId: Region ID
        :type RegionId: int
        :param Ipv6Enable: Whether to support IPv6 address access. Valid values: 0 (support), 1 (not support)
        :type Ipv6Enable: int
        """
        self.RegionName = None
        self.RegionAbbr = None
        self.RegionId = None
        self.Ipv6Enable = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.RegionAbbr = params.get("RegionAbbr")
        self.RegionId = params.get("RegionId")
        self.Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTablesRequest(AbstractModel):
    """RollbackTables request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table to be rolled back resides
        :type ClusterId: str
        :param SelectedTables: List of tables to be rolled back
        :type SelectedTables: list of SelectedTableInfoNew
        :param RollbackTime: Time to roll back to
        :type RollbackTime: str
        :param Mode: Rollback mode. `KEYS` is supported
        :type Mode: str
        """
        self.ClusterId = None
        self.SelectedTables = None
        self.RollbackTime = None
        self.Mode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        self.RollbackTime = params.get("RollbackTime")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTablesResponse(AbstractModel):
    """RollbackTables response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of table rollback task results
        :type TotalCount: int
        :param TableResults: Table rollback task result list
        :type TableResults: list of TableRollbackResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableRollbackResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class SelectedTableInfoNew(AbstractModel):
    """Information of selected table

    """

    def __init__(self):
        r"""
        :param TableGroupId: ID of the table group where a table resides
        :type TableGroupId: str
        :param TableName: Table name
        :type TableName: str
        :param TableInstanceId: Table instance ID
        :type TableInstanceId: str
        :param TableIdlType: Table description language type. Valid values: PROTO, TDR
        :type TableIdlType: str
        :param TableType: Table data structure type. Valid values: GENERIC, LIST
        :type TableType: str
        :param ListElementNum: Number of LIST-type table elements
        :type ListElementNum: int
        :param ReservedVolume: Reserved table capacity in GB
        :type ReservedVolume: int
        :param ReservedReadQps: Reserved table read QPS
        :type ReservedReadQps: int
        :param ReservedWriteQps: Reserved table write QPS
        :type ReservedWriteQps: int
        :param Memo: Table remarks
        :type Memo: str
        :param FileName: Key rollback filename, which is only used for rollback
        :type FileName: str
        :param FileExtType: Key rollback file extension, which is only used for rollback
        :type FileExtType: str
        :param FileSize: Key rollback file size, which is only used for rollback
        :type FileSize: int
        :param FileContent: Key rollback file content, which is only used for rollback
        :type FileContent: str
        """
        self.TableGroupId = None
        self.TableName = None
        self.TableInstanceId = None
        self.TableIdlType = None
        self.TableType = None
        self.ListElementNum = None
        self.ReservedVolume = None
        self.ReservedReadQps = None
        self.ReservedWriteQps = None
        self.Memo = None
        self.FileName = None
        self.FileExtType = None
        self.FileSize = None
        self.FileContent = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableIdlType = params.get("TableIdlType")
        self.TableType = params.get("TableType")
        self.ListElementNum = params.get("ListElementNum")
        self.ReservedVolume = params.get("ReservedVolume")
        self.ReservedReadQps = params.get("ReservedReadQps")
        self.ReservedWriteQps = params.get("ReservedWriteQps")
        self.Memo = params.get("Memo")
        self.FileName = params.get("FileName")
        self.FileExtType = params.get("FileExtType")
        self.FileSize = params.get("FileSize")
        self.FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectedTableWithField(AbstractModel):
    """The list of tables to which the specified fields belong

    """

    def __init__(self):
        r"""
        :param TableGroupId: ID of the table group where the table resides
        :type TableGroupId: str
        :param TableName: Table name
        :type TableName: str
        :param TableInstanceId: Table ID
        :type TableInstanceId: str
        :param TableIdlType: Table description language. Valid values: `PROTO`, `TDR`
        :type TableIdlType: str
        :param TableType: Table data structure. Valid values: `GENERIC`, `LIST`
        :type TableType: str
        :param SelectedFields: The list of fields on which indexes will be created, table caching enabled, or data subscription enabled
        :type SelectedFields: list of FieldInfo
        :param ShardNum: The number of index shards
        :type ShardNum: int
        :param KafkaInfo: CKafka instance information
        :type KafkaInfo: :class:`tencentcloud.tcaplusdb.v20190823.models.KafkaInfo`
        """
        self.TableGroupId = None
        self.TableName = None
        self.TableInstanceId = None
        self.TableIdlType = None
        self.TableType = None
        self.SelectedFields = None
        self.ShardNum = None
        self.KafkaInfo = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableIdlType = params.get("TableIdlType")
        self.TableType = params.get("TableType")
        if params.get("SelectedFields") is not None:
            self.SelectedFields = []
            for item in params.get("SelectedFields"):
                obj = FieldInfo()
                obj._deserialize(item)
                self.SelectedFields.append(obj)
        self.ShardNum = params.get("ShardNum")
        if params.get("KafkaInfo") is not None:
            self.KafkaInfo = KafkaInfo()
            self.KafkaInfo._deserialize(params.get("KafkaInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerDetailInfo(AbstractModel):
    """Information of the machine at the storage layer (tcapsvr) in a dedicated cluster

    """

    def __init__(self):
        r"""
        :param ServerUid: The unique ID of the storage layer (tcapsvr)
        :type ServerUid: str
        :param MachineType: Machine type
        :type MachineType: str
        :param MemoryRate: Memory utilization
        :type MemoryRate: int
        :param DiskRate: Disk utilization
        :type DiskRate: int
        :param ReadNum: The number of reads
        :type ReadNum: int
        :param WriteNum: The number of writes
        :type WriteNum: int
        """
        self.ServerUid = None
        self.MachineType = None
        self.MemoryRate = None
        self.DiskRate = None
        self.ReadNum = None
        self.WriteNum = None


    def _deserialize(self, params):
        self.ServerUid = params.get("ServerUid")
        self.MachineType = params.get("MachineType")
        self.MemoryRate = params.get("MemoryRate")
        self.DiskRate = params.get("DiskRate")
        self.ReadNum = params.get("ReadNum")
        self.WriteNum = params.get("WriteNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerMachineInfo(AbstractModel):
    """`ServerList`, the list of machines at the storage layer (tcapsvr)

    """

    def __init__(self):
        r"""
        :param ServerUid: The unique ID of the machine
        :type ServerUid: str
        :param MachineType: Machine type
        :type MachineType: str
        """
        self.ServerUid = None
        self.MachineType = None


    def _deserialize(self, params):
        self.ServerUid = params.get("ServerUid")
        self.MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTableDataFlowRequest(AbstractModel):
    """SetTableDataFlow request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The ID of the cluster where the tables reside
        :type ClusterId: str
        :param SelectedTables: The list of tables for which data subscription will be enabled
        :type SelectedTables: list of SelectedTableWithField
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableWithField()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTableDataFlowResponse(AbstractModel):
    """SetTableDataFlow response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of tables for which data subscription has been enabled
        :type TotalCount: int
        :param TableResults: The result list of tables for which data subscription has been enabled
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class SetTableIndexRequest(AbstractModel):
    """SetTableIndex request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where the table resides
        :type ClusterId: str
        :param SelectedTables: The list of tables that need to create global indexes
        :type SelectedTables: list of SelectedTableWithField
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableWithField()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTableIndexResponse(AbstractModel):
    """SetTableIndex response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of tables whose global indexes are created
        :type TotalCount: int
        :param TableResults: The list of global index creation results
        :type TableResults: list of TableResultNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class SnapshotInfo(AbstractModel):
    """Snapshot list

    """

    def __init__(self):
        r"""
        :param TableGroupId: The ID of the table group where the table resides
        :type TableGroupId: str
        :param TableName: Table name
        :type TableName: str
        :param SnapshotName: Snapshot name
        :type SnapshotName: str
        :param SnapshotTime: The time of the data from which the snapshot was created
        :type SnapshotTime: str
        :param SnapshotDeadTime: Snapshot expiration time
        :type SnapshotDeadTime: str
        """
        self.TableGroupId = None
        self.TableName = None
        self.SnapshotName = None
        self.SnapshotTime = None
        self.SnapshotDeadTime = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.SnapshotName = params.get("SnapshotName")
        self.SnapshotTime = params.get("SnapshotTime")
        self.SnapshotDeadTime = params.get("SnapshotDeadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotInfoNew(AbstractModel):
    """New expiration time of a snapshot

    """

    def __init__(self):
        r"""
        :param TableGroupId: The ID of the table group where the table resides
        :type TableGroupId: str
        :param TableName: Table name
        :type TableName: str
        :param SnapshotName: Snapshot name
        :type SnapshotName: str
        :param SnapshotDeadTime: Snapshot expiration time
        :type SnapshotDeadTime: str
        """
        self.TableGroupId = None
        self.TableName = None
        self.SnapshotName = None
        self.SnapshotDeadTime = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.SnapshotName = params.get("SnapshotName")
        self.SnapshotDeadTime = params.get("SnapshotDeadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotResult(AbstractModel):
    """The result of snapshot creation

    """

    def __init__(self):
        r"""
        :param TableGroupId: The ID of the table group where the table resides
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param TableName: Table name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TableName: str
        :param TaskId: Task ID, which is valid for the API that creates one task at a time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskId: str
        :param Error: Error information
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param SnapshotName: Snapshot name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotName: str
        :param SnapshotTime: The time of the data from which the snapshot was created
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotTime: str
        :param SnapshotDeadTime: When the snapshot expires
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotDeadTime: str
        :param SnapshotCreateTime: When the snapshot was created
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotCreateTime: str
        :param SnapshotSize: Snapshot size
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotSize: int
        :param SnapshotStatus: Snapshot status. Valid values: `0` (creating), `1` (normal), `2` (deleting), `3` (expired), `4` (rolling back).
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotStatus: int
        """
        self.TableGroupId = None
        self.TableName = None
        self.TaskId = None
        self.Error = None
        self.SnapshotName = None
        self.SnapshotTime = None
        self.SnapshotDeadTime = None
        self.SnapshotCreateTime = None
        self.SnapshotSize = None
        self.SnapshotStatus = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.SnapshotName = params.get("SnapshotName")
        self.SnapshotTime = params.get("SnapshotTime")
        self.SnapshotDeadTime = params.get("SnapshotDeadTime")
        self.SnapshotCreateTime = params.get("SnapshotCreateTime")
        self.SnapshotSize = params.get("SnapshotSize")
        self.SnapshotStatus = params.get("SnapshotStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncTableField(AbstractModel):
    """Mapping of cache table field name

    """

    def __init__(self):
        r"""
        :param SourceName: Field name of TcaplusDB table
        :type SourceName: str
        :param TargetName: Field name of the target cache table
        :type TargetName: str
        """
        self.SourceName = None
        self.TargetName = None


    def _deserialize(self, params):
        self.SourceName = params.get("SourceName")
        self.TargetName = params.get("TargetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncTableInfo(AbstractModel):
    """TcaplusDB cache table information

    """

    def __init__(self):
        r"""
        :param TargetTableSplitNum: Sharded table quantity of the target cache table
        :type TargetTableSplitNum: int
        :param TargetTableNamePrefix: Prefix of the target cache table name
        :type TargetTableNamePrefix: list of str
        :param TargetSyncDBInstanceId: Instance ID of the cache database
        :type TargetSyncDBInstanceId: str
        :param TargetDatabaseName: Name of the database where the cache table resides
        :type TargetDatabaseName: str
        :param Status: Caching status. Valid values: `0` (creating), `1` (caching), `2` (disabled), `-1` (deleted).
        :type Status: int
        :param ClusterId: ID of cluster where the table resides
        :type ClusterId: str
        :param TableGroupId: The ID of the table group where the table resides
        :type TableGroupId: int
        :param TableName: Table name
        :type TableName: str
        :param TableId: Table ID
        :type TableId: str
        :param KeyFieldMapping: Mapping from the primary key field of the TcaplusDB table to the field of the target cache table
        :type KeyFieldMapping: list of SyncTableField
        :param ValueFieldMapping: Mapping of TcaplusDB table field to target cache table field
        :type ValueFieldMapping: list of SyncTableField
        """
        self.TargetTableSplitNum = None
        self.TargetTableNamePrefix = None
        self.TargetSyncDBInstanceId = None
        self.TargetDatabaseName = None
        self.Status = None
        self.ClusterId = None
        self.TableGroupId = None
        self.TableName = None
        self.TableId = None
        self.KeyFieldMapping = None
        self.ValueFieldMapping = None


    def _deserialize(self, params):
        self.TargetTableSplitNum = params.get("TargetTableSplitNum")
        self.TargetTableNamePrefix = params.get("TargetTableNamePrefix")
        self.TargetSyncDBInstanceId = params.get("TargetSyncDBInstanceId")
        self.TargetDatabaseName = params.get("TargetDatabaseName")
        self.Status = params.get("Status")
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.TableId = params.get("TableId")
        if params.get("KeyFieldMapping") is not None:
            self.KeyFieldMapping = []
            for item in params.get("KeyFieldMapping"):
                obj = SyncTableField()
                obj._deserialize(item)
                self.KeyFieldMapping.append(obj)
        if params.get("ValueFieldMapping") is not None:
            self.ValueFieldMapping = []
            for item in params.get("ValueFieldMapping"):
                obj = SyncTableField()
                obj._deserialize(item)
                self.ValueFieldMapping.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableGroupInfo(AbstractModel):
    """Table group details

    """

    def __init__(self):
        r"""
        :param TableGroupId: Table group ID
        :type TableGroupId: str
        :param TableGroupName: Table group name
        :type TableGroupName: str
        :param CreatedTime: Table group creation time
        :type CreatedTime: str
        :param TableCount: Number of tables in table group
        :type TableCount: int
        :param TotalSize: Total table storage capacity in MB in table group
        :type TotalSize: int
        """
        self.TableGroupId = None
        self.TableGroupName = None
        self.CreatedTime = None
        self.TableCount = None
        self.TotalSize = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")
        self.CreatedTime = params.get("CreatedTime")
        self.TableCount = params.get("TableCount")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableInfoNew(AbstractModel):
    """Table details

    """

    def __init__(self):
        r"""
        :param TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param TableInstanceId: Table instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableInstanceId: str
        :param TableType: Table data structure type, such as `GENERIC` or `LIST`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableType: str
        :param TableIdlType: Table data interface description language (IDL) type, such as `PROTO` or `TDR`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableIdlType: str
        :param ClusterId: ID of the cluster where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param ClusterName: Name of the cluster where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param TableGroupId: ID of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param TableGroupName: Name of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupName: str
        :param KeyStruct: JSON string of table's primary key field structure
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyStruct: str
        :param ValueStruct: JSON string of table non-primary key field structure
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValueStruct: str
        :param ShardingKeySet: Table shardkey set, which is valid for PROTO-type tables
Note: this field may return null, indicating that no valid values can be obtained.
        :type ShardingKeySet: str
        :param IndexStruct: Table index key field set, which is valid for PROTO-type tables
Note: this field may return null, indicating that no valid values can be obtained.
        :type IndexStruct: str
        :param ListElementNum: Number of LIST-type table elements
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListElementNum: int
        :param IdlFiles: Information list of IDL files associated with table
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdlFiles: list of IdlFileInfo
        :param ReservedVolume: Reserved table capacity in GB
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReservedVolume: int
        :param ReservedReadQps: Reserved table read QPS
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReservedReadQps: int
        :param ReservedWriteQps: Reserved table write QPS
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReservedWriteQps: int
        :param TableSize: Actual table data size in MB
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableSize: int
        :param Status: Table status
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param CreatedTime: Table creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param UpdatedTime: Table's last modified time
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdatedTime: str
        :param Memo: Table remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Memo: str
        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param ApiAccessId: TcaplusDB SDK data access ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAccessId: str
        :param SortFieldNum: Number of SORTLIST-type table sort fields
Note: this field may return null, indicating that no valid values can be obtained.
        :type SortFieldNum: int
        :param SortRule: Sort order of SORTLIST-type tables
Note: this field may return null, indicating that no valid values can be obtained.
        :type SortRule: int
        :param DbClusterInfoStruct: Information about global indexes, table caching, or data subscription
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DbClusterInfoStruct: str
        :param TxhBackupExpireDay: The number of days after which the table Txh backup files will be expire and deleted.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TxhBackupExpireDay: int
        :param SyncTableInfo: Cached information of the table
Note: This field may return null, indicating that no valid values can be obtained.
        :type SyncTableInfo: :class:`tencentcloud.tcaplusdb.v20190823.models.SyncTableInfo`
        """
        self.TableName = None
        self.TableInstanceId = None
        self.TableType = None
        self.TableIdlType = None
        self.ClusterId = None
        self.ClusterName = None
        self.TableGroupId = None
        self.TableGroupName = None
        self.KeyStruct = None
        self.ValueStruct = None
        self.ShardingKeySet = None
        self.IndexStruct = None
        self.ListElementNum = None
        self.IdlFiles = None
        self.ReservedVolume = None
        self.ReservedReadQps = None
        self.ReservedWriteQps = None
        self.TableSize = None
        self.Status = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.Memo = None
        self.Error = None
        self.ApiAccessId = None
        self.SortFieldNum = None
        self.SortRule = None
        self.DbClusterInfoStruct = None
        self.TxhBackupExpireDay = None
        self.SyncTableInfo = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")
        self.KeyStruct = params.get("KeyStruct")
        self.ValueStruct = params.get("ValueStruct")
        self.ShardingKeySet = params.get("ShardingKeySet")
        self.IndexStruct = params.get("IndexStruct")
        self.ListElementNum = params.get("ListElementNum")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        self.ReservedVolume = params.get("ReservedVolume")
        self.ReservedReadQps = params.get("ReservedReadQps")
        self.ReservedWriteQps = params.get("ReservedWriteQps")
        self.TableSize = params.get("TableSize")
        self.Status = params.get("Status")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.Memo = params.get("Memo")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.ApiAccessId = params.get("ApiAccessId")
        self.SortFieldNum = params.get("SortFieldNum")
        self.SortRule = params.get("SortRule")
        self.DbClusterInfoStruct = params.get("DbClusterInfoStruct")
        self.TxhBackupExpireDay = params.get("TxhBackupExpireDay")
        if params.get("SyncTableInfo") is not None:
            self.SyncTableInfo = SyncTableInfo()
            self.SyncTableInfo._deserialize(params.get("SyncTableInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableResultNew(AbstractModel):
    """Table processing result information

    """

    def __init__(self):
        r"""
        :param TableInstanceId: Table instance ID in the format of `tcaplus-3be64cbb`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableInstanceId: str
        :param TaskId: Task ID, which is valid for the API that creates one task
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param TableType: Table data structure type, such as `GENERIC` or `LIST`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableType: str
        :param TableIdlType: Table data interface description language (IDL) type, such as `PROTO` or `TDR`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableIdlType: str
        :param TableGroupId: ID of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param TaskIds: Task ID list, which is valid for the API that creates multiple tasks
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskIds: list of str
        :param ApplicationId: Cluster operation application ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplicationId: str
        """
        self.TableInstanceId = None
        self.TaskId = None
        self.TableName = None
        self.TableType = None
        self.TableIdlType = None
        self.TableGroupId = None
        self.Error = None
        self.TaskIds = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.TableInstanceId = params.get("TableInstanceId")
        self.TaskId = params.get("TaskId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.TaskIds = params.get("TaskIds")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableRollbackResultNew(AbstractModel):
    """Table rollback result information

    """

    def __init__(self):
        r"""
        :param TableInstanceId: Table instance ID in the format of `tcaplus-3be64cbb`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableInstanceId: str
        :param TaskId: Task ID, which is valid for the API that creates one task
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param TableType: Table data structure type, such as `GENERIC` or `LIST`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableType: str
        :param TableIdlType: Table data interface description language (IDL) type, such as `PROTO` or `TDR`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableIdlType: str
        :param TableGroupId: ID of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param TaskIds: Task ID list, which is valid for the API that creates multiple tasks
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskIds: list of str
        :param FileId: ID of uploaded key file
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileId: str
        :param SuccKeyNum: Number of keys successfully verified
Note: this field may return null, indicating that no valid values can be obtained.
        :type SuccKeyNum: int
        :param TotalKeyNum: Total number of keys contained in key file
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalKeyNum: int
        """
        self.TableInstanceId = None
        self.TaskId = None
        self.TableName = None
        self.TableType = None
        self.TableIdlType = None
        self.TableGroupId = None
        self.Error = None
        self.TaskIds = None
        self.FileId = None
        self.SuccKeyNum = None
        self.TotalKeyNum = None


    def _deserialize(self, params):
        self.TableInstanceId = params.get("TableInstanceId")
        self.TaskId = params.get("TaskId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.TaskIds = params.get("TaskIds")
        self.FileId = params.get("FileId")
        self.SuccKeyNum = params.get("SuccKeyNum")
        self.TotalKeyNum = params.get("TotalKeyNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfoUnit(AbstractModel):
    """Tag information unit

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
        


class TagsInfoOfCluster(AbstractModel):
    """Cluster tag information

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Tags: Tag information
        :type Tags: list of TagInfoUnit
        :param Error: Error message
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self.ClusterId = None
        self.Tags = None
        self.Error = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfTable(AbstractModel):
    """Table tag information

    """

    def __init__(self):
        r"""
        :param TableInstanceId: Table instance ID
        :type TableInstanceId: str
        :param TableName: Table name
        :type TableName: str
        :param TableGroupId: Table group ID
        :type TableGroupId: str
        :param Tags: Tag information
        :type Tags: list of TagInfoUnit
        :param Error: Error message
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self.TableInstanceId = None
        self.TableName = None
        self.TableGroupId = None
        self.Tags = None
        self.Error = None


    def _deserialize(self, params):
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableName = params.get("TableName")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfTableGroup(AbstractModel):
    """Table group tag information

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param TableGroupId: Table group ID
        :type TableGroupId: str
        :param Tags: Tag information
        :type Tags: list of TagInfoUnit
        :param Error: Error message
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self.ClusterId = None
        self.TableGroupId = None
        self.Tags = None
        self.Error = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfoNew(AbstractModel):
    """Task details

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID
        :type TaskId: str
        :param TaskType: Task type
        :type TaskType: str
        :param TransId: ID of TcaplusDB internal transaction associated with task
        :type TransId: str
        :param ClusterId: ID of the cluster where a task resides
        :type ClusterId: str
        :param ClusterName: Name of the cluster where a task resides
        :type ClusterName: str
        :param Progress: Task progress
        :type Progress: int
        :param StartTime: Task creation time
        :type StartTime: str
        :param UpdateTime: Task last modified time
        :type UpdateTime: str
        :param Operator: Operator
        :type Operator: str
        :param Content: Task details
        :type Content: str
        """
        self.TaskId = None
        self.TaskType = None
        self.TransId = None
        self.ClusterId = None
        self.ClusterName = None
        self.Progress = None
        self.StartTime = None
        self.UpdateTime = None
        self.Operator = None
        self.Content = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.TransId = params.get("TransId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Progress = params.get("Progress")
        self.StartTime = params.get("StartTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Operator = params.get("Operator")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApplyRequest(AbstractModel):
    """UpdateApply request structure.

    """

    def __init__(self):
        r"""
        :param ApplyStatus: Application status
        :type ApplyStatus: list of ApplyStatus
        """
        self.ApplyStatus = None


    def _deserialize(self, params):
        if params.get("ApplyStatus") is not None:
            self.ApplyStatus = []
            for item in params.get("ApplyStatus"):
                obj = ApplyStatus()
                obj._deserialize(item)
                self.ApplyStatus.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApplyResponse(AbstractModel):
    """UpdateApply response structure.

    """

    def __init__(self):
        r"""
        :param ApplyResults: List of updated applications
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplyResults: list of ApplyResult
        :param TotalCount: Total number of updated applications
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ApplyResults = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApplyResults") is not None:
            self.ApplyResults = []
            for item in params.get("ApplyResults"):
                obj = ApplyResult()
                obj._deserialize(item)
                self.ApplyResults.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class VerifyIdlFilesRequest(AbstractModel):
    """VerifyIdlFiles request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster where to create a table
        :type ClusterId: str
        :param TableGroupId: ID of the table group where to create a table
        :type TableGroupId: str
        :param ExistingIdlFiles: List of information of uploaded IDL files. Either this parameter or `NewIdlFiles` must be present
        :type ExistingIdlFiles: list of IdlFileInfo
        :param NewIdlFiles: List of information of IDL files to be uploaded. Either this parameter or `ExistingIdlFiles` must be present
        :type NewIdlFiles: list of IdlFileInfo
        """
        self.ClusterId = None
        self.TableGroupId = None
        self.ExistingIdlFiles = None
        self.NewIdlFiles = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("ExistingIdlFiles") is not None:
            self.ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self.NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.NewIdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyIdlFilesResponse(AbstractModel):
    """VerifyIdlFiles response structure.

    """

    def __init__(self):
        r"""
        :param IdlFiles: Information list of all IDL files uploaded and verified in this request
        :type IdlFiles: list of IdlFileInfo
        :param TotalCount: Number of valid tables parsed by reading IDL description file, excluding tables already created
        :type TotalCount: int
        :param TableInfos: List of valid tables parsed by reading IDL description file, excluding tables already created
        :type TableInfos: list of ParsedTableInfoNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IdlFiles = None
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")