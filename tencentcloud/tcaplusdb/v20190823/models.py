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


class Application(AbstractModel):
    """Cluster operation application

    """

    def __init__(self):
        """
        :param ApplicationId: Application ID\n        :type ApplicationId: str\n        :param ApplicationType: Application type\n        :type ApplicationType: int\n        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param ClusterName: Cluster name\n        :type ClusterName: str\n        :param TableGroupName: Table group name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type TableGroupName: str\n        :param TableName: Table name\n        :type TableName: str\n        :param Applicant: Applicant\n        :type Applicant: str\n        :param CreatedTime: The creation time of the application\n        :type CreatedTime: str\n        :param ApplicationStatus: Status. Valid values: `-1` (canceled), `0` (pending approval), `1` (application approved and task submitted), `2` (rejected)\n        :type ApplicationStatus: int\n        :param TableGroupId: Table group ID\n        :type TableGroupId: str\n        :param TaskId: ID of the submitted task (if the application is not approved, this parameter is `0`)\n        :type TaskId: str\n        :param TableInstanceId: Globally unique table ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type TableInstanceId: str\n        :param UpdateTime: Update time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type UpdateTime: str\n        :param ExecuteUser: Approver
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ExecuteUser: str\n        :param ExecuteStatus: Execution status
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ExecuteStatus: str\n        :param CanCensor: Whether the application can be approved by the API caller
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type CanCensor: bool\n        :param CanWithdrawal: Whether the application can be canceled by the API caller
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type CanWithdrawal: bool\n        """
        self.ApplicationId = None
        self.ApplicationType = None
        self.ClusterId = None
        self.ClusterName = None
        self.TableGroupName = None
        self.TableName = None
        self.Applicant = None
        self.CreatedTime = None
        self.ApplicationStatus = None
        self.TableGroupId = None
        self.TaskId = None
        self.TableInstanceId = None
        self.UpdateTime = None
        self.ExecuteUser = None
        self.ExecuteStatus = None
        self.CanCensor = None
        self.CanWithdrawal = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationType = params.get("ApplicationType")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.TableGroupName = params.get("TableGroupName")
        self.TableName = params.get("TableName")
        self.Applicant = params.get("Applicant")
        self.CreatedTime = params.get("CreatedTime")
        self.ApplicationStatus = params.get("ApplicationStatus")
        self.TableGroupId = params.get("TableGroupId")
        self.TaskId = params.get("TaskId")
        self.TableInstanceId = params.get("TableInstanceId")
        self.UpdateTime = params.get("UpdateTime")
        self.ExecuteUser = params.get("ExecuteUser")
        self.ExecuteStatus = params.get("ExecuteStatus")
        self.CanCensor = params.get("CanCensor")
        self.CanWithdrawal = params.get("CanWithdrawal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyResult(AbstractModel):
    """Application update results

    """

    def __init__(self):
        """
        :param ApplicationId: Application ID\n        :type ApplicationId: str\n        :param ApplicationType: Application type\n        :type ApplicationType: int\n        :param ApplicationStatus: Status. Valid values: `0` (pending approval), `1` (application approved and task submitted), `2` (rejected)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ApplicationStatus: int\n        :param TaskId: ID of the submitted task
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type TaskId: str\n        :param Error: Error information
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
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
        """
        :param ApplicationId: Value format: cluster ID-application ID\n        :type ApplicationId: str\n        :param ApplicationStatus: Status. Valid values: `-1` (canceled), `0` (pending approval), `1` (application approved and task submitted), `2` (rejected). Only applications in the pending approval status can be updated.\n        :type ApplicationStatus: int\n        :param ApplicationType: Application type\n        :type ApplicationType: int\n        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        """
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
        """
        :param ClusterId: ID of the cluster instance where a table resides\n        :type ClusterId: str\n        :param SelectedTables: List of information of tables to be cleared\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
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
        """
        :param TotalCount: Number of cleared tables\n        :type TotalCount: int\n        :param TableResults: List of table clearing results\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterName: Cluster name\n        :type ClusterName: str\n        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param Region: Cluster region\n        :type Region: str\n        :param IdlType: Cluster data description language type, such as `PROTO`, `TDR`, or `MIX`\n        :type IdlType: str\n        :param NetworkType: Network type\n        :type NetworkType: str\n        :param VpcId: ID of the VPC instance with which a cluster is associated\n        :type VpcId: str\n        :param SubnetId: ID of the subnet instance with which a cluster is associated\n        :type SubnetId: str\n        :param CreatedTime: Creation time\n        :type CreatedTime: str\n        :param Password: Cluster password\n        :type Password: str\n        :param PasswordStatus: Password status\n        :type PasswordStatus: str\n        :param ApiAccessId: TcaplusDB SDK connection parameter: access ID\n        :type ApiAccessId: str\n        :param ApiAccessIp: TcaplusDB SDK connection parameter: access address\n        :type ApiAccessIp: str\n        :param ApiAccessPort: TcaplusDB SDK connection parameter: access port\n        :type ApiAccessPort: int\n        :param OldPasswordExpireTime: If `PasswordStatus` is `unmodifiable`, the old password has not expired, and this field will display its expiration time; otherwise, this field will be empty
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OldPasswordExpireTime: str\n        :param ApiAccessIpv6: TcaplusDB SDK connection parameter for accessing IPv6 addresses
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiAccessIpv6: str\n        :param ClusterType: Cluster type
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ClusterType: int\n        :param ClusterStatus: Cluster status
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ClusterStatus: int\n        :param ReadCapacityUnit: Read CU
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ReadCapacityUnit: int\n        :param WriteCapacityUnit: Write CU
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type WriteCapacityUnit: int\n        :param DiskVolume: Disk capacity
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type DiskVolume: int\n        :param ServerList: Information of the machine at the storage layer (tcapsvr) in a dedicated cluster
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ServerList: list of ServerDetailInfo\n        :param ProxyList: Information of the machine at the access layer (tcaproxy) in a dedicated cluster
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ProxyList: list of ProxyDetailInfo\n        :param Censorship: Whether the cluster operation approval feature is enabled. Valid values: `0` (disabled), `1` (enabled)\n        :type Censorship: int\n        :param DbaUins: Approver UIN list
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type DbaUins: list of str\n        """
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
        """
        :param ClusterId: ID of the cluster where the table to be modified resides\n        :type ClusterId: str\n        :param SelectedTables: List of tables to be modified\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param ExistingIdlFiles: Selected list of uploaded IDL files. Either this parameter or `NewIdlFiles` must be selected\n        :type ExistingIdlFiles: list of IdlFileInfo\n        :param NewIdlFiles: List of IDL files to be uploaded. Either this parameter or `ExistingIdlFiles` must be selected\n        :type NewIdlFiles: list of IdlFileInfo\n        """
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
        """
        :param IdlFiles: Information list of all IDL files uploaded and verified in this request\n        :type IdlFiles: list of IdlFileInfo\n        :param TotalCount: Number of tables verified to be valid in this request\n        :type TotalCount: int\n        :param TableInfos: Verification result parsed from the selected table after the IDL description file is read\n        :type TableInfos: list of ParsedTableInfoNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param SrcTableClusterId: Cluster ID of the source table\n        :type SrcTableClusterId: str\n        :param SrcTableGroupId: Table group ID of the source table\n        :type SrcTableGroupId: str\n        :param SrcTableName: Source table name\n        :type SrcTableName: str\n        :param DstTableClusterId: Cluster ID of the target table\n        :type DstTableClusterId: str\n        :param DstTableGroupId: Table group ID of the target table\n        :type DstTableGroupId: str\n        :param DstTableName: Target table name\n        :type DstTableName: str\n        :param SrcTableInstanceId: Source table ID\n        :type SrcTableInstanceId: str\n        :param DstTableInstanceId: Target table ID\n        :type DstTableInstanceId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where the table to be backed up resides\n        :type ClusterId: str\n        :param SelectedTables: Information list of tables to be backed up\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param Remark: Remarks\n        :type Remark: str\n        """
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
        """
        :param TaskIds: List of backup creation task IDs
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type TaskIds: list of str\n        :param ApplicationIds: List of backup creation application IDs
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ApplicationIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param IdlType: Cluster data description language type, such as `PROTO`, `TDR`, or `MIX`\n        :type IdlType: str\n        :param ClusterName: Cluster name, which can contain up to 32 letters and digits\n        :type ClusterName: str\n        :param VpcId: ID of the VPC instance bound to a cluster in the format of `vpc-f49l6u0z`\n        :type VpcId: str\n        :param SubnetId: ID of the subnet instance bound to a cluster in the format of `subnet-pxir56ns`\n        :type SubnetId: str\n        :param Password: Cluster access password, which must contain lowercase letters (a-z), uppercase letters (A-Z), and digits (0-9).\n        :type Password: str\n        :param ResourceTags: Cluster tag list\n        :type ResourceTags: list of TagInfoUnit\n        :param Ipv6Enable: Whether to enable IPv6 address access for clusters\n        :type Ipv6Enable: int\n        :param ServerList: Information of the machine at the storage layer (tcapsvr) in a dedicated cluster\n        :type ServerList: list of MachineInfo\n        :param ProxyList: Information of the machine at the access layer (tcaproxy) in a dedicated cluster\n        :type ProxyList: list of MachineInfo\n        :param ClusterType: Cluster type. Valid values: `1` (standard), `2` (dedicated)\n        :type ClusterType: int\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateSnapshotsRequest(AbstractModel):
    """CreateSnapshots request structure.

    """

    def __init__(self):
        """
        :param ClusterId: The ID of the cluster where the table resides\n        :type ClusterId: str\n        :param SelectedTables: Snapshot list\n        :type SelectedTables: list of SnapshotInfo\n        """
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
        """
        :param TotalCount: The number of snapshots created in batches\n        :type TotalCount: int\n        :param TableResults: The result list of snapshots created in batches\n        :type TableResults: list of SnapshotResult\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where a table group resides\n        :type ClusterId: str\n        :param TableGroupName: Table group name, which can contain up to 32 letters and digits\n        :type TableGroupName: str\n        :param TableGroupId: Table group ID, which can be customized but must be unique in one cluster. If it is not specified, the auto-increment mode will be used.\n        :type TableGroupId: str\n        :param ResourceTags: Table group tag list\n        :type ResourceTags: list of TagInfoUnit\n        """
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
        """
        :param TableGroupId: ID of table group successfully created\n        :type TableGroupId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TableGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.RequestId = params.get("RequestId")


class CreateTablesRequest(AbstractModel):
    """CreateTables request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ID of the cluster where to create a table\n        :type ClusterId: str\n        :param IdlFiles: Table creation IDL file list selected by user\n        :type IdlFiles: list of IdlFileInfo\n        :param SelectedTables: Information list of tables to be created\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param ResourceTags: Table tag list\n        :type ResourceTags: list of TagInfoUnit\n        """
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
        """
        :param TotalCount: Number of tables created in batches\n        :type TotalCount: int\n        :param TableResults: List of tables created in batches\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of cluster to be deleted\n        :type ClusterId: str\n        """
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
        """
        :param TaskId: Task ID generated by cluster deletion\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteIdlFilesRequest(AbstractModel):
    """DeleteIdlFiles request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ID of the cluster where IDL resides\n        :type ClusterId: str\n        :param IdlFiles: List of information of IDL files to be deleted\n        :type IdlFiles: list of IdlFileInfo\n        """
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
        """
        :param TotalCount: Number of returned results\n        :type TotalCount: int\n        :param IdlFileInfos: Deletion result\n        :type IdlFileInfos: list of IdlFileInfoWithoutContent\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: The ID of the cluster where the table resides\n        :type ClusterId: str\n        :param SelectedTables: The list of snapshots to delete\n        :type SelectedTables: list of SnapshotInfoNew\n        """
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
        """
        :param TotalCount: The number of snapshots deleted in batches\n        :type TotalCount: int\n        :param TableResults: The result list of snapshots deleted in batches\n        :type TableResults: list of SnapshotResult\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DeleteTableGroupRequest(AbstractModel):
    """DeleteTableGroup request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ID of the cluster where a table group resides\n        :type ClusterId: str\n        :param TableGroupId: Table group ID\n        :type TableGroupId: str\n        """
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
        """
        :param TaskId: Task ID generated by table group deletion\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteTableIndexRequest(AbstractModel):
    """DeleteTableIndex request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ID of the cluster where the table resides\n        :type ClusterId: str\n        :param SelectedTables: The list of tables whose global indexes need to be deleted\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
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
        """
        :param TotalCount: The number of tables whose global indexes are deleted\n        :type TotalCount: int\n        :param TableResults: The list of global index deletion results\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where the table to be dropped resides\n        :type ClusterId: str\n        :param SelectedTables: List of information of tables to be dropped\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
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
        """
        :param TotalCount: Number of dropped tables\n        :type TotalCount: int\n        :param TableResults: List of details of dropped tables\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ID of the cluster whose applications will be queried\n        :type ClusterId: str\n        :param Limit: The maximum number of results returned per page\n        :type Limit: int\n        :param Offset: Pagination offset\n        :type Offset: int\n        :param CensorStatus: Application status used as a filter condition\n        :type CensorStatus: int\n        :param TableGroupId: Table group ID used as a filter condition\n        :type TableGroupId: str\n        :param TableName: Table name used as a filter condition\n        :type TableName: str\n        :param Applicant: Applicant UIN used as a filter condition\n        :type Applicant: str\n        :param ApplyType: Application type used as a filter condition\n        :type ApplyType: int\n        """
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.CensorStatus = None
        self.TableGroupId = None
        self.TableName = None
        self.Applicant = None
        self.ApplyType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.CensorStatus = params.get("CensorStatus")
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.Applicant = params.get("Applicant")
        self.ApplyType = params.get("ApplyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications response structure.

    """

    def __init__(self):
        """
        :param Applications: Application list\n        :type Applications: list of Application\n        :param TotalCount: Total number of applications\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Applications = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Applications") is not None:
            self.Applications = []
            for item in params.get("Applications"):
                obj = Application()
                obj._deserialize(item)
                self.Applications.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClusterTagsRequest(AbstractModel):
    """DescribeClusterTags request structure.

    """

    def __init__(self):
        """
        :param ClusterIds: The list of cluster IDs\n        :type ClusterIds: list of str\n        """
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
        """
        :param Rows: The information list of cluster tags\n        :type Rows: list of TagsInfoOfCluster\n        :param TotalCount: The number of returned results\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterIds: List of IDs of clusters to be queried\n        :type ClusterIds: list of str\n        :param Filters: Query filter\n        :type Filters: list of Filter\n        :param Offset: Query list offset\n        :type Offset: int\n        :param Limit: Number of returned results in query list. Default value: 20\n        :type Limit: int\n        :param Ipv6Enable: Whether to enable IPv6 address access\n        :type Ipv6Enable: int\n        """
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
        """
        :param TotalCount: Number of cluster instances\n        :type TotalCount: int\n        :param Clusters: Cluster instance list\n        :type Clusters: list of ClusterInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where a file resides\n        :type ClusterId: str\n        :param TableGroupIds: ID of the table group where a file resides\n        :type TableGroupIds: list of str\n        :param IdlFileIds: File ID list\n        :type IdlFileIds: list of str\n        :param Offset: Query list offset\n        :type Offset: int\n        :param Limit: Number of returned results in query list\n        :type Limit: int\n        """
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
        """
        :param TotalCount: Number of files\n        :type TotalCount: int\n        :param IdlFileInfos: List of file details\n        :type IdlFileInfos: list of IdlFileInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Ipv6Enable: If this parameter is not `0`, machines supporting IPv6 will be queried.\n        :type Ipv6Enable: int\n        """
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
        """
        :param PoolList: The list of dedicated machine resources\n        :type PoolList: list of PoolInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TotalCount: Number of queried AZs\n        :type TotalCount: int\n        :param RegionInfos: List of AZ query results\n        :type RegionInfos: list of RegionInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: The ID of the cluster where the table resides\n        :type ClusterId: str\n        :param TableGroupId: The ID of the table group where the table resides\n        :type TableGroupId: str\n        :param TableName: Table name\n        :type TableName: str\n        :param SnapshotName: Snapshot name\n        :type SnapshotName: str\n        """
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
        """
        :param TotalCount: The number of snapshots\n        :type TotalCount: int\n        :param TableResults: The result list of snapshots\n        :type TableResults: list of SnapshotResult\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: The ID of the cluster where table group tags need to be queried\n        :type ClusterId: str\n        :param TableGroupIds: The list of IDs of the table groups whose tags need to be queried\n        :type TableGroupIds: list of str\n        """
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
        """
        :param Rows: The information list of table group tags\n        :type Rows: list of TagsInfoOfTableGroup\n        :param TotalCount: The number of returned results\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where a table group resides\n        :type ClusterId: str\n        :param TableGroupIds: Table group ID list\n        :type TableGroupIds: list of str\n        :param Filters: Filter. Valid values: TableGroupName, TableGroupId\n        :type Filters: list of Filter\n        :param Offset: Query list offset\n        :type Offset: int\n        :param Limit: Number of returned results in query list\n        :type Limit: int\n        """
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
        """
        :param TotalCount: Number of table groups\n        :type TotalCount: int\n        :param TableGroups: Table group information list\n        :type TableGroups: list of TableGroupInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: The ID of the cluster where a table resides\n        :type ClusterId: str\n        :param SelectedTables: Table list\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
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
        """
        :param TotalCount: The total number of returned results\n        :type TotalCount: int\n        :param Rows: The information list of table tags\n        :type Rows: list of TagsInfoOfTable\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where the table to be queried resides\n        :type ClusterId: str\n        :param TableGroupIds: List of IDs of the table groups where the table to be queried resides\n        :type TableGroupIds: list of str\n        :param Filters: Filter. Valid values: TableName, TableInstanceId\n        :type Filters: list of Filter\n        :param Offset: Query result offset\n        :type Offset: int\n        :param Limit: Number of returned query results\n        :type Limit: int\n        """
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
        """
        :param TotalCount: Number of tables\n        :type TotalCount: int\n        :param TableInfos: Table details result list\n        :type TableInfos: list of TableInfoNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where the table to be queried resides\n        :type ClusterId: str\n        :param TableGroupIds: List of IDs of the table groups where the table to be queried resides\n        :type TableGroupIds: list of str\n        :param SelectedTables: Information list of tables to be queried\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param Filters: Filter. Valid values: TableName, TableInstanceId\n        :type Filters: list of Filter\n        :param Offset: Query result offset\n        :type Offset: int\n        :param Limit: Number of returned query results\n        :type Limit: int\n        """
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
        """
        :param TotalCount: Number of tables\n        :type TotalCount: int\n        :param TableInfos: Table details result list\n        :type TableInfos: list of TableInfoNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterIds: List of IDs of clusters where the tasks to be queried reside\n        :type ClusterIds: list of str\n        :param TaskIds: List of IDs of tasks to be queried\n        :type TaskIds: list of str\n        :param Filters: Filter. Valid values: Content, TaskType, Operator, Time\n        :type Filters: list of Filter\n        :param Offset: Query list offset\n        :type Offset: int\n        :param Limit: Number of returned results in query list\n        :type Limit: int\n        """
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
        """
        :param TotalCount: Number of tasks\n        :type TotalCount: int\n        :param TaskInfos: List of details of queried tasks\n        :type TaskInfos: list of TaskInfoNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Result: Query result. FALSE: yes, TRUE: no\n        :type Result: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableRestProxyRequest(AbstractModel):
    """DisableRestProxy request structure.

    """

    def __init__(self):
        """
        :param ClusterId: The value is the same as `appid`.\n        :type ClusterId: str\n        """
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
        """
        :param RestProxyStatus: RestProxy status. Valid values: 0 (disabled), 1 (enabling), 2 (enabled), 3 (disabling).\n        :type RestProxyStatus: int\n        :param TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, used to identify tasks of different clusters.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: The value is the same as `appid`.\n        :type ClusterId: str\n        """
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
        """
        :param RestProxyStatus: RestProxy status. Valid values: 0 (disabled), 1 (enabling), 2 (enabled), 3 (disabling).\n        :type RestProxyStatus: int\n        :param TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, used to identify tasks of different clusters.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Code: Error code\n        :type Code: str\n        :param Message: Error message\n        :type Message: str\n        """
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
        """
        :param FieldName: Table field name\n        :type FieldName: str\n        :param IsPrimaryKey: Whether it is a primary key field\n        :type IsPrimaryKey: str\n        :param FieldType: Field type\n        :type FieldType: str\n        :param FieldSize: Field length\n        :type FieldSize: int\n        """
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
        """
        :param Name: Filter field name\n        :type Name: str\n        :param Value: Filter field value\n        :type Value: str\n        :param Values: Filter field value\n        :type Values: list of str\n        """
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
        """
        :param FileName: Filename excluding extension\n        :type FileName: str\n        :param FileType: Data interface description language (IDL) type\n        :type FileType: str\n        :param FileExtType: File extension\n        :type FileExtType: str\n        :param FileSize: File size in bytes\n        :type FileSize: int\n        :param FileId: File ID, which is meaningful for files already uploaded
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: int\n        :param FileContent: File content, which is meaningful for files to be uploaded in this request
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileContent: str\n        """
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
        """
        :param FileName: Filename excluding extension
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileName: str\n        :param FileType: Data interface description language (IDL) type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileType: str\n        :param FileExtType: File extension
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileExtType: str\n        :param FileSize: File size in bytes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileSize: int\n        :param FileId: File ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: int\n        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
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
        """
        :param ClusterId: The ID of the cluster where the original table (from which the snapshot was created) resides\n        :type ClusterId: str\n        :param Snapshots: The information of the snapshot to import\n        :type Snapshots: :class:`tencentcloud.tcaplusdb.v20190823.models.SnapshotInfo`\n        :param ImportSpecialKey: Whether to import partial data of the snapshot. Valid values: `TRUE` (import partial data), `FALSE` (import all data).\n        :type ImportSpecialKey: str\n        :param ImportOriginTable: Whether to import to the original table. Valid values: `TRUE` (import to the original table), `FALSE` (import to a new table).\n        :type ImportOriginTable: str\n        :param KeyFile: The file of the keys of the partial data\n        :type KeyFile: :class:`tencentcloud.tcaplusdb.v20190823.models.KeyFile`\n        :param NewTableGroupId: The ID of the table group where the new table resides, which is valid only when `ImportOriginTable` is set to `FALSE`\n        :type NewTableGroupId: str\n        :param NewTableName: The name of the new table, which is valid only when `ImportOriginTable` is set to `FALSE`. TcaplusDB will automatically create a table named `NewTableName` of the same structure as that of the original table.\n        :type NewTableName: str\n        """
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
        """
        :param TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, used to identify tasks of different clusters.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class KeyFile(AbstractModel):
    """The file of keys used to import partial snapshot data

    """

    def __init__(self):
        """
        :param FileName: Key file name\n        :type FileName: str\n        :param FileExtType: Key file extension\n        :type FileExtType: str\n        :param FileContent: Key file content\n        :type FileContent: str\n        :param FileSize: Key file size\n        :type FileSize: int\n        """
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
        """
        :param MachineType: Machine type\n        :type MachineType: str\n        :param MachineNum: Machine quantity\n        :type MachineNum: int\n        """
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
        """
        :param TaskId: Task ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type TaskId: str\n        :param Error: If table merging is successful, `null` will be returned
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param Table: Comparison results of tables\n        :type Table: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`\n        :param ApplicationId: Application ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ApplicationId: str\n        """
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
        """
        :param SelectedTables: Tables to be merged\n        :type SelectedTables: list of MergeTablesInfo\n        :param IsOnlyCompare: Valid values: `true` (only compare), `false` (compare and merge)\n        :type IsOnlyCompare: bool\n        """
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
        """
        :param Results: Table merging results\n        :type Results: list of MergeTableResult\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param MergeTables: Information of tables to be merged\n        :type MergeTables: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`\n        :param CheckIndex: Whether to check indexes\n        :type CheckIndex: bool\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param Censorship: Whether to enable the operation approval feature for this cluster. Valid values: `0` (disable), `1` (enable)\n        :type Censorship: int\n        :param Uins: Approver UIN list\n        :type Uins: list of str\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param Uins: Approver UIN list
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Uins: list of str\n        :param Censorship: Whether the operation approval feature is enabled for this cluster. Valid values: `0` (disabled), `1` (enabled)\n        :type Censorship: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param ServerList: Information of the machines at the storage layer (tcapsvr)\n        :type ServerList: list of MachineInfo\n        :param ProxyList: Information of the machines at the access layer (tcaproxy)\n        :type ProxyList: list of MachineInfo\n        :param ClusterType: Cluster type. Valid values: `1` (standard), `2` (dedicated)\n        :type ClusterType: int\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ID of the cluster to be renamed\n        :type ClusterId: str\n        :param ClusterName: Cluster name to be changed to, which can contain up to 32 letters and digits\n        :type ClusterName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterPasswordRequest(AbstractModel):
    """ModifyClusterPassword request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ID of the cluster for which to modify the password\n        :type ClusterId: str\n        :param OldPassword: Old cluster password\n        :type OldPassword: str\n        :param OldPasswordExpireTime: Expected expiration time of old cluster password\n        :type OldPasswordExpireTime: str\n        :param NewPassword: New cluster password, which must contain lowercase letters (a-z), uppercase letters (A-Z), and digits (0-9).\n        :type NewPassword: str\n        :param Mode: Update mode. 1: updates password, 2: updates old password expiration time. Default value: 1\n        :type Mode: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterTagsRequest(AbstractModel):
    """ModifyClusterTags request structure.

    """

    def __init__(self):
        """
        :param ClusterId: The ID of the cluster whose tags need to be modified\n        :type ClusterId: str\n        :param ReplaceTags: The list of tags to add or modify\n        :type ReplaceTags: list of TagInfoUnit\n        :param DeleteTags: Tags to delete\n        :type DeleteTags: list of TagInfoUnit\n        """
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
        """
        :param TaskId: Task ID\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifySnapshotsRequest(AbstractModel):
    """ModifySnapshots request structure.

    """

    def __init__(self):
        """
        :param ClusterId: The ID of the cluster where the table resides\n        :type ClusterId: str\n        :param SelectedTables: Snapshot list\n        :type SelectedTables: list of SnapshotInfoNew\n        """
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
        """
        :param TotalCount: The number of snapshots modified in batches\n        :type TotalCount: int\n        :param TableResults: The result list of snapshots modified in batches\n        :type TableResults: list of SnapshotResult\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where a table group resides\n        :type ClusterId: str\n        :param TableGroupId: ID of the table group to be renamed\n        :type TableGroupId: str\n        :param TableGroupName: New table group name, which can contain letters and symbols\n        :type TableGroupName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTableGroupTagsRequest(AbstractModel):
    """ModifyTableGroupTags request structure.

    """

    def __init__(self):
        """
        :param ClusterId: The ID of the cluster where table group tags need to be modified\n        :type ClusterId: str\n        :param TableGroupId: The ID of the table group whose tags need to be modified\n        :type TableGroupId: str\n        :param ReplaceTags: The list of tags to add or modify\n        :type ReplaceTags: list of TagInfoUnit\n        :param DeleteTags: Tags to delete\n        :type DeleteTags: list of TagInfoUnit\n        """
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
        """
        :param TaskId: Task ID\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyTableMemosRequest(AbstractModel):
    """ModifyTableMemos request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ID of the cluster instance where a table resides\n        :type ClusterId: str\n        :param TableMemos: List of details of selected tables\n        :type TableMemos: list of SelectedTableInfoNew\n        """
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
        """
        :param TotalCount: Number of tables modified for remarks\n        :type TotalCount: int\n        :param TableResults: List of table remarks modification results\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where the table to be scaled resides\n        :type ClusterId: str\n        :param TableQuotas: List of quotas of tables selected for modification\n        :type TableQuotas: list of SelectedTableInfoNew\n        """
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
        """
        :param TotalCount: Number of scaled tables\n        :type TotalCount: int\n        :param TableResults: List of table scaling results\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: The ID of the cluster where table tags need to be modified\n        :type ClusterId: str\n        :param SelectedTables: The list of tables whose tags need to be modified\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param ReplaceTags: The list of tags to add or modify\n        :type ReplaceTags: list of TagInfoUnit\n        :param DeleteTags: The list of tags to delete\n        :type DeleteTags: list of TagInfoUnit\n        """
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
        """
        :param TotalCount: The total number of returned results\n        :type TotalCount: int\n        :param TableResults: Returned results\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where the table to be modified resides\n        :type ClusterId: str\n        :param IdlFiles: Selected table modification IDL files\n        :type IdlFiles: list of IdlFileInfo\n        :param SelectedTables: List of tables to be modified\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
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
        """
        :param TotalCount: Number of modified tables\n        :type TotalCount: int\n        :param TableResults: List of table modification results\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TableIdlType: Table description language type. Valid values: PROTO, TDR
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableIdlType: str\n        :param TableInstanceId: Table instance ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableInstanceId: str\n        :param TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableName: str\n        :param TableType: Table data structure type. Valid values: GENERIC, LIST
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableType: str\n        :param KeyFields: Primary key field information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyFields: str\n        :param OldKeyFields: Old primary key field information, which is valid during verification of table modification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OldKeyFields: str\n        :param ValueFields: Non-primary key field information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ValueFields: str\n        :param OldValueFields: Old non-primary key field information, which is valid during verification of table modification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OldValueFields: str\n        :param TableGroupId: Table group ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableGroupId: str\n        :param SumKeyFieldSize: Total size of primary key field
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SumKeyFieldSize: int\n        :param SumValueFieldSize: Total size of non-primary key fields
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SumValueFieldSize: int\n        :param IndexKeySet: Index key set
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IndexKeySet: str\n        :param ShardingKeySet: Shardkey set
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ShardingKeySet: str\n        :param TdrVersion: TDR version number
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TdrVersion: int\n        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param ListElementNum: Number of LIST-type table elements
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ListElementNum: int\n        :param SortFieldNum: Number of SORTLIST-type table sort fields
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SortFieldNum: int\n        :param SortRule: Sort order of SORTLIST-type tables
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SortRule: int\n        """
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
        """
        :param PoolUid: Unique ID\n        :type PoolUid: int\n        :param Ipv6Enable: Whether IPv6 is supported\n        :type Ipv6Enable: int\n        :param AvailableAppCount: Remaining available cluster resources\n        :type AvailableAppCount: int\n        :param ServerList: The list of machines at the storage layer (tcapsvr)\n        :type ServerList: list of ServerMachineInfo\n        :param ProxyList: The list of machines at the access layer (tcaproxy)\n        :type ProxyList: list of ProxyMachineInfo\n        """
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
        """
        :param ProxyUid: The unique ID of the access layer (tcaproxy)\n        :type ProxyUid: str\n        :param MachineType: Machine type\n        :type MachineType: str\n        :param ProcessSpeed: The speed of processing request packets\n        :type ProcessSpeed: int\n        :param AverageProcessDelay: Request packet delay\n        :type AverageProcessDelay: int\n        :param SlowProcessSpeed: The speed of processing delayed request packets\n        :type SlowProcessSpeed: int\n        """
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
        """
        :param ProxyUid: Unique ID\n        :type ProxyUid: str\n        :param MachineType: Machine type\n        :type MachineType: str\n        """
        self.ProxyUid = None
        self.MachineType = None


    def _deserialize(self, params):
        self.ProxyUid = params.get("ProxyUid")
        self.MachineType = params.get("MachineType")
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
        """
        :param ClusterId: ID of the cluster where a table resides\n        :type ClusterId: str\n        :param SelectedTables: Information of tables to be recovered\n        :type SelectedTables: list of SelectedTableInfoNew\n        """
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
        """
        :param TotalCount: Number of recovered tables\n        :type TotalCount: int\n        :param TableResults: List of information of recovered tables\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param RegionName: Region `Ap-code`\n        :type RegionName: str\n        :param RegionAbbr: Region abbreviation\n        :type RegionAbbr: str\n        :param RegionId: Region ID\n        :type RegionId: int\n        :param Ipv6Enable: Whether to support IPv6 address access. Valid values: 0 (support), 1 (not support)\n        :type Ipv6Enable: int\n        """
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
        """
        :param ClusterId: ID of the cluster where the table to be rolled back resides\n        :type ClusterId: str\n        :param SelectedTables: List of tables to be rolled back\n        :type SelectedTables: list of SelectedTableInfoNew\n        :param RollbackTime: Time to roll back to\n        :type RollbackTime: str\n        :param Mode: Rollback mode. `KEYS` is supported\n        :type Mode: str\n        """
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
        """
        :param TotalCount: Number of table rollback task results\n        :type TotalCount: int\n        :param TableResults: Table rollback task result list\n        :type TableResults: list of TableRollbackResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TableGroupId: ID of the table group where a table resides\n        :type TableGroupId: str\n        :param TableName: Table name\n        :type TableName: str\n        :param TableInstanceId: Table instance ID\n        :type TableInstanceId: str\n        :param TableIdlType: Table description language type. Valid values: PROTO, TDR\n        :type TableIdlType: str\n        :param TableType: Table data structure type. Valid values: GENERIC, LIST\n        :type TableType: str\n        :param ListElementNum: Number of LIST-type table elements\n        :type ListElementNum: int\n        :param ReservedVolume: Reserved table capacity in GB\n        :type ReservedVolume: int\n        :param ReservedReadQps: Reserved table read QPS\n        :type ReservedReadQps: int\n        :param ReservedWriteQps: Reserved table write QPS\n        :type ReservedWriteQps: int\n        :param Memo: Table remarks\n        :type Memo: str\n        :param FileName: Key rollback filename, which is only used for rollback\n        :type FileName: str\n        :param FileExtType: Key rollback file extension, which is only used for rollback\n        :type FileExtType: str\n        :param FileSize: Key rollback file size, which is only used for rollback\n        :type FileSize: int\n        :param FileContent: Key rollback file content, which is only used for rollback\n        :type FileContent: str\n        """
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
        """
        :param TableGroupId: ID of the table group where the table resides\n        :type TableGroupId: str\n        :param TableName: Table name\n        :type TableName: str\n        :param TableInstanceId: Table ID\n        :type TableInstanceId: str\n        :param TableIdlType: Table description language. Valid values: `PROTO`, `TDR`\n        :type TableIdlType: str\n        :param TableType: Table data structure. Valid values: `GENERIC`, `LIST`\n        :type TableType: str\n        :param SelectedFields: The list of fields on which indexes need to be created\n        :type SelectedFields: list of FieldInfo\n        :param ShardNum: The number of index shards\n        :type ShardNum: int\n        """
        self.TableGroupId = None
        self.TableName = None
        self.TableInstanceId = None
        self.TableIdlType = None
        self.TableType = None
        self.SelectedFields = None
        self.ShardNum = None


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
        """
        :param ServerUid: The unique ID of the storage layer (tcapsvr)\n        :type ServerUid: str\n        :param MachineType: Machine type\n        :type MachineType: str\n        :param MemoryRate: Memory utilization\n        :type MemoryRate: int\n        :param DiskRate: Disk utilization\n        :type DiskRate: int\n        :param ReadNum: The number of reads\n        :type ReadNum: int\n        :param WriteNum: The number of writes\n        :type WriteNum: int\n        """
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
        """
        :param ServerUid: The unique ID of the machine\n        :type ServerUid: str\n        :param MachineType: Machine type\n        :type MachineType: str\n        """
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
        


class SetTableIndexRequest(AbstractModel):
    """SetTableIndex request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ID of the cluster where the table resides\n        :type ClusterId: str\n        :param SelectedTables: The list of tables that need to create global indexes\n        :type SelectedTables: list of SelectedTableWithField\n        """
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
        """
        :param TotalCount: The number of tables whose global indexes are created\n        :type TotalCount: int\n        :param TableResults: The list of global index creation results\n        :type TableResults: list of TableResultNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TableGroupId: The ID of the table group where the table resides\n        :type TableGroupId: str\n        :param TableName: Table name\n        :type TableName: str\n        :param SnapshotName: Snapshot name\n        :type SnapshotName: str\n        :param SnapshotTime: The time of the data from which the snapshot was created\n        :type SnapshotTime: str\n        :param SnapshotDeadTime: Snapshot expiration time\n        :type SnapshotDeadTime: str\n        """
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
        """
        :param TableGroupId: The ID of the table group where the table resides\n        :type TableGroupId: str\n        :param TableName: Table name\n        :type TableName: str\n        :param SnapshotName: Snapshot name\n        :type SnapshotName: str\n        :param SnapshotDeadTime: Snapshot expiration time\n        :type SnapshotDeadTime: str\n        """
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
        """
        :param TableGroupId: The ID of the table group where the table resides
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type TableGroupId: str\n        :param TableName: Table name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type TableName: str\n        :param TaskId: Task ID, which is valid for the API that creates one task at a time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type TaskId: str\n        :param Error: Error information
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param SnapshotName: Snapshot name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type SnapshotName: str\n        :param SnapshotTime: The time of the data from which the snapshot was created
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type SnapshotTime: str\n        :param SnapshotDeadTime: When the snapshot expires
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type SnapshotDeadTime: str\n        :param SnapshotCreateTime: When the snapshot was created
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type SnapshotCreateTime: str\n        :param SnapshotSize: Snapshot size
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type SnapshotSize: int\n        :param SnapshotStatus: Snapshot status. Valid values: `0` (creating), `1` (normal), `2` (deleting), `3` (expired), `4` (rolling back).
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type SnapshotStatus: int\n        """
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
        


class TableGroupInfo(AbstractModel):
    """Table group details

    """

    def __init__(self):
        """
        :param TableGroupId: Table group ID\n        :type TableGroupId: str\n        :param TableGroupName: Table group name\n        :type TableGroupName: str\n        :param CreatedTime: Table group creation time\n        :type CreatedTime: str\n        :param TableCount: Number of tables in table group\n        :type TableCount: int\n        :param TotalSize: Total table storage capacity in MB in table group\n        :type TotalSize: int\n        """
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
        """
        :param TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableName: str\n        :param TableInstanceId: Table instance ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableInstanceId: str\n        :param TableType: Table data structure type, such as `GENERIC` or `LIST`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableType: str\n        :param TableIdlType: Table data interface description language (IDL) type, such as `PROTO` or `TDR`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableIdlType: str\n        :param ClusterId: ID of the cluster where a table resides
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClusterId: str\n        :param ClusterName: Name of the cluster where a table resides
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClusterName: str\n        :param TableGroupId: ID of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableGroupId: str\n        :param TableGroupName: Name of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableGroupName: str\n        :param KeyStruct: JSON string of table's primary key field structure
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyStruct: str\n        :param ValueStruct: JSON string of table non-primary key field structure
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ValueStruct: str\n        :param ShardingKeySet: Table shardkey set, which is valid for PROTO-type tables
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ShardingKeySet: str\n        :param IndexStruct: Table index key field set, which is valid for PROTO-type tables
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IndexStruct: str\n        :param ListElementNum: Number of LIST-type table elements
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ListElementNum: int\n        :param IdlFiles: Information list of IDL files associated with table
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IdlFiles: list of IdlFileInfo\n        :param ReservedVolume: Reserved table capacity in GB
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReservedVolume: int\n        :param ReservedReadQps: Reserved table read QPS
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReservedReadQps: int\n        :param ReservedWriteQps: Reserved table write QPS
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReservedWriteQps: int\n        :param TableSize: Actual table data size in MB
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableSize: int\n        :param Status: Table status
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: str\n        :param CreatedTime: Table creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        :param UpdatedTime: Table's last modified time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UpdatedTime: str\n        :param Memo: Table remarks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Memo: str\n        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param ApiAccessId: TcaplusDB SDK data access ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApiAccessId: str\n        :param SortFieldNum: Number of SORTLIST-type table sort fields
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SortFieldNum: int\n        :param SortRule: Sort order of SORTLIST-type tables
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SortRule: int\n        :param DbClusterInfoStruct: Distributed index information of table\n        :type DbClusterInfoStruct: str\n        """
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
        """
        :param TableInstanceId: Table instance ID in the format of `tcaplus-3be64cbb`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableInstanceId: str\n        :param TaskId: Task ID, which is valid for the API that creates one task
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskId: str\n        :param TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableName: str\n        :param TableType: Table data structure type, such as `GENERIC` or `LIST`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableType: str\n        :param TableIdlType: Table data interface description language (IDL) type, such as `PROTO` or `TDR`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableIdlType: str\n        :param TableGroupId: ID of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableGroupId: str\n        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param TaskIds: Task ID list, which is valid for the API that creates multiple tasks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskIds: list of str\n        :param ApplicationId: Cluster operation application ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ApplicationId: str\n        """
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
        """
        :param TableInstanceId: Table instance ID in the format of `tcaplus-3be64cbb`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableInstanceId: str\n        :param TaskId: Task ID, which is valid for the API that creates one task
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskId: str\n        :param TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableName: str\n        :param TableType: Table data structure type, such as `GENERIC` or `LIST`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableType: str\n        :param TableIdlType: Table data interface description language (IDL) type, such as `PROTO` or `TDR`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableIdlType: str\n        :param TableGroupId: ID of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TableGroupId: str\n        :param Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        :param TaskIds: Task ID list, which is valid for the API that creates multiple tasks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskIds: list of str\n        :param FileId: ID of uploaded key file
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: str\n        :param SuccKeyNum: Number of keys successfully verified
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SuccKeyNum: int\n        :param TotalKeyNum: Total number of keys contained in key file
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalKeyNum: int\n        """
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
        """
        :param TagKey: Tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: str\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param Tags: Tag information\n        :type Tags: list of TagInfoUnit\n        :param Error: Error message\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
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
        """
        :param TableInstanceId: Table instance ID\n        :type TableInstanceId: str\n        :param TableName: Table name\n        :type TableName: str\n        :param TableGroupId: Table group ID\n        :type TableGroupId: str\n        :param Tags: Tag information\n        :type Tags: list of TagInfoUnit\n        :param Error: Error message\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
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
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: str\n        :param TableGroupId: Table group ID\n        :type TableGroupId: str\n        :param Tags: Tag information\n        :type Tags: list of TagInfoUnit\n        :param Error: Error message\n        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`\n        """
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
        """
        :param TaskId: Task ID\n        :type TaskId: str\n        :param TaskType: Task type\n        :type TaskType: str\n        :param TransId: ID of TcaplusDB internal transaction associated with task\n        :type TransId: str\n        :param ClusterId: ID of the cluster where a task resides\n        :type ClusterId: str\n        :param ClusterName: Name of the cluster where a task resides\n        :type ClusterName: str\n        :param Progress: Task progress\n        :type Progress: int\n        :param StartTime: Task creation time\n        :type StartTime: str\n        :param UpdateTime: Task last modified time\n        :type UpdateTime: str\n        :param Operator: Operator\n        :type Operator: str\n        :param Content: Task details\n        :type Content: str\n        """
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
        """
        :param ApplyStatus: Application status\n        :type ApplyStatus: list of ApplyStatus\n        """
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
        """
        :param ApplyResults: List of updated applications
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ApplyResults: list of ApplyResult\n        :param TotalCount: Total number of updated applications\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ClusterId: ID of the cluster where to create a table\n        :type ClusterId: str\n        :param TableGroupId: ID of the table group where to create a table\n        :type TableGroupId: str\n        :param ExistingIdlFiles: List of information of uploaded IDL files. Either this parameter or `NewIdlFiles` must be present\n        :type ExistingIdlFiles: list of IdlFileInfo\n        :param NewIdlFiles: List of information of IDL files to be uploaded. Either this parameter or `ExistingIdlFiles` must be present\n        :type NewIdlFiles: list of IdlFileInfo\n        """
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
        """
        :param IdlFiles: Information list of all IDL files uploaded and verified in this request\n        :type IdlFiles: list of IdlFileInfo\n        :param TotalCount: Number of valid tables parsed by reading IDL description file, excluding tables already created\n        :type TotalCount: int\n        :param TableInfos: List of valid tables parsed by reading IDL description file, excluding tables already created\n        :type TableInfos: list of ParsedTableInfoNew\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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