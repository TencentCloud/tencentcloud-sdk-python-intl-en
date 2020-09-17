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


class ClearTablesRequest(AbstractModel):
    """ClearTables request structure.

    """

    def __init__(self):
        """
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


class ClearTablesResponse(AbstractModel):
    """ClearTables response structure.

    """

    def __init__(self):
        """
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
        """
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


class CompareIdlFilesRequest(AbstractModel):
    """CompareIdlFiles request structure.

    """

    def __init__(self):
        """
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


class CompareIdlFilesResponse(AbstractModel):
    """CompareIdlFiles response structure.

    """

    def __init__(self):
        """
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


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        """
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


class CreateBackupResponse(AbstractModel):
    """CreateBackup response structure.

    """

    def __init__(self):
        """
        :param TaskIds: List of IDs of created backup tasks
        :type TaskIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster request structure.

    """

    def __init__(self):
        """
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
        """
        self.IdlType = None
        self.ClusterName = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.ResourceTags = None
        self.Ipv6Enable = None


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


class CreateClusterResponse(AbstractModel):
    """CreateCluster response structure.

    """

    def __init__(self):
        """
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


class CreateTableGroupRequest(AbstractModel):
    """CreateTableGroup request structure.

    """

    def __init__(self):
        """
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


class CreateTableGroupResponse(AbstractModel):
    """CreateTableGroup response structure.

    """

    def __init__(self):
        """
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
        """
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


class CreateTablesResponse(AbstractModel):
    """CreateTables response structure.

    """

    def __init__(self):
        """
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
        """
        :param ClusterId: ID of cluster to be deleted
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster response structure.

    """

    def __init__(self):
        """
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
        """
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


class DeleteIdlFilesResponse(AbstractModel):
    """DeleteIdlFiles response structure.

    """

    def __init__(self):
        """
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


class DeleteTableGroupRequest(AbstractModel):
    """DeleteTableGroup request structure.

    """

    def __init__(self):
        """
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


class DeleteTableGroupResponse(AbstractModel):
    """DeleteTableGroup response structure.

    """

    def __init__(self):
        """
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


class DeleteTablesRequest(AbstractModel):
    """DeleteTables request structure.

    """

    def __init__(self):
        """
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


class DeleteTablesResponse(AbstractModel):
    """DeleteTables response structure.

    """

    def __init__(self):
        """
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
        """
        :param ClusterIds: The list of cluster IDs
        :type ClusterIds: list of str
        """
        self.ClusterIds = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")


class DescribeClusterTagsResponse(AbstractModel):
    """DescribeClusterTags response structure.

    """

    def __init__(self):
        """
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
        """
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


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters response structure.

    """

    def __init__(self):
        """
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
        """
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


class DescribeIdlFileInfosResponse(AbstractModel):
    """DescribeIdlFileInfos response structure.

    """

    def __init__(self):
        """
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


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        """
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


class DescribeTableGroupTagsRequest(AbstractModel):
    """DescribeTableGroupTags request structure.

    """

    def __init__(self):
        """
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


class DescribeTableGroupTagsResponse(AbstractModel):
    """DescribeTableGroupTags response structure.

    """

    def __init__(self):
        """
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
        """
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


class DescribeTableGroupsResponse(AbstractModel):
    """DescribeTableGroups response structure.

    """

    def __init__(self):
        """
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
        """
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


class DescribeTableTagsResponse(AbstractModel):
    """DescribeTableTags response structure.

    """

    def __init__(self):
        """
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
        """
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


class DescribeTablesInRecycleResponse(AbstractModel):
    """DescribeTablesInRecycle response structure.

    """

    def __init__(self):
        """
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
        """
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


class DescribeTablesResponse(AbstractModel):
    """DescribeTables response structure.

    """

    def __init__(self):
        """
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
        """
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


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks response structure.

    """

    def __init__(self):
        """
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
        """
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


class ErrorInfo(AbstractModel):
    """Describes the details of errors that may occur during the processing of each instance (application, region, or table).

    """

    def __init__(self):
        """
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


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        """
        :param Name: Filter field name
        :type Name: str
        :param Value: Filter field value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class IdlFileInfo(AbstractModel):
    """Table definition file details, including file content

    """

    def __init__(self):
        """
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


