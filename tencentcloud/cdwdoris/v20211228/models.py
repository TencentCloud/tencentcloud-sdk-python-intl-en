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


class AttachCBSSpec(AbstractModel):
    """Specifications of nodes in the cluster and disk specifications description

    """

    def __init__(self):
        r"""
        :param _DiskType: Node disk type, such as CLOUD_SSD"\"CLOUD_PREMIUM
        :type DiskType: str
        :param _DiskSize: Disk capacity, in GB
        :type DiskSize: int
        :param _DiskCount: Total number of disks
        :type DiskCount: int
        :param _DiskDesc: Description
        :type DiskDesc: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None
        self._DiskDesc = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskDesc(self):
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskCount = params.get("DiskCount")
        self._DiskDesc = params.get("DiskDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargeProperties(AbstractModel):
    """Cluster billing-related information

    """

    def __init__(self):
        r"""
        :param _ChargeType: Billing type: PREPAID for prepayment, and POSTPAID_BY_HOUR for postpayment.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _RenewFlag: Whether to automatically renew. 1 means automatic renewal is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param _TimeSpan: Billing duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param _TimeUnit: Billing time unit, and "m" means month, etc.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        """
        self._ChargeType = None
        self._RenewFlag = None
        self._TimeSpan = None
        self._TimeUnit = None

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._ChargeType = params.get("ChargeType")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterConfigsInfoFromEMR(AbstractModel):
    """It is used to return configuration files and content in XML format, as well as other information related to the configuration files.

    """

    def __init__(self):
        r"""
        :param _FileName: Configuration file's name
        :type FileName: str
        :param _FileConf: Related attribute information corresponding to the configuration files
        :type FileConf: str
        :param _KeyConf: Other attribute information corresponding to the configuration files
        :type KeyConf: str
        :param _OriParam: Contents of the configuration files, base64 encoded
        :type OriParam: str
        :param _NeedRestart: This is used to indicate whether the current configuration file has been modified without a restart, and reminds the user that a restart is needed.
        :type NeedRestart: int
        :param _FilePath: Configuration file path
