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


class Ability(AbstractModel):
    """Features supported by the cluster

    """

    def __init__(self):
        r"""
        :param _IsSupportSlaveZone: Whether secondary AZ is supported
        :type IsSupportSlaveZone: str
        :param _NonsupportSlaveZoneReason: The reason why secondary AZ is not supported
Note: This field may return null, indicating that no valid values can be obtained.
        :type NonsupportSlaveZoneReason: str
        :param _IsSupportRo: Whether read-only instance is supported
        :type IsSupportRo: str
        :param _NonsupportRoReason: The reason why read-only instance is not supported
Note: This field may return null, indicating that no valid values can be obtained.
        :type NonsupportRoReason: str
        """
        self._IsSupportSlaveZone = None
        self._NonsupportSlaveZoneReason = None
        self._IsSupportRo = None
        self._NonsupportRoReason = None

    @property
    def IsSupportSlaveZone(self):
        return self._IsSupportSlaveZone

    @IsSupportSlaveZone.setter
    def IsSupportSlaveZone(self, IsSupportSlaveZone):
        self._IsSupportSlaveZone = IsSupportSlaveZone

    @property
    def NonsupportSlaveZoneReason(self):
        return self._NonsupportSlaveZoneReason

    @NonsupportSlaveZoneReason.setter
    def NonsupportSlaveZoneReason(self, NonsupportSlaveZoneReason):
        self._NonsupportSlaveZoneReason = NonsupportSlaveZoneReason

    @property
    def IsSupportRo(self):
        return self._IsSupportRo

    @IsSupportRo.setter
    def IsSupportRo(self, IsSupportRo):
        self._IsSupportRo = IsSupportRo

    @property
    def NonsupportRoReason(self):
        return self._NonsupportRoReason

    @NonsupportRoReason.setter
    def NonsupportRoReason(self, NonsupportRoReason):
        self._NonsupportRoReason = NonsupportRoReason


    def _deserialize(self, params):
        self._IsSupportSlaveZone = params.get("IsSupportSlaveZone")
        self._NonsupportSlaveZoneReason = params.get("NonsupportSlaveZoneReason")
        self._IsSupportRo = params.get("IsSupportRo")
        self._NonsupportRoReason = params.get("NonsupportRoReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Account(AbstractModel):
    """Database account information

    """

    def __init__(self):
        r"""
        :param _AccountName: Database account name
        :type AccountName: str
        :param _Description: Database account description
        :type Description: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Host: Host
        :type Host: str
        :param _MaxUserConnections: The max connections
        :type MaxUserConnections: int
        """
        self._AccountName = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Host = None
        self._MaxUserConnections = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Host = params.get("Host")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateInstanceRequest(AbstractModel):
    """ActivateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIdList: List of instance IDs in the format of `cynosdbmysql-ins-n7ocdslw` as displayed in the TDSQL-C for MySQL console. You can use the instance list querying API to query the ID, i.e., the `InstanceId` value in the output parameters.
        :type InstanceIdList: list of str
        """
        self._ClusterId = None
        self._InstanceIdList = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateInstanceResponse(AbstractModel):
    """ActivateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class AddClusterSlaveZoneRequest(AbstractModel):
    """AddClusterSlaveZone request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _SlaveZone: Replica AZ
        :type SlaveZone: str
        """
        self._ClusterId = None
        self._SlaveZone = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddClusterSlaveZoneResponse(AbstractModel):
    """AddClusterSlaveZone response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async FlowId
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class AddInstancesRequest(AbstractModel):
    """AddInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Memory: Memory in GB
        :type Memory: int
        :param _ReadOnlyCount: Number of added read-only instances. Value range: (0,16].
        :type ReadOnlyCount: int
        :param _InstanceGrpId: Instance group ID, which will be used when you add an instance in an existing RO group. If this parameter is left empty, an RO group will be created. But it is not recommended to pass in this parameter for the current version, as this version has been disused.
        :type InstanceGrpId: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID. If `VpcId` is set, `SubnetId` is required.
        :type SubnetId: str
        :param _Port: The port used when adding an RO group. Value range: [0,65535).
        :type Port: int
        :param _InstanceName: Instance name. String length range: [0,64).
        :type InstanceName: str
        :param _AutoVoucher: Whether to automatically select a voucher. 1: yes; 0: no. Default value: 0
        :type AutoVoucher: int
        :param _DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        :param _OrderSource: Order source. String length range: [0,64).
        :type OrderSource: str
        :param _DealMode: Transaction mode. Valid values: `0` (place and pay for an order), `1` (place an order)
        :type DealMode: int
        :param _ParamTemplateId: Parameter template ID
        :type ParamTemplateId: int
        :param _InstanceParams: Parameter list, which is valid only if `InstanceParams` is passed in to `ParamTemplateId`.
        :type InstanceParams: list of ModifyParamItem
        :param _SecurityGroupIds: Security group ID. You can specify an security group when creating a read-only instance.
        :type SecurityGroupIds: list of str
        """
        self._ClusterId = None
        self._Cpu = None
        self._Memory = None
        self._ReadOnlyCount = None
        self._InstanceGrpId = None
        self._VpcId = None
        self._SubnetId = None
        self._Port = None
        self._InstanceName = None
        self._AutoVoucher = None
        self._DbType = None
        self._OrderSource = None
        self._DealMode = None
        self._ParamTemplateId = None
        self._InstanceParams = None
        self._SecurityGroupIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def ReadOnlyCount(self):
        return self._ReadOnlyCount

    @ReadOnlyCount.setter
    def ReadOnlyCount(self, ReadOnlyCount):
        self._ReadOnlyCount = ReadOnlyCount

    @property
    def InstanceGrpId(self):
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        self._InstanceGrpId = InstanceGrpId

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def OrderSource(self):
        return self._OrderSource

    @OrderSource.setter
    def OrderSource(self, OrderSource):
        self._OrderSource = OrderSource

    @property
    def DealMode(self):
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def ParamTemplateId(self):
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def InstanceParams(self):
        return self._InstanceParams

    @InstanceParams.setter
    def InstanceParams(self, InstanceParams):
        self._InstanceParams = InstanceParams

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._ReadOnlyCount = params.get("ReadOnlyCount")
        self._InstanceGrpId = params.get("InstanceGrpId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Port = params.get("Port")
        self._InstanceName = params.get("InstanceName")
        self._AutoVoucher = params.get("AutoVoucher")
        self._DbType = params.get("DbType")
        self._OrderSource = params.get("OrderSource")
        self._DealMode = params.get("DealMode")
        self._ParamTemplateId = params.get("ParamTemplateId")
        if params.get("InstanceParams") is not None:
            self._InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._InstanceParams.append(obj)
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddInstancesResponse(AbstractModel):
    """AddInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TranId: Freezing transaction. One freezing transaction ID is generated each time an instance is added.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param _DealNames: Pay-as-You-Go order ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param _ResourceIds: List of IDs of delivered resources
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceIds: list of str
        :param _BigDealIds: Big order ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BigDealIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TranId = None
        self._DealNames = None
        self._ResourceIds = None
        self._BigDealIds = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._DealNames = params.get("DealNames")
        self._ResourceIds = params.get("ResourceIds")
        self._BigDealIds = params.get("BigDealIds")
        self._RequestId = params.get("RequestId")


class Addr(AbstractModel):
    """Database address

    """

    def __init__(self):
        r"""
        :param _IP: IP address
        :type IP: str
        :param _Port: Port
        :type Port: int
        """
        self._IP = None
        self._Port = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRuleFilters(AbstractModel):
    """Filter of rule audit

    """

    def __init__(self):
        r"""
        :param _RuleFilters: Audit rule
        :type RuleFilters: list of RuleFilters
        """
        self._RuleFilters = None

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters


    def _deserialize(self, params):
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRuleTemplateInfo(AbstractModel):
    """Details of an audit rule template

    """

    def __init__(self):
        r"""
        :param _RuleTemplateId: Rule template ID
        :type RuleTemplateId: str
        :param _RuleTemplateName: Rule template name
        :type RuleTemplateName: str
        :param _RuleFilters: Filter of the rule template
        :type RuleFilters: list of RuleFilters
        :param _Description: Description of a rule template
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _CreateAt: Creation time of a rule template
        :type CreateAt: str
        """
        self._RuleTemplateId = None
        self._RuleTemplateName = None
        self._RuleFilters = None
        self._Description = None
        self._CreateAt = None

    @property
    def RuleTemplateId(self):
        return self._RuleTemplateId

    @RuleTemplateId.setter
    def RuleTemplateId(self, RuleTemplateId):
        self._RuleTemplateId = RuleTemplateId

    @property
    def RuleTemplateName(self):
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt


    def _deserialize(self, params):
        self._RuleTemplateId = params.get("RuleTemplateId")
        self._RuleTemplateName = params.get("RuleTemplateName")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._Description = params.get("Description")
        self._CreateAt = params.get("CreateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFileInfo(AbstractModel):
    """Backup file information

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot file ID, which is deprecated. You need to use `BackupId`.
        :type SnapshotId: int
        :param _FileName: Backup file name
        :type FileName: str
        :param _FileSize: Backup file size
        :type FileSize: int
        :param _StartTime: Backup start time
        :type StartTime: str
        :param _FinishTime: Backup end time
        :type FinishTime: str
        :param _BackupType: Backup type. Valid values: `snapshot` (snapshot backup), `logic` (logic backup).
        :type BackupType: str
        :param _BackupMethod: Back mode. auto: auto backup; manual: manual backup
        :type BackupMethod: str
        :param _BackupStatus: Backup file status. success: backup succeeded; fail: backup failed; creating: creating backup file; deleting: deleting backup file
        :type BackupStatus: str
        :param _SnapshotTime: Backup file time
        :type SnapshotTime: str
        :param _BackupId: Backup ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupId: int
        :param _SnapShotType: 
        :type SnapShotType: str
        :param _BackupName: Backup file alias
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupName: str
        """
        self._SnapshotId = None
        self._FileName = None
        self._FileSize = None
        self._StartTime = None
        self._FinishTime = None
        self._BackupType = None
        self._BackupMethod = None
        self._BackupStatus = None
        self._SnapshotTime = None
        self._BackupId = None
        self._SnapShotType = None
        self._BackupName = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupStatus(self):
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def SnapshotTime(self):
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def SnapShotType(self):
        return self._SnapShotType

    @SnapShotType.setter
    def SnapShotType(self, SnapShotType):
        self._SnapShotType = SnapShotType

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._BackupType = params.get("BackupType")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupStatus = params.get("BackupStatus")
        self._SnapshotTime = params.get("SnapshotTime")
        self._BackupId = params.get("BackupId")
        self._SnapShotType = params.get("SnapShotType")
        self._BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingResourceInfo(AbstractModel):
    """Billable resource information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIds: Instance ID list
        :type InstanceIds: list of str
        :param _DealName: Order ID
        :type DealName: str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._DealName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindClusterResourcePackagesRequest(AbstractModel):
    """BindClusterResourcePackages request structure.

    """

    def __init__(self):
        r"""
        :param _PackageIds: The unique ID of a resource pack
        :type PackageIds: list of str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._PackageIds = None
        self._ClusterId = None

    @property
    def PackageIds(self):
        return self._PackageIds

    @PackageIds.setter
    def PackageIds(self, PackageIds):
        self._PackageIds = PackageIds

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._PackageIds = params.get("PackageIds")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindClusterResourcePackagesResponse(AbstractModel):
    """BindClusterResourcePackages response structure.

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


class BindInstanceInfo(AbstractModel):
    """Information of the instance bound to the resource pack

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the bound cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceRegion: Region of the instance bound Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceRegion: str
        :param _InstanceType: Type of the instance bound Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _ExtendIds: ID of the instance in the bound cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtendIds: list of str
        """
        self._InstanceId = None
        self._InstanceRegion = None
        self._InstanceType = None
        self._ExtendIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRegion(self):
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ExtendIds(self):
        return self._ExtendIds

    @ExtendIds.setter
    def ExtendIds(self, ExtendIds):
        self._ExtendIds = ExtendIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceRegion = params.get("InstanceRegion")
        self._InstanceType = params.get("InstanceType")
        self._ExtendIds = params.get("ExtendIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogItem(AbstractModel):
    """Binlog description

    """

    def __init__(self):
        r"""
        :param _FileName: Binlog filename
        :type FileName: str
        :param _FileSize: File size in bytes
        :type FileSize: int
        :param _StartTime: Transaction start time
        :type StartTime: str
        :param _FinishTime: Transaction end time
        :type FinishTime: str
        :param _BinlogId: Binlog file ID
        :type BinlogId: int
        """
        self._FileName = None
        self._FileSize = None
        self._StartTime = None
        self._FinishTime = None
        self._BinlogId = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def BinlogId(self):
        return self._BinlogId

    @BinlogId.setter
    def BinlogId(self, BinlogId):
        self._BinlogId = BinlogId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._BinlogId = params.get("BinlogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseAuditServiceRequest(AbstractModel):
    """CloseAuditService request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
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
        


class CloseAuditServiceResponse(AbstractModel):
    """CloseAuditService response structure.

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


class CloseClusterPasswordComplexityRequest(AbstractModel):
    """CloseClusterPasswordComplexity request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: Cluster IDs in array
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
        


class CloseClusterPasswordComplexityResponse(AbstractModel):
    """CloseClusterPasswordComplexity response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloseProxyRequest(AbstractModel):
    """CloseProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        :param _OnlyCloseRW: Whether only to disable read/write separation. Valid values: `true`, `false`.
        :type OnlyCloseRW: bool
        """
        self._ClusterId = None
        self._ProxyGroupId = None
        self._OnlyCloseRW = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def OnlyCloseRW(self):
        return self._OnlyCloseRW

    @OnlyCloseRW.setter
    def OnlyCloseRW(self, OnlyCloseRW):
        self._OnlyCloseRW = OnlyCloseRW


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._OnlyCloseRW = params.get("OnlyCloseRW")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProxyResponse(AbstractModel):
    """CloseProxy response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async flow ID
        :type FlowId: int
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CloseWanRequest(AbstractModel):
    """CloseWan request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceGrpId: Instance group ID
        :type InstanceGrpId: str
        """
        self._InstanceGrpId = None

    @property
    def InstanceGrpId(self):
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        self._InstanceGrpId = InstanceGrpId


    def _deserialize(self, params):
        self._InstanceGrpId = params.get("InstanceGrpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWanResponse(AbstractModel):
    """CloseWan response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ClusterInstanceDetail(AbstractModel):
    """Cluster instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceType: Engine type
        :type InstanceType: str
        :param _InstanceStatus: Instance status
        :type InstanceStatus: str
        :param _InstanceStatusDesc: Instance status description
        :type InstanceStatusDesc: str
        :param _InstanceCpu: Number of CPU cores
        :type InstanceCpu: int
        :param _InstanceMemory: Memory
        :type InstanceMemory: int
        :param _InstanceStorage: Disk
        :type InstanceStorage: int
        :param _InstanceRole: Instance role
        :type InstanceRole: str
        :param _MaintainStartTime: Execution start time in seconds from 0:00	
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaintainStartTime: int
        :param _MaintainDuration: Duration in seconds	
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaintainDuration: int
        :param _MaintainWeekDays: Execution time. Valid values: `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, Sat`, `Sun`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaintainWeekDays: list of str
        :param _ServerlessStatus: Serverless instance enablement status
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServerlessStatus: str
        :param _InstanceTasks: 
        :type InstanceTasks: list of ObjectTask
        :param _InstanceDeviceType: 
        :type InstanceDeviceType: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._InstanceStatus = None
        self._InstanceStatusDesc = None
        self._InstanceCpu = None
        self._InstanceMemory = None
        self._InstanceStorage = None
        self._InstanceRole = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._MaintainWeekDays = None
        self._ServerlessStatus = None
        self._InstanceTasks = None
        self._InstanceDeviceType = None

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
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def InstanceStatusDesc(self):
        return self._InstanceStatusDesc

    @InstanceStatusDesc.setter
    def InstanceStatusDesc(self, InstanceStatusDesc):
        self._InstanceStatusDesc = InstanceStatusDesc

    @property
    def InstanceCpu(self):
        return self._InstanceCpu

    @InstanceCpu.setter
    def InstanceCpu(self, InstanceCpu):
        self._InstanceCpu = InstanceCpu

    @property
    def InstanceMemory(self):
        return self._InstanceMemory

    @InstanceMemory.setter
    def InstanceMemory(self, InstanceMemory):
        self._InstanceMemory = InstanceMemory

    @property
    def InstanceStorage(self):
        return self._InstanceStorage

    @InstanceStorage.setter
    def InstanceStorage(self, InstanceStorage):
        self._InstanceStorage = InstanceStorage

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def MaintainStartTime(self):
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def InstanceTasks(self):
        return self._InstanceTasks

    @InstanceTasks.setter
    def InstanceTasks(self, InstanceTasks):
        self._InstanceTasks = InstanceTasks

    @property
    def InstanceDeviceType(self):
        return self._InstanceDeviceType

    @InstanceDeviceType.setter
    def InstanceDeviceType(self, InstanceDeviceType):
        self._InstanceDeviceType = InstanceDeviceType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatus = params.get("InstanceStatus")
        self._InstanceStatusDesc = params.get("InstanceStatusDesc")
        self._InstanceCpu = params.get("InstanceCpu")
        self._InstanceMemory = params.get("InstanceMemory")
        self._InstanceStorage = params.get("InstanceStorage")
        self._InstanceRole = params.get("InstanceRole")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        self._ServerlessStatus = params.get("ServerlessStatus")
        if params.get("InstanceTasks") is not None:
            self._InstanceTasks = []
            for item in params.get("InstanceTasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._InstanceTasks.append(obj)
        self._InstanceDeviceType = params.get("InstanceDeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyClusterPasswordComplexityRequest(AbstractModel):
    """CopyClusterPasswordComplexity request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: A parameter used to replicate the array of cluster IDs
        :type ClusterIds: list of str
        :param _SourceClusterId: Cluster ID
        :type SourceClusterId: str
        """
        self._ClusterIds = None
        self._SourceClusterId = None

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def SourceClusterId(self):
        return self._SourceClusterId

    @SourceClusterId.setter
    def SourceClusterId(self, SourceClusterId):
        self._SourceClusterId = SourceClusterId


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._SourceClusterId = params.get("SourceClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyClusterPasswordComplexityResponse(AbstractModel):
    """CopyClusterPasswordComplexity response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateAccountsRequest(AbstractModel):
    """CreateAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Accounts: List of new accounts
        :type Accounts: list of NewAccount
        """
        self._ClusterId = None
        self._Accounts = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = NewAccount()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsResponse(AbstractModel):
    """CreateAccounts response structure.

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


class CreateAuditRuleTemplateRequest(AbstractModel):
    """CreateAuditRuleTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _RuleFilters: Audit rule
        :type RuleFilters: list of RuleFilters
        :param _RuleTemplateName: Rule template name
        :type RuleTemplateName: str
        :param _Description: Rule template description.
        :type Description: str
        """
        self._RuleFilters = None
        self._RuleTemplateName = None
        self._Description = None

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def RuleTemplateName(self):
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._RuleTemplateName = params.get("RuleTemplateName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditRuleTemplateResponse(AbstractModel):
    """CreateAuditRuleTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RuleTemplateId: The generated rule template ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleTemplateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleTemplateId = None
        self._RequestId = None

    @property
    def RuleTemplateId(self):
        return self._RuleTemplateId

    @RuleTemplateId.setter
    def RuleTemplateId(self, RuleTemplateId):
        self._RuleTemplateId = RuleTemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleTemplateId = params.get("RuleTemplateId")
        self._RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _BackupType: Backup type. Valid values: `logic` (logic backup), `snapshot` (physical backup)
        :type BackupType: str
        :param _BackupDatabases: Backup database, which is valid when `BackupType` is `logic`.
        :type BackupDatabases: list of str
        :param _BackupTables: Backup table, which is valid when `BackupType` is `logic`.
        :type BackupTables: list of DatabaseTables
        :param _BackupName: Backup name
        :type BackupName: str
        """
        self._ClusterId = None
        self._BackupType = None
        self._BackupDatabases = None
        self._BackupTables = None
        self._BackupName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupDatabases(self):
        return self._BackupDatabases

    @BackupDatabases.setter
    def BackupDatabases(self, BackupDatabases):
        self._BackupDatabases = BackupDatabases

    @property
    def BackupTables(self):
        return self._BackupTables

    @BackupTables.setter
    def BackupTables(self, BackupTables):
        self._BackupTables = BackupTables

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupType = params.get("BackupType")
        self._BackupDatabases = params.get("BackupDatabases")
        if params.get("BackupTables") is not None:
            self._BackupTables = []
            for item in params.get("BackupTables"):
                obj = DatabaseTables()
                obj._deserialize(item)
                self._BackupTables.append(obj)
        self._BackupName = params.get("BackupName")
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
        :param _FlowId: Async task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateClusterDatabaseRequest(AbstractModel):
    """CreateClusterDatabase request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _DbName: Database name
        :type DbName: str
        :param _CharacterSet: Character set
        :type CharacterSet: str
        :param _CollateRule: Collation
        :type CollateRule: str
        :param _UserHostPrivileges: Host permissions of the authorized user
        :type UserHostPrivileges: list of UserHostPrivilege
        :param _Description: Remarks
        :type Description: str
        """
        self._ClusterId = None
        self._DbName = None
        self._CharacterSet = None
        self._CollateRule = None
        self._UserHostPrivileges = None
        self._Description = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CharacterSet(self):
        return self._CharacterSet

    @CharacterSet.setter
    def CharacterSet(self, CharacterSet):
        self._CharacterSet = CharacterSet

    @property
    def CollateRule(self):
        return self._CollateRule

    @CollateRule.setter
    def CollateRule(self, CollateRule):
        self._CollateRule = CollateRule

    @property
    def UserHostPrivileges(self):
        return self._UserHostPrivileges

    @UserHostPrivileges.setter
    def UserHostPrivileges(self, UserHostPrivileges):
        self._UserHostPrivileges = UserHostPrivileges

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DbName = params.get("DbName")
        self._CharacterSet = params.get("CharacterSet")
        self._CollateRule = params.get("CollateRule")
        if params.get("UserHostPrivileges") is not None:
            self._UserHostPrivileges = []
            for item in params.get("UserHostPrivileges"):
                obj = UserHostPrivilege()
                obj._deserialize(item)
                self._UserHostPrivileges.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterDatabaseResponse(AbstractModel):
    """CreateClusterDatabase response structure.

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


class CreateClustersRequest(AbstractModel):
    """CreateClusters request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ
        :type Zone: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        :param _DbVersion: Database version. Valid values: 
<li> Valid values for `MYSQL`: 5.7 and 8.0 </li>
        :type DbVersion: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _Cpu: It is required when `DbMode` is set to `NORMAL` or left empty.
Number of CPU cores of normal instance
        :type Cpu: int
        :param _Memory: It is required when `DbMode` is set to `NORMAL` or left empty.
Memory of a non-serverless instance in GB
        :type Memory: int
        :param _Storage: This parameter has been deprecated.
Storage capacity in GB
        :type Storage: int
        :param _ClusterName: Cluster name, which can contain less than 64 letters, digits, or symbols (-_.).
        :type ClusterName: str
        :param _AdminPassword: Account password, which must contain 8-64 characters in at least three of the following four types: uppercase letters, lowercase letters, digits, and symbols (~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/).
        :type AdminPassword: str
        :param _Port: Port. Valid range: [0, 65535). Default value: 3306
        :type Port: int
        :param _PayMode: Billing mode. `0`: pay-as-you-go; `1`: monthly subscription. Default value: `0`
        :type PayMode: int
        :param _Count: Number of purchased clusters. Valid range: [1,50]. Default value: 1
        :type Count: int
        :param _RollbackStrategy: Rollback type:
noneRollback: no rollback;
snapRollback: rollback by snapshot;
timeRollback: rollback by time point
        :type RollbackStrategy: str
        :param _RollbackId: `snapshotId` for snapshot rollback or `queryId` for time point rollback. 0 indicates to determine whether the time point is valid
        :type RollbackId: int
        :param _OriginalClusterId: The source cluster ID passed in during rollback to find the source `poolId`
        :type OriginalClusterId: str
        :param _ExpectTime: Specified time for time point rollback or snapshot time for snapshot rollback
        :type ExpectTime: str
        :param _ExpectTimeThresh: This parameter has been deprecated.
Specified allowed time range for time point rollback
        :type ExpectTimeThresh: int
        :param _StorageLimit: Storage upper limit of normal instance in GB
If `DbType` is `MYSQL` and the storage billing mode is monthly subscription, the parameter value can’t exceed the maximum storage corresponding to the CPU and memory specifications.
        :type StorageLimit: int
        :param _InstanceCount: Number of Instances. Valid range: (0,16]
        :type InstanceCount: int
        :param _TimeSpan: Purchase duration of monthly subscription plan
        :type TimeSpan: int
        :param _TimeUnit: Duration unit of monthly subscription. Valid values: `s`, `d`, `m`, `y`
        :type TimeUnit: str
        :param _AutoRenewFlag: Whether auto-renewal is enabled for monthly subscription plan. Default value: `0`
        :type AutoRenewFlag: int
        :param _AutoVoucher: Whether to automatically select a voucher. `1`: yes; `0`: no. Default value: `0`
        :type AutoVoucher: int
        :param _HaCount: Number of instances (this parameter has been disused and is retained only for compatibility with existing instances)
        :type HaCount: int
        :param _OrderSource: Order source
        :type OrderSource: str
        :param _ResourceTags: Array of tags to be bound to the created cluster
        :type ResourceTags: list of Tag
        :param _DbMode: Database type
Valid values when `DbType` is `MYSQL` (default value: `NORMAL`):
<li>NORMAL</li>
<li>SERVERLESS</li>
        :type DbMode: str
        :param _MinCpu: This parameter is required if `DbMode` is `SERVERLESS`.
Minimum number of CPU cores. For the value range, see the returned result of `DescribeServerlessInstanceSpecs`.
        :type MinCpu: float
        :param _MaxCpu: This parameter is required if `DbMode` is `SERVERLESS`.
Maximum number of CPU cores. For the value range, see the returned result of `DescribeServerlessInstanceSpecs`.
        :type MaxCpu: float
        :param _AutoPause: This parameter specifies whether the cluster will be automatically paused if `DbMode` is `SERVERLESS`. Valid values:
<li>yes</li>
<li>no</li>
Default value: yes
        :type AutoPause: str
        :param _AutoPauseDelay: This parameter specifies the delay for automatic cluster pause in seconds if `DbMode` is `SERVERLESS`. Value range: [600,691200]
Default value: `600`
        :type AutoPauseDelay: int
        :param _StoragePayMode: The billing mode of cluster storage. Valid values: `0` (pay-as-you-go), `1` (monthly subscription). Default value: `0`.
If `DbType` is `MYSQL` and the billing mode of cluster compute is pay-as-you-go (or the `DbMode` is `SERVERLESS`), the billing mode of cluster storage must be pay-as-you-go.
Clusters with storage billed in monthly subscription can’t be cloned or rolled back.
        :type StoragePayMode: int
        :param _SecurityGroupIds: Array of security group IDs
        :type SecurityGroupIds: list of str
        :param _AlarmPolicyIds: Array of alarm policy IDs
        :type AlarmPolicyIds: list of str
        :param _ClusterParams: Array of parameters. Valid values: `character_set_server` (utf8｜latin1｜gbk｜utf8mb4), `lower_case_table_names`. 0: case-sensitive; 1: case-insensitive).
        :type ClusterParams: list of ParamItem
        :param _DealMode: Transaction mode. Valid values: `0` (place and pay for an order), `1` (place an order)
        :type DealMode: int
        :param _ParamTemplateId: Parameter template ID, which can be obtained by querying parameter template information “DescribeParamTemplates”
        :type ParamTemplateId: int
        :param _SlaveZone: Multi-AZ address
        :type SlaveZone: str
        :param _InstanceInitInfos: Instance initialization configuration information, which is used to select instances with different specifications when purchasing a cluster.
        :type InstanceInitInfos: list of InstanceInitInfo
        """
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._DbType = None
        self._DbVersion = None
        self._ProjectId = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._ClusterName = None
        self._AdminPassword = None
        self._Port = None
        self._PayMode = None
        self._Count = None
        self._RollbackStrategy = None
        self._RollbackId = None
        self._OriginalClusterId = None
        self._ExpectTime = None
        self._ExpectTimeThresh = None
        self._StorageLimit = None
        self._InstanceCount = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None
        self._HaCount = None
        self._OrderSource = None
        self._ResourceTags = None
        self._DbMode = None
        self._MinCpu = None
        self._MaxCpu = None
        self._AutoPause = None
        self._AutoPauseDelay = None
        self._StoragePayMode = None
        self._SecurityGroupIds = None
        self._AlarmPolicyIds = None
        self._ClusterParams = None
        self._DealMode = None
        self._ParamTemplateId = None
        self._SlaveZone = None
        self._InstanceInitInfos = None

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
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def AdminPassword(self):
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RollbackStrategy(self):
        return self._RollbackStrategy

    @RollbackStrategy.setter
    def RollbackStrategy(self, RollbackStrategy):
        self._RollbackStrategy = RollbackStrategy

    @property
    def RollbackId(self):
        return self._RollbackId

    @RollbackId.setter
    def RollbackId(self, RollbackId):
        self._RollbackId = RollbackId

    @property
    def OriginalClusterId(self):
        return self._OriginalClusterId

    @OriginalClusterId.setter
    def OriginalClusterId(self, OriginalClusterId):
        self._OriginalClusterId = OriginalClusterId

    @property
    def ExpectTime(self):
        return self._ExpectTime

    @ExpectTime.setter
    def ExpectTime(self, ExpectTime):
        self._ExpectTime = ExpectTime

    @property
    def ExpectTimeThresh(self):
        return self._ExpectTimeThresh

    @ExpectTimeThresh.setter
    def ExpectTimeThresh(self, ExpectTimeThresh):
        self._ExpectTimeThresh = ExpectTimeThresh

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

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

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def HaCount(self):
        return self._HaCount

    @HaCount.setter
    def HaCount(self, HaCount):
        self._HaCount = HaCount

    @property
    def OrderSource(self):
        return self._OrderSource

    @OrderSource.setter
    def OrderSource(self, OrderSource):
        self._OrderSource = OrderSource

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def MinCpu(self):
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def AutoPause(self):
        return self._AutoPause

    @AutoPause.setter
    def AutoPause(self, AutoPause):
        self._AutoPause = AutoPause

    @property
    def AutoPauseDelay(self):
        return self._AutoPauseDelay

    @AutoPauseDelay.setter
    def AutoPauseDelay(self, AutoPauseDelay):
        self._AutoPauseDelay = AutoPauseDelay

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AlarmPolicyIds(self):
        return self._AlarmPolicyIds

    @AlarmPolicyIds.setter
    def AlarmPolicyIds(self, AlarmPolicyIds):
        self._AlarmPolicyIds = AlarmPolicyIds

    @property
    def ClusterParams(self):
        return self._ClusterParams

    @ClusterParams.setter
    def ClusterParams(self, ClusterParams):
        self._ClusterParams = ClusterParams

    @property
    def DealMode(self):
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def ParamTemplateId(self):
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def InstanceInitInfos(self):
        return self._InstanceInitInfos

    @InstanceInitInfos.setter
    def InstanceInitInfos(self, InstanceInitInfos):
        self._InstanceInitInfos = InstanceInitInfos


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DbType = params.get("DbType")
        self._DbVersion = params.get("DbVersion")
        self._ProjectId = params.get("ProjectId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._ClusterName = params.get("ClusterName")
        self._AdminPassword = params.get("AdminPassword")
        self._Port = params.get("Port")
        self._PayMode = params.get("PayMode")
        self._Count = params.get("Count")
        self._RollbackStrategy = params.get("RollbackStrategy")
        self._RollbackId = params.get("RollbackId")
        self._OriginalClusterId = params.get("OriginalClusterId")
        self._ExpectTime = params.get("ExpectTime")
        self._ExpectTimeThresh = params.get("ExpectTimeThresh")
        self._StorageLimit = params.get("StorageLimit")
        self._InstanceCount = params.get("InstanceCount")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        self._HaCount = params.get("HaCount")
        self._OrderSource = params.get("OrderSource")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DbMode = params.get("DbMode")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._AutoPause = params.get("AutoPause")
        self._AutoPauseDelay = params.get("AutoPauseDelay")
        self._StoragePayMode = params.get("StoragePayMode")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._AlarmPolicyIds = params.get("AlarmPolicyIds")
        if params.get("ClusterParams") is not None:
            self._ClusterParams = []
            for item in params.get("ClusterParams"):
                obj = ParamItem()
                obj._deserialize(item)
                self._ClusterParams.append(obj)
        self._DealMode = params.get("DealMode")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._SlaveZone = params.get("SlaveZone")
        if params.get("InstanceInitInfos") is not None:
            self._InstanceInitInfos = []
            for item in params.get("InstanceInitInfos"):
                obj = InstanceInitInfo()
                obj._deserialize(item)
                self._InstanceInitInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClustersResponse(AbstractModel):
    """CreateClusters response structure.

    """

    def __init__(self):
        r"""
        :param _TranId: Freezing transaction ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param _DealNames: Order ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param _ResourceIds: List of resource IDs (This field has been deprecated. You need to use `dealNames` in the `DescribeResourcesByDealName` API to get resource IDs.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceIds: list of str
        :param _ClusterIds: List of cluster IDs (This field has been deprecated. You need to use `dealNames` in the `DescribeResourcesByDealName` API to get cluster IDs.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterIds: list of str
        :param _BigDealIds: Big order ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BigDealIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TranId = None
        self._DealNames = None
        self._ResourceIds = None
        self._ClusterIds = None
        self._BigDealIds = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._DealNames = params.get("DealNames")
        self._ResourceIds = params.get("ResourceIds")
        self._ClusterIds = params.get("ClusterIds")
        self._BigDealIds = params.get("BigDealIds")
        self._RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateName: Template name
        :type TemplateName: str
        :param _EngineVersion: MySQL version number
        :type EngineVersion: str
        :param _TemplateDescription: Template description
        :type TemplateDescription: str
        :param _TemplateId: ID of the template to be copied
        :type TemplateId: int
        :param _DbMode: Database type. Valid values:  `NORMAL` (default), `SERVERLESS`.
        :type DbMode: str
        :param _ParamList: List of the parameters
        :type ParamList: list of ParamItem
        """
        self._TemplateName = None
        self._EngineVersion = None
        self._TemplateDescription = None
        self._TemplateId = None
        self._DbMode = None
        self._ParamList = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TemplateDescription(self):
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._EngineVersion = params.get("EngineVersion")
        self._TemplateDescription = params.get("TemplateDescription")
        self._TemplateId = params.get("TemplateId")
        self._DbMode = params.get("DbMode")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamItem()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParamTemplateResponse(AbstractModel):
    """CreateParamTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID
        :type TemplateId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateProxyEndPointRequest(AbstractModel):
    """CreateProxyEndPoint request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _UniqueVpcId: VPC ID, which is the same as that of the cluster by default.
        :type UniqueVpcId: str
        :param _UniqueSubnetId: VPCe subnet ID, which is the same as that of the cluster by default.
        :type UniqueSubnetId: str
        :param _ConnectionPoolType: Connection pool type. Valid value: `SessionConnectionPool` (session-level connection pool)
        :type ConnectionPoolType: str
        :param _OpenConnectionPool: Whether to enable connection pool. Valid value: `yes` (enable), `no` (disable).
        :type OpenConnectionPool: str
        :param _ConnectionPoolTimeOut: Connection pool threshold in seconds
        :type ConnectionPoolTimeOut: int
        :param _SecurityGroupIds: Array of security group IDs
        :type SecurityGroupIds: list of str
        :param _Description: Description
        :type Description: str
        :param _Vip: VIP information
        :type Vip: str
        :param _WeightMode: Weight mode. 
Valid values: `system` (system-assigned), `custom` (custom).
        :type WeightMode: str
        :param _AutoAddRo: Whether to automatically add read-only instance. Valid value: `yes`, `no`.
        :type AutoAddRo: str
        :param _FailOver: Whether to enable failover
        :type FailOver: str
        :param _ConsistencyType: Consistency type. Valid values: 
`eventual`, `global`, `session`.
        :type ConsistencyType: str
        :param _RwType: Read-write attribute. Valid values: 
`READWRITE`, `READONLY`.
        :type RwType: str
        :param _ConsistencyTimeOut: Consistency timeout period
        :type ConsistencyTimeOut: int
        :param _TransSplit: Transaction split
        :type TransSplit: bool
        :param _AccessMode: Connection mode. Valid values:
`nearby`, `balance`.
        :type AccessMode: str
        :param _InstanceWeights: Instance weight
        :type InstanceWeights: list of ProxyInstanceWeight
        """
        self._ClusterId = None
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._ConnectionPoolType = None
        self._OpenConnectionPool = None
        self._ConnectionPoolTimeOut = None
        self._SecurityGroupIds = None
        self._Description = None
        self._Vip = None
        self._WeightMode = None
        self._AutoAddRo = None
        self._FailOver = None
        self._ConsistencyType = None
        self._RwType = None
        self._ConsistencyTimeOut = None
        self._TransSplit = None
        self._AccessMode = None
        self._InstanceWeights = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def UniqueVpcId(self):
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def OpenConnectionPool(self):
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolTimeOut(self):
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def ConsistencyType(self):
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def RwType(self):
        return self._RwType

    @RwType.setter
    def RwType(self, RwType):
        self._RwType = RwType

    @property
    def ConsistencyTimeOut(self):
        return self._ConsistencyTimeOut

    @ConsistencyTimeOut.setter
    def ConsistencyTimeOut(self, ConsistencyTimeOut):
        self._ConsistencyTimeOut = ConsistencyTimeOut

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def AccessMode(self):
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def InstanceWeights(self):
        return self._InstanceWeights

    @InstanceWeights.setter
    def InstanceWeights(self, InstanceWeights):
        self._InstanceWeights = InstanceWeights


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        self._OpenConnectionPool = params.get("OpenConnectionPool")
        self._ConnectionPoolTimeOut = params.get("ConnectionPoolTimeOut")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Description = params.get("Description")
        self._Vip = params.get("Vip")
        self._WeightMode = params.get("WeightMode")
        self._AutoAddRo = params.get("AutoAddRo")
        self._FailOver = params.get("FailOver")
        self._ConsistencyType = params.get("ConsistencyType")
        self._RwType = params.get("RwType")
        self._ConsistencyTimeOut = params.get("ConsistencyTimeOut")
        self._TransSplit = params.get("TransSplit")
        self._AccessMode = params.get("AccessMode")
        if params.get("InstanceWeights") is not None:
            self._InstanceWeights = []
            for item in params.get("InstanceWeights"):
                obj = ProxyInstanceWeight()
                obj._deserialize(item)
                self._InstanceWeights.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyEndPointResponse(AbstractModel):
    """CreateProxyEndPoint response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async flow ID
        :type FlowId: int
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._ProxyGroupId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._RequestId = params.get("RequestId")


class CreateProxyRequest(AbstractModel):
    """CreateProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Mem: Memory
        :type Mem: int
        :param _UniqueVpcId: VPC ID, which is the same as that of the cluster by default.
        :type UniqueVpcId: str
        :param _UniqueSubnetId: VPC subnet ID, which is the same as that of the cluster by default.
        :type UniqueSubnetId: str
        :param _ProxyCount: Number of nodes in the proxy group
        :type ProxyCount: int
        :param _ConnectionPoolType: Connection pool type. Valid value: `SessionConnectionPool` (session-level connection pool)
        :type ConnectionPoolType: str
        :param _OpenConnectionPool: Whether to enable connection pool. Valid value: `yes` (enable), `no` (disable).
        :type OpenConnectionPool: str
        :param _ConnectionPoolTimeOut: Connection pool threshold in seconds
        :type ConnectionPoolTimeOut: int
        :param _SecurityGroupIds: Array of security group IDs
        :type SecurityGroupIds: list of str
        :param _Description: Description
        :type Description: str
        :param _ProxyZones: Database node information
        :type ProxyZones: list of ProxyZone
        """
        self._ClusterId = None
        self._Cpu = None
        self._Mem = None
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._ProxyCount = None
        self._ConnectionPoolType = None
        self._OpenConnectionPool = None
        self._ConnectionPoolTimeOut = None
        self._SecurityGroupIds = None
        self._Description = None
        self._ProxyZones = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def UniqueVpcId(self):
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def ProxyCount(self):
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def OpenConnectionPool(self):
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolTimeOut(self):
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProxyZones(self):
        return self._ProxyZones

    @ProxyZones.setter
    def ProxyZones(self, ProxyZones):
        self._ProxyZones = ProxyZones


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._ProxyCount = params.get("ProxyCount")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        self._OpenConnectionPool = params.get("OpenConnectionPool")
        self._ConnectionPoolTimeOut = params.get("ConnectionPoolTimeOut")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Description = params.get("Description")
        if params.get("ProxyZones") is not None:
            self._ProxyZones = []
            for item in params.get("ProxyZones"):
                obj = ProxyZone()
                obj._deserialize(item)
                self._ProxyZones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyResponse(AbstractModel):
    """CreateProxy response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async flow ID
        :type FlowId: int
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._ProxyGroupId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._RequestId = params.get("RequestId")


class CreateResourcePackageRequest(AbstractModel):
    """CreateResourcePackage request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _PackageRegion: Region of the resource pack. Valid values: `China` (Chinese mainland), `overseas` (outside Chinese mainland).
        :type PackageRegion: str
        :param _PackageType: Resource pack type. Valid values: `CCU` (compute resource pack), `DISK` (storage resource pack).
        :type PackageType: str
        :param _PackageVersion: Resource pack edition. Valid values: `base` (basic edition), `common` (general edition), `enterprise` (enterprise edition).
        :type PackageVersion: str
        :param _PackageSpec: Resource pack size. Unit of the compute resource pack: Ten thousand.  Unit of the storage resource pack:  GB
        :type PackageSpec: float
        :param _ExpireDay: Validity period of a resource pack in days
        :type ExpireDay: int
        :param _PackageCount: Number of the resource packs to be purchased
        :type PackageCount: int
        :param _PackageName: Resource pack name
        :type PackageName: str
        """
        self._InstanceType = None
        self._PackageRegion = None
        self._PackageType = None
        self._PackageVersion = None
        self._PackageSpec = None
        self._ExpireDay = None
        self._PackageCount = None
        self._PackageName = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def PackageSpec(self):
        return self._PackageSpec

    @PackageSpec.setter
    def PackageSpec(self, PackageSpec):
        self._PackageSpec = PackageSpec

    @property
    def ExpireDay(self):
        return self._ExpireDay

    @ExpireDay.setter
    def ExpireDay(self, ExpireDay):
        self._ExpireDay = ExpireDay

    @property
    def PackageCount(self):
        return self._PackageCount

    @PackageCount.setter
    def PackageCount(self, PackageCount):
        self._PackageCount = PackageCount

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._PackageRegion = params.get("PackageRegion")
        self._PackageType = params.get("PackageType")
        self._PackageVersion = params.get("PackageVersion")
        self._PackageSpec = params.get("PackageSpec")
        self._ExpireDay = params.get("ExpireDay")
        self._PackageCount = params.get("PackageCount")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourcePackageResponse(AbstractModel):
    """CreateResourcePackage response structure.

    """

    def __init__(self):
        r"""
        :param _BigDealIds: Big order number
        :type BigDealIds: list of str
        :param _DealNames: Each item has only one `dealName`, through which you need to ensure the idempotency of the delivery API.
        :type DealNames: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BigDealIds = None
        self._DealNames = None
        self._RequestId = None

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BigDealIds = params.get("BigDealIds")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CynosdbCluster(AbstractModel):
    """Cluster information

    """

    def __init__(self):
        r"""
        :param _Status: Cluster status. Valid values are as follows:
creating
running
isolating
isolated
activating (removing isolation)
offlining (deactivating)
offlined (deactivated)
deleting
deleted
        :type Status: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Zone: AZ
        :type Zone: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _Region: Region
        :type Region: str
        :param _DbVersion: Database version
        :type DbVersion: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceNum: Number of instances
        :type InstanceNum: int
        :param _Uin: User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _DbType: Engine type
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbType: str
        :param _AppId: User `appid`
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _StatusDesc: Cluster status description
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusDesc: str
        :param _CreateTime: Cluster creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _PayMode: Billing mode. `0`: Pay-as-you-go; `1`: Monthly subscription.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: int
        :param _PeriodEndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.
        :type PeriodEndTime: str
        :param _Vip: Cluster read-write VIP
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vip: str
        :param _Vport: Cluster read-write vport
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vport: int
        :param _ProjectID: Project ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectID: int
        :param _VpcId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _CynosVersion: TDSQL-C kernel version
Note: This field may return null, indicating that no valid values can be obtained.
        :type CynosVersion: str
        :param _StorageLimit: Storage capacity
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageLimit: int
        :param _RenewFlag: Renewal flag
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param _ProcessingTask: Task in progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcessingTask: str
        :param _Tasks: Array of tasks in the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tasks: list of ObjectTask
        :param _ResourceTags: Array of tags bound to the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceTags: list of Tag
        :param _DbMode: Database type. Valid values: `NORMAL`, `SERVERLESS`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbMode: str
        :param _ServerlessStatus: Serverless cluster status when the database type is `SERVERLESS`. Valid values:
`resume`
`pause`
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServerlessStatus: str
        :param _Storage: Prepaid cluster storage capacity
Note: This field may return null, indicating that no valid values can be obtained.
        :type Storage: int
        :param _StorageId: Cluster storage ID used in prepaid storage modification
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageId: str
        :param _StoragePayMode: Billing mode of cluster storage. Valid values: `0` (pay-as-you-go), `1` (monthly subscription).
Note: This field may return null, indicating that no valid values can be obtained.
        :type StoragePayMode: int
        :param _MinStorageSize: The minimum storage corresponding to the compute specification of the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type MinStorageSize: int
        :param _MaxStorageSize: The maximum storage corresponding to the compute specification of the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxStorageSize: int
        :param _NetAddrs: Network information of the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetAddrs: list of NetAddr
        :param _PhysicalZone: Physical AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhysicalZone: str
        :param _MasterZone: Primary AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterZone: str
        :param _HasSlaveZone: Whether there is a secondary AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasSlaveZone: str
        :param _SlaveZones: Secondary AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaveZones: list of str
        :param _BusinessType: Business type
Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessType: str
        :param _IsFreeze: Whether to freeze
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFreeze: str
        :param _OrderSource: Order source
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrderSource: str
        :param _Ability: Capability
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ability: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        :param _ResourcePackages: Information of the resource pack bound to an instance when `packageType` is `DISK`. Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourcePackages: list of ResourcePackage
        """
        self._Status = None
        self._UpdateTime = None
        self._Zone = None
        self._ClusterName = None
        self._Region = None
        self._DbVersion = None
        self._ClusterId = None
        self._InstanceNum = None
        self._Uin = None
        self._DbType = None
        self._AppId = None
        self._StatusDesc = None
        self._CreateTime = None
        self._PayMode = None
        self._PeriodEndTime = None
        self._Vip = None
        self._Vport = None
        self._ProjectID = None
        self._VpcId = None
        self._SubnetId = None
        self._CynosVersion = None
        self._StorageLimit = None
        self._RenewFlag = None
        self._ProcessingTask = None
        self._Tasks = None
        self._ResourceTags = None
        self._DbMode = None
        self._ServerlessStatus = None
        self._Storage = None
        self._StorageId = None
        self._StoragePayMode = None
        self._MinStorageSize = None
        self._MaxStorageSize = None
        self._NetAddrs = None
        self._PhysicalZone = None
        self._MasterZone = None
        self._HasSlaveZone = None
        self._SlaveZones = None
        self._BusinessType = None
        self._IsFreeze = None
        self._OrderSource = None
        self._Ability = None
        self._ResourcePackages = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceNum(self):
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

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
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

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
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ProcessingTask(self):
        return self._ProcessingTask

    @ProcessingTask.setter
    def ProcessingTask(self, ProcessingTask):
        self._ProcessingTask = ProcessingTask

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageId(self):
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def MinStorageSize(self):
        return self._MinStorageSize

    @MinStorageSize.setter
    def MinStorageSize(self, MinStorageSize):
        self._MinStorageSize = MinStorageSize

    @property
    def MaxStorageSize(self):
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def NetAddrs(self):
        return self._NetAddrs

    @NetAddrs.setter
    def NetAddrs(self, NetAddrs):
        self._NetAddrs = NetAddrs

    @property
    def PhysicalZone(self):
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def HasSlaveZone(self):
        return self._HasSlaveZone

    @HasSlaveZone.setter
    def HasSlaveZone(self, HasSlaveZone):
        self._HasSlaveZone = HasSlaveZone

    @property
    def SlaveZones(self):
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def IsFreeze(self):
        return self._IsFreeze

    @IsFreeze.setter
    def IsFreeze(self, IsFreeze):
        self._IsFreeze = IsFreeze

    @property
    def OrderSource(self):
        return self._OrderSource

    @OrderSource.setter
    def OrderSource(self, OrderSource):
        self._OrderSource = OrderSource

    @property
    def Ability(self):
        return self._Ability

    @Ability.setter
    def Ability(self, Ability):
        self._Ability = Ability

    @property
    def ResourcePackages(self):
        return self._ResourcePackages

    @ResourcePackages.setter
    def ResourcePackages(self, ResourcePackages):
        self._ResourcePackages = ResourcePackages


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._UpdateTime = params.get("UpdateTime")
        self._Zone = params.get("Zone")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._DbVersion = params.get("DbVersion")
        self._ClusterId = params.get("ClusterId")
        self._InstanceNum = params.get("InstanceNum")
        self._Uin = params.get("Uin")
        self._DbType = params.get("DbType")
        self._AppId = params.get("AppId")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._PayMode = params.get("PayMode")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._ProjectID = params.get("ProjectID")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CynosVersion = params.get("CynosVersion")
        self._StorageLimit = params.get("StorageLimit")
        self._RenewFlag = params.get("RenewFlag")
        self._ProcessingTask = params.get("ProcessingTask")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DbMode = params.get("DbMode")
        self._ServerlessStatus = params.get("ServerlessStatus")
        self._Storage = params.get("Storage")
        self._StorageId = params.get("StorageId")
        self._StoragePayMode = params.get("StoragePayMode")
        self._MinStorageSize = params.get("MinStorageSize")
        self._MaxStorageSize = params.get("MaxStorageSize")
        if params.get("NetAddrs") is not None:
            self._NetAddrs = []
            for item in params.get("NetAddrs"):
                obj = NetAddr()
                obj._deserialize(item)
                self._NetAddrs.append(obj)
        self._PhysicalZone = params.get("PhysicalZone")
        self._MasterZone = params.get("MasterZone")
        self._HasSlaveZone = params.get("HasSlaveZone")
        self._SlaveZones = params.get("SlaveZones")
        self._BusinessType = params.get("BusinessType")
        self._IsFreeze = params.get("IsFreeze")
        self._OrderSource = params.get("OrderSource")
        if params.get("Ability") is not None:
            self._Ability = Ability()
            self._Ability._deserialize(params.get("Ability"))
        if params.get("ResourcePackages") is not None:
            self._ResourcePackages = []
            for item in params.get("ResourcePackages"):
                obj = ResourcePackage()
                obj._deserialize(item)
                self._ResourcePackages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbClusterDetail(AbstractModel):
    """Cluster details

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _Region: Region
        :type Region: str
        :param _Zone: AZ
        :type Zone: str
        :param _PhysicalZone: Physical AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhysicalZone: str
        :param _Status: Status
        :type Status: str
        :param _StatusDesc: Status description
        :type StatusDesc: str
        :param _ServerlessStatus: Serverless cluster status when the database type is `SERVERLESS`. Valid values:
resume
resuming
pause
pausing
        :type ServerlessStatus: str
        :param _StorageId: Storage ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageId: str
        :param _Storage: Storage capacity in GB
Note: This field may return null, indicating that no valid values can be obtained.
        :type Storage: int
        :param _MaxStorageSize: Maximum storage specification in GB
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxStorageSize: int
        :param _MinStorageSize: Minimum storage specification in GB
Note: This field may return null, indicating that no valid values can be obtained.
        :type MinStorageSize: int
        :param _StoragePayMode: Storage billing mode. Valid values: `1` (monthly subscription), `0` (pay-as-you-go).
Note: This field may return null, indicating that no valid values can be obtained.
        :type StoragePayMode: int
        :param _VpcName: VPC name
        :type VpcName: str
        :param _VpcId: Unique VPC ID
        :type VpcId: str
        :param _SubnetName: Subnet name
        :type SubnetName: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _Charset: Character set
        :type Charset: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _DbType: Database type
        :type DbType: str
        :param _DbMode: Database type. Valid values: `normal`, `serverless`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbMode: str
        :param _DbVersion: Database version
        :type DbVersion: str
        :param _StorageLimit: Maximum storage space
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageLimit: int
        :param _UsedStorage: Used capacity
        :type UsedStorage: int
        :param _Vip: VIP
        :type Vip: str
        :param _Vport: vport
        :type Vport: int
        :param _RoAddr: VIP and vport of the read-only instance in a cluster
        :type RoAddr: list of Addr
        :param _Ability: Features supported by the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ability: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        :param _CynosVersion: TDSQL-C version
Note: This field may return null, indicating that no valid values can be obtained.
        :type CynosVersion: str
        :param _BusinessType: Business type
Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessType: str
        :param _HasSlaveZone: Whether there is a secondary AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasSlaveZone: str
        :param _IsFreeze: Whether to freeze
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFreeze: str
        :param _Tasks: Task list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tasks: list of ObjectTask
        :param _MasterZone: Primary AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterZone: str
        :param _SlaveZones: Secondary AZ list
Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaveZones: list of str
        :param _InstanceSet: Instance information
        :type InstanceSet: list of ClusterInstanceDetail
        :param _PayMode: Billing mode
        :type PayMode: int
        :param _PeriodEndTime: Expiration time
        :type PeriodEndTime: str
        :param _ProjectID: Project ID
        :type ProjectID: int
        :param _ResourceTags: Array of tags bound to instance
        :type ResourceTags: list of Tag
        :param _ProxyStatus: Proxy status
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyStatus: str
        :param _LogBin: Binlog switch. Valid values: `ON`, `OFF`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogBin: str
        :param _IsSkipTrade: Whether to skip the transaction
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsSkipTrade: str
        :param _PitrType: PITR type. Valid values: `normal`, `redo_pitr`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PitrType: str
        :param _IsOpenPasswordComplexity: Whether to enable password complexity
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsOpenPasswordComplexity: str
        :param _NetworkStatus: Network type
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetworkStatus: str
        :param _ResourcePackages: Information of the resource pack bound to a cluster Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourcePackages: list of ResourcePackage
        :param _RenewFlag: The auto-renewal flag. Valid values: `0`: (manual renewal, default), `1` (auto-renewal). Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param _NetworkType: 
        :type NetworkType: str
        :param _SlaveZoneAttr: 
        :type SlaveZoneAttr: list of SlaveZoneAttrItem
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._Zone = None
        self._PhysicalZone = None
        self._Status = None
        self._StatusDesc = None
        self._ServerlessStatus = None
        self._StorageId = None
        self._Storage = None
        self._MaxStorageSize = None
        self._MinStorageSize = None
        self._StoragePayMode = None
        self._VpcName = None
        self._VpcId = None
        self._SubnetName = None
        self._SubnetId = None
        self._Charset = None
        self._CreateTime = None
        self._DbType = None
        self._DbMode = None
        self._DbVersion = None
        self._StorageLimit = None
        self._UsedStorage = None
        self._Vip = None
        self._Vport = None
        self._RoAddr = None
        self._Ability = None
        self._CynosVersion = None
        self._BusinessType = None
        self._HasSlaveZone = None
        self._IsFreeze = None
        self._Tasks = None
        self._MasterZone = None
        self._SlaveZones = None
        self._InstanceSet = None
        self._PayMode = None
        self._PeriodEndTime = None
        self._ProjectID = None
        self._ResourceTags = None
        self._ProxyStatus = None
        self._LogBin = None
        self._IsSkipTrade = None
        self._PitrType = None
        self._IsOpenPasswordComplexity = None
        self._NetworkStatus = None
        self._ResourcePackages = None
        self._RenewFlag = None
        self._NetworkType = None
        self._SlaveZoneAttr = None

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
    def PhysicalZone(self):
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def StorageId(self):
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def MaxStorageSize(self):
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def MinStorageSize(self):
        return self._MinStorageSize

    @MinStorageSize.setter
    def MinStorageSize(self, MinStorageSize):
        self._MinStorageSize = MinStorageSize

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def UsedStorage(self):
        return self._UsedStorage

    @UsedStorage.setter
    def UsedStorage(self, UsedStorage):
        self._UsedStorage = UsedStorage

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
    def RoAddr(self):
        return self._RoAddr

    @RoAddr.setter
    def RoAddr(self, RoAddr):
        self._RoAddr = RoAddr

    @property
    def Ability(self):
        return self._Ability

    @Ability.setter
    def Ability(self, Ability):
        self._Ability = Ability

    @property
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def HasSlaveZone(self):
        return self._HasSlaveZone

    @HasSlaveZone.setter
    def HasSlaveZone(self, HasSlaveZone):
        self._HasSlaveZone = HasSlaveZone

    @property
    def IsFreeze(self):
        return self._IsFreeze

    @IsFreeze.setter
    def IsFreeze(self, IsFreeze):
        self._IsFreeze = IsFreeze

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def ProxyStatus(self):
        return self._ProxyStatus

    @ProxyStatus.setter
    def ProxyStatus(self, ProxyStatus):
        self._ProxyStatus = ProxyStatus

    @property
    def LogBin(self):
        return self._LogBin

    @LogBin.setter
    def LogBin(self, LogBin):
        self._LogBin = LogBin

    @property
    def IsSkipTrade(self):
        return self._IsSkipTrade

    @IsSkipTrade.setter
    def IsSkipTrade(self, IsSkipTrade):
        self._IsSkipTrade = IsSkipTrade

    @property
    def PitrType(self):
        return self._PitrType

    @PitrType.setter
    def PitrType(self, PitrType):
        self._PitrType = PitrType

    @property
    def IsOpenPasswordComplexity(self):
        return self._IsOpenPasswordComplexity

    @IsOpenPasswordComplexity.setter
    def IsOpenPasswordComplexity(self, IsOpenPasswordComplexity):
        self._IsOpenPasswordComplexity = IsOpenPasswordComplexity

    @property
    def NetworkStatus(self):
        return self._NetworkStatus

    @NetworkStatus.setter
    def NetworkStatus(self, NetworkStatus):
        self._NetworkStatus = NetworkStatus

    @property
    def ResourcePackages(self):
        return self._ResourcePackages

    @ResourcePackages.setter
    def ResourcePackages(self, ResourcePackages):
        self._ResourcePackages = ResourcePackages

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def SlaveZoneAttr(self):
        return self._SlaveZoneAttr

    @SlaveZoneAttr.setter
    def SlaveZoneAttr(self, SlaveZoneAttr):
        self._SlaveZoneAttr = SlaveZoneAttr


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._PhysicalZone = params.get("PhysicalZone")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._ServerlessStatus = params.get("ServerlessStatus")
        self._StorageId = params.get("StorageId")
        self._Storage = params.get("Storage")
        self._MaxStorageSize = params.get("MaxStorageSize")
        self._MinStorageSize = params.get("MinStorageSize")
        self._StoragePayMode = params.get("StoragePayMode")
        self._VpcName = params.get("VpcName")
        self._VpcId = params.get("VpcId")
        self._SubnetName = params.get("SubnetName")
        self._SubnetId = params.get("SubnetId")
        self._Charset = params.get("Charset")
        self._CreateTime = params.get("CreateTime")
        self._DbType = params.get("DbType")
        self._DbMode = params.get("DbMode")
        self._DbVersion = params.get("DbVersion")
        self._StorageLimit = params.get("StorageLimit")
        self._UsedStorage = params.get("UsedStorage")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        if params.get("RoAddr") is not None:
            self._RoAddr = []
            for item in params.get("RoAddr"):
                obj = Addr()
                obj._deserialize(item)
                self._RoAddr.append(obj)
        if params.get("Ability") is not None:
            self._Ability = Ability()
            self._Ability._deserialize(params.get("Ability"))
        self._CynosVersion = params.get("CynosVersion")
        self._BusinessType = params.get("BusinessType")
        self._HasSlaveZone = params.get("HasSlaveZone")
        self._IsFreeze = params.get("IsFreeze")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._MasterZone = params.get("MasterZone")
        self._SlaveZones = params.get("SlaveZones")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ClusterInstanceDetail()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._PayMode = params.get("PayMode")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._ProjectID = params.get("ProjectID")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._ProxyStatus = params.get("ProxyStatus")
        self._LogBin = params.get("LogBin")
        self._IsSkipTrade = params.get("IsSkipTrade")
        self._PitrType = params.get("PitrType")
        self._IsOpenPasswordComplexity = params.get("IsOpenPasswordComplexity")
        self._NetworkStatus = params.get("NetworkStatus")
        if params.get("ResourcePackages") is not None:
            self._ResourcePackages = []
            for item in params.get("ResourcePackages"):
                obj = ResourcePackage()
                obj._deserialize(item)
                self._ResourcePackages.append(obj)
        self._RenewFlag = params.get("RenewFlag")
        self._NetworkType = params.get("NetworkType")
        if params.get("SlaveZoneAttr") is not None:
            self._SlaveZoneAttr = []
            for item in params.get("SlaveZoneAttr"):
                obj = SlaveZoneAttrItem()
                obj._deserialize(item)
                self._SlaveZoneAttr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbErrorLogItem(AbstractModel):
    """Types of the returned error logs for an instance

    """

    def __init__(self):
        r"""
        :param _Timestamp: Log timestamp Note: This field may return null, indicating that no valid values can be obtained.
        :type Timestamp: int
        :param _Level: Log level Note: This field may return null, indicating that no valid values can be obtained.
        :type Level: str
        :param _Content: Log content Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: str
        """
        self._Timestamp = None
        self._Level = None
        self._Content = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Level = params.get("Level")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstance(AbstractModel):
    """Instance information

    """

    def __init__(self):
        r"""
        :param _Uin: User `Uin`
        :type Uin: str
        :param _AppId: User `AppId`
        :type AppId: int
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Region: Region
        :type Region: str
        :param _Zone: AZ
        :type Zone: str
        :param _Status: Instance status
        :type Status: str
        :param _StatusDesc: Instance status description
        :type StatusDesc: str
        :param _DbMode: Instance type, which is used to indicate whether it is a serverless instance.
        :type DbMode: str
        :param _DbType: Database type
        :type DbType: str
        :param _DbVersion: Database version
        :type DbVersion: str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Memory: Memory in GB
        :type Memory: int
        :param _Storage: Storage capacity in GB
        :type Storage: int
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _InstanceRole: Current instance role
        :type InstanceRole: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _Vip: Private IP of instance
        :type Vip: str
        :param _Vport: Private port of instance
        :type Vport: int
        :param _PayMode: Billing mode
        :type PayMode: int
        :param _PeriodEndTime: Instance expiration time
        :type PeriodEndTime: str
        :param _DestroyDeadlineText: Termination deadline
        :type DestroyDeadlineText: str
        :param _IsolateTime: Isolation time
        :type IsolateTime: str
        :param _NetType: Network type
        :type NetType: int
        :param _WanDomain: Public domain name
        :type WanDomain: str
        :param _WanIP: Public IP
        :type WanIP: str
        :param _WanPort: Public port
        :type WanPort: int
        :param _WanStatus: Public network status
        :type WanStatus: str
        :param _DestroyTime: Instance termination time
        :type DestroyTime: str
        :param _CynosVersion: TDSQL-C kernel version
        :type CynosVersion: str
        :param _ProcessingTask: Task in progress
        :type ProcessingTask: str
        :param _RenewFlag: Renewal flag
        :type RenewFlag: int
        :param _MinCpu: Minimum number of CPU cores for serverless instance
        :type MinCpu: float
        :param _MaxCpu: Maximum number of CPU cores for serverless instance
        :type MaxCpu: float
        :param _ServerlessStatus: Serverless instance status. Valid values:
resume
pause
        :type ServerlessStatus: str
        :param _StorageId: Prepaid storage ID
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type StorageId: str
        :param _StoragePayMode: Storage billing mode
        :type StoragePayMode: int
        :param _PhysicalZone: Physical zone
        :type PhysicalZone: str
        :param _BusinessType: Business type
Note: This field may return null, indicating that no valid value can be obtained.
        :type BusinessType: str
        :param _Tasks: Task
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tasks: list of ObjectTask
        :param _IsFreeze: Whether to freeze
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFreeze: str
        :param _ResourceTags: The resource tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceTags: list of Tag
        :param _MasterZone: Source AZ
Note: This field may return null, indicating that no valid value can be obtained.
        :type MasterZone: str
        :param _SlaveZones: Replica AZ
Note: This field may return null, indicating that no valid value can be obtained.
        :type SlaveZones: list of str
        :param _InstanceNetInfo: Instance network information
Note: This field may return null, indicating that no valid value can be obtained.
        :type InstanceNetInfo: list of InstanceNetInfo
        :param _ResourcePackages: Information of the resource pack bound to an instance when `packageType` is `CCU`. Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourcePackages: list of ResourcePackage
        """
        self._Uin = None
        self._AppId = None
        self._ClusterId = None
        self._ClusterName = None
        self._InstanceId = None
        self._InstanceName = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._Status = None
        self._StatusDesc = None
        self._DbMode = None
        self._DbType = None
        self._DbVersion = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._InstanceType = None
        self._InstanceRole = None
        self._UpdateTime = None
        self._CreateTime = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vport = None
        self._PayMode = None
        self._PeriodEndTime = None
        self._DestroyDeadlineText = None
        self._IsolateTime = None
        self._NetType = None
        self._WanDomain = None
        self._WanIP = None
        self._WanPort = None
        self._WanStatus = None
        self._DestroyTime = None
        self._CynosVersion = None
        self._ProcessingTask = None
        self._RenewFlag = None
        self._MinCpu = None
        self._MaxCpu = None
        self._ServerlessStatus = None
        self._StorageId = None
        self._StoragePayMode = None
        self._PhysicalZone = None
        self._BusinessType = None
        self._Tasks = None
        self._IsFreeze = None
        self._ResourceTags = None
        self._MasterZone = None
        self._SlaveZones = None
        self._InstanceNetInfo = None
        self._ResourcePackages = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def DestroyDeadlineText(self):
        return self._DestroyDeadlineText

    @DestroyDeadlineText.setter
    def DestroyDeadlineText(self, DestroyDeadlineText):
        self._DestroyDeadlineText = DestroyDeadlineText

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def DestroyTime(self):
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def ProcessingTask(self):
        return self._ProcessingTask

    @ProcessingTask.setter
    def ProcessingTask(self, ProcessingTask):
        self._ProcessingTask = ProcessingTask

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def MinCpu(self):
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def StorageId(self):
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def PhysicalZone(self):
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def IsFreeze(self):
        return self._IsFreeze

    @IsFreeze.setter
    def IsFreeze(self, IsFreeze):
        self._IsFreeze = IsFreeze

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def InstanceNetInfo(self):
        return self._InstanceNetInfo

    @InstanceNetInfo.setter
    def InstanceNetInfo(self, InstanceNetInfo):
        self._InstanceNetInfo = InstanceNetInfo

    @property
    def ResourcePackages(self):
        return self._ResourcePackages

    @ResourcePackages.setter
    def ResourcePackages(self, ResourcePackages):
        self._ResourcePackages = ResourcePackages


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DbMode = params.get("DbMode")
        self._DbType = params.get("DbType")
        self._DbVersion = params.get("DbVersion")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceType = params.get("InstanceType")
        self._InstanceRole = params.get("InstanceRole")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._PayMode = params.get("PayMode")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._DestroyDeadlineText = params.get("DestroyDeadlineText")
        self._IsolateTime = params.get("IsolateTime")
        self._NetType = params.get("NetType")
        self._WanDomain = params.get("WanDomain")
        self._WanIP = params.get("WanIP")
        self._WanPort = params.get("WanPort")
        self._WanStatus = params.get("WanStatus")
        self._DestroyTime = params.get("DestroyTime")
        self._CynosVersion = params.get("CynosVersion")
        self._ProcessingTask = params.get("ProcessingTask")
        self._RenewFlag = params.get("RenewFlag")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._ServerlessStatus = params.get("ServerlessStatus")
        self._StorageId = params.get("StorageId")
        self._StoragePayMode = params.get("StoragePayMode")
        self._PhysicalZone = params.get("PhysicalZone")
        self._BusinessType = params.get("BusinessType")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._IsFreeze = params.get("IsFreeze")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._MasterZone = params.get("MasterZone")
        self._SlaveZones = params.get("SlaveZones")
        if params.get("InstanceNetInfo") is not None:
            self._InstanceNetInfo = []
            for item in params.get("InstanceNetInfo"):
                obj = InstanceNetInfo()
                obj._deserialize(item)
                self._InstanceNetInfo.append(obj)
        if params.get("ResourcePackages") is not None:
            self._ResourcePackages = []
            for item in params.get("ResourcePackages"):
                obj = ResourcePackage()
                obj._deserialize(item)
                self._ResourcePackages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceDetail(AbstractModel):
    """Instance details

    """

    def __init__(self):
        r"""
        :param _Uin: User `Uin`
        :type Uin: str
        :param _AppId: User `AppId`
        :type AppId: int
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Region: Region
        :type Region: str
        :param _Zone: AZ
        :type Zone: str
        :param _Status: Instance status
        :type Status: str
        :param _StatusDesc: Instance status description
        :type StatusDesc: str
        :param _DbType: Database type
        :type DbType: str
        :param _DbVersion: Database version
        :type DbVersion: str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Memory: Memory in GB
        :type Memory: int
        :param _Storage: Storage capacity in GB
        :type Storage: int
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _InstanceRole: Current instance role
        :type InstanceRole: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _PayMode: Billing mode
        :type PayMode: int
        :param _PeriodEndTime: Instance expiration time
        :type PeriodEndTime: str
        :param _NetType: Network type
        :type NetType: int
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _Vip: Private IP of instance
        :type Vip: str
        :param _Vport: Private port of instance
        :type Vport: int
        :param _WanDomain: Public domain name of instance
        :type WanDomain: str
        :param _Charset: Character set
        :type Charset: str
        :param _CynosVersion: TDSQL-C kernel version
        :type CynosVersion: str
        :param _RenewFlag: Renewal flag
        :type RenewFlag: int
        :param _MinCpu: The minimum number of CPU cores for a serverless instance
        :type MinCpu: float
        :param _MaxCpu: The maximum number of CPU cores for a serverless instance
        :type MaxCpu: float
        :param _ServerlessStatus: Serverless instance status. Valid values:
resume
pause
        :type ServerlessStatus: str
        """
        self._Uin = None
        self._AppId = None
        self._ClusterId = None
        self._ClusterName = None
        self._InstanceId = None
        self._InstanceName = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._Status = None
        self._StatusDesc = None
        self._DbType = None
        self._DbVersion = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._InstanceType = None
        self._InstanceRole = None
        self._UpdateTime = None
        self._CreateTime = None
        self._PayMode = None
        self._PeriodEndTime = None
        self._NetType = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._Charset = None
        self._CynosVersion = None
        self._RenewFlag = None
        self._MinCpu = None
        self._MaxCpu = None
        self._ServerlessStatus = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

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
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def MinCpu(self):
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DbType = params.get("DbType")
        self._DbVersion = params.get("DbVersion")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceType = params.get("InstanceType")
        self._InstanceRole = params.get("InstanceRole")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._PayMode = params.get("PayMode")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._NetType = params.get("NetType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._Charset = params.get("Charset")
        self._CynosVersion = params.get("CynosVersion")
        self._RenewFlag = params.get("RenewFlag")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._ServerlessStatus = params.get("ServerlessStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceGrp(AbstractModel):
    """Instance group information

    """

    def __init__(self):
        r"""
        :param _AppId: User `appId`
        :type AppId: int
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _CreatedTime: Creation time
        :type CreatedTime: str
        :param _DeletedTime: Deletion time
        :type DeletedTime: str
        :param _InstanceGrpId: Instance group ID
        :type InstanceGrpId: str
        :param _Status: Status
        :type Status: str
        :param _Type: Instance group type. ha: HA group; ro: RO group
        :type Type: str
        :param _UpdatedTime: Update time
        :type UpdatedTime: str
        :param _Vip: Private IP
        :type Vip: str
        :param _Vport: Private port
        :type Vport: int
        :param _WanDomain: Public domain name
        :type WanDomain: str
        :param _WanIP: Public IP
        :type WanIP: str
        :param _WanPort: Public port
        :type WanPort: int
        :param _WanStatus: Public network status
        :type WanStatus: str
        :param _InstanceSet: Information of instances contained in instance group
        :type InstanceSet: list of CynosdbInstance
        :param _UniqVpcId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param _UniqSubnetId: Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqSubnetId: str
        :param _OldAddrInfo: Information of the old IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type OldAddrInfo: :class:`tencentcloud.cynosdb.v20190107.models.OldAddrInfo`
        :param _ProcessingTasks: Task in progress
        :type ProcessingTasks: list of str
        :param _Tasks: Task list
        :type Tasks: list of ObjectTask
        :param _NetServiceId: biz_net_service table ID
        :type NetServiceId: int
        """
        self._AppId = None
        self._ClusterId = None
        self._CreatedTime = None
        self._DeletedTime = None
        self._InstanceGrpId = None
        self._Status = None
        self._Type = None
        self._UpdatedTime = None
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._WanIP = None
        self._WanPort = None
        self._WanStatus = None
        self._InstanceSet = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._OldAddrInfo = None
        self._ProcessingTasks = None
        self._Tasks = None
        self._NetServiceId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DeletedTime(self):
        return self._DeletedTime

    @DeletedTime.setter
    def DeletedTime(self, DeletedTime):
        self._DeletedTime = DeletedTime

    @property
    def InstanceGrpId(self):
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        self._InstanceGrpId = InstanceGrpId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

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
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

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
    def OldAddrInfo(self):
        return self._OldAddrInfo

    @OldAddrInfo.setter
    def OldAddrInfo(self, OldAddrInfo):
        self._OldAddrInfo = OldAddrInfo

    @property
    def ProcessingTasks(self):
        return self._ProcessingTasks

    @ProcessingTasks.setter
    def ProcessingTasks(self, ProcessingTasks):
        self._ProcessingTasks = ProcessingTasks

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def NetServiceId(self):
        return self._NetServiceId

    @NetServiceId.setter
    def NetServiceId(self, NetServiceId):
        self._NetServiceId = NetServiceId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._CreatedTime = params.get("CreatedTime")
        self._DeletedTime = params.get("DeletedTime")
        self._InstanceGrpId = params.get("InstanceGrpId")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._UpdatedTime = params.get("UpdatedTime")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._WanIP = params.get("WanIP")
        self._WanPort = params.get("WanPort")
        self._WanStatus = params.get("WanStatus")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        if params.get("OldAddrInfo") is not None:
            self._OldAddrInfo = OldAddrInfo()
            self._OldAddrInfo._deserialize(params.get("OldAddrInfo"))
        self._ProcessingTasks = params.get("ProcessingTasks")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._NetServiceId = params.get("NetServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivileges(AbstractModel):
    """Database permission list

    """

    def __init__(self):
        r"""
        :param _Db: Database
        :type Db: str
        :param _Privileges: Permission list
        :type Privileges: list of str
        """
        self._Db = None
        self._Privileges = None

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTables(AbstractModel):
    """Database table information

    """

    def __init__(self):
        r"""
        :param _Database: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param _Tables: Table name list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of str
        """
        self._Database = None
        self._Tables = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Tables = params.get("Tables")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbInfo(AbstractModel):
    """Database details

    """

    def __init__(self):
        r"""
        :param _DbName: Database name
        :type DbName: str
        :param _CharacterSet: Character set
        :type CharacterSet: str
        :param _Status: Database status
        :type Status: str
        :param _CollateRule: Collation
        :type CollateRule: str
        :param _Description: Database remarks Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _UserHostPrivileges: User permissions Note: This field may return null, indicating that no valid values can be obtained.
        :type UserHostPrivileges: list of UserHostPrivilege
        :param _DbId: Database ID Note: This field may return null, indicating that no valid values can be obtained.
        :type DbId: int
        :param _CreateTime: Creation time Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _AppId: User appid Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _Uin: User Uin Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _ClusterId: Cluster ID Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        """
        self._DbName = None
        self._CharacterSet = None
        self._Status = None
        self._CollateRule = None
        self._Description = None
        self._UserHostPrivileges = None
        self._DbId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AppId = None
        self._Uin = None
        self._ClusterId = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CharacterSet(self):
        return self._CharacterSet

    @CharacterSet.setter
    def CharacterSet(self, CharacterSet):
        self._CharacterSet = CharacterSet

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CollateRule(self):
        return self._CollateRule

    @CollateRule.setter
    def CollateRule(self, CollateRule):
        self._CollateRule = CollateRule

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserHostPrivileges(self):
        return self._UserHostPrivileges

    @UserHostPrivileges.setter
    def UserHostPrivileges(self, UserHostPrivileges):
        self._UserHostPrivileges = UserHostPrivileges

    @property
    def DbId(self):
        return self._DbId

    @DbId.setter
    def DbId(self, DbId):
        self._DbId = DbId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._CharacterSet = params.get("CharacterSet")
        self._Status = params.get("Status")
        self._CollateRule = params.get("CollateRule")
        self._Description = params.get("Description")
        if params.get("UserHostPrivileges") is not None:
            self._UserHostPrivileges = []
            for item in params.get("UserHostPrivileges"):
                obj = UserHostPrivilege()
                obj._deserialize(item)
                self._UserHostPrivileges.append(obj)
        self._DbId = params.get("DbId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsRequest(AbstractModel):
    """DeleteAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Accounts: Accounts in array, which contains `account` and `host`.
        :type Accounts: list of InputAccount
        """
        self._ClusterId = None
        self._Accounts = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = InputAccount()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsResponse(AbstractModel):
    """DeleteAccounts response structure.

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


class DeleteAuditRuleTemplatesRequest(AbstractModel):
    """DeleteAuditRuleTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _RuleTemplateIds: Audit rule template ID
        :type RuleTemplateIds: list of str
        """
        self._RuleTemplateIds = None

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds


    def _deserialize(self, params):
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditRuleTemplatesResponse(AbstractModel):
    """DeleteAuditRuleTemplates response structure.

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


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _SnapshotIdList: Backup file ID. This field is used by legacy versions and thus not recommended.
        :type SnapshotIdList: list of int
        :param _BackupIds: Backup file ID. This field is recommended.
        :type BackupIds: list of int
        """
        self._ClusterId = None
        self._SnapshotIdList = None
        self._BackupIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SnapshotIdList(self):
        return self._SnapshotIdList

    @SnapshotIdList.setter
    def SnapshotIdList(self, SnapshotIdList):
        self._SnapshotIdList = SnapshotIdList

    @property
    def BackupIds(self):
        return self._BackupIds

    @BackupIds.setter
    def BackupIds(self, BackupIds):
        self._BackupIds = BackupIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SnapshotIdList = params.get("SnapshotIdList")
        self._BackupIds = params.get("BackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupResponse(AbstractModel):
    """DeleteBackup response structure.

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


class DeleteClusterDatabaseRequest(AbstractModel):
    """DeleteClusterDatabase request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _DbNames: 
        :type DbNames: list of str
        """
        self._ClusterId = None
        self._DbNames = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbNames(self):
        return self._DbNames

    @DbNames.setter
    def DbNames(self, DbNames):
        self._DbNames = DbNames


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DbNames = params.get("DbNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterDatabaseResponse(AbstractModel):
    """DeleteClusterDatabase response structure.

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


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParamTemplateResponse(AbstractModel):
    """DeleteParamTemplate response structure.

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


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _AccountName: Account name
        :type AccountName: str
        :param _Host: Host
        :type Host: str
        :param _Db: When the database name is “*”, the value specified in `Type` and `TableName` will be ignored, indicating that the user's global permissions are being modified.
        :type Db: str
        :param _Type: Object type in a specified database. Valid values: `table`, `*`.
        :type Type: str
        :param _TableName: The database name can be specified when `Type` is 'table'.
        :type TableName: str
        """
        self._ClusterId = None
        self._AccountName = None
        self._Host = None
        self._Db = None
        self._Type = None
        self._TableName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AccountName = params.get("AccountName")
        self._Host = params.get("Host")
        self._Db = params.get("Db")
        self._Type = params.get("Type")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _Privileges: The list of permissions, such as  ["select","update","delete","create","drop","references","index","alter","show_db","create_tmp_table","lock_tables","execute","create_view","show_view","create_routine","alter_routine","event","trigger"]
        :type Privileges: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Privileges = None
        self._RequestId = None

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Privileges = params.get("Privileges")
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _AccountNames: List of accounts to be filtered
        :type AccountNames: list of str
        :param _DbType: Database type. Valid values: 
<li> MYSQL </li>
This parameter has been disused.
        :type DbType: str
        :param _Hosts: List of accounts to be filtered
        :type Hosts: list of str
        :param _Limit: Maximum entries returned per page
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _AccountRegular: Keywords for fuzzy search (match `AccountName` and `AccountHost` at the same time), which supports regex. The union results will be returned.
        :type AccountRegular: str
        """
        self._ClusterId = None
        self._AccountNames = None
        self._DbType = None
        self._Hosts = None
        self._Limit = None
        self._Offset = None
        self._AccountRegular = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AccountNames(self):
        return self._AccountNames

    @AccountNames.setter
    def AccountNames(self, AccountNames):
        self._AccountNames = AccountNames

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

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
    def AccountRegular(self):
        return self._AccountRegular

    @AccountRegular.setter
    def AccountRegular(self, AccountRegular):
        self._AccountRegular = AccountRegular


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AccountNames = params.get("AccountNames")
        self._DbType = params.get("DbType")
        self._Hosts = params.get("Hosts")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AccountRegular = params.get("AccountRegular")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _AccountSet: Database account list
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountSet: list of Account
        :param _TotalCount: Total number of accounts
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AccountSet(self):
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

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
        if params.get("AccountSet") is not None:
            self._AccountSet = []
            for item in params.get("AccountSet"):
                obj = Account()
                obj._deserialize(item)
                self._AccountSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAuditRuleTemplatesRequest(AbstractModel):
    """DescribeAuditRuleTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _RuleTemplateIds: Rule template ID
        :type RuleTemplateIds: list of str
        :param _RuleTemplateNames: Rule template name
        :type RuleTemplateNames: list of str
        :param _Limit: Number of results returned per request. Default value: `20`.
        :type Limit: int
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        """
        self._RuleTemplateIds = None
        self._RuleTemplateNames = None
        self._Limit = None
        self._Offset = None

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds

    @property
    def RuleTemplateNames(self):
        return self._RuleTemplateNames

    @RuleTemplateNames.setter
    def RuleTemplateNames(self, RuleTemplateNames):
        self._RuleTemplateNames = RuleTemplateNames

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


    def _deserialize(self, params):
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        self._RuleTemplateNames = params.get("RuleTemplateNames")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditRuleTemplatesResponse(AbstractModel):
    """DescribeAuditRuleTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances
        :type TotalCount: int
        :param _Items: List of rule template details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of AuditRuleTemplateInfo
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
                obj = AuditRuleTemplateInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditRuleWithInstanceIdsRequest(AbstractModel):
    """DescribeAuditRuleWithInstanceIds request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID. Currently, only one single instance can be queried.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditRuleWithInstanceIdsResponse(AbstractModel):
    """DescribeAuditRuleWithInstanceIds response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: None
        :type TotalCount: int
        :param _Items: Audit rule information of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of InstanceAuditRule
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
                obj = InstanceAuditRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
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
        


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig response structure.

    """

    def __init__(self):
        r"""
        :param _BackupTimeBeg: Full backup start time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively
        :type BackupTimeBeg: int
        :param _BackupTimeEnd: Full backup end time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively
        :type BackupTimeEnd: int
        :param _ReserveDuration: Backup retention period in seconds. Backups will be cleared after this period elapses. 7 days is represented by 3600*24*7 = 604800
        :type ReserveDuration: int
        :param _BackupFreq: Backup frequency. It is an array of 7 elements corresponding to Monday through Sunday. full: full backup; increment: incremental backup
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupFreq: list of str
        :param _BackupType: Backup mode. logic: logic backup; snapshot: snapshot backup
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupType: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupTimeBeg = None
        self._BackupTimeEnd = None
        self._ReserveDuration = None
        self._BackupFreq = None
        self._BackupType = None
        self._RequestId = None

    @property
    def BackupTimeBeg(self):
        return self._BackupTimeBeg

    @BackupTimeBeg.setter
    def BackupTimeBeg(self, BackupTimeBeg):
        self._BackupTimeBeg = BackupTimeBeg

    @property
    def BackupTimeEnd(self):
        return self._BackupTimeEnd

    @BackupTimeEnd.setter
    def BackupTimeEnd(self, BackupTimeEnd):
        self._BackupTimeEnd = BackupTimeEnd

    @property
    def ReserveDuration(self):
        return self._ReserveDuration

    @ReserveDuration.setter
    def ReserveDuration(self, ReserveDuration):
        self._ReserveDuration = ReserveDuration

    @property
    def BackupFreq(self):
        return self._BackupFreq

    @BackupFreq.setter
    def BackupFreq(self, BackupFreq):
        self._BackupFreq = BackupFreq

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupTimeBeg = params.get("BackupTimeBeg")
        self._BackupTimeEnd = params.get("BackupTimeEnd")
        self._ReserveDuration = params.get("ReserveDuration")
        self._BackupFreq = params.get("BackupFreq")
        self._BackupType = params.get("BackupType")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadUrlRequest(AbstractModel):
    """DescribeBackupDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _BackupId: Backup ID
        :type BackupId: int
        """
        self._ClusterId = None
        self._BackupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadUrlResponse(AbstractModel):
    """DescribeBackupDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: Backup download address
        :type DownloadUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeBackupListRequest(AbstractModel):
    """DescribeBackupList request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Limit: The number of results to be returned. Value range: (0,100]
        :type Limit: int
        :param _Offset: Record offset. Value range: [0,INF)
        :type Offset: int
        :param _DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        :param _BackupIds: Backup ID
        :type BackupIds: list of int
        :param _BackupType: Backup type. Valid values: `snapshot` (snapshot backup), `logic` (logic backup).
        :type BackupType: str
        :param _BackupMethod: Back mode. Valid values: `auto` (automatic backup), `manual` (manual backup)
        :type BackupMethod: str
        :param _SnapShotType: 
        :type SnapShotType: str
        :param _StartTime: Backup start time
        :type StartTime: str
        :param _EndTime: Backup end time
        :type EndTime: str
        :param _FileNames: 
        :type FileNames: list of str
        :param _BackupNames: Backup alias, which supports fuzzy query.
        :type BackupNames: list of str
        :param _SnapshotIdList: ID list of the snapshot backup
        :type SnapshotIdList: list of int
        """
        self._ClusterId = None
        self._Limit = None
        self._Offset = None
        self._DbType = None
        self._BackupIds = None
        self._BackupType = None
        self._BackupMethod = None
        self._SnapShotType = None
        self._StartTime = None
        self._EndTime = None
        self._FileNames = None
        self._BackupNames = None
        self._SnapshotIdList = None

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
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def BackupIds(self):
        return self._BackupIds

    @BackupIds.setter
    def BackupIds(self, BackupIds):
        self._BackupIds = BackupIds

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def SnapShotType(self):
        return self._SnapShotType

    @SnapShotType.setter
    def SnapShotType(self, SnapShotType):
        self._SnapShotType = SnapShotType

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
    def FileNames(self):
        return self._FileNames

    @FileNames.setter
    def FileNames(self, FileNames):
        self._FileNames = FileNames

    @property
    def BackupNames(self):
        return self._BackupNames

    @BackupNames.setter
    def BackupNames(self, BackupNames):
        self._BackupNames = BackupNames

    @property
    def SnapshotIdList(self):
        return self._SnapshotIdList

    @SnapshotIdList.setter
    def SnapshotIdList(self, SnapshotIdList):
        self._SnapshotIdList = SnapshotIdList


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DbType = params.get("DbType")
        self._BackupIds = params.get("BackupIds")
        self._BackupType = params.get("BackupType")
        self._BackupMethod = params.get("BackupMethod")
        self._SnapShotType = params.get("SnapShotType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._FileNames = params.get("FileNames")
        self._BackupNames = params.get("BackupNames")
        self._SnapshotIdList = params.get("SnapshotIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupListResponse(AbstractModel):
    """DescribeBackupList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of backup files
        :type TotalCount: int
        :param _BackupList: Backup file list
        :type BackupList: list of BackupFileInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupList(self):
        return self._BackupList

    @BackupList.setter
    def BackupList(self, BackupList):
        self._BackupList = BackupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BackupList") is not None:
            self._BackupList = []
            for item in params.get("BackupList"):
                obj = BackupFileInfo()
                obj._deserialize(item)
                self._BackupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBinlogDownloadUrlRequest(AbstractModel):
    """DescribeBinlogDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _BinlogId: Binlog file ID
        :type BinlogId: int
        """
        self._ClusterId = None
        self._BinlogId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BinlogId(self):
        return self._BinlogId

    @BinlogId.setter
    def BinlogId(self, BinlogId):
        self._BinlogId = BinlogId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BinlogId = params.get("BinlogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogDownloadUrlResponse(AbstractModel):
    """DescribeBinlogDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: Download address
        :type DownloadUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeBinlogSaveDaysRequest(AbstractModel):
    """DescribeBinlogSaveDays request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
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
        


class DescribeBinlogSaveDaysResponse(AbstractModel):
    """DescribeBinlogSaveDays response structure.

    """

    def __init__(self):
        r"""
        :param _BinlogSaveDays: Binlog retention period in days
        :type BinlogSaveDays: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BinlogSaveDays = None
        self._RequestId = None

    @property
    def BinlogSaveDays(self):
        return self._BinlogSaveDays

    @BinlogSaveDays.setter
    def BinlogSaveDays(self, BinlogSaveDays):
        self._BinlogSaveDays = BinlogSaveDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BinlogSaveDays = params.get("BinlogSaveDays")
        self._RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Maximum number
        :type Limit: int
        """
        self._ClusterId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _Binlogs: Binlog list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Binlogs: list of BinlogItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Binlogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Binlogs(self):
        return self._Binlogs

    @Binlogs.setter
    def Binlogs(self, Binlogs):
        self._Binlogs = Binlogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Binlogs") is not None:
            self._Binlogs = []
            for item in params.get("Binlogs"):
                obj = BinlogItem()
                obj._deserialize(item)
                self._Binlogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterDetailDatabasesRequest(AbstractModel):
    """DescribeClusterDetailDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: `20`. Maximum value: `100`.
        :type Limit: int
        :param _DbName: Database name
        :type DbName: str
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None
        self._DbName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailDatabasesResponse(AbstractModel):
    """DescribeClusterDetailDatabases response structure.

    """

    def __init__(self):
        r"""
        :param _DbInfos: Database information Note: This field may return null, indicating that no valid values can be obtained.
        :type DbInfos: list of DbInfo
        :param _TotalCount: The total count
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DbInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DbInfos(self):
        return self._DbInfos

    @DbInfos.setter
    def DbInfos(self, DbInfos):
        self._DbInfos = DbInfos

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
        if params.get("DbInfos") is not None:
            self._DbInfos = []
            for item in params.get("DbInfos"):
                obj = DbInfo()
                obj._deserialize(item)
                self._DbInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
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
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Detail: Cluster details
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbClusterDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Detail = None
        self._RequestId = None

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self._Detail = CynosdbClusterDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeClusterInstanceGrpsRequest(AbstractModel):
    """DescribeClusterInstanceGrps request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
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
        


class DescribeClusterInstanceGrpsResponse(AbstractModel):
    """DescribeClusterInstanceGrps response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instance groups
        :type TotalCount: int
        :param _InstanceGrpInfoList: Instance group list
        :type InstanceGrpInfoList: list of CynosdbInstanceGrp
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceGrpInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceGrpInfoList(self):
        return self._InstanceGrpInfoList

    @InstanceGrpInfoList.setter
    def InstanceGrpInfoList(self, InstanceGrpInfoList):
        self._InstanceGrpInfoList = InstanceGrpInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceGrpInfoList") is not None:
            self._InstanceGrpInfoList = []
            for item in params.get("InstanceGrpInfoList"):
                obj = CynosdbInstanceGrp()
                obj._deserialize(item)
                self._InstanceGrpInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterParamsRequest(AbstractModel):
    """DescribeClusterParams request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ParamName: Parameter name
        :type ParamName: str
        """
        self._ClusterId = None
        self._ParamName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ParamName = params.get("ParamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterParamsResponse(AbstractModel):
    """DescribeClusterParams response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of parameters
        :type TotalCount: int
        :param _Items: Instance parameter list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of ParamInfo
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
                obj = ParamInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterPasswordComplexityRequest(AbstractModel):
    """DescribeClusterPasswordComplexity request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
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
        


class DescribeClusterPasswordComplexityResponse(AbstractModel):
    """DescribeClusterPasswordComplexity response structure.

    """

    def __init__(self):
        r"""
        :param _ValidatePasswordDictionary: Data dictionary parameter Note: This field may return null, indicating that no valid values can be obtained.
        :type ValidatePasswordDictionary: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordLength: The length of the password Note: This field may return null, indicating that no valid values can be obtained.
        :type ValidatePasswordLength: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordMixedCaseCount: Number of case-sensitive characters Note: This field may return null, indicating that no valid values can be obtained.
        :type ValidatePasswordMixedCaseCount: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordNumberCount: Number of digits Note: This field may return null, indicating that no valid values can be obtained.
        :type ValidatePasswordNumberCount: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordPolicy: Password level Note: This field may return null, indicating that no valid values can be obtained.
        :type ValidatePasswordPolicy: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordSpecialCharCount: Number of symbols Note: This field may return null, indicating that no valid values can be obtained.
        :type ValidatePasswordSpecialCharCount: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ValidatePasswordDictionary = None
        self._ValidatePasswordLength = None
        self._ValidatePasswordMixedCaseCount = None
        self._ValidatePasswordNumberCount = None
        self._ValidatePasswordPolicy = None
        self._ValidatePasswordSpecialCharCount = None
        self._RequestId = None

    @property
    def ValidatePasswordDictionary(self):
        return self._ValidatePasswordDictionary

    @ValidatePasswordDictionary.setter
    def ValidatePasswordDictionary(self, ValidatePasswordDictionary):
        self._ValidatePasswordDictionary = ValidatePasswordDictionary

    @property
    def ValidatePasswordLength(self):
        return self._ValidatePasswordLength

    @ValidatePasswordLength.setter
    def ValidatePasswordLength(self, ValidatePasswordLength):
        self._ValidatePasswordLength = ValidatePasswordLength

    @property
    def ValidatePasswordMixedCaseCount(self):
        return self._ValidatePasswordMixedCaseCount

    @ValidatePasswordMixedCaseCount.setter
    def ValidatePasswordMixedCaseCount(self, ValidatePasswordMixedCaseCount):
        self._ValidatePasswordMixedCaseCount = ValidatePasswordMixedCaseCount

    @property
    def ValidatePasswordNumberCount(self):
        return self._ValidatePasswordNumberCount

    @ValidatePasswordNumberCount.setter
    def ValidatePasswordNumberCount(self, ValidatePasswordNumberCount):
        self._ValidatePasswordNumberCount = ValidatePasswordNumberCount

    @property
    def ValidatePasswordPolicy(self):
        return self._ValidatePasswordPolicy

    @ValidatePasswordPolicy.setter
    def ValidatePasswordPolicy(self, ValidatePasswordPolicy):
        self._ValidatePasswordPolicy = ValidatePasswordPolicy

    @property
    def ValidatePasswordSpecialCharCount(self):
        return self._ValidatePasswordSpecialCharCount

    @ValidatePasswordSpecialCharCount.setter
    def ValidatePasswordSpecialCharCount(self, ValidatePasswordSpecialCharCount):
        self._ValidatePasswordSpecialCharCount = ValidatePasswordSpecialCharCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ValidatePasswordDictionary") is not None:
            self._ValidatePasswordDictionary = ParamInfo()
            self._ValidatePasswordDictionary._deserialize(params.get("ValidatePasswordDictionary"))
        if params.get("ValidatePasswordLength") is not None:
            self._ValidatePasswordLength = ParamInfo()
            self._ValidatePasswordLength._deserialize(params.get("ValidatePasswordLength"))
        if params.get("ValidatePasswordMixedCaseCount") is not None:
            self._ValidatePasswordMixedCaseCount = ParamInfo()
            self._ValidatePasswordMixedCaseCount._deserialize(params.get("ValidatePasswordMixedCaseCount"))
        if params.get("ValidatePasswordNumberCount") is not None:
            self._ValidatePasswordNumberCount = ParamInfo()
            self._ValidatePasswordNumberCount._deserialize(params.get("ValidatePasswordNumberCount"))
        if params.get("ValidatePasswordPolicy") is not None:
            self._ValidatePasswordPolicy = ParamInfo()
            self._ValidatePasswordPolicy._deserialize(params.get("ValidatePasswordPolicy"))
        if params.get("ValidatePasswordSpecialCharCount") is not None:
            self._ValidatePasswordSpecialCharCount = ParamInfo()
            self._ValidatePasswordSpecialCharCount._deserialize(params.get("ValidatePasswordSpecialCharCount"))
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        r"""
        :param _DbType: Engine type. Currently, `MYSQL` is supported.
        :type DbType: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param _Offset: Record offset. Default value: 0
        :type Offset: int
        :param _OrderBy: Sort by field. Valid values:
<li> CREATETIME: creation time</li>
<li> PERIODENDTIME: expiration time</li>
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values:
<li> ASC: ascending</li>
<li> DESC: descending</li>
        :type OrderByType: str
        :param _Filters: Filter. If more than one filter exists, the logical relationship between these filters is `AND`.
        :type Filters: list of QueryFilter
        """
        self._DbType = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DbType = params.get("DbType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
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
        :param _TotalCount: Number of clusters
        :type TotalCount: int
        :param _ClusterSet: Cluster list
        :type ClusterSet: list of CynosdbCluster
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = CynosdbCluster()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance group ID
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
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group information
        :type Groups: list of SecurityGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task flow status. Valid values: `0` (succeeded), `1` (failed), `2` (Processing).
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeInstanceDetailRequest(AbstractModel):
    """DescribeInstanceDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
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
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Detail: Instance details
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbInstanceDetail`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Detail = None
        self._RequestId = None

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self._Detail = CynosdbInstanceDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceErrorLogsRequest(AbstractModel):
    """DescribeInstanceErrorLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Limit: Limit on the number of logs
        :type Limit: int
        :param _Offset: Offset of the log number
        :type Offset: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _OrderBy: Sorting field. Valid value: 'Timestamp'.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: `ASC`, `DESC`.
        :type OrderByType: str
        :param _LogLevels: Log level, which supports combo search by multiple levels. Valid values: `error`, `warning`, `note`.
        :type LogLevels: list of str
        :param _KeyWords: 
        :type KeyWords: list of str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._StartTime = None
        self._EndTime = None
        self._OrderBy = None
        self._OrderByType = None
        self._LogLevels = None
        self._KeyWords = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def LogLevels(self):
        return self._LogLevels

    @LogLevels.setter
    def LogLevels(self, LogLevels):
        self._LogLevels = LogLevels

    @property
    def KeyWords(self):
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._LogLevels = params.get("LogLevels")
        self._KeyWords = params.get("KeyWords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceErrorLogsResponse(AbstractModel):
    """DescribeInstanceErrorLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of logs Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ErrorLogs: Error log list Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorLogs: list of CynosdbErrorLogItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ErrorLogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ErrorLogs(self):
        return self._ErrorLogs

    @ErrorLogs.setter
    def ErrorLogs(self, ErrorLogs):
        self._ErrorLogs = ErrorLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ErrorLogs") is not None:
            self._ErrorLogs = []
            for item in params.get("ErrorLogs"):
                obj = CynosdbErrorLogItem()
                obj._deserialize(item)
                self._ErrorLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIds: Instance ID, which supports batch query.
        :type InstanceIds: list of str
        :param _ParamKeyword: Search condition for a parameter name, which supports fuzzy search.
        :type ParamKeyword: str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._ParamKeyword = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamKeyword(self):
        return self._ParamKeyword

    @ParamKeyword.setter
    def ParamKeyword(self, ParamKeyword):
        self._ParamKeyword = ParamKeyword


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        self._ParamKeyword = params.get("ParamKeyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams response structure.

    """

    def __init__(self):
        r"""
        :param _Items: List of instance parameters
        :type Items: list of InstanceParamItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceParamItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceSlowQueriesRequest(AbstractModel):
    """DescribeInstanceSlowQueries request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _StartTime: Transaction start time
        :type StartTime: str
        :param _EndTime: Transaction end time
        :type EndTime: str
        :param _Limit: Maximum number
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _Username: Username
        :type Username: str
        :param _Host: Client host
        :type Host: str
        :param _Database: Database name
        :type Database: str
        :param _OrderBy: Sorting field. Valid values: QueryTime, LockTime, RowsExamined, RowsSent.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: asc, desc.
        :type OrderByType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Username = None
        self._Host = None
        self._Database = None
        self._OrderBy = None
        self._OrderByType = None

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
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Username = params.get("Username")
        self._Host = params.get("Host")
        self._Database = params.get("Database")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSlowQueriesResponse(AbstractModel):
    """DescribeInstanceSlowQueries response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _SlowQueries: Slow query record
        :type SlowQueries: list of SlowQueriesItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowQueries = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowQueries(self):
        return self._SlowQueries

    @SlowQueries.setter
    def SlowQueries(self, SlowQueries):
        self._SlowQueries = SlowQueries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SlowQueries") is not None:
            self._SlowQueries = []
            for item in params.get("SlowQueries"):
                obj = SlowQueriesItem()
                obj._deserialize(item)
                self._SlowQueries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceSpecsRequest(AbstractModel):
    """DescribeInstanceSpecs request structure.

    """

    def __init__(self):
        r"""
        :param _DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        :param _IncludeZoneStocks: Whether to return the AZ information.
        :type IncludeZoneStocks: bool
        """
        self._DbType = None
        self._IncludeZoneStocks = None

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def IncludeZoneStocks(self):
        return self._IncludeZoneStocks

    @IncludeZoneStocks.setter
    def IncludeZoneStocks(self, IncludeZoneStocks):
        self._IncludeZoneStocks = IncludeZoneStocks


    def _deserialize(self, params):
        self._DbType = params.get("DbType")
        self._IncludeZoneStocks = params.get("IncludeZoneStocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSpecsResponse(AbstractModel):
    """DescribeInstanceSpecs response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceSpecSet: Specification information
        :type InstanceSpecSet: list of InstanceSpec
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceSpecSet = None
        self._RequestId = None

    @property
    def InstanceSpecSet(self):
        return self._InstanceSpecSet

    @InstanceSpecSet.setter
    def InstanceSpecSet(self, InstanceSpecSet):
        self._InstanceSpecSet = InstanceSpecSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceSpecSet") is not None:
            self._InstanceSpecSet = []
            for item in params.get("InstanceSpecSet"):
                obj = InstanceSpec()
                obj._deserialize(item)
                self._InstanceSpecSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100
        :type Limit: int
        :param _Offset: Record offset. Default value: 0
        :type Offset: int
        :param _OrderBy: Sort by field. Valid values:
<li> CREATETIME: creation time</li>
<li> PERIODENDTIME: expiration time</li>
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values:
<li> ASC: ascending</li>
<li> DESC: descending</li>
        :type OrderByType: str
        :param _Filters: Filter. If more than one filter exists, the logical relationship between these filters is `AND`.
        :type Filters: list of QueryFilter
        :param _DbType: Engine type. Currently, `MYSQL` is supported.
        :type DbType: str
        :param _Status: Instance status. Valid values:
creating
running
isolating
isolated
activating: Removing the instance from isolation
offlining: Eliminating the instance
offlined: Instance eliminated
        :type Status: str
        :param _InstanceIds: Instance ID list
        :type InstanceIds: list of str
        """
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None
        self._DbType = None
        self._Status = None
        self._InstanceIds = None

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DbType = params.get("DbType")
        self._Status = params.get("Status")
        self._InstanceIds = params.get("InstanceIds")
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
        :param _TotalCount: Number of instances
        :type TotalCount: int
        :param _InstanceSet: Instance list
        :type InstanceSet: list of CynosdbInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMaintainPeriodRequest(AbstractModel):
    """DescribeMaintainPeriod request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
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
        


class DescribeMaintainPeriodResponse(AbstractModel):
    """DescribeMaintainPeriod response structure.

    """

    def __init__(self):
        r"""
        :param _MaintainWeekDays: Maintenance days of the week
        :type MaintainWeekDays: list of str
        :param _MaintainStartTime: Maintenance start time in seconds
        :type MaintainStartTime: int
        :param _MaintainDuration: Maintenance duration in seconds
        :type MaintainDuration: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MaintainWeekDays = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._RequestId = None

    @property
    def MaintainWeekDays(self):
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays

    @property
    def MaintainStartTime(self):
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._RequestId = params.get("RequestId")


class DescribeParamTemplateDetailRequest(AbstractModel):
    """DescribeParamTemplateDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplateDetailResponse(AbstractModel):
    """DescribeParamTemplateDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID
        :type TemplateId: int
        :param _TemplateName: Parameter template name
        :type TemplateName: str
        :param _TemplateDescription: Parameter template description
        :type TemplateDescription: str
        :param _EngineVersion: Engine version
        :type EngineVersion: str
        :param _TotalCount: Total number of parameters
        :type TotalCount: int
        :param _Items: List of parameters
        :type Items: list of ParamDetail
        :param _DbMode: Database type. Valid values:  `NORMAL`, `SERVERLESS`.
        :type DbMode: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateDescription = None
        self._EngineVersion = None
        self._TotalCount = None
        self._Items = None
        self._DbMode = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

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
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateDescription = params.get("TemplateDescription")
        self._EngineVersion = params.get("EngineVersion")
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._DbMode = params.get("DbMode")
        self._RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _EngineVersions: Database engine version number
        :type EngineVersions: list of str
        :param _TemplateNames: Template name
        :type TemplateNames: list of str
        :param _TemplateIds: Template ID
        :type TemplateIds: list of int
        :param _DbModes: Database Type. Valid values: `NORMAL`, `SERVERLESS`.
        :type DbModes: list of str
        :param _Offset: Offset for query
        :type Offset: int
        :param _Limit: Limit on queries
        :type Limit: int
        :param _Products: Product type of the queried template
        :type Products: list of str
        :param _TemplateTypes: Template type
        :type TemplateTypes: list of str
        :param _EngineTypes: Version type
        :type EngineTypes: list of str
        :param _OrderBy: The sorting order of the returned results
        :type OrderBy: str
        :param _OrderDirection: Sorting order. Valid values: `desc`, `asc `.
        :type OrderDirection: str
        """
        self._EngineVersions = None
        self._TemplateNames = None
        self._TemplateIds = None
        self._DbModes = None
        self._Offset = None
        self._Limit = None
        self._Products = None
        self._TemplateTypes = None
        self._EngineTypes = None
        self._OrderBy = None
        self._OrderDirection = None

    @property
    def EngineVersions(self):
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions

    @property
    def TemplateNames(self):
        return self._TemplateNames

    @TemplateNames.setter
    def TemplateNames(self, TemplateNames):
        self._TemplateNames = TemplateNames

    @property
    def TemplateIds(self):
        return self._TemplateIds

    @TemplateIds.setter
    def TemplateIds(self, TemplateIds):
        self._TemplateIds = TemplateIds

    @property
    def DbModes(self):
        return self._DbModes

    @DbModes.setter
    def DbModes(self, DbModes):
        self._DbModes = DbModes

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
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def TemplateTypes(self):
        return self._TemplateTypes

    @TemplateTypes.setter
    def TemplateTypes(self, TemplateTypes):
        self._TemplateTypes = TemplateTypes

    @property
    def EngineTypes(self):
        return self._EngineTypes

    @EngineTypes.setter
    def EngineTypes(self, EngineTypes):
        self._EngineTypes = EngineTypes

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._EngineVersions = params.get("EngineVersions")
        self._TemplateNames = params.get("TemplateNames")
        self._TemplateIds = params.get("TemplateIds")
        self._DbModes = params.get("DbModes")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Products = params.get("Products")
        self._TemplateTypes = params.get("TemplateTypes")
        self._EngineTypes = params.get("EngineTypes")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of parameter templates
        :type TotalCount: int
        :param _Items: Parameter template information
        :type Items: list of ParamTemplateListInfo
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
                obj = ParamTemplateListInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Limit: Maximum entries returned per page
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _SearchKey: Search by keyword
        :type SearchKey: str
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._SearchKey = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group details
        :type Groups: list of SecurityGroup
        :param _Total: The total number of groups
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProxiesRequest(AbstractModel):
    """DescribeProxies request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Limit: Number of returned results. Default value: `20`. Maximum value: `100`,
        :type Limit: int
        :param _Offset: Record offset. Default value: `0`.
        :type Offset: int
        :param _OrderBy: Sorting field. Valid values:
<li> CREATETIME: Creation time</li>
<li> PERIODENDTIME: Expiration time</li>
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values:
<li> `ASC`: Ascending.</li>
<li> `DESC`: Descending</li>
        :type OrderByType: str
        :param _Filters: Filter. If there are more than one filter, the logical relationship between these filters is `AND`.
        :type Filters: list of QueryParamFilter
        """
        self._ClusterId = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryParamFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxiesResponse(AbstractModel):
    """DescribeProxies response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of database proxy groups
        :type TotalCount: int
        :param _ProxyGroupInfos: List of database proxy groups
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyGroupInfos: list of ProxyGroupInfo
        :param _ProxyNodeInfos: Database proxy node
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyNodeInfos: list of ProxyNodeInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProxyGroupInfos = None
        self._ProxyNodeInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProxyGroupInfos(self):
        return self._ProxyGroupInfos

    @ProxyGroupInfos.setter
    def ProxyGroupInfos(self, ProxyGroupInfos):
        self._ProxyGroupInfos = ProxyGroupInfos

    @property
    def ProxyNodeInfos(self):
        return self._ProxyNodeInfos

    @ProxyNodeInfos.setter
    def ProxyNodeInfos(self, ProxyNodeInfos):
        self._ProxyNodeInfos = ProxyNodeInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ProxyGroupInfos") is not None:
            self._ProxyGroupInfos = []
            for item in params.get("ProxyGroupInfos"):
                obj = ProxyGroupInfo()
                obj._deserialize(item)
                self._ProxyGroupInfos.append(obj)
        if params.get("ProxyNodeInfos") is not None:
            self._ProxyNodeInfos = []
            for item in params.get("ProxyNodeInfos"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self._ProxyNodeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxyNodesRequest(AbstractModel):
    """DescribeProxyNodes request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of returned results. Default value: `20`. Maximum value: `100`,
        :type Limit: int
        :param _Offset: Record offset. Default value: `0`.
        :type Offset: int
        :param _OrderBy: Sorting field. Valid values:
<li> CREATETIME: Creation time</li>
<li> PERIODENDTIME: Expiration time</li>
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values:
<li> `ASC`: Ascending.</li>
<li> `DESC`: Descending</li>
        :type OrderByType: str
        :param _Filters: Filter. If there are more than one filter, the logical relationship between these filters is `AND`.
        :type Filters: list of QueryFilter
        """
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyNodesResponse(AbstractModel):
    """DescribeProxyNodes response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of the database proxy nodes
        :type TotalCount: int
        :param _ProxyNodeInfos: List of the database proxy nodes
        :type ProxyNodeInfos: list of ProxyNodeInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProxyNodeInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProxyNodeInfos(self):
        return self._ProxyNodeInfos

    @ProxyNodeInfos.setter
    def ProxyNodeInfos(self, ProxyNodeInfos):
        self._ProxyNodeInfos = ProxyNodeInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ProxyNodeInfos") is not None:
            self._ProxyNodeInfos = []
            for item in params.get("ProxyNodeInfos"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self._ProxyNodeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxySpecsRequest(AbstractModel):
    """DescribeProxySpecs request structure.

    """


class DescribeProxySpecsResponse(AbstractModel):
    """DescribeProxySpecs response structure.

    """

    def __init__(self):
        r"""
        :param _ProxySpecs: List of database proxyspecifications
        :type ProxySpecs: list of ProxySpec
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxySpecs = None
        self._RequestId = None

    @property
    def ProxySpecs(self):
        return self._ProxySpecs

    @ProxySpecs.setter
    def ProxySpecs(self, ProxySpecs):
        self._ProxySpecs = ProxySpecs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProxySpecs") is not None:
            self._ProxySpecs = []
            for item in params.get("ProxySpecs"):
                obj = ProxySpec()
                obj._deserialize(item)
                self._ProxySpecs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcePackageDetailRequest(AbstractModel):
    """DescribeResourcePackageDetail request structure.

    """

    def __init__(self):
        r"""
        :param _PackageId: The unique ID of a resource pack
        :type PackageId: str
        :param _ClusterIds: Cluster ID
        :type ClusterIds: list of str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Offset: Offset
        :type Offset: str
        :param _Limit: Limit
        :type Limit: str
        :param _InstanceIds: Instance D
        :type InstanceIds: list of str
        """
        self._PackageId = None
        self._ClusterIds = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._InstanceIds = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

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
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._ClusterIds = params.get("ClusterIds")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcePackageDetailResponse(AbstractModel):
    """DescribeResourcePackageDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of deducted resource packs
        :type Total: int
        :param _Detail: Resource pack details
        :type Detail: list of PackageDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = PackageDetail()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcePackageListRequest(AbstractModel):
    """DescribeResourcePackageList request structure.

    """

    def __init__(self):
        r"""
        :param _PackageId: The unique ID of a resource pack
        :type PackageId: list of str
        :param _PackageName: Resource pack name
        :type PackageName: list of str
        :param _PackageType: Resource pack type. Valid values: `CCU` (compute resource pack), `DISK` (storage resource pack).
        :type PackageType: list of str
        :param _PackageRegion: Region of the resource pack. Valid values: `China` (Chinese mainland), `overseas` (outside Chinese mainland).
        :type PackageRegion: list of str
        :param _Status: Resource pack status. Valid values: `using`, `expired`, `normal_finish` (used up), `apply_refund` (requesting a refund), `refund` (refunded).
        :type Status: list of str
        :param _OrderBy: Sorting conditions. Valid values: `startTime` (effective time), `expireTime` (expiration date), `packageUsedSpec` (used capacity), `packageTotalSpec` (total storage capacity). 
Sorting by array order
        :type OrderBy: list of str
        :param _OrderDirection: Sorting order. Valid values: `ASC` (ascending), `DESC` (descending).
        :type OrderDirection: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Limit
        :type Limit: int
        """
        self._PackageId = None
        self._PackageName = None
        self._PackageType = None
        self._PackageRegion = None
        self._Status = None
        self._OrderBy = None
        self._OrderDirection = None
        self._Offset = None
        self._Limit = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

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
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        self._PackageType = params.get("PackageType")
        self._PackageRegion = params.get("PackageRegion")
        self._Status = params.get("Status")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcePackageListResponse(AbstractModel):
    """DescribeResourcePackageList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of resource packs
        :type Total: int
        :param _Detail: Resource pack details Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of Package
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = Package()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcePackageSaleSpecRequest(AbstractModel):
    """DescribeResourcePackageSaleSpec request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _PackageRegion: Region of the resource pack. Valid values: `China` (Chinese mainland), `overseas` (outside Chinese mainland).
        :type PackageRegion: str
        :param _PackageType: Resource pack type. Valid values: `CCU` (compute resource pack, `DISK` (storage resource pack).
        :type PackageType: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Limit
        :type Limit: int
        """
        self._InstanceType = None
        self._PackageRegion = None
        self._PackageType = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

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
        self._InstanceType = params.get("InstanceType")
        self._PackageRegion = params.get("PackageRegion")
        self._PackageType = params.get("PackageType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcePackageSaleSpecResponse(AbstractModel):
    """DescribeResourcePackageSaleSpec response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of available resource packs
        :type Total: int
        :param _Detail: Resource pack details Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of SalePackageSpec
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = SalePackageSpec()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesByDealNameRequest(AbstractModel):
    """DescribeResourcesByDealName request structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order ID. (If the cluster is not delivered yet, the `DescribeResourcesByDealName` API may return the `InvalidParameterValue.DealNameNotFound` error. Call the API again until it succeeds.)
        :type DealName: str
        :param _DealNames: Order ID, which can be used to query the resource information of multiple orders ID (If the cluster is not delivered yet, the `DescribeResourcesByDealName` API may return the `InvalidParameterValue.DealNameNotFound` error. Call the API again until it succeeds.)
        :type DealNames: list of str
        """
        self._DealName = None
        self._DealNames = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByDealNameResponse(AbstractModel):
    """DescribeResourcesByDealName response structure.

    """

    def __init__(self):
        r"""
        :param _BillingResourceInfos: Billable resource ID information array
        :type BillingResourceInfos: list of BillingResourceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BillingResourceInfos = None
        self._RequestId = None

    @property
    def BillingResourceInfos(self):
        return self._BillingResourceInfos

    @BillingResourceInfos.setter
    def BillingResourceInfos(self, BillingResourceInfos):
        self._BillingResourceInfos = BillingResourceInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BillingResourceInfos") is not None:
            self._BillingResourceInfos = []
            for item in params.get("BillingResourceInfos"):
                obj = BillingResourceInfo()
                obj._deserialize(item)
                self._BillingResourceInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRollbackTimeRangeRequest(AbstractModel):
    """DescribeRollbackTimeRange request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
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
        


class DescribeRollbackTimeRangeResponse(AbstractModel):
    """DescribeRollbackTimeRange response structure.

    """

    def __init__(self):
        r"""
        :param _TimeRangeStart: Start time of valid rollback time range (disused)
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeRangeStart: str
        :param _TimeRangeEnd: End time of valid rollback time range (disused)
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeRangeEnd: str
        :param _RollbackTimeRanges: Time range available for rollback
        :type RollbackTimeRanges: list of RollbackTimeRange
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TimeRangeStart = None
        self._TimeRangeEnd = None
        self._RollbackTimeRanges = None
        self._RequestId = None

    @property
    def TimeRangeStart(self):
        return self._TimeRangeStart

    @TimeRangeStart.setter
    def TimeRangeStart(self, TimeRangeStart):
        self._TimeRangeStart = TimeRangeStart

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

    @property
    def RollbackTimeRanges(self):
        return self._RollbackTimeRanges

    @RollbackTimeRanges.setter
    def RollbackTimeRanges(self, RollbackTimeRanges):
        self._RollbackTimeRanges = RollbackTimeRanges

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TimeRangeStart = params.get("TimeRangeStart")
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        if params.get("RollbackTimeRanges") is not None:
            self._RollbackTimeRanges = []
            for item in params.get("RollbackTimeRanges"):
                obj = RollbackTimeRange()
                obj._deserialize(item)
                self._RollbackTimeRanges.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRollbackTimeValidityRequest(AbstractModel):
    """DescribeRollbackTimeValidity request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ExpectTime: Expected time point to roll back to
        :type ExpectTime: str
        :param _ExpectTimeThresh: Error tolerance range for rollback time point
        :type ExpectTimeThresh: int
        """
        self._ClusterId = None
        self._ExpectTime = None
        self._ExpectTimeThresh = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ExpectTime(self):
        return self._ExpectTime

    @ExpectTime.setter
    def ExpectTime(self, ExpectTime):
        self._ExpectTime = ExpectTime

    @property
    def ExpectTimeThresh(self):
        return self._ExpectTimeThresh

    @ExpectTimeThresh.setter
    def ExpectTimeThresh(self, ExpectTimeThresh):
        self._ExpectTimeThresh = ExpectTimeThresh


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ExpectTime = params.get("ExpectTime")
        self._ExpectTimeThresh = params.get("ExpectTimeThresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeValidityResponse(AbstractModel):
    """DescribeRollbackTimeValidity response structure.

    """

    def __init__(self):
        r"""
        :param _PoolId: Storage `poolID`
        :type PoolId: int
        :param _QueryId: Rollback task ID, which needs to be passed in when rolling back to this time point
        :type QueryId: int
        :param _Status: Whether the time point is valid. pass: check passed; fail: check failed
        :type Status: str
        :param _SuggestTime: Suggested time point. This value takes effect only if `Status` is `fail`
        :type SuggestTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PoolId = None
        self._QueryId = None
        self._Status = None
        self._SuggestTime = None
        self._RequestId = None

    @property
    def PoolId(self):
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

    @property
    def QueryId(self):
        return self._QueryId

    @QueryId.setter
    def QueryId(self, QueryId):
        self._QueryId = QueryId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SuggestTime(self):
        return self._SuggestTime

    @SuggestTime.setter
    def SuggestTime(self, SuggestTime):
        self._SuggestTime = SuggestTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PoolId = params.get("PoolId")
        self._QueryId = params.get("QueryId")
        self._Status = params.get("Status")
        self._SuggestTime = params.get("SuggestTime")
        self._RequestId = params.get("RequestId")


class DescribeSupportProxyVersionRequest(AbstractModel):
    """DescribeSupportProxyVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        """
        self._ClusterId = None
        self._ProxyGroupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupportProxyVersionResponse(AbstractModel):
    """DescribeSupportProxyVersion response structure.

    """

    def __init__(self):
        r"""
        :param _SupportProxyVersions: Collection of supported database proxy versions
Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportProxyVersions: list of str
        :param _CurrentProxyVersion: The current proxy version
Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentProxyVersion: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SupportProxyVersions = None
        self._CurrentProxyVersion = None
        self._RequestId = None

    @property
    def SupportProxyVersions(self):
        return self._SupportProxyVersions

    @SupportProxyVersions.setter
    def SupportProxyVersions(self, SupportProxyVersions):
        self._SupportProxyVersions = SupportProxyVersions

    @property
    def CurrentProxyVersion(self):
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SupportProxyVersions = params.get("SupportProxyVersions")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """

    def __init__(self):
        r"""
        :param _IncludeVirtualZones: Whether the virtual zone is included.–
        :type IncludeVirtualZones: bool
        :param _ShowPermission: Whether to display all AZs in a region and the user’s permissions in each AZ.
        :type ShowPermission: bool
        """
        self._IncludeVirtualZones = None
        self._ShowPermission = None

    @property
    def IncludeVirtualZones(self):
        return self._IncludeVirtualZones

    @IncludeVirtualZones.setter
    def IncludeVirtualZones(self, IncludeVirtualZones):
        self._IncludeVirtualZones = IncludeVirtualZones

    @property
    def ShowPermission(self):
        return self._ShowPermission

    @ShowPermission.setter
    def ShowPermission(self, ShowPermission):
        self._ShowPermission = ShowPermission


    def _deserialize(self, params):
        self._IncludeVirtualZones = params.get("IncludeVirtualZones")
        self._ShowPermission = params.get("ShowPermission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param _RegionSet: Region information
        :type RegionSet: list of SaleRegion
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = SaleRegion()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class ErrorLogItemExport(AbstractModel):
    """The export format for an error log

    """

    def __init__(self):
        r"""
        :param _Timestamp: Time Note: This field may return null, indicating that no valid values can be obtained.
        :type Timestamp: str
        :param _Level: Log level. Valid values: `error`, `warning`, `note`. Note: This field may return null, indicating that no valid values can be obtained.
        :type Level: str
        :param _Content: Log content Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: str
        """
        self._Timestamp = None
        self._Level = None
        self._Content = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Level = params.get("Level")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInstanceErrorLogsRequest(AbstractModel):
    """ExportInstanceErrorLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _StartTime: Log start time
        :type StartTime: str
        :param _EndTime: Log end time
        :type EndTime: str
        :param _Limit: The max number of returned results
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _LogLevels: Log level
        :type LogLevels: list of str
        :param _KeyWords: 
        :type KeyWords: list of str
        :param _FileType: The template type. Valid values: `csv`, `original`.
        :type FileType: str
        :param _OrderBy: Valid value: `Timestamp`
        :type OrderBy: str
        :param _OrderByType: Valid values: `ASC` or `DESC`.
        :type OrderByType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._LogLevels = None
        self._KeyWords = None
        self._FileType = None
        self._OrderBy = None
        self._OrderByType = None

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
    def LogLevels(self):
        return self._LogLevels

    @LogLevels.setter
    def LogLevels(self, LogLevels):
        self._LogLevels = LogLevels

    @property
    def KeyWords(self):
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._LogLevels = params.get("LogLevels")
        self._KeyWords = params.get("KeyWords")
        self._FileType = params.get("FileType")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInstanceErrorLogsResponse(AbstractModel):
    """ExportInstanceErrorLogs response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorLogItems: Export content of the error log Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorLogItems: list of ErrorLogItemExport
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorLogItems = None
        self._RequestId = None

    @property
    def ErrorLogItems(self):
        return self._ErrorLogItems

    @ErrorLogItems.setter
    def ErrorLogItems(self, ErrorLogItems):
        self._ErrorLogItems = ErrorLogItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorLogItems") is not None:
            self._ErrorLogItems = []
            for item in params.get("ErrorLogItems"):
                obj = ErrorLogItemExport()
                obj._deserialize(item)
                self._ErrorLogItems.append(obj)
        self._RequestId = params.get("RequestId")


class ExportInstanceSlowQueriesRequest(AbstractModel):
    """ExportInstanceSlowQueries request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _StartTime: Transaction start time
        :type StartTime: str
        :param _EndTime: Transaction end time
        :type EndTime: str
        :param _Limit: Maximum number
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _Username: Username
        :type Username: str
        :param _Host: Client host
        :type Host: str
        :param _Database: Database name
        :type Database: str
        :param _FileType: File type. Valid values: csv, original.
        :type FileType: str
        :param _OrderBy: Sorting field. Valid values: `QueryTime`, `LockTime`, `RowsExamined`, and `RowsSent`.
        :type OrderBy: str
        :param _OrderByType: Sorting order. Valid values: `asc`, `desc`.
        :type OrderByType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Username = None
        self._Host = None
        self._Database = None
        self._FileType = None
        self._OrderBy = None
        self._OrderByType = None

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
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Username = params.get("Username")
        self._Host = params.get("Host")
        self._Database = params.get("Database")
        self._FileType = params.get("FileType")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInstanceSlowQueriesResponse(AbstractModel):
    """ExportInstanceSlowQueries response structure.

    """

    def __init__(self):
        r"""
        :param _FileContent: Slow query export content
        :type FileContent: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileContent = None
        self._RequestId = None

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._RequestId = params.get("RequestId")


class InputAccount(AbstractModel):
    """Account. Valid values: `accountName`, `host`.

    """

    def __init__(self):
        r"""
        :param _AccountName: Account
        :type AccountName: str
        :param _Host: Host. Default value: `%`
        :type Host: str
        """
        self._AccountName = None
        self._Host = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateRequest(AbstractModel):
    """InquirePriceCreate request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ
        :type Zone: str
        :param _GoodsNum: Number of compute node to purchase
        :type GoodsNum: int
        :param _InstancePayMode: Instance type for purchase. Valid values: `PREPAID`, `POSTPAID`, `SERVERLESS`.
        :type InstancePayMode: str
        :param _StoragePayMode: Storage type for purchase. Valid values: `PREPAID`, `POSTPAID`.
        :type StoragePayMode: str
        :param _DeviceType: device type:common, exclusive
        :type DeviceType: str
        :param _Cpu: Number of CPU cores, which is required when `InstancePayMode` is `PREPAID` or `POSTPAID`.
        :type Cpu: int
        :param _Memory: Memory size in GB, which is required when `InstancePayMode` is `PREPAID` or `POSTPAID`.
        :type Memory: int
        :param _Ccu: CCU size, which is required when `InstancePayMode` is `SERVERLESS`.
        :type Ccu: float
        :param _StorageLimit: Storage size, which is required when `StoragePayMode` is `PREPAID`.
        :type StorageLimit: int
        :param _TimeSpan: Validity period, which is required when `InstancePayMode` is `PREPAID`.
        :type TimeSpan: int
        :param _TimeUnit: Duration unit, which is required when `InstancePayMode` is `PREPAID`. Valid values: `m` (month), `d` (day).
        :type TimeUnit: str
        """
        self._Zone = None
        self._GoodsNum = None
        self._InstancePayMode = None
        self._StoragePayMode = None
        self._DeviceType = None
        self._Cpu = None
        self._Memory = None
        self._Ccu = None
        self._StorageLimit = None
        self._TimeSpan = None
        self._TimeUnit = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def InstancePayMode(self):
        return self._InstancePayMode

    @InstancePayMode.setter
    def InstancePayMode(self, InstancePayMode):
        self._InstancePayMode = InstancePayMode

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Ccu(self):
        return self._Ccu

    @Ccu.setter
    def Ccu(self, Ccu):
        self._Ccu = Ccu

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

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
        self._Zone = params.get("Zone")
        self._GoodsNum = params.get("GoodsNum")
        self._InstancePayMode = params.get("InstancePayMode")
        self._StoragePayMode = params.get("StoragePayMode")
        self._DeviceType = params.get("DeviceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Ccu = params.get("Ccu")
        self._StorageLimit = params.get("StorageLimit")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateResponse(AbstractModel):
    """InquirePriceCreate response structure.

    """

    def __init__(self):
        r"""
        :param _InstancePrice: Instance price
        :type InstancePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param _StoragePrice: Storage price
        :type StoragePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstancePrice = None
        self._StoragePrice = None
        self._RequestId = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def StoragePrice(self):
        return self._StoragePrice

    @StoragePrice.setter
    def StoragePrice(self, StoragePrice):
        self._StoragePrice = StoragePrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = TradePrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("StoragePrice") is not None:
            self._StoragePrice = TradePrice()
            self._StoragePrice._deserialize(params.get("StoragePrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceRenewRequest(AbstractModel):
    """InquirePriceRenew request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _TimeSpan: Validity period, which needs to be used together with `TimeUnit`.
        :type TimeSpan: int
        :param _TimeUnit: Unit of validity period, which needs to be used together with `TimeSpan`. Valid values: `d` (day), `m` (month).
        :type TimeUnit: str
        """
        self._ClusterId = None
        self._TimeSpan = None
        self._TimeUnit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        self._ClusterId = params.get("ClusterId")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewResponse(AbstractModel):
    """InquirePriceRenew response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIds: Instance ID list
        :type InstanceIds: list of str
        :param _Prices: Price of instance specification in array
        :type Prices: list of TradePrice
        :param _InstanceRealTotalPrice: Total renewal price of compute node
        :type InstanceRealTotalPrice: int
        :param _StorageRealTotalPrice: Total renewal price of storage node
        :type StorageRealTotalPrice: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._Prices = None
        self._InstanceRealTotalPrice = None
        self._StorageRealTotalPrice = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Prices(self):
        return self._Prices

    @Prices.setter
    def Prices(self, Prices):
        self._Prices = Prices

    @property
    def InstanceRealTotalPrice(self):
        return self._InstanceRealTotalPrice

    @InstanceRealTotalPrice.setter
    def InstanceRealTotalPrice(self, InstanceRealTotalPrice):
        self._InstanceRealTotalPrice = InstanceRealTotalPrice

    @property
    def StorageRealTotalPrice(self):
        return self._StorageRealTotalPrice

    @StorageRealTotalPrice.setter
    def StorageRealTotalPrice(self, StorageRealTotalPrice):
        self._StorageRealTotalPrice = StorageRealTotalPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Prices") is not None:
            self._Prices = []
            for item in params.get("Prices"):
                obj = TradePrice()
                obj._deserialize(item)
                self._Prices.append(obj)
        self._InstanceRealTotalPrice = params.get("InstanceRealTotalPrice")
        self._StorageRealTotalPrice = params.get("StorageRealTotalPrice")
        self._RequestId = params.get("RequestId")


class InstanceAuditRule(AbstractModel):
    """Audit rule details of the instance, which is an output parameter of the `DescribeAuditRuleWithInstanceIds` API.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _AuditRule: Whether the audit is rule audit. Valid values: `true` (rule audit), `false` (full audit).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuditRule: bool
        :param _AuditRuleFilters: Audit rule details, which is valid only when `AuditRule` is `true`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuditRuleFilters: list of AuditRuleFilters
        """
        self._InstanceId = None
        self._AuditRule = None
        self._AuditRuleFilters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AuditRule(self):
        return self._AuditRule

    @AuditRule.setter
    def AuditRule(self, AuditRule):
        self._AuditRule = AuditRule

    @property
    def AuditRuleFilters(self):
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AuditRule = params.get("AuditRule")
        if params.get("AuditRuleFilters") is not None:
            self._AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self._AuditRuleFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInitInfo(AbstractModel):
    """Instance initialization configuration information

    """

    def __init__(self):
        r"""
        :param _Cpu: Instance CPU
        :type Cpu: int
        :param _Memory: Instance memory
        :type Memory: int
        :param _InstanceType: Instance type. Valid values:`rw`, `ro`.
        :type InstanceType: str
        :param _InstanceCount: Number of the instances. Value range: 1-15.
        :type InstanceCount: int
        :param _MinRoCount: Minimum number of serverless instances. Value range: 1-15.
        :type MinRoCount: int
        :param _MaxRoCount: Maximum number of serverless instances. Value range: 1-15.
        :type MaxRoCount: int
        :param _MinRoCpu: Minimum specifications for serverless instance
        :type MinRoCpu: float
        :param _MaxRoCpu: Maximum specifications for serverless instance
        :type MaxRoCpu: float
        """
        self._Cpu = None
        self._Memory = None
        self._InstanceType = None
        self._InstanceCount = None
        self._MinRoCount = None
        self._MaxRoCount = None
        self._MinRoCpu = None
        self._MaxRoCpu = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def MinRoCount(self):
        return self._MinRoCount

    @MinRoCount.setter
    def MinRoCount(self, MinRoCount):
        self._MinRoCount = MinRoCount

    @property
    def MaxRoCount(self):
        return self._MaxRoCount

    @MaxRoCount.setter
    def MaxRoCount(self, MaxRoCount):
        self._MaxRoCount = MaxRoCount

    @property
    def MinRoCpu(self):
        return self._MinRoCpu

    @MinRoCpu.setter
    def MinRoCpu(self, MinRoCpu):
        self._MinRoCpu = MinRoCpu

    @property
    def MaxRoCpu(self):
        return self._MaxRoCpu

    @MaxRoCpu.setter
    def MaxRoCpu(self, MaxRoCpu):
        self._MaxRoCpu = MaxRoCpu


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._InstanceType = params.get("InstanceType")
        self._InstanceCount = params.get("InstanceCount")
        self._MinRoCount = params.get("MinRoCount")
        self._MaxRoCount = params.get("MaxRoCount")
        self._MinRoCpu = params.get("MinRoCpu")
        self._MaxRoCpu = params.get("MaxRoCpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetInfo(AbstractModel):
    """Instance network information

    """

    def __init__(self):
        r"""
        :param _InstanceGroupType: Network type
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceGroupType: str
        :param _InstanceGroupId: Instance group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceGroupId: str
        :param _VpcId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _NetType: Network type
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetType: int
        :param _Vip: VPC IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vip: str
        :param _Vport: VPC port
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vport: int
        :param _WanDomain: Public network domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanDomain: str
        :param _WanIP: 
        :type WanIP: str
        :param _WanPort: Public network port
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanPort: int
        :param _WanStatus: Public network status
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanStatus: str
        """
        self._InstanceGroupType = None
        self._InstanceGroupId = None
        self._VpcId = None
        self._SubnetId = None
        self._NetType = None
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._WanIP = None
        self._WanPort = None
        self._WanStatus = None

    @property
    def InstanceGroupType(self):
        return self._InstanceGroupType

    @InstanceGroupType.setter
    def InstanceGroupType(self, InstanceGroupType):
        self._InstanceGroupType = InstanceGroupType

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

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
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

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
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus


    def _deserialize(self, params):
        self._InstanceGroupType = params.get("InstanceGroupType")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._NetType = params.get("NetType")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._WanIP = params.get("WanIP")
        self._WanPort = params.get("WanPort")
        self._WanStatus = params.get("WanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParamItem(AbstractModel):
    """Instance parameter information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ParamsItems: List of instance parameters
        :type ParamsItems: list of ParamItemDetail
        """
        self._InstanceId = None
        self._ParamsItems = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ParamsItems(self):
        return self._ParamsItems

    @ParamsItems.setter
    def ParamsItems(self, ParamsItems):
        self._ParamsItems = ParamsItems


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ParamsItems") is not None:
            self._ParamsItems = []
            for item in params.get("ParamsItems"):
                obj = ParamItemDetail()
                obj._deserialize(item)
                self._ParamsItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSpec(AbstractModel):
    """Details of purchasable instance specifications. `Cpu` and `Memory` determine the instance specification during instance creation. The value range of the storage capacity is [MinStorageSize,MaxStorageSize]

    """

    def __init__(self):
        r"""
        :param _Cpu: Number of instance CPU cores
        :type Cpu: int
        :param _Memory: Instance memory in GB
        :type Memory: int
        :param _MaxStorageSize: Maximum instance storage capacity GB
        :type MaxStorageSize: int
        :param _MinStorageSize: Minimum instance storage capacity GB
        :type MinStorageSize: int
        :param _HasStock: Whether there is an inventory.
        :type HasStock: bool
        :param _MachineType: Machine type
        :type MachineType: str
        :param _MaxIops: Maximum IOPS
        :type MaxIops: int
        :param _MaxIoBandWidth: Maximum bandwidth
        :type MaxIoBandWidth: int
        :param _ZoneStockInfos: Inventory information in a region
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneStockInfos: list of ZoneStockInfo
        :param _StockCount: Quantity in stock
Note: This field may return null, indicating that no valid values can be obtained.
        :type StockCount: int
        """
        self._Cpu = None
        self._Memory = None
        self._MaxStorageSize = None
        self._MinStorageSize = None
        self._HasStock = None
        self._MachineType = None
        self._MaxIops = None
        self._MaxIoBandWidth = None
        self._ZoneStockInfos = None
        self._StockCount = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def MaxStorageSize(self):
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def MinStorageSize(self):
        return self._MinStorageSize

    @MinStorageSize.setter
    def MinStorageSize(self, MinStorageSize):
        self._MinStorageSize = MinStorageSize

    @property
    def HasStock(self):
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MaxIops(self):
        return self._MaxIops

    @MaxIops.setter
    def MaxIops(self, MaxIops):
        self._MaxIops = MaxIops

    @property
    def MaxIoBandWidth(self):
        return self._MaxIoBandWidth

    @MaxIoBandWidth.setter
    def MaxIoBandWidth(self, MaxIoBandWidth):
        self._MaxIoBandWidth = MaxIoBandWidth

    @property
    def ZoneStockInfos(self):
        return self._ZoneStockInfos

    @ZoneStockInfos.setter
    def ZoneStockInfos(self, ZoneStockInfos):
        self._ZoneStockInfos = ZoneStockInfos

    @property
    def StockCount(self):
        return self._StockCount

    @StockCount.setter
    def StockCount(self, StockCount):
        self._StockCount = StockCount


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._MaxStorageSize = params.get("MaxStorageSize")
        self._MinStorageSize = params.get("MinStorageSize")
        self._HasStock = params.get("HasStock")
        self._MachineType = params.get("MachineType")
        self._MaxIops = params.get("MaxIops")
        self._MaxIoBandWidth = params.get("MaxIoBandWidth")
        if params.get("ZoneStockInfos") is not None:
            self._ZoneStockInfos = []
            for item in params.get("ZoneStockInfos"):
                obj = ZoneStockInfo()
                obj._deserialize(item)
                self._ZoneStockInfos.append(obj)
        self._StockCount = params.get("StockCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterRequest(AbstractModel):
    """IsolateCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _DbType: This parameter has been disused.
        :type DbType: str
        """
        self._ClusterId = None
        self._DbType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterResponse(AbstractModel):
    """IsolateCluster response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _DealNames: Refund order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._DealNames = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class IsolateInstanceRequest(AbstractModel):
    """IsolateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIdList: Instance ID array
        :type InstanceIdList: list of str
        :param _DbType: This parameter has been disused.
        :type DbType: str
        """
        self._ClusterId = None
        self._InstanceIdList = None
        self._DbType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdList = params.get("InstanceIdList")
        self._DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateInstanceResponse(AbstractModel):
    """IsolateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _DealNames: Order ID for isolated instance (prepaid instance)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._DealNames = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class ModifiableInfo(AbstractModel):
    """Details of whether the parameter can be modified

    """


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription request structure.

    """

    def __init__(self):
        r"""
        :param _AccountName: Database account name
        :type AccountName: str
        :param _Description: Database account description
        :type Description: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Host: Host. Default value: `%`
        :type Host: str
        """
        self._AccountName = None
        self._Description = None
        self._ClusterId = None
        self._Host = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._Description = params.get("Description")
        self._ClusterId = params.get("ClusterId")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription response structure.

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


class ModifyAccountHostRequest(AbstractModel):
    """ModifyAccountHost request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NewHost: New host
        :type NewHost: str
        :param _Account: Account infomation
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        """
        self._ClusterId = None
        self._NewHost = None
        self._Account = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NewHost(self):
        return self._NewHost

    @NewHost.setter
    def NewHost(self, NewHost):
        self._NewHost = NewHost

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NewHost = params.get("NewHost")
        if params.get("Account") is not None:
            self._Account = InputAccount()
            self._Account._deserialize(params.get("Account"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountHostResponse(AbstractModel):
    """ModifyAccountHost response structure.

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


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Account: Account infomation
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        :param _GlobalPrivileges: Array of global permissions
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: Array of database permissions
        :type DatabasePrivileges: list of DatabasePrivileges
        :param _TablePrivileges: Array of table permissions
        :type TablePrivileges: list of TablePrivileges
        """
        self._ClusterId = None
        self._Account = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def GlobalPrivileges(self):
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self._Account = InputAccount()
            self._Account._deserialize(params.get("Account"))
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivileges()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivileges()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges response structure.

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


class ModifyAuditRuleTemplatesRequest(AbstractModel):
    """ModifyAuditRuleTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _RuleTemplateIds: Audit rule template ID
        :type RuleTemplateIds: list of str
        :param _RuleFilters: Audit rule after modification
        :type RuleFilters: list of RuleFilters
        :param _RuleTemplateName: New name of the rule template
        :type RuleTemplateName: str
        :param _Description: New description of the rule template
        :type Description: str
        """
        self._RuleTemplateIds = None
        self._RuleFilters = None
        self._RuleTemplateName = None
        self._Description = None

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def RuleTemplateName(self):
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._RuleTemplateName = params.get("RuleTemplateName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditRuleTemplatesResponse(AbstractModel):
    """ModifyAuditRuleTemplates response structure.

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


class ModifyAuditServiceRequest(AbstractModel):
    """ModifyAuditService request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _LogExpireDay: Log retention period
        :type LogExpireDay: int
        :param _HighLogExpireDay: Frequent log retention period
        :type HighLogExpireDay: int
        :param _AuditAll: The parameter used to change the audit rule of the instance to full audit
        :type AuditAll: bool
        :param _AuditRuleFilters: Rule audit
        :type AuditRuleFilters: list of AuditRuleFilters
        :param _RuleTemplateIds: Rule template ID
        :type RuleTemplateIds: list of str
        """
        self._InstanceId = None
        self._LogExpireDay = None
        self._HighLogExpireDay = None
        self._AuditAll = None
        self._AuditRuleFilters = None
        self._RuleTemplateIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HighLogExpireDay(self):
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay

    @property
    def AuditAll(self):
        return self._AuditAll

    @AuditAll.setter
    def AuditAll(self, AuditAll):
        self._AuditAll = AuditAll

    @property
    def AuditRuleFilters(self):
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._HighLogExpireDay = params.get("HighLogExpireDay")
        self._AuditAll = params.get("AuditAll")
        if params.get("AuditRuleFilters") is not None:
            self._AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self._AuditRuleFilters.append(obj)
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditServiceResponse(AbstractModel):
    """ModifyAuditService response structure.

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


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _BackupTimeBeg: Full backup start time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively
        :type BackupTimeBeg: int
        :param _BackupTimeEnd: Full backup end time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively.
        :type BackupTimeEnd: int
        :param _ReserveDuration: Backup retention period in seconds. Backups will be cleared after this period elapses. 7 days is represented by 3600*24*7 = 604800. Maximum value: 158112000.
        :type ReserveDuration: int
        :param _BackupFreq: Backup frequency. It is an array of 7 elements corresponding to Monday through Sunday. full: full backup; increment: incremental backup. This parameter cannot be modified currently and doesn't need to be entered.
        :type BackupFreq: list of str
        :param _BackupType: Backup mode. logic: logic backup; snapshot: snapshot backup. This parameter cannot be modified currently and doesn't need to be entered.
        :type BackupType: str
        """
        self._ClusterId = None
        self._BackupTimeBeg = None
        self._BackupTimeEnd = None
        self._ReserveDuration = None
        self._BackupFreq = None
        self._BackupType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupTimeBeg(self):
        return self._BackupTimeBeg

    @BackupTimeBeg.setter
    def BackupTimeBeg(self, BackupTimeBeg):
        self._BackupTimeBeg = BackupTimeBeg

    @property
    def BackupTimeEnd(self):
        return self._BackupTimeEnd

    @BackupTimeEnd.setter
    def BackupTimeEnd(self, BackupTimeEnd):
        self._BackupTimeEnd = BackupTimeEnd

    @property
    def ReserveDuration(self):
        return self._ReserveDuration

    @ReserveDuration.setter
    def ReserveDuration(self, ReserveDuration):
        self._ReserveDuration = ReserveDuration

    @property
    def BackupFreq(self):
        return self._BackupFreq

    @BackupFreq.setter
    def BackupFreq(self, BackupFreq):
        self._BackupFreq = BackupFreq

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupTimeBeg = params.get("BackupTimeBeg")
        self._BackupTimeEnd = params.get("BackupTimeEnd")
        self._ReserveDuration = params.get("ReserveDuration")
        self._BackupFreq = params.get("BackupFreq")
        self._BackupType = params.get("BackupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig response structure.

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


class ModifyBackupNameRequest(AbstractModel):
    """ModifyBackupName request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _BackupId: Backup file ID
        :type BackupId: int
        :param _BackupName: Backup name, which can contain up to 60 characters.
        :type BackupName: str
        """
        self._ClusterId = None
        self._BackupId = None
        self._BackupName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupId = params.get("BackupId")
        self._BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupNameResponse(AbstractModel):
    """ModifyBackupName response structure.

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


class ModifyBinlogSaveDaysRequest(AbstractModel):
    """ModifyBinlogSaveDays request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _BinlogSaveDays: Binlog retention period in days
        :type BinlogSaveDays: int
        """
        self._ClusterId = None
        self._BinlogSaveDays = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BinlogSaveDays(self):
        return self._BinlogSaveDays

    @BinlogSaveDays.setter
    def BinlogSaveDays(self, BinlogSaveDays):
        self._BinlogSaveDays = BinlogSaveDays


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BinlogSaveDays = params.get("BinlogSaveDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBinlogSaveDaysResponse(AbstractModel):
    """ModifyBinlogSaveDays response structure.

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


class ModifyClusterDatabaseRequest(AbstractModel):
    """ModifyClusterDatabase request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _DbName: Database name
        :type DbName: str
        :param _NewUserHostPrivileges: Host permissions of the new authorized user
        :type NewUserHostPrivileges: list of UserHostPrivilege
        :param _Description: Remarks
        :type Description: str
        :param _OldUserHostPrivileges: Host permissions of previously authorized users
        :type OldUserHostPrivileges: list of UserHostPrivilege
        """
        self._ClusterId = None
        self._DbName = None
        self._NewUserHostPrivileges = None
        self._Description = None
        self._OldUserHostPrivileges = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def NewUserHostPrivileges(self):
        return self._NewUserHostPrivileges

    @NewUserHostPrivileges.setter
    def NewUserHostPrivileges(self, NewUserHostPrivileges):
        self._NewUserHostPrivileges = NewUserHostPrivileges

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OldUserHostPrivileges(self):
        return self._OldUserHostPrivileges

    @OldUserHostPrivileges.setter
    def OldUserHostPrivileges(self, OldUserHostPrivileges):
        self._OldUserHostPrivileges = OldUserHostPrivileges


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DbName = params.get("DbName")
        if params.get("NewUserHostPrivileges") is not None:
            self._NewUserHostPrivileges = []
            for item in params.get("NewUserHostPrivileges"):
                obj = UserHostPrivilege()
                obj._deserialize(item)
                self._NewUserHostPrivileges.append(obj)
        self._Description = params.get("Description")
        if params.get("OldUserHostPrivileges") is not None:
            self._OldUserHostPrivileges = []
            for item in params.get("OldUserHostPrivileges"):
                obj = UserHostPrivilege()
                obj._deserialize(item)
                self._OldUserHostPrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterDatabaseResponse(AbstractModel):
    """ModifyClusterDatabase response structure.

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


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterName: Cluster name
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


class ModifyClusterParamRequest(AbstractModel):
    """ModifyClusterParam request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ParamList: List of the parameters to be modified. Each element in the list is a combination of `ParamName`, `CurrentValue`, and `OldValue`. `ParamName` is the parameter name; `CurrentValue` is the current value; `OldValue` is the old value that doesn’t need to be verified.
        :type ParamList: list of ParamItem
        :param _IsInMaintainPeriod: Valid values: `yes` (execute during maintenance time), `no` (execute now)
        :type IsInMaintainPeriod: str
        """
        self._ClusterId = None
        self._ParamList = None
        self._IsInMaintainPeriod = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamItem()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterParamResponse(AbstractModel):
    """ModifyClusterParam response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async request ID used to query the result
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


class ModifyClusterPasswordComplexityRequest(AbstractModel):
    """ModifyClusterPasswordComplexity request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ValidatePasswordLength: Password length
        :type ValidatePasswordLength: int
        :param _ValidatePasswordMixedCaseCount: Number of letters
        :type ValidatePasswordMixedCaseCount: int
        :param _ValidatePasswordSpecialCharCount: Number of symbols
        :type ValidatePasswordSpecialCharCount: int
        :param _ValidatePasswordNumberCount: Number of digits
        :type ValidatePasswordNumberCount: int
        :param _ValidatePasswordPolicy: Password strength. Valid values: `MEDIUM`, `STRONG`.
        :type ValidatePasswordPolicy: str
        :param _ValidatePasswordDictionary: Data dictionary
        :type ValidatePasswordDictionary: list of str
        """
        self._ClusterId = None
        self._ValidatePasswordLength = None
        self._ValidatePasswordMixedCaseCount = None
        self._ValidatePasswordSpecialCharCount = None
        self._ValidatePasswordNumberCount = None
        self._ValidatePasswordPolicy = None
        self._ValidatePasswordDictionary = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ValidatePasswordLength(self):
        return self._ValidatePasswordLength

    @ValidatePasswordLength.setter
    def ValidatePasswordLength(self, ValidatePasswordLength):
        self._ValidatePasswordLength = ValidatePasswordLength

    @property
    def ValidatePasswordMixedCaseCount(self):
        return self._ValidatePasswordMixedCaseCount

    @ValidatePasswordMixedCaseCount.setter
    def ValidatePasswordMixedCaseCount(self, ValidatePasswordMixedCaseCount):
        self._ValidatePasswordMixedCaseCount = ValidatePasswordMixedCaseCount

    @property
    def ValidatePasswordSpecialCharCount(self):
        return self._ValidatePasswordSpecialCharCount

    @ValidatePasswordSpecialCharCount.setter
    def ValidatePasswordSpecialCharCount(self, ValidatePasswordSpecialCharCount):
        self._ValidatePasswordSpecialCharCount = ValidatePasswordSpecialCharCount

    @property
    def ValidatePasswordNumberCount(self):
        return self._ValidatePasswordNumberCount

    @ValidatePasswordNumberCount.setter
    def ValidatePasswordNumberCount(self, ValidatePasswordNumberCount):
        self._ValidatePasswordNumberCount = ValidatePasswordNumberCount

    @property
    def ValidatePasswordPolicy(self):
        return self._ValidatePasswordPolicy

    @ValidatePasswordPolicy.setter
    def ValidatePasswordPolicy(self, ValidatePasswordPolicy):
        self._ValidatePasswordPolicy = ValidatePasswordPolicy

    @property
    def ValidatePasswordDictionary(self):
        return self._ValidatePasswordDictionary

    @ValidatePasswordDictionary.setter
    def ValidatePasswordDictionary(self, ValidatePasswordDictionary):
        self._ValidatePasswordDictionary = ValidatePasswordDictionary


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ValidatePasswordLength = params.get("ValidatePasswordLength")
        self._ValidatePasswordMixedCaseCount = params.get("ValidatePasswordMixedCaseCount")
        self._ValidatePasswordSpecialCharCount = params.get("ValidatePasswordSpecialCharCount")
        self._ValidatePasswordNumberCount = params.get("ValidatePasswordNumberCount")
        self._ValidatePasswordPolicy = params.get("ValidatePasswordPolicy")
        self._ValidatePasswordDictionary = params.get("ValidatePasswordDictionary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterPasswordComplexityResponse(AbstractModel):
    """ModifyClusterPasswordComplexity response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyClusterSlaveZoneRequest(AbstractModel):
    """ModifyClusterSlaveZone request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _OldSlaveZone: Old replica AZ
        :type OldSlaveZone: str
        :param _NewSlaveZone: New replica AZ
        :type NewSlaveZone: str
        """
        self._ClusterId = None
        self._OldSlaveZone = None
        self._NewSlaveZone = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def OldSlaveZone(self):
        return self._OldSlaveZone

    @OldSlaveZone.setter
    def OldSlaveZone(self, OldSlaveZone):
        self._OldSlaveZone = OldSlaveZone

    @property
    def NewSlaveZone(self):
        return self._NewSlaveZone

    @NewSlaveZone.setter
    def NewSlaveZone(self, NewSlaveZone):
        self._NewSlaveZone = NewSlaveZone


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._OldSlaveZone = params.get("OldSlaveZone")
        self._NewSlaveZone = params.get("NewSlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterSlaveZoneResponse(AbstractModel):
    """ModifyClusterSlaveZone response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async FlowId
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance group ID
        :type InstanceId: str
        :param _SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.
        :type SecurityGroupIds: list of str
        :param _Zone: AZ
        :type Zone: str
        """
        self._InstanceId = None
        self._SecurityGroupIds = None
        self._Zone = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups response structure.

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


class ModifyInstanceNameRequest(AbstractModel):
    """ModifyInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
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
        


class ModifyInstanceNameResponse(AbstractModel):
    """ModifyInstanceName response structure.

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


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIds: Instance ID
        :type InstanceIds: list of str
        :param _ClusterParamList: List of cluster parameters
        :type ClusterParamList: list of ModifyParamItem
        :param _InstanceParamList: List of the instance parameters
        :type InstanceParamList: list of ModifyParamItem
        :param _IsInMaintainPeriod: Valid values: `yes` (modify in maintenance window),  `no`  (execute now by default).
        :type IsInMaintainPeriod: str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._ClusterParamList = None
        self._InstanceParamList = None
        self._IsInMaintainPeriod = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClusterParamList(self):
        return self._ClusterParamList

    @ClusterParamList.setter
    def ClusterParamList(self, ClusterParamList):
        self._ClusterParamList = ClusterParamList

    @property
    def InstanceParamList(self):
        return self._InstanceParamList

    @InstanceParamList.setter
    def InstanceParamList(self, InstanceParamList):
        self._InstanceParamList = InstanceParamList

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ClusterParamList") is not None:
            self._ClusterParamList = []
            for item in params.get("ClusterParamList"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._ClusterParamList.append(obj)
        if params.get("InstanceParamList") is not None:
            self._InstanceParamList = []
            for item in params.get("InstanceParamList"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._InstanceParamList.append(obj)
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyMaintainPeriodConfigRequest(AbstractModel):
    """ModifyMaintainPeriodConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _MaintainStartTime: Maintenance start time in seconds. For example, 03:00 AM is represented by 10800
        :type MaintainStartTime: int
        :param _MaintainDuration: Maintenance duration in seconds. For example, one hour is represented by 3600
        :type MaintainDuration: int
        :param _MaintainWeekDays: Maintenance days of the week. Valid values: [Mon, Tue, Wed, Thu, Fri, Sat, Sun].
        :type MaintainWeekDays: list of str
        """
        self._InstanceId = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._MaintainWeekDays = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MaintainStartTime(self):
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintainPeriodConfigResponse(AbstractModel):
    """ModifyMaintainPeriodConfig response structure.

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


class ModifyParamItem(AbstractModel):
    """Information of the modified instance parameter

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _CurrentValue: Current parameter value
        :type CurrentValue: str
        :param _OldValue: Old parameter value, which is used only in output parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OldValue: str
        """
        self._ParamName = None
        self._CurrentValue = None
        self._OldValue = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._CurrentValue = params.get("CurrentValue")
        self._OldValue = params.get("OldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID
        :type TemplateId: int
        :param _TemplateName: Template name
        :type TemplateName: str
        :param _TemplateDescription: Template description
        :type TemplateDescription: str
        :param _ParamList: Parameter list
        :type ParamList: list of ModifyParamItem
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateDescription = None
        self._ParamList = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateDescription = params.get("TemplateDescription")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateResponse(AbstractModel):
    """ModifyParamTemplate response structure.

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


class ModifyProxyDescRequest(AbstractModel):
    """ModifyProxyDesc request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        :param _Description: Database proxy description
        :type Description: str
        """
        self._ClusterId = None
        self._ProxyGroupId = None
        self._Description = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyDescResponse(AbstractModel):
    """ModifyProxyDesc response structure.

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


class ModifyProxyRwSplitRequest(AbstractModel):
    """ModifyProxyRwSplit request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        :param _ConsistencyType: Consistency type. Valid values: `eventual` (eventual consistency), `session` (session consistency), `global` (global consistency).
        :type ConsistencyType: str
        :param _ConsistencyTimeOut: Consistency timeout period
        :type ConsistencyTimeOut: str
        :param _WeightMode: Assignment mode of read/write weights. Valid values: `system` (auto-assigned), `custom`
        :type WeightMode: str
        :param _InstanceWeights: Read-Only weight of an instance
        :type InstanceWeights: list of ProxyInstanceWeight
        :param _FailOver: Whether to enable failover. If it is enabled, the connection address will route requests to the source instance in case of proxy failure. Valid values: `true`, `false`.
        :type FailOver: str
        :param _AutoAddRo: Whether to automatically add read-only instances. Valid values: `true`, `false`
        :type AutoAddRo: str
        :param _OpenRw: Whether to enable read/write separation
        :type OpenRw: str
        :param _RwType: Read/Write type. Valid values:
`READWRITE`, `READONLY`.
        :type RwType: str
        :param _TransSplit: Transaction split
        :type TransSplit: bool
        :param _AccessMode: Connection mode. Valid values:
`nearby`, `balance`.
        :type AccessMode: str
        :param _OpenConnectionPool: Whether to enable the connection pool. Valid values: 
`yes`, `no`.
        :type OpenConnectionPool: str
        :param _ConnectionPoolType: Connection pool type. Valid values:
`ConnectionPoolType`, `SessionConnectionPool`.
        :type ConnectionPoolType: str
        :param _ConnectionPoolTimeOut: Connection persistence timeout
        :type ConnectionPoolTimeOut: int
        """
        self._ClusterId = None
        self._ProxyGroupId = None
        self._ConsistencyType = None
        self._ConsistencyTimeOut = None
        self._WeightMode = None
        self._InstanceWeights = None
        self._FailOver = None
        self._AutoAddRo = None
        self._OpenRw = None
        self._RwType = None
        self._TransSplit = None
        self._AccessMode = None
        self._OpenConnectionPool = None
        self._ConnectionPoolType = None
        self._ConnectionPoolTimeOut = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ConsistencyType(self):
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def ConsistencyTimeOut(self):
        return self._ConsistencyTimeOut

    @ConsistencyTimeOut.setter
    def ConsistencyTimeOut(self, ConsistencyTimeOut):
        self._ConsistencyTimeOut = ConsistencyTimeOut

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def InstanceWeights(self):
        return self._InstanceWeights

    @InstanceWeights.setter
    def InstanceWeights(self, InstanceWeights):
        self._InstanceWeights = InstanceWeights

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def OpenRw(self):
        return self._OpenRw

    @OpenRw.setter
    def OpenRw(self, OpenRw):
        self._OpenRw = OpenRw

    @property
    def RwType(self):
        return self._RwType

    @RwType.setter
    def RwType(self, RwType):
        self._RwType = RwType

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def AccessMode(self):
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def OpenConnectionPool(self):
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def ConnectionPoolTimeOut(self):
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ConsistencyType = params.get("ConsistencyType")
        self._ConsistencyTimeOut = params.get("ConsistencyTimeOut")
        self._WeightMode = params.get("WeightMode")
        if params.get("InstanceWeights") is not None:
            self._InstanceWeights = []
            for item in params.get("InstanceWeights"):
                obj = ProxyInstanceWeight()
                obj._deserialize(item)
                self._InstanceWeights.append(obj)
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        self._OpenRw = params.get("OpenRw")
        self._RwType = params.get("RwType")
        self._TransSplit = params.get("TransSplit")
        self._AccessMode = params.get("AccessMode")
        self._OpenConnectionPool = params.get("OpenConnectionPool")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        self._ConnectionPoolTimeOut = params.get("ConnectionPoolTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyRwSplitResponse(AbstractModel):
    """ModifyProxyRwSplit response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async FlowId
        :type FlowId: int
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyResourcePackageClustersRequest(AbstractModel):
    """ModifyResourcePackageClusters request structure.

    """

    def __init__(self):
        r"""
        :param _PackageId: The unique ID of a resource pack
        :type PackageId: str
        :param _BindClusterIds: ID of the cluster to be bound
        :type BindClusterIds: list of str
        :param _UnbindClusterIds: ID of the cluster to be unbound
        :type UnbindClusterIds: list of str
        """
        self._PackageId = None
        self._BindClusterIds = None
        self._UnbindClusterIds = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def BindClusterIds(self):
        return self._BindClusterIds

    @BindClusterIds.setter
    def BindClusterIds(self, BindClusterIds):
        self._BindClusterIds = BindClusterIds

    @property
    def UnbindClusterIds(self):
        return self._UnbindClusterIds

    @UnbindClusterIds.setter
    def UnbindClusterIds(self, UnbindClusterIds):
        self._UnbindClusterIds = UnbindClusterIds


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._BindClusterIds = params.get("BindClusterIds")
        self._UnbindClusterIds = params.get("UnbindClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcePackageClustersResponse(AbstractModel):
    """ModifyResourcePackageClusters response structure.

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


class ModifyResourcePackageNameRequest(AbstractModel):
    """ModifyResourcePackageName request structure.

    """

    def __init__(self):
        r"""
        :param _PackageId: The unique ID of a resource pack
        :type PackageId: str
        :param _PackageName: Custom resource pack name, which can contains up to 120 characters.
        :type PackageName: str
        """
        self._PackageId = None
        self._PackageName = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcePackageNameResponse(AbstractModel):
    """ModifyResourcePackageName response structure.

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


class ModifyVipVportRequest(AbstractModel):
    """ModifyVipVport request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceGrpId: Instance group ID
        :type InstanceGrpId: str
        :param _Vip: Target IP to be modified
        :type Vip: str
        :param _Vport: Target port to be modified
        :type Vport: int
        :param _DbType: Database type. Valid values: 
<li> MYSQL </li>
        :type DbType: str
        :param _OldIpReserveHours: Valid hours of old IPs. If it is set to `0` hours, the IPs will be released immediately.
        :type OldIpReserveHours: int
        """
        self._ClusterId = None
        self._InstanceGrpId = None
        self._Vip = None
        self._Vport = None
        self._DbType = None
        self._OldIpReserveHours = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceGrpId(self):
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        self._InstanceGrpId = InstanceGrpId

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
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def OldIpReserveHours(self):
        return self._OldIpReserveHours

    @OldIpReserveHours.setter
    def OldIpReserveHours(self, OldIpReserveHours):
        self._OldIpReserveHours = OldIpReserveHours


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceGrpId = params.get("InstanceGrpId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._DbType = params.get("DbType")
        self._OldIpReserveHours = params.get("OldIpReserveHours")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVipVportResponse(AbstractModel):
    """ModifyVipVport response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class Module(AbstractModel):
    """Modules supported by the system

    """

    def __init__(self):
        r"""
        :param _IsDisable: Whether it is supported. Valid values: `yes`, `no`.
        :type IsDisable: str
        :param _ModuleName: Module name
        :type ModuleName: str
        """
        self._IsDisable = None
        self._ModuleName = None

    @property
    def IsDisable(self):
        return self._IsDisable

    @IsDisable.setter
    def IsDisable(self, IsDisable):
        self._IsDisable = IsDisable

    @property
    def ModuleName(self):
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName


    def _deserialize(self, params):
        self._IsDisable = params.get("IsDisable")
        self._ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetAddr(AbstractModel):
    """Network information

    """

    def __init__(self):
        r"""
        :param _Vip: Private network IP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Vip: str
        :param _Vport: Private network port number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Vport: int
        :param _WanDomain: Public network domain name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WanDomain: str
        :param _WanPort: Public network port number
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WanPort: int
        :param _NetType: Network type. Valid values: `ro` (read-only), `rw` or `ha` (read-write)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type NetType: str
        :param _UniqSubnetId: Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqSubnetId: str
        :param _UniqVpcId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param _Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _WanIP: Public IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanIP: str
        :param _WanStatus: Public network status
Note: This field may return null, indicating that no valid values can be obtained.
        :type WanStatus: str
        :param _InstanceGroupId: Instance group ID Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceGroupId: str
        """
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._WanPort = None
        self._NetType = None
        self._UniqSubnetId = None
        self._UniqVpcId = None
        self._Description = None
        self._WanIP = None
        self._WanStatus = None
        self._InstanceGroupId = None

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
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WanIP(self):
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._WanPort = params.get("WanPort")
        self._NetType = params.get("NetType")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Description = params.get("Description")
        self._WanIP = params.get("WanIP")
        self._WanStatus = params.get("WanStatus")
        self._InstanceGroupId = params.get("InstanceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewAccount(AbstractModel):
    """The newly created x08 account

    """

    def __init__(self):
        r"""
        :param _AccountName: Account name, which can contain 1-16 letters, digits, and underscores. It must begin with a letter and end with a letter or digit.
        :type AccountName: str
        :param _AccountPassword: Password, which can contain 8-64 characters.
        :type AccountPassword: str
        :param _Host: Host
        :type Host: str
        :param _Description: Description
        :type Description: str
        :param _MaxUserConnections: Maximum number of user connections, which cannot be above 10,240.
        :type MaxUserConnections: int
        """
        self._AccountName = None
        self._AccountPassword = None
        self._Host = None
        self._Description = None
        self._MaxUserConnections = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._Host = params.get("Host")
        self._Description = params.get("Description")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTask(AbstractModel):
    """Task information

    """

    def __init__(self):
        r"""
        :param _TaskId: Auto-Incrementing task ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param _TaskType: Task type
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskType: str
        :param _TaskStatus: Task status
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskStatus: str
        :param _ObjectId: Task ID (cluster ID | instance group ID | instance ID)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ObjectId: str
        :param _ObjectType: Task type
Note: this field may return null, indicating that no valid values can be obtained.
        :type ObjectType: str
        """
        self._TaskId = None
        self._TaskType = None
        self._TaskStatus = None
        self._ObjectId = None
        self._ObjectType = None

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
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ObjectId(self):
        return self._ObjectId

    @ObjectId.setter
    def ObjectId(self, ObjectId):
        self._ObjectId = ObjectId

    @property
    def ObjectType(self):
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._TaskStatus = params.get("TaskStatus")
        self._ObjectId = params.get("ObjectId")
        self._ObjectType = params.get("ObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineClusterRequest(AbstractModel):
    """OfflineCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
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
        


class OfflineClusterResponse(AbstractModel):
    """OfflineCluster response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OfflineInstanceRequest(AbstractModel):
    """OfflineInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIdList: Instance ID array
        :type InstanceIdList: list of str
        """
        self._ClusterId = None
        self._InstanceIdList = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineInstanceResponse(AbstractModel):
    """OfflineInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OldAddrInfo(AbstractModel):
    """Database address

    """

    def __init__(self):
        r"""
        :param _Vip: IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vip: str
        :param _Vport: Port
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vport: int
        :param _ReturnTime: Expected valid hours of old IPs
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReturnTime: str
        """
        self._Vip = None
        self._Vport = None
        self._ReturnTime = None

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
    def ReturnTime(self):
        return self._ReturnTime

    @ReturnTime.setter
    def ReturnTime(self, ReturnTime):
        self._ReturnTime = ReturnTime


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._ReturnTime = params.get("ReturnTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAuditServiceRequest(AbstractModel):
    """OpenAuditService request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _LogExpireDay: Log retention period
        :type LogExpireDay: int
        :param _HighLogExpireDay: Frequent log retention period
        :type HighLogExpireDay: int
        :param _AuditRuleFilters: Audit rule. If both this parameter and `RuleTemplateIds` are left empty, full audit will be applied.
        :type AuditRuleFilters: list of AuditRuleFilters
        :param _RuleTemplateIds: Rule template ID. If both this parameter and `AuditRuleFilters` are left empty, full audit will be applied.
        :type RuleTemplateIds: list of str
        """
        self._InstanceId = None
        self._LogExpireDay = None
        self._HighLogExpireDay = None
        self._AuditRuleFilters = None
        self._RuleTemplateIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HighLogExpireDay(self):
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay

    @property
    def AuditRuleFilters(self):
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._HighLogExpireDay = params.get("HighLogExpireDay")
        if params.get("AuditRuleFilters") is not None:
            self._AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self._AuditRuleFilters.append(obj)
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAuditServiceResponse(AbstractModel):
    """OpenAuditService response structure.

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


class OpenClusterPasswordComplexityRequest(AbstractModel):
    """OpenClusterPasswordComplexity request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ValidatePasswordLength: Password length
        :type ValidatePasswordLength: int
        :param _ValidatePasswordMixedCaseCount: Number of letters
        :type ValidatePasswordMixedCaseCount: int
        :param _ValidatePasswordSpecialCharCount: Number of symbols
        :type ValidatePasswordSpecialCharCount: int
        :param _ValidatePasswordNumberCount: Number of digits
        :type ValidatePasswordNumberCount: int
        :param _ValidatePasswordPolicy: Password strength. Valid values: `MEDIUM`, `STRONG`.
        :type ValidatePasswordPolicy: str
        :param _ValidatePasswordDictionary: Data dictionary
        :type ValidatePasswordDictionary: list of str
        """
        self._ClusterId = None
        self._ValidatePasswordLength = None
        self._ValidatePasswordMixedCaseCount = None
        self._ValidatePasswordSpecialCharCount = None
        self._ValidatePasswordNumberCount = None
        self._ValidatePasswordPolicy = None
        self._ValidatePasswordDictionary = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ValidatePasswordLength(self):
        return self._ValidatePasswordLength

    @ValidatePasswordLength.setter
    def ValidatePasswordLength(self, ValidatePasswordLength):
        self._ValidatePasswordLength = ValidatePasswordLength

    @property
    def ValidatePasswordMixedCaseCount(self):
        return self._ValidatePasswordMixedCaseCount

    @ValidatePasswordMixedCaseCount.setter
    def ValidatePasswordMixedCaseCount(self, ValidatePasswordMixedCaseCount):
        self._ValidatePasswordMixedCaseCount = ValidatePasswordMixedCaseCount

    @property
    def ValidatePasswordSpecialCharCount(self):
        return self._ValidatePasswordSpecialCharCount

    @ValidatePasswordSpecialCharCount.setter
    def ValidatePasswordSpecialCharCount(self, ValidatePasswordSpecialCharCount):
        self._ValidatePasswordSpecialCharCount = ValidatePasswordSpecialCharCount

    @property
    def ValidatePasswordNumberCount(self):
        return self._ValidatePasswordNumberCount

    @ValidatePasswordNumberCount.setter
    def ValidatePasswordNumberCount(self, ValidatePasswordNumberCount):
        self._ValidatePasswordNumberCount = ValidatePasswordNumberCount

    @property
    def ValidatePasswordPolicy(self):
        return self._ValidatePasswordPolicy

    @ValidatePasswordPolicy.setter
    def ValidatePasswordPolicy(self, ValidatePasswordPolicy):
        self._ValidatePasswordPolicy = ValidatePasswordPolicy

    @property
    def ValidatePasswordDictionary(self):
        return self._ValidatePasswordDictionary

    @ValidatePasswordDictionary.setter
    def ValidatePasswordDictionary(self, ValidatePasswordDictionary):
        self._ValidatePasswordDictionary = ValidatePasswordDictionary


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ValidatePasswordLength = params.get("ValidatePasswordLength")
        self._ValidatePasswordMixedCaseCount = params.get("ValidatePasswordMixedCaseCount")
        self._ValidatePasswordSpecialCharCount = params.get("ValidatePasswordSpecialCharCount")
        self._ValidatePasswordNumberCount = params.get("ValidatePasswordNumberCount")
        self._ValidatePasswordPolicy = params.get("ValidatePasswordPolicy")
        self._ValidatePasswordDictionary = params.get("ValidatePasswordDictionary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenClusterPasswordComplexityResponse(AbstractModel):
    """OpenClusterPasswordComplexity response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OpenClusterReadOnlyInstanceGroupAccessRequest(AbstractModel):
    """OpenClusterReadOnlyInstanceGroupAccess request structure.

    """


class OpenClusterReadOnlyInstanceGroupAccessResponse(AbstractModel):
    """OpenClusterReadOnlyInstanceGroupAccess response structure.

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


class OpenReadOnlyInstanceExclusiveAccessRequest(AbstractModel):
    """OpenReadOnlyInstanceExclusiveAccess request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceId: ID of the read-only instance with dedicated access to be enabled
        :type InstanceId: str
        :param _VpcId: Specified VPC ID
        :type VpcId: str
        :param _SubnetId: Specified subnet ID
        :type SubnetId: str
        :param _Port: Port
        :type Port: int
        :param _SecurityGroupIds: Security group
        :type SecurityGroupIds: list of str
        """
        self._ClusterId = None
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._Port = None
        self._SecurityGroupIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Port = params.get("Port")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenReadOnlyInstanceExclusiveAccessResponse(AbstractModel):
    """OpenReadOnlyInstanceExclusiveAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Activation process ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OpenWanRequest(AbstractModel):
    """OpenWan request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceGrpId: Instance group ID
        :type InstanceGrpId: str
        """
        self._InstanceGrpId = None

    @property
    def InstanceGrpId(self):
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        self._InstanceGrpId = InstanceGrpId


    def _deserialize(self, params):
        self._InstanceGrpId = params.get("InstanceGrpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWanResponse(AbstractModel):
    """OpenWan response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task flow ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class Package(AbstractModel):
    """Resource pack

    """

    def __init__(self):
        r"""
        :param _AppId: AppID Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _PackageId: The unique ID of a resource pack Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageId: str
        :param _PackageName: Resource pack name Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageName: str
        :param _PackageType: Resource pack type. Valid values: `CCU` (compute resource pack), `DISK` (storage resource pack). Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param _PackageRegion: Region of the resource pack. Valid values: `China` (Chinese mainland), `overseas` (outside Chinese mainland). Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageRegion: str
        :param _Status: Resource pack status. Valid values: `creating`, `using`, `expired`, `normal_finish` (used up), `apply_refund` (requesting a refund), `refund` (refunded). 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _PackageTotalSpec: Total number of resource packs Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageTotalSpec: float
        :param _PackageUsedSpec: Consumed usage of resource packs Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageUsedSpec: float
        :param _HasQuota: Remaining usage of resource packs Note: This field may return null, indicating that no valid values can be obtained.
        :type HasQuota: bool
        :param _BindInstanceInfos: Information of the instance bound Note: This field may return null, indicating that no valid values can be obtained.
        :type BindInstanceInfos: list of BindInstanceInfo
        :param _StartTime: Validity time:  2022-07-01 00:00:00 Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _ExpireTime: Validity time:  2022-08-01 00:00:00 Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        """
        self._AppId = None
        self._PackageId = None
        self._PackageName = None
        self._PackageType = None
        self._PackageRegion = None
        self._Status = None
        self._PackageTotalSpec = None
        self._PackageUsedSpec = None
        self._HasQuota = None
        self._BindInstanceInfos = None
        self._StartTime = None
        self._ExpireTime = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PackageTotalSpec(self):
        return self._PackageTotalSpec

    @PackageTotalSpec.setter
    def PackageTotalSpec(self, PackageTotalSpec):
        self._PackageTotalSpec = PackageTotalSpec

    @property
    def PackageUsedSpec(self):
        return self._PackageUsedSpec

    @PackageUsedSpec.setter
    def PackageUsedSpec(self, PackageUsedSpec):
        self._PackageUsedSpec = PackageUsedSpec

    @property
    def HasQuota(self):
        return self._HasQuota

    @HasQuota.setter
    def HasQuota(self, HasQuota):
        self._HasQuota = HasQuota

    @property
    def BindInstanceInfos(self):
        return self._BindInstanceInfos

    @BindInstanceInfos.setter
    def BindInstanceInfos(self, BindInstanceInfos):
        self._BindInstanceInfos = BindInstanceInfos

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        self._PackageType = params.get("PackageType")
        self._PackageRegion = params.get("PackageRegion")
        self._Status = params.get("Status")
        self._PackageTotalSpec = params.get("PackageTotalSpec")
        self._PackageUsedSpec = params.get("PackageUsedSpec")
        self._HasQuota = params.get("HasQuota")
        if params.get("BindInstanceInfos") is not None:
            self._BindInstanceInfos = []
            for item in params.get("BindInstanceInfos"):
                obj = BindInstanceInfo()
                obj._deserialize(item)
                self._BindInstanceInfos.append(obj)
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageDetail(AbstractModel):
    """Resource pack details

    """

    def __init__(self):
        r"""
        :param _AppId: Account ID of `AppId` Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _PackageId: The unique ID of a resource pack Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageId: str
        :param _InstanceId: Instance ID Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _SuccessDeductSpec: The successfully deducted capacity Note: This field may return null, indicating that no valid values can be obtained.
        :type SuccessDeductSpec: float
        :param _PackageTotalUsedSpec: Used capacity of a resource pack as of now Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageTotalUsedSpec: float
        :param _StartTime: Deduction start time Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: Deduction end time Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _ExtendInfo: Extended information Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtendInfo: str
        """
        self._AppId = None
        self._PackageId = None
        self._InstanceId = None
        self._SuccessDeductSpec = None
        self._PackageTotalUsedSpec = None
        self._StartTime = None
        self._EndTime = None
        self._ExtendInfo = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SuccessDeductSpec(self):
        return self._SuccessDeductSpec

    @SuccessDeductSpec.setter
    def SuccessDeductSpec(self, SuccessDeductSpec):
        self._SuccessDeductSpec = SuccessDeductSpec

    @property
    def PackageTotalUsedSpec(self):
        return self._PackageTotalUsedSpec

    @PackageTotalUsedSpec.setter
    def PackageTotalUsedSpec(self, PackageTotalUsedSpec):
        self._PackageTotalUsedSpec = PackageTotalUsedSpec

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
    def ExtendInfo(self):
        return self._ExtendInfo

    @ExtendInfo.setter
    def ExtendInfo(self, ExtendInfo):
        self._ExtendInfo = ExtendInfo


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._PackageId = params.get("PackageId")
        self._InstanceId = params.get("InstanceId")
        self._SuccessDeductSpec = params.get("SuccessDeductSpec")
        self._PackageTotalUsedSpec = params.get("PackageTotalUsedSpec")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExtendInfo = params.get("ExtendInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDetail(AbstractModel):
    """Instance parameter details

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _ParamType: Parameter type. Valid values:  `integer`, `enum`, `float`, `string`, `func`.
        :type ParamType: str
        :param _SupportFunc: Whether `func` is supported. Valid values: `true` (supported), `false` (not supported).
        :type SupportFunc: bool
        :param _Default: Default value
        :type Default: str
        :param _Description: Parameter description
        :type Description: str
        :param _CurrentValue: Current value of the parameter
        :type CurrentValue: str
        :param _NeedReboot: Whether to restart the database for the modified parameters to take effect. Valid values:  `0` (no), `1` (yes).
        :type NeedReboot: int
        :param _Max: Maximum value of the parameter
        :type Max: str
        :param _Min: Minimum value of the parameter
        :type Min: str
        :param _EnumValue: Enumerated values of the parameter.  It is null if the parameter is non-enumerated. Note: This field may return null, indicating that no valid values can be obtained.
        :type EnumValue: list of str
        :param _IsGlobal: Valid values: `1` (global parameter),  `0`  (non-global parameter).
        :type IsGlobal: int
        :param _MatchType: The match type. Valid value: `multiVal`.
        :type MatchType: str
        :param _MatchValue: Match values, which will be separated by comma when `MatchType` is `multiVal`.
        :type MatchValue: str
        :param _IsFunc: Whether it is a `func` type. Valid values: `true` (yes), `false` (no). Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFunc: bool
        :param _Func: Formula content returned when `ParamType` is `func`. Note: This field may return null, indicating that no valid values can be obtained.
        :type Func: str
        :param _ModifiableInfo: Whether the parameter can be modified Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifiableInfo: :class:`tencentcloud.cynosdb.v20190107.models.ModifiableInfo`
        """
        self._ParamName = None
        self._ParamType = None
        self._SupportFunc = None
        self._Default = None
        self._Description = None
        self._CurrentValue = None
        self._NeedReboot = None
        self._Max = None
        self._Min = None
        self._EnumValue = None
        self._IsGlobal = None
        self._MatchType = None
        self._MatchValue = None
        self._IsFunc = None
        self._Func = None
        self._ModifiableInfo = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def SupportFunc(self):
        return self._SupportFunc

    @SupportFunc.setter
    def SupportFunc(self, SupportFunc):
        self._SupportFunc = SupportFunc

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def MatchValue(self):
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def IsFunc(self):
        return self._IsFunc

    @IsFunc.setter
    def IsFunc(self, IsFunc):
        self._IsFunc = IsFunc

    @property
    def Func(self):
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func

    @property
    def ModifiableInfo(self):
        return self._ModifiableInfo

    @ModifiableInfo.setter
    def ModifiableInfo(self, ModifiableInfo):
        self._ModifiableInfo = ModifiableInfo


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ParamType = params.get("ParamType")
        self._SupportFunc = params.get("SupportFunc")
        self._Default = params.get("Default")
        self._Description = params.get("Description")
        self._CurrentValue = params.get("CurrentValue")
        self._NeedReboot = params.get("NeedReboot")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        self._IsGlobal = params.get("IsGlobal")
        self._MatchType = params.get("MatchType")
        self._MatchValue = params.get("MatchValue")
        self._IsFunc = params.get("IsFunc")
        self._Func = params.get("Func")
        if params.get("ModifiableInfo") is not None:
            self._ModifiableInfo = ModifiableInfo()
            self._ModifiableInfo._deserialize(params.get("ModifiableInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    """Parameter information

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _Default: Default value
        :type Default: str
        :param _EnumValue: List of valid values when parameter type is `enum`, `string` or `bool`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnumValue: list of str
        :param _Max: Maximum value when parameter type is `float` or `integer`.
        :type Max: str
        :param _Min: Minimum value when parameter type is `float` or `integer`.
        :type Min: str
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _NeedReboot: Whether to restart the instance for the modified parameters to take effect.
        :type NeedReboot: int
        :param _ParamType: Parameter type: `integer`, `float`, `string`, `enum`, `bool`.
        :type ParamType: str
        :param _MatchType: Match type. Regex can be used when parameter type is `string`. Valid value: `multiVal`.
        :type MatchType: str
        :param _MatchValue: Match values, which will be separated by semicolon when match type is `multiVal`.
        :type MatchValue: str
        :param _Description: Parameter description
        :type Description: str
        :param _IsGlobal: Whether it is global parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsGlobal: int
        :param _ModifiableInfo: Whether the parameter can be modified
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifiableInfo: :class:`tencentcloud.cynosdb.v20190107.models.ModifiableInfo`
        :param _IsFunc: Whether it is a function
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFunc: bool
        :param _Func: Function
Note: This field may return null, indicating that no valid values can be obtained.
        :type Func: str
        """
        self._CurrentValue = None
        self._Default = None
        self._EnumValue = None
        self._Max = None
        self._Min = None
        self._ParamName = None
        self._NeedReboot = None
        self._ParamType = None
        self._MatchType = None
        self._MatchValue = None
        self._Description = None
        self._IsGlobal = None
        self._ModifiableInfo = None
        self._IsFunc = None
        self._Func = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def MatchValue(self):
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def ModifiableInfo(self):
        return self._ModifiableInfo

    @ModifiableInfo.setter
    def ModifiableInfo(self, ModifiableInfo):
        self._ModifiableInfo = ModifiableInfo

    @property
    def IsFunc(self):
        return self._IsFunc

    @IsFunc.setter
    def IsFunc(self, IsFunc):
        self._IsFunc = IsFunc

    @property
    def Func(self):
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._Default = params.get("Default")
        self._EnumValue = params.get("EnumValue")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._ParamName = params.get("ParamName")
        self._NeedReboot = params.get("NeedReboot")
        self._ParamType = params.get("ParamType")
        self._MatchType = params.get("MatchType")
        self._MatchValue = params.get("MatchValue")
        self._Description = params.get("Description")
        self._IsGlobal = params.get("IsGlobal")
        if params.get("ModifiableInfo") is not None:
            self._ModifiableInfo = ModifiableInfo()
            self._ModifiableInfo._deserialize(params.get("ModifiableInfo"))
        self._IsFunc = params.get("IsFunc")
        self._Func = params.get("Func")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamItem(AbstractModel):
    """Parameter to be modified

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _CurrentValue: New value
        :type CurrentValue: str
        :param _OldValue: Original value
        :type OldValue: str
        """
        self._ParamName = None
        self._CurrentValue = None
        self._OldValue = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._CurrentValue = params.get("CurrentValue")
        self._OldValue = params.get("OldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamItemDetail(AbstractModel):
    """Instance parameter information

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _Default: Default value
        :type Default: str
        :param _EnumValue: Enumerated values of the parameter It is null if the parameter is non-enumerated.
        :type EnumValue: list of str
        :param _IsGlobal: Valid values: `1` (global parameter),  `0`  (non-global parameter).
        :type IsGlobal: int
        :param _Max: Maximum value
        :type Max: str
        :param _Min: Minimum value
        :type Min: str
        :param _NeedReboot: Whether to restart the database for the modified parameters to take effect. Valid values:  `0` (no), `1` (yes)
        :type NeedReboot: int
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _ParamType: Parameter type. Valid values:  `integer`, `enum`, `float`, `string`, `func`.
        :type ParamType: str
        :param _Description: Parameter description
        :type Description: str
        :param _IsFunc: Whether `ParamType` is a `func` Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFunc: bool
        :param _Func: Parameter configuration formula Note: This field may return null, indicating that no valid values can be obtained.
        :type Func: str
        """
        self._CurrentValue = None
        self._Default = None
        self._EnumValue = None
        self._IsGlobal = None
        self._Max = None
        self._Min = None
        self._NeedReboot = None
        self._ParamName = None
        self._ParamType = None
        self._Description = None
        self._IsFunc = None
        self._Func = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsFunc(self):
        return self._IsFunc

    @IsFunc.setter
    def IsFunc(self, IsFunc):
        self._IsFunc = IsFunc

    @property
    def Func(self):
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._Default = params.get("Default")
        self._EnumValue = params.get("EnumValue")
        self._IsGlobal = params.get("IsGlobal")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._NeedReboot = params.get("NeedReboot")
        self._ParamName = params.get("ParamName")
        self._ParamType = params.get("ParamType")
        self._Description = params.get("Description")
        self._IsFunc = params.get("IsFunc")
        self._Func = params.get("Func")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateListInfo(AbstractModel):
    """Parameter template information

    """

    def __init__(self):
        r"""
        :param _Id: Parameter template ID
        :type Id: int
        :param _TemplateName: Parameter template name
        :type TemplateName: str
        :param _TemplateDescription: Parameter template description
        :type TemplateDescription: str
        :param _EngineVersion: Engine version
        :type EngineVersion: str
        :param _DbMode: Database Type. Valid values: `NORMAL`, `SERVERLESS`.
        :type DbMode: str
        :param _ParamInfoSet: Parameter template details
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParamInfoSet: list of TemplateParamInfo
        """
        self._Id = None
        self._TemplateName = None
        self._TemplateDescription = None
        self._EngineVersion = None
        self._DbMode = None
        self._ParamInfoSet = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def ParamInfoSet(self):
        return self._ParamInfoSet

    @ParamInfoSet.setter
    def ParamInfoSet(self, ParamInfoSet):
        self._ParamInfoSet = ParamInfoSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TemplateName = params.get("TemplateName")
        self._TemplateDescription = params.get("TemplateDescription")
        self._EngineVersion = params.get("EngineVersion")
        self._DbMode = params.get("DbMode")
        if params.get("ParamInfoSet") is not None:
            self._ParamInfoSet = []
            for item in params.get("ParamInfoSet"):
                obj = TemplateParamInfo()
                obj._deserialize(item)
                self._ParamInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseServerlessRequest(AbstractModel):
    """PauseServerless request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ForcePause: Whether to pause forcibly and ignore the current user connections. Valid values: `0` (no), `1` (yes). Default value: `1`
        :type ForcePause: int
        """
        self._ClusterId = None
        self._ForcePause = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ForcePause(self):
        return self._ForcePause

    @ForcePause.setter
    def ForcePause(self, ForcePause):
        self._ForcePause = ForcePause


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ForcePause = params.get("ForcePause")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseServerlessResponse(AbstractModel):
    """PauseServerless response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class PolicyRule(AbstractModel):
    """Security group rule

    """

    def __init__(self):
        r"""
        :param _Action: Policy, which can be `ACCEPT` or `DROP`
        :type Action: str
        :param _CidrIp: Source IP or source IP range, such as 192.168.0.0/16
        :type CidrIp: str
        :param _PortRange: Port
        :type PortRange: str
        :param _IpProtocol: Network protocol, such as UDP and TCP
        :type IpProtocol: str
        :param _ServiceModule: Protocol port ID or protocol port group ID.
        :type ServiceModule: str
        :param _AddressModule: IP address ID or IP address group ID.
        :type AddressModule: str
        :param _Id: id
        :type Id: str
        :param _Desc: Description
        :type Desc: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._ServiceModule = None
        self._AddressModule = None
        self._Id = None
        self._Desc = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def ServiceModule(self):
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._ServiceModule = params.get("ServiceModule")
        self._AddressModule = params.get("AddressModule")
        self._Id = params.get("Id")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyConnectionPoolInfo(AbstractModel):
    """Connection pool information for the database proxy

    """

    def __init__(self):
        r"""
        :param _ConnectionPoolTimeOut: Connection persistence timeout in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConnectionPoolTimeOut: int
        :param _OpenConnectionPool: Whether the connection pool is enabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type OpenConnectionPool: str
        :param _ConnectionPoolType: Connection pool type. Valid value: `SessionConnectionPool` (session-level).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConnectionPoolType: str
        """
        self._ConnectionPoolTimeOut = None
        self._OpenConnectionPool = None
        self._ConnectionPoolType = None

    @property
    def ConnectionPoolTimeOut(self):
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut

    @property
    def OpenConnectionPool(self):
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType


    def _deserialize(self, params):
        self._ConnectionPoolTimeOut = params.get("ConnectionPoolTimeOut")
        self._OpenConnectionPool = params.get("OpenConnectionPool")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroup(AbstractModel):
    """Proxy group

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        :param _ProxyNodeCount: Number of nodes in the proxy group
        :type ProxyNodeCount: int
        :param _Status: Database proxy group status
        :type Status: str
        :param _Region: Region
        :type Region: str
        :param _Zone: AZ
        :type Zone: str
        :param _CurrentProxyVersion: Current proxy version
        :type CurrentProxyVersion: str
        :param _ClusterId: Cluster ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _AppId: User `AppId`
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _OpenRw: Enabling read/write separation for database proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :type OpenRw: str
        """
        self._ProxyGroupId = None
        self._ProxyNodeCount = None
        self._Status = None
        self._Region = None
        self._Zone = None
        self._CurrentProxyVersion = None
        self._ClusterId = None
        self._AppId = None
        self._OpenRw = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyNodeCount(self):
        return self._ProxyNodeCount

    @ProxyNodeCount.setter
    def ProxyNodeCount(self, ProxyNodeCount):
        self._ProxyNodeCount = ProxyNodeCount

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def CurrentProxyVersion(self):
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OpenRw(self):
        return self._OpenRw

    @OpenRw.setter
    def OpenRw(self, OpenRw):
        self._OpenRw = OpenRw


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyNodeCount = params.get("ProxyNodeCount")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        self._ClusterId = params.get("ClusterId")
        self._AppId = params.get("AppId")
        self._OpenRw = params.get("OpenRw")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupInfo(AbstractModel):
    """Database proxy group details

    """

    def __init__(self):
        r"""
        :param _ProxyGroup: Database proxy group
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyGroup: :class:`tencentcloud.cynosdb.v20190107.models.ProxyGroup`
        :param _ProxyGroupRwInfo: Read/write separation information of the database proxy group
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyGroupRwInfo: :class:`tencentcloud.cynosdb.v20190107.models.ProxyGroupRwInfo`
        :param _ProxyNodes: Node information of the database proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyNodes: list of ProxyNodeInfo
        :param _ConnectionPool: Connection pool information for the database proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConnectionPool: :class:`tencentcloud.cynosdb.v20190107.models.ProxyConnectionPoolInfo`
        :param _NetAddrInfos: Network information for database proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetAddrInfos: list of NetAddr
        :param _Tasks: Task set of the database proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tasks: list of ObjectTask
        """
        self._ProxyGroup = None
        self._ProxyGroupRwInfo = None
        self._ProxyNodes = None
        self._ConnectionPool = None
        self._NetAddrInfos = None
        self._Tasks = None

    @property
    def ProxyGroup(self):
        return self._ProxyGroup

    @ProxyGroup.setter
    def ProxyGroup(self, ProxyGroup):
        self._ProxyGroup = ProxyGroup

    @property
    def ProxyGroupRwInfo(self):
        return self._ProxyGroupRwInfo

    @ProxyGroupRwInfo.setter
    def ProxyGroupRwInfo(self, ProxyGroupRwInfo):
        self._ProxyGroupRwInfo = ProxyGroupRwInfo

    @property
    def ProxyNodes(self):
        return self._ProxyNodes

    @ProxyNodes.setter
    def ProxyNodes(self, ProxyNodes):
        self._ProxyNodes = ProxyNodes

    @property
    def ConnectionPool(self):
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def NetAddrInfos(self):
        return self._NetAddrInfos

    @NetAddrInfos.setter
    def NetAddrInfos(self, NetAddrInfos):
        self._NetAddrInfos = NetAddrInfos

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks


    def _deserialize(self, params):
        if params.get("ProxyGroup") is not None:
            self._ProxyGroup = ProxyGroup()
            self._ProxyGroup._deserialize(params.get("ProxyGroup"))
        if params.get("ProxyGroupRwInfo") is not None:
            self._ProxyGroupRwInfo = ProxyGroupRwInfo()
            self._ProxyGroupRwInfo._deserialize(params.get("ProxyGroupRwInfo"))
        if params.get("ProxyNodes") is not None:
            self._ProxyNodes = []
            for item in params.get("ProxyNodes"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self._ProxyNodes.append(obj)
        if params.get("ConnectionPool") is not None:
            self._ConnectionPool = ProxyConnectionPoolInfo()
            self._ConnectionPool._deserialize(params.get("ConnectionPool"))
        if params.get("NetAddrInfos") is not None:
            self._NetAddrInfos = []
            for item in params.get("NetAddrInfos"):
                obj = NetAddr()
                obj._deserialize(item)
                self._NetAddrInfos.append(obj)
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupRwInfo(AbstractModel):
    """Read/write separation information of the database proxy group

    """

    def __init__(self):
        r"""
        :param _ConsistencyType: Consistency type. Valid values: `eventual` (eventual consistency), `session` (session consistency), `global` (global consistency).
        :type ConsistencyType: str
        :param _ConsistencyTimeOut: Consistency timeout period
        :type ConsistencyTimeOut: int
        :param _WeightMode: Weight mode. Valid values: `system` (auto-assigned), `custom`.
        :type WeightMode: str
        :param _FailOver: Whether to enable failover
        :type FailOver: str
        :param _AutoAddRo: Whether to automatically add read-only instance. Valid value: `yes`, `no`.
        :type AutoAddRo: str
        :param _InstanceWeights: Instance weight array
        :type InstanceWeights: list of ProxyInstanceWeight
        :param _OpenRw: Whether to enable read-write node. Valid values: `yes`, `no`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OpenRw: str
        :param _RwType: Read/write attribute. Valid values: `READWRITE`, `READONLY`.
        :type RwType: str
        :param _TransSplit: Transaction split
        :type TransSplit: bool
        :param _AccessMode: Connection mode. Valid values: `balance`, `nearby`.
        :type AccessMode: str
        """
        self._ConsistencyType = None
        self._ConsistencyTimeOut = None
        self._WeightMode = None
        self._FailOver = None
        self._AutoAddRo = None
        self._InstanceWeights = None
        self._OpenRw = None
        self._RwType = None
        self._TransSplit = None
        self._AccessMode = None

    @property
    def ConsistencyType(self):
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def ConsistencyTimeOut(self):
        return self._ConsistencyTimeOut

    @ConsistencyTimeOut.setter
    def ConsistencyTimeOut(self, ConsistencyTimeOut):
        self._ConsistencyTimeOut = ConsistencyTimeOut

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def InstanceWeights(self):
        return self._InstanceWeights

    @InstanceWeights.setter
    def InstanceWeights(self, InstanceWeights):
        self._InstanceWeights = InstanceWeights

    @property
    def OpenRw(self):
        return self._OpenRw

    @OpenRw.setter
    def OpenRw(self, OpenRw):
        self._OpenRw = OpenRw

    @property
    def RwType(self):
        return self._RwType

    @RwType.setter
    def RwType(self, RwType):
        self._RwType = RwType

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def AccessMode(self):
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode


    def _deserialize(self, params):
        self._ConsistencyType = params.get("ConsistencyType")
        self._ConsistencyTimeOut = params.get("ConsistencyTimeOut")
        self._WeightMode = params.get("WeightMode")
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        if params.get("InstanceWeights") is not None:
            self._InstanceWeights = []
            for item in params.get("InstanceWeights"):
                obj = ProxyInstanceWeight()
                obj._deserialize(item)
                self._InstanceWeights.append(obj)
        self._OpenRw = params.get("OpenRw")
        self._RwType = params.get("RwType")
        self._TransSplit = params.get("TransSplit")
        self._AccessMode = params.get("AccessMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyInstanceWeight(AbstractModel):
    """Weight ratio between read-write instances and read-only instances

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanID
        :type InstanceId: str
        :param _Weight: Instance weight
        :type Weight: int
        """
        self._InstanceId = None
        self._Weight = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodeInfo(AbstractModel):
    """Node in the database proxy group

    """

    def __init__(self):
        r"""
        :param _ProxyNodeId: Database proxy node ID
        :type ProxyNodeId: str
        :param _ProxyNodeConnections: Current node connections, which is not returned by the `DescribeProxyNodes` API.
        :type ProxyNodeConnections: int
        :param _Cpu: CPU of the database proxy node
        :type Cpu: int
        :param _Mem: Memory of the database proxy node
        :type Mem: int
        :param _Status: Status of the database proxy node
        :type Status: str
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _AppId: User AppID
        :type AppId: int
        :param _Region: Region
        :type Region: str
        :param _Zone: AZ
        :type Zone: str
        """
        self._ProxyNodeId = None
        self._ProxyNodeConnections = None
        self._Cpu = None
        self._Mem = None
        self._Status = None
        self._ProxyGroupId = None
        self._ClusterId = None
        self._AppId = None
        self._Region = None
        self._Zone = None

    @property
    def ProxyNodeId(self):
        return self._ProxyNodeId

    @ProxyNodeId.setter
    def ProxyNodeId(self, ProxyNodeId):
        self._ProxyNodeId = ProxyNodeId

    @property
    def ProxyNodeConnections(self):
        return self._ProxyNodeConnections

    @ProxyNodeConnections.setter
    def ProxyNodeConnections(self, ProxyNodeConnections):
        self._ProxyNodeConnections = ProxyNodeConnections

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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


    def _deserialize(self, params):
        self._ProxyNodeId = params.get("ProxyNodeId")
        self._ProxyNodeConnections = params.get("ProxyNodeConnections")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Status = params.get("Status")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ClusterId = params.get("ClusterId")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxySpec(AbstractModel):
    """Database proxy specifications

    """

    def __init__(self):
        r"""
        :param _Cpu: Number of database proxy CPU cores
        :type Cpu: int
        :param _Mem: Database proxy memory
        :type Mem: int
        """
        self._Cpu = None
        self._Mem = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyZone(AbstractModel):
    """Number of proxy nodes and their AZs

    """

    def __init__(self):
        r"""
        :param _ProxyNodeZone: AZ of the proxy node
        :type ProxyNodeZone: str
        :param _ProxyNodeCount: The number of proxy nodes
        :type ProxyNodeCount: int
        """
        self._ProxyNodeZone = None
        self._ProxyNodeCount = None

    @property
    def ProxyNodeZone(self):
        return self._ProxyNodeZone

    @ProxyNodeZone.setter
    def ProxyNodeZone(self, ProxyNodeZone):
        self._ProxyNodeZone = ProxyNodeZone

    @property
    def ProxyNodeCount(self):
        return self._ProxyNodeCount

    @ProxyNodeCount.setter
    def ProxyNodeCount(self, ProxyNodeCount):
        self._ProxyNodeCount = ProxyNodeCount


    def _deserialize(self, params):
        self._ProxyNodeZone = params.get("ProxyNodeZone")
        self._ProxyNodeCount = params.get("ProxyNodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """Query filter

    """

    def __init__(self):
        r"""
        :param _Names: Search field. Valid values: "InstanceId", "ProjectId", "InstanceName", "Vip"
        :type Names: list of str
        :param _Values: Search string
        :type Values: list of str
        :param _ExactMatch: Whether to use exact match
        :type ExactMatch: bool
        :param _Name: Search field
        :type Name: str
        :param _Operator: Operator
        :type Operator: str
        """
        self._Names = None
        self._Values = None
        self._ExactMatch = None
        self._Name = None
        self._Operator = None

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Names = params.get("Names")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        self._Name = params.get("Name")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryParamFilter(AbstractModel):
    """Filters for query

    """

    def __init__(self):
        r"""
        :param _Names: Search field. Valid values: "InstanceId", "ProjectId", "InstanceName", "Vip"
        :type Names: list of str
        :param _Values: Search string
        :type Values: list of str
        :param _ExactMatch: Whether to use exact match
        :type ExactMatch: bool
        """
        self._Names = None
        self._Values = None
        self._ExactMatch = None

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._Names = params.get("Names")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundResourcePackageRequest(AbstractModel):
    """RefundResourcePackage request structure.

    """

    def __init__(self):
        r"""
        :param _PackageId: The unique ID of a resource pack
        :type PackageId: str
        """
        self._PackageId = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundResourcePackageResponse(AbstractModel):
    """RefundResourcePackage response structure.

    """

    def __init__(self):
        r"""
        :param _DealNames: Each item has only one `dealName`, through which you can ensure the idempotency of the delivery API.
        :type DealNames: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealNames = None
        self._RequestId = None

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class ReloadBalanceProxyNodeRequest(AbstractModel):
    """ReloadBalanceProxyNode request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        """
        self._ClusterId = None
        self._ProxyGroupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadBalanceProxyNodeResponse(AbstractModel):
    """ReloadBalanceProxyNode response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async flow ID
        :type FlowId: int
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class RemoveClusterSlaveZoneRequest(AbstractModel):
    """RemoveClusterSlaveZone request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _SlaveZone: Replica AZ
        :type SlaveZone: str
        """
        self._ClusterId = None
        self._SlaveZone = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveClusterSlaveZoneResponse(AbstractModel):
    """RemoveClusterSlaveZone response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async FlowId
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword request structure.

    """

    def __init__(self):
        r"""
        :param _AccountName: Database account name
        :type AccountName: str
        :param _AccountPassword: New password of the database account
        :type AccountPassword: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Host: Host. Default value: `%`
        :type Host: str
        """
        self._AccountName = None
        self._AccountPassword = None
        self._ClusterId = None
        self._Host = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._ClusterId = params.get("ClusterId")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword response structure.

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


class ResourcePackage(AbstractModel):
    """Information of a resource pack

    """

    def __init__(self):
        r"""
        :param _PackageId: The unique ID of a resource pack Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageId: str
        :param _PackageType: Resource pack type. Valid values:  `CCU` (compute resource pack),  `DISK`  (storage resource pack). Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        """
        self._PackageId = None
        self._PackageType = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    """RestartInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
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
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ResumeServerlessRequest(AbstractModel):
    """ResumeServerless request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
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
        


class ResumeServerlessResponse(AbstractModel):
    """ResumeServerless response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RollbackTimeRange(AbstractModel):
    """Rollback time range

    """

    def __init__(self):
        r"""
        :param _TimeRangeStart: Start time
        :type TimeRangeStart: str
        :param _TimeRangeEnd: End time
        :type TimeRangeEnd: str
        """
        self._TimeRangeStart = None
        self._TimeRangeEnd = None

    @property
    def TimeRangeStart(self):
        return self._TimeRangeStart

    @TimeRangeStart.setter
    def TimeRangeStart(self, TimeRangeStart):
        self._TimeRangeStart = TimeRangeStart

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd


    def _deserialize(self, params):
        self._TimeRangeStart = params.get("TimeRangeStart")
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleFilters(AbstractModel):
    """Filter of the audit rule

    """

    def __init__(self):
        r"""
        :param _Type: Filter parameter name of the audit rule. Valid values: `host` (client IP), `user` (database account), `dbName` (database name), `sqlType` (SQL type), `sql` (SQL statement).
        :type Type: str
        :param _Compare: Filter match type of the audit rule. Valid values: `INC` (including), `EXC` (excluding), `EQS` (equal to), `NEQ` (not equal to).
        :type Compare: str
        :param _Value: Filter match value of the audit rule
        :type Value: list of str
        """
        self._Type = None
        self._Compare = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Compare = params.get("Compare")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SalePackageSpec(AbstractModel):
    """Resource pack details

    """

    def __init__(self):
        r"""
        :param _PackageRegion: Region of the resource pack Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageRegion: str
        :param _PackageType: Resource pack type. Valid values: `CCU` (compute resource pack), `DISK` (storage resource pack). Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param _PackageVersion: Resource pack edition. Valid values: `base` (basic edition), `common` (general edition), `enterprise` (enterprise edition). Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageVersion: str
        :param _MinPackageSpec: Minimum number of resources for the current edition of the resource pack.  Unit of the compute resources: pcs.  Unit of the storage resources: GB. Note: This field may return null, indicating that no valid values can be obtained.
        :type MinPackageSpec: float
        :param _MaxPackageSpec: Maximum number of resources for the current edition of the resource pack.  Unit of the compute resources: pcs.  Unit of the storage resources: GB. Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxPackageSpec: float
        :param _ExpireDay: Validity period of a resource pack in days Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireDay: int
        """
        self._PackageRegion = None
        self._PackageType = None
        self._PackageVersion = None
        self._MinPackageSpec = None
        self._MaxPackageSpec = None
        self._ExpireDay = None

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def MinPackageSpec(self):
        return self._MinPackageSpec

    @MinPackageSpec.setter
    def MinPackageSpec(self, MinPackageSpec):
        self._MinPackageSpec = MinPackageSpec

    @property
    def MaxPackageSpec(self):
        return self._MaxPackageSpec

    @MaxPackageSpec.setter
    def MaxPackageSpec(self, MaxPackageSpec):
        self._MaxPackageSpec = MaxPackageSpec

    @property
    def ExpireDay(self):
        return self._ExpireDay

    @ExpireDay.setter
    def ExpireDay(self, ExpireDay):
        self._ExpireDay = ExpireDay


    def _deserialize(self, params):
        self._PackageRegion = params.get("PackageRegion")
        self._PackageType = params.get("PackageType")
        self._PackageVersion = params.get("PackageVersion")
        self._MinPackageSpec = params.get("MinPackageSpec")
        self._MaxPackageSpec = params.get("MaxPackageSpec")
        self._ExpireDay = params.get("ExpireDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleRegion(AbstractModel):
    """Information of a purchasable region

    """

    def __init__(self):
        r"""
        :param _Region: Region name
        :type Region: str
        :param _RegionId: Numeric ID of a region
        :type RegionId: int
        :param _RegionZh: Region name
        :type RegionZh: str
        :param _ZoneSet: List of purchasable AZs
        :type ZoneSet: list of SaleZone
        :param _DbType: Engine type
        :type DbType: str
        :param _Modules: Supported modules in a region
        :type Modules: list of Module
        """
        self._Region = None
        self._RegionId = None
        self._RegionZh = None
        self._ZoneSet = None
        self._DbType = None
        self._Modules = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionZh(self):
        return self._RegionZh

    @RegionZh.setter
    def RegionZh(self, RegionZh):
        self._RegionZh = RegionZh

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Modules(self):
        return self._Modules

    @Modules.setter
    def Modules(self, Modules):
        self._Modules = Modules


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._RegionZh = params.get("RegionZh")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = SaleZone()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._DbType = params.get("DbType")
        if params.get("Modules") is not None:
            self._Modules = []
            for item in params.get("Modules"):
                obj = Module()
                obj._deserialize(item)
                self._Modules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleZone(AbstractModel):
    """Information of a purchasable AZ

    """

    def __init__(self):
        r"""
        :param _Zone: AZ name
        :type Zone: str
        :param _ZoneId: Numeric ID of an AZ
        :type ZoneId: int
        :param _ZoneZh: AZ name
        :type ZoneZh: str
        :param _IsSupportServerless: Whether serverless cluster is supported. Valid values: <br>
`0`: No<br>
`1`: Yes
        :type IsSupportServerless: int
        :param _IsSupportNormal: Whether standard cluster is supported. Valid values: <br>
`0`: No<br>
`1`: Yes
        :type IsSupportNormal: int
        :param _PhysicalZone: Physical zone
        :type PhysicalZone: str
        :param _HasPermission: Whether the user has AZ permission
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasPermission: bool
        :param _IsWholeRdmaZone: Whether it is a full-linkage RDMA AZ.
        :type IsWholeRdmaZone: str
        """
        self._Zone = None
        self._ZoneId = None
        self._ZoneZh = None
        self._IsSupportServerless = None
        self._IsSupportNormal = None
        self._PhysicalZone = None
        self._HasPermission = None
        self._IsWholeRdmaZone = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneZh(self):
        return self._ZoneZh

    @ZoneZh.setter
    def ZoneZh(self, ZoneZh):
        self._ZoneZh = ZoneZh

    @property
    def IsSupportServerless(self):
        return self._IsSupportServerless

    @IsSupportServerless.setter
    def IsSupportServerless(self, IsSupportServerless):
        self._IsSupportServerless = IsSupportServerless

    @property
    def IsSupportNormal(self):
        return self._IsSupportNormal

    @IsSupportNormal.setter
    def IsSupportNormal(self, IsSupportNormal):
        self._IsSupportNormal = IsSupportNormal

    @property
    def PhysicalZone(self):
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def HasPermission(self):
        return self._HasPermission

    @HasPermission.setter
    def HasPermission(self, HasPermission):
        self._HasPermission = HasPermission

    @property
    def IsWholeRdmaZone(self):
        return self._IsWholeRdmaZone

    @IsWholeRdmaZone.setter
    def IsWholeRdmaZone(self, IsWholeRdmaZone):
        self._IsWholeRdmaZone = IsWholeRdmaZone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneZh = params.get("ZoneZh")
        self._IsSupportServerless = params.get("IsSupportServerless")
        self._IsSupportNormal = params.get("IsSupportNormal")
        self._PhysicalZone = params.get("PhysicalZone")
        self._HasPermission = params.get("HasPermission")
        self._IsWholeRdmaZone = params.get("IsWholeRdmaZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClusterDatabasesRequest(AbstractModel):
    """SearchClusterDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The cluster ID
        :type ClusterId: str
        :param _Database: Database name
        :type Database: str
        :param _MatchType: Whether to search exactly
Valid values: `0` (fuzzy search), `1` (exact search). 
Default value: `0`.
        :type MatchType: int
        """
        self._ClusterId = None
        self._Database = None
        self._MatchType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Database = params.get("Database")
        self._MatchType = params.get("MatchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClusterDatabasesResponse(AbstractModel):
    """SearchClusterDatabases response structure.

    """

    def __init__(self):
        r"""
        :param _Databases: Database List
Note: This field may return null, indicating that no valid values can be obtained.
        :type Databases: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Databases = None
        self._RequestId = None

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Databases = params.get("Databases")
        self._RequestId = params.get("RequestId")


class SearchClusterTablesRequest(AbstractModel):
    """SearchClusterTables request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Database: Database name
        :type Database: str
        :param _Table: Data table name
        :type Table: str
        :param _TableType: Data table type. Valid values:
`view`: Only return to view,
`base_table`: Only return to basic table,
`all`: Return to view and table.
        :type TableType: str
        """
        self._ClusterId = None
        self._Database = None
        self._Table = None
        self._TableType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._TableType = params.get("TableType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClusterTablesResponse(AbstractModel):
    """SearchClusterTables response structure.

    """

    def __init__(self):
        r"""
        :param _Tables: Data table list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of DatabaseTables
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tables = None
        self._RequestId = None

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTables()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """Security group details

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _Inbound: Inbound rule
        :type Inbound: list of PolicyRule
        :param _Outbound: Outbound rule
        :type Outbound: list of PolicyRule
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._Inbound = None
        self._Outbound = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Inbound(self):
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self._Outbound.append(obj)
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewFlagRequest(AbstractModel):
    """SetRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _ResourceIds: ID of the instance to be manipulated
        :type ResourceIds: list of str
        :param _AutoRenewFlag: Auto-renewal flag. 0: normal renewal, 1: auto-renewal, 2: no renewal.
        :type AutoRenewFlag: int
        """
        self._ResourceIds = None
        self._AutoRenewFlag = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewFlagResponse(AbstractModel):
    """SetRenewFlag response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of successfully manipulated instances
        :type Count: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class SlaveZoneAttrItem(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Zone: 
        :type Zone: str
        :param _BinlogSyncWay: 
        :type BinlogSyncWay: str
        """
        self._Zone = None
        self._BinlogSyncWay = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def BinlogSyncWay(self):
        return self._BinlogSyncWay

    @BinlogSyncWay.setter
    def BinlogSyncWay(self, BinlogSyncWay):
        self._BinlogSyncWay = BinlogSyncWay


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._BinlogSyncWay = params.get("BinlogSyncWay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowQueriesItem(AbstractModel):
    """Slow query information of the instance

    """

    def __init__(self):
        r"""
        :param _Timestamp: Execution timestamp
        :type Timestamp: int
        :param _QueryTime: Execution duration in seconds
        :type QueryTime: float
        :param _SqlText: SQL statement
        :type SqlText: str
        :param _UserHost: Client host
        :type UserHost: str
        :param _UserName: Username
        :type UserName: str
        :param _Database: Database name
        :type Database: str
        :param _LockTime: Lock duration in seconds
        :type LockTime: float
        :param _RowsExamined: Number of scanned rows
        :type RowsExamined: int
        :param _RowsSent: Number of returned rows
        :type RowsSent: int
        :param _SqlTemplate: SQL template
        :type SqlTemplate: str
        :param _SqlMd5: MD5 value of the SQL statement
        :type SqlMd5: str
        """
        self._Timestamp = None
        self._QueryTime = None
        self._SqlText = None
        self._UserHost = None
        self._UserName = None
        self._Database = None
        self._LockTime = None
        self._RowsExamined = None
        self._RowsSent = None
        self._SqlTemplate = None
        self._SqlMd5 = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def UserHost(self):
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def LockTime(self):
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def RowsExamined(self):
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsSent(self):
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def SqlTemplate(self):
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def SqlMd5(self):
        return self._SqlMd5

    @SqlMd5.setter
    def SqlMd5(self, SqlMd5):
        self._SqlMd5 = SqlMd5


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._QueryTime = params.get("QueryTime")
        self._SqlText = params.get("SqlText")
        self._UserHost = params.get("UserHost")
        self._UserName = params.get("UserName")
        self._Database = params.get("Database")
        self._LockTime = params.get("LockTime")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsSent = params.get("RowsSent")
        self._SqlTemplate = params.get("SqlTemplate")
        self._SqlMd5 = params.get("SqlMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterVpcRequest(AbstractModel):
    """SwitchClusterVpc request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _UniqVpcId: VPC ID in string
        :type UniqVpcId: str
        :param _UniqSubnetId: Subnet ID in string
        :type UniqSubnetId: str
        :param _OldIpReserveHours: Valid hours of old IP
        :type OldIpReserveHours: int
        """
        self._ClusterId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._OldIpReserveHours = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def OldIpReserveHours(self):
        return self._OldIpReserveHours

    @OldIpReserveHours.setter
    def OldIpReserveHours(self, OldIpReserveHours):
        self._OldIpReserveHours = OldIpReserveHours


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._OldIpReserveHours = params.get("OldIpReserveHours")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterVpcResponse(AbstractModel):
    """SwitchClusterVpc response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SwitchClusterZoneRequest(AbstractModel):
    """SwitchClusterZone request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _OldZone: The current AZ
        :type OldZone: str
        :param _NewZone: New AZ
        :type NewZone: str
        :param _IsInMaintainPeriod: Valid values: `yes` (execute during maintenance time), `no` (execute now)
        :type IsInMaintainPeriod: str
        """
        self._ClusterId = None
        self._OldZone = None
        self._NewZone = None
        self._IsInMaintainPeriod = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def OldZone(self):
        return self._OldZone

    @OldZone.setter
    def OldZone(self, OldZone):
        self._OldZone = OldZone

    @property
    def NewZone(self):
        return self._NewZone

    @NewZone.setter
    def NewZone(self, NewZone):
        self._NewZone = NewZone

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._OldZone = params.get("OldZone")
        self._NewZone = params.get("NewZone")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterZoneResponse(AbstractModel):
    """SwitchClusterZone response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async FlowId
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SwitchProxyVpcRequest(AbstractModel):
    """SwitchProxyVpc request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _UniqVpcId: VPC ID in string
        :type UniqVpcId: str
        :param _UniqSubnetId: Subnet ID in string
        :type UniqSubnetId: str
        :param _OldIpReserveHours: Valid hours of old IP
        :type OldIpReserveHours: int
        :param _ProxyGroupId: Database proxy group ID (required), which can be obtained through the `DescribeProxies` API.
        :type ProxyGroupId: str
        """
        self._ClusterId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._OldIpReserveHours = None
        self._ProxyGroupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def OldIpReserveHours(self):
        return self._OldIpReserveHours

    @OldIpReserveHours.setter
    def OldIpReserveHours(self, OldIpReserveHours):
        self._OldIpReserveHours = OldIpReserveHours

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._OldIpReserveHours = params.get("OldIpReserveHours")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchProxyVpcResponse(AbstractModel):
    """SwitchProxyVpc response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class TablePrivileges(AbstractModel):
    """MySQL table permission

    """

    def __init__(self):
        r"""
        :param _Db: Database name
        :type Db: str
        :param _TableName: Table name
        :type TableName: str
        :param _Privileges: Permission list
        :type Privileges: list of str
        """
        self._Db = None
        self._TableName = None
        self._Privileges = None

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._TableName = params.get("TableName")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Information of tags associated with cluster, including `TagKey` and `TagValue`

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
        


class TemplateParamInfo(AbstractModel):
    """Parameter template details

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _Default: Default value
        :type Default: str
        :param _EnumValue: The collection of valid value types when parameter type is `enum`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnumValue: list of str
        :param _Max: Maximum value when parameter type is `float` or `integer`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Max: str
        :param _Min: Minimum value when parameter type is `float` or `integer`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Min: str
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _NeedReboot: Whether to restart the instance for the parameter to take effect
        :type NeedReboot: int
        :param _Description: Parameter description
        :type Description: str
        :param _ParamType: Parameter type. Valid value: `integer`, `float`, `string`, `enum`.
        :type ParamType: str
        """
        self._CurrentValue = None
        self._Default = None
        self._EnumValue = None
        self._Max = None
        self._Min = None
        self._ParamName = None
        self._NeedReboot = None
        self._Description = None
        self._ParamType = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._Default = params.get("Default")
        self._EnumValue = params.get("EnumValue")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._ParamName = params.get("ParamName")
        self._NeedReboot = params.get("NeedReboot")
        self._Description = params.get("Description")
        self._ParamType = params.get("ParamType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradePrice(AbstractModel):
    """Billing details

    """

    def __init__(self):
        r"""
        :param _TotalPrice: The non-discounted total price of monthly subscribed resources (unit: US cent)
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPrice: int
        :param _Discount: Total discount. `100` means no discount.
        :type Discount: float
        :param _TotalPriceDiscount: The discounted total price of monthly subscribed resources (unit: US cent). If a discount is applied, `TotalPriceDiscount` will be the product of `TotalPrice` and `Discount`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPriceDiscount: int
        :param _UnitPrice: The non-discounted unit price of pay-as-you-go resources (unit: US cent)
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPrice: int
        :param _UnitPriceDiscount: The discounted unit price of pay-as-you-go resources (unit: US cent). If a discount is applied, `UnitPriceDiscount` will be the product of `UnitPrice` and `Discount`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: int
        :param _ChargeUnit: Price unit
        :type ChargeUnit: str
        """
        self._TotalPrice = None
        self._Discount = None
        self._TotalPriceDiscount = None
        self._UnitPrice = None
        self._UnitPriceDiscount = None
        self._ChargeUnit = None

    @property
    def TotalPrice(self):
        return self._TotalPrice

    @TotalPrice.setter
    def TotalPrice(self, TotalPrice):
        self._TotalPrice = TotalPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def TotalPriceDiscount(self):
        return self._TotalPriceDiscount

    @TotalPriceDiscount.setter
    def TotalPriceDiscount(self, TotalPriceDiscount):
        self._TotalPriceDiscount = TotalPriceDiscount

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit


    def _deserialize(self, params):
        self._TotalPrice = params.get("TotalPrice")
        self._Discount = params.get("Discount")
        self._TotalPriceDiscount = params.get("TotalPriceDiscount")
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._ChargeUnit = params.get("ChargeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindClusterResourcePackagesRequest(AbstractModel):
    """UnbindClusterResourcePackages request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _PackageIds: The unique ID of a resource pack. If this parameter is left empty, all resource packs of the instance will be unbound.
        :type PackageIds: list of str
        """
        self._ClusterId = None
        self._PackageIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def PackageIds(self):
        return self._PackageIds

    @PackageIds.setter
    def PackageIds(self, PackageIds):
        self._PackageIds = PackageIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._PackageIds = params.get("PackageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindClusterResourcePackagesResponse(AbstractModel):
    """UnbindClusterResourcePackages response structure.

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


class UpgradeClusterVersionRequest(AbstractModel):
    """UpgradeClusterVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _CynosVersion: Kernel version
        :type CynosVersion: str
        :param _UpgradeType: Upgrade time type. Valid values: `upgradeImmediate`, `upgradeInMaintain`.
        :type UpgradeType: str
        """
        self._ClusterId = None
        self._CynosVersion = None
        self._UpgradeType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def UpgradeType(self):
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._CynosVersion = params.get("CynosVersion")
        self._UpgradeType = params.get("UpgradeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterVersionResponse(AbstractModel):
    """UpgradeClusterVersion response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Cpu: Database CPU
        :type Cpu: int
        :param _Memory: Database memory in GB
        :type Memory: int
        :param _UpgradeType: Upgrade type. Valid values: upgradeImmediate, upgradeInMaintain
        :type UpgradeType: str
        :param _StorageLimit: This parameter has been disused.
        :type StorageLimit: int
        :param _AutoVoucher: Whether to automatically select a voucher. 1: yes; 0: no. Default value: 0
        :type AutoVoucher: int
        :param _DbType: This parameter has been disused.
        :type DbType: str
        :param _DealMode: Transaction mode. Valid values: `0` (place and pay for an order), `1` (place an order)
        :type DealMode: int
        :param _UpgradeMode: Valid values: `NormalUpgrade` (Normal mode), `FastUpgrade` (QuickChange). If the system detects that the configuration modification process will cause a momentary disconnection, the process will be terminated.
        :type UpgradeMode: str
        """
        self._InstanceId = None
        self._Cpu = None
        self._Memory = None
        self._UpgradeType = None
        self._StorageLimit = None
        self._AutoVoucher = None
        self._DbType = None
        self._DealMode = None
        self._UpgradeMode = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def UpgradeType(self):
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DealMode(self):
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def UpgradeMode(self):
        return self._UpgradeMode

    @UpgradeMode.setter
    def UpgradeMode(self, UpgradeMode):
        self._UpgradeMode = UpgradeMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._UpgradeType = params.get("UpgradeType")
        self._StorageLimit = params.get("StorageLimit")
        self._AutoVoucher = params.get("AutoVoucher")
        self._DbType = params.get("DbType")
        self._DealMode = params.get("DealMode")
        self._UpgradeMode = params.get("UpgradeMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TranId: Freezing transaction ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param _BigDealIds: Big order ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BigDealIds: list of str
        :param _DealNames: Order ID
        :type DealNames: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TranId = None
        self._BigDealIds = None
        self._DealNames = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._BigDealIds = params.get("BigDealIds")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class UpgradeProxyRequest(AbstractModel):
    """UpgradeProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Mem: Memory
        :type Mem: int
        :param _ProxyCount: Number of nodes in the proxy group
        :type ProxyCount: int
        :param _ProxyGroupId: ID of the database proxy group (disused)
        :type ProxyGroupId: str
        :param _ReloadBalance: Load rebalance mode. Valid values: `auto`, `manual`
        :type ReloadBalance: str
        :param _IsInMaintainPeriod: Upgrade time. Valid values: `no` (upon upgrade completion), `timeWindow` (upgrade during instance maintenance time)
        :type IsInMaintainPeriod: str
        :param _ProxyZones: Node information of the atabase proxy
        :type ProxyZones: list of ProxyZone
        """
        self._ClusterId = None
        self._Cpu = None
        self._Mem = None
        self._ProxyCount = None
        self._ProxyGroupId = None
        self._ReloadBalance = None
        self._IsInMaintainPeriod = None
        self._ProxyZones = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def ProxyCount(self):
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ReloadBalance(self):
        return self._ReloadBalance

    @ReloadBalance.setter
    def ReloadBalance(self, ReloadBalance):
        self._ReloadBalance = ReloadBalance

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod

    @property
    def ProxyZones(self):
        return self._ProxyZones

    @ProxyZones.setter
    def ProxyZones(self, ProxyZones):
        self._ProxyZones = ProxyZones


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._ProxyCount = params.get("ProxyCount")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ReloadBalance = params.get("ReloadBalance")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        if params.get("ProxyZones") is not None:
            self._ProxyZones = []
            for item in params.get("ProxyZones"):
                obj = ProxyZone()
                obj._deserialize(item)
                self._ProxyZones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeProxyResponse(AbstractModel):
    """UpgradeProxy response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async flow ID
        :type FlowId: int
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UpgradeProxyVersionRequest(AbstractModel):
    """UpgradeProxyVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _SrcProxyVersion: Current version of database proxy
        :type SrcProxyVersion: str
        :param _DstProxyVersion: Target version of database proxy
        :type DstProxyVersion: str
        :param _ProxyGroupId: Database proxy group ID
        :type ProxyGroupId: str
        :param _IsInMaintainPeriod: Upgrade time. Valid values: `no` (upon upgrade completion), `yes` (upgrade during instance maintenance time)
        :type IsInMaintainPeriod: str
        """
        self._ClusterId = None
        self._SrcProxyVersion = None
        self._DstProxyVersion = None
        self._ProxyGroupId = None
        self._IsInMaintainPeriod = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SrcProxyVersion(self):
        return self._SrcProxyVersion

    @SrcProxyVersion.setter
    def SrcProxyVersion(self, SrcProxyVersion):
        self._SrcProxyVersion = SrcProxyVersion

    @property
    def DstProxyVersion(self):
        return self._DstProxyVersion

    @DstProxyVersion.setter
    def DstProxyVersion(self, DstProxyVersion):
        self._DstProxyVersion = DstProxyVersion

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SrcProxyVersion = params.get("SrcProxyVersion")
        self._DstProxyVersion = params.get("DstProxyVersion")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeProxyVersionResponse(AbstractModel):
    """UpgradeProxyVersion response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async flow ID
        :type FlowId: int
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UserHostPrivilege(AbstractModel):
    """User host permissions

    """

    def __init__(self):
        r"""
        :param _DbUserName: Authorized user
        :type DbUserName: str
        :param _DbHost: Client IP Note: This field may return null, indicating that no valid values can be obtained.
        :type DbHost: str
        :param _DbPrivilege: User permissions Note: This field may return null, indicating that no valid values can be obtained.
        :type DbPrivilege: str
        """
        self._DbUserName = None
        self._DbHost = None
        self._DbPrivilege = None

    @property
    def DbUserName(self):
        return self._DbUserName

    @DbUserName.setter
    def DbUserName(self, DbUserName):
        self._DbUserName = DbUserName

    @property
    def DbHost(self):
        return self._DbHost

    @DbHost.setter
    def DbHost(self, DbHost):
        self._DbHost = DbHost

    @property
    def DbPrivilege(self):
        return self._DbPrivilege

    @DbPrivilege.setter
    def DbPrivilege(self, DbPrivilege):
        self._DbPrivilege = DbPrivilege


    def _deserialize(self, params):
        self._DbUserName = params.get("DbUserName")
        self._DbHost = params.get("DbHost")
        self._DbPrivilege = params.get("DbPrivilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneStockInfo(AbstractModel):
    """Inventory information in an AZ

    """

    def __init__(self):
        r"""
        :param _Zone: AZ
        :type Zone: str
        :param _HasStock: Whether there is an inventory.
        :type HasStock: bool
        :param _StockCount: Quantity in stock
        :type StockCount: int
        """
        self._Zone = None
        self._HasStock = None
        self._StockCount = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def HasStock(self):
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock

    @property
    def StockCount(self):
        return self._StockCount

    @StockCount.setter
    def StockCount(self, StockCount):
        self._StockCount = StockCount


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._HasStock = params.get("HasStock")
        self._StockCount = params.get("StockCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        