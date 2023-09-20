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
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _ApplicationType: Application type
        :type ApplicationType: int
        :param _ApplicationStatus: Status. Valid values: `0` (pending approval), `1` (application approved and task submitted), `2` (rejected)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplicationStatus: int
        :param _TaskId: ID of the submitted task
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _Error: Error information
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._ApplicationId = None
        self._ApplicationType = None
        self._ApplicationStatus = None
        self._TaskId = None
        self._Error = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ApplicationStatus(self):
        return self._ApplicationStatus

    @ApplicationStatus.setter
    def ApplicationStatus(self, ApplicationStatus):
        self._ApplicationStatus = ApplicationStatus

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationType = params.get("ApplicationType")
        self._ApplicationStatus = params.get("ApplicationStatus")
        self._TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyStatus(AbstractModel):
    """Application ID and status

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Value format: cluster ID-application ID
        :type ApplicationId: str
        :param _ApplicationStatus: Status. Valid values: `-1` (canceled), `0` (pending approval), `1` (application approved and task submitted), `2` (rejected). Only applications in the pending approval status can be updated.
        :type ApplicationStatus: int
        :param _ApplicationType: Application type
        :type ApplicationType: int
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._ApplicationId = None
        self._ApplicationStatus = None
        self._ApplicationType = None
        self._ClusterId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationStatus(self):
        return self._ApplicationStatus

    @ApplicationStatus.setter
    def ApplicationStatus(self, ApplicationStatus):
        self._ApplicationStatus = ApplicationStatus

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationStatus = params.get("ApplicationStatus")
        self._ApplicationType = params.get("ApplicationType")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupExpireRuleInfo(AbstractModel):
    """The details of backup retention policy
    Policy for cluster: `ClusterId` = cluster ID, TableGroupId·= `-1`, `TableName`= `-1`.
    Policy for cluster + table group: `ClusterId` = cluster ID, `TableGroupId` = table group ID, `TableName` = `-1`.
    Policy for cluster + table group + table: ClusterId` = cluster ID, `TableGroupId` = table group ID, `TableName` = table name.

    For `FileTag`, valid values: `0` (txh engine file), `1` (ulog file). When `FileTag` is set to `1`, `TableGroupId` = `-1` and `TableName` = `-1` remain unchanged.
    `ExpireDay` is an integer number falling in the range of 1 (inclusive) to 999 (exclusive).
    For `OperType, valid values: `0` (Add), `1` (Delete), `2` (Modify). The values `0` and `2` can be mixed, and the backend implementation is compatible.

    """

    def __init__(self):
        r"""
        :param _TableGroupId: The ID of the table group where the table resides
        :type TableGroupId: str
        :param _TableName: Table name
        :type TableName: str
        :param _FileTag: file tag, which is described above.
        :type FileTag: int
        :param _ExpireDay: Retention days, which is described above.
        :type ExpireDay: int
        :param _OperType: Operation type, which is described above.
        :type OperType: int
        """
        self._TableGroupId = None
        self._TableName = None
        self._FileTag = None
        self._ExpireDay = None
        self._OperType = None

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def FileTag(self):
        return self._FileTag

    @FileTag.setter
    def FileTag(self, FileTag):
        self._FileTag = FileTag

    @property
    def ExpireDay(self):
        return self._ExpireDay

    @ExpireDay.setter
    def ExpireDay(self, ExpireDay):
        self._ExpireDay = ExpireDay

    @property
    def OperType(self):
        return self._OperType

    @OperType.setter
    def OperType(self, OperType):
        self._OperType = OperType


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._FileTag = params.get("FileTag")
        self._ExpireDay = params.get("ExpireDay")
        self._OperType = params.get("OperType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupRecords(AbstractModel):
    """Backup records
    When it is used as an output parameter, each field will be filled.
    When it is used as an input parameter, each field will be filled back into the structure as it is. This API can only be called if `FIleTag` = `OSDATA`.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Table group ID
        :type ZoneId: int
        :param _TableName: Table name
        :type TableName: str
        :param _BackupType: Backup source
        :type BackupType: str
        :param _FileTag: File tag: TCAPLUS_FULL or OSDATA
        :type FileTag: str
        :param _ShardCount: Number of shards
        :type ShardCount: int
        :param _BackupBatchTime: Backup batch date
        :type BackupBatchTime: str
        :param _BackupFileSize: Total size of backup files
        :type BackupFileSize: int
        :param _BackupSuccRate: Backup success rate
        :type BackupSuccRate: str
        :param _BackupExpireTime: Backup file expiration time
        :type BackupExpireTime: str
        :param _AppId: Business ID
        :type AppId: int
        """
        self._ZoneId = None
        self._TableName = None
        self._BackupType = None
        self._FileTag = None
        self._ShardCount = None
        self._BackupBatchTime = None
        self._BackupFileSize = None
        self._BackupSuccRate = None
        self._BackupExpireTime = None
        self._AppId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def FileTag(self):
        return self._FileTag

    @FileTag.setter
    def FileTag(self, FileTag):
        self._FileTag = FileTag

    @property
    def ShardCount(self):
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def BackupBatchTime(self):
        return self._BackupBatchTime

    @BackupBatchTime.setter
    def BackupBatchTime(self, BackupBatchTime):
        self._BackupBatchTime = BackupBatchTime

    @property
    def BackupFileSize(self):
        return self._BackupFileSize

    @BackupFileSize.setter
    def BackupFileSize(self, BackupFileSize):
        self._BackupFileSize = BackupFileSize

    @property
    def BackupSuccRate(self):
        return self._BackupSuccRate

    @BackupSuccRate.setter
    def BackupSuccRate(self, BackupSuccRate):
        self._BackupSuccRate = BackupSuccRate

    @property
    def BackupExpireTime(self):
        return self._BackupExpireTime

    @BackupExpireTime.setter
    def BackupExpireTime(self, BackupExpireTime):
        self._BackupExpireTime = BackupExpireTime

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TableName = params.get("TableName")
        self._BackupType = params.get("BackupType")
        self._FileTag = params.get("FileTag")
        self._ShardCount = params.get("ShardCount")
        self._BackupBatchTime = params.get("BackupBatchTime")
        self._BackupFileSize = params.get("BackupFileSize")
        self._BackupSuccRate = params.get("BackupSuccRate")
        self._BackupExpireTime = params.get("BackupExpireTime")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearTablesRequest(AbstractModel):
    """ClearTables request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster instance where a table resides
        :type ClusterId: str
        :param _SelectedTables: List of information of tables to be cleared
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearTablesResponse(AbstractModel):
    """ClearTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of cleared tables
        :type TotalCount: int
        :param _TableResults: List of table clearing results
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ClusterInfo(AbstractModel):
    """Cluster details

    """

    def __init__(self):
        r"""
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Region: Cluster region
        :type Region: str
        :param _IdlType: Cluster data description language type, such as `PROTO`, `TDR`, or `MIX`
        :type IdlType: str
        :param _NetworkType: Network type
        :type NetworkType: str
        :param _VpcId: ID of the VPC instance with which a cluster is associated
        :type VpcId: str
        :param _SubnetId: ID of the subnet instance with which a cluster is associated
        :type SubnetId: str
        :param _CreatedTime: Creation time
        :type CreatedTime: str
        :param _Password: Cluster password
        :type Password: str
        :param _PasswordStatus: Password status
        :type PasswordStatus: str
        :param _ApiAccessId: TcaplusDB SDK connection parameter: access ID
        :type ApiAccessId: str
        :param _ApiAccessIp: TcaplusDB SDK connection parameter: access address
        :type ApiAccessIp: str
        :param _ApiAccessPort: TcaplusDB SDK connection parameter: access port
        :type ApiAccessPort: int
        :param _OldPasswordExpireTime: If `PasswordStatus` is `unmodifiable`, the old password has not expired, and this field will display its expiration time; otherwise, this field will be empty
Note: this field may return null, indicating that no valid values can be obtained.
        :type OldPasswordExpireTime: str
        :param _ApiAccessIpv6: TcaplusDB SDK connection parameter for accessing IPv6 addresses
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAccessIpv6: str
        :param _ClusterType: Cluster type. Valid values: `0` and `1` (shared cluster), `2` (dedicated cluster).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterType: int
        :param _ClusterStatus: Cluster status. Valid values: `0` (Running), `1` (Isolated. This status is caused by overdue payments), `2` (To be repossessed. This status is caused when the cluster is actively deleted.),·`3` (To be released. The resources occupied by the table can be released in this status.), `4` (Modifying).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterStatus: int
        :param _ReadCapacityUnit: Read CU
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReadCapacityUnit: int
        :param _WriteCapacityUnit: Write CU
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WriteCapacityUnit: int
        :param _DiskVolume: Disk capacity
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiskVolume: int
        :param _ServerList: Information of the machine at the storage layer (tcapsvr) in a dedicated cluster
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ServerList: list of ServerDetailInfo
        :param _ProxyList: Information of the machine at the access layer (tcaproxy) in a dedicated cluster
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProxyList: list of ProxyDetailInfo
        :param _Censorship: Whether the cluster operation approval feature is enabled. Valid values: `0` (disabled), `1` (enabled)
        :type Censorship: int
        :param _DbaUins: Approver UIN list
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type DbaUins: list of str
        :param _DataFlowStatus: Whether data subscription is enabled
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DataFlowStatus: int
        :param _KafkaInfo: CKafka information when data subscription is enabled
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type KafkaInfo: :class:`tencentcloud.tcaplusdb.v20190823.models.KafkaInfo`
        :param _TxhBackupExpireDay: The number of days after which the cluster Txh backup file will expire and be deleted.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TxhBackupExpireDay: int
        :param _UlogBackupExpireDay: The number of days after which the cluster Ulog backup file will expire and be deleted.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UlogBackupExpireDay: int
        :param _IsReadOnlyUlogBackupExpireDay: Whether the expiration policy of cluster Ulog backup file is read-only. `0`: Yes; `1`: No.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsReadOnlyUlogBackupExpireDay: int
        :param _RestProxyStatus: restproxy Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type RestProxyStatus: int
        """
        self._ClusterName = None
        self._ClusterId = None
        self._Region = None
        self._IdlType = None
        self._NetworkType = None
        self._VpcId = None
        self._SubnetId = None
        self._CreatedTime = None
        self._Password = None
        self._PasswordStatus = None
        self._ApiAccessId = None
        self._ApiAccessIp = None
        self._ApiAccessPort = None
        self._OldPasswordExpireTime = None
        self._ApiAccessIpv6 = None
        self._ClusterType = None
        self._ClusterStatus = None
        self._ReadCapacityUnit = None
        self._WriteCapacityUnit = None
        self._DiskVolume = None
        self._ServerList = None
        self._ProxyList = None
        self._Censorship = None
        self._DbaUins = None
        self._DataFlowStatus = None
        self._KafkaInfo = None
        self._TxhBackupExpireDay = None
        self._UlogBackupExpireDay = None
        self._IsReadOnlyUlogBackupExpireDay = None
        self._RestProxyStatus = None

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def IdlType(self):
        return self._IdlType

    @IdlType.setter
    def IdlType(self, IdlType):
        self._IdlType = IdlType

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

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
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordStatus(self):
        return self._PasswordStatus

    @PasswordStatus.setter
    def PasswordStatus(self, PasswordStatus):
        self._PasswordStatus = PasswordStatus

    @property
    def ApiAccessId(self):
        return self._ApiAccessId

    @ApiAccessId.setter
    def ApiAccessId(self, ApiAccessId):
        self._ApiAccessId = ApiAccessId

    @property
    def ApiAccessIp(self):
        return self._ApiAccessIp

    @ApiAccessIp.setter
    def ApiAccessIp(self, ApiAccessIp):
        self._ApiAccessIp = ApiAccessIp

    @property
    def ApiAccessPort(self):
        return self._ApiAccessPort

    @ApiAccessPort.setter
    def ApiAccessPort(self, ApiAccessPort):
        self._ApiAccessPort = ApiAccessPort

    @property
    def OldPasswordExpireTime(self):
        return self._OldPasswordExpireTime

    @OldPasswordExpireTime.setter
    def OldPasswordExpireTime(self, OldPasswordExpireTime):
        self._OldPasswordExpireTime = OldPasswordExpireTime

    @property
    def ApiAccessIpv6(self):
        return self._ApiAccessIpv6

    @ApiAccessIpv6.setter
    def ApiAccessIpv6(self, ApiAccessIpv6):
        self._ApiAccessIpv6 = ApiAccessIpv6

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def ReadCapacityUnit(self):
        return self._ReadCapacityUnit

    @ReadCapacityUnit.setter
    def ReadCapacityUnit(self, ReadCapacityUnit):
        self._ReadCapacityUnit = ReadCapacityUnit

    @property
    def WriteCapacityUnit(self):
        return self._WriteCapacityUnit

    @WriteCapacityUnit.setter
    def WriteCapacityUnit(self, WriteCapacityUnit):
        self._WriteCapacityUnit = WriteCapacityUnit

    @property
    def DiskVolume(self):
        return self._DiskVolume

    @DiskVolume.setter
    def DiskVolume(self, DiskVolume):
        self._DiskVolume = DiskVolume

    @property
    def ServerList(self):
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def ProxyList(self):
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList

    @property
    def Censorship(self):
        return self._Censorship

    @Censorship.setter
    def Censorship(self, Censorship):
        self._Censorship = Censorship

    @property
    def DbaUins(self):
        return self._DbaUins

    @DbaUins.setter
    def DbaUins(self, DbaUins):
        self._DbaUins = DbaUins

    @property
    def DataFlowStatus(self):
        return self._DataFlowStatus

    @DataFlowStatus.setter
    def DataFlowStatus(self, DataFlowStatus):
        self._DataFlowStatus = DataFlowStatus

    @property
    def KafkaInfo(self):
        return self._KafkaInfo

    @KafkaInfo.setter
    def KafkaInfo(self, KafkaInfo):
        self._KafkaInfo = KafkaInfo

    @property
    def TxhBackupExpireDay(self):
        return self._TxhBackupExpireDay

    @TxhBackupExpireDay.setter
    def TxhBackupExpireDay(self, TxhBackupExpireDay):
        self._TxhBackupExpireDay = TxhBackupExpireDay

    @property
    def UlogBackupExpireDay(self):
        return self._UlogBackupExpireDay

    @UlogBackupExpireDay.setter
    def UlogBackupExpireDay(self, UlogBackupExpireDay):
        self._UlogBackupExpireDay = UlogBackupExpireDay

    @property
    def IsReadOnlyUlogBackupExpireDay(self):
        return self._IsReadOnlyUlogBackupExpireDay

    @IsReadOnlyUlogBackupExpireDay.setter
    def IsReadOnlyUlogBackupExpireDay(self, IsReadOnlyUlogBackupExpireDay):
        self._IsReadOnlyUlogBackupExpireDay = IsReadOnlyUlogBackupExpireDay

    @property
    def RestProxyStatus(self):
        return self._RestProxyStatus

    @RestProxyStatus.setter
    def RestProxyStatus(self, RestProxyStatus):
        self._RestProxyStatus = RestProxyStatus


    def _deserialize(self, params):
        self._ClusterName = params.get("ClusterName")
        self._ClusterId = params.get("ClusterId")
        self._Region = params.get("Region")
        self._IdlType = params.get("IdlType")
        self._NetworkType = params.get("NetworkType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CreatedTime = params.get("CreatedTime")
        self._Password = params.get("Password")
        self._PasswordStatus = params.get("PasswordStatus")
        self._ApiAccessId = params.get("ApiAccessId")
        self._ApiAccessIp = params.get("ApiAccessIp")
        self._ApiAccessPort = params.get("ApiAccessPort")
        self._OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self._ApiAccessIpv6 = params.get("ApiAccessIpv6")
        self._ClusterType = params.get("ClusterType")
        self._ClusterStatus = params.get("ClusterStatus")
        self._ReadCapacityUnit = params.get("ReadCapacityUnit")
        self._WriteCapacityUnit = params.get("WriteCapacityUnit")
        self._DiskVolume = params.get("DiskVolume")
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = ServerDetailInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyDetailInfo()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        self._Censorship = params.get("Censorship")
        self._DbaUins = params.get("DbaUins")
        self._DataFlowStatus = params.get("DataFlowStatus")
        if params.get("KafkaInfo") is not None:
            self._KafkaInfo = KafkaInfo()
            self._KafkaInfo._deserialize(params.get("KafkaInfo"))
        self._TxhBackupExpireDay = params.get("TxhBackupExpireDay")
        self._UlogBackupExpireDay = params.get("UlogBackupExpireDay")
        self._IsReadOnlyUlogBackupExpireDay = params.get("IsReadOnlyUlogBackupExpireDay")
        self._RestProxyStatus = params.get("RestProxyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareIdlFilesRequest(AbstractModel):
    """CompareIdlFiles request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table to be modified resides
        :type ClusterId: str
        :param _SelectedTables: List of tables to be modified
        :type SelectedTables: list of SelectedTableInfoNew
        :param _ExistingIdlFiles: Selected list of uploaded IDL files. Either this parameter or `NewIdlFiles` must be selected
        :type ExistingIdlFiles: list of IdlFileInfo
        :param _NewIdlFiles: List of IDL files to be uploaded. Either this parameter or `ExistingIdlFiles` must be selected
        :type NewIdlFiles: list of IdlFileInfo
        """
        self._ClusterId = None
        self._SelectedTables = None
        self._ExistingIdlFiles = None
        self._NewIdlFiles = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def ExistingIdlFiles(self):
        return self._ExistingIdlFiles

    @ExistingIdlFiles.setter
    def ExistingIdlFiles(self, ExistingIdlFiles):
        self._ExistingIdlFiles = ExistingIdlFiles

    @property
    def NewIdlFiles(self):
        return self._NewIdlFiles

    @NewIdlFiles.setter
    def NewIdlFiles(self, NewIdlFiles):
        self._NewIdlFiles = NewIdlFiles


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        if params.get("ExistingIdlFiles") is not None:
            self._ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self._NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._NewIdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareIdlFilesResponse(AbstractModel):
    """CompareIdlFiles response structure.

    """

    def __init__(self):
        r"""
        :param _IdlFiles: Information list of all IDL files uploaded and verified in this request
        :type IdlFiles: list of IdlFileInfo
        :param _TotalCount: Number of tables verified to be valid in this request
        :type TotalCount: int
        :param _TableInfos: Verification result parsed from the selected table after the IDL description file is read
        :type TableInfos: list of ParsedTableInfoNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IdlFiles = None
        self._TotalCount = None
        self._TableInfos = None
        self._RequestId = None

    @property
    def IdlFiles(self):
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableInfos(self):
        return self._TableInfos

    @TableInfos.setter
    def TableInfos(self, TableInfos):
        self._TableInfos = TableInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self._TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self._TableInfos.append(obj)
        self._RequestId = params.get("RequestId")