class IdlFileInfoWithoutContent(AbstractModel):
    """Table definition file details, excluding file content

    """

    def __init__(self):
        """
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


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName request structure.

    """

    def __init__(self):
        """
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


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName response structure.

    """

    def __init__(self):
        """
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
        """
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


class ModifyClusterPasswordResponse(AbstractModel):
    """ModifyClusterPassword response structure.

    """

    def __init__(self):
        """
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
        """
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


class ModifyClusterTagsResponse(AbstractModel):
    """ModifyClusterTags response structure.

    """

    def __init__(self):
        """
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


class ModifyTableGroupNameRequest(AbstractModel):
    """ModifyTableGroupName request structure.

    """

    def __init__(self):
        """
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


class ModifyTableGroupNameResponse(AbstractModel):
    """ModifyTableGroupName response structure.

    """

    def __init__(self):
        """
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
        """
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


class ModifyTableGroupTagsResponse(AbstractModel):
    """ModifyTableGroupTags response structure.

    """

    def __init__(self):
        """
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
        """
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


class ModifyTableMemosResponse(AbstractModel):
    """ModifyTableMemos response structure.

    """

    def __init__(self):
        """
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
        """
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


class ModifyTableQuotasResponse(AbstractModel):
    """ModifyTableQuotas response structure.

    """

    def __init__(self):
        """
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
        """
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


class ModifyTableTagsResponse(AbstractModel):
    """ModifyTableTags response structure.

    """

    def __init__(self):
        """
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
        """
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


class ModifyTablesResponse(AbstractModel):
    """ModifyTables response structure.

    """

    def __init__(self):
        """
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
        """
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


class RecoverRecycleTablesRequest(AbstractModel):
    """RecoverRecycleTables request structure.

    """

    def __init__(self):
        """
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


class RecoverRecycleTablesResponse(AbstractModel):
    """RecoverRecycleTables response structure.

    """

    def __init__(self):
        """
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
        """
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


class RollbackTablesRequest(AbstractModel):
    """RollbackTables request structure.

    """

    def __init__(self):
        """
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


class RollbackTablesResponse(AbstractModel):
    """RollbackTables response structure.

    """

    def __init__(self):
        """
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
        """
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


class TableGroupInfo(AbstractModel):
    """Table group details

    """

    def __init__(self):
        """
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


class TableInfoNew(AbstractModel):
    """Table details

    """

    def __init__(self):
        """
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
        :param DbClusterInfoStruct: Distributed index information of table
        :type DbClusterInfoStruct: str
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


class TableResultNew(AbstractModel):
    """Table processing result information

    """

    def __init__(self):
        """
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
        """
        self.TableInstanceId = None
        self.TaskId = None
        self.TableName = None
        self.TableType = None
        self.TableIdlType = None
        self.TableGroupId = None
        self.Error = None
        self.TaskIds = None


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


class TableRollbackResultNew(AbstractModel):
    """Table rollback result information

    """

    def __init__(self):
        """
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


class TagInfoUnit(AbstractModel):
    """Tag information unit

    """

    def __init__(self):
        """
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


class TagsInfoOfCluster(AbstractModel):
    """Cluster tag information

    """

    def __init__(self):
        """
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


class TagsInfoOfTable(AbstractModel):
    """Table tag information

    """

    def __init__(self):
        """
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


class TagsInfoOfTableGroup(AbstractModel):
    """Table group tag information

    """

    def __init__(self):
        """
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


class TaskInfoNew(AbstractModel):
    """Task details

    """

    def __init__(self):
        """
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


class VerifyIdlFilesRequest(AbstractModel):
    """VerifyIdlFiles request structure.

    """

    def __init__(self):
        """
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


class VerifyIdlFilesResponse(AbstractModel):
    """VerifyIdlFiles response structure.

    """

    def __init__(self):
        """
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