Note: This field may return null, indicating that no valid values can be obtained.
        :type FilePath: str
        :param _FileKeyValues: kv value of a configuration file
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileKeyValues: str
        :param _FileKeyValuesNew: kv value of a configuration file
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileKeyValuesNew: list of ConfigKeyValue
        """
        self._FileName = None
        self._FileConf = None
        self._KeyConf = None
        self._OriParam = None
        self._NeedRestart = None
        self._FilePath = None
        self._FileKeyValues = None
        self._FileKeyValuesNew = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileConf(self):
        return self._FileConf

    @FileConf.setter
    def FileConf(self, FileConf):
        self._FileConf = FileConf

    @property
    def KeyConf(self):
        return self._KeyConf

    @KeyConf.setter
    def KeyConf(self, KeyConf):
        self._KeyConf = KeyConf

    @property
    def OriParam(self):
        return self._OriParam

    @OriParam.setter
    def OriParam(self, OriParam):
        self._OriParam = OriParam

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileKeyValues(self):
        warnings.warn("parameter `FileKeyValues` is deprecated", DeprecationWarning) 

        return self._FileKeyValues

    @FileKeyValues.setter
    def FileKeyValues(self, FileKeyValues):
        warnings.warn("parameter `FileKeyValues` is deprecated", DeprecationWarning) 

        self._FileKeyValues = FileKeyValues

    @property
    def FileKeyValuesNew(self):
        return self._FileKeyValuesNew

    @FileKeyValuesNew.setter
    def FileKeyValuesNew(self, FileKeyValuesNew):
        self._FileKeyValuesNew = FileKeyValuesNew


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileConf = params.get("FileConf")
        self._KeyConf = params.get("KeyConf")
        self._OriParam = params.get("OriParam")
        self._NeedRestart = params.get("NeedRestart")
        self._FilePath = params.get("FilePath")
        self._FileKeyValues = params.get("FileKeyValues")
        if params.get("FileKeyValuesNew") is not None:
            self._FileKeyValuesNew = []
            for item in params.get("FileKeyValuesNew"):
                obj = ConfigKeyValue()
                obj._deserialize(item)
                self._FileKeyValuesNew.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigKeyValue(AbstractModel):
    """Return the configuration file content (key-value)

    """

    def __init__(self):
        r"""
        :param _KeyName: key
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyName: str
        :param _Value: Value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param _Message: Notes
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _Display: 1 indicates read-only, 2 indicates editable but undeletable, and 3 indicates deletable.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Display: int
        :param _SupportHotUpdate: 0 means not supported, and 1 means hot update is supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportHotUpdate: int
        """
        self._KeyName = None
        self._Value = None
        self._Message = None
        self._Display = None
        self._SupportHotUpdate = None

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Display(self):
        return self._Display

    @Display.setter
    def Display(self, Display):
        self._Display = Display

    @property
    def SupportHotUpdate(self):
        return self._SupportHotUpdate

    @SupportHotUpdate.setter
    def SupportHotUpdate(self, SupportHotUpdate):
        self._SupportHotUpdate = SupportHotUpdate


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._Value = params.get("Value")
        self._Message = params.get("Message")
        self._Display = params.get("Display")
        self._SupportHotUpdate = params.get("SupportHotUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNewRequest(AbstractModel):
    """CreateInstanceNew request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone
        :type Zone: str
        :param _FeSpec: FE specifications
        :type FeSpec: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        :param _BeSpec: BE specifications.
        :type BeSpec: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceSpec`
        :param _HaFlag: Whether it is highly available.
        :type HaFlag: bool
        :param _UserVPCId: User VPCID
        :type UserVPCId: str
        :param _UserSubnetId: User subnet ID
        :type UserSubnetId: str
        :param _ProductVersion: Product version number
        :type ProductVersion: str
        :param _ChargeProperties: Payment type
        :type ChargeProperties: :class:`tencentcloud.cdwdoris.v20211228.models.ChargeProperties`
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _DorisUserPwd: Database password
        :type DorisUserPwd: str
        :param _Tags: Tag list
        :type Tags: list of Tag
        :param _HaType: High availability type:
0 indicates non-high availability (only one FE, FeSpec.CreateInstanceSpec.Count=1),
1 indicates read high availability (at least 3 FEs must be deployed, FeSpec.CreateInstanceSpec.Count>=3, and it must be an odd number),
2 indicates read and write high availability (at least 5 FEs must be deployed, FeSpec.CreateInstanceSpec.Count>=5, and it must be an odd number).
        :type HaType: int
        :param _CaseSensitive: Whether the table name is case sensitive, 0 refers to sensitive, 1 refers to insensitive, compared in lowercase; 2 refers to insensitive, and the table name is changed to lowercase for storage.
        :type CaseSensitive: int
        :param _EnableMultiZones: Whether to enable multi-availability zone.
        :type EnableMultiZones: bool
        :param _UserMultiZoneInfos: After the Multi-AZ is enabled, all user's Availability Zones and Subnets information are shown.
        :type UserMultiZoneInfos: :class:`tencentcloud.cdwdoris.v20211228.models.NetworkInfo`
        """
        self._Zone = None
        self._FeSpec = None
        self._BeSpec = None
        self._HaFlag = None
        self._UserVPCId = None
        self._UserSubnetId = None
        self._ProductVersion = None
        self._ChargeProperties = None
        self._InstanceName = None
        self._DorisUserPwd = None
        self._Tags = None
        self._HaType = None
        self._CaseSensitive = None
        self._EnableMultiZones = None
        self._UserMultiZoneInfos = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def FeSpec(self):
        return self._FeSpec

    @FeSpec.setter
    def FeSpec(self, FeSpec):
        self._FeSpec = FeSpec

    @property
    def BeSpec(self):
        return self._BeSpec

    @BeSpec.setter
    def BeSpec(self, BeSpec):
        self._BeSpec = BeSpec

    @property
    def HaFlag(self):
        return self._HaFlag

    @HaFlag.setter
    def HaFlag(self, HaFlag):
        self._HaFlag = HaFlag

    @property
    def UserVPCId(self):
        return self._UserVPCId

    @UserVPCId.setter
    def UserVPCId(self, UserVPCId):
        self._UserVPCId = UserVPCId

    @property
    def UserSubnetId(self):
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def ProductVersion(self):
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def ChargeProperties(self):
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def DorisUserPwd(self):
        return self._DorisUserPwd

    @DorisUserPwd.setter
    def DorisUserPwd(self, DorisUserPwd):
        self._DorisUserPwd = DorisUserPwd

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HaType(self):
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def EnableMultiZones(self):
        return self._EnableMultiZones

    @EnableMultiZones.setter
    def EnableMultiZones(self, EnableMultiZones):
        self._EnableMultiZones = EnableMultiZones

    @property
    def UserMultiZoneInfos(self):
        return self._UserMultiZoneInfos

    @UserMultiZoneInfos.setter
    def UserMultiZoneInfos(self, UserMultiZoneInfos):
        self._UserMultiZoneInfos = UserMultiZoneInfos


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        if params.get("FeSpec") is not None:
            self._FeSpec = CreateInstanceSpec()
            self._FeSpec._deserialize(params.get("FeSpec"))
        if params.get("BeSpec") is not None:
            self._BeSpec = CreateInstanceSpec()
            self._BeSpec._deserialize(params.get("BeSpec"))
        self._HaFlag = params.get("HaFlag")
        self._UserVPCId = params.get("UserVPCId")
        self._UserSubnetId = params.get("UserSubnetId")
        self._ProductVersion = params.get("ProductVersion")
        if params.get("ChargeProperties") is not None:
            self._ChargeProperties = ChargeProperties()
            self._ChargeProperties._deserialize(params.get("ChargeProperties"))
        self._InstanceName = params.get("InstanceName")
        self._DorisUserPwd = params.get("DorisUserPwd")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HaType = params.get("HaType")
        self._CaseSensitive = params.get("CaseSensitive")
        self._EnableMultiZones = params.get("EnableMultiZones")
        if params.get("UserMultiZoneInfos") is not None:
            self._UserMultiZoneInfos = NetworkInfo()
            self._UserMultiZoneInfos._deserialize(params.get("UserMultiZoneInfos"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNewResponse(AbstractModel):
    """CreateInstanceNew response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID
        :type FlowId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class CreateInstanceSpec(AbstractModel):
    """Cluster specifications

    """

    def __init__(self):
        r"""
        :param _SpecName: Specification name
        :type SpecName: str
        :param _Count: Quantities
        :type Count: int
        :param _DiskSize: Cloud disk size
        :type DiskSize: int
        """
        self._SpecName = None
        self._Count = None
        self._DiskSize = None

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataBaseAuditRecord(AbstractModel):
    """Database audit

    """

    def __init__(self):
        r"""
        :param _OsUser: Query user
Note: This field may return null, indicating that no valid values can be obtained.
        :type OsUser: str
        :param _InitialQueryId: Query ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InitialQueryId: str
        :param _Sql: SQL statement
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sql: str
        :param _QueryStartTime: Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type QueryStartTime: str
        :param _DurationMs: Execution duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type DurationMs: int
        :param _ReadRows: The number of read rows
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReadRows: int
        :param _ResultRows: Total number of read bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultRows: int
        :param _ResultBytes: Result bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultBytes: int
        :param _MemoryUsage: Memory
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemoryUsage: int
        :param _InitialAddress: Initial query IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type InitialAddress: str
        :param _DbName: Database
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _SqlType: SQL type
Note: This field may return null, indicating that no valid values can be obtained.
        :type SqlType: str
        :param _Catalog: Catalog name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Catalog: str
        """
        self._OsUser = None
        self._InitialQueryId = None
        self._Sql = None
        self._QueryStartTime = None
        self._DurationMs = None
        self._ReadRows = None
        self._ResultRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._InitialAddress = None
        self._DbName = None
        self._SqlType = None
        self._Catalog = None

    @property
    def OsUser(self):
        return self._OsUser

    @OsUser.setter
    def OsUser(self, OsUser):
        self._OsUser = OsUser

    @property
    def InitialQueryId(self):
        return self._InitialQueryId

    @InitialQueryId.setter
    def InitialQueryId(self, InitialQueryId):
        self._InitialQueryId = InitialQueryId

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def QueryStartTime(self):
        return self._QueryStartTime

    @QueryStartTime.setter
    def QueryStartTime(self, QueryStartTime):
        self._QueryStartTime = QueryStartTime

    @property
    def DurationMs(self):
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def ReadRows(self):
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultRows(self):
        return self._ResultRows

    @ResultRows.setter
    def ResultRows(self, ResultRows):
        self._ResultRows = ResultRows

    @property
    def ResultBytes(self):
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def InitialAddress(self):
        return self._InitialAddress

    @InitialAddress.setter
    def InitialAddress(self, InitialAddress):
        self._InitialAddress = InitialAddress

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SqlType(self):
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog


    def _deserialize(self, params):
        self._OsUser = params.get("OsUser")
        self._InitialQueryId = params.get("InitialQueryId")
        self._Sql = params.get("Sql")
        self._QueryStartTime = params.get("QueryStartTime")
        self._DurationMs = params.get("DurationMs")
        self._ReadRows = params.get("ReadRows")
        self._ResultRows = params.get("ResultRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._InitialAddress = params.get("InitialAddress")
        self._DbName = params.get("DbName")
        self._SqlType = params.get("SqlType")
        self._Catalog = params.get("Catalog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterConfigsRequest(AbstractModel):
    """DescribeClusterConfigs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        :param _ConfigType: 0 indicates public cloud query, and 1 Qinge query. Qinge query shows all that needs to be displayed.
        :type ConfigType: int
        :param _FileName: Search for files with fuzzy keywords
        :type FileName: str
        :param _ClusterConfigType: 0 indicates cluster dimension and 1 node dimension
        :type ClusterConfigType: int
        :param _IPAddress: eth0's IP address
        :type IPAddress: str
        """
        self._InstanceId = None
        self._ConfigType = None
        self._FileName = None
        self._ClusterConfigType = None
        self._IPAddress = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigType(self):
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ClusterConfigType(self):
        return self._ClusterConfigType

    @ClusterConfigType.setter
    def ClusterConfigType(self, ClusterConfigType):
        self._ClusterConfigType = ClusterConfigType

    @property
    def IPAddress(self):
        return self._IPAddress

    @IPAddress.setter
    def IPAddress(self, IPAddress):
        self._IPAddress = IPAddress


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConfigType = params.get("ConfigType")
        self._FileName = params.get("FileName")
        self._ClusterConfigType = params.get("ClusterConfigType")
        self._IPAddress = params.get("IPAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterConfigsResponse(AbstractModel):
    """DescribeClusterConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterConfList: Return information about the instance's configuration file.
        :type ClusterConfList: list of ClusterConfigsInfoFromEMR
        :param _BuildVersion: Return the current kernel version. If it does not exist, a null character string is returned.
        :type BuildVersion: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterConfList = None
        self._BuildVersion = None
        self._RequestId = None

    @property
    def ClusterConfList(self):
        return self._ClusterConfList

    @ClusterConfList.setter
    def ClusterConfList(self, ClusterConfList):
        self._ClusterConfList = ClusterConfList

    @property
    def BuildVersion(self):
        return self._BuildVersion

    @BuildVersion.setter
    def BuildVersion(self, BuildVersion):
        self._BuildVersion = BuildVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterConfList") is not None:
            self._ClusterConfList = []
            for item in params.get("ClusterConfList"):
                obj = ClusterConfigsInfoFromEMR()
                obj._deserialize(item)
                self._ClusterConfList.append(obj)
        self._BuildVersion = params.get("BuildVersion")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseAuditDownloadRequest(AbstractModel):
    """DescribeDatabaseAuditDownload request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Paging
        :type PageSize: int
        :param _PageNum: Paging
        :type PageNum: int
        :param _OrderType: Sort parameters
        :type OrderType: str
        :param _User: User
        :type User: str
        :param _DbName: Database
        :type DbName: str
        :param _SqlType: SQL type
        :type SqlType: str
        :param _Sql: SQL statement
        :type Sql: str
        :param _Users: Users (multiple selections)
        :type Users: list of str
        :param _DbNames: Databases (multiple selections)
        :type DbNames: list of str
        :param _SqlTypes: SQL types (multiple selections)
        :type SqlTypes: list of str
        :param _Catalogs: Catalog names (multiple selections)
        :type Catalogs: list of str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNum = None
        self._OrderType = None
        self._User = None
        self._DbName = None
        self._SqlType = None
        self._Sql = None
        self._Users = None
        self._DbNames = None
        self._SqlTypes = None
        self._Catalogs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SqlType(self):
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def DbNames(self):
        return self._DbNames

    @DbNames.setter
    def DbNames(self, DbNames):
        self._DbNames = DbNames

    @property
    def SqlTypes(self):
        return self._SqlTypes

    @SqlTypes.setter
    def SqlTypes(self, SqlTypes):
        self._SqlTypes = SqlTypes

    @property
    def Catalogs(self):
        return self._Catalogs

    @Catalogs.setter
    def Catalogs(self, Catalogs):
        self._Catalogs = Catalogs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._OrderType = params.get("OrderType")
        self._User = params.get("User")
        self._DbName = params.get("DbName")
        self._SqlType = params.get("SqlType")
        self._Sql = params.get("Sql")
        self._Users = params.get("Users")
        self._DbNames = params.get("DbNames")
        self._SqlTypes = params.get("SqlTypes")
        self._Catalogs = params.get("Catalogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseAuditDownloadResponse(AbstractModel):
    """DescribeDatabaseAuditDownload response structure.

    """

    def __init__(self):
        r"""
        :param _CosUrl: The cos address of the log
        :type CosUrl: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CosUrl = None
        self._RequestId = None

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseAuditRecordsRequest(AbstractModel):
    """DescribeDatabaseAuditRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Paging
        :type PageSize: int
        :param _PageNum: Paging
        :type PageNum: int
        :param _OrderType: Sort parameters
        :type OrderType: str
        :param _User: User
        :type User: str
        :param _DbName: Database
        :type DbName: str
        :param _SqlType: SQL type
        :type SqlType: str
        :param _Sql: SQL statement
        :type Sql: str
        :param _Users: Users (multiple selections)
        :type Users: list of str
        :param _DbNames: Databases (multiple selections)
        :type DbNames: list of str
        :param _SqlTypes: SQL types (multiple selections)
        :type SqlTypes: list of str
        :param _Catalogs: Catalog names (multiple selections)
        :type Catalogs: list of str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNum = None
        self._OrderType = None
        self._User = None
        self._DbName = None
        self._SqlType = None
        self._Sql = None
        self._Users = None
        self._DbNames = None
        self._SqlTypes = None
        self._Catalogs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SqlType(self):
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def DbNames(self):
        return self._DbNames

    @DbNames.setter
    def DbNames(self, DbNames):
        self._DbNames = DbNames

    @property
    def SqlTypes(self):
        return self._SqlTypes

    @SqlTypes.setter
    def SqlTypes(self, SqlTypes):
        self._SqlTypes = SqlTypes

    @property
    def Catalogs(self):
        return self._Catalogs

    @Catalogs.setter
    def Catalogs(self, Catalogs):
        self._Catalogs = Catalogs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._OrderType = params.get("OrderType")
        self._User = params.get("User")
        self._DbName = params.get("DbName")
        self._SqlType = params.get("SqlType")
        self._Sql = params.get("Sql")
        self._Users = params.get("Users")
        self._DbNames = params.get("DbNames")
        self._SqlTypes = params.get("SqlTypes")
        self._Catalogs = params.get("Catalogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseAuditRecordsResponse(AbstractModel):
    """DescribeDatabaseAuditRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total
        :type TotalCount: int
        :param _SlowQueryRecords: Record list
        :type SlowQueryRecords: :class:`tencentcloud.cdwdoris.v20211228.models.DataBaseAuditRecord`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowQueryRecords = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowQueryRecords(self):
        return self._SlowQueryRecords

    @SlowQueryRecords.setter
    def SlowQueryRecords(self, SlowQueryRecords):
        self._SlowQueryRecords = SlowQueryRecords

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SlowQueryRecords") is not None:
            self._SlowQueryRecords = DataBaseAuditRecord()
            self._SlowQueryRecords._deserialize(params.get("SlowQueryRecords"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesInfoRequest(AbstractModel):
    """DescribeInstanceNodesInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceID: Cluster ID
        :type InstanceID: str
        """
        self._InstanceID = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesInfoResponse(AbstractModel):
    """DescribeInstanceNodesInfo response structure.

    """

    def __init__(self):
        r"""
        :param _BeNodes: Be node
Note: This field may return null, indicating that no valid values can be obtained.
        :type BeNodes: list of str
        :param _FeNodes: Fe node
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeNodes: list of str
        :param _FeMaster: Fe master node
        :type FeMaster: str
        :param _BeNodeInfos: Be node information
Note: This field may return null, indicating that no valid values can be obtained.
        :type BeNodeInfos: list of NodeInfo
        :param _FeNodeInfos: Fe node information
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeNodeInfos: list of NodeInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BeNodes = None
        self._FeNodes = None
        self._FeMaster = None
        self._BeNodeInfos = None
        self._FeNodeInfos = None
        self._RequestId = None

    @property
    def BeNodes(self):
        return self._BeNodes

    @BeNodes.setter
    def BeNodes(self, BeNodes):
        self._BeNodes = BeNodes

    @property
    def FeNodes(self):
        return self._FeNodes

    @FeNodes.setter
    def FeNodes(self, FeNodes):
        self._FeNodes = FeNodes

    @property
    def FeMaster(self):
        return self._FeMaster

    @FeMaster.setter
    def FeMaster(self, FeMaster):
        self._FeMaster = FeMaster

    @property
    def BeNodeInfos(self):
        return self._BeNodeInfos

    @BeNodeInfos.setter
    def BeNodeInfos(self, BeNodeInfos):
        self._BeNodeInfos = BeNodeInfos

    @property
    def FeNodeInfos(self):
        return self._FeNodeInfos

    @FeNodeInfos.setter
    def FeNodeInfos(self, FeNodeInfos):
        self._FeNodeInfos = FeNodeInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BeNodes = params.get("BeNodes")
        self._FeNodes = params.get("FeNodes")
        self._FeMaster = params.get("FeMaster")
        if params.get("BeNodeInfos") is not None:
            self._BeNodeInfos = []
            for item in params.get("BeNodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._BeNodeInfos.append(obj)
        if params.get("FeNodeInfos") is not None:
            self._FeNodeInfos = []
            for item in params.get("FeNodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._FeNodeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesRequest(AbstractModel):
    """DescribeInstanceNodes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        :param _NodeRole: Cluster role type, defaulted as "data node".
        :type NodeRole: str
        :param _Offset: Pagination parameters. The first page is 0, and the second page is 10.
        :type Offset: int
        :param _Limit: Pagination parameters. The pagination step length is 10 by default.
        :type Limit: int
        :param _DisplayPolicy: Display policy, and all items are displayed when All is selected.
        :type DisplayPolicy: str
        """
        self._InstanceId = None
        self._NodeRole = None
        self._Offset = None
        self._Limit = None
        self._DisplayPolicy = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

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
    def DisplayPolicy(self):
        return self._DisplayPolicy

    @DisplayPolicy.setter
    def DisplayPolicy(self, DisplayPolicy):
        self._DisplayPolicy = DisplayPolicy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeRole = params.get("NodeRole")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DisplayPolicy = params.get("DisplayPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesResponse(AbstractModel):
    """DescribeInstanceNodes response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _InstanceNodesList: Total number of instance nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceNodesList: list of InstanceNode
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceNodesList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceNodesList(self):
        return self._InstanceNodesList

    @InstanceNodesList.setter
    def InstanceNodesList(self, InstanceNodesList):
        self._InstanceNodesList = InstanceNodesList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceNodesList") is not None:
            self._InstanceNodesList = []
            for item in params.get("InstanceNodesList"):
                obj = InstanceNode()
                obj._deserialize(item)
                self._InstanceNodesList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeInstanceResponse(AbstractModel):
    """DescribeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceInfo: Instance description information
        :type InstanceInfo: :class:`tencentcloud.cdwdoris.v20211228.models.InstanceInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceInfo = None
        self._RequestId = None

    @property
    def InstanceInfo(self):
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceStateRequest(AbstractModel):
    """DescribeInstanceState request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance name
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeInstanceStateResponse(AbstractModel):
    """DescribeInstanceState response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceState: Cluster status. Example: Serving
        :type InstanceState: str
        :param _FlowCreateTime: Creation time of cluster operation
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowCreateTime: str
        :param _FlowName: Cluster operation name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowName: str
        :param _FlowProgress: Cluster operation progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowProgress: float
        :param _InstanceStateDesc: Cluster status description. Example: running
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceStateDesc: str
        :param _FlowMsg: Cluster process error messages, such as "Creation failed, insufficient resources"
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._RequestId = None

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: The name of the cluster ID for the search
        :type SearchInstanceId: str
        :param _SearchInstanceName: The cluster name for the search
        :type SearchInstanceName: str
        :param _Offset: Pagination parameters. The first page is 0, and the second page is 10.
        :type Offset: int
        :param _Limit: Pagination parameters. The pagination step length is 10 by default.
        :type Limit: int
        :param _SearchTags: Search tag list
        :type SearchTags: list of SearchTags
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None

    @property
    def SearchInstanceId(self):
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

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
    def SearchTags(self):
        return self._SearchTags

    @SearchTags.setter
    def SearchTags(self, SearchTags):
        self._SearchTags = SearchTags


    def _deserialize(self, params):
        self._SearchInstanceId = params.get("SearchInstanceId")
        self._SearchInstanceName = params.get("SearchInstanceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("SearchTags") is not None:
            self._SearchTags = []
            for item in params.get("SearchTags"):
                obj = SearchTags()
                obj._deserialize(item)
                self._SearchTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total Number of Instances
        :type TotalCount: int
        :param _InstancesList: Quantities of instances array
        :type InstancesList: list of InstanceInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstancesList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryRecordsDownloadRequest(AbstractModel):
    """DescribeSlowQueryRecordsDownload request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _QueryDurationMs: Slow log time
        :type QueryDurationMs: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _DurationMs: Sort parameters
        :type DurationMs: str
        :param _Sql: Query SQL
        :type Sql: str
        :param _ReadRows: Sort parameters
        :type ReadRows: str
        :param _ResultBytes: Sort parameters
        :type ResultBytes: str
        :param _MemoryUsage: Sort parameters
        :type MemoryUsage: str
        :param _IsQuery: IsQuery condition
        :type IsQuery: int
        :param _DbName: Database name
        :type DbName: list of str
        :param _CatalogName: catalog name
        :type CatalogName: list of str
        """
        self._InstanceId = None
        self._QueryDurationMs = None
        self._StartTime = None
        self._EndTime = None
        self._DurationMs = None
        self._Sql = None
        self._ReadRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._IsQuery = None
        self._DbName = None
        self._CatalogName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def QueryDurationMs(self):
        return self._QueryDurationMs

    @QueryDurationMs.setter
    def QueryDurationMs(self, QueryDurationMs):
        self._QueryDurationMs = QueryDurationMs

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
    def DurationMs(self):
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def ReadRows(self):
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultBytes(self):
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def IsQuery(self):
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CatalogName(self):
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._QueryDurationMs = params.get("QueryDurationMs")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DurationMs = params.get("DurationMs")
        self._Sql = params.get("Sql")
        self._ReadRows = params.get("ReadRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._IsQuery = params.get("IsQuery")
        self._DbName = params.get("DbName")
        self._CatalogName = params.get("CatalogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryRecordsDownloadResponse(AbstractModel):
    """DescribeSlowQueryRecordsDownload response structure.

    """

    def __init__(self):
        r"""
        :param _CosUrl: cos address
        :type CosUrl: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CosUrl = None
        self._RequestId = None

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class DescribeSlowQueryRecordsRequest(AbstractModel):
    """DescribeSlowQueryRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _QueryDurationMs: Slow log time
        :type QueryDurationMs: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Paging
        :type PageSize: int
        :param _PageNum: Paging
        :type PageNum: int
        :param _DurationMs: Sort parameters
        :type DurationMs: str
        :param _DbName: Database name
        :type DbName: list of str
        :param _IsQuery: Whether it is a query. 0 indicates no, and 1 indicates yes.
        :type IsQuery: int
        :param _CatalogName: catalog name
        :type CatalogName: list of str
        :param _Sql: SQL name
        :type Sql: str
        :param _ReadRows: ReadRows sort field
        :type ReadRows: str
        :param _ResultBytes: ResultBytes sort field
        :type ResultBytes: str
        :param _MemoryUsage: MemoryUsage sort field
        :type MemoryUsage: str
        """
        self._InstanceId = None
        self._QueryDurationMs = None
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNum = None
        self._DurationMs = None
        self._DbName = None
        self._IsQuery = None
        self._CatalogName = None
        self._Sql = None
        self._ReadRows = None
        self._ResultBytes = None
        self._MemoryUsage = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def QueryDurationMs(self):
        return self._QueryDurationMs

    @QueryDurationMs.setter
    def QueryDurationMs(self, QueryDurationMs):
        self._QueryDurationMs = QueryDurationMs

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
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def DurationMs(self):
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def IsQuery(self):
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def CatalogName(self):
        return self._CatalogName

    @CatalogName.setter
    def CatalogName(self, CatalogName):
        self._CatalogName = CatalogName

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def ReadRows(self):
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultBytes(self):
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._QueryDurationMs = params.get("QueryDurationMs")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._DurationMs = params.get("DurationMs")
        self._DbName = params.get("DbName")
        self._IsQuery = params.get("IsQuery")
        self._CatalogName = params.get("CatalogName")
        self._Sql = params.get("Sql")
        self._ReadRows = params.get("ReadRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowQueryRecordsResponse(AbstractModel):
    """DescribeSlowQueryRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total
        :type TotalCount: int
        :param _SlowQueryRecords: Record list
        :type SlowQueryRecords: list of SlowQueryRecord
        :param _DBNameList: All database names
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBNameList: list of str
        :param _CatalogNameList: All catalog names
Note: This field may return null, indicating that no valid values can be obtained.
        :type CatalogNameList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowQueryRecords = None
        self._DBNameList = None
        self._CatalogNameList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowQueryRecords(self):
        return self._SlowQueryRecords

    @SlowQueryRecords.setter
    def SlowQueryRecords(self, SlowQueryRecords):
        self._SlowQueryRecords = SlowQueryRecords

    @property
    def DBNameList(self):
        return self._DBNameList

    @DBNameList.setter
    def DBNameList(self, DBNameList):
        self._DBNameList = DBNameList

    @property
    def CatalogNameList(self):
        return self._CatalogNameList

    @CatalogNameList.setter
    def CatalogNameList(self, CatalogNameList):
        self._CatalogNameList = CatalogNameList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SlowQueryRecords") is not None:
            self._SlowQueryRecords = []
            for item in params.get("SlowQueryRecords"):
                obj = SlowQueryRecord()
                obj._deserialize(item)
                self._SlowQueryRecords.append(obj)
        self._DBNameList = params.get("DBNameList")
        self._CatalogNameList = params.get("CatalogNameList")
        self._RequestId = params.get("RequestId")


class DestroyInstanceRequest(AbstractModel):
    """DestroyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DestroyInstanceResponse(AbstractModel):
    """DestroyInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID
        :type FlowId: str
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """Instance description information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID, "cdw-xxxx" string type
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Cluster instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Status: Status,
Init is being created. Serving is running. 
Deleted indicates the cluster has been terminated. Deleting indicates the cluster is being terminated.
Modify indicates the cluster is being changed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _Region: Region, ap-guangzhou
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zone: Availability zone, ap-guangzhou-3
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _VpcId: VPC name
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _PayMode: Payment type: hour and prepay
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ExpireTime: Expiration time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _MasterSummary: Data node description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterSummary: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        :param _CoreSummary: Zookeeper node description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type CoreSummary: :class:`tencentcloud.cdwdoris.v20211228.models.NodesSummary`
        :param _HA: High availability, being true or false
Note: This field may return null, indicating that no valid values can be obtained.
        :type HA: str
        :param _HaType: High availability type:
0: non-high availability
1: read high availability
2: read-write high availability
Note: This field may return null, indicating that no valid values can be obtained.
        :type HaType: int
        :param _AccessInfo: Access address. Example: 10.0.0.1:9000
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessInfo: str
        :param _Id: Record ID, in numerical type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _RegionId: Region ID, indicating the region
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _ZoneDesc: Note about availability zone, such as Guangzhou Zone 2
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneDesc: str
        :param _FlowMsg: Error process description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowMsg: str
        :param _StatusDesc: Status description, such as "running"
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusDesc: str
        :param _RenewFlag: Automatic renewal marker
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: bool
        :param _Tags: Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Monitor: Monitoring Information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Monitor: str
        :param _HasClsTopic: Whether to enable logs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasClsTopic: bool
        :param _ClsTopicId: Log Topic ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClsTopicId: str
        :param _ClsLogSetId: Logset ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClsLogSetId: str
        :param _EnableXMLConfig: Whether to support XML configuration management.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableXMLConfig: int
        :param _RegionDesc: Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionDesc: str
        :param _Eip: Elastic network interface address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Eip: str
        :param _CosMoveFactor: Cold and hot stratification coefficient
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosMoveFactor: int
        :param _Kind: external/local/yunti
Note: This field may return null, indicating that no valid values can be obtained.
        :type Kind: str
        :param _CosBucketName: COS bucket
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosBucketName: str
        :param _CanAttachCbs: cbs
Note: This field may return null, indicating that no valid values can be obtained.
        :type CanAttachCbs: bool
        :param _BuildVersion: Minor versions
Note: This field may return null, indicating that no valid values can be obtained.
        :type BuildVersion: str
        :param _Components: Component Information
Note: The return type here is map[string]struct, not the string type displayed. You can refer to "Sample Value" to parse the data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Components: str
        :param _IfExistCatalog: Determine whether the audit log table has a catalog field.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IfExistCatalog: int
        :param _Characteristic: Page features, used to block some page entrances on the front end.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Characteristic: list of str
        :param _RestartTimeout: Timeout period, in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type RestartTimeout: str
        :param _GraceShutdownWaitSeconds: The timeout time for the graceful restart of the kernel. If it is -1, it means it is not set.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GraceShutdownWaitSeconds: str
        :param _CaseSensitive: Whether the table name is case sensitive, 0 refers to sensitive, 1 refers to insensitive, compared in lowercase; 2 refers to insensitive, and the table name is changed to lowercase for storage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CaseSensitive: int
        :param _IsWhiteSGs: Whether users can bind security groups.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsWhiteSGs: bool
        :param _BindSGs: Bound security group information
Note: This field may return null, indicating that no valid values can be obtained.
        :type BindSGs: list of str
        :param _EnableMultiZones: Whether it is a multi-AZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableMultiZones: bool
        :param _UserNetworkInfos: User availability zone and subnet information
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserNetworkInfos: str
        :param _EnableCoolDown: Whether to enable hot and cold stratification. 0 refers to disabled, and 1 refers to enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableCoolDown: int
        :param _CoolDownBucket: COS buckets are used for hot and cold stratification
Note: This field may return null, indicating that no valid values can be obtained.
        :type CoolDownBucket: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._Version = None
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._PayMode = None
        self._CreateTime = None
        self._ExpireTime = None
        self._MasterSummary = None
        self._CoreSummary = None
        self._HA = None
        self._HaType = None
        self._AccessInfo = None
        self._Id = None
        self._RegionId = None
        self._ZoneDesc = None
        self._FlowMsg = None
        self._StatusDesc = None
        self._RenewFlag = None
        self._Tags = None
        self._Monitor = None
        self._HasClsTopic = None
        self._ClsTopicId = None
        self._ClsLogSetId = None
        self._EnableXMLConfig = None
        self._RegionDesc = None
        self._Eip = None
        self._CosMoveFactor = None
        self._Kind = None
        self._CosBucketName = None
        self._CanAttachCbs = None
        self._BuildVersion = None
        self._Components = None
        self._IfExistCatalog = None
        self._Characteristic = None
        self._RestartTimeout = None
        self._GraceShutdownWaitSeconds = None
        self._CaseSensitive = None
        self._IsWhiteSGs = None
        self._BindSGs = None
        self._EnableMultiZones = None
        self._UserNetworkInfos = None
        self._EnableCoolDown = None
        self._CoolDownBucket = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def MasterSummary(self):
        return self._MasterSummary

    @MasterSummary.setter
    def MasterSummary(self, MasterSummary):
        self._MasterSummary = MasterSummary

    @property
    def CoreSummary(self):
        return self._CoreSummary

    @CoreSummary.setter
    def CoreSummary(self, CoreSummary):
        self._CoreSummary = CoreSummary

    @property
    def HA(self):
        return self._HA

    @HA.setter
    def HA(self, HA):
        self._HA = HA

    @property
    def HaType(self):
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType

    @property
    def AccessInfo(self):
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneDesc(self):
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def FlowMsg(self):
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Monitor(self):
        return self._Monitor

    @Monitor.setter
    def Monitor(self, Monitor):
        self._Monitor = Monitor

    @property
    def HasClsTopic(self):
        return self._HasClsTopic

    @HasClsTopic.setter
    def HasClsTopic(self, HasClsTopic):
        self._HasClsTopic = HasClsTopic

    @property
    def ClsTopicId(self):
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def ClsLogSetId(self):
        return self._ClsLogSetId

    @ClsLogSetId.setter
    def ClsLogSetId(self, ClsLogSetId):
        self._ClsLogSetId = ClsLogSetId

    @property
    def EnableXMLConfig(self):
        return self._EnableXMLConfig

    @EnableXMLConfig.setter
    def EnableXMLConfig(self, EnableXMLConfig):
        self._EnableXMLConfig = EnableXMLConfig

    @property
    def RegionDesc(self):
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def Eip(self):
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def CosMoveFactor(self):
        return self._CosMoveFactor

    @CosMoveFactor.setter
    def CosMoveFactor(self, CosMoveFactor):
        self._CosMoveFactor = CosMoveFactor

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def CosBucketName(self):
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CanAttachCbs(self):
        return self._CanAttachCbs

    @CanAttachCbs.setter
    def CanAttachCbs(self, CanAttachCbs):
        self._CanAttachCbs = CanAttachCbs

    @property
    def BuildVersion(self):
        return self._BuildVersion

    @BuildVersion.setter
    def BuildVersion(self, BuildVersion):
        self._BuildVersion = BuildVersion

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def IfExistCatalog(self):
        warnings.warn("parameter `IfExistCatalog` is deprecated", DeprecationWarning) 

        return self._IfExistCatalog

    @IfExistCatalog.setter
    def IfExistCatalog(self, IfExistCatalog):
        warnings.warn("parameter `IfExistCatalog` is deprecated", DeprecationWarning) 

        self._IfExistCatalog = IfExistCatalog

    @property
    def Characteristic(self):
        return self._Characteristic

    @Characteristic.setter
    def Characteristic(self, Characteristic):
        self._Characteristic = Characteristic

    @property
    def RestartTimeout(self):
        return self._RestartTimeout

    @RestartTimeout.setter
    def RestartTimeout(self, RestartTimeout):
        self._RestartTimeout = RestartTimeout

    @property
    def GraceShutdownWaitSeconds(self):
        return self._GraceShutdownWaitSeconds

    @GraceShutdownWaitSeconds.setter
    def GraceShutdownWaitSeconds(self, GraceShutdownWaitSeconds):
        self._GraceShutdownWaitSeconds = GraceShutdownWaitSeconds

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def IsWhiteSGs(self):
        return self._IsWhiteSGs

    @IsWhiteSGs.setter
    def IsWhiteSGs(self, IsWhiteSGs):
        self._IsWhiteSGs = IsWhiteSGs

    @property
    def BindSGs(self):
        return self._BindSGs

    @BindSGs.setter
    def BindSGs(self, BindSGs):
        self._BindSGs = BindSGs

    @property
    def EnableMultiZones(self):
        return self._EnableMultiZones

    @EnableMultiZones.setter
    def EnableMultiZones(self, EnableMultiZones):
        self._EnableMultiZones = EnableMultiZones

    @property
    def UserNetworkInfos(self):
        return self._UserNetworkInfos

    @UserNetworkInfos.setter
    def UserNetworkInfos(self, UserNetworkInfos):
        self._UserNetworkInfos = UserNetworkInfos

    @property
    def EnableCoolDown(self):
        return self._EnableCoolDown

    @EnableCoolDown.setter
    def EnableCoolDown(self, EnableCoolDown):
        self._EnableCoolDown = EnableCoolDown

    @property
    def CoolDownBucket(self):
        return self._CoolDownBucket

    @CoolDownBucket.setter
    def CoolDownBucket(self, CoolDownBucket):
        self._CoolDownBucket = CoolDownBucket


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._Version = params.get("Version")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        if params.get("MasterSummary") is not None:
            self._MasterSummary = NodesSummary()
            self._MasterSummary._deserialize(params.get("MasterSummary"))
        if params.get("CoreSummary") is not None:
            self._CoreSummary = NodesSummary()
            self._CoreSummary._deserialize(params.get("CoreSummary"))
        self._HA = params.get("HA")
        self._HaType = params.get("HaType")
        self._AccessInfo = params.get("AccessInfo")
        self._Id = params.get("Id")
        self._RegionId = params.get("RegionId")
        self._ZoneDesc = params.get("ZoneDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._StatusDesc = params.get("StatusDesc")
        self._RenewFlag = params.get("RenewFlag")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Monitor = params.get("Monitor")
        self._HasClsTopic = params.get("HasClsTopic")
        self._ClsTopicId = params.get("ClsTopicId")
        self._ClsLogSetId = params.get("ClsLogSetId")
        self._EnableXMLConfig = params.get("EnableXMLConfig")
        self._RegionDesc = params.get("RegionDesc")
        self._Eip = params.get("Eip")
        self._CosMoveFactor = params.get("CosMoveFactor")
        self._Kind = params.get("Kind")
        self._CosBucketName = params.get("CosBucketName")
        self._CanAttachCbs = params.get("CanAttachCbs")
        self._BuildVersion = params.get("BuildVersion")
        self._Components = params.get("Components")
        self._IfExistCatalog = params.get("IfExistCatalog")
        self._Characteristic = params.get("Characteristic")
        self._RestartTimeout = params.get("RestartTimeout")
        self._GraceShutdownWaitSeconds = params.get("GraceShutdownWaitSeconds")
        self._CaseSensitive = params.get("CaseSensitive")
        self._IsWhiteSGs = params.get("IsWhiteSGs")
        self._BindSGs = params.get("BindSGs")
        self._EnableMultiZones = params.get("EnableMultiZones")
        self._UserNetworkInfos = params.get("UserNetworkInfos")
        self._EnableCoolDown = params.get("EnableCoolDown")
        self._CoolDownBucket = params.get("CoolDownBucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    """Instance node description information

    """

    def __init__(self):
        r"""
        :param _Ip: IP address
        :type Ip: str
        :param _Spec: Model, such as S1
        :type Spec: str
        :param _Core: Number of CPU cores
        :type Core: int
        :param _Memory: Memory size
        :type Memory: int
        :param _DiskType: Disk type
        :type DiskType: str
        :param _DiskSize: Disk size
        :type DiskSize: int
        :param _Role: The name of the clickhouse cluster to which it belongs.
        :type Role: str
        :param _Status: Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Rip: rip
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rip: str
        :param _FeRole: FE node role
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeRole: str
        :param _UUID: UUID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UUID: str
        """
        self._Ip = None
        self._Spec = None
        self._Core = None
        self._Memory = None
        self._DiskType = None
        self._DiskSize = None
        self._Role = None
        self._Status = None
        self._Rip = None
        self._FeRole = None
        self._UUID = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Core(self):
        return self._Core

    @Core.setter
    def Core(self, Core):
        self._Core = Core

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rip(self):
        return self._Rip

    @Rip.setter
    def Rip(self, Rip):
        self._Rip = Rip

    @property
    def FeRole(self):
        return self._FeRole

    @FeRole.setter
    def FeRole(self, FeRole):
        self._FeRole = FeRole

    @property
    def UUID(self):
        return self._UUID

    @UUID.setter
    def UUID(self, UUID):
        self._UUID = UUID


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Spec = params.get("Spec")
        self._Core = params.get("Core")
        self._Memory = params.get("Memory")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._Rip = params.get("Rip")
        self._FeRole = params.get("FeRole")
        self._UUID = params.get("UUID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Newly modified instance name
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class NetworkInfo(AbstractModel):
    """Network information

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _SubnetId: Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _SubnetIpNum: The number of available IP addresses in the current subnet
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetIpNum: int
        """
        self._Zone = None
        self._SubnetId = None
        self._SubnetIpNum = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetIpNum(self):
        return self._SubnetIpNum

    @SubnetIpNum.setter
    def SubnetIpNum(self, SubnetIpNum):
        self._SubnetIpNum = SubnetIpNum


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        self._SubnetIpNum = params.get("SubnetIpNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """NodeInfo

    """

    def __init__(self):
        r"""
        :param _Ip: User IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param _Status: Node status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _NodeName: Node role name
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeName: str
        :param _ComponentName: Component name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentName: str
        :param _NodeRole: Node role
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeRole: str
        :param _LastRestartTime: The time when the node was last restarted
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastRestartTime: str
        :param _Zone: The availability zone where the node is located
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        """
        self._Ip = None
        self._Status = None
        self._NodeName = None
        self._ComponentName = None
        self._NodeRole = None
        self._LastRestartTime = None
        self._Zone = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def LastRestartTime(self):
        return self._LastRestartTime

    @LastRestartTime.setter
    def LastRestartTime(self, LastRestartTime):
        self._LastRestartTime = LastRestartTime

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Status = params.get("Status")
        self._NodeName = params.get("NodeName")
        self._ComponentName = params.get("ComponentName")
        self._NodeRole = params.get("NodeRole")
        self._LastRestartTime = params.get("LastRestartTime")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodesSummary(AbstractModel):
    """Node role description information

    """

    def __init__(self):
        r"""
        :param _Spec: Model, such as S1
        :type Spec: str
        :param _NodeSize: Number of nodes
        :type NodeSize: int
        :param _Core: Number of CPU cores, in counts
        :type Core: int
        :param _Memory: Memory size, in GB
        :type Memory: int
        :param _Disk: Disk size, in GB
        :type Disk: int
        :param _DiskType: Disk type
        :type DiskType: str
        :param _DiskDesc: Disk description
        :type DiskDesc: str
        :param _AttachCBSSpec: Information of mounted cloud disks
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttachCBSSpec: :class:`tencentcloud.cdwdoris.v20211228.models.AttachCBSSpec`
        :param _SubProductType: Sub-product name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubProductType: str
        :param _SpecCore: Specified cores
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecCore: int
        :param _SpecMemory: Specified memory
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecMemory: int
        :param _DiskCount: Disk size
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskCount: int
        :param _Encrypt: Whether it is encrypted.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Encrypt: int
        :param _MaxDiskSize: Maximum disk
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxDiskSize: int
        """
        self._Spec = None
        self._NodeSize = None
        self._Core = None
        self._Memory = None
        self._Disk = None
        self._DiskType = None
        self._DiskDesc = None
        self._AttachCBSSpec = None
        self._SubProductType = None
        self._SpecCore = None
        self._SpecMemory = None
        self._DiskCount = None
        self._Encrypt = None
        self._MaxDiskSize = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def NodeSize(self):
        return self._NodeSize

    @NodeSize.setter
    def NodeSize(self, NodeSize):
        self._NodeSize = NodeSize

    @property
    def Core(self):
        return self._Core

    @Core.setter
    def Core(self, Core):
        self._Core = Core

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def AttachCBSSpec(self):
        return self._AttachCBSSpec

    @AttachCBSSpec.setter
    def AttachCBSSpec(self, AttachCBSSpec):
        self._AttachCBSSpec = AttachCBSSpec

    @property
    def SubProductType(self):
        return self._SubProductType

    @SubProductType.setter
    def SubProductType(self, SubProductType):
        self._SubProductType = SubProductType

    @property
    def SpecCore(self):
        return self._SpecCore

    @SpecCore.setter
    def SpecCore(self, SpecCore):
        self._SpecCore = SpecCore

    @property
    def SpecMemory(self):
        return self._SpecMemory

    @SpecMemory.setter
    def SpecMemory(self, SpecMemory):
        self._SpecMemory = SpecMemory

    @property
    def DiskCount(self):
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def MaxDiskSize(self):
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._NodeSize = params.get("NodeSize")
        self._Core = params.get("Core")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._DiskType = params.get("DiskType")
        self._DiskDesc = params.get("DiskDesc")
        if params.get("AttachCBSSpec") is not None:
            self._AttachCBSSpec = AttachCBSSpec()
            self._AttachCBSSpec._deserialize(params.get("AttachCBSSpec"))
        self._SubProductType = params.get("SubProductType")
        self._SpecCore = params.get("SpecCore")
        self._SpecMemory = params.get("SpecMemory")
        self._DiskCount = params.get("DiskCount")
        self._Encrypt = params.get("Encrypt")
        self._MaxDiskSize = params.get("MaxDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskRequest(AbstractModel):
    """ResizeDisk request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _Type: Role (MATER/CORE), MASTER corresponds to FE, CORE corresponds to BE.
        :type Type: str
        :param _DiskSize: Cloud disk size
        :type DiskSize: int
        """
        self._InstanceId = None
        self._Type = None
        self._DiskSize = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskResponse(AbstractModel):
    """ResizeDisk response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _FlowId: Process ID
        :type FlowId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class RestartClusterForNodeRequest(AbstractModel):
    """RestartClusterForNode request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID, such as cdwch-xxxx
        :type InstanceId: str
        :param _ConfigName: Configuration file's name
        :type ConfigName: str
        :param _BatchSize: Each batch of restarts
        :type BatchSize: int
        :param _NodeList: Restart node
        :type NodeList: list of str
        :param _RollingRestart: False means non-rolling restart, and true means rolling restart.
        :type RollingRestart: bool
        """
        self._InstanceId = None
        self._ConfigName = None
        self._BatchSize = None
        self._NodeList = None
        self._RollingRestart = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigName(self):
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def BatchSize(self):
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def RollingRestart(self):
        return self._RollingRestart

    @RollingRestart.setter
    def RollingRestart(self, RollingRestart):
        self._RollingRestart = RollingRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConfigName = params.get("ConfigName")
        self._BatchSize = params.get("BatchSize")
        self._NodeList = params.get("NodeList")
        self._RollingRestart = params.get("RollingRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterForNodeResponse(AbstractModel):
    """RestartClusterForNode response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process related information
        :type FlowId: int
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _Type: Role (MATER/CORE), MASTER corresponds to FE, CORE corresponds to BE.
        :type Type: str
        :param _NodeCount: Number of nodes
        :type NodeCount: int
        :param _HaType: Cluster high availability type after scaled out: 0 indicates non-high availability, 1 indicates read high availability, and 2 indicates read-write high availability.
        :type HaType: int
        """
        self._InstanceId = None
        self._Type = None
        self._NodeCount = None
        self._HaType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def HaType(self):
        return self._HaType

    @HaType.setter
    def HaType(self, HaType):
        self._HaType = HaType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._NodeCount = params.get("NodeCount")
        self._HaType = params.get("HaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID
        :type FlowId: str
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ScaleUpInstanceRequest(AbstractModel):
    """ScaleUpInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _SpecName: Node specifications
        :type SpecName: str
        :param _Type: Role (MATER/CORE). MASTER corresponds to FE, and CORE corresponds to BE.
        :type Type: str
        """
        self._InstanceId = None
        self._SpecName = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpecName = params.get("SpecName")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpInstanceResponse(AbstractModel):
    """ScaleUpInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID
        :type FlowId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ErrorMsg: Error message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class SearchTags(AbstractModel):
    """The searched marker list on the list page

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        :param _AllValue: 1 means only the tag key is entered without a value, and 0 means both the key and the value are entered.
        :type AllValue: int
        """
        self._TagKey = None
        self._TagValue = None
        self._AllValue = None

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

    @property
    def AllValue(self):
        return self._AllValue

    @AllValue.setter
    def AllValue(self, AllValue):
        self._AllValue = AllValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._AllValue = params.get("AllValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowQueryRecord(AbstractModel):
    """Slow log records

    """

    def __init__(self):
        r"""
        :param _OsUser: User query 
        :type OsUser: str
        :param _InitialQueryId: ID query
        :type InitialQueryId: str
        :param _Sql: SQL statement
        :type Sql: str
        :param _QueryStartTime: Start time
        :type QueryStartTime: str
        :param _DurationMs: Execution duration
        :type DurationMs: int
        :param _ReadRows: The number of read rows
        :type ReadRows: int
        :param _ResultRows: Total number of read bytes
        :type ResultRows: int
        :param _ResultBytes: Result bytes
        :type ResultBytes: int
        :param _MemoryUsage: Memory
        :type MemoryUsage: int
        :param _InitialAddress: Initial query IP
        :type InitialAddress: str
        :param _DbName: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _IsQuery: Whether it is a query. 0 indicates no, and 1 indicates query statement.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsQuery: int
        :param _ResultBytesMB: MB format of ResultBytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultBytesMB: float
        :param _MemoryUsageMB: MemoryUsage, in MB
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemoryUsageMB: float
        :param _DurationSec: DurationMs, in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type DurationSec: float
        """
        self._OsUser = None
        self._InitialQueryId = None
        self._Sql = None
        self._QueryStartTime = None
        self._DurationMs = None
        self._ReadRows = None
        self._ResultRows = None
        self._ResultBytes = None
        self._MemoryUsage = None
        self._InitialAddress = None
        self._DbName = None
        self._IsQuery = None
        self._ResultBytesMB = None
        self._MemoryUsageMB = None
        self._DurationSec = None

    @property
    def OsUser(self):
        return self._OsUser

    @OsUser.setter
    def OsUser(self, OsUser):
        self._OsUser = OsUser

    @property
    def InitialQueryId(self):
        return self._InitialQueryId

    @InitialQueryId.setter
    def InitialQueryId(self, InitialQueryId):
        self._InitialQueryId = InitialQueryId

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def QueryStartTime(self):
        return self._QueryStartTime

    @QueryStartTime.setter
    def QueryStartTime(self, QueryStartTime):
        self._QueryStartTime = QueryStartTime

    @property
    def DurationMs(self):
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def ReadRows(self):
        return self._ReadRows

    @ReadRows.setter
    def ReadRows(self, ReadRows):
        self._ReadRows = ReadRows

    @property
    def ResultRows(self):
        return self._ResultRows

    @ResultRows.setter
    def ResultRows(self, ResultRows):
        self._ResultRows = ResultRows

    @property
    def ResultBytes(self):
        return self._ResultBytes

    @ResultBytes.setter
    def ResultBytes(self, ResultBytes):
        self._ResultBytes = ResultBytes

    @property
    def MemoryUsage(self):
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def InitialAddress(self):
        return self._InitialAddress

    @InitialAddress.setter
    def InitialAddress(self, InitialAddress):
        self._InitialAddress = InitialAddress

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def IsQuery(self):
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def ResultBytesMB(self):
        return self._ResultBytesMB

    @ResultBytesMB.setter
    def ResultBytesMB(self, ResultBytesMB):
        self._ResultBytesMB = ResultBytesMB

    @property
    def MemoryUsageMB(self):
        return self._MemoryUsageMB

    @MemoryUsageMB.setter
    def MemoryUsageMB(self, MemoryUsageMB):
        self._MemoryUsageMB = MemoryUsageMB

    @property
    def DurationSec(self):
        return self._DurationSec

    @DurationSec.setter
    def DurationSec(self, DurationSec):
        self._DurationSec = DurationSec


    def _deserialize(self, params):
        self._OsUser = params.get("OsUser")
        self._InitialQueryId = params.get("InitialQueryId")
        self._Sql = params.get("Sql")
        self._QueryStartTime = params.get("QueryStartTime")
        self._DurationMs = params.get("DurationMs")
        self._ReadRows = params.get("ReadRows")
        self._ResultRows = params.get("ResultRows")
        self._ResultBytes = params.get("ResultBytes")
        self._MemoryUsage = params.get("MemoryUsage")
        self._InitialAddress = params.get("InitialAddress")
        self._DbName = params.get("DbName")
        self._IsQuery = params.get("IsQuery")
        self._ResultBytesMB = params.get("ResultBytesMB")
        self._MemoryUsageMB = params.get("MemoryUsageMB")
        self._DurationSec = params.get("DurationSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag description

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
        