class CompareTablesInfo(AbstractModel):
    """Compare the meta information of two tables

    """

    def __init__(self):
        r"""
        :param _SrcTableClusterId: Cluster ID of the source table
        :type SrcTableClusterId: str
        :param _SrcTableGroupId: Table group ID of the source table
        :type SrcTableGroupId: str
        :param _SrcTableName: Source table name
        :type SrcTableName: str
        :param _DstTableClusterId: Cluster ID of the target table
        :type DstTableClusterId: str
        :param _DstTableGroupId: Table group ID of the target table
        :type DstTableGroupId: str
        :param _DstTableName: Target table name
        :type DstTableName: str
        :param _SrcTableInstanceId: Source table ID
        :type SrcTableInstanceId: str
        :param _DstTableInstanceId: Target table ID
        :type DstTableInstanceId: str
        """
        self._SrcTableClusterId = None
        self._SrcTableGroupId = None
        self._SrcTableName = None
        self._DstTableClusterId = None
        self._DstTableGroupId = None
        self._DstTableName = None
        self._SrcTableInstanceId = None
        self._DstTableInstanceId = None

    @property
    def SrcTableClusterId(self):
        return self._SrcTableClusterId

    @SrcTableClusterId.setter
    def SrcTableClusterId(self, SrcTableClusterId):
        self._SrcTableClusterId = SrcTableClusterId

    @property
    def SrcTableGroupId(self):
        return self._SrcTableGroupId

    @SrcTableGroupId.setter
    def SrcTableGroupId(self, SrcTableGroupId):
        self._SrcTableGroupId = SrcTableGroupId

    @property
    def SrcTableName(self):
        return self._SrcTableName

    @SrcTableName.setter
    def SrcTableName(self, SrcTableName):
        self._SrcTableName = SrcTableName

    @property
    def DstTableClusterId(self):
        return self._DstTableClusterId

    @DstTableClusterId.setter
    def DstTableClusterId(self, DstTableClusterId):
        self._DstTableClusterId = DstTableClusterId

    @property
    def DstTableGroupId(self):
        return self._DstTableGroupId

    @DstTableGroupId.setter
    def DstTableGroupId(self, DstTableGroupId):
        self._DstTableGroupId = DstTableGroupId

    @property
    def DstTableName(self):
        return self._DstTableName

    @DstTableName.setter
    def DstTableName(self, DstTableName):
        self._DstTableName = DstTableName

    @property
    def SrcTableInstanceId(self):
        return self._SrcTableInstanceId

    @SrcTableInstanceId.setter
    def SrcTableInstanceId(self, SrcTableInstanceId):
        self._SrcTableInstanceId = SrcTableInstanceId

    @property
    def DstTableInstanceId(self):
        return self._DstTableInstanceId

    @DstTableInstanceId.setter
    def DstTableInstanceId(self, DstTableInstanceId):
        self._DstTableInstanceId = DstTableInstanceId


    def _deserialize(self, params):
        self._SrcTableClusterId = params.get("SrcTableClusterId")
        self._SrcTableGroupId = params.get("SrcTableGroupId")
        self._SrcTableName = params.get("SrcTableName")
        self._DstTableClusterId = params.get("DstTableClusterId")
        self._DstTableGroupId = params.get("DstTableGroupId")
        self._DstTableName = params.get("DstTableName")
        self._SrcTableInstanceId = params.get("SrcTableInstanceId")
        self._DstTableInstanceId = params.get("DstTableInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table to be backed up resides
        :type ClusterId: str
        :param _SelectedTables: Information list of tables to be backed up
        :type SelectedTables: list of SelectedTableInfoNew
        :param _Remark: Remarks
        :type Remark: str
        """
        self._ClusterId = None
        self._SelectedTables = None
        self._Remark = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup response structure.

    """

    def __init__(self):
        r"""
        :param _TaskIds: List of backup creation task IDs
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskIds: list of str
        :param _ApplicationIds: List of backup creation application IDs
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplicationIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskIds = None
        self._ApplicationIds = None
        self._RequestId = None

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def ApplicationIds(self):
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        self._ApplicationIds = params.get("ApplicationIds")
        self._RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster request structure.

    """

    def __init__(self):
        r"""
        :param _IdlType: Cluster data description language type, such as `PROTO`, `TDR`, or `MIX`
        :type IdlType: str
        :param _ClusterName: Cluster name, which can contain up to 32 letters and digits
        :type ClusterName: str
        :param _VpcId: ID of the VPC instance bound to a cluster in the format of `vpc-f49l6u0z`
        :type VpcId: str
        :param _SubnetId: ID of the subnet instance bound to a cluster in the format of `subnet-pxir56ns`
        :type SubnetId: str
        :param _Password: Cluster access password, which must contain lowercase letters (a-z), uppercase letters (A-Z), and digits (0-9).
        :type Password: str
        :param _ResourceTags: Cluster tag list
        :type ResourceTags: list of TagInfoUnit
        :param _Ipv6Enable: Whether to enable IPv6 address access for clusters
        :type Ipv6Enable: int
        :param _ServerList: Information of the machine at the storage layer (tcapsvr) in a dedicated cluster
        :type ServerList: list of MachineInfo
        :param _ProxyList: Information of the machine at the access layer (tcaproxy) in a dedicated cluster
        :type ProxyList: list of MachineInfo
        :param _ClusterType: Cluster type. Valid values: `1` (standard), `2` (dedicated)
        :type ClusterType: int
        :param _AuthType: Authentication type. Valid values: `0` (static password), `1` (signature)
        :type AuthType: int
        """
        self._IdlType = None
        self._ClusterName = None
        self._VpcId = None
        self._SubnetId = None
        self._Password = None
        self._ResourceTags = None
        self._Ipv6Enable = None
        self._ServerList = None
        self._ProxyList = None
        self._ClusterType = None
        self._AuthType = None

    @property
    def IdlType(self):
        return self._IdlType

    @IdlType.setter
    def IdlType(self, IdlType):
        self._IdlType = IdlType

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

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
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Ipv6Enable(self):
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable

    @property
    def ServerList(self):
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def ProxyList(self):
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType


    def _deserialize(self, params):
        self._IdlType = params.get("IdlType")
        self._ClusterName = params.get("ClusterName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Password = params.get("Password")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Ipv6Enable = params.get("Ipv6Enable")
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        self._ClusterType = params.get("ClusterType")
        self._AuthType = params.get("AuthType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class CreateSnapshotsRequest(AbstractModel):
    """CreateSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where the table resides
        :type ClusterId: str
        :param _SelectedTables: Snapshot list
        :type SelectedTables: list of SnapshotInfo
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotsResponse(AbstractModel):
    """CreateSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of snapshots created in batches
        :type TotalCount: int
        :param _TableResults: The result list of snapshots created in batches
        :type TableResults: list of SnapshotResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class CreateTableGroupRequest(AbstractModel):
    """CreateTableGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where a table group resides
        :type ClusterId: str
        :param _TableGroupName: Table group name, which can contain up to 32 letters and digits
        :type TableGroupName: str
        :param _TableGroupId: Table group ID, which can be customized but must be unique in one cluster. If it is not specified, the auto-increment mode will be used.
        :type TableGroupId: str
        :param _ResourceTags: Table group tag list
        :type ResourceTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._TableGroupName = None
        self._TableGroupId = None
        self._ResourceTags = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupName(self):
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupName = params.get("TableGroupName")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTableGroupResponse(AbstractModel):
    """CreateTableGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TableGroupId: ID of table group successfully created
        :type TableGroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TableGroupId = None
        self._RequestId = None

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._RequestId = params.get("RequestId")


class CreateTablesRequest(AbstractModel):
    """CreateTables request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where to create a table
        :type ClusterId: str
        :param _IdlFiles: Table creation IDL file list selected by user
        :type IdlFiles: list of IdlFileInfo
        :param _SelectedTables: Information list of tables to be created
        :type SelectedTables: list of SelectedTableInfoNew
        :param _ResourceTags: Table tag list
        :type ResourceTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._IdlFiles = None
        self._SelectedTables = None
        self._ResourceTags = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IdlFiles(self):
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTablesResponse(AbstractModel):
    """CreateTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of tables created in batches
        :type TotalCount: int
        :param _TableResults: List of tables created in batches
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteBackupRecordsRequest(AbstractModel):
    """DeleteBackupRecords request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID of the backup records to be deleted
        :type ClusterId: str
        :param _BackupRecords: Details of the backup records to be deleted
        :type BackupRecords: list of BackupRecords
        """
        self._ClusterId = None
        self._BackupRecords = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupRecords(self):
        return self._BackupRecords

    @BackupRecords.setter
    def BackupRecords(self, BackupRecords):
        self._BackupRecords = BackupRecords


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("BackupRecords") is not None:
            self._BackupRecords = []
            for item in params.get("BackupRecords"):
                obj = BackupRecords()
                obj._deserialize(item)
                self._BackupRecords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupRecordsResponse(AbstractModel):
    """DeleteBackupRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, which is used to identify tasks of different clusters.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of cluster to be deleted
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID generated by cluster deletion
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteIdlFilesRequest(AbstractModel):
    """DeleteIdlFiles request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where IDL resides
        :type ClusterId: str
        :param _IdlFiles: List of information of IDL files to be deleted
        :type IdlFiles: list of IdlFileInfo
        """
        self._ClusterId = None
        self._IdlFiles = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IdlFiles(self):
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIdlFilesResponse(AbstractModel):
    """DeleteIdlFiles response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of returned results
        :type TotalCount: int
        :param _IdlFileInfos: Deletion result
        :type IdlFileInfos: list of IdlFileInfoWithoutContent
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._IdlFileInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IdlFileInfos(self):
        return self._IdlFileInfos

    @IdlFileInfos.setter
    def IdlFileInfos(self, IdlFileInfos):
        self._IdlFileInfos = IdlFileInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("IdlFileInfos") is not None:
            self._IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfoWithoutContent()
                obj._deserialize(item)
                self._IdlFileInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where the table resides
        :type ClusterId: str
        :param _SelectedTables: The list of snapshots to delete
        :type SelectedTables: list of SnapshotInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of snapshots deleted in batches
        :type TotalCount: int
        :param _TableResults: The result list of snapshots deleted in batches
        :type TableResults: list of SnapshotResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteTableDataFlowRequest(AbstractModel):
    """DeleteTableDataFlow request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where the tables reside
        :type ClusterId: str
        :param _SelectedTables: The list of tables for which data subscription will be disabled
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableDataFlowResponse(AbstractModel):
    """DeleteTableDataFlow response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of tables for which data subscription has been disabled
        :type TotalCount: int
        :param _TableResults: The result list of tables for which data subscription has been disabled
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteTableGroupRequest(AbstractModel):
    """DeleteTableGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where a table group resides
        :type ClusterId: str
        :param _TableGroupId: Table group ID
        :type TableGroupId: str
        """
        self._ClusterId = None
        self._TableGroupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableGroupResponse(AbstractModel):
    """DeleteTableGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID generated by table group deletion
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteTableIndexRequest(AbstractModel):
    """DeleteTableIndex request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table resides
        :type ClusterId: str
        :param _SelectedTables: The list of tables whose global indexes need to be deleted
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableIndexResponse(AbstractModel):
    """DeleteTableIndex response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of tables whose global indexes are deleted
        :type TotalCount: int
        :param _TableResults: The list of global index deletion results
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteTablesRequest(AbstractModel):
    """DeleteTables request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table to be dropped resides
        :type ClusterId: str
        :param _SelectedTables: List of information of tables to be dropped
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTablesResponse(AbstractModel):
    """DeleteTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of dropped tables
        :type TotalCount: int
        :param _TableResults: List of details of dropped tables
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupRecordsRequest(AbstractModel):
    """DescribeBackupRecords request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID, which is used to query a specified cluster
        :type ClusterId: str
        :param _Limit: Number of results per page
        :type Limit: int
        :param _Offset: Page offset
        :type Offset: int
        :param _TableGroupId: Table group ID used as a filter condition
        :type TableGroupId: str
        :param _TableName: Table name used as a filter condition
        :type TableName: str
        """
        self._ClusterId = None
        self._Limit = None
        self._Offset = None
        self._TableGroupId = None
        self._TableName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupRecordsResponse(AbstractModel):
    """DescribeBackupRecords response structure.

    """

    def __init__(self):
        r"""
        :param _BackupRecords: Backup record details
        :type BackupRecords: list of BackupRecords
        :param _TotalCount: Number of returned entries
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupRecords = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BackupRecords(self):
        return self._BackupRecords

    @BackupRecords.setter
    def BackupRecords(self, BackupRecords):
        self._BackupRecords = BackupRecords

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackupRecords") is not None:
            self._BackupRecords = []
            for item in params.get("BackupRecords"):
                obj = BackupRecords()
                obj._deserialize(item)
                self._BackupRecords.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClusterTagsRequest(AbstractModel):
    """DescribeClusterTags request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: The list of cluster IDs
        :type ClusterIds: list of str
        """
        self._ClusterIds = None

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterTagsResponse(AbstractModel):
    """DescribeClusterTags response structure.

    """

    def __init__(self):
        r"""
        :param _Rows: The information list of cluster tags
        :type Rows: list of TagsInfoOfCluster
        :param _TotalCount: The number of returned results
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Rows = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfCluster()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: List of IDs of clusters to be queried
        :type ClusterIds: list of str
        :param _Filters: Query filter
        :type Filters: list of Filter
        :param _Offset: Query list offset
        :type Offset: int
        :param _Limit: Number of returned results in query list. Default value: 20
        :type Limit: int
        :param _Ipv6Enable: Whether to enable IPv6 address access
        :type Ipv6Enable: int
        """
        self._ClusterIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Ipv6Enable = None

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def Ipv6Enable(self):
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of cluster instances
        :type TotalCount: int
        :param _Clusters: Cluster instance list
        :type Clusters: list of ClusterInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Clusters = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Clusters(self):
        return self._Clusters

    @Clusters.setter
    def Clusters(self, Clusters):
        self._Clusters = Clusters

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Clusters") is not None:
            self._Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self._Clusters.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIdlFileInfosRequest(AbstractModel):
    """DescribeIdlFileInfos request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where a file resides
        :type ClusterId: str
        :param _TableGroupIds: ID of the table group where a file resides
        :type TableGroupIds: list of str
        :param _IdlFileIds: File ID list
        :type IdlFileIds: list of str
        :param _Offset: Query list offset
        :type Offset: int
        :param _Limit: Number of returned results in query list
        :type Limit: int
        """
        self._ClusterId = None
        self._TableGroupIds = None
        self._IdlFileIds = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds

    @property
    def IdlFileIds(self):
        return self._IdlFileIds

    @IdlFileIds.setter
    def IdlFileIds(self, IdlFileIds):
        self._IdlFileIds = IdlFileIds

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


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
        self._IdlFileIds = params.get("IdlFileIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdlFileInfosResponse(AbstractModel):
    """DescribeIdlFileInfos response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of files
        :type TotalCount: int
        :param _IdlFileInfos: List of file details
        :type IdlFileInfos: list of IdlFileInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._IdlFileInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IdlFileInfos(self):
        return self._IdlFileInfos

    @IdlFileInfos.setter
    def IdlFileInfos(self, IdlFileInfos):
        self._IdlFileInfos = IdlFileInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("IdlFileInfos") is not None:
            self._IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFileInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineRequest(AbstractModel):
    """DescribeMachine request structure.

    """

    def __init__(self):
        r"""
        :param _Ipv6Enable: If this parameter is not `0`, machines supporting IPv6 will be queried.
        :type Ipv6Enable: int
        """
        self._Ipv6Enable = None

    @property
    def Ipv6Enable(self):
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable


    def _deserialize(self, params):
        self._Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineResponse(AbstractModel):
    """DescribeMachine response structure.

    """

    def __init__(self):
        r"""
        :param _PoolList: The list of dedicated machine resources
        :type PoolList: list of PoolInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PoolList = None
        self._RequestId = None

    @property
    def PoolList(self):
        return self._PoolList

    @PoolList.setter
    def PoolList(self, PoolList):
        self._PoolList = PoolList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PoolList") is not None:
            self._PoolList = []
            for item in params.get("PoolList"):
                obj = PoolInfo()
                obj._deserialize(item)
                self._PoolList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of queried AZs
        :type TotalCount: int
        :param _RegionInfos: List of AZ query results
        :type RegionInfos: list of RegionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionInfos(self):
        return self._RegionInfos

    @RegionInfos.setter
    def RegionInfos(self, RegionInfos):
        self._RegionInfos = RegionInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionInfos") is not None:
            self._RegionInfos = []
            for item in params.get("RegionInfos"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where the table resides
        :type ClusterId: str
        :param _TableGroupId: The ID of the table group where the table resides
        :type TableGroupId: str
        :param _TableName: Table name
        :type TableName: str
        :param _SnapshotName: Snapshot name
        :type SnapshotName: str
        :param _SelectedTables: The list of snapshots pulled in batches
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._TableName = None
        self._SnapshotName = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._SnapshotName = params.get("SnapshotName")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of snapshots
        :type TotalCount: int
        :param _TableResults: The result list of snapshots
        :type TableResults: list of SnapshotResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTableGroupTagsRequest(AbstractModel):
    """DescribeTableGroupTags request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where table group tags need to be queried
        :type ClusterId: str
        :param _TableGroupIds: The list of IDs of the table groups whose tags need to be queried
        :type TableGroupIds: list of str
        """
        self._ClusterId = None
        self._TableGroupIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableGroupTagsResponse(AbstractModel):
    """DescribeTableGroupTags response structure.

    """

    def __init__(self):
        r"""
        :param _Rows: The information list of table group tags
        :type Rows: list of TagsInfoOfTableGroup
        :param _TotalCount: The number of returned results
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Rows = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfTableGroup()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTableGroupsRequest(AbstractModel):
    """DescribeTableGroups request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where a table group resides
        :type ClusterId: str
        :param _TableGroupIds: Table group ID list
        :type TableGroupIds: list of str
        :param _Filters: Filter. Valid values: TableGroupName, TableGroupId
        :type Filters: list of Filter
        :param _Offset: Query list offset
        :type Offset: int
        :param _Limit: Number of returned results in query list
        :type Limit: int
        """
        self._ClusterId = None
        self._TableGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableGroupsResponse(AbstractModel):
    """DescribeTableGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of table groups
        :type TotalCount: int
        :param _TableGroups: Table group information list
        :type TableGroups: list of TableGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableGroups(self):
        return self._TableGroups

    @TableGroups.setter
    def TableGroups(self, TableGroups):
        self._TableGroups = TableGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableGroups") is not None:
            self._TableGroups = []
            for item in params.get("TableGroups"):
                obj = TableGroupInfo()
                obj._deserialize(item)
                self._TableGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTableTagsRequest(AbstractModel):
    """DescribeTableTags request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where a table resides
        :type ClusterId: str
        :param _SelectedTables: Table list
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableTagsResponse(AbstractModel):
    """DescribeTableTags response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of returned results
        :type TotalCount: int
        :param _Rows: The information list of table tags
        :type Rows: list of TagsInfoOfTable
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfTable()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesInRecycleRequest(AbstractModel):
    """DescribeTablesInRecycle request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table to be queried resides
        :type ClusterId: str
        :param _TableGroupIds: List of IDs of the table groups where the table to be queried resides
        :type TableGroupIds: list of str
        :param _Filters: Filter. Valid values: TableName, TableInstanceId
        :type Filters: list of Filter
        :param _Offset: Query result offset
        :type Offset: int
        :param _Limit: Number of returned query results
        :type Limit: int
        """
        self._ClusterId = None
        self._TableGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesInRecycleResponse(AbstractModel):
    """DescribeTablesInRecycle response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of tables
        :type TotalCount: int
        :param _TableInfos: Table details result list
        :type TableInfos: list of TableInfoNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableInfos(self):
        return self._TableInfos

    @TableInfos.setter
    def TableInfos(self, TableInfos):
        self._TableInfos = TableInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self._TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self._TableInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table to be queried resides
        :type ClusterId: str
        :param _TableGroupIds: List of IDs of the table groups where the table to be queried resides
        :type TableGroupIds: list of str
        :param _SelectedTables: Information list of tables to be queriedu200d. If you need to filter the tables, use the`Filter` parameter.
        :type SelectedTables: list of SelectedTableInfoNew
        :param _Filters: Filter. Valid values: TableName, TableInstanceId
        :type Filters: list of Filter
        :param _Offset: Query result offset
        :type Offset: int
        :param _Limit: Number of returned query results
        :type Limit: int
        """
        self._ClusterId = None
        self._TableGroupIds = None
        self._SelectedTables = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupIds(self):
        return self._TableGroupIds

    @TableGroupIds.setter
    def TableGroupIds(self, TableGroupIds):
        self._TableGroupIds = TableGroupIds

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupIds = params.get("TableGroupIds")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of tables
        :type TotalCount: int
        :param _TableInfos: Table details result list
        :type TableInfos: list of TableInfoNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableInfos(self):
        return self._TableInfos

    @TableInfos.setter
    def TableInfos(self, TableInfos):
        self._TableInfos = TableInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self._TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self._TableInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: List of IDs of clusters where the tasks to be queried reside
        :type ClusterIds: list of str
        :param _TaskIds: List of IDs of tasks to be queried
        :type TaskIds: list of str
        :param _Filters: Filter. Valid values: Content, TaskType, Operator, Time
        :type Filters: list of Filter
        :param _Offset: Query list offset
        :type Offset: int
        :param _Limit: Number of returned results in query list
        :type Limit: int
        """
        self._ClusterIds = None
        self._TaskIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._TaskIds = params.get("TaskIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of tasks
        :type TotalCount: int
        :param _TaskInfos: List of details of queried tasks
        :type TaskInfos: list of TaskInfoNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskInfos(self):
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = TaskInfoNew()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUinInWhitelistRequest(AbstractModel):
    """DescribeUinInWhitelist request structure.

    """


class DescribeUinInWhitelistResponse(AbstractModel):
    """DescribeUinInWhitelist response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Query result. FALSE: yes, TRUE: no
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DisableRestProxyRequest(AbstractModel):
    """DisableRestProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The value is the same as `appid`.
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRestProxyResponse(AbstractModel):
    """DisableRestProxy response structure.

    """

    def __init__(self):
        r"""
        :param _RestProxyStatus: RestProxy status. Valid values: 0 (disabled), 1 (enabling), 2 (enabled), 3 (disabling).
        :type RestProxyStatus: int
        :param _TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, used to identify tasks of different clusters.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RestProxyStatus = None
        self._TaskId = None
        self._RequestId = None

    @property
    def RestProxyStatus(self):
        return self._RestProxyStatus

    @RestProxyStatus.setter
    def RestProxyStatus(self, RestProxyStatus):
        self._RestProxyStatus = RestProxyStatus

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RestProxyStatus = params.get("RestProxyStatus")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class EnableRestProxyRequest(AbstractModel):
    """EnableRestProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The value is the same as `appid`.
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRestProxyResponse(AbstractModel):
    """EnableRestProxy response structure.

    """

    def __init__(self):
        r"""
        :param _RestProxyStatus: RestProxy status. Valid values: 0 (disabled), 1 (enabling), 2 (enabled), 3 (disabling).
        :type RestProxyStatus: int
        :param _TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, used to identify tasks of different clusters.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RestProxyStatus = None
        self._TaskId = None
        self._RequestId = None

    @property
    def RestProxyStatus(self):
        return self._RestProxyStatus

    @RestProxyStatus.setter
    def RestProxyStatus(self, RestProxyStatus):
        self._RestProxyStatus = RestProxyStatus

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RestProxyStatus = params.get("RestProxyStatus")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ErrorInfo(AbstractModel):
    """Describes the details of errors that may occur during the processing of each instance (application, region, or table).

    """

    def __init__(self):
        r"""
        :param _Code: Error code
        :type Code: str
        :param _Message: Error message
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FieldInfo(AbstractModel):
    """The list of table field information

    """

    def __init__(self):
        r"""
        :param _FieldName: Table field name
        :type FieldName: str
        :param _IsPrimaryKey: Whether it is a primary key field
        :type IsPrimaryKey: str
        :param _FieldType: Field type
        :type FieldType: str
        :param _FieldSize: Field length
        :type FieldSize: int
        """
        self._FieldName = None
        self._IsPrimaryKey = None
        self._FieldType = None
        self._FieldSize = None

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def IsPrimaryKey(self):
        return self._IsPrimaryKey

    @IsPrimaryKey.setter
    def IsPrimaryKey(self, IsPrimaryKey):
        self._IsPrimaryKey = IsPrimaryKey

    @property
    def FieldType(self):
        return self._FieldType

    @FieldType.setter
    def FieldType(self, FieldType):
        self._FieldType = FieldType

    @property
    def FieldSize(self):
        return self._FieldSize

    @FieldSize.setter
    def FieldSize(self, FieldSize):
        self._FieldSize = FieldSize


    def _deserialize(self, params):
        self._FieldName = params.get("FieldName")
        self._IsPrimaryKey = params.get("IsPrimaryKey")
        self._FieldType = params.get("FieldType")
        self._FieldSize = params.get("FieldSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        r"""
        :param _Name: Filter field name
        :type Name: str
        :param _Value: Filter field value
        :type Value: str
        :param _Values: Filter field value
        :type Values: list of str
        """
        self._Name = None
        self._Value = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdlFileInfo(AbstractModel):
    """Table definition file details, including file content

    """

    def __init__(self):
        r"""
        :param _FileName: Filename excluding extension
        :type FileName: str
        :param _FileType: Data interface description language (IDL) type
        :type FileType: str
        :param _FileExtType: File extension
        :type FileExtType: str
        :param _FileSize: File size in bytes
        :type FileSize: int
        :param _FileId: File ID, which is meaningful for files already uploaded
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileId: int
        :param _FileContent: File content, which is meaningful for files to be uploaded in this request
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileContent: str
        """
        self._FileName = None
        self._FileType = None
        self._FileExtType = None
        self._FileSize = None
        self._FileId = None
        self._FileContent = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileExtType(self):
        return self._FileExtType

    @FileExtType.setter
    def FileExtType(self, FileExtType):
        self._FileExtType = FileExtType

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._FileExtType = params.get("FileExtType")
        self._FileSize = params.get("FileSize")
        self._FileId = params.get("FileId")
        self._FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdlFileInfoWithoutContent(AbstractModel):
    """Table definition file details, excluding file content

    """

    def __init__(self):
        r"""
        :param _FileName: Filename excluding extension
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileName: str
        :param _FileType: Data interface description language (IDL) type
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileType: str
        :param _FileExtType: File extension
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileExtType: str
        :param _FileSize: File size in bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileSize: int
        :param _FileId: File ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileId: int
        :param _Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._FileName = None
        self._FileType = None
        self._FileExtType = None
        self._FileSize = None
        self._FileId = None
        self._Error = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileExtType(self):
        return self._FileExtType

    @FileExtType.setter
    def FileExtType(self, FileExtType):
        self._FileExtType = FileExtType

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._FileExtType = params.get("FileExtType")
        self._FileSize = params.get("FileSize")
        self._FileId = params.get("FileId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSnapshotsRequest(AbstractModel):
    """ImportSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where the original table (from which the snapshot was created) resides
        :type ClusterId: str
        :param _Snapshots: The information of the snapshot to import
        :type Snapshots: :class:`tencentcloud.tcaplusdb.v20190823.models.SnapshotInfo`
        :param _ImportSpecialKey: Whether to import partial data of the snapshot. Valid values: `TRUE` (import partial data), `FALSE` (import all data).
        :type ImportSpecialKey: str
        :param _ImportOriginTable: Whether to import to the original table. Valid values: `TRUE` (import to the original table), `FALSE` (import to a new table).
        :type ImportOriginTable: str
        :param _KeyFile: The file of the keys of the partial data
        :type KeyFile: :class:`tencentcloud.tcaplusdb.v20190823.models.KeyFile`
        :param _NewTableGroupId: The ID of the table group where the new table resides, which is valid only when `ImportOriginTable` is set to `FALSE`
        :type NewTableGroupId: str
        :param _NewTableName: The name of the new table, which is valid only when `ImportOriginTable` is set to `FALSE`. TcaplusDB will automatically create a table named `NewTableName` of the same structure as that of the original table.
        :type NewTableName: str
        """
        self._ClusterId = None
        self._Snapshots = None
        self._ImportSpecialKey = None
        self._ImportOriginTable = None
        self._KeyFile = None
        self._NewTableGroupId = None
        self._NewTableName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Snapshots(self):
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots

    @property
    def ImportSpecialKey(self):
        return self._ImportSpecialKey

    @ImportSpecialKey.setter
    def ImportSpecialKey(self, ImportSpecialKey):
        self._ImportSpecialKey = ImportSpecialKey

    @property
    def ImportOriginTable(self):
        return self._ImportOriginTable

    @ImportOriginTable.setter
    def ImportOriginTable(self, ImportOriginTable):
        self._ImportOriginTable = ImportOriginTable

    @property
    def KeyFile(self):
        return self._KeyFile

    @KeyFile.setter
    def KeyFile(self, KeyFile):
        self._KeyFile = KeyFile

    @property
    def NewTableGroupId(self):
        return self._NewTableGroupId

    @NewTableGroupId.setter
    def NewTableGroupId(self, NewTableGroupId):
        self._NewTableGroupId = NewTableGroupId

    @property
    def NewTableName(self):
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Snapshots") is not None:
            self._Snapshots = SnapshotInfo()
            self._Snapshots._deserialize(params.get("Snapshots"))
        self._ImportSpecialKey = params.get("ImportSpecialKey")
        self._ImportOriginTable = params.get("ImportOriginTable")
        if params.get("KeyFile") is not None:
            self._KeyFile = KeyFile()
            self._KeyFile._deserialize(params.get("KeyFile"))
        self._NewTableGroupId = params.get("NewTableGroupId")
        self._NewTableName = params.get("NewTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSnapshotsResponse(AbstractModel):
    """ImportSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, used to identify tasks of different clusters.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _ApplicationId: `ApplicationId` is in the format of `AppInstanceId-applicationId`, which is used to identify applications of different clusters.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._ApplicationId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ApplicationId = params.get("ApplicationId")
        self._RequestId = params.get("RequestId")


class KafkaInfo(AbstractModel):
    """CKafka address

    """

    def __init__(self):
        r"""
        :param _Address: CKafka address
        :type Address: str
        :param _Topic: CKafka topic
        :type Topic: str
        :param _User: CKafka username
        :type User: str
        :param _Password: CKafka password
        :type Password: str
        :param _Instance: CKafka instance
        :type Instance: str
        :param _IsVpc: Whether VPC access is enabled
        :type IsVpc: int
        """
        self._Address = None
        self._Topic = None
        self._User = None
        self._Password = None
        self._Instance = None
        self._IsVpc = None

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

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
    def Instance(self):
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def IsVpc(self):
        return self._IsVpc

    @IsVpc.setter
    def IsVpc(self, IsVpc):
        self._IsVpc = IsVpc


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Topic = params.get("Topic")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Instance = params.get("Instance")
        self._IsVpc = params.get("IsVpc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyFile(AbstractModel):
    """The file of keys used to import partial snapshot data

    """

    def __init__(self):
        r"""
        :param _FileName: Key file name
        :type FileName: str
        :param _FileExtType: Key file extension
        :type FileExtType: str
        :param _FileContent: Key file content
        :type FileContent: str
        :param _FileSize: Key file size
        :type FileSize: int
        """
        self._FileName = None
        self._FileExtType = None
        self._FileContent = None
        self._FileSize = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileExtType(self):
        return self._FileExtType

    @FileExtType.setter
    def FileExtType(self, FileExtType):
        self._FileExtType = FileExtType

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileExtType = params.get("FileExtType")
        self._FileContent = params.get("FileContent")
        self._FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineInfo(AbstractModel):
    """Machine type and quantity

    """

    def __init__(self):
        r"""
        :param _MachineType: Machine type
        :type MachineType: str
        :param _MachineNum: Machine quantity
        :type MachineNum: int
        """
        self._MachineType = None
        self._MachineNum = None

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineNum(self):
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTableResult(AbstractModel):
    """Table merging results

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _Error: If table merging is successful, `null` will be returned
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _Table: Comparison results of tables
        :type Table: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`
        :param _ApplicationId: Application ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplicationId: str
        """
        self._TaskId = None
        self._Error = None
        self._Table = None
        self._ApplicationId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        if params.get("Table") is not None:
            self._Table = CompareTablesInfo()
            self._Table._deserialize(params.get("Table"))
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTablesDataRequest(AbstractModel):
    """MergeTablesData request structure.

    """

    def __init__(self):
        r"""
        :param _SelectedTables: Tables to be merged
        :type SelectedTables: list of MergeTablesInfo
        :param _IsOnlyCompare: Valid values: `true` (only compare), `false` (compare and merge)
        :type IsOnlyCompare: bool
        """
        self._SelectedTables = None
        self._IsOnlyCompare = None

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def IsOnlyCompare(self):
        return self._IsOnlyCompare

    @IsOnlyCompare.setter
    def IsOnlyCompare(self, IsOnlyCompare):
        self._IsOnlyCompare = IsOnlyCompare


    def _deserialize(self, params):
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = MergeTablesInfo()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        self._IsOnlyCompare = params.get("IsOnlyCompare")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeTablesDataResponse(AbstractModel):
    """MergeTablesData response structure.

    """

    def __init__(self):
        r"""
        :param _Results: Table merging results
        :type Results: list of MergeTableResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = MergeTableResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class MergeTablesInfo(AbstractModel):
    """Request parameters used to merge tables

    """

    def __init__(self):
        r"""
        :param _MergeTables: Information of tables to be merged
        :type MergeTables: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareTablesInfo`
        :param _CheckIndex: Whether to check indexes
        :type CheckIndex: bool
        """
        self._MergeTables = None
        self._CheckIndex = None

    @property
    def MergeTables(self):
        return self._MergeTables

    @MergeTables.setter
    def MergeTables(self, MergeTables):
        self._MergeTables = MergeTables

    @property
    def CheckIndex(self):
        return self._CheckIndex

    @CheckIndex.setter
    def CheckIndex(self, CheckIndex):
        self._CheckIndex = CheckIndex


    def _deserialize(self, params):
        if params.get("MergeTables") is not None:
            self._MergeTables = CompareTablesInfo()
            self._MergeTables._deserialize(params.get("MergeTables"))
        self._CheckIndex = params.get("CheckIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCensorshipRequest(AbstractModel):
    """ModifyCensorship request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Censorship: Whether to enable the operation approval feature for this cluster. Valid values: `0` (disable), `1` (enable)
        :type Censorship: int
        :param _Uins: Approver UIN list
        :type Uins: list of str
        """
        self._ClusterId = None
        self._Censorship = None
        self._Uins = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Censorship(self):
        return self._Censorship

    @Censorship.setter
    def Censorship(self, Censorship):
        self._Censorship = Censorship

    @property
    def Uins(self):
        return self._Uins

    @Uins.setter
    def Uins(self, Uins):
        self._Uins = Uins


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Censorship = params.get("Censorship")
        self._Uins = params.get("Uins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCensorshipResponse(AbstractModel):
    """ModifyCensorship response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Uins: Approver UIN list
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Uins: list of str
        :param _Censorship: Whether the operation approval feature is enabled for this cluster. Valid values: `0` (disabled), `1` (enabled)
        :type Censorship: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterId = None
        self._Uins = None
        self._Censorship = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Uins(self):
        return self._Uins

    @Uins.setter
    def Uins(self, Uins):
        self._Uins = Uins

    @property
    def Censorship(self):
        return self._Censorship

    @Censorship.setter
    def Censorship(self, Censorship):
        self._Censorship = Censorship

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Uins = params.get("Uins")
        self._Censorship = params.get("Censorship")
        self._RequestId = params.get("RequestId")


class ModifyClusterMachineRequest(AbstractModel):
    """ModifyClusterMachine request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ServerList: Information of the machines at the storage layer (tcapsvr)
        :type ServerList: list of MachineInfo
        :param _ProxyList: Information of the machines at the access layer (tcaproxy)
        :type ProxyList: list of MachineInfo
        :param _ClusterType: Cluster type. Valid values: `1` (standard), `2` (dedicated)
        :type ClusterType: int
        """
        self._ClusterId = None
        self._ServerList = None
        self._ProxyList = None
        self._ClusterType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ServerList(self):
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def ProxyList(self):
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        self._ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterMachineResponse(AbstractModel):
    """ModifyClusterMachine response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster to be renamed
        :type ClusterId: str
        :param _ClusterName: Cluster name to be changed to, which can contain up to 32 letters and digits
        :type ClusterName: str
        """
        self._ClusterId = None
        self._ClusterName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName response structure.

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


class ModifyClusterPasswordRequest(AbstractModel):
    """ModifyClusterPassword request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster for which to modify the password
        :type ClusterId: str
        :param _OldPassword: Old cluster password
        :type OldPassword: str
        :param _OldPasswordExpireTime: Expected expiration time of old cluster password
        :type OldPasswordExpireTime: str
        :param _NewPassword: New cluster password, which must contain lowercase letters (a-z), uppercase letters (A-Z), and digits (0-9).
        :type NewPassword: str
        :param _Mode: Update mode. 1: updates password, 2: updates old password expiration time. Default value: 1
        :type Mode: str
        """
        self._ClusterId = None
        self._OldPassword = None
        self._OldPasswordExpireTime = None
        self._NewPassword = None
        self._Mode = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def OldPassword(self):
        return self._OldPassword

    @OldPassword.setter
    def OldPassword(self, OldPassword):
        self._OldPassword = OldPassword

    @property
    def OldPasswordExpireTime(self):
        return self._OldPasswordExpireTime

    @OldPasswordExpireTime.setter
    def OldPasswordExpireTime(self, OldPasswordExpireTime):
        self._OldPasswordExpireTime = OldPasswordExpireTime

    @property
    def NewPassword(self):
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._OldPassword = params.get("OldPassword")
        self._OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self._NewPassword = params.get("NewPassword")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterPasswordResponse(AbstractModel):
    """ModifyClusterPassword response structure.

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


class ModifyClusterTagsRequest(AbstractModel):
    """ModifyClusterTags request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster whose tags need to be modified
        :type ClusterId: str
        :param _ReplaceTags: The list of tags to add or modify
        :type ReplaceTags: list of TagInfoUnit
        :param _DeleteTags: Tags to delete
        :type DeleteTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ReplaceTags(self):
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterTagsResponse(AbstractModel):
    """ModifyClusterTags response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifySnapshotsRequest(AbstractModel):
    """ModifySnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where the table resides
        :type ClusterId: str
        :param _SelectedTables: Snapshot list
        :type SelectedTables: list of SnapshotInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SnapshotInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotsResponse(AbstractModel):
    """ModifySnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of snapshots modified in batches
        :type TotalCount: int
        :param _TableResults: The result list of snapshots modified in batches
        :type TableResults: list of SnapshotResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = SnapshotResult()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyTableGroupNameRequest(AbstractModel):
    """ModifyTableGroupName request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where a table group resides
        :type ClusterId: str
        :param _TableGroupId: ID of the table group to be renamed
        :type TableGroupId: str
        :param _TableGroupName: New table group name, which can contain letters and symbols
        :type TableGroupName: str
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._TableGroupName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableGroupName(self):
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        self._TableGroupName = params.get("TableGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableGroupNameResponse(AbstractModel):
    """ModifyTableGroupName response structure.

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


class ModifyTableGroupTagsRequest(AbstractModel):
    """ModifyTableGroupTags request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where table group tags need to be modified
        :type ClusterId: str
        :param _TableGroupId: The ID of the table group whose tags need to be modified
        :type TableGroupId: str
        :param _ReplaceTags: The list of tags to add or modify
        :type ReplaceTags: list of TagInfoUnit
        :param _DeleteTags: Tags to delete
        :type DeleteTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def ReplaceTags(self):
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableGroupTagsResponse(AbstractModel):
    """ModifyTableGroupTags response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyTableMemosRequest(AbstractModel):
    """ModifyTableMemos request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster instance where a table resides
        :type ClusterId: str
        :param _TableMemos: List of details of selected tables
        :type TableMemos: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._TableMemos = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableMemos(self):
        return self._TableMemos

    @TableMemos.setter
    def TableMemos(self, TableMemos):
        self._TableMemos = TableMemos


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("TableMemos") is not None:
            self._TableMemos = []
            for item in params.get("TableMemos"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._TableMemos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableMemosResponse(AbstractModel):
    """ModifyTableMemos response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of tables modified for remarks
        :type TotalCount: int
        :param _TableResults: List of table remarks modification results
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyTableQuotasRequest(AbstractModel):
    """ModifyTableQuotas request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table to be scaled resides
        :type ClusterId: str
        :param _TableQuotas: List of quotas of tables selected for modification
        :type TableQuotas: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._TableQuotas = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableQuotas(self):
        return self._TableQuotas

    @TableQuotas.setter
    def TableQuotas(self, TableQuotas):
        self._TableQuotas = TableQuotas


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("TableQuotas") is not None:
            self._TableQuotas = []
            for item in params.get("TableQuotas"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._TableQuotas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableQuotasResponse(AbstractModel):
    """ModifyTableQuotas response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of scaled tables
        :type TotalCount: int
        :param _TableResults: List of table scaling results
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyTableTagsRequest(AbstractModel):
    """ModifyTableTags request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where table tags need to be modified
        :type ClusterId: str
        :param _SelectedTables: The list of tables whose tags need to be modified
        :type SelectedTables: list of SelectedTableInfoNew
        :param _ReplaceTags: The list of tags to add or modify
        :type ReplaceTags: list of TagInfoUnit
        :param _DeleteTags: The list of tags to delete
        :type DeleteTags: list of TagInfoUnit
        """
        self._ClusterId = None
        self._SelectedTables = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def ReplaceTags(self):
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableTagsResponse(AbstractModel):
    """ModifyTableTags response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of returned results
        :type TotalCount: int
        :param _TableResults: Returned results
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyTablesRequest(AbstractModel):
    """ModifyTables request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table to be modified resides
        :type ClusterId: str
        :param _IdlFiles: Selected table modification IDL files
        :type IdlFiles: list of IdlFileInfo
        :param _SelectedTables: List of tables to be modified
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._IdlFiles = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IdlFiles(self):
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTablesResponse(AbstractModel):
    """ModifyTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of modified tables
        :type TotalCount: int
        :param _TableResults: List of table modification results
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class ParsedTableInfoNew(AbstractModel):
    """Table information parsed from IDL table description file

    """

    def __init__(self):
        r"""
        :param _TableIdlType: Table description language type. Valid values: PROTO, TDR
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableIdlType: str
        :param _TableInstanceId: Table instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableInstanceId: str
        :param _TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _TableType: Table data structure type. Valid values: GENERIC, LIST
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableType: str
        :param _KeyFields: Primary key field information
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyFields: str
        :param _OldKeyFields: Old primary key field information, which is valid during verification of table modification
Note: this field may return null, indicating that no valid values can be obtained.
        :type OldKeyFields: str
        :param _ValueFields: Non-primary key field information
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValueFields: str
        :param _OldValueFields: Old non-primary key field information, which is valid during verification of table modification
Note: this field may return null, indicating that no valid values can be obtained.
        :type OldValueFields: str
        :param _TableGroupId: Table group ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param _SumKeyFieldSize: Total size of primary key field
Note: this field may return null, indicating that no valid values can be obtained.
        :type SumKeyFieldSize: int
        :param _SumValueFieldSize: Total size of non-primary key fields
Note: this field may return null, indicating that no valid values can be obtained.
        :type SumValueFieldSize: int
        :param _IndexKeySet: Index key set
Note: this field may return null, indicating that no valid values can be obtained.
        :type IndexKeySet: str
        :param _ShardingKeySet: Shardkey set
Note: this field may return null, indicating that no valid values can be obtained.
        :type ShardingKeySet: str
        :param _TdrVersion: TDR version number
Note: this field may return null, indicating that no valid values can be obtained.
        :type TdrVersion: int
        :param _Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _ListElementNum: Number of LIST-type table elements
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListElementNum: int
        :param _SortFieldNum: Number of SORTLIST-type table sort fields
Note: this field may return null, indicating that no valid values can be obtained.
        :type SortFieldNum: int
        :param _SortRule: Sort order of SORTLIST-type tables
Note: this field may return null, indicating that no valid values can be obtained.
        :type SortRule: int
        """
        self._TableIdlType = None
        self._TableInstanceId = None
        self._TableName = None
        self._TableType = None
        self._KeyFields = None
        self._OldKeyFields = None
        self._ValueFields = None
        self._OldValueFields = None
        self._TableGroupId = None
        self._SumKeyFieldSize = None
        self._SumValueFieldSize = None
        self._IndexKeySet = None
        self._ShardingKeySet = None
        self._TdrVersion = None
        self._Error = None
        self._ListElementNum = None
        self._SortFieldNum = None
        self._SortRule = None

    @property
    def TableIdlType(self):
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def TableInstanceId(self):
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def KeyFields(self):
        return self._KeyFields

    @KeyFields.setter
    def KeyFields(self, KeyFields):
        self._KeyFields = KeyFields

    @property
    def OldKeyFields(self):
        return self._OldKeyFields

    @OldKeyFields.setter
    def OldKeyFields(self, OldKeyFields):
        self._OldKeyFields = OldKeyFields

    @property
    def ValueFields(self):
        return self._ValueFields

    @ValueFields.setter
    def ValueFields(self, ValueFields):
        self._ValueFields = ValueFields

    @property
    def OldValueFields(self):
        return self._OldValueFields

    @OldValueFields.setter
    def OldValueFields(self, OldValueFields):
        self._OldValueFields = OldValueFields

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def SumKeyFieldSize(self):
        return self._SumKeyFieldSize

    @SumKeyFieldSize.setter
    def SumKeyFieldSize(self, SumKeyFieldSize):
        self._SumKeyFieldSize = SumKeyFieldSize

    @property
    def SumValueFieldSize(self):
        return self._SumValueFieldSize

    @SumValueFieldSize.setter
    def SumValueFieldSize(self, SumValueFieldSize):
        self._SumValueFieldSize = SumValueFieldSize

    @property
    def IndexKeySet(self):
        return self._IndexKeySet

    @IndexKeySet.setter
    def IndexKeySet(self, IndexKeySet):
        self._IndexKeySet = IndexKeySet

    @property
    def ShardingKeySet(self):
        return self._ShardingKeySet

    @ShardingKeySet.setter
    def ShardingKeySet(self, ShardingKeySet):
        self._ShardingKeySet = ShardingKeySet

    @property
    def TdrVersion(self):
        return self._TdrVersion

    @TdrVersion.setter
    def TdrVersion(self, TdrVersion):
        self._TdrVersion = TdrVersion

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def ListElementNum(self):
        return self._ListElementNum

    @ListElementNum.setter
    def ListElementNum(self, ListElementNum):
        self._ListElementNum = ListElementNum

    @property
    def SortFieldNum(self):
        return self._SortFieldNum

    @SortFieldNum.setter
    def SortFieldNum(self, SortFieldNum):
        self._SortFieldNum = SortFieldNum

    @property
    def SortRule(self):
        return self._SortRule

    @SortRule.setter
    def SortRule(self, SortRule):
        self._SortRule = SortRule


    def _deserialize(self, params):
        self._TableIdlType = params.get("TableIdlType")
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableName = params.get("TableName")
        self._TableType = params.get("TableType")
        self._KeyFields = params.get("KeyFields")
        self._OldKeyFields = params.get("OldKeyFields")
        self._ValueFields = params.get("ValueFields")
        self._OldValueFields = params.get("OldValueFields")
        self._TableGroupId = params.get("TableGroupId")
        self._SumKeyFieldSize = params.get("SumKeyFieldSize")
        self._SumValueFieldSize = params.get("SumValueFieldSize")
        self._IndexKeySet = params.get("IndexKeySet")
        self._ShardingKeySet = params.get("ShardingKeySet")
        self._TdrVersion = params.get("TdrVersion")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._ListElementNum = params.get("ListElementNum")
        self._SortFieldNum = params.get("SortFieldNum")
        self._SortRule = params.get("SortRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoolInfo(AbstractModel):
    """Information of the machines in the resource pool

    """

    def __init__(self):
        r"""
        :param _PoolUid: Unique ID
        :type PoolUid: int
        :param _Ipv6Enable: Whether IPv6 is supported
        :type Ipv6Enable: int
        :param _AvailableAppCount: Remaining available cluster resources
        :type AvailableAppCount: int
        :param _ServerList: The list of machines at the storage layer (tcapsvr)
        :type ServerList: list of ServerMachineInfo
        :param _ProxyList: The list of machines at the access layer (tcaproxy)
        :type ProxyList: list of ProxyMachineInfo
        """
        self._PoolUid = None
        self._Ipv6Enable = None
        self._AvailableAppCount = None
        self._ServerList = None
        self._ProxyList = None

    @property
    def PoolUid(self):
        return self._PoolUid

    @PoolUid.setter
    def PoolUid(self, PoolUid):
        self._PoolUid = PoolUid

    @property
    def Ipv6Enable(self):
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable

    @property
    def AvailableAppCount(self):
        return self._AvailableAppCount

    @AvailableAppCount.setter
    def AvailableAppCount(self, AvailableAppCount):
        self._AvailableAppCount = AvailableAppCount

    @property
    def ServerList(self):
        return self._ServerList

    @ServerList.setter
    def ServerList(self, ServerList):
        self._ServerList = ServerList

    @property
    def ProxyList(self):
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList


    def _deserialize(self, params):
        self._PoolUid = params.get("PoolUid")
        self._Ipv6Enable = params.get("Ipv6Enable")
        self._AvailableAppCount = params.get("AvailableAppCount")
        if params.get("ServerList") is not None:
            self._ServerList = []
            for item in params.get("ServerList"):
                obj = ServerMachineInfo()
                obj._deserialize(item)
                self._ServerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyMachineInfo()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyDetailInfo(AbstractModel):
    """Information of the machine at the access layer (tcaproxy) in a dedicated cluster

    """

    def __init__(self):
        r"""
        :param _ProxyUid: The unique ID of the access layer (tcaproxy)
        :type ProxyUid: str
        :param _MachineType: Machine type
        :type MachineType: str
        :param _ProcessSpeed: The speed of processing request packets
        :type ProcessSpeed: int
        :param _AverageProcessDelay: Request packet delay
        :type AverageProcessDelay: int
        :param _SlowProcessSpeed: The speed of processing delayed request packets
        :type SlowProcessSpeed: int
        :param _Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        """
        self._ProxyUid = None
        self._MachineType = None
        self._ProcessSpeed = None
        self._AverageProcessDelay = None
        self._SlowProcessSpeed = None
        self._Version = None

    @property
    def ProxyUid(self):
        return self._ProxyUid

    @ProxyUid.setter
    def ProxyUid(self, ProxyUid):
        self._ProxyUid = ProxyUid

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def ProcessSpeed(self):
        return self._ProcessSpeed

    @ProcessSpeed.setter
    def ProcessSpeed(self, ProcessSpeed):
        self._ProcessSpeed = ProcessSpeed

    @property
    def AverageProcessDelay(self):
        return self._AverageProcessDelay

    @AverageProcessDelay.setter
    def AverageProcessDelay(self, AverageProcessDelay):
        self._AverageProcessDelay = AverageProcessDelay

    @property
    def SlowProcessSpeed(self):
        return self._SlowProcessSpeed

    @SlowProcessSpeed.setter
    def SlowProcessSpeed(self, SlowProcessSpeed):
        self._SlowProcessSpeed = SlowProcessSpeed

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._ProxyUid = params.get("ProxyUid")
        self._MachineType = params.get("MachineType")
        self._ProcessSpeed = params.get("ProcessSpeed")
        self._AverageProcessDelay = params.get("AverageProcessDelay")
        self._SlowProcessSpeed = params.get("SlowProcessSpeed")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyMachineInfo(AbstractModel):
    """Information of the machine at the access layer (tcaproxy)

    """

    def __init__(self):
        r"""
        :param _ProxyUid: Unique ID
        :type ProxyUid: str
        :param _MachineType: Machine type
        :type MachineType: str
        :param _AvailableCount: The number of proxy resources to be assigned
        :type AvailableCount: int
        """
        self._ProxyUid = None
        self._MachineType = None
        self._AvailableCount = None

    @property
    def ProxyUid(self):
        return self._ProxyUid

    @ProxyUid.setter
    def ProxyUid(self, ProxyUid):
        self._ProxyUid = ProxyUid

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def AvailableCount(self):
        return self._AvailableCount

    @AvailableCount.setter
    def AvailableCount(self, AvailableCount):
        self._AvailableCount = AvailableCount


    def _deserialize(self, params):
        self._ProxyUid = params.get("ProxyUid")
        self._MachineType = params.get("MachineType")
        self._AvailableCount = params.get("AvailableCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverRecycleTablesRequest(AbstractModel):
    """RecoverRecycleTables request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where a table resides
        :type ClusterId: str
        :param _SelectedTables: Information of tables to be recovered
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverRecycleTablesResponse(AbstractModel):
    """RecoverRecycleTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of recovered tables
        :type TotalCount: int
        :param _TableResults: List of information of recovered tables
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """TcaplusDB service region details

    """

    def __init__(self):
        r"""
        :param _RegionName: Region `Ap-code`
        :type RegionName: str
        :param _RegionAbbr: Region abbreviation
        :type RegionAbbr: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _Ipv6Enable: Whether to support IPv6 address access. Valid values: 0 (support), 1 (not support)
        :type Ipv6Enable: int
        """
        self._RegionName = None
        self._RegionAbbr = None
        self._RegionId = None
        self._Ipv6Enable = None

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionAbbr(self):
        return self._RegionAbbr

    @RegionAbbr.setter
    def RegionAbbr(self, RegionAbbr):
        self._RegionAbbr = RegionAbbr

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Ipv6Enable(self):
        return self._Ipv6Enable

    @Ipv6Enable.setter
    def Ipv6Enable(self, Ipv6Enable):
        self._Ipv6Enable = Ipv6Enable


    def _deserialize(self, params):
        self._RegionName = params.get("RegionName")
        self._RegionAbbr = params.get("RegionAbbr")
        self._RegionId = params.get("RegionId")
        self._Ipv6Enable = params.get("Ipv6Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTablesRequest(AbstractModel):
    """RollbackTables request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table to be rolled back resides
        :type ClusterId: str
        :param _SelectedTables: List of tables to be rolled back
        :type SelectedTables: list of SelectedTableInfoNew
        :param _RollbackTime: Time to roll back to
        :type RollbackTime: str
        :param _Mode: Rollback mode. `KEYS` is supported
        :type Mode: str
        """
        self._ClusterId = None
        self._SelectedTables = None
        self._RollbackTime = None
        self._Mode = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables

    @property
    def RollbackTime(self):
        return self._RollbackTime

    @RollbackTime.setter
    def RollbackTime(self, RollbackTime):
        self._RollbackTime = RollbackTime

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        self._RollbackTime = params.get("RollbackTime")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTablesResponse(AbstractModel):
    """RollbackTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of table rollback task results
        :type TotalCount: int
        :param _TableResults: Table rollback task result list
        :type TableResults: list of TableRollbackResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableRollbackResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class SelectedTableInfoNew(AbstractModel):
    """Information of selected table

    """

    def __init__(self):
        r"""
        :param _TableGroupId: ID of the table group where a table resides
        :type TableGroupId: str
        :param _TableName: Table name
        :type TableName: str
        :param _TableInstanceId: Table instance ID
        :type TableInstanceId: str
        :param _TableIdlType: Table description language type. Valid values: PROTO, TDR
        :type TableIdlType: str
        :param _TableType: Table data structure type. Valid values: GENERIC, LIST
        :type TableType: str
        :param _ListElementNum: Number of LIST-type table elements
        :type ListElementNum: int
        :param _ReservedVolume: Reserved table capacity in GB
        :type ReservedVolume: int
        :param _ReservedReadQps: Reserved table read QPS
        :type ReservedReadQps: int
        :param _ReservedWriteQps: Reserved table write QPS
        :type ReservedWriteQps: int
        :param _Memo: Table remarks
        :type Memo: str
        :param _FileName: Key rollback filename, which is only used for rollback
        :type FileName: str
        :param _FileExtType: Key rollback file extension, which is only used for rollback
        :type FileExtType: str
        :param _FileSize: Key rollback file size, which is only used for rollback
        :type FileSize: int
        :param _FileContent: Key rollback file content, which is only used for rollback
        :type FileContent: str
        """
        self._TableGroupId = None
        self._TableName = None
        self._TableInstanceId = None
        self._TableIdlType = None
        self._TableType = None
        self._ListElementNum = None
        self._ReservedVolume = None
        self._ReservedReadQps = None
        self._ReservedWriteQps = None
        self._Memo = None
        self._FileName = None
        self._FileExtType = None
        self._FileSize = None
        self._FileContent = None

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableInstanceId(self):
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableIdlType(self):
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def ListElementNum(self):
        return self._ListElementNum

    @ListElementNum.setter
    def ListElementNum(self, ListElementNum):
        self._ListElementNum = ListElementNum

    @property
    def ReservedVolume(self):
        return self._ReservedVolume

    @ReservedVolume.setter
    def ReservedVolume(self, ReservedVolume):
        self._ReservedVolume = ReservedVolume

    @property
    def ReservedReadQps(self):
        return self._ReservedReadQps

    @ReservedReadQps.setter
    def ReservedReadQps(self, ReservedReadQps):
        self._ReservedReadQps = ReservedReadQps

    @property
    def ReservedWriteQps(self):
        return self._ReservedWriteQps

    @ReservedWriteQps.setter
    def ReservedWriteQps(self, ReservedWriteQps):
        self._ReservedWriteQps = ReservedWriteQps

    @property
    def Memo(self):
        return self._Memo

    @Memo.setter
    def Memo(self, Memo):
        self._Memo = Memo

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileExtType(self):
        return self._FileExtType

    @FileExtType.setter
    def FileExtType(self, FileExtType):
        self._FileExtType = FileExtType

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableIdlType = params.get("TableIdlType")
        self._TableType = params.get("TableType")
        self._ListElementNum = params.get("ListElementNum")
        self._ReservedVolume = params.get("ReservedVolume")
        self._ReservedReadQps = params.get("ReservedReadQps")
        self._ReservedWriteQps = params.get("ReservedWriteQps")
        self._Memo = params.get("Memo")
        self._FileName = params.get("FileName")
        self._FileExtType = params.get("FileExtType")
        self._FileSize = params.get("FileSize")
        self._FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectedTableWithField(AbstractModel):
    """The list of tables to which the specified fields belong

    """

    def __init__(self):
        r"""
        :param _TableGroupId: ID of the table group where the table resides
        :type TableGroupId: str
        :param _TableName: Table name
        :type TableName: str
        :param _TableInstanceId: Table ID
        :type TableInstanceId: str
        :param _TableIdlType: Table description language. Valid values: `PROTO`, `TDR`
        :type TableIdlType: str
        :param _TableType: Table data structure. Valid values: `GENERIC`, `LIST`
        :type TableType: str
        :param _SelectedFields: The list of fields on which indexes will be created, table caching enabled, or data subscription enabled
        :type SelectedFields: list of FieldInfo
        :param _ShardNum: The number of index shards
        :type ShardNum: int
        :param _KafkaInfo: CKafka instance information
        :type KafkaInfo: :class:`tencentcloud.tcaplusdb.v20190823.models.KafkaInfo`
        """
        self._TableGroupId = None
        self._TableName = None
        self._TableInstanceId = None
        self._TableIdlType = None
        self._TableType = None
        self._SelectedFields = None
        self._ShardNum = None
        self._KafkaInfo = None

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableInstanceId(self):
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableIdlType(self):
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def SelectedFields(self):
        return self._SelectedFields

    @SelectedFields.setter
    def SelectedFields(self, SelectedFields):
        self._SelectedFields = SelectedFields

    @property
    def ShardNum(self):
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def KafkaInfo(self):
        return self._KafkaInfo

    @KafkaInfo.setter
    def KafkaInfo(self, KafkaInfo):
        self._KafkaInfo = KafkaInfo


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableIdlType = params.get("TableIdlType")
        self._TableType = params.get("TableType")
        if params.get("SelectedFields") is not None:
            self._SelectedFields = []
            for item in params.get("SelectedFields"):
                obj = FieldInfo()
                obj._deserialize(item)
                self._SelectedFields.append(obj)
        self._ShardNum = params.get("ShardNum")
        if params.get("KafkaInfo") is not None:
            self._KafkaInfo = KafkaInfo()
            self._KafkaInfo._deserialize(params.get("KafkaInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerDetailInfo(AbstractModel):
    """Information of the machine at the storage layer (tcapsvr) in a dedicated cluster

    """

    def __init__(self):
        r"""
        :param _ServerUid: The unique ID of the storage layer (tcapsvr)
        :type ServerUid: str
        :param _MachineType: Machine type
        :type MachineType: str
        :param _MemoryRate: Memory utilization
        :type MemoryRate: int
        :param _DiskRate: Disk utilization
        :type DiskRate: int
        :param _ReadNum: The number of reads
        :type ReadNum: int
        :param _WriteNum: The number of writes
        :type WriteNum: int
        :param _Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        """
        self._ServerUid = None
        self._MachineType = None
        self._MemoryRate = None
        self._DiskRate = None
        self._ReadNum = None
        self._WriteNum = None
        self._Version = None

    @property
    def ServerUid(self):
        return self._ServerUid

    @ServerUid.setter
    def ServerUid(self, ServerUid):
        self._ServerUid = ServerUid

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MemoryRate(self):
        return self._MemoryRate

    @MemoryRate.setter
    def MemoryRate(self, MemoryRate):
        self._MemoryRate = MemoryRate

    @property
    def DiskRate(self):
        return self._DiskRate

    @DiskRate.setter
    def DiskRate(self, DiskRate):
        self._DiskRate = DiskRate

    @property
    def ReadNum(self):
        return self._ReadNum

    @ReadNum.setter
    def ReadNum(self, ReadNum):
        self._ReadNum = ReadNum

    @property
    def WriteNum(self):
        return self._WriteNum

    @WriteNum.setter
    def WriteNum(self, WriteNum):
        self._WriteNum = WriteNum

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._ServerUid = params.get("ServerUid")
        self._MachineType = params.get("MachineType")
        self._MemoryRate = params.get("MemoryRate")
        self._DiskRate = params.get("DiskRate")
        self._ReadNum = params.get("ReadNum")
        self._WriteNum = params.get("WriteNum")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerMachineInfo(AbstractModel):
    """`ServerList`, the list of machines at the storage layer (tcapsvr)

    """

    def __init__(self):
        r"""
        :param _ServerUid: The unique ID of the machine
        :type ServerUid: str
        :param _MachineType: Machine type
        :type MachineType: str
        """
        self._ServerUid = None
        self._MachineType = None

    @property
    def ServerUid(self):
        return self._ServerUid

    @ServerUid.setter
    def ServerUid(self, ServerUid):
        self._ServerUid = ServerUid

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        self._ServerUid = params.get("ServerUid")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetBackupExpireRuleRequest(AbstractModel):
    """SetBackupExpireRule request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where the tables reside
        :type ClusterId: str
        :param _BackupExpireRules: Array of retention policies
        :type BackupExpireRules: list of BackupExpireRuleInfo
        """
        self._ClusterId = None
        self._BackupExpireRules = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupExpireRules(self):
        return self._BackupExpireRules

    @BackupExpireRules.setter
    def BackupExpireRules(self, BackupExpireRules):
        self._BackupExpireRules = BackupExpireRules


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("BackupExpireRules") is not None:
            self._BackupExpireRules = []
            for item in params.get("BackupExpireRules"):
                obj = BackupExpireRuleInfo()
                obj._deserialize(item)
                self._BackupExpireRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetBackupExpireRuleResponse(AbstractModel):
    """SetBackupExpireRule response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: `TaskId` is in the format of `AppInstanceId-taskId`, which is used to identify tasks of different clusters.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SetTableDataFlowRequest(AbstractModel):
    """SetTableDataFlow request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The ID of the cluster where the tables reside
        :type ClusterId: str
        :param _SelectedTables: The list of tables for which data subscription will be enabled
        :type SelectedTables: list of SelectedTableWithField
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableWithField()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTableDataFlowResponse(AbstractModel):
    """SetTableDataFlow response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of tables for which data subscription has been enabled
        :type TotalCount: int
        :param _TableResults: The result list of tables for which data subscription has been enabled
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class SetTableIndexRequest(AbstractModel):
    """SetTableIndex request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where the table resides
        :type ClusterId: str
        :param _SelectedTables: The list of tables that need to create global indexes
        :type SelectedTables: list of SelectedTableWithField
        """
        self._ClusterId = None
        self._SelectedTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelectedTables(self):
        return self._SelectedTables

    @SelectedTables.setter
    def SelectedTables(self, SelectedTables):
        self._SelectedTables = SelectedTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self._SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableWithField()
                obj._deserialize(item)
                self._SelectedTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTableIndexResponse(AbstractModel):
    """SetTableIndex response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of tables whose global indexes are created
        :type TotalCount: int
        :param _TableResults: The list of global index creation results
        :type TableResults: list of TableResultNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TableResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableResults(self):
        return self._TableResults

    @TableResults.setter
    def TableResults(self, TableResults):
        self._TableResults = TableResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self._TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self._TableResults.append(obj)
        self._RequestId = params.get("RequestId")


class SnapshotInfo(AbstractModel):
    """Snapshot list

    """

    def __init__(self):
        r"""
        :param _TableGroupId: The ID of the table group where the table resides
        :type TableGroupId: str
        :param _TableName: Table name
        :type TableName: str
        :param _SnapshotName: Snapshot name
        :type SnapshotName: str
        :param _SnapshotTime: The time of the data from which the snapshot was created
        :type SnapshotTime: str
        :param _SnapshotDeadTime: Snapshot expiration time
        :type SnapshotDeadTime: str
        """
        self._TableGroupId = None
        self._TableName = None
        self._SnapshotName = None
        self._SnapshotTime = None
        self._SnapshotDeadTime = None

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotTime(self):
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime

    @property
    def SnapshotDeadTime(self):
        return self._SnapshotDeadTime

    @SnapshotDeadTime.setter
    def SnapshotDeadTime(self, SnapshotDeadTime):
        self._SnapshotDeadTime = SnapshotDeadTime


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotTime = params.get("SnapshotTime")
        self._SnapshotDeadTime = params.get("SnapshotDeadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotInfoNew(AbstractModel):
    """New expiration time of a snapshot

    """

    def __init__(self):
        r"""
        :param _TableGroupId: The ID of the table group where the table resides
        :type TableGroupId: str
        :param _TableName: Table name
        :type TableName: str
        :param _SnapshotName: Snapshot name
        :type SnapshotName: str
        :param _SnapshotDeadTime: Snapshot expiration time
        :type SnapshotDeadTime: str
        """
        self._TableGroupId = None
        self._TableName = None
        self._SnapshotName = None
        self._SnapshotDeadTime = None

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotDeadTime(self):
        return self._SnapshotDeadTime

    @SnapshotDeadTime.setter
    def SnapshotDeadTime(self, SnapshotDeadTime):
        self._SnapshotDeadTime = SnapshotDeadTime


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotDeadTime = params.get("SnapshotDeadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotResult(AbstractModel):
    """The result of snapshot creation

    """

    def __init__(self):
        r"""
        :param _TableGroupId: The ID of the table group where the table resides
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param _TableName: Table name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TableName: str
        :param _TaskId: Task ID, which is valid for the API that creates one task at a time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _Error: Error information
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _SnapshotName: Snapshot name
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotName: str
        :param _SnapshotTime: The time of the data from which the snapshot was created
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotTime: str
        :param _SnapshotDeadTime: When the snapshot expires
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotDeadTime: str
        :param _SnapshotCreateTime: When the snapshot was created
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotCreateTime: str
        :param _SnapshotSize: Snapshot size
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotSize: int
        :param _SnapshotStatus: Snapshot status. Valid values: `0` (creating), `1` (normal), `2` (deleting), `3` (expired), `4` (rolling back).
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SnapshotStatus: int
        """
        self._TableGroupId = None
        self._TableName = None
        self._TaskId = None
        self._Error = None
        self._SnapshotName = None
        self._SnapshotTime = None
        self._SnapshotDeadTime = None
        self._SnapshotCreateTime = None
        self._SnapshotSize = None
        self._SnapshotStatus = None

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotTime(self):
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime

    @property
    def SnapshotDeadTime(self):
        return self._SnapshotDeadTime

    @SnapshotDeadTime.setter
    def SnapshotDeadTime(self, SnapshotDeadTime):
        self._SnapshotDeadTime = SnapshotDeadTime

    @property
    def SnapshotCreateTime(self):
        return self._SnapshotCreateTime

    @SnapshotCreateTime.setter
    def SnapshotCreateTime(self, SnapshotCreateTime):
        self._SnapshotCreateTime = SnapshotCreateTime

    @property
    def SnapshotSize(self):
        return self._SnapshotSize

    @SnapshotSize.setter
    def SnapshotSize(self, SnapshotSize):
        self._SnapshotSize = SnapshotSize

    @property
    def SnapshotStatus(self):
        return self._SnapshotStatus

    @SnapshotStatus.setter
    def SnapshotStatus(self, SnapshotStatus):
        self._SnapshotStatus = SnapshotStatus


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._TaskId = params.get("TaskId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotTime = params.get("SnapshotTime")
        self._SnapshotDeadTime = params.get("SnapshotDeadTime")
        self._SnapshotCreateTime = params.get("SnapshotCreateTime")
        self._SnapshotSize = params.get("SnapshotSize")
        self._SnapshotStatus = params.get("SnapshotStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncTableField(AbstractModel):
    """Mapping of cache table field name

    """

    def __init__(self):
        r"""
        :param _SourceName: Field name of TcaplusDB table
        :type SourceName: str
        :param _TargetName: Field name of the target cache table
        :type TargetName: str
        """
        self._SourceName = None
        self._TargetName = None

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def TargetName(self):
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName


    def _deserialize(self, params):
        self._SourceName = params.get("SourceName")
        self._TargetName = params.get("TargetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncTableInfo(AbstractModel):
    """TcaplusDB cache table information

    """

    def __init__(self):
        r"""
        :param _TargetTableSplitNum: Sharded table quantity of the target cache table
        :type TargetTableSplitNum: int
        :param _TargetTableNamePrefix: Prefix of the target cache table name
        :type TargetTableNamePrefix: list of str
        :param _TargetSyncDBInstanceId: Instance ID of the cache database
        :type TargetSyncDBInstanceId: str
        :param _TargetDatabaseName: Name of the database where the cache table resides
        :type TargetDatabaseName: str
        :param _Status: Caching status. Valid values: `0` (creating), `1` (caching), `2` (disabled), `-1` (deleted).
        :type Status: int
        :param _ClusterId: ID of cluster where the table resides
        :type ClusterId: str
        :param _TableGroupId: The ID of the table group where the table resides
        :type TableGroupId: int
        :param _TableName: Table name
        :type TableName: str
        :param _TableId: Table ID
        :type TableId: str
        :param _KeyFieldMapping: Mapping from the primary key field of the TcaplusDB table to the field of the target cache table
        :type KeyFieldMapping: list of SyncTableField
        :param _ValueFieldMapping: Mapping of TcaplusDB table field to target cache table field
        :type ValueFieldMapping: list of SyncTableField
        """
        self._TargetTableSplitNum = None
        self._TargetTableNamePrefix = None
        self._TargetSyncDBInstanceId = None
        self._TargetDatabaseName = None
        self._Status = None
        self._ClusterId = None
        self._TableGroupId = None
        self._TableName = None
        self._TableId = None
        self._KeyFieldMapping = None
        self._ValueFieldMapping = None

    @property
    def TargetTableSplitNum(self):
        return self._TargetTableSplitNum

    @TargetTableSplitNum.setter
    def TargetTableSplitNum(self, TargetTableSplitNum):
        self._TargetTableSplitNum = TargetTableSplitNum

    @property
    def TargetTableNamePrefix(self):
        return self._TargetTableNamePrefix

    @TargetTableNamePrefix.setter
    def TargetTableNamePrefix(self, TargetTableNamePrefix):
        self._TargetTableNamePrefix = TargetTableNamePrefix

    @property
    def TargetSyncDBInstanceId(self):
        return self._TargetSyncDBInstanceId

    @TargetSyncDBInstanceId.setter
    def TargetSyncDBInstanceId(self, TargetSyncDBInstanceId):
        self._TargetSyncDBInstanceId = TargetSyncDBInstanceId

    @property
    def TargetDatabaseName(self):
        return self._TargetDatabaseName

    @TargetDatabaseName.setter
    def TargetDatabaseName(self, TargetDatabaseName):
        self._TargetDatabaseName = TargetDatabaseName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableId(self):
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def KeyFieldMapping(self):
        return self._KeyFieldMapping

    @KeyFieldMapping.setter
    def KeyFieldMapping(self, KeyFieldMapping):
        self._KeyFieldMapping = KeyFieldMapping

    @property
    def ValueFieldMapping(self):
        return self._ValueFieldMapping

    @ValueFieldMapping.setter
    def ValueFieldMapping(self, ValueFieldMapping):
        self._ValueFieldMapping = ValueFieldMapping


    def _deserialize(self, params):
        self._TargetTableSplitNum = params.get("TargetTableSplitNum")
        self._TargetTableNamePrefix = params.get("TargetTableNamePrefix")
        self._TargetSyncDBInstanceId = params.get("TargetSyncDBInstanceId")
        self._TargetDatabaseName = params.get("TargetDatabaseName")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        self._TableName = params.get("TableName")
        self._TableId = params.get("TableId")
        if params.get("KeyFieldMapping") is not None:
            self._KeyFieldMapping = []
            for item in params.get("KeyFieldMapping"):
                obj = SyncTableField()
                obj._deserialize(item)
                self._KeyFieldMapping.append(obj)
        if params.get("ValueFieldMapping") is not None:
            self._ValueFieldMapping = []
            for item in params.get("ValueFieldMapping"):
                obj = SyncTableField()
                obj._deserialize(item)
                self._ValueFieldMapping.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableGroupInfo(AbstractModel):
    """Table group details

    """

    def __init__(self):
        r"""
        :param _TableGroupId: Table group ID
        :type TableGroupId: str
        :param _TableGroupName: Table group name
        :type TableGroupName: str
        :param _CreatedTime: Table group creation time
        :type CreatedTime: str
        :param _TableCount: Number of tables in table group
        :type TableCount: int
        :param _TotalSize: Total table storage capacity in MB in table group
        :type TotalSize: int
        :param _TxhBackupExpireDay: The number of days before the backup files of the Txh tables expire and are deleted.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TxhBackupExpireDay: int
        :param _EnableMysql: Whether MySQL load rebalancing is enabled. Valid values: `0` (Disabled), `1` (Enabling), `2` (Enabled).
        :type EnableMysql: int
        :param _MysqlConnIp: MySQL load rebalancing vip
Note: This field may return null, indicating that no valid values can be obtained.
        :type MysqlConnIp: str
        :param _MysqlConnPort: MySQL load rebalancing vport
Note: This field may return null, indicating that no valid values can be obtained.
        :type MysqlConnPort: int
        """
        self._TableGroupId = None
        self._TableGroupName = None
        self._CreatedTime = None
        self._TableCount = None
        self._TotalSize = None
        self._TxhBackupExpireDay = None
        self._EnableMysql = None
        self._MysqlConnIp = None
        self._MysqlConnPort = None

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableGroupName(self):
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def TableCount(self):
        return self._TableCount

    @TableCount.setter
    def TableCount(self, TableCount):
        self._TableCount = TableCount

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def TxhBackupExpireDay(self):
        return self._TxhBackupExpireDay

    @TxhBackupExpireDay.setter
    def TxhBackupExpireDay(self, TxhBackupExpireDay):
        self._TxhBackupExpireDay = TxhBackupExpireDay

    @property
    def EnableMysql(self):
        return self._EnableMysql

    @EnableMysql.setter
    def EnableMysql(self, EnableMysql):
        self._EnableMysql = EnableMysql

    @property
    def MysqlConnIp(self):
        return self._MysqlConnIp

    @MysqlConnIp.setter
    def MysqlConnIp(self, MysqlConnIp):
        self._MysqlConnIp = MysqlConnIp

    @property
    def MysqlConnPort(self):
        return self._MysqlConnPort

    @MysqlConnPort.setter
    def MysqlConnPort(self, MysqlConnPort):
        self._MysqlConnPort = MysqlConnPort


    def _deserialize(self, params):
        self._TableGroupId = params.get("TableGroupId")
        self._TableGroupName = params.get("TableGroupName")
        self._CreatedTime = params.get("CreatedTime")
        self._TableCount = params.get("TableCount")
        self._TotalSize = params.get("TotalSize")
        self._TxhBackupExpireDay = params.get("TxhBackupExpireDay")
        self._EnableMysql = params.get("EnableMysql")
        self._MysqlConnIp = params.get("MysqlConnIp")
        self._MysqlConnPort = params.get("MysqlConnPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableInfoNew(AbstractModel):
    """Table details

    """

    def __init__(self):
        r"""
        :param _TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _TableInstanceId: Table instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableInstanceId: str
        :param _TableType: Table data structure type, such as `GENERIC` or `LIST`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableType: str
        :param _TableIdlType: Table data interface description language (IDL) type, such as `PROTO` or `TDR`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableIdlType: str
        :param _ClusterId: ID of the cluster where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _ClusterName: Name of the cluster where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param _TableGroupId: ID of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param _TableGroupName: Name of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupName: str
        :param _KeyStruct: JSON string of table's primary key field structure
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyStruct: str
        :param _ValueStruct: JSON string of table non-primary key field structure
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValueStruct: str
        :param _ShardingKeySet: Table shardkey set, which is valid for PROTO-type tables
Note: this field may return null, indicating that no valid values can be obtained.
        :type ShardingKeySet: str
        :param _IndexStruct: Table index key field set, which is valid for PROTO-type tables
Note: this field may return null, indicating that no valid values can be obtained.
        :type IndexStruct: str
        :param _ListElementNum: Number of LIST-type table elements
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListElementNum: int
        :param _IdlFiles: Information list of IDL files associated with table
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdlFiles: list of IdlFileInfo
        :param _ReservedVolume: Reserved table capacity in GB
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReservedVolume: int
        :param _ReservedReadQps: Reserved table read QPS
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReservedReadQps: int
        :param _ReservedWriteQps: Reserved table write QPS
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReservedWriteQps: int
        :param _TableSize: Actual table data size in MB
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableSize: int
        :param _Status: Table status
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _CreatedTime: Table creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _UpdatedTime: Table's last modified time
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdatedTime: str
        :param _Memo: Table remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Memo: str
        :param _Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _ApiAccessId: TcaplusDB SDK data access ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApiAccessId: str
        :param _SortFieldNum: Number of SORTLIST-type table sort fields
Note: this field may return null, indicating that no valid values can be obtained.
        :type SortFieldNum: int
        :param _SortRule: Sort order of SORTLIST-type tables
Note: this field may return null, indicating that no valid values can be obtained.
        :type SortRule: int
        :param _DbClusterInfoStruct: Information about global indexes, table caching, or data subscription
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DbClusterInfoStruct: str
        :param _TxhBackupExpireDay: The number of days after which the table Txh backup files will be expire and deleted.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TxhBackupExpireDay: int
        :param _SyncTableInfo: Cached information of the table
Note: This field may return null, indicating that no valid values can be obtained.
        :type SyncTableInfo: :class:`tencentcloud.tcaplusdb.v20190823.models.SyncTableInfo`
        """
        self._TableName = None
        self._TableInstanceId = None
        self._TableType = None
        self._TableIdlType = None
        self._ClusterId = None
        self._ClusterName = None
        self._TableGroupId = None
        self._TableGroupName = None
        self._KeyStruct = None
        self._ValueStruct = None
        self._ShardingKeySet = None
        self._IndexStruct = None
        self._ListElementNum = None
        self._IdlFiles = None
        self._ReservedVolume = None
        self._ReservedReadQps = None
        self._ReservedWriteQps = None
        self._TableSize = None
        self._Status = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._Memo = None
        self._Error = None
        self._ApiAccessId = None
        self._SortFieldNum = None
        self._SortRule = None
        self._DbClusterInfoStruct = None
        self._TxhBackupExpireDay = None
        self._SyncTableInfo = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableInstanceId(self):
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def TableIdlType(self):
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def TableGroupName(self):
        return self._TableGroupName

    @TableGroupName.setter
    def TableGroupName(self, TableGroupName):
        self._TableGroupName = TableGroupName

    @property
    def KeyStruct(self):
        return self._KeyStruct

    @KeyStruct.setter
    def KeyStruct(self, KeyStruct):
        self._KeyStruct = KeyStruct

    @property
    def ValueStruct(self):
        return self._ValueStruct

    @ValueStruct.setter
    def ValueStruct(self, ValueStruct):
        self._ValueStruct = ValueStruct

    @property
    def ShardingKeySet(self):
        return self._ShardingKeySet

    @ShardingKeySet.setter
    def ShardingKeySet(self, ShardingKeySet):
        self._ShardingKeySet = ShardingKeySet

    @property
    def IndexStruct(self):
        return self._IndexStruct

    @IndexStruct.setter
    def IndexStruct(self, IndexStruct):
        self._IndexStruct = IndexStruct

    @property
    def ListElementNum(self):
        return self._ListElementNum

    @ListElementNum.setter
    def ListElementNum(self, ListElementNum):
        self._ListElementNum = ListElementNum

    @property
    def IdlFiles(self):
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def ReservedVolume(self):
        return self._ReservedVolume

    @ReservedVolume.setter
    def ReservedVolume(self, ReservedVolume):
        self._ReservedVolume = ReservedVolume

    @property
    def ReservedReadQps(self):
        return self._ReservedReadQps

    @ReservedReadQps.setter
    def ReservedReadQps(self, ReservedReadQps):
        self._ReservedReadQps = ReservedReadQps

    @property
    def ReservedWriteQps(self):
        return self._ReservedWriteQps

    @ReservedWriteQps.setter
    def ReservedWriteQps(self, ReservedWriteQps):
        self._ReservedWriteQps = ReservedWriteQps

    @property
    def TableSize(self):
        return self._TableSize

    @TableSize.setter
    def TableSize(self, TableSize):
        self._TableSize = TableSize

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Memo(self):
        return self._Memo

    @Memo.setter
    def Memo(self, Memo):
        self._Memo = Memo

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def ApiAccessId(self):
        return self._ApiAccessId

    @ApiAccessId.setter
    def ApiAccessId(self, ApiAccessId):
        self._ApiAccessId = ApiAccessId

    @property
    def SortFieldNum(self):
        return self._SortFieldNum

    @SortFieldNum.setter
    def SortFieldNum(self, SortFieldNum):
        self._SortFieldNum = SortFieldNum

    @property
    def SortRule(self):
        return self._SortRule

    @SortRule.setter
    def SortRule(self, SortRule):
        self._SortRule = SortRule

    @property
    def DbClusterInfoStruct(self):
        return self._DbClusterInfoStruct

    @DbClusterInfoStruct.setter
    def DbClusterInfoStruct(self, DbClusterInfoStruct):
        self._DbClusterInfoStruct = DbClusterInfoStruct

    @property
    def TxhBackupExpireDay(self):
        return self._TxhBackupExpireDay

    @TxhBackupExpireDay.setter
    def TxhBackupExpireDay(self, TxhBackupExpireDay):
        self._TxhBackupExpireDay = TxhBackupExpireDay

    @property
    def SyncTableInfo(self):
        return self._SyncTableInfo

    @SyncTableInfo.setter
    def SyncTableInfo(self, SyncTableInfo):
        self._SyncTableInfo = SyncTableInfo


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableType = params.get("TableType")
        self._TableIdlType = params.get("TableIdlType")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._TableGroupId = params.get("TableGroupId")
        self._TableGroupName = params.get("TableGroupName")
        self._KeyStruct = params.get("KeyStruct")
        self._ValueStruct = params.get("ValueStruct")
        self._ShardingKeySet = params.get("ShardingKeySet")
        self._IndexStruct = params.get("IndexStruct")
        self._ListElementNum = params.get("ListElementNum")
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        self._ReservedVolume = params.get("ReservedVolume")
        self._ReservedReadQps = params.get("ReservedReadQps")
        self._ReservedWriteQps = params.get("ReservedWriteQps")
        self._TableSize = params.get("TableSize")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._Memo = params.get("Memo")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._ApiAccessId = params.get("ApiAccessId")
        self._SortFieldNum = params.get("SortFieldNum")
        self._SortRule = params.get("SortRule")
        self._DbClusterInfoStruct = params.get("DbClusterInfoStruct")
        self._TxhBackupExpireDay = params.get("TxhBackupExpireDay")
        if params.get("SyncTableInfo") is not None:
            self._SyncTableInfo = SyncTableInfo()
            self._SyncTableInfo._deserialize(params.get("SyncTableInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableResultNew(AbstractModel):
    """Table processing result information

    """

    def __init__(self):
        r"""
        :param _TableInstanceId: Table instance ID in the format of `tcaplus-3be64cbb`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableInstanceId: str
        :param _TaskId: Task ID, which is valid for the API that creates one task
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _TableType: Table data structure type, such as `GENERIC` or `LIST`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableType: str
        :param _TableIdlType: Table data interface description language (IDL) type, such as `PROTO` or `TDR`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableIdlType: str
        :param _TableGroupId: ID of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param _Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _TaskIds: Task ID list, which is valid for the API that creates multiple tasks
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskIds: list of str
        :param _ApplicationId: Cluster operation application ID
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplicationId: str
        """
        self._TableInstanceId = None
        self._TaskId = None
        self._TableName = None
        self._TableType = None
        self._TableIdlType = None
        self._TableGroupId = None
        self._Error = None
        self._TaskIds = None
        self._ApplicationId = None

    @property
    def TableInstanceId(self):
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def TableIdlType(self):
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._TableInstanceId = params.get("TableInstanceId")
        self._TaskId = params.get("TaskId")
        self._TableName = params.get("TableName")
        self._TableType = params.get("TableType")
        self._TableIdlType = params.get("TableIdlType")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._TaskIds = params.get("TaskIds")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableRollbackResultNew(AbstractModel):
    """Table rollback result information

    """

    def __init__(self):
        r"""
        :param _TableInstanceId: Table instance ID in the format of `tcaplus-3be64cbb`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableInstanceId: str
        :param _TaskId: Task ID, which is valid for the API that creates one task
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _TableName: Table name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _TableType: Table data structure type, such as `GENERIC` or `LIST`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableType: str
        :param _TableIdlType: Table data interface description language (IDL) type, such as `PROTO` or `TDR`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableIdlType: str
        :param _TableGroupId: ID of the table group where a table resides
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableGroupId: str
        :param _Error: Error message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param _TaskIds: Task ID list, which is valid for the API that creates multiple tasks
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskIds: list of str
        :param _FileId: ID of uploaded key file
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileId: str
        :param _SuccKeyNum: Number of keys successfully verified
Note: this field may return null, indicating that no valid values can be obtained.
        :type SuccKeyNum: int
        :param _TotalKeyNum: Total number of keys contained in key file
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalKeyNum: int
        """
        self._TableInstanceId = None
        self._TaskId = None
        self._TableName = None
        self._TableType = None
        self._TableIdlType = None
        self._TableGroupId = None
        self._Error = None
        self._TaskIds = None
        self._FileId = None
        self._SuccKeyNum = None
        self._TotalKeyNum = None

    @property
    def TableInstanceId(self):
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def TableIdlType(self):
        return self._TableIdlType

    @TableIdlType.setter
    def TableIdlType(self, TableIdlType):
        self._TableIdlType = TableIdlType

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def SuccKeyNum(self):
        return self._SuccKeyNum

    @SuccKeyNum.setter
    def SuccKeyNum(self, SuccKeyNum):
        self._SuccKeyNum = SuccKeyNum

    @property
    def TotalKeyNum(self):
        return self._TotalKeyNum

    @TotalKeyNum.setter
    def TotalKeyNum(self, TotalKeyNum):
        self._TotalKeyNum = TotalKeyNum


    def _deserialize(self, params):
        self._TableInstanceId = params.get("TableInstanceId")
        self._TaskId = params.get("TaskId")
        self._TableName = params.get("TableName")
        self._TableType = params.get("TableType")
        self._TableIdlType = params.get("TableIdlType")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._TaskIds = params.get("TaskIds")
        self._FileId = params.get("FileId")
        self._SuccKeyNum = params.get("SuccKeyNum")
        self._TotalKeyNum = params.get("TotalKeyNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfoUnit(AbstractModel):
    """Tag information unit

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
        


class TagsInfoOfCluster(AbstractModel):
    """Cluster tag information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Tags: Tag information
        :type Tags: list of TagInfoUnit
        :param _Error: Error message
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._ClusterId = None
        self._Tags = None
        self._Error = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfTable(AbstractModel):
    """Table tag information

    """

    def __init__(self):
        r"""
        :param _TableInstanceId: Table instance ID
        :type TableInstanceId: str
        :param _TableName: Table name
        :type TableName: str
        :param _TableGroupId: Table group ID
        :type TableGroupId: str
        :param _Tags: Tag information
        :type Tags: list of TagInfoUnit
        :param _Error: Error message
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._TableInstanceId = None
        self._TableName = None
        self._TableGroupId = None
        self._Tags = None
        self._Error = None

    @property
    def TableInstanceId(self):
        return self._TableInstanceId

    @TableInstanceId.setter
    def TableInstanceId(self, TableInstanceId):
        self._TableInstanceId = TableInstanceId

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._TableInstanceId = params.get("TableInstanceId")
        self._TableName = params.get("TableName")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfTableGroup(AbstractModel):
    """Table group tag information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _TableGroupId: Table group ID
        :type TableGroupId: str
        :param _Tags: Tag information
        :type Tags: list of TagInfoUnit
        :param _Error: Error message
        :type Error: :class:`tencentcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._Tags = None
        self._Error = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfoNew(AbstractModel):
    """Task details

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _TaskType: Task type
        :type TaskType: str
        :param _TransId: ID of TcaplusDB internal transaction associated with task
        :type TransId: str
        :param _ClusterId: ID of the cluster where a task resides
        :type ClusterId: str
        :param _ClusterName: Name of the cluster where a task resides
        :type ClusterName: str
        :param _Progress: Task progress
        :type Progress: int
        :param _StartTime: Task creation time
        :type StartTime: str
        :param _UpdateTime: Task last modified time
        :type UpdateTime: str
        :param _Operator: Operator
        :type Operator: str
        :param _Content: Task details
        :type Content: str
        """
        self._TaskId = None
        self._TaskType = None
        self._TransId = None
        self._ClusterId = None
        self._ClusterName = None
        self._Progress = None
        self._StartTime = None
        self._UpdateTime = None
        self._Operator = None
        self._Content = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TransId(self):
        return self._TransId

    @TransId.setter
    def TransId(self, TransId):
        self._TransId = TransId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._TransId = params.get("TransId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Progress = params.get("Progress")
        self._StartTime = params.get("StartTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Operator = params.get("Operator")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApplyRequest(AbstractModel):
    """UpdateApply request structure.

    """

    def __init__(self):
        r"""
        :param _ApplyStatus: Application status
        :type ApplyStatus: list of ApplyStatus
        """
        self._ApplyStatus = None

    @property
    def ApplyStatus(self):
        return self._ApplyStatus

    @ApplyStatus.setter
    def ApplyStatus(self, ApplyStatus):
        self._ApplyStatus = ApplyStatus


    def _deserialize(self, params):
        if params.get("ApplyStatus") is not None:
            self._ApplyStatus = []
            for item in params.get("ApplyStatus"):
                obj = ApplyStatus()
                obj._deserialize(item)
                self._ApplyStatus.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApplyResponse(AbstractModel):
    """UpdateApply response structure.

    """

    def __init__(self):
        r"""
        :param _ApplyResults: List of updated applications
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ApplyResults: list of ApplyResult
        :param _TotalCount: Total number of updated applications
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApplyResults = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ApplyResults(self):
        return self._ApplyResults

    @ApplyResults.setter
    def ApplyResults(self, ApplyResults):
        self._ApplyResults = ApplyResults

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ApplyResults") is not None:
            self._ApplyResults = []
            for item in params.get("ApplyResults"):
                obj = ApplyResult()
                obj._deserialize(item)
                self._ApplyResults.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class VerifyIdlFilesRequest(AbstractModel):
    """VerifyIdlFiles request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster where to create a table
        :type ClusterId: str
        :param _TableGroupId: ID of the table group where to create a table
        :type TableGroupId: str
        :param _ExistingIdlFiles: List of information of uploaded IDL files. Either this parameter or `NewIdlFiles` must be present
        :type ExistingIdlFiles: list of IdlFileInfo
        :param _NewIdlFiles: List of information of IDL files to be uploaded. Either this parameter or `ExistingIdlFiles` must be present
        :type NewIdlFiles: list of IdlFileInfo
        """
        self._ClusterId = None
        self._TableGroupId = None
        self._ExistingIdlFiles = None
        self._NewIdlFiles = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TableGroupId(self):
        return self._TableGroupId

    @TableGroupId.setter
    def TableGroupId(self, TableGroupId):
        self._TableGroupId = TableGroupId

    @property
    def ExistingIdlFiles(self):
        return self._ExistingIdlFiles

    @ExistingIdlFiles.setter
    def ExistingIdlFiles(self, ExistingIdlFiles):
        self._ExistingIdlFiles = ExistingIdlFiles

    @property
    def NewIdlFiles(self):
        return self._NewIdlFiles

    @NewIdlFiles.setter
    def NewIdlFiles(self, NewIdlFiles):
        self._NewIdlFiles = NewIdlFiles


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TableGroupId = params.get("TableGroupId")
        if params.get("ExistingIdlFiles") is not None:
            self._ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self._NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._NewIdlFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyIdlFilesResponse(AbstractModel):
    """VerifyIdlFiles response structure.

    """

    def __init__(self):
        r"""
        :param _IdlFiles: Information list of all IDL files uploaded and verified in this request
        :type IdlFiles: list of IdlFileInfo
        :param _TotalCount: Number of valid tables parsed by reading IDL description file, excluding tables already created
        :type TotalCount: int
        :param _TableInfos: List of valid tables parsed by reading IDL description file, excluding tables already created
        :type TableInfos: list of ParsedTableInfoNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IdlFiles = None
        self._TotalCount = None
        self._TableInfos = None
        self._RequestId = None

    @property
    def IdlFiles(self):
        return self._IdlFiles

    @IdlFiles.setter
    def IdlFiles(self, IdlFiles):
        self._IdlFiles = IdlFiles

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TableInfos(self):
        return self._TableInfos

    @TableInfos.setter
    def TableInfos(self, TableInfos):
        self._TableInfos = TableInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IdlFiles") is not None:
            self._IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self._IdlFiles.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self._TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self._TableInfos.append(obj)
        self._RequestId = params.get("RequestId")