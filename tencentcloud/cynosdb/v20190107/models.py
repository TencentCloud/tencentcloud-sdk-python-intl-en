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
        :param _NonsupportSlaveZoneReason: The causes for no support from an availability zone.
        :type NonsupportSlaveZoneReason: str
        :param _IsSupportRo: Whether read-only instance is supported
        :type IsSupportRo: str
        :param _NonsupportRoReason: Reasons why RO instances are not supported.
        :type NonsupportRoReason: str
        :param _IsSupportManualSnapshot: Whether manual snapshot backup initiation is supported.
        :type IsSupportManualSnapshot: str
        :param _IsSupportTransparentDataEncryption: Whether transparent data encryption is supported.
        :type IsSupportTransparentDataEncryption: str
        :param _NoSupportTransparentDataEncryptionReason: Reasons for no support of transparent data encryption.
        :type NoSupportTransparentDataEncryptionReason: str
        :param _IsSupportManualLogic: Whether manual initiation of logical backup is supported.
        :type IsSupportManualLogic: str
        """
        self._IsSupportSlaveZone = None
        self._NonsupportSlaveZoneReason = None
        self._IsSupportRo = None
        self._NonsupportRoReason = None
        self._IsSupportManualSnapshot = None
        self._IsSupportTransparentDataEncryption = None
        self._NoSupportTransparentDataEncryptionReason = None
        self._IsSupportManualLogic = None

    @property
    def IsSupportSlaveZone(self):
        """Whether secondary AZ is supported
        :rtype: str
        """
        return self._IsSupportSlaveZone

    @IsSupportSlaveZone.setter
    def IsSupportSlaveZone(self, IsSupportSlaveZone):
        self._IsSupportSlaveZone = IsSupportSlaveZone

    @property
    def NonsupportSlaveZoneReason(self):
        """The causes for no support from an availability zone.
        :rtype: str
        """
        return self._NonsupportSlaveZoneReason

    @NonsupportSlaveZoneReason.setter
    def NonsupportSlaveZoneReason(self, NonsupportSlaveZoneReason):
        self._NonsupportSlaveZoneReason = NonsupportSlaveZoneReason

    @property
    def IsSupportRo(self):
        """Whether read-only instance is supported
        :rtype: str
        """
        return self._IsSupportRo

    @IsSupportRo.setter
    def IsSupportRo(self, IsSupportRo):
        self._IsSupportRo = IsSupportRo

    @property
    def NonsupportRoReason(self):
        """Reasons why RO instances are not supported.
        :rtype: str
        """
        return self._NonsupportRoReason

    @NonsupportRoReason.setter
    def NonsupportRoReason(self, NonsupportRoReason):
        self._NonsupportRoReason = NonsupportRoReason

    @property
    def IsSupportManualSnapshot(self):
        """Whether manual snapshot backup initiation is supported.
        :rtype: str
        """
        return self._IsSupportManualSnapshot

    @IsSupportManualSnapshot.setter
    def IsSupportManualSnapshot(self, IsSupportManualSnapshot):
        self._IsSupportManualSnapshot = IsSupportManualSnapshot

    @property
    def IsSupportTransparentDataEncryption(self):
        """Whether transparent data encryption is supported.
        :rtype: str
        """
        return self._IsSupportTransparentDataEncryption

    @IsSupportTransparentDataEncryption.setter
    def IsSupportTransparentDataEncryption(self, IsSupportTransparentDataEncryption):
        self._IsSupportTransparentDataEncryption = IsSupportTransparentDataEncryption

    @property
    def NoSupportTransparentDataEncryptionReason(self):
        """Reasons for no support of transparent data encryption.
        :rtype: str
        """
        return self._NoSupportTransparentDataEncryptionReason

    @NoSupportTransparentDataEncryptionReason.setter
    def NoSupportTransparentDataEncryptionReason(self, NoSupportTransparentDataEncryptionReason):
        self._NoSupportTransparentDataEncryptionReason = NoSupportTransparentDataEncryptionReason

    @property
    def IsSupportManualLogic(self):
        """Whether manual initiation of logical backup is supported.
        :rtype: str
        """
        return self._IsSupportManualLogic

    @IsSupportManualLogic.setter
    def IsSupportManualLogic(self, IsSupportManualLogic):
        self._IsSupportManualLogic = IsSupportManualLogic


    def _deserialize(self, params):
        self._IsSupportSlaveZone = params.get("IsSupportSlaveZone")
        self._NonsupportSlaveZoneReason = params.get("NonsupportSlaveZoneReason")
        self._IsSupportRo = params.get("IsSupportRo")
        self._NonsupportRoReason = params.get("NonsupportRoReason")
        self._IsSupportManualSnapshot = params.get("IsSupportManualSnapshot")
        self._IsSupportTransparentDataEncryption = params.get("IsSupportTransparentDataEncryption")
        self._NoSupportTransparentDataEncryptionReason = params.get("NoSupportTransparentDataEncryptionReason")
        self._IsSupportManualLogic = params.get("IsSupportManualLogic")
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
        """Database account name
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Description(self):
        """Database account description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Host(self):
        """Host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def MaxUserConnections(self):
        """The max connections
        :rtype: int
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdList(self):
        """List of instance IDs in the format of `cynosdbmysql-ins-n7ocdslw` as displayed in the TDSQL-C for MySQL console. You can use the instance list querying API to query the ID, i.e., the `InstanceId` value in the output parameters.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SlaveZone(self):
        """Replica AZ
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async FlowId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Cpu(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Memory in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def ReadOnlyCount(self):
        """Number of added read-only instances. Value range: (0,16].
        :rtype: int
        """
        return self._ReadOnlyCount

    @ReadOnlyCount.setter
    def ReadOnlyCount(self, ReadOnlyCount):
        self._ReadOnlyCount = ReadOnlyCount

    @property
    def InstanceGrpId(self):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        """Instance group ID, which will be used when you add an instance in an existing RO group. If this parameter is left empty, an RO group will be created. But it is not recommended to pass in this parameter for the current version, as this version has been disused.
        :rtype: str
        """
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        self._InstanceGrpId = InstanceGrpId

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID. If `VpcId` is set, `SubnetId` is required.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Port(self):
        """The port used when adding an RO group. Value range: [0,65535).
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceName(self):
        """Instance name. String length range: [0,64).
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AutoVoucher(self):
        """Whether to automatically select a voucher. 1: yes; 0: no. Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def DbType(self):
        """Database type. Valid values: 
<li> MYSQL </li>
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def OrderSource(self):
        """Order source. String length range: [0,64).
        :rtype: str
        """
        return self._OrderSource

    @OrderSource.setter
    def OrderSource(self, OrderSource):
        self._OrderSource = OrderSource

    @property
    def DealMode(self):
        """Transaction mode. Valid values: `0` (place and pay for an order), `1` (place an order)
        :rtype: int
        """
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def ParamTemplateId(self):
        """Parameter template ID
        :rtype: int
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def InstanceParams(self):
        """Parameter list, which is valid only if `InstanceParams` is passed in to `ParamTemplateId`.
        :rtype: list of ModifyParamItem
        """
        return self._InstanceParams

    @InstanceParams.setter
    def InstanceParams(self, InstanceParams):
        self._InstanceParams = InstanceParams

    @property
    def SecurityGroupIds(self):
        """Security group ID. You can specify an security group when creating a read-only instance.
        :rtype: list of str
        """
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
        :param _TranId: Freeze transaction. one frozen transaction is activated at a time.
        :type TranId: str
        :param _DealNames: Specifies the post-paid order number.
        :type DealNames: list of str
        :param _ResourceIds: Delivery resource id list.
        :type ResourceIds: list of str
        :param _BigDealIds: Large order number.
        :type BigDealIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TranId = None
        self._DealNames = None
        self._ResourceIds = None
        self._BigDealIds = None
        self._RequestId = None

    @property
    def TranId(self):
        """Freeze transaction. one frozen transaction is activated at a time.
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def DealNames(self):
        """Specifies the post-paid order number.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ResourceIds(self):
        """Delivery resource id list.
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def BigDealIds(self):
        """Large order number.
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """IP address
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        """Port
        :rtype: int
        """
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
        :param _RuleFilters: A single audit rule.
        :type RuleFilters: list of RuleFilters
        """
        self._RuleFilters = None

    @property
    def RuleFilters(self):
        """A single audit rule.
        :rtype: list of RuleFilters
        """
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
        :param _Description: Rule template description.
        :type Description: str
        :param _CreateAt: Creation time of a rule template
        :type CreateAt: str
        :param _UpdateAt: Rule template modification time.
        :type UpdateAt: str
        :param _AlarmLevel: Alarm level. valid values: 1 (low risk), 2 (medium risk), 3 (high risk).
        :type AlarmLevel: int
        :param _AlarmPolicy: Alarm policy. 0 - no alert, 1 - alert.
        :type AlarmPolicy: int
        :param _Status: Template status. 0 - no task, 1 - modifying.
        :type Status: int
        :param _AffectedInstances: Template application is used in which instances.
        :type AffectedInstances: list of str
        """
        self._RuleTemplateId = None
        self._RuleTemplateName = None
        self._RuleFilters = None
        self._Description = None
        self._CreateAt = None
        self._UpdateAt = None
        self._AlarmLevel = None
        self._AlarmPolicy = None
        self._Status = None
        self._AffectedInstances = None

    @property
    def RuleTemplateId(self):
        """Rule template ID
        :rtype: str
        """
        return self._RuleTemplateId

    @RuleTemplateId.setter
    def RuleTemplateId(self, RuleTemplateId):
        self._RuleTemplateId = RuleTemplateId

    @property
    def RuleTemplateName(self):
        """Rule template name
        :rtype: str
        """
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def RuleFilters(self):
        """Filter of the rule template
        :rtype: list of RuleFilters
        """
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def Description(self):
        """Rule template description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateAt(self):
        """Creation time of a rule template
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        """Rule template modification time.
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def AlarmLevel(self):
        """Alarm level. valid values: 1 (low risk), 2 (medium risk), 3 (high risk).
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmPolicy(self):
        """Alarm policy. 0 - no alert, 1 - alert.
        :rtype: int
        """
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy

    @property
    def Status(self):
        """Template status. 0 - no task, 1 - modifying.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AffectedInstances(self):
        """Template application is used in which instances.
        :rtype: list of str
        """
        return self._AffectedInstances

    @AffectedInstances.setter
    def AffectedInstances(self, AffectedInstances):
        self._AffectedInstances = AffectedInstances


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
        self._UpdateAt = params.get("UpdateAt")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmPolicy = params.get("AlarmPolicy")
        self._Status = params.get("Status")
        self._AffectedInstances = params.get("AffectedInstances")
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
        :param _BackupId: Backup ID.
        :type BackupId: int
        :param _SnapShotType: Specifies the snapshot type. valid values: full (full snapshot); increment (incremental snapshot).
        :type SnapShotType: str
        :param _BackupName: Specifies the remark of the backup file.
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
        """Snapshot file ID, which is deprecated. You need to use `BackupId`.
        :rtype: int
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def FileName(self):
        """Backup file name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """Backup file size
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def StartTime(self):
        """Backup start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        """Backup end time
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def BackupType(self):
        """Backup type. Valid values: `snapshot` (snapshot backup), `logic` (logic backup).
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupMethod(self):
        """Back mode. auto: auto backup; manual: manual backup
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupStatus(self):
        """Backup file status. success: backup succeeded; fail: backup failed; creating: creating backup file; deleting: deleting backup file
        :rtype: str
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def SnapshotTime(self):
        """Backup file time
        :rtype: str
        """
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime

    @property
    def BackupId(self):
        """Backup ID.
        :rtype: int
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def SnapShotType(self):
        """Specifies the snapshot type. valid values: full (full snapshot); increment (incremental snapshot).
        :rtype: str
        """
        return self._SnapShotType

    @SnapShotType.setter
    def SnapShotType(self, SnapShotType):
        self._SnapShotType = SnapShotType

    @property
    def BackupName(self):
        """Specifies the remark of the backup file.
        :rtype: str
        """
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
        


class BackupLimitClusterRestriction(AbstractModel):
    """Specifies the backup download cluster restrictions parameter.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _BackupLimitRestriction: Download limit configuration.
        :type BackupLimitRestriction: :class:`tencentcloud.cynosdb.v20190107.models.BackupLimitRestriction`
        """
        self._ClusterId = None
        self._BackupLimitRestriction = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupLimitRestriction(self):
        """Download limit configuration.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.BackupLimitRestriction`
        """
        return self._BackupLimitRestriction

    @BackupLimitRestriction.setter
    def BackupLimitRestriction(self, BackupLimitRestriction):
        self._BackupLimitRestriction = BackupLimitRestriction


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("BackupLimitRestriction") is not None:
            self._BackupLimitRestriction = BackupLimitRestriction()
            self._BackupLimitRestriction._deserialize(params.get("BackupLimitRestriction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupLimitRestriction(AbstractModel):
    """Specifies the backup download limit parameter.

    """

    def __init__(self):
        r"""
        :param _LimitType: Restriction type.
        :type LimitType: str
        :param _VpcComparisonSymbol: This parameter only supports In, which indicates that the vpc specified by LimitVpc can be downloaded. the default is In.
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: Specified ips can download; specified ips are not allowed to download.
        :type IpComparisonSymbol: str
        :param _LimitVpcs: Specifies the vpc setting for download restrictions.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LimitVpcs: list of BackupLimitVpcItem
        :param _LimitIps: Specifies the ip settings for limiting downloads.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LimitIps: list of str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpcs = None
        self._LimitIps = None

    @property
    def LimitType(self):
        """Restriction type.
        :rtype: str
        """
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        """This parameter only supports In, which indicates that the vpc specified by LimitVpc can be downloaded. the default is In.
        :rtype: str
        """
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        """Specified ips can download; specified ips are not allowed to download.
        :rtype: str
        """
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpcs(self):
        """Specifies the vpc setting for download restrictions.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BackupLimitVpcItem
        """
        return self._LimitVpcs

    @LimitVpcs.setter
    def LimitVpcs(self, LimitVpcs):
        self._LimitVpcs = LimitVpcs

    @property
    def LimitIps(self):
        """Specifies the ip settings for limiting downloads.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._LimitIps

    @LimitIps.setter
    def LimitIps(self, LimitIps):
        self._LimitIps = LimitIps


    def _deserialize(self, params):
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpcs") is not None:
            self._LimitVpcs = []
            for item in params.get("LimitVpcs"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpcs.append(obj)
        self._LimitIps = params.get("LimitIps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupLimitVpcItem(AbstractModel):
    """VPC settings for restricting backup download sources.

    """

    def __init__(self):
        r"""
        :param _Region: Specifies the region for limiting download sources. currently only supports the current region.
        :type Region: str
        :param _VpcList: Limit the vpc list for downloads.
        :type VpcList: list of str
        """
        self._Region = None
        self._VpcList = None

    @property
    def Region(self):
        """Specifies the region for limiting download sources. currently only supports the current region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcList(self):
        """Limit the vpc list for downloads.
        :rtype: list of str
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._VpcList = params.get("VpcList")
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        """Instance ID list
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DealName(self):
        """Order ID
        :rtype: str
        """
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
        """The unique ID of a resource pack
        :rtype: list of str
        """
        return self._PackageIds

    @PackageIds.setter
    def PackageIds(self, PackageIds):
        self._PackageIds = PackageIds

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _InstanceId: ID of the bound cluster.
        :type InstanceId: str
        :param _InstanceRegion: The region where the bound instance is located.
        :type InstanceRegion: str
        :param _InstanceType: Type of the bound instance.
        :type InstanceType: str
        :param _ExtendIds: The instance ID under the bound cluster.
        :type ExtendIds: list of str
        """
        self._InstanceId = None
        self._InstanceRegion = None
        self._InstanceType = None
        self._ExtendIds = None

    @property
    def InstanceId(self):
        """ID of the bound cluster.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRegion(self):
        """The region where the bound instance is located.
        :rtype: str
        """
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def InstanceType(self):
        """Type of the bound instance.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ExtendIds(self):
        """The instance ID under the bound cluster.
        :rtype: list of str
        """
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
        


class BinlogConfigInfo(AbstractModel):
    """Specifies the binlog configuration message.

    """

    def __init__(self):
        r"""
        :param _BinlogSaveDays: Specifies the retention time of binlogs.
        :type BinlogSaveDays: int
        :param _BinlogCrossRegionsEnable: Whether binlog cross-region backup is enabled.
        :type BinlogCrossRegionsEnable: str
        :param _BinlogCrossRegions: binlog in a different region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BinlogCrossRegions: list of str
        """
        self._BinlogSaveDays = None
        self._BinlogCrossRegionsEnable = None
        self._BinlogCrossRegions = None

    @property
    def BinlogSaveDays(self):
        """Specifies the retention time of binlogs.
        :rtype: int
        """
        return self._BinlogSaveDays

    @BinlogSaveDays.setter
    def BinlogSaveDays(self, BinlogSaveDays):
        self._BinlogSaveDays = BinlogSaveDays

    @property
    def BinlogCrossRegionsEnable(self):
        """Whether binlog cross-region backup is enabled.
        :rtype: str
        """
        return self._BinlogCrossRegionsEnable

    @BinlogCrossRegionsEnable.setter
    def BinlogCrossRegionsEnable(self, BinlogCrossRegionsEnable):
        self._BinlogCrossRegionsEnable = BinlogCrossRegionsEnable

    @property
    def BinlogCrossRegions(self):
        """binlog in a different region.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._BinlogCrossRegions

    @BinlogCrossRegions.setter
    def BinlogCrossRegions(self, BinlogCrossRegions):
        self._BinlogCrossRegions = BinlogCrossRegions


    def _deserialize(self, params):
        self._BinlogSaveDays = params.get("BinlogSaveDays")
        self._BinlogCrossRegionsEnable = params.get("BinlogCrossRegionsEnable")
        self._BinlogCrossRegions = params.get("BinlogCrossRegions")
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
        """Binlog filename
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """File size in bytes
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def StartTime(self):
        """Transaction start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        """Transaction end time
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def BinlogId(self):
        """Binlog file ID
        :rtype: int
        """
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
        """Instance ID
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
        


class CloseAuditServiceResponse(AbstractModel):
    """CloseAuditService response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster IDs in array
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloseProxyEndPointRequest(AbstractModel):
    """CloseProxyEndPoint request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ProxyGroupId: Database proxy group ID.
        :type ProxyGroupId: str
        """
        self._ClusterId = None
        self._ProxyGroupId = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        """Database proxy group ID.
        :rtype: str
        """
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
        


class CloseProxyEndPointResponse(AbstractModel):
    """CloseProxyEndPoint response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async process ID.
        :type FlowId: int
        :param _TaskId: Asynchronous Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async process ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        """Asynchronous Task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        """Database proxy group ID
        :rtype: str
        """
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def OnlyCloseRW(self):
        """Whether only to disable read/write separation. Valid values: `true`, `false`.
        :rtype: bool
        """
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
        """Async flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        """Async task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CloseSSLRequest(AbstractModel):
    """CloseSSL request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._ClusterId = None
        self._InstanceId = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseSSLResponse(AbstractModel):
    """CloseSSL response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID

Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _TaskId: Task ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Process ID

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        """Task ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        """Instance group ID
        :rtype: str
        """
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _MaintainStartTime: Execution start time (seconds from 0 o'clock).	
        :type MaintainStartTime: int
        :param _MaintainDuration: Specifies the continuous time. the unit is second.	
        :type MaintainDuration: int
        :param _MaintainWeekDays: Specifies the time when it can be executed. valid values: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].
        :type MaintainWeekDays: list of str
        :param _ServerlessStatus: serverless instance substatus.
        :type ServerlessStatus: str
        :param _InstanceTasks: Instance task information.
        :type InstanceTasks: list of ObjectTask
        :param _InstanceDeviceType: Instance machine type.
        :type InstanceDeviceType: str
        :param _InstanceStorageType: Instance storage type.
        :type InstanceStorageType: str
        :param _DbMode: Database type.
        :type DbMode: str
        :param _NodeList: Node list
        :type NodeList: list of str
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
        self._InstanceStorageType = None
        self._DbMode = None
        self._NodeList = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        """Engine type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        """Instance status
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def InstanceStatusDesc(self):
        """Instance status description
        :rtype: str
        """
        return self._InstanceStatusDesc

    @InstanceStatusDesc.setter
    def InstanceStatusDesc(self, InstanceStatusDesc):
        self._InstanceStatusDesc = InstanceStatusDesc

    @property
    def InstanceCpu(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._InstanceCpu

    @InstanceCpu.setter
    def InstanceCpu(self, InstanceCpu):
        self._InstanceCpu = InstanceCpu

    @property
    def InstanceMemory(self):
        """Memory
        :rtype: int
        """
        return self._InstanceMemory

    @InstanceMemory.setter
    def InstanceMemory(self, InstanceMemory):
        self._InstanceMemory = InstanceMemory

    @property
    def InstanceStorage(self):
        """Disk
        :rtype: int
        """
        return self._InstanceStorage

    @InstanceStorage.setter
    def InstanceStorage(self, InstanceStorage):
        self._InstanceStorage = InstanceStorage

    @property
    def InstanceRole(self):
        """Instance role
        :rtype: str
        """
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def MaintainStartTime(self):
        """Execution start time (seconds from 0 o'clock).	
        :rtype: int
        """
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        """Specifies the continuous time. the unit is second.	
        :rtype: int
        """
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        """Specifies the time when it can be executed. valid values: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].
        :rtype: list of str
        """
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays

    @property
    def ServerlessStatus(self):
        """serverless instance substatus.
        :rtype: str
        """
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def InstanceTasks(self):
        """Instance task information.
        :rtype: list of ObjectTask
        """
        return self._InstanceTasks

    @InstanceTasks.setter
    def InstanceTasks(self, InstanceTasks):
        self._InstanceTasks = InstanceTasks

    @property
    def InstanceDeviceType(self):
        """Instance machine type.
        :rtype: str
        """
        return self._InstanceDeviceType

    @InstanceDeviceType.setter
    def InstanceDeviceType(self, InstanceDeviceType):
        self._InstanceDeviceType = InstanceDeviceType

    @property
    def InstanceStorageType(self):
        """Instance storage type.
        :rtype: str
        """
        return self._InstanceStorageType

    @InstanceStorageType.setter
    def InstanceStorageType(self, InstanceStorageType):
        self._InstanceStorageType = InstanceStorageType

    @property
    def DbMode(self):
        """Database type.
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def NodeList(self):
        """Node list
        :rtype: list of str
        """
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList


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
        self._InstanceStorageType = params.get("InstanceStorageType")
        self._DbMode = params.get("DbMode")
        self._NodeList = params.get("NodeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterReadOnlyValue(AbstractModel):
    """Cluster read-only switch list.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ReadOnlyValue: Specifies the value of the read-only switch.
        :type ReadOnlyValue: str
        """
        self._ClusterId = None
        self._ReadOnlyValue = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ReadOnlyValue(self):
        """Specifies the value of the read-only switch.
        :rtype: str
        """
        return self._ReadOnlyValue

    @ReadOnlyValue.setter
    def ReadOnlyValue(self, ReadOnlyValue):
        self._ReadOnlyValue = ReadOnlyValue


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ReadOnlyValue = params.get("ReadOnlyValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterTaskId(AbstractModel):
    """Cluster task ID.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _TaskId: Task ID
        :type TaskId: str
        """
        self._ClusterId = None
        self._TaskId = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TaskId(self):
        """Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TaskId = params.get("TaskId")
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
        """A parameter used to replicate the array of cluster IDs
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def SourceClusterId(self):
        """Cluster ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Accounts(self):
        """List of new accounts
        :rtype: list of NewAccount
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Audit rule
        :rtype: list of RuleFilters
        """
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def RuleTemplateName(self):
        """Rule template name
        :rtype: str
        """
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def Description(self):
        """Rule template description.
        :rtype: str
        """
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
        :param _RuleTemplateId: The generated rule template ID.
        :type RuleTemplateId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleTemplateId = None
        self._RequestId = None

    @property
    def RuleTemplateId(self):
        """The generated rule template ID.
        :rtype: str
        """
        return self._RuleTemplateId

    @RuleTemplateId.setter
    def RuleTemplateId(self, RuleTemplateId):
        self._RuleTemplateId = RuleTemplateId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupType(self):
        """Backup type. Valid values: `logic` (logic backup), `snapshot` (physical backup)
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupDatabases(self):
        """Backup database, which is valid when `BackupType` is `logic`.
        :rtype: list of str
        """
        return self._BackupDatabases

    @BackupDatabases.setter
    def BackupDatabases(self, BackupDatabases):
        self._BackupDatabases = BackupDatabases

    @property
    def BackupTables(self):
        """Backup table, which is valid when `BackupType` is `logic`.
        :rtype: list of DatabaseTables
        """
        return self._BackupTables

    @BackupTables.setter
    def BackupTables(self, BackupTables):
        self._BackupTables = BackupTables

    @property
    def BackupName(self):
        """Backup name
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbName(self):
        """Database name
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CharacterSet(self):
        """Character set
        :rtype: str
        """
        return self._CharacterSet

    @CharacterSet.setter
    def CharacterSet(self, CharacterSet):
        self._CharacterSet = CharacterSet

    @property
    def CollateRule(self):
        """Collation
        :rtype: str
        """
        return self._CollateRule

    @CollateRule.setter
    def CollateRule(self, CollateRule):
        self._CollateRule = CollateRule

    @property
    def UserHostPrivileges(self):
        """Host permissions of the authorized user
        :rtype: list of UserHostPrivilege
        """
        return self._UserHostPrivileges

    @UserHostPrivileges.setter
    def UserHostPrivileges(self, UserHostPrivileges):
        self._UserHostPrivileges = UserHostPrivileges

    @property
    def Description(self):
        """Remarks
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _InstanceCount: Instance count. valid values: a quantity range from 0 to 16. the default value is 2 (that is, one rw instance + one ro instance). the transmitted n represents 1 rw instance + (n - 1) ro instances (with identical specifications). if a more precise cluster composition collocation is required, please use InstanceInitInfos.
        :type InstanceCount: int
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
        :param _TimeSpan: Purchase duration of monthly subscription plan
        :type TimeSpan: int
        :param _TimeUnit: Duration unit of monthly subscription. Valid values: `s`, `d`, `m`, `y`
        :type TimeUnit: str
        :param _AutoRenewFlag: Specifies whether the annual/monthly subscription is auto-renewed. the default value is 0.
0 indicates the default renewal method. 1 means auto-renewal. 2 means no auto-renewal.
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
        self._InstanceCount = None
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
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DbType(self):
        """Database type. Valid values: 
<li> MYSQL </li>
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        """Database version. Valid values: 
<li> Valid values for `MYSQL`: 5.7 and 8.0 </li>
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def ProjectId(self):
        """Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Cpu(self):
        """It is required when `DbMode` is set to `NORMAL` or left empty.
Number of CPU cores of normal instance
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """It is required when `DbMode` is set to `NORMAL` or left empty.
Memory of a non-serverless instance in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceCount(self):
        """Instance count. valid values: a quantity range from 0 to 16. the default value is 2 (that is, one rw instance + one ro instance). the transmitted n represents 1 rw instance + (n - 1) ro instances (with identical specifications). if a more precise cluster composition collocation is required, please use InstanceInitInfos.
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Storage(self):
        """This parameter has been deprecated.
Storage capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ClusterName(self):
        """Cluster name, which can contain less than 64 letters, digits, or symbols (-_.).
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def AdminPassword(self):
        """Account password, which must contain 8-64 characters in at least three of the following four types: uppercase letters, lowercase letters, digits, and symbols (~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/).
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Port(self):
        """Port. Valid range: [0, 65535). Default value: 3306
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def PayMode(self):
        """Billing mode. `0`: pay-as-you-go; `1`: monthly subscription. Default value: `0`
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Count(self):
        """Number of purchased clusters. Valid range: [1,50]. Default value: 1
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RollbackStrategy(self):
        """Rollback type:
noneRollback: no rollback;
snapRollback: rollback by snapshot;
timeRollback: rollback by time point
        :rtype: str
        """
        return self._RollbackStrategy

    @RollbackStrategy.setter
    def RollbackStrategy(self, RollbackStrategy):
        self._RollbackStrategy = RollbackStrategy

    @property
    def RollbackId(self):
        """`snapshotId` for snapshot rollback or `queryId` for time point rollback. 0 indicates to determine whether the time point is valid
        :rtype: int
        """
        return self._RollbackId

    @RollbackId.setter
    def RollbackId(self, RollbackId):
        self._RollbackId = RollbackId

    @property
    def OriginalClusterId(self):
        """The source cluster ID passed in during rollback to find the source `poolId`
        :rtype: str
        """
        return self._OriginalClusterId

    @OriginalClusterId.setter
    def OriginalClusterId(self, OriginalClusterId):
        self._OriginalClusterId = OriginalClusterId

    @property
    def ExpectTime(self):
        """Specified time for time point rollback or snapshot time for snapshot rollback
        :rtype: str
        """
        return self._ExpectTime

    @ExpectTime.setter
    def ExpectTime(self, ExpectTime):
        self._ExpectTime = ExpectTime

    @property
    def ExpectTimeThresh(self):
        """This parameter has been deprecated.
Specified allowed time range for time point rollback
        :rtype: int
        """
        return self._ExpectTimeThresh

    @ExpectTimeThresh.setter
    def ExpectTimeThresh(self, ExpectTimeThresh):
        self._ExpectTimeThresh = ExpectTimeThresh

    @property
    def StorageLimit(self):
        """Storage upper limit of normal instance in GB
If `DbType` is `MYSQL` and the storage billing mode is monthly subscription, the parameter value can’t exceed the maximum storage corresponding to the CPU and memory specifications.
        :rtype: int
        """
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def TimeSpan(self):
        """Purchase duration of monthly subscription plan
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """Duration unit of monthly subscription. Valid values: `s`, `d`, `m`, `y`
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def AutoRenewFlag(self):
        """Specifies whether the annual/monthly subscription is auto-renewed. the default value is 0.
0 indicates the default renewal method. 1 means auto-renewal. 2 means no auto-renewal.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        """Whether to automatically select a voucher. `1`: yes; `0`: no. Default value: `0`
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def HaCount(self):
        """Number of instances (this parameter has been disused and is retained only for compatibility with existing instances)
        :rtype: int
        """
        return self._HaCount

    @HaCount.setter
    def HaCount(self, HaCount):
        self._HaCount = HaCount

    @property
    def OrderSource(self):
        """Order source
        :rtype: str
        """
        return self._OrderSource

    @OrderSource.setter
    def OrderSource(self, OrderSource):
        self._OrderSource = OrderSource

    @property
    def ResourceTags(self):
        """Array of tags to be bound to the created cluster
        :rtype: list of Tag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbMode(self):
        """Database type
Valid values when `DbType` is `MYSQL` (default value: `NORMAL`):
<li>NORMAL</li>
<li>SERVERLESS</li>
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def MinCpu(self):
        """This parameter is required if `DbMode` is `SERVERLESS`.
Minimum number of CPU cores. For the value range, see the returned result of `DescribeServerlessInstanceSpecs`.
        :rtype: float
        """
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        """This parameter is required if `DbMode` is `SERVERLESS`.
Maximum number of CPU cores. For the value range, see the returned result of `DescribeServerlessInstanceSpecs`.
        :rtype: float
        """
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def AutoPause(self):
        """This parameter specifies whether the cluster will be automatically paused if `DbMode` is `SERVERLESS`. Valid values:
<li>yes</li>
<li>no</li>
Default value: yes
        :rtype: str
        """
        return self._AutoPause

    @AutoPause.setter
    def AutoPause(self, AutoPause):
        self._AutoPause = AutoPause

    @property
    def AutoPauseDelay(self):
        """This parameter specifies the delay for automatic cluster pause in seconds if `DbMode` is `SERVERLESS`. Value range: [600,691200]
Default value: `600`
        :rtype: int
        """
        return self._AutoPauseDelay

    @AutoPauseDelay.setter
    def AutoPauseDelay(self, AutoPauseDelay):
        self._AutoPauseDelay = AutoPauseDelay

    @property
    def StoragePayMode(self):
        """The billing mode of cluster storage. Valid values: `0` (pay-as-you-go), `1` (monthly subscription). Default value: `0`.
If `DbType` is `MYSQL` and the billing mode of cluster compute is pay-as-you-go (or the `DbMode` is `SERVERLESS`), the billing mode of cluster storage must be pay-as-you-go.
Clusters with storage billed in monthly subscription can’t be cloned or rolled back.
        :rtype: int
        """
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def SecurityGroupIds(self):
        """Array of security group IDs
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AlarmPolicyIds(self):
        """Array of alarm policy IDs
        :rtype: list of str
        """
        return self._AlarmPolicyIds

    @AlarmPolicyIds.setter
    def AlarmPolicyIds(self, AlarmPolicyIds):
        self._AlarmPolicyIds = AlarmPolicyIds

    @property
    def ClusterParams(self):
        """Array of parameters. Valid values: `character_set_server` (utf8｜latin1｜gbk｜utf8mb4), `lower_case_table_names`. 0: case-sensitive; 1: case-insensitive).
        :rtype: list of ParamItem
        """
        return self._ClusterParams

    @ClusterParams.setter
    def ClusterParams(self, ClusterParams):
        self._ClusterParams = ClusterParams

    @property
    def DealMode(self):
        """Transaction mode. Valid values: `0` (place and pay for an order), `1` (place an order)
        :rtype: int
        """
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def ParamTemplateId(self):
        """Parameter template ID, which can be obtained by querying parameter template information “DescribeParamTemplates”
        :rtype: int
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def SlaveZone(self):
        """Multi-AZ address
        :rtype: str
        """
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def InstanceInitInfos(self):
        """Instance initialization configuration information, which is used to select instances with different specifications when purchasing a cluster.
        :rtype: list of InstanceInitInfo
        """
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
        self._InstanceCount = params.get("InstanceCount")
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
        :param _TranId: Frozen transaction ID.
        :type TranId: str
        :param _DealNames: Order ID
        :type DealNames: list of str
        :param _ResourceIds: Resource ID list (this field is no longer maintained. please use the dealNames field and the DescribeResourcesByDealName query API to obtain resource ids.).
        :type ResourceIds: list of str
        :param _ClusterIds: Cluster ID list. this field is no longer maintained. please use the dealNames field and the DescribeResourcesByDealName query API to get the cluster ID.
        :type ClusterIds: list of str
        :param _BigDealIds: Big order ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BigDealIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Frozen transaction ID.
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def DealNames(self):
        """Order ID
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ResourceIds(self):
        """Resource ID list (this field is no longer maintained. please use the dealNames field and the DescribeResourcesByDealName query API to obtain resource ids.).
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ClusterIds(self):
        """Cluster ID list. this field is no longer maintained. please use the dealNames field and the DescribeResourcesByDealName query API to get the cluster ID.
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def BigDealIds(self):
        """Big order ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Template name
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def EngineVersion(self):
        """MySQL version number
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TemplateDescription(self):
        """Template description
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def TemplateId(self):
        """ID of the template to be copied
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DbMode(self):
        """Database type. Valid values:  `NORMAL` (default), `SERVERLESS`.
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def ParamList(self):
        """List of the parameters
        :rtype: list of ParamItem
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        """Template ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def UniqueVpcId(self):
        """VPC ID, which is the same as that of the cluster by default.
        :rtype: str
        """
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        """VPCe subnet ID, which is the same as that of the cluster by default.
        :rtype: str
        """
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def ConnectionPoolType(self):
        """Connection pool type. Valid value: `SessionConnectionPool` (session-level connection pool)
        :rtype: str
        """
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def OpenConnectionPool(self):
        """Whether to enable connection pool. Valid value: `yes` (enable), `no` (disable).
        :rtype: str
        """
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolTimeOut(self):
        """Connection pool threshold in seconds
        :rtype: int
        """
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut

    @property
    def SecurityGroupIds(self):
        """Array of security group IDs
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Vip(self):
        """VIP information
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def WeightMode(self):
        """Weight mode. 
Valid values: `system` (system-assigned), `custom` (custom).
        :rtype: str
        """
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def AutoAddRo(self):
        """Whether to automatically add read-only instance. Valid value: `yes`, `no`.
        :rtype: str
        """
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def FailOver(self):
        """Whether to enable failover
        :rtype: str
        """
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def ConsistencyType(self):
        """Consistency type. Valid values: 
`eventual`, `global`, `session`.
        :rtype: str
        """
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def RwType(self):
        """Read-write attribute. Valid values: 
`READWRITE`, `READONLY`.
        :rtype: str
        """
        return self._RwType

    @RwType.setter
    def RwType(self, RwType):
        self._RwType = RwType

    @property
    def ConsistencyTimeOut(self):
        """Consistency timeout period
        :rtype: int
        """
        return self._ConsistencyTimeOut

    @ConsistencyTimeOut.setter
    def ConsistencyTimeOut(self, ConsistencyTimeOut):
        self._ConsistencyTimeOut = ConsistencyTimeOut

    @property
    def TransSplit(self):
        """Transaction split
        :rtype: bool
        """
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def AccessMode(self):
        """Connection mode. Valid values:
`nearby`, `balance`.
        :rtype: str
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def InstanceWeights(self):
        """Instance weight
        :rtype: list of ProxyInstanceWeight
        """
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
        """Async flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        """Async task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProxyGroupId(self):
        """Database proxy group ID
        :rtype: str
        """
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Cpu(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        """Memory
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def UniqueVpcId(self):
        """VPC ID, which is the same as that of the cluster by default.
        :rtype: str
        """
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        """VPC subnet ID, which is the same as that of the cluster by default.
        :rtype: str
        """
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def ProxyCount(self):
        """Number of nodes in the proxy group
        :rtype: int
        """
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def ConnectionPoolType(self):
        """Connection pool type. Valid value: `SessionConnectionPool` (session-level connection pool)
        :rtype: str
        """
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def OpenConnectionPool(self):
        """Whether to enable connection pool. Valid value: `yes` (enable), `no` (disable).
        :rtype: str
        """
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolTimeOut(self):
        """Connection pool threshold in seconds
        :rtype: int
        """
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut

    @property
    def SecurityGroupIds(self):
        """Array of security group IDs
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProxyZones(self):
        """Database node information
        :rtype: list of ProxyZone
        """
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
        """Async flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        """Async task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProxyGroupId(self):
        """Database proxy group ID
        :rtype: str
        """
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _InstanceType: Instance type. currently fixed to cynosdb-serverless.
        :type InstanceType: str
        :param _PackageRegion: Resource package region of use: chineseMainland - common in the chinese mainland. overseas - universally applicable in hong kong (china), macao (china), taiwan (china), and overseas.
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
        """Instance type. currently fixed to cynosdb-serverless.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PackageRegion(self):
        """Resource package region of use: chineseMainland - common in the chinese mainland. overseas - universally applicable in hong kong (china), macao (china), taiwan (china), and overseas.
        :rtype: str
        """
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def PackageType(self):
        """Resource pack type. Valid values: `CCU` (compute resource pack), `DISK` (storage resource pack).
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageVersion(self):
        """Resource pack edition. Valid values: `base` (basic edition), `common` (general edition), `enterprise` (enterprise edition).
        :rtype: str
        """
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def PackageSpec(self):
        """Resource pack size. Unit of the compute resource pack: Ten thousand.  Unit of the storage resource pack:  GB
        :rtype: float
        """
        return self._PackageSpec

    @PackageSpec.setter
    def PackageSpec(self, PackageSpec):
        self._PackageSpec = PackageSpec

    @property
    def ExpireDay(self):
        """Validity period of a resource pack in days
        :rtype: int
        """
        return self._ExpireDay

    @ExpireDay.setter
    def ExpireDay(self, ExpireDay):
        self._ExpireDay = ExpireDay

    @property
    def PackageCount(self):
        """Number of the resource packs to be purchased
        :rtype: int
        """
        return self._PackageCount

    @PackageCount.setter
    def PackageCount(self, PackageCount):
        self._PackageCount = PackageCount

    @property
    def PackageName(self):
        """Resource pack name
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BigDealIds = None
        self._DealNames = None
        self._RequestId = None

    @property
    def BigDealIds(self):
        """Big order number
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def DealNames(self):
        """Each item has only one `dealName`, through which you need to ensure the idempotency of the delivery API.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :type Uin: str
        :param _DbType: Engine type.
        :type DbType: str
        :param _AppId: User appid.
        :type AppId: int
        :param _StatusDesc: Cluster status description
        :type StatusDesc: str
        :param _CreateTime: Cluster Creation Time
        :type CreateTime: str
        :param _PayMode: Payment mode. 0: pay-as-you-go; 1: monthly subscription.
        :type PayMode: int
        :param _PeriodEndTime: Expiration time.
        :type PeriodEndTime: str
        :param _Vip: Cluster read/write vip.
        :type Vip: str
        :param _Vport: Cluster read/write vport.
        :type Vport: int
        :param _ProjectID: Project ID
        :type ProjectID: int
        :param _VpcId: Specifies the virtual private cloud ID.
        :type VpcId: str
        :param _SubnetId: Specifies the subnet ID.
        :type SubnetId: str
        :param _CynosVersion: Specifies the cynos kernel version.
        :type CynosVersion: str
        :param _StorageLimit: Specifies the storage capacity.
        :type StorageLimit: int
        :param _RenewFlag: Renewal Flag
        :type RenewFlag: int
        :param _ProcessingTask: Task being processed.
        :type ProcessingTask: str
        :param _Tasks: Task array of the cluster.
        :type Tasks: list of ObjectTask
        :param _ResourceTags: Array of tags bound to the cluster.
        :type ResourceTags: list of Tag
        :param _DbMode: Db type (NORMAL, SERVERLESS).
        :type DbMode: str
        :param _ServerlessStatus: Specifies the status of the SERVERLESS cluster when the Db type is SERVERLESS. valid values:.
resume
pause
        :type ServerlessStatus: str
        :param _Storage: Cluster prepaid storage size.
        :type Storage: int
        :param _StorageId: Cluster storage ID for prepaid storage, specifies the storage ID used for prepaid storage modification.
        :type StorageId: str
        :param _StoragePayMode: Cluster storage payment mode. 0: pay-as-you-go; 1: monthly subscription.
        :type StoragePayMode: int
        :param _MinStorageSize: Minimum storage value corresponding to cluster computing specifications.
        :type MinStorageSize: int
        :param _MaxStorageSize: The maximum storage value corresponding to the cluster computing specification.
        :type MaxStorageSize: int
        :param _NetAddrs: Specifies the cluster network information.
        :type NetAddrs: list of NetAddr
        :param _PhysicalZone: Physical availability zone.
        :type PhysicalZone: str
        :param _MasterZone: Primary AZ.
        :type MasterZone: str
        :param _HasSlaveZone: Whether there is an availability zone.
        :type HasSlaveZone: str
        :param _SlaveZones: Secondary AZ.
        :type SlaveZones: list of str
        :param _BusinessType: Business type.
        :type BusinessType: str
        :param _IsFreeze: Whether to freeze.
        :type IsFreeze: str
        :param _OrderSource: Order Source
        :type OrderSource: str
        :param _Ability: Capacity.
        :type Ability: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        :param _ResourcePackages: Specifies the information of the resource package bound to the instance (only the storage resource package is returned here, that is, packageType=DISK).	
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
        """Cluster status. Valid values are as follows:
creating
running
isolating
isolated
activating (removing isolation)
offlining (deactivating)
offlined (deactivated)
deleting
deleted
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Zone(self):
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ClusterName(self):
        """Cluster name
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def DbVersion(self):
        """Database version
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceNum(self):
        """Number of instances
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def Uin(self):
        """User UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def DbType(self):
        """Engine type.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def AppId(self):
        """User appid.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def StatusDesc(self):
        """Cluster status description
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        """Cluster Creation Time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PayMode(self):
        """Payment mode. 0: pay-as-you-go; 1: monthly subscription.
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        """Expiration time.
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def Vip(self):
        """Cluster read/write vip.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Cluster read/write vport.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def ProjectID(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def VpcId(self):
        """Specifies the virtual private cloud ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Specifies the subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CynosVersion(self):
        """Specifies the cynos kernel version.
        :rtype: str
        """
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def StorageLimit(self):
        """Specifies the storage capacity.
        :rtype: int
        """
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def RenewFlag(self):
        """Renewal Flag
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ProcessingTask(self):
        """Task being processed.
        :rtype: str
        """
        return self._ProcessingTask

    @ProcessingTask.setter
    def ProcessingTask(self, ProcessingTask):
        self._ProcessingTask = ProcessingTask

    @property
    def Tasks(self):
        """Task array of the cluster.
        :rtype: list of ObjectTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def ResourceTags(self):
        """Array of tags bound to the cluster.
        :rtype: list of Tag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbMode(self):
        """Db type (NORMAL, SERVERLESS).
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def ServerlessStatus(self):
        """Specifies the status of the SERVERLESS cluster when the Db type is SERVERLESS. valid values:.
resume
pause
        :rtype: str
        """
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def Storage(self):
        """Cluster prepaid storage size.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageId(self):
        """Cluster storage ID for prepaid storage, specifies the storage ID used for prepaid storage modification.
        :rtype: str
        """
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId

    @property
    def StoragePayMode(self):
        """Cluster storage payment mode. 0: pay-as-you-go; 1: monthly subscription.
        :rtype: int
        """
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def MinStorageSize(self):
        """Minimum storage value corresponding to cluster computing specifications.
        :rtype: int
        """
        return self._MinStorageSize

    @MinStorageSize.setter
    def MinStorageSize(self, MinStorageSize):
        self._MinStorageSize = MinStorageSize

    @property
    def MaxStorageSize(self):
        """The maximum storage value corresponding to the cluster computing specification.
        :rtype: int
        """
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def NetAddrs(self):
        """Specifies the cluster network information.
        :rtype: list of NetAddr
        """
        return self._NetAddrs

    @NetAddrs.setter
    def NetAddrs(self, NetAddrs):
        self._NetAddrs = NetAddrs

    @property
    def PhysicalZone(self):
        """Physical availability zone.
        :rtype: str
        """
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def MasterZone(self):
        """Primary AZ.
        :rtype: str
        """
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def HasSlaveZone(self):
        """Whether there is an availability zone.
        :rtype: str
        """
        return self._HasSlaveZone

    @HasSlaveZone.setter
    def HasSlaveZone(self, HasSlaveZone):
        self._HasSlaveZone = HasSlaveZone

    @property
    def SlaveZones(self):
        """Secondary AZ.
        :rtype: list of str
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def BusinessType(self):
        """Business type.
        :rtype: str
        """
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def IsFreeze(self):
        """Whether to freeze.
        :rtype: str
        """
        return self._IsFreeze

    @IsFreeze.setter
    def IsFreeze(self, IsFreeze):
        self._IsFreeze = IsFreeze

    @property
    def OrderSource(self):
        """Order Source
        :rtype: str
        """
        return self._OrderSource

    @OrderSource.setter
    def OrderSource(self, OrderSource):
        self._OrderSource = OrderSource

    @property
    def Ability(self):
        """Capacity.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        """
        return self._Ability

    @Ability.setter
    def Ability(self, Ability):
        self._Ability = Ability

    @property
    def ResourcePackages(self):
        """Specifies the information of the resource package bound to the instance (only the storage resource package is returned here, that is, packageType=DISK).	
        :rtype: list of ResourcePackage
        """
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
        :param _PhysicalZone: Physical availability zone.
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
        :param _StorageId: Storage Id.
        :type StorageId: str
        :param _Storage: Storage size in gb.
        :type Storage: int
        :param _MaxStorageSize: Maximum storage specification, in gb.
        :type MaxStorageSize: int
        :param _MinStorageSize: Specifies the minimum storage specification, in gb.
        :type MinStorageSize: int
        :param _StoragePayMode: Storage billing type. 1 indicates monthly subscription, and 0 indicates pay-as-you-go.
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
        :param _DbMode: Db type: <li>NORMAL</li> <li>SERVERLESS</li>.
        :type DbMode: str
        :param _DbVersion: Database version
        :type DbVersion: str
        :param _StorageLimit: Specifies the maximum storage space.
        :type StorageLimit: int
        :param _UsedStorage: Used capacity
        :type UsedStorage: int
        :param _Vip: VIP
        :type Vip: str
        :param _Vport: vport
        :type Vport: int
        :param _RoAddr: VIP and vport of the read-only instance in a cluster
        :type RoAddr: list of Addr
        :param _Ability: Functions supported by the cluster.
        :type Ability: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        :param _CynosVersion: Specifies the cynos version.
        :type CynosVersion: str
        :param _BusinessType: Business type.
        :type BusinessType: str
        :param _HasSlaveZone: Whether there is an availability zone.
        :type HasSlaveZone: str
        :param _IsFreeze: Whether to freeze.
        :type IsFreeze: str
        :param _Tasks: Task list.
        :type Tasks: list of ObjectTask
        :param _MasterZone: Primary AZ.
        :type MasterZone: str
        :param _SlaveZones: Availability zone list.
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
        :param _ProxyStatus: Proxy status.
        :type ProxyStatus: str
        :param _LogBin: binlog switch. valid values: ON, OFF.
        :type LogBin: str
        :param _IsSkipTrade: Specifies whether to skip the transaction.
        :type IsSkipTrade: str
        :param _PitrType: PITR type: valid values: normal, redo_pitr.
        :type PitrType: str
        :param _IsOpenPasswordComplexity: Whether to enable password complexity.
        :type IsOpenPasswordComplexity: str
        :param _NetworkStatus: Network type.
        :type NetworkStatus: str
        :param _ResourcePackages: The resource package information that is bound to the cluster.	
        :type ResourcePackages: list of ResourcePackage
        :param _RenewFlag: Auto-Renewal flag. 1 indicates auto-renewal. 0 indicates non-renewal upon expiration.
        :type RenewFlag: int
        :param _NetworkType: Specifies the node network type.
        :type NetworkType: str
        :param _SlaveZoneAttr: Secondary availability zone property.
        :type SlaveZoneAttr: list of SlaveZoneAttrItem
        :param _CynosVersionTag: Version Tag.
        :type CynosVersionTag: str
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
        self._CynosVersionTag = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """Cluster name
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def PhysicalZone(self):
        """Physical availability zone.
        :rtype: str
        """
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def Status(self):
        """Status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Status description
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ServerlessStatus(self):
        """Serverless cluster status when the database type is `SERVERLESS`. Valid values:
resume
resuming
pause
pausing
        :rtype: str
        """
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def StorageId(self):
        """Storage Id.
        :rtype: str
        """
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId

    @property
    def Storage(self):
        """Storage size in gb.
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def MaxStorageSize(self):
        """Maximum storage specification, in gb.
        :rtype: int
        """
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def MinStorageSize(self):
        """Specifies the minimum storage specification, in gb.
        :rtype: int
        """
        return self._MinStorageSize

    @MinStorageSize.setter
    def MinStorageSize(self, MinStorageSize):
        self._MinStorageSize = MinStorageSize

    @property
    def StoragePayMode(self):
        """Storage billing type. 1 indicates monthly subscription, and 0 indicates pay-as-you-go.
        :rtype: int
        """
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def VpcName(self):
        """VPC name
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcId(self):
        """Unique VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetName(self):
        """Subnet name
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def SubnetId(self):
        """Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Charset(self):
        """Character set
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DbType(self):
        """Database type
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbMode(self):
        """Db type: <li>NORMAL</li> <li>SERVERLESS</li>.
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def DbVersion(self):
        """Database version
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def StorageLimit(self):
        """Specifies the maximum storage space.
        :rtype: int
        """
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def UsedStorage(self):
        """Used capacity
        :rtype: int
        """
        return self._UsedStorage

    @UsedStorage.setter
    def UsedStorage(self, UsedStorage):
        self._UsedStorage = UsedStorage

    @property
    def Vip(self):
        """VIP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """vport
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def RoAddr(self):
        """VIP and vport of the read-only instance in a cluster
        :rtype: list of Addr
        """
        return self._RoAddr

    @RoAddr.setter
    def RoAddr(self, RoAddr):
        self._RoAddr = RoAddr

    @property
    def Ability(self):
        """Functions supported by the cluster.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        """
        return self._Ability

    @Ability.setter
    def Ability(self, Ability):
        self._Ability = Ability

    @property
    def CynosVersion(self):
        """Specifies the cynos version.
        :rtype: str
        """
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def BusinessType(self):
        """Business type.
        :rtype: str
        """
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def HasSlaveZone(self):
        """Whether there is an availability zone.
        :rtype: str
        """
        return self._HasSlaveZone

    @HasSlaveZone.setter
    def HasSlaveZone(self, HasSlaveZone):
        self._HasSlaveZone = HasSlaveZone

    @property
    def IsFreeze(self):
        """Whether to freeze.
        :rtype: str
        """
        return self._IsFreeze

    @IsFreeze.setter
    def IsFreeze(self, IsFreeze):
        self._IsFreeze = IsFreeze

    @property
    def Tasks(self):
        """Task list.
        :rtype: list of ObjectTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def MasterZone(self):
        """Primary AZ.
        :rtype: str
        """
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        """Availability zone list.
        :rtype: list of str
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def InstanceSet(self):
        """Instance information
        :rtype: list of ClusterInstanceDetail
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def PayMode(self):
        """Billing mode
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        """Expiration time
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def ProjectID(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def ResourceTags(self):
        """Array of tags bound to instance
        :rtype: list of Tag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def ProxyStatus(self):
        """Proxy status.
        :rtype: str
        """
        return self._ProxyStatus

    @ProxyStatus.setter
    def ProxyStatus(self, ProxyStatus):
        self._ProxyStatus = ProxyStatus

    @property
    def LogBin(self):
        """binlog switch. valid values: ON, OFF.
        :rtype: str
        """
        return self._LogBin

    @LogBin.setter
    def LogBin(self, LogBin):
        self._LogBin = LogBin

    @property
    def IsSkipTrade(self):
        """Specifies whether to skip the transaction.
        :rtype: str
        """
        return self._IsSkipTrade

    @IsSkipTrade.setter
    def IsSkipTrade(self, IsSkipTrade):
        self._IsSkipTrade = IsSkipTrade

    @property
    def PitrType(self):
        """PITR type: valid values: normal, redo_pitr.
        :rtype: str
        """
        return self._PitrType

    @PitrType.setter
    def PitrType(self, PitrType):
        self._PitrType = PitrType

    @property
    def IsOpenPasswordComplexity(self):
        """Whether to enable password complexity.
        :rtype: str
        """
        return self._IsOpenPasswordComplexity

    @IsOpenPasswordComplexity.setter
    def IsOpenPasswordComplexity(self, IsOpenPasswordComplexity):
        self._IsOpenPasswordComplexity = IsOpenPasswordComplexity

    @property
    def NetworkStatus(self):
        """Network type.
        :rtype: str
        """
        return self._NetworkStatus

    @NetworkStatus.setter
    def NetworkStatus(self, NetworkStatus):
        self._NetworkStatus = NetworkStatus

    @property
    def ResourcePackages(self):
        """The resource package information that is bound to the cluster.	
        :rtype: list of ResourcePackage
        """
        return self._ResourcePackages

    @ResourcePackages.setter
    def ResourcePackages(self, ResourcePackages):
        self._ResourcePackages = ResourcePackages

    @property
    def RenewFlag(self):
        """Auto-Renewal flag. 1 indicates auto-renewal. 0 indicates non-renewal upon expiration.
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def NetworkType(self):
        """Specifies the node network type.
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def SlaveZoneAttr(self):
        """Secondary availability zone property.
        :rtype: list of SlaveZoneAttrItem
        """
        return self._SlaveZoneAttr

    @SlaveZoneAttr.setter
    def SlaveZoneAttr(self, SlaveZoneAttr):
        self._SlaveZoneAttr = SlaveZoneAttr

    @property
    def CynosVersionTag(self):
        """Version Tag.
        :rtype: str
        """
        return self._CynosVersionTag

    @CynosVersionTag.setter
    def CynosVersionTag(self, CynosVersionTag):
        self._CynosVersionTag = CynosVersionTag


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
        self._CynosVersionTag = params.get("CynosVersionTag")
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
        :param _Timestamp: Log timestamp.
        :type Timestamp: int
        :param _Level: Log level.
        :type Level: str
        :param _Content: Log content.
        :type Content: str
        """
        self._Timestamp = None
        self._Level = None
        self._Content = None

    @property
    def Timestamp(self):
        """Log timestamp.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Level(self):
        """Log level.
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Content(self):
        """Log content.
        :rtype: str
        """
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
        :param _StorageId: Prepayment storage Id.
        :type StorageId: str
        :param _StoragePayMode: Storage billing mode
        :type StoragePayMode: int
        :param _PhysicalZone: Physical zone
        :type PhysicalZone: str
        :param _BusinessType: Business type.
        :type BusinessType: str
        :param _Tasks: Task
        :type Tasks: list of ObjectTask
        :param _IsFreeze: Whether to freeze.
        :type IsFreeze: str
        :param _ResourceTags: The resource tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceTags: list of Tag
        :param _MasterZone: Primary AZ.
        :type MasterZone: str
        :param _SlaveZones: Replica AZ
Note: This field may return null, indicating that no valid value can be obtained.
        :type SlaveZones: list of str
        :param _InstanceNetInfo: Network information of the instance.
        :type InstanceNetInfo: list of InstanceNetInfo
        :param _ResourcePackages: Information of the resource pack bound to an instance when `packageType` is `CCU`. Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourcePackages: list of ResourcePackage
        :param _InstanceIndexMode: Specifies the instance index form. valid values include mixedRowColumn (row and column hybrid storage) and onlyRowIndex (row-only storage).
        :type InstanceIndexMode: str
        :param _InstanceAbility: Supported capabilities of the existing instance.
        :type InstanceAbility: :class:`tencentcloud.cynosdb.v20190107.models.InstanceAbility`
        :param _DeviceType: Instance machine type.
        :type DeviceType: str
        :param _InstanceStorageType: Specifies the instance storage type.
        :type InstanceStorageType: str
        :param _CynosVersionTag: Unknown field.
        :type CynosVersionTag: str
        :param _NodeList: Specifies the node information of libradb.
        :type NodeList: list of str
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
        self._InstanceIndexMode = None
        self._InstanceAbility = None
        self._DeviceType = None
        self._InstanceStorageType = None
        self._CynosVersionTag = None
        self._NodeList = None

    @property
    def Uin(self):
        """User `Uin`
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AppId(self):
        """User `AppId`
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """Cluster name
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        """Instance status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Instance status description
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DbMode(self):
        """Instance type, which is used to indicate whether it is a serverless instance.
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def DbType(self):
        """Database type
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        """Database version
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Cpu(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Memory in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Storage capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceType(self):
        """Instance type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceRole(self):
        """Current instance role
        :rtype: str
        """
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        """Private IP of instance
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Private port of instance
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def PayMode(self):
        """Billing mode
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        """Instance expiration time
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def DestroyDeadlineText(self):
        """Termination deadline
        :rtype: str
        """
        return self._DestroyDeadlineText

    @DestroyDeadlineText.setter
    def DestroyDeadlineText(self, DestroyDeadlineText):
        self._DestroyDeadlineText = DestroyDeadlineText

    @property
    def IsolateTime(self):
        """Isolation time
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def NetType(self):
        """Network type
        :rtype: int
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def WanDomain(self):
        """Public domain name
        :rtype: str
        """
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        """Public IP
        :rtype: str
        """
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        """Public port
        :rtype: int
        """
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        """Public network status
        :rtype: str
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def DestroyTime(self):
        """Instance termination time
        :rtype: str
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def CynosVersion(self):
        """TDSQL-C kernel version
        :rtype: str
        """
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def ProcessingTask(self):
        """Task in progress
        :rtype: str
        """
        return self._ProcessingTask

    @ProcessingTask.setter
    def ProcessingTask(self, ProcessingTask):
        self._ProcessingTask = ProcessingTask

    @property
    def RenewFlag(self):
        """Renewal flag
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def MinCpu(self):
        """Minimum number of CPU cores for serverless instance
        :rtype: float
        """
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        """Maximum number of CPU cores for serverless instance
        :rtype: float
        """
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def ServerlessStatus(self):
        """Serverless instance status. Valid values:
resume
pause
        :rtype: str
        """
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def StorageId(self):
        """Prepayment storage Id.
        :rtype: str
        """
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId

    @property
    def StoragePayMode(self):
        """Storage billing mode
        :rtype: int
        """
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def PhysicalZone(self):
        """Physical zone
        :rtype: str
        """
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def BusinessType(self):
        """Business type.
        :rtype: str
        """
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def Tasks(self):
        """Task
        :rtype: list of ObjectTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def IsFreeze(self):
        """Whether to freeze.
        :rtype: str
        """
        return self._IsFreeze

    @IsFreeze.setter
    def IsFreeze(self, IsFreeze):
        self._IsFreeze = IsFreeze

    @property
    def ResourceTags(self):
        """The resource tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def MasterZone(self):
        """Primary AZ.
        :rtype: str
        """
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        """Replica AZ
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def InstanceNetInfo(self):
        """Network information of the instance.
        :rtype: list of InstanceNetInfo
        """
        return self._InstanceNetInfo

    @InstanceNetInfo.setter
    def InstanceNetInfo(self, InstanceNetInfo):
        self._InstanceNetInfo = InstanceNetInfo

    @property
    def ResourcePackages(self):
        """Information of the resource pack bound to an instance when `packageType` is `CCU`. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ResourcePackage
        """
        return self._ResourcePackages

    @ResourcePackages.setter
    def ResourcePackages(self, ResourcePackages):
        self._ResourcePackages = ResourcePackages

    @property
    def InstanceIndexMode(self):
        """Specifies the instance index form. valid values include mixedRowColumn (row and column hybrid storage) and onlyRowIndex (row-only storage).
        :rtype: str
        """
        return self._InstanceIndexMode

    @InstanceIndexMode.setter
    def InstanceIndexMode(self, InstanceIndexMode):
        self._InstanceIndexMode = InstanceIndexMode

    @property
    def InstanceAbility(self):
        """Supported capabilities of the existing instance.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.InstanceAbility`
        """
        return self._InstanceAbility

    @InstanceAbility.setter
    def InstanceAbility(self, InstanceAbility):
        self._InstanceAbility = InstanceAbility

    @property
    def DeviceType(self):
        """Instance machine type.
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceStorageType(self):
        """Specifies the instance storage type.
        :rtype: str
        """
        return self._InstanceStorageType

    @InstanceStorageType.setter
    def InstanceStorageType(self, InstanceStorageType):
        self._InstanceStorageType = InstanceStorageType

    @property
    def CynosVersionTag(self):
        """Unknown field.
        :rtype: str
        """
        return self._CynosVersionTag

    @CynosVersionTag.setter
    def CynosVersionTag(self, CynosVersionTag):
        self._CynosVersionTag = CynosVersionTag

    @property
    def NodeList(self):
        """Specifies the node information of libradb.
        :rtype: list of str
        """
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList


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
        self._InstanceIndexMode = params.get("InstanceIndexMode")
        if params.get("InstanceAbility") is not None:
            self._InstanceAbility = InstanceAbility()
            self._InstanceAbility._deserialize(params.get("InstanceAbility"))
        self._DeviceType = params.get("DeviceType")
        self._InstanceStorageType = params.get("InstanceStorageType")
        self._CynosVersionTag = params.get("CynosVersionTag")
        self._NodeList = params.get("NodeList")
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
        :param _ServerlessStatus: Serverless instance status. Valid values:
resume
pause
        :type ServerlessStatus: str
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
        :param _DbMode: Db type: <li>NORMAL</li> <li>SERVERLESS</li>.
        :type DbMode: str
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
        self._ServerlessStatus = None
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
        self._DbMode = None

    @property
    def Uin(self):
        """User `Uin`
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AppId(self):
        """User `AppId`
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """Cluster name
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        """Instance status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Instance status description
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ServerlessStatus(self):
        """Serverless instance status. Valid values:
resume
pause
        :rtype: str
        """
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def DbType(self):
        """Database type
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        """Database version
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Cpu(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Memory in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """Storage capacity in GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceType(self):
        """Instance type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceRole(self):
        """Current instance role
        :rtype: str
        """
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PayMode(self):
        """Billing mode
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        """Instance expiration time
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def NetType(self):
        """Network type
        :rtype: int
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        """Private IP of instance
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Private port of instance
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def WanDomain(self):
        """Public domain name of instance
        :rtype: str
        """
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def Charset(self):
        """Character set
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CynosVersion(self):
        """TDSQL-C kernel version
        :rtype: str
        """
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def RenewFlag(self):
        """Renewal flag
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def MinCpu(self):
        """The minimum number of CPU cores for a serverless instance
        :rtype: float
        """
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        """The maximum number of CPU cores for a serverless instance
        :rtype: float
        """
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def DbMode(self):
        """Db type: <li>NORMAL</li> <li>SERVERLESS</li>.
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode


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
        self._ServerlessStatus = params.get("ServerlessStatus")
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
        self._DbMode = params.get("DbMode")
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
        """User `appId`
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CreatedTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DeletedTime(self):
        """Deletion time
        :rtype: str
        """
        return self._DeletedTime

    @DeletedTime.setter
    def DeletedTime(self, DeletedTime):
        self._DeletedTime = DeletedTime

    @property
    def InstanceGrpId(self):
        """Instance group ID
        :rtype: str
        """
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        self._InstanceGrpId = InstanceGrpId

    @property
    def Status(self):
        """Status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """Instance group type. ha: HA group; ro: RO group
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdatedTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Vip(self):
        """Private IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Private port
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def WanDomain(self):
        """Public domain name
        :rtype: str
        """
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        """Public IP
        :rtype: str
        """
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        """Public port
        :rtype: int
        """
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        """Public network status
        :rtype: str
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def InstanceSet(self):
        """Information of instances contained in instance group
        :rtype: list of CynosdbInstance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def UniqVpcId(self):
        """VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        """Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def OldAddrInfo(self):
        """Information of the old IP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OldAddrInfo`
        """
        return self._OldAddrInfo

    @OldAddrInfo.setter
    def OldAddrInfo(self, OldAddrInfo):
        self._OldAddrInfo = OldAddrInfo

    @property
    def ProcessingTasks(self):
        """Task in progress
        :rtype: list of str
        """
        return self._ProcessingTasks

    @ProcessingTasks.setter
    def ProcessingTasks(self, ProcessingTasks):
        self._ProcessingTasks = ProcessingTasks

    @property
    def Tasks(self):
        """Task list
        :rtype: list of ObjectTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def NetServiceId(self):
        """biz_net_service table ID
        :rtype: int
        """
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
        :param _Db: Database.
        :type Db: str
        :param _Privileges: Permission list
        :type Privileges: list of str
        """
        self._Db = None
        self._Privileges = None

    @property
    def Db(self):
        """Database.
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Privileges(self):
        """Permission list
        :rtype: list of str
        """
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
        :type Database: str
        :param _Tables: Table name list.
        :type Tables: list of str
        """
        self._Database = None
        self._Tables = None

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Tables(self):
        """Table name list.
        :rtype: list of str
        """
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
        :param _Description: Specifies the remark of the database.
        :type Description: str
        :param _UserHostPrivileges: User permission
        :type UserHostPrivileges: list of UserHostPrivilege
        :param _DbId: Database ID
        :type DbId: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _AppId: User appid.
        :type AppId: int
        :param _Uin: User UIN
        :type Uin: str
        :param _ClusterId: Cluster ID
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
        """Database name
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CharacterSet(self):
        """Character set
        :rtype: str
        """
        return self._CharacterSet

    @CharacterSet.setter
    def CharacterSet(self, CharacterSet):
        self._CharacterSet = CharacterSet

    @property
    def Status(self):
        """Database status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CollateRule(self):
        """Collation
        :rtype: str
        """
        return self._CollateRule

    @CollateRule.setter
    def CollateRule(self, CollateRule):
        self._CollateRule = CollateRule

    @property
    def Description(self):
        """Specifies the remark of the database.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserHostPrivileges(self):
        """User permission
        :rtype: list of UserHostPrivilege
        """
        return self._UserHostPrivileges

    @UserHostPrivileges.setter
    def UserHostPrivileges(self, UserHostPrivileges):
        self._UserHostPrivileges = UserHostPrivileges

    @property
    def DbId(self):
        """Database ID
        :rtype: int
        """
        return self._DbId

    @DbId.setter
    def DbId(self, DbId):
        self._DbId = DbId

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AppId(self):
        """User appid.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        """User UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Accounts(self):
        """Accounts in array, which contains `account` and `host`.
        :rtype: list of InputAccount
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Audit rule template ID
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SnapshotIdList(self):
        """Backup file ID. This field is used by legacy versions and thus not recommended.
        :rtype: list of int
        """
        return self._SnapshotIdList

    @SnapshotIdList.setter
    def SnapshotIdList(self, SnapshotIdList):
        self._SnapshotIdList = SnapshotIdList

    @property
    def BackupIds(self):
        """Backup file ID. This field is recommended.
        :rtype: list of int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbNames(self):
        """
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Parameter template ID
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AccountName(self):
        """Account name
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Host(self):
        """Host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Db(self):
        """When the database name is “*”, the value specified in `Type` and `TableName` will be ignored, indicating that the user's global permissions are being modified.
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Type(self):
        """Object type in a specified database. Valid values: `table`, `*`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TableName(self):
        """The database name can be specified when `Type` is 'table'.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Privileges = None
        self._RequestId = None

    @property
    def Privileges(self):
        """The list of permissions, such as  ["select","update","delete","create","drop","references","index","alter","show_db","create_tmp_table","lock_tables","execute","create_view","show_view","create_routine","alter_routine","event","trigger"]
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AccountNames(self):
        """List of accounts to be filtered
        :rtype: list of str
        """
        return self._AccountNames

    @AccountNames.setter
    def AccountNames(self, AccountNames):
        self._AccountNames = AccountNames

    @property
    def DbType(self):
        """Database type. Valid values: 
<li> MYSQL </li>
This parameter has been disused.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Hosts(self):
        """List of accounts to be filtered
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def Limit(self):
        """Maximum entries returned per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AccountRegular(self):
        """Keywords for fuzzy search (match `AccountName` and `AccountHost` at the same time), which supports regex. The union results will be returned.
        :rtype: str
        """
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
        :param _AccountSet: Database account list.
        :type AccountSet: list of Account
        :param _TotalCount: Total number of accounts
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AccountSet(self):
        """Database account list.
        :rtype: list of Account
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def TotalCount(self):
        """Total number of accounts
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Rule template ID
        :rtype: list of str
        """
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds

    @property
    def RuleTemplateNames(self):
        """Rule template name
        :rtype: list of str
        """
        return self._RuleTemplateNames

    @RuleTemplateNames.setter
    def RuleTemplateNames(self, RuleTemplateNames):
        self._RuleTemplateNames = RuleTemplateNames

    @property
    def Limit(self):
        """Number of results returned per request. Default value: `20`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: `0`.
        :rtype: int
        """
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
        :param _Items: Rule template detail list.
        :type Items: list of AuditRuleTemplateInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Rule template detail list.
        :rtype: list of AuditRuleTemplateInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Instance ID. Currently, only one single instance can be queried.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """None
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Audit rule information of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceAuditRule
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
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
        :param _BackupFreq: Backup frequency. an array with a length of 7, indicating the backup methods corresponding to monday to sunday respectively. full represents full backup, and increment represents incremental backup.
        :type BackupFreq: list of str
        :param _BackupType: Backup method. specifies the method of backup. valid values: logic (indicates logical backup), snapshot (indicates snapshot backup).
        :type BackupType: str
        :param _LogicCrossRegionsConfigUpdateTime: Cross-Regional logical backup configuration modification time.
        :type LogicCrossRegionsConfigUpdateTime: str
        :param _LogicBackupConfig: Automatic logical backup configuration.
        :type LogicBackupConfig: :class:`tencentcloud.cynosdb.v20190107.models.LogicBackupConfigInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupTimeBeg = None
        self._BackupTimeEnd = None
        self._ReserveDuration = None
        self._BackupFreq = None
        self._BackupType = None
        self._LogicCrossRegionsConfigUpdateTime = None
        self._LogicBackupConfig = None
        self._RequestId = None

    @property
    def BackupTimeBeg(self):
        """Full backup start time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively
        :rtype: int
        """
        return self._BackupTimeBeg

    @BackupTimeBeg.setter
    def BackupTimeBeg(self, BackupTimeBeg):
        self._BackupTimeBeg = BackupTimeBeg

    @property
    def BackupTimeEnd(self):
        """Full backup end time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively
        :rtype: int
        """
        return self._BackupTimeEnd

    @BackupTimeEnd.setter
    def BackupTimeEnd(self, BackupTimeEnd):
        self._BackupTimeEnd = BackupTimeEnd

    @property
    def ReserveDuration(self):
        """Backup retention period in seconds. Backups will be cleared after this period elapses. 7 days is represented by 3600*24*7 = 604800
        :rtype: int
        """
        return self._ReserveDuration

    @ReserveDuration.setter
    def ReserveDuration(self, ReserveDuration):
        self._ReserveDuration = ReserveDuration

    @property
    def BackupFreq(self):
        """Backup frequency. an array with a length of 7, indicating the backup methods corresponding to monday to sunday respectively. full represents full backup, and increment represents incremental backup.
        :rtype: list of str
        """
        return self._BackupFreq

    @BackupFreq.setter
    def BackupFreq(self, BackupFreq):
        self._BackupFreq = BackupFreq

    @property
    def BackupType(self):
        """Backup method. specifies the method of backup. valid values: logic (indicates logical backup), snapshot (indicates snapshot backup).
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def LogicCrossRegionsConfigUpdateTime(self):
        """Cross-Regional logical backup configuration modification time.
        :rtype: str
        """
        return self._LogicCrossRegionsConfigUpdateTime

    @LogicCrossRegionsConfigUpdateTime.setter
    def LogicCrossRegionsConfigUpdateTime(self, LogicCrossRegionsConfigUpdateTime):
        self._LogicCrossRegionsConfigUpdateTime = LogicCrossRegionsConfigUpdateTime

    @property
    def LogicBackupConfig(self):
        """Automatic logical backup configuration.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.LogicBackupConfigInfo`
        """
        return self._LogicBackupConfig

    @LogicBackupConfig.setter
    def LogicBackupConfig(self, LogicBackupConfig):
        self._LogicBackupConfig = LogicBackupConfig

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        self._LogicCrossRegionsConfigUpdateTime = params.get("LogicCrossRegionsConfigUpdateTime")
        if params.get("LogicBackupConfig") is not None:
            self._LogicBackupConfig = LogicBackupConfigInfo()
            self._LogicBackupConfig._deserialize(params.get("LogicBackupConfig"))
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    """DescribeBackupDownloadRestriction request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: Cluster ID
        :type ClusterIds: list of str
        """
        self._ClusterIds = None

    @property
    def ClusterIds(self):
        """Cluster ID
        :rtype: list of str
        """
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
        


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    """DescribeBackupDownloadRestriction response structure.

    """

    def __init__(self):
        r"""
        :param _BackupLimitClusterRestrictions: Cluster backup download limit.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupLimitClusterRestrictions: list of BackupLimitClusterRestriction
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupLimitClusterRestrictions = None
        self._RequestId = None

    @property
    def BackupLimitClusterRestrictions(self):
        """Cluster backup download limit.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BackupLimitClusterRestriction
        """
        return self._BackupLimitClusterRestrictions

    @BackupLimitClusterRestrictions.setter
    def BackupLimitClusterRestrictions(self, BackupLimitClusterRestrictions):
        self._BackupLimitClusterRestrictions = BackupLimitClusterRestrictions

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackupLimitClusterRestrictions") is not None:
            self._BackupLimitClusterRestrictions = []
            for item in params.get("BackupLimitClusterRestrictions"):
                obj = BackupLimitClusterRestriction()
                obj._deserialize(item)
                self._BackupLimitClusterRestrictions.append(obj)
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
        :param _DownloadRestriction: Backup download source restriction condition.
        :type DownloadRestriction: :class:`tencentcloud.cynosdb.v20190107.models.BackupLimitRestriction`
        """
        self._ClusterId = None
        self._BackupId = None
        self._DownloadRestriction = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupId(self):
        """Backup ID
        :rtype: int
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def DownloadRestriction(self):
        """Backup download source restriction condition.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.BackupLimitRestriction`
        """
        return self._DownloadRestriction

    @DownloadRestriction.setter
    def DownloadRestriction(self, DownloadRestriction):
        self._DownloadRestriction = DownloadRestriction


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupId = params.get("BackupId")
        if params.get("DownloadRestriction") is not None:
            self._DownloadRestriction = BackupLimitRestriction()
            self._DownloadRestriction._deserialize(params.get("DownloadRestriction"))
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        """Backup download address
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadUserRestrictionRequest(AbstractModel):
    """DescribeBackupDownloadUserRestriction request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Pagination size
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _OnlyUserRestriction: Specifies whether to query only user-level download limits. true - yes, false - no.
        :type OnlyUserRestriction: bool
        """
        self._Limit = None
        self._Offset = None
        self._OnlyUserRestriction = None

    @property
    def Limit(self):
        """Pagination size
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OnlyUserRestriction(self):
        """Specifies whether to query only user-level download limits. true - yes, false - no.
        :rtype: bool
        """
        return self._OnlyUserRestriction

    @OnlyUserRestriction.setter
    def OnlyUserRestriction(self, OnlyUserRestriction):
        self._OnlyUserRestriction = OnlyUserRestriction


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OnlyUserRestriction = params.get("OnlyUserRestriction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadUserRestrictionResponse(AbstractModel):
    """DescribeBackupDownloadUserRestriction response structure.

    """

    def __init__(self):
        r"""
        :param _BackupLimitClusterRestrictions: Cluster backup download limit information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupLimitClusterRestrictions: list of BackupLimitClusterRestriction
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupLimitClusterRestrictions = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BackupLimitClusterRestrictions(self):
        """Cluster backup download limit information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BackupLimitClusterRestriction
        """
        return self._BackupLimitClusterRestrictions

    @BackupLimitClusterRestrictions.setter
    def BackupLimitClusterRestrictions(self, BackupLimitClusterRestrictions):
        self._BackupLimitClusterRestrictions = BackupLimitClusterRestrictions

    @property
    def TotalCount(self):
        """Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackupLimitClusterRestrictions") is not None:
            self._BackupLimitClusterRestrictions = []
            for item in params.get("BackupLimitClusterRestrictions"):
                obj = BackupLimitClusterRestriction()
                obj._deserialize(item)
                self._BackupLimitClusterRestrictions.append(obj)
        self._TotalCount = params.get("TotalCount")
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Limit(self):
        """The number of results to be returned. Value range: (0,100]
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Record offset. Value range: [0,INF)
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DbType(self):
        """Database type. Valid values: 
<li> MYSQL </li>
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def BackupIds(self):
        """Backup ID
        :rtype: list of int
        """
        return self._BackupIds

    @BackupIds.setter
    def BackupIds(self, BackupIds):
        self._BackupIds = BackupIds

    @property
    def BackupType(self):
        """Backup type. Valid values: `snapshot` (snapshot backup), `logic` (logic backup).
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupMethod(self):
        """Back mode. Valid values: `auto` (automatic backup), `manual` (manual backup)
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def SnapShotType(self):
        """
        :rtype: str
        """
        return self._SnapShotType

    @SnapShotType.setter
    def SnapShotType(self, SnapShotType):
        self._SnapShotType = SnapShotType

    @property
    def StartTime(self):
        """Backup start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Backup end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FileNames(self):
        """
        :rtype: list of str
        """
        return self._FileNames

    @FileNames.setter
    def FileNames(self, FileNames):
        self._FileNames = FileNames

    @property
    def BackupNames(self):
        """Backup alias, which supports fuzzy query.
        :rtype: list of str
        """
        return self._BackupNames

    @BackupNames.setter
    def BackupNames(self, BackupNames):
        self._BackupNames = BackupNames

    @property
    def SnapshotIdList(self):
        """ID list of the snapshot backup
        :rtype: list of int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of backup files
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupList(self):
        """Backup file list
        :rtype: list of BackupFileInfo
        """
        return self._BackupList

    @BackupList.setter
    def BackupList(self, BackupList):
        self._BackupList = BackupList

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeBinlogConfigRequest(AbstractModel):
    """DescribeBinlogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
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
        


class DescribeBinlogConfigResponse(AbstractModel):
    """DescribeBinlogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _BinlogCrossRegionsConfigUpdateTime: Configuration update time for cross-regional Binlog.
        :type BinlogCrossRegionsConfigUpdateTime: str
        :param _BinlogConfig: Specifies the Binlog configuration message.
        :type BinlogConfig: :class:`tencentcloud.cynosdb.v20190107.models.BinlogConfigInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BinlogCrossRegionsConfigUpdateTime = None
        self._BinlogConfig = None
        self._RequestId = None

    @property
    def BinlogCrossRegionsConfigUpdateTime(self):
        """Configuration update time for cross-regional Binlog.
        :rtype: str
        """
        return self._BinlogCrossRegionsConfigUpdateTime

    @BinlogCrossRegionsConfigUpdateTime.setter
    def BinlogCrossRegionsConfigUpdateTime(self, BinlogCrossRegionsConfigUpdateTime):
        self._BinlogCrossRegionsConfigUpdateTime = BinlogCrossRegionsConfigUpdateTime

    @property
    def BinlogConfig(self):
        """Specifies the Binlog configuration message.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.BinlogConfigInfo`
        """
        return self._BinlogConfig

    @BinlogConfig.setter
    def BinlogConfig(self, BinlogConfig):
        self._BinlogConfig = BinlogConfig

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BinlogCrossRegionsConfigUpdateTime = params.get("BinlogCrossRegionsConfigUpdateTime")
        if params.get("BinlogConfig") is not None:
            self._BinlogConfig = BinlogConfigInfo()
            self._BinlogConfig._deserialize(params.get("BinlogConfig"))
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
        :param _DownloadRestriction: Backup download source restriction condition.
        :type DownloadRestriction: :class:`tencentcloud.cynosdb.v20190107.models.BackupLimitRestriction`
        """
        self._ClusterId = None
        self._BinlogId = None
        self._DownloadRestriction = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BinlogId(self):
        """Binlog file ID
        :rtype: int
        """
        return self._BinlogId

    @BinlogId.setter
    def BinlogId(self, BinlogId):
        self._BinlogId = BinlogId

    @property
    def DownloadRestriction(self):
        """Backup download source restriction condition.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.BackupLimitRestriction`
        """
        return self._DownloadRestriction

    @DownloadRestriction.setter
    def DownloadRestriction(self, DownloadRestriction):
        self._DownloadRestriction = DownloadRestriction


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BinlogId = params.get("BinlogId")
        if params.get("DownloadRestriction") is not None:
            self._DownloadRestriction = BackupLimitRestriction()
            self._DownloadRestriction._deserialize(params.get("DownloadRestriction"))
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        """Download address
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BinlogSaveDays = None
        self._RequestId = None

    @property
    def BinlogSaveDays(self):
        """Binlog retention period in days
        :rtype: int
        """
        return self._BinlogSaveDays

    @BinlogSaveDays.setter
    def BinlogSaveDays(self, BinlogSaveDays):
        self._BinlogSaveDays = BinlogSaveDays

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number
        :rtype: int
        """
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
        :param _Binlogs: Binlog list.
        :type Binlogs: list of BinlogItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Binlogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Binlogs(self):
        """Binlog list.
        :rtype: list of BinlogItem
        """
        return self._Binlogs

    @Binlogs.setter
    def Binlogs(self, Binlogs):
        self._Binlogs = Binlogs

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeClusterDatabaseTablesRequest(AbstractModel):
    """DescribeClusterDatabaseTables request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Db: Database name
        :type Db: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Number
        :type Limit: int
        :param _TableType: Specifies the table type.
Specifies that "view" only returns the view, "base_table" only returns the basic table, and "all" returns both the view and the table. the default value is all.
        :type TableType: str
        """
        self._ClusterId = None
        self._Db = None
        self._Offset = None
        self._Limit = None
        self._TableType = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Db(self):
        """Database name
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TableType(self):
        """Specifies the table type.
Specifies that "view" only returns the view, "base_table" only returns the basic table, and "all" returns both the view and the table. the default value is all.
        :rtype: str
        """
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Db = params.get("Db")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TableType = params.get("TableType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDatabaseTablesResponse(AbstractModel):
    """DescribeClusterDatabaseTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Offset: Pagination Offset
        :type Offset: int
        :param _Limit: Pagination limit.
        :type Limit: int
        :param _Tables: Database table list.
        :type Tables: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tables = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        """Pagination Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tables(self):
        """Database table list.
        :rtype: list of str
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Tables = params.get("Tables")
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        """Offset. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results. Default value: `20`. Maximum value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DbName(self):
        """Database name
        :rtype: str
        """
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
        :param _DbInfos: Database information
        :type DbInfos: list of DbInfo
        :param _TotalCount: The total count
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DbInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DbInfos(self):
        """Database information
        :rtype: list of DbInfo
        """
        return self._DbInfos

    @DbInfos.setter
    def DbInfos(self, DbInfos):
        self._DbInfos = DbInfos

    @property
    def TotalCount(self):
        """The total count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
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
        """Cluster details
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbClusterDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceGrpInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of instance groups
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceGrpInfoList(self):
        warnings.warn("parameter `InstanceGrpInfoList` is deprecated", DeprecationWarning) 

        """Instance group list
        :rtype: list of CynosdbInstanceGrp
        """
        return self._InstanceGrpInfoList

    @InstanceGrpInfoList.setter
    def InstanceGrpInfoList(self, InstanceGrpInfoList):
        warnings.warn("parameter `InstanceGrpInfoList` is deprecated", DeprecationWarning) 

        self._InstanceGrpInfoList = InstanceGrpInfoList

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ParamName(self):
        """Parameter name
        :rtype: str
        """
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
        :param _Items: Instance parameter list.
        :type Items: list of ParamInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of parameters
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Instance parameter list.
        :rtype: list of ParamInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
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
        :param _ValidatePasswordDictionary: Data dictionary parameter.
        :type ValidatePasswordDictionary: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordLength: Specifies the password length.
        :type ValidatePasswordLength: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordMixedCaseCount: Case-Sensitive character count.
        :type ValidatePasswordMixedCaseCount: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordNumberCount: Number of digits.
        :type ValidatePasswordNumberCount: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordPolicy: Password level.
        :type ValidatePasswordPolicy: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordSpecialCharCount: Number of special characters.
        :type ValidatePasswordSpecialCharCount: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Data dictionary parameter.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        """
        return self._ValidatePasswordDictionary

    @ValidatePasswordDictionary.setter
    def ValidatePasswordDictionary(self, ValidatePasswordDictionary):
        self._ValidatePasswordDictionary = ValidatePasswordDictionary

    @property
    def ValidatePasswordLength(self):
        """Specifies the password length.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        """
        return self._ValidatePasswordLength

    @ValidatePasswordLength.setter
    def ValidatePasswordLength(self, ValidatePasswordLength):
        self._ValidatePasswordLength = ValidatePasswordLength

    @property
    def ValidatePasswordMixedCaseCount(self):
        """Case-Sensitive character count.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        """
        return self._ValidatePasswordMixedCaseCount

    @ValidatePasswordMixedCaseCount.setter
    def ValidatePasswordMixedCaseCount(self, ValidatePasswordMixedCaseCount):
        self._ValidatePasswordMixedCaseCount = ValidatePasswordMixedCaseCount

    @property
    def ValidatePasswordNumberCount(self):
        """Number of digits.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        """
        return self._ValidatePasswordNumberCount

    @ValidatePasswordNumberCount.setter
    def ValidatePasswordNumberCount(self, ValidatePasswordNumberCount):
        self._ValidatePasswordNumberCount = ValidatePasswordNumberCount

    @property
    def ValidatePasswordPolicy(self):
        """Password level.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        """
        return self._ValidatePasswordPolicy

    @ValidatePasswordPolicy.setter
    def ValidatePasswordPolicy(self, ValidatePasswordPolicy):
        self._ValidatePasswordPolicy = ValidatePasswordPolicy

    @property
    def ValidatePasswordSpecialCharCount(self):
        """Number of special characters.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        """
        return self._ValidatePasswordSpecialCharCount

    @ValidatePasswordSpecialCharCount.setter
    def ValidatePasswordSpecialCharCount(self, ValidatePasswordSpecialCharCount):
        self._ValidatePasswordSpecialCharCount = ValidatePasswordSpecialCharCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeClusterReadOnlyRequest(AbstractModel):
    """DescribeClusterReadOnly request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: List of cluster IDs
        :type ClusterIds: list of str
        """
        self._ClusterIds = None

    @property
    def ClusterIds(self):
        """List of cluster IDs
        :rtype: list of str
        """
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
        


class DescribeClusterReadOnlyResponse(AbstractModel):
    """DescribeClusterReadOnly response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterReadOnlyValues: List of cluster read-only switches.
        :type ClusterReadOnlyValues: list of ClusterReadOnlyValue
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterReadOnlyValues = None
        self._RequestId = None

    @property
    def ClusterReadOnlyValues(self):
        """List of cluster read-only switches.
        :rtype: list of ClusterReadOnlyValue
        """
        return self._ClusterReadOnlyValues

    @ClusterReadOnlyValues.setter
    def ClusterReadOnlyValues(self, ClusterReadOnlyValues):
        self._ClusterReadOnlyValues = ClusterReadOnlyValues

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterReadOnlyValues") is not None:
            self._ClusterReadOnlyValues = []
            for item in params.get("ClusterReadOnlyValues"):
                obj = ClusterReadOnlyValue()
                obj._deserialize(item)
                self._ClusterReadOnlyValues.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterTransparentEncryptInfoRequest(AbstractModel):
    """DescribeClusterTransparentEncryptInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
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
        


class DescribeClusterTransparentEncryptInfoResponse(AbstractModel):
    """DescribeClusterTransparentEncryptInfo response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Encryption key id.
        :type KeyId: str
        :param _KeyRegion: Encryption key region.

        :type KeyRegion: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._KeyRegion = None
        self._RequestId = None

    @property
    def KeyId(self):
        """Encryption key id.
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyRegion(self):
        """Encryption key region.

        :rtype: str
        """
        return self._KeyRegion

    @KeyRegion.setter
    def KeyRegion(self, KeyRegion):
        self._KeyRegion = KeyRegion

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyRegion = params.get("KeyRegion")
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
        """Engine type. Currently, `MYSQL` is supported.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Record offset. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """Sort by field. Valid values:
<li> CREATETIME: creation time</li>
<li> PERIODENDTIME: expiration time</li>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values:
<li> ASC: ascending</li>
<li> DESC: descending</li>
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        """Filter. If more than one filter exists, the logical relationship between these filters is `AND`.
        :rtype: list of QueryFilter
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of clusters
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        """Cluster list
        :rtype: list of CynosdbCluster
        """
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _InstanceId: Specifies that the instance ID must be provided by selecting either InstanceId or InstanceGroupId.
        :type InstanceId: str
        :param _InstanceGroupId: Specifies that the instance group ID must be provided by selecting either InstanceId or InstanceGroupId.
        :type InstanceGroupId: str
        """
        self._InstanceId = None
        self._InstanceGroupId = None

    @property
    def InstanceId(self):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        """Specifies that the instance ID must be provided by selecting either InstanceId or InstanceGroupId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        self._InstanceId = InstanceId

    @property
    def InstanceGroupId(self):
        """Specifies that the instance group ID must be provided by selecting either InstanceId or InstanceGroupId.
        :rtype: str
        """
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceGroupId = params.get("InstanceGroupId")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        """Security group information
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Task flow ID
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Task flow status. Valid values: `0` (succeeded), `1` (failed), `2` (Processing).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Instance ID
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
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Detail: Instance details
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbInstanceDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Detail = None
        self._RequestId = None

    @property
    def Detail(self):
        """Instance details
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbInstanceDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """Limit on the number of logs
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset of the log number
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def OrderBy(self):
        """Sorting field. Valid value: 'Timestamp'.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values: `ASC`, `DESC`.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def LogLevels(self):
        """Log level, which supports combo search by multiple levels. Valid values: `error`, `warning`, `note`.
        :rtype: list of str
        """
        return self._LogLevels

    @LogLevels.setter
    def LogLevels(self, LogLevels):
        self._LogLevels = LogLevels

    @property
    def KeyWords(self):
        """
        :rtype: list of str
        """
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
        :param _TotalCount: Number of logs.
        :type TotalCount: int
        :param _ErrorLogs: Error log list.
        :type ErrorLogs: list of CynosdbErrorLogItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ErrorLogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of logs.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ErrorLogs(self):
        """Error log list.
        :rtype: list of CynosdbErrorLogItem
        """
        return self._ErrorLogs

    @ErrorLogs.setter
    def ErrorLogs(self, ErrorLogs):
        self._ErrorLogs = ErrorLogs

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        """Instance ID, which supports batch query.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamKeyword(self):
        """Search condition for a parameter name, which supports fuzzy search.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """List of instance parameters
        :rtype: list of InstanceParamItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _SqlText: sql statement.
        :type SqlText: str
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
        self._SqlText = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Transaction start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Transaction end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """Maximum number
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Username(self):
        """Username
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Host(self):
        """Client host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def OrderBy(self):
        """Sorting field. Valid values: QueryTime, LockTime, RowsExamined, RowsSent.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values: asc, desc.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def SqlText(self):
        """sql statement.
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText


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
        self._SqlText = params.get("SqlText")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowQueries = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowQueries(self):
        """Slow query record
        :rtype: list of SlowQueriesItem
        """
        return self._SlowQueries

    @SlowQueries.setter
    def SlowQueries(self, SlowQueries):
        self._SlowQueries = SlowQueries

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Database type. Valid values: 
<li> MYSQL </li>
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def IncludeZoneStocks(self):
        """Whether to return the AZ information.
        :rtype: bool
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceSpecSet = None
        self._RequestId = None

    @property
    def InstanceSpecSet(self):
        """Specification information
        :rtype: list of InstanceSpec
        """
        return self._InstanceSpecSet

    @InstanceSpecSet.setter
    def InstanceSpecSet(self, InstanceSpecSet):
        self._InstanceSpecSet = InstanceSpecSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Number of returned results. Default value: 20. Maximum value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Record offset. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """Sort by field. Valid values:
<li> CREATETIME: creation time</li>
<li> PERIODENDTIME: expiration time</li>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values:
<li> ASC: ascending</li>
<li> DESC: descending</li>
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        """Filter. If more than one filter exists, the logical relationship between these filters is `AND`.
        :rtype: list of QueryFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DbType(self):
        """Engine type. Currently, `MYSQL` is supported.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Status(self):
        """Instance status. Valid values:
creating
running
isolating
isolated
activating: Removing the instance from isolation
offlining: Eliminating the instance
offlined: Instance eliminated
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceIds(self):
        """Instance ID list
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        """Instance list
        :rtype: list of CynosdbInstance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeInstancesWithinSameClusterRequest(AbstractModel):
    """DescribeInstancesWithinSameCluster request structure.

    """

    def __init__(self):
        r"""
        :param _UniqVpcId: vpcId
        :type UniqVpcId: str
        :param _Vip: vip
        :type Vip: str
        """
        self._UniqVpcId = None
        self._Vip = None

    @property
    def UniqVpcId(self):
        """vpcId
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Vip(self):
        """vip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._UniqVpcId = params.get("UniqVpcId")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesWithinSameClusterResponse(AbstractModel):
    """DescribeInstancesWithinSameCluster response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instances.
        :type TotalCount: int
        :param _InstanceIds: Instance ID list.
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of instances.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceIds(self):
        """Instance ID list.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class DescribeIsolatedInstancesRequest(AbstractModel):
    """DescribeIsolatedInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of returned results. the default value is 20. the maximum value is 100.
        :type Limit: int
        :param _Offset: Record offset. default value: 0.
        :type Offset: int
        :param _OrderBy: Sorting field. valid values:.
<Li>CREATETIME: creation time</li>.
<li> PERIODENDTIME: expiration time</li>.
        :type OrderBy: str
        :param _OrderByType: Sorting type. value range:.
<Li>ASC: specifies ascending sort.</li>.
<li> DESC: sorts in descending order. </li>.
        :type OrderByType: str
        :param _Filters: Search criteria. when multiple filters exist, the relationship between filters is logical AND.
        :type Filters: list of QueryFilter
        :param _DbType: Engine type: currently supports "MYSQL", "POSTGRESQL".
        :type DbType: str
        """
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None
        self._DbType = None

    @property
    def Limit(self):
        """Number of returned results. the default value is 20. the maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Record offset. default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """Sorting field. valid values:.
<Li>CREATETIME: creation time</li>.
<li> PERIODENDTIME: expiration time</li>.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting type. value range:.
<Li>ASC: specifies ascending sort.</li>.
<li> DESC: sorts in descending order. </li>.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        """Search criteria. when multiple filters exist, the relationship between filters is logical AND.
        :rtype: list of QueryFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DbType(self):
        """Engine type: currently supports "MYSQL", "POSTGRESQL".
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIsolatedInstancesResponse(AbstractModel):
    """DescribeIsolatedInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instances.
        :type TotalCount: int
        :param _InstanceSet: Instance list
        :type InstanceSet: list of CynosdbInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of instances.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        """Instance list
        :rtype: list of CynosdbInstance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Instance ID
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MaintainWeekDays = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._RequestId = None

    @property
    def MaintainWeekDays(self):
        """Maintenance days of the week
        :rtype: list of str
        """
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays

    @property
    def MaintainStartTime(self):
        """Maintenance start time in seconds
        :rtype: int
        """
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        """Maintenance duration in seconds
        :rtype: int
        """
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Parameter template ID
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Parameter template ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """Parameter template name
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        """Parameter template description
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def EngineVersion(self):
        """Engine version
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TotalCount(self):
        """Total number of parameters
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """List of parameters
        :rtype: list of ParamDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def DbMode(self):
        """Database type. Valid values:  `NORMAL`, `SERVERLESS`.
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Database engine version number
        :rtype: list of str
        """
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions

    @property
    def TemplateNames(self):
        """Template name
        :rtype: list of str
        """
        return self._TemplateNames

    @TemplateNames.setter
    def TemplateNames(self, TemplateNames):
        self._TemplateNames = TemplateNames

    @property
    def TemplateIds(self):
        """Template ID
        :rtype: list of int
        """
        return self._TemplateIds

    @TemplateIds.setter
    def TemplateIds(self, TemplateIds):
        self._TemplateIds = TemplateIds

    @property
    def DbModes(self):
        """Database Type. Valid values: `NORMAL`, `SERVERLESS`.
        :rtype: list of str
        """
        return self._DbModes

    @DbModes.setter
    def DbModes(self, DbModes):
        self._DbModes = DbModes

    @property
    def Offset(self):
        """Offset for query
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit on queries
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Products(self):
        """Product type of the queried template
        :rtype: list of str
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def TemplateTypes(self):
        """Template type
        :rtype: list of str
        """
        return self._TemplateTypes

    @TemplateTypes.setter
    def TemplateTypes(self, TemplateTypes):
        self._TemplateTypes = TemplateTypes

    @property
    def EngineTypes(self):
        """Version type
        :rtype: list of str
        """
        return self._EngineTypes

    @EngineTypes.setter
    def EngineTypes(self, EngineTypes):
        self._EngineTypes = EngineTypes

    @property
    def OrderBy(self):
        """The sorting order of the returned results
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        """Sorting order. Valid values: `desc`, `asc `.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of parameter templates
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Parameter template information
        :rtype: list of ParamTemplateListInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Limit(self):
        """Maximum entries returned per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SearchKey(self):
        """Search by keyword
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        """Security group details
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Total(self):
        """The total number of groups
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _ClusterId: Cluster ID (this parameter is required. for example, cynosdbmysql-2u2mh111).
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
        """Cluster ID (this parameter is required. for example, cynosdbmysql-2u2mh111).
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Limit(self):
        """Number of returned results. Default value: `20`. Maximum value: `100`,
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Record offset. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """Sorting field. Valid values:
<li> CREATETIME: Creation time</li>
<li> PERIODENDTIME: Expiration time</li>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values:
<li> `ASC`: Ascending.</li>
<li> `DESC`: Descending</li>
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        """Filter. If there are more than one filter, the logical relationship between these filters is `AND`.
        :rtype: list of QueryParamFilter
        """
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
        :param _ProxyGroupInfos: List of database proxy groups.
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
        """Number of database proxy groups
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProxyGroupInfos(self):
        """List of database proxy groups.
        :rtype: list of ProxyGroupInfo
        """
        return self._ProxyGroupInfos

    @ProxyGroupInfos.setter
    def ProxyGroupInfos(self, ProxyGroupInfos):
        self._ProxyGroupInfos = ProxyGroupInfos

    @property
    def ProxyNodeInfos(self):
        """Database proxy node
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ProxyNodeInfo
        """
        return self._ProxyNodeInfos

    @ProxyNodeInfos.setter
    def ProxyNodeInfos(self, ProxyNodeInfos):
        self._ProxyNodeInfos = ProxyNodeInfos

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Number of returned results. Default value: `20`. Maximum value: `100`,
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Record offset. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """Sorting field. Valid values:
<li> CREATETIME: Creation time</li>
<li> PERIODENDTIME: Expiration time</li>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values:
<li> `ASC`: Ascending.</li>
<li> `DESC`: Descending</li>
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        """Filter. If there are more than one filter, the logical relationship between these filters is `AND`.
        :rtype: list of QueryFilter
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProxyNodeInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of the database proxy nodes
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProxyNodeInfos(self):
        """List of the database proxy nodes
        :rtype: list of ProxyNodeInfo
        """
        return self._ProxyNodeInfos

    @ProxyNodeInfos.setter
    def ProxyNodeInfos(self, ProxyNodeInfos):
        self._ProxyNodeInfos = ProxyNodeInfos

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
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
        


class DescribeProxySpecsResponse(AbstractModel):
    """DescribeProxySpecs response structure.

    """

    def __init__(self):
        r"""
        :param _ProxySpecs: List of database proxyspecifications
        :type ProxySpecs: list of ProxySpec
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxySpecs = None
        self._RequestId = None

    @property
    def ProxySpecs(self):
        """List of database proxyspecifications
        :rtype: list of ProxySpec
        """
        return self._ProxySpecs

    @ProxySpecs.setter
    def ProxySpecs(self, ProxySpecs):
        self._ProxySpecs = ProxySpecs

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """The unique ID of a resource pack
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def ClusterIds(self):
        """Cluster ID
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """Offset
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceIds(self):
        """Instance D
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of deducted resource packs
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        """Resource pack details
        :rtype: list of PackageDetail
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """The unique ID of a resource pack
        :rtype: list of str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        """Resource pack name
        :rtype: list of str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageType(self):
        """Resource pack type. Valid values: `CCU` (compute resource pack), `DISK` (storage resource pack).
        :rtype: list of str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageRegion(self):
        """Region of the resource pack. Valid values: `China` (Chinese mainland), `overseas` (outside Chinese mainland).
        :rtype: list of str
        """
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def Status(self):
        """Resource pack status. Valid values: `using`, `expired`, `normal_finish` (used up), `apply_refund` (requesting a refund), `refund` (refunded).
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderBy(self):
        """Sorting conditions. Valid values: `startTime` (effective time), `expireTime` (expiration date), `packageUsedSpec` (used capacity), `packageTotalSpec` (total storage capacity). 
Sorting by array order
        :rtype: list of str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        """Sorting order. Valid values: `ASC` (ascending), `DESC` (descending).
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit
        :rtype: int
        """
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
        :param _Detail: Resource pack details.
        :type Detail: list of Package
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of resource packs
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        """Resource pack details.
        :rtype: list of Package
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Instance type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PackageRegion(self):
        """Region of the resource pack. Valid values: `China` (Chinese mainland), `overseas` (outside Chinese mainland).
        :rtype: str
        """
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def PackageType(self):
        """Resource pack type. Valid values: `CCU` (compute resource pack, `DISK` (storage resource pack).
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit
        :rtype: int
        """
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
        :param _Detail: Specifies the details of the resource pack.
        :type Detail: list of SalePackageSpec
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of available resource packs
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        """Specifies the details of the resource pack.
        :rtype: list of SalePackageSpec
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Order ID. (If the cluster is not delivered yet, the `DescribeResourcesByDealName` API may return the `InvalidParameterValue.DealNameNotFound` error. Call the API again until it succeeds.)
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def DealNames(self):
        """Order ID, which can be used to query the resource information of multiple orders ID (If the cluster is not delivered yet, the `DescribeResourcesByDealName` API may return the `InvalidParameterValue.DealNameNotFound` error. Call the API again until it succeeds.)
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BillingResourceInfos = None
        self._RequestId = None

    @property
    def BillingResourceInfos(self):
        """Billable resource ID information array
        :rtype: list of BillingResourceInfo
        """
        return self._BillingResourceInfos

    @BillingResourceInfos.setter
    def BillingResourceInfos(self, BillingResourceInfos):
        self._BillingResourceInfos = BillingResourceInfos

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
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
        :param _TimeRangeStart: Valid regression time range start time point (abandoned).
        :type TimeRangeStart: str
        :param _TimeRangeEnd: Valid regression time range end time point (abandoned).
        :type TimeRangeEnd: str
        :param _RollbackTimeRanges: Time range available for rollback
        :type RollbackTimeRanges: list of RollbackTimeRange
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TimeRangeStart = None
        self._TimeRangeEnd = None
        self._RollbackTimeRanges = None
        self._RequestId = None

    @property
    def TimeRangeStart(self):
        """Valid regression time range start time point (abandoned).
        :rtype: str
        """
        return self._TimeRangeStart

    @TimeRangeStart.setter
    def TimeRangeStart(self, TimeRangeStart):
        self._TimeRangeStart = TimeRangeStart

    @property
    def TimeRangeEnd(self):
        """Valid regression time range end time point (abandoned).
        :rtype: str
        """
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

    @property
    def RollbackTimeRanges(self):
        """Time range available for rollback
        :rtype: list of RollbackTimeRange
        """
        return self._RollbackTimeRanges

    @RollbackTimeRanges.setter
    def RollbackTimeRanges(self, RollbackTimeRanges):
        self._RollbackTimeRanges = RollbackTimeRanges

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeServerlessInstanceSpecsRequest(AbstractModel):
    """DescribeServerlessInstanceSpecs request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        """Availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessInstanceSpecsResponse(AbstractModel):
    """DescribeServerlessInstanceSpecs response structure.

    """

    def __init__(self):
        r"""
        :param _Specs: Available specifications of Serverless instance.
        :type Specs: list of ServerlessSpec
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Specs = None
        self._RequestId = None

    @property
    def Specs(self):
        """Available specifications of Serverless instance.
        :rtype: list of ServerlessSpec
        """
        return self._Specs

    @Specs.setter
    def Specs(self, Specs):
        self._Specs = Specs

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Specs") is not None:
            self._Specs = []
            for item in params.get("Specs"):
                obj = ServerlessSpec()
                obj._deserialize(item)
                self._Specs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServerlessStrategyRequest(AbstractModel):
    """DescribeServerlessStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Specifies the serverless cluster id.
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """Specifies the serverless cluster id.
        :rtype: str
        """
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
        


class DescribeServerlessStrategyResponse(AbstractModel):
    """DescribeServerlessStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _AutoPauseDelay: Specifies how long (in seconds) the auto-pause is triggered when the cpu load is 0.
        :type AutoPauseDelay: int
        :param _AutoScaleUpDelay: Specifies how long (in seconds) the auto-scaling is triggered when the cpu load exceeds the number of cores in the current specifications.
        :type AutoScaleUpDelay: int
        :param _AutoScaleDownDelay: Specifies how long (in seconds) the system will wait for the cpu load to be lower than the number of cores in the lower specification before triggering automatic scaling down.
        :type AutoScaleDownDelay: int
        :param _AutoPause: Whether to automatically pause. valid values:.
yes
no
        :type AutoPause: str
        :param _AutoScaleUp: Specifies whether the cluster allows upward scaling. valid values: <li>yes</li><li>no</li>.
        :type AutoScaleUp: str
        :param _AutoScaleDown: Whether the cluster is allowed to scale down. valid values: <li>yes</li><li>no</li>.
        :type AutoScaleDown: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoPauseDelay = None
        self._AutoScaleUpDelay = None
        self._AutoScaleDownDelay = None
        self._AutoPause = None
        self._AutoScaleUp = None
        self._AutoScaleDown = None
        self._RequestId = None

    @property
    def AutoPauseDelay(self):
        """Specifies how long (in seconds) the auto-pause is triggered when the cpu load is 0.
        :rtype: int
        """
        return self._AutoPauseDelay

    @AutoPauseDelay.setter
    def AutoPauseDelay(self, AutoPauseDelay):
        self._AutoPauseDelay = AutoPauseDelay

    @property
    def AutoScaleUpDelay(self):
        """Specifies how long (in seconds) the auto-scaling is triggered when the cpu load exceeds the number of cores in the current specifications.
        :rtype: int
        """
        return self._AutoScaleUpDelay

    @AutoScaleUpDelay.setter
    def AutoScaleUpDelay(self, AutoScaleUpDelay):
        self._AutoScaleUpDelay = AutoScaleUpDelay

    @property
    def AutoScaleDownDelay(self):
        """Specifies how long (in seconds) the system will wait for the cpu load to be lower than the number of cores in the lower specification before triggering automatic scaling down.
        :rtype: int
        """
        return self._AutoScaleDownDelay

    @AutoScaleDownDelay.setter
    def AutoScaleDownDelay(self, AutoScaleDownDelay):
        self._AutoScaleDownDelay = AutoScaleDownDelay

    @property
    def AutoPause(self):
        """Whether to automatically pause. valid values:.
yes
no
        :rtype: str
        """
        return self._AutoPause

    @AutoPause.setter
    def AutoPause(self, AutoPause):
        self._AutoPause = AutoPause

    @property
    def AutoScaleUp(self):
        """Specifies whether the cluster allows upward scaling. valid values: <li>yes</li><li>no</li>.
        :rtype: str
        """
        return self._AutoScaleUp

    @AutoScaleUp.setter
    def AutoScaleUp(self, AutoScaleUp):
        self._AutoScaleUp = AutoScaleUp

    @property
    def AutoScaleDown(self):
        """Whether the cluster is allowed to scale down. valid values: <li>yes</li><li>no</li>.
        :rtype: str
        """
        return self._AutoScaleDown

    @AutoScaleDown.setter
    def AutoScaleDown(self, AutoScaleDown):
        self._AutoScaleDown = AutoScaleDown

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoPauseDelay = params.get("AutoPauseDelay")
        self._AutoScaleUpDelay = params.get("AutoScaleUpDelay")
        self._AutoScaleDownDelay = params.get("AutoScaleDownDelay")
        self._AutoPause = params.get("AutoPause")
        self._AutoScaleUp = params.get("AutoScaleUp")
        self._AutoScaleDown = params.get("AutoScaleDown")
        self._RequestId = params.get("RequestId")


class DescribeSlaveZonesRequest(AbstractModel):
    """DescribeSlaveZones request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone
        :type Zone: str
        :param _OssClusterId: Cloud frame cluster ID.
        :type OssClusterId: int
        """
        self._Zone = None
        self._OssClusterId = None

    @property
    def Zone(self):
        """Availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def OssClusterId(self):
        """Cloud frame cluster ID.
        :rtype: int
        """
        return self._OssClusterId

    @OssClusterId.setter
    def OssClusterId(self, OssClusterId):
        self._OssClusterId = OssClusterId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._OssClusterId = params.get("OssClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlaveZonesResponse(AbstractModel):
    """DescribeSlaveZones response structure.

    """

    def __init__(self):
        r"""
        :param _SlaveZones: Secondary AZ.
        :type SlaveZones: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SlaveZones = None
        self._RequestId = None

    @property
    def SlaveZones(self):
        """Secondary AZ.
        :rtype: list of str
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SlaveZones = params.get("SlaveZones")
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        """Database proxy group ID
        :rtype: str
        """
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
        :param _SupportProxyVersions: Supported database proxy version collections.
        :type SupportProxyVersions: list of str
        :param _CurrentProxyVersion: The current proxy version number.
        :type CurrentProxyVersion: str
        :param _SupportProxyVersionDetail: Specifies the proxy version details.
        :type SupportProxyVersionDetail: list of ProxyVersionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SupportProxyVersions = None
        self._CurrentProxyVersion = None
        self._SupportProxyVersionDetail = None
        self._RequestId = None

    @property
    def SupportProxyVersions(self):
        """Supported database proxy version collections.
        :rtype: list of str
        """
        return self._SupportProxyVersions

    @SupportProxyVersions.setter
    def SupportProxyVersions(self, SupportProxyVersions):
        self._SupportProxyVersions = SupportProxyVersions

    @property
    def CurrentProxyVersion(self):
        """The current proxy version number.
        :rtype: str
        """
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def SupportProxyVersionDetail(self):
        """Specifies the proxy version details.
        :rtype: list of ProxyVersionInfo
        """
        return self._SupportProxyVersionDetail

    @SupportProxyVersionDetail.setter
    def SupportProxyVersionDetail(self, SupportProxyVersionDetail):
        self._SupportProxyVersionDetail = SupportProxyVersionDetail

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SupportProxyVersions = params.get("SupportProxyVersions")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        if params.get("SupportProxyVersionDetail") is not None:
            self._SupportProxyVersionDetail = []
            for item in params.get("SupportProxyVersionDetail"):
                obj = ProxyVersionInfo()
                obj._deserialize(item)
                self._SupportProxyVersionDetail.append(obj)
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
        """Whether the virtual zone is included.–
        :rtype: bool
        """
        return self._IncludeVirtualZones

    @IncludeVirtualZones.setter
    def IncludeVirtualZones(self, IncludeVirtualZones):
        self._IncludeVirtualZones = IncludeVirtualZones

    @property
    def ShowPermission(self):
        """Whether to display all AZs in a region and the user’s permissions in each AZ.
        :rtype: bool
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        """Region information
        :rtype: list of SaleRegion
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _Timestamp: Time
        :type Timestamp: str
        :param _Level: Specifies the log level. valid values are note, warning, and error.
        :type Level: str
        :param _Content: Log content.
        :type Content: str
        """
        self._Timestamp = None
        self._Level = None
        self._Content = None

    @property
    def Timestamp(self):
        """Time
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Level(self):
        """Specifies the log level. valid values are note, warning, and error.
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Content(self):
        """Log content.
        :rtype: str
        """
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
        :param _OrderByType: Sorting type. valid values: ASC or DESC.
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Log start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Log end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """The max number of returned results
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def LogLevels(self):
        """Log level
        :rtype: list of str
        """
        return self._LogLevels

    @LogLevels.setter
    def LogLevels(self, LogLevels):
        self._LogLevels = LogLevels

    @property
    def KeyWords(self):
        """
        :rtype: list of str
        """
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords

    @property
    def FileType(self):
        """The template type. Valid values: `csv`, `original`.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def OrderBy(self):
        """Valid value: `Timestamp`
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting type. valid values: ASC or DESC.
        :rtype: str
        """
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
        :param _ErrorLogItems: Exported error log content.
        :type ErrorLogItems: list of ErrorLogItemExport
        :param _FileContent: Error log string.
        :type FileContent: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorLogItems = None
        self._FileContent = None
        self._RequestId = None

    @property
    def ErrorLogItems(self):
        """Exported error log content.
        :rtype: list of ErrorLogItemExport
        """
        return self._ErrorLogItems

    @ErrorLogItems.setter
    def ErrorLogItems(self, ErrorLogItems):
        self._ErrorLogItems = ErrorLogItems

    @property
    def FileContent(self):
        """Error log string.
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        self._FileContent = params.get("FileContent")
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Transaction start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Transaction end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """Maximum number
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Username(self):
        """Username
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Host(self):
        """Client host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def FileType(self):
        """File type. Valid values: csv, original.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def OrderBy(self):
        """Sorting field. Valid values: `QueryTime`, `LockTime`, `RowsExamined`, and `RowsSent`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting order. Valid values: `asc`, `desc`.
        :rtype: str
        """
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
        """Slow query export content
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._RequestId = params.get("RequestId")


class ExportResourcePackageDeductDetailsRequest(AbstractModel):
    """ExportResourcePackageDeductDetails request structure.

    """

    def __init__(self):
        r"""
        :param _PackageId: Resource package ID to be exported.
        :type PackageId: str
        :param _ClusterIds: Specifies the cluster ID of the cynos cluster that uses the resource package capacity.
        :type ClusterIds: list of str
        :param _OrderBy: Sorting field. currently supports: createTime (resource package deduction time), successDeductSpec (resource package deduction amount).
        :type OrderBy: str
        :param _OrderByType: Sorting type. supports ASC, DESC, ASC, DESC.
        :type OrderByType: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _Limit: A maximum of 2000 rows of data can be exported at a time. currently, a maximum of 2000 rows are supported.
        :type Limit: str
        :param _Offset: Offset and page number.
        :type Offset: str
        :param _FileType: Specifies the format for exporting data. currently only supports csv format, reserved for future expansion.
        :type FileType: str
        """
        self._PackageId = None
        self._ClusterIds = None
        self._OrderBy = None
        self._OrderByType = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._FileType = None

    @property
    def PackageId(self):
        """Resource package ID to be exported.
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def ClusterIds(self):
        """Specifies the cluster ID of the cynos cluster that uses the resource package capacity.
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def OrderBy(self):
        """Sorting field. currently supports: createTime (resource package deduction time), successDeductSpec (resource package deduction amount).
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """Sorting type. supports ASC, DESC, ASC, DESC.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def StartTime(self):
        """Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """A maximum of 2000 rows of data can be exported at a time. currently, a maximum of 2000 rows are supported.
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset and page number.
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def FileType(self):
        """Specifies the format for exporting data. currently only supports csv format, reserved for future expansion.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._ClusterIds = params.get("ClusterIds")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportResourcePackageDeductDetailsResponse(AbstractModel):
    """ExportResourcePackageDeductDetails response structure.

    """

    def __init__(self):
        r"""
        :param _FileContent: File detail.
        :type FileContent: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileContent = None
        self._RequestId = None

    @property
    def FileContent(self):
        """File detail.
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Account
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Host(self):
        """Host. Default value: `%`
        :rtype: str
        """
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
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def GoodsNum(self):
        """Number of compute node to purchase
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def InstancePayMode(self):
        """Instance type for purchase. Valid values: `PREPAID`, `POSTPAID`, `SERVERLESS`.
        :rtype: str
        """
        return self._InstancePayMode

    @InstancePayMode.setter
    def InstancePayMode(self, InstancePayMode):
        self._InstancePayMode = InstancePayMode

    @property
    def StoragePayMode(self):
        """Storage type for purchase. Valid values: `PREPAID`, `POSTPAID`.
        :rtype: str
        """
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def DeviceType(self):
        """device type:common, exclusive
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Cpu(self):
        """Number of CPU cores, which is required when `InstancePayMode` is `PREPAID` or `POSTPAID`.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Memory size in GB, which is required when `InstancePayMode` is `PREPAID` or `POSTPAID`.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Ccu(self):
        """CCU size, which is required when `InstancePayMode` is `SERVERLESS`.
        :rtype: float
        """
        return self._Ccu

    @Ccu.setter
    def Ccu(self, Ccu):
        self._Ccu = Ccu

    @property
    def StorageLimit(self):
        """Storage size, which is required when `StoragePayMode` is `PREPAID`.
        :rtype: int
        """
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def TimeSpan(self):
        """Validity period, which is required when `InstancePayMode` is `PREPAID`.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """Duration unit, which is required when `InstancePayMode` is `PREPAID`. Valid values: `m` (month), `d` (day).
        :rtype: str
        """
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
        """Instance price
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def StoragePrice(self):
        """Storage price
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        """
        return self._StoragePrice

    @StoragePrice.setter
    def StoragePrice(self, StoragePrice):
        self._StoragePrice = StoragePrice

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class InquirePriceModifyRequest(AbstractModel):
    """InquirePriceModify request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Cpu: Specifies the number of CPU cores.
        :type Cpu: int
        :param _Memory: Memory Size
        :type Memory: int
        :param _StorageLimit: Storage size, storage resource adjustment: ClusterId, StorageLimit.
        :type StorageLimit: int
        :param _InstanceId: Instance ID. computational resource adjustment requires passing: ClusterId, instance ID, Cpu, Memory.
        :type InstanceId: str
        :param _DeviceType: Instance device type.
        :type DeviceType: str
        :param _Ccu: Specifies the ccu size of the serverless instance.
        :type Ccu: float
        """
        self._ClusterId = None
        self._Cpu = None
        self._Memory = None
        self._StorageLimit = None
        self._InstanceId = None
        self._DeviceType = None
        self._Ccu = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Cpu(self):
        """Specifies the number of CPU cores.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Memory Size
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def StorageLimit(self):
        """Storage size, storage resource adjustment: ClusterId, StorageLimit.
        :rtype: int
        """
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def InstanceId(self):
        """Instance ID. computational resource adjustment requires passing: ClusterId, instance ID, Cpu, Memory.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceType(self):
        """Instance device type.
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Ccu(self):
        """Specifies the ccu size of the serverless instance.
        :rtype: float
        """
        return self._Ccu

    @Ccu.setter
    def Ccu(self, Ccu):
        self._Ccu = Ccu


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._StorageLimit = params.get("StorageLimit")
        self._InstanceId = params.get("InstanceId")
        self._DeviceType = params.get("DeviceType")
        self._Ccu = params.get("Ccu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyResponse(AbstractModel):
    """InquirePriceModify response structure.

    """

    def __init__(self):
        r"""
        :param _InstancePrice: Instance price.
        :type InstancePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param _StoragePrice: Specifies the storage price.
        :type StoragePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstancePrice = None
        self._StoragePrice = None
        self._RequestId = None

    @property
    def InstancePrice(self):
        """Instance price.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def StoragePrice(self):
        """Specifies the storage price.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        """
        return self._StoragePrice

    @StoragePrice.setter
    def StoragePrice(self, StoragePrice):
        self._StoragePrice = StoragePrice

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TimeSpan(self):
        """Validity period, which needs to be used together with `TimeUnit`.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """Unit of validity period, which needs to be used together with `TimeSpan`. Valid values: `d` (day), `m` (month).
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        """Instance ID list
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Prices(self):
        """Price of instance specification in array
        :rtype: list of TradePrice
        """
        return self._Prices

    @Prices.setter
    def Prices(self, Prices):
        self._Prices = Prices

    @property
    def InstanceRealTotalPrice(self):
        """Total renewal price of compute node
        :rtype: int
        """
        return self._InstanceRealTotalPrice

    @InstanceRealTotalPrice.setter
    def InstanceRealTotalPrice(self, InstanceRealTotalPrice):
        self._InstanceRealTotalPrice = InstanceRealTotalPrice

    @property
    def StorageRealTotalPrice(self):
        """Total renewal price of storage node
        :rtype: int
        """
        return self._StorageRealTotalPrice

    @StorageRealTotalPrice.setter
    def StorageRealTotalPrice(self, StorageRealTotalPrice):
        self._StorageRealTotalPrice = StorageRealTotalPrice

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class InstanceAbility(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _IsSupportForceRestart: Specifies whether the instance supports forced reboot. valid values: yes (supported), no (unsupported).
        :type IsSupportForceRestart: str
        :param _NonsupportForceRestartReason: Specifies the causes for not supporting forced reboot.
        :type NonsupportForceRestartReason: str
        """
        self._IsSupportForceRestart = None
        self._NonsupportForceRestartReason = None

    @property
    def IsSupportForceRestart(self):
        """Specifies whether the instance supports forced reboot. valid values: yes (supported), no (unsupported).
        :rtype: str
        """
        return self._IsSupportForceRestart

    @IsSupportForceRestart.setter
    def IsSupportForceRestart(self, IsSupportForceRestart):
        self._IsSupportForceRestart = IsSupportForceRestart

    @property
    def NonsupportForceRestartReason(self):
        """Specifies the causes for not supporting forced reboot.
        :rtype: str
        """
        return self._NonsupportForceRestartReason

    @NonsupportForceRestartReason.setter
    def NonsupportForceRestartReason(self, NonsupportForceRestartReason):
        self._NonsupportForceRestartReason = NonsupportForceRestartReason


    def _deserialize(self, params):
        self._IsSupportForceRestart = params.get("IsSupportForceRestart")
        self._NonsupportForceRestartReason = params.get("NonsupportForceRestartReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAuditRule(AbstractModel):
    """Audit rule details of the instance, which is an output parameter of the `DescribeAuditRuleWithInstanceIds` API.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _AuditRule: Specifies whether it is a rule-based audit. true - rule-based audit; false - comprehensive audit.
        :type AuditRule: bool
        :param _AuditRuleFilters: Specifies the audit rule details. valid when AuditRule=true.
        :type AuditRuleFilters: list of AuditRuleFilters
        :param _OldRule: Whether it is an audit policy.
        :type OldRule: bool
        :param _RuleTemplates: The rule template details of the instance application.
        :type RuleTemplates: list of RuleTemplateInfo
        """
        self._InstanceId = None
        self._AuditRule = None
        self._AuditRuleFilters = None
        self._OldRule = None
        self._RuleTemplates = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AuditRule(self):
        """Specifies whether it is a rule-based audit. true - rule-based audit; false - comprehensive audit.
        :rtype: bool
        """
        return self._AuditRule

    @AuditRule.setter
    def AuditRule(self, AuditRule):
        self._AuditRule = AuditRule

    @property
    def AuditRuleFilters(self):
        """Specifies the audit rule details. valid when AuditRule=true.
        :rtype: list of AuditRuleFilters
        """
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters

    @property
    def OldRule(self):
        """Whether it is an audit policy.
        :rtype: bool
        """
        return self._OldRule

    @OldRule.setter
    def OldRule(self, OldRule):
        self._OldRule = OldRule

    @property
    def RuleTemplates(self):
        """The rule template details of the instance application.
        :rtype: list of RuleTemplateInfo
        """
        return self._RuleTemplates

    @RuleTemplates.setter
    def RuleTemplates(self, RuleTemplates):
        self._RuleTemplates = RuleTemplates


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AuditRule = params.get("AuditRule")
        if params.get("AuditRuleFilters") is not None:
            self._AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self._AuditRuleFilters.append(obj)
        self._OldRule = params.get("OldRule")
        if params.get("RuleTemplates") is not None:
            self._RuleTemplates = []
            for item in params.get("RuleTemplates"):
                obj = RuleTemplateInfo()
                obj._deserialize(item)
                self._RuleTemplates.append(obj)
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
        """Instance CPU
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Instance memory
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceType(self):
        """Instance type. Valid values:`rw`, `ro`.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceCount(self):
        """Number of the instances. Value range: 1-15.
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def MinRoCount(self):
        """Minimum number of serverless instances. Value range: 1-15.
        :rtype: int
        """
        return self._MinRoCount

    @MinRoCount.setter
    def MinRoCount(self, MinRoCount):
        self._MinRoCount = MinRoCount

    @property
    def MaxRoCount(self):
        """Maximum number of serverless instances. Value range: 1-15.
        :rtype: int
        """
        return self._MaxRoCount

    @MaxRoCount.setter
    def MaxRoCount(self, MaxRoCount):
        self._MaxRoCount = MaxRoCount

    @property
    def MinRoCpu(self):
        """Minimum specifications for serverless instance
        :rtype: float
        """
        return self._MinRoCpu

    @MinRoCpu.setter
    def MinRoCpu(self, MinRoCpu):
        self._MinRoCpu = MinRoCpu

    @property
    def MaxRoCpu(self):
        """Maximum specifications for serverless instance
        :rtype: float
        """
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
        :param _InstanceGroupType: Network type.
        :type InstanceGroupType: str
        :param _InstanceGroupId: Instance group ID
        :type InstanceGroupId: str
        :param _VpcId: Specifies the virtual private cloud ID.
        :type VpcId: str
        :param _SubnetId: Specifies the subnet ID.
        :type SubnetId: str
        :param _NetType: Network type. valid values: 0 (basic network), 1 (vpc network), 2 (blackstone network).
        :type NetType: int
        :param _Vip: VPC IP.
        :type Vip: str
        :param _Vport: VPC port.
        :type Vport: int
        :param _WanDomain: Specifies the public network domain name.
        :type WanDomain: str
        :param _WanIP: Public IP address
        :type WanIP: str
        :param _WanPort: Public network port.
        :type WanPort: int
        :param _WanStatus: Public network enabled status.
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
        """Network type.
        :rtype: str
        """
        return self._InstanceGroupType

    @InstanceGroupType.setter
    def InstanceGroupType(self, InstanceGroupType):
        self._InstanceGroupType = InstanceGroupType

    @property
    def InstanceGroupId(self):
        """Instance group ID
        :rtype: str
        """
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def VpcId(self):
        """Specifies the virtual private cloud ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Specifies the subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def NetType(self):
        """Network type. valid values: 0 (basic network), 1 (vpc network), 2 (blackstone network).
        :rtype: int
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Vip(self):
        """VPC IP.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """VPC port.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def WanDomain(self):
        """Specifies the public network domain name.
        :rtype: str
        """
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        """Public IP address
        :rtype: str
        """
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        """Public network port.
        :rtype: int
        """
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        """Public network enabled status.
        :rtype: str
        """
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ParamsItems(self):
        """List of instance parameters
        :rtype: list of ParamItemDetail
        """
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
        :param _ZoneStockInfos: Regional inventory information.
        :type ZoneStockInfos: list of ZoneStockInfo
        :param _StockCount: Inventory quantity.
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
        """Number of instance CPU cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Instance memory in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def MaxStorageSize(self):
        """Maximum instance storage capacity GB
        :rtype: int
        """
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def MinStorageSize(self):
        """Minimum instance storage capacity GB
        :rtype: int
        """
        return self._MinStorageSize

    @MinStorageSize.setter
    def MinStorageSize(self, MinStorageSize):
        self._MinStorageSize = MinStorageSize

    @property
    def HasStock(self):
        """Whether there is an inventory.
        :rtype: bool
        """
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock

    @property
    def MachineType(self):
        """Machine type
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MaxIops(self):
        """Maximum IOPS
        :rtype: int
        """
        return self._MaxIops

    @MaxIops.setter
    def MaxIops(self, MaxIops):
        self._MaxIops = MaxIops

    @property
    def MaxIoBandWidth(self):
        """Maximum bandwidth
        :rtype: int
        """
        return self._MaxIoBandWidth

    @MaxIoBandWidth.setter
    def MaxIoBandWidth(self, MaxIoBandWidth):
        self._MaxIoBandWidth = MaxIoBandWidth

    @property
    def ZoneStockInfos(self):
        """Regional inventory information.
        :rtype: list of ZoneStockInfo
        """
        return self._ZoneStockInfos

    @ZoneStockInfos.setter
    def ZoneStockInfos(self, ZoneStockInfos):
        self._ZoneStockInfos = ZoneStockInfos

    @property
    def StockCount(self):
        """Inventory quantity.
        :rtype: int
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbType(self):
        """This parameter has been disused.
        :rtype: str
        """
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
        :param _FlowId: Task flow ID (returned for pay-as-you-go or serverless resources. if necessary to sync task status, please use the DescribeFlow api).
        :type FlowId: int
        :param _DealNames: Refund order number (returned for prepaid resources. if necessary, synchronize the order status by using the billing product's DescribeDealsByCond to synchronize the order status).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._DealNames = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID (returned for pay-as-you-go or serverless resources. if necessary to sync task status, please use the DescribeFlow api).
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        """Refund order number (returned for prepaid resources. if necessary, synchronize the order status by using the billing product's DescribeDealsByCond to synchronize the order status).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdList(self):
        """Instance ID array
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def DbType(self):
        """This parameter has been disused.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._DealNames = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        """Order ID for isolated instance (prepaid instance)
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class LogicBackupConfigInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _LogicBackupEnable: Whether automatic logical backup is enabled.
        :type LogicBackupEnable: str
        :param _LogicBackupTimeBeg: Specifies the automatic logic backup start time.
        :type LogicBackupTimeBeg: int
        :param _LogicBackupTimeEnd: Specifies the termination time of automatic logical backup.
        :type LogicBackupTimeEnd: int
        :param _LogicReserveDuration: Specifies the retention time for automatic logical backup.
        :type LogicReserveDuration: int
        :param _LogicCrossRegionsEnable: Whether cross-regional logical backup is enabled.
        :type LogicCrossRegionsEnable: str
        :param _LogicCrossRegions: 
        :type LogicCrossRegions: list of str
        """
        self._LogicBackupEnable = None
        self._LogicBackupTimeBeg = None
        self._LogicBackupTimeEnd = None
        self._LogicReserveDuration = None
        self._LogicCrossRegionsEnable = None
        self._LogicCrossRegions = None

    @property
    def LogicBackupEnable(self):
        """Whether automatic logical backup is enabled.
        :rtype: str
        """
        return self._LogicBackupEnable

    @LogicBackupEnable.setter
    def LogicBackupEnable(self, LogicBackupEnable):
        self._LogicBackupEnable = LogicBackupEnable

    @property
    def LogicBackupTimeBeg(self):
        """Specifies the automatic logic backup start time.
        :rtype: int
        """
        return self._LogicBackupTimeBeg

    @LogicBackupTimeBeg.setter
    def LogicBackupTimeBeg(self, LogicBackupTimeBeg):
        self._LogicBackupTimeBeg = LogicBackupTimeBeg

    @property
    def LogicBackupTimeEnd(self):
        """Specifies the termination time of automatic logical backup.
        :rtype: int
        """
        return self._LogicBackupTimeEnd

    @LogicBackupTimeEnd.setter
    def LogicBackupTimeEnd(self, LogicBackupTimeEnd):
        self._LogicBackupTimeEnd = LogicBackupTimeEnd

    @property
    def LogicReserveDuration(self):
        """Specifies the retention time for automatic logical backup.
        :rtype: int
        """
        return self._LogicReserveDuration

    @LogicReserveDuration.setter
    def LogicReserveDuration(self, LogicReserveDuration):
        self._LogicReserveDuration = LogicReserveDuration

    @property
    def LogicCrossRegionsEnable(self):
        """Whether cross-regional logical backup is enabled.
        :rtype: str
        """
        return self._LogicCrossRegionsEnable

    @LogicCrossRegionsEnable.setter
    def LogicCrossRegionsEnable(self, LogicCrossRegionsEnable):
        self._LogicCrossRegionsEnable = LogicCrossRegionsEnable

    @property
    def LogicCrossRegions(self):
        """
        :rtype: list of str
        """
        return self._LogicCrossRegions

    @LogicCrossRegions.setter
    def LogicCrossRegions(self, LogicCrossRegions):
        self._LogicCrossRegions = LogicCrossRegions


    def _deserialize(self, params):
        self._LogicBackupEnable = params.get("LogicBackupEnable")
        self._LogicBackupTimeBeg = params.get("LogicBackupTimeBeg")
        self._LogicBackupTimeEnd = params.get("LogicBackupTimeEnd")
        self._LogicReserveDuration = params.get("LogicReserveDuration")
        self._LogicCrossRegionsEnable = params.get("LogicCrossRegionsEnable")
        self._LogicCrossRegions = params.get("LogicCrossRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifiableInfo(AbstractModel):
    """Details of whether the parameter can be modified

    """

    def __init__(self):
        r"""
        :param _IsModifiable: 
        :type IsModifiable: int
        """
        self._IsModifiable = None

    @property
    def IsModifiable(self):
        """
        :rtype: int
        """
        return self._IsModifiable

    @IsModifiable.setter
    def IsModifiable(self, IsModifiable):
        self._IsModifiable = IsModifiable


    def _deserialize(self, params):
        self._IsModifiable = params.get("IsModifiable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """Database account name
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Description(self):
        """Database account description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Host(self):
        """Host. Default value: `%`
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NewHost(self):
        """New host
        :rtype: str
        """
        return self._NewHost

    @NewHost.setter
    def NewHost(self, NewHost):
        self._NewHost = NewHost

    @property
    def Account(self):
        """Account infomation
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Account(self):
        """Account infomation
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def GlobalPrivileges(self):
        """Array of global permissions
        :rtype: list of str
        """
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        """Array of database permissions
        :rtype: list of DatabasePrivileges
        """
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        """Array of table permissions
        :rtype: list of TablePrivileges
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Audit rule template ID
        :rtype: list of str
        """
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds

    @property
    def RuleFilters(self):
        """Audit rule after modification
        :rtype: list of RuleFilters
        """
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def RuleTemplateName(self):
        """New name of the rule template
        :rtype: str
        """
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def Description(self):
        """New description of the rule template
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        """Log retention period
        :rtype: int
        """
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HighLogExpireDay(self):
        """Frequent log retention period
        :rtype: int
        """
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay

    @property
    def AuditAll(self):
        """The parameter used to change the audit rule of the instance to full audit
        :rtype: bool
        """
        return self._AuditAll

    @AuditAll.setter
    def AuditAll(self, AuditAll):
        self._AuditAll = AuditAll

    @property
    def AuditRuleFilters(self):
        """Rule audit
        :rtype: list of AuditRuleFilters
        """
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters

    @property
    def RuleTemplateIds(self):
        """Rule template ID
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _BackupType: Currently, this parameter does not support modification and is not required.
        :type BackupType: str
        :param _LogicBackupConfig: 
        :type LogicBackupConfig: :class:`tencentcloud.cynosdb.v20190107.models.LogicBackupConfigInfo`
        :param _DeleteAutoLogicBackup: 
        :type DeleteAutoLogicBackup: bool
        """
        self._ClusterId = None
        self._BackupTimeBeg = None
        self._BackupTimeEnd = None
        self._ReserveDuration = None
        self._BackupFreq = None
        self._BackupType = None
        self._LogicBackupConfig = None
        self._DeleteAutoLogicBackup = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupTimeBeg(self):
        """Full backup start time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively
        :rtype: int
        """
        return self._BackupTimeBeg

    @BackupTimeBeg.setter
    def BackupTimeBeg(self, BackupTimeBeg):
        self._BackupTimeBeg = BackupTimeBeg

    @property
    def BackupTimeEnd(self):
        """Full backup end time. Value range: [0-24*3600]. For example, 0:00 AM, 1:00 AM, and 2:00 AM are represented by 0, 3600, and 7200, respectively.
        :rtype: int
        """
        return self._BackupTimeEnd

    @BackupTimeEnd.setter
    def BackupTimeEnd(self, BackupTimeEnd):
        self._BackupTimeEnd = BackupTimeEnd

    @property
    def ReserveDuration(self):
        """Backup retention period in seconds. Backups will be cleared after this period elapses. 7 days is represented by 3600*24*7 = 604800. Maximum value: 158112000.
        :rtype: int
        """
        return self._ReserveDuration

    @ReserveDuration.setter
    def ReserveDuration(self, ReserveDuration):
        self._ReserveDuration = ReserveDuration

    @property
    def BackupFreq(self):
        """Backup frequency. It is an array of 7 elements corresponding to Monday through Sunday. full: full backup; increment: incremental backup. This parameter cannot be modified currently and doesn't need to be entered.
        :rtype: list of str
        """
        return self._BackupFreq

    @BackupFreq.setter
    def BackupFreq(self, BackupFreq):
        self._BackupFreq = BackupFreq

    @property
    def BackupType(self):
        """Currently, this parameter does not support modification and is not required.
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def LogicBackupConfig(self):
        """
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.LogicBackupConfigInfo`
        """
        return self._LogicBackupConfig

    @LogicBackupConfig.setter
    def LogicBackupConfig(self, LogicBackupConfig):
        self._LogicBackupConfig = LogicBackupConfig

    @property
    def DeleteAutoLogicBackup(self):
        """
        :rtype: bool
        """
        return self._DeleteAutoLogicBackup

    @DeleteAutoLogicBackup.setter
    def DeleteAutoLogicBackup(self, DeleteAutoLogicBackup):
        self._DeleteAutoLogicBackup = DeleteAutoLogicBackup


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupTimeBeg = params.get("BackupTimeBeg")
        self._BackupTimeEnd = params.get("BackupTimeEnd")
        self._ReserveDuration = params.get("ReserveDuration")
        self._BackupFreq = params.get("BackupFreq")
        self._BackupType = params.get("BackupType")
        if params.get("LogicBackupConfig") is not None:
            self._LogicBackupConfig = LogicBackupConfigInfo()
            self._LogicBackupConfig._deserialize(params.get("LogicBackupConfig"))
        self._DeleteAutoLogicBackup = params.get("DeleteAutoLogicBackup")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    """ModifyBackupDownloadRestriction request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: Cluster ID
        :type ClusterIds: list of str
        :param _LimitType: Download limit type. valid values: NoLimit (unlimited), LimitOnlyIntranet (limited to private network), Customize (custom).
        :type LimitType: str
        :param _VpcComparisonSymbol: This parameter only supports In, which indicates that the vpc specified by LimitVpc can be downloaded. the default is In.
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: Specified ips can download; specified ips are not allowed to download.
        :type IpComparisonSymbol: str
        :param _LimitVpcs: Limit the vpc settings for downloads.
        :type LimitVpcs: list of BackupLimitVpcItem
        :param _LimitIps: Specifies the ip settings for limiting downloads.
        :type LimitIps: list of str
        """
        self._ClusterIds = None
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpcs = None
        self._LimitIps = None

    @property
    def ClusterIds(self):
        """Cluster ID
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def LimitType(self):
        """Download limit type. valid values: NoLimit (unlimited), LimitOnlyIntranet (limited to private network), Customize (custom).
        :rtype: str
        """
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        """This parameter only supports In, which indicates that the vpc specified by LimitVpc can be downloaded. the default is In.
        :rtype: str
        """
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        """Specified ips can download; specified ips are not allowed to download.
        :rtype: str
        """
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpcs(self):
        """Limit the vpc settings for downloads.
        :rtype: list of BackupLimitVpcItem
        """
        return self._LimitVpcs

    @LimitVpcs.setter
    def LimitVpcs(self, LimitVpcs):
        self._LimitVpcs = LimitVpcs

    @property
    def LimitIps(self):
        """Specifies the ip settings for limiting downloads.
        :rtype: list of str
        """
        return self._LimitIps

    @LimitIps.setter
    def LimitIps(self, LimitIps):
        self._LimitIps = LimitIps


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpcs") is not None:
            self._LimitVpcs = []
            for item in params.get("LimitVpcs"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpcs.append(obj)
        self._LimitIps = params.get("LimitIps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadRestrictionResponse(AbstractModel):
    """ModifyBackupDownloadRestriction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBackupDownloadUserRestrictionRequest(AbstractModel):
    """ModifyBackupDownloadUserRestriction request structure.

    """

    def __init__(self):
        r"""
        :param _LimitType: Download limit type. valid values: NoLimit (unlimited), LimitOnlyIntranet (limited to private network), Customize (custom).
        :type LimitType: str
        :param _VpcComparisonSymbol: This parameter only supports In, which indicates that the vpc specified by LimitVpc can be downloaded. the default is In.
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: Specified ips can download; specified ips are not allowed to download.
        :type IpComparisonSymbol: str
        :param _LimitVpcs: Limit the vpc settings for downloads.
        :type LimitVpcs: list of BackupLimitVpcItem
        :param _LimitIps: Specifies the ip settings for limiting downloads.
        :type LimitIps: list of str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpcs = None
        self._LimitIps = None

    @property
    def LimitType(self):
        """Download limit type. valid values: NoLimit (unlimited), LimitOnlyIntranet (limited to private network), Customize (custom).
        :rtype: str
        """
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        """This parameter only supports In, which indicates that the vpc specified by LimitVpc can be downloaded. the default is In.
        :rtype: str
        """
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        """Specified ips can download; specified ips are not allowed to download.
        :rtype: str
        """
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpcs(self):
        """Limit the vpc settings for downloads.
        :rtype: list of BackupLimitVpcItem
        """
        return self._LimitVpcs

    @LimitVpcs.setter
    def LimitVpcs(self, LimitVpcs):
        self._LimitVpcs = LimitVpcs

    @property
    def LimitIps(self):
        """Specifies the ip settings for limiting downloads.
        :rtype: list of str
        """
        return self._LimitIps

    @LimitIps.setter
    def LimitIps(self, LimitIps):
        self._LimitIps = LimitIps


    def _deserialize(self, params):
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpcs") is not None:
            self._LimitVpcs = []
            for item in params.get("LimitVpcs"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpcs.append(obj)
        self._LimitIps = params.get("LimitIps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadUserRestrictionResponse(AbstractModel):
    """ModifyBackupDownloadUserRestriction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupId(self):
        """Backup file ID
        :rtype: int
        """
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupName(self):
        """Backup name, which can contain up to 60 characters.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBinlogConfigRequest(AbstractModel):
    """ModifyBinlogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _BinlogConfig: Specifies the Binlog configuration message.
        :type BinlogConfig: :class:`tencentcloud.cynosdb.v20190107.models.BinlogConfigInfo`
        """
        self._ClusterId = None
        self._BinlogConfig = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BinlogConfig(self):
        """Specifies the Binlog configuration message.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.BinlogConfigInfo`
        """
        return self._BinlogConfig

    @BinlogConfig.setter
    def BinlogConfig(self, BinlogConfig):
        self._BinlogConfig = BinlogConfig


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("BinlogConfig") is not None:
            self._BinlogConfig = BinlogConfigInfo()
            self._BinlogConfig._deserialize(params.get("BinlogConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBinlogConfigResponse(AbstractModel):
    """ModifyBinlogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BinlogSaveDays(self):
        """Binlog retention period in days
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbName(self):
        """Database name
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def NewUserHostPrivileges(self):
        """Host permissions of the new authorized user
        :rtype: list of UserHostPrivilege
        """
        return self._NewUserHostPrivileges

    @NewUserHostPrivileges.setter
    def NewUserHostPrivileges(self, NewUserHostPrivileges):
        self._NewUserHostPrivileges = NewUserHostPrivileges

    @property
    def Description(self):
        """Remarks
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OldUserHostPrivileges(self):
        """Host permissions of previously authorized users
        :rtype: list of UserHostPrivilege
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """Cluster name
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ParamList(self):
        """List of the parameters to be modified. Each element in the list is a combination of `ParamName`, `CurrentValue`, and `OldValue`. `ParamName` is the parameter name; `CurrentValue` is the current value; `OldValue` is the old value that doesn’t need to be verified.
        :rtype: list of ParamItem
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def IsInMaintainPeriod(self):
        """Valid values: `yes` (execute during maintenance time), `no` (execute now)
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        """Async request ID used to query the result
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ValidatePasswordLength(self):
        """Password length
        :rtype: int
        """
        return self._ValidatePasswordLength

    @ValidatePasswordLength.setter
    def ValidatePasswordLength(self, ValidatePasswordLength):
        self._ValidatePasswordLength = ValidatePasswordLength

    @property
    def ValidatePasswordMixedCaseCount(self):
        """Number of letters
        :rtype: int
        """
        return self._ValidatePasswordMixedCaseCount

    @ValidatePasswordMixedCaseCount.setter
    def ValidatePasswordMixedCaseCount(self, ValidatePasswordMixedCaseCount):
        self._ValidatePasswordMixedCaseCount = ValidatePasswordMixedCaseCount

    @property
    def ValidatePasswordSpecialCharCount(self):
        """Number of symbols
        :rtype: int
        """
        return self._ValidatePasswordSpecialCharCount

    @ValidatePasswordSpecialCharCount.setter
    def ValidatePasswordSpecialCharCount(self, ValidatePasswordSpecialCharCount):
        self._ValidatePasswordSpecialCharCount = ValidatePasswordSpecialCharCount

    @property
    def ValidatePasswordNumberCount(self):
        """Number of digits
        :rtype: int
        """
        return self._ValidatePasswordNumberCount

    @ValidatePasswordNumberCount.setter
    def ValidatePasswordNumberCount(self, ValidatePasswordNumberCount):
        self._ValidatePasswordNumberCount = ValidatePasswordNumberCount

    @property
    def ValidatePasswordPolicy(self):
        """Password strength. Valid values: `MEDIUM`, `STRONG`.
        :rtype: str
        """
        return self._ValidatePasswordPolicy

    @ValidatePasswordPolicy.setter
    def ValidatePasswordPolicy(self, ValidatePasswordPolicy):
        self._ValidatePasswordPolicy = ValidatePasswordPolicy

    @property
    def ValidatePasswordDictionary(self):
        """Data dictionary
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyClusterReadOnlyRequest(AbstractModel):
    """ModifyClusterReadOnly request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: List of cluster IDs
        :type ClusterIds: list of str
        :param _ReadOnlyOperation: Cluster read-only switch, valid values: ON, OFF.
        :type ReadOnlyOperation: str
        :param _IsInMaintainPeriod: Valid values: `yes` (modify in maintenance window), `no` (execute now by default).
        :type IsInMaintainPeriod: str
        """
        self._ClusterIds = None
        self._ReadOnlyOperation = None
        self._IsInMaintainPeriod = None

    @property
    def ClusterIds(self):
        """List of cluster IDs
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def ReadOnlyOperation(self):
        """Cluster read-only switch, valid values: ON, OFF.
        :rtype: str
        """
        return self._ReadOnlyOperation

    @ReadOnlyOperation.setter
    def ReadOnlyOperation(self, ReadOnlyOperation):
        self._ReadOnlyOperation = ReadOnlyOperation

    @property
    def IsInMaintainPeriod(self):
        """Valid values: `yes` (modify in maintenance window), `no` (execute now by default).
        :rtype: str
        """
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._ReadOnlyOperation = params.get("ReadOnlyOperation")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterReadOnlyResponse(AbstractModel):
    """ModifyClusterReadOnly response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterTaskIds: List of cluster task ids.
        :type ClusterTaskIds: list of ClusterTaskId
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterTaskIds = None
        self._RequestId = None

    @property
    def ClusterTaskIds(self):
        """List of cluster task ids.
        :rtype: list of ClusterTaskId
        """
        return self._ClusterTaskIds

    @ClusterTaskIds.setter
    def ClusterTaskIds(self, ClusterTaskIds):
        self._ClusterTaskIds = ClusterTaskIds

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterTaskIds") is not None:
            self._ClusterTaskIds = []
            for item in params.get("ClusterTaskIds"):
                obj = ClusterTaskId()
                obj._deserialize(item)
                self._ClusterTaskIds.append(obj)
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
        :param _BinlogSyncWay: Specifies the binlog synchronization mode. the default value is async. valid values are sync, semisync, and async.
        :type BinlogSyncWay: str
        """
        self._ClusterId = None
        self._OldSlaveZone = None
        self._NewSlaveZone = None
        self._BinlogSyncWay = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def OldSlaveZone(self):
        """Old replica AZ
        :rtype: str
        """
        return self._OldSlaveZone

    @OldSlaveZone.setter
    def OldSlaveZone(self, OldSlaveZone):
        self._OldSlaveZone = OldSlaveZone

    @property
    def NewSlaveZone(self):
        """New replica AZ
        :rtype: str
        """
        return self._NewSlaveZone

    @NewSlaveZone.setter
    def NewSlaveZone(self, NewSlaveZone):
        self._NewSlaveZone = NewSlaveZone

    @property
    def BinlogSyncWay(self):
        """Specifies the binlog synchronization mode. the default value is async. valid values are sync, semisync, and async.
        :rtype: str
        """
        return self._BinlogSyncWay

    @BinlogSyncWay.setter
    def BinlogSyncWay(self, BinlogSyncWay):
        self._BinlogSyncWay = BinlogSyncWay


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._OldSlaveZone = params.get("OldSlaveZone")
        self._NewSlaveZone = params.get("NewSlaveZone")
        self._BinlogSyncWay = params.get("BinlogSyncWay")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async FlowId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _InstanceId: Network group id (starting with the cynosdbmysql-grp- prefix) or cluster id.
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
        """Network group id (starting with the cynosdbmysql-grp- prefix) or cluster id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        """List of IDs of security groups to be modified, which is an array of one or more security group IDs.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zone(self):
        """AZ
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        """Instance ID
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClusterParamList(self):
        """List of cluster parameters
        :rtype: list of ModifyParamItem
        """
        return self._ClusterParamList

    @ClusterParamList.setter
    def ClusterParamList(self, ClusterParamList):
        self._ClusterParamList = ClusterParamList

    @property
    def InstanceParamList(self):
        """List of the instance parameters
        :rtype: list of ModifyParamItem
        """
        return self._InstanceParamList

    @InstanceParamList.setter
    def InstanceParamList(self, InstanceParamList):
        self._InstanceParamList = InstanceParamList

    @property
    def IsInMaintainPeriod(self):
        """Valid values: `yes` (modify in maintenance window),  `no`  (execute now by default).
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MaintainStartTime(self):
        """Maintenance start time in seconds. For example, 03:00 AM is represented by 10800
        :rtype: int
        """
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        """Maintenance duration in seconds. For example, one hour is represented by 3600
        :rtype: int
        """
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        """Maintenance days of the week. Valid values: [Mon, Tue, Wed, Thu, Fri, Sat, Sun].
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _OldValue: Old parameter value (useful only in output parameters).
        :type OldValue: str
        :param _Component: libra component type.
        :type Component: str
        """
        self._ParamName = None
        self._CurrentValue = None
        self._OldValue = None
        self._Component = None

    @property
    def ParamName(self):
        """Parameter name
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def CurrentValue(self):
        """Current parameter value
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def OldValue(self):
        """Old parameter value (useful only in output parameters).
        :rtype: str
        """
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def Component(self):
        """libra component type.
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._CurrentValue = params.get("CurrentValue")
        self._OldValue = params.get("OldValue")
        self._Component = params.get("Component")
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
        """Template ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """Template name
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        """Template description
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def ParamList(self):
        """Parameter list
        :rtype: list of ModifyParamItem
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        """Database proxy group ID
        :rtype: str
        """
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def Description(self):
        """Database proxy description
        :rtype: str
        """
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
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        """Database proxy group ID
        :rtype: str
        """
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ConsistencyType(self):
        """Consistency type. Valid values: `eventual` (eventual consistency), `session` (session consistency), `global` (global consistency).
        :rtype: str
        """
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def ConsistencyTimeOut(self):
        """Consistency timeout period
        :rtype: str
        """
        return self._ConsistencyTimeOut

    @ConsistencyTimeOut.setter
    def ConsistencyTimeOut(self, ConsistencyTimeOut):
        self._ConsistencyTimeOut = ConsistencyTimeOut

    @property
    def WeightMode(self):
        """Assignment mode of read/write weights. Valid values: `system` (auto-assigned), `custom`
        :rtype: str
        """
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def InstanceWeights(self):
        """Read-Only weight of an instance
        :rtype: list of ProxyInstanceWeight
        """
        return self._InstanceWeights

    @InstanceWeights.setter
    def InstanceWeights(self, InstanceWeights):
        self._InstanceWeights = InstanceWeights

    @property
    def FailOver(self):
        """Whether to enable failover. If it is enabled, the connection address will route requests to the source instance in case of proxy failure. Valid values: `true`, `false`.
        :rtype: str
        """
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        """Whether to automatically add read-only instances. Valid values: `true`, `false`
        :rtype: str
        """
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def OpenRw(self):
        """Whether to enable read/write separation
        :rtype: str
        """
        return self._OpenRw

    @OpenRw.setter
    def OpenRw(self, OpenRw):
        self._OpenRw = OpenRw

    @property
    def RwType(self):
        """Read/Write type. Valid values:
`READWRITE`, `READONLY`.
        :rtype: str
        """
        return self._RwType

    @RwType.setter
    def RwType(self, RwType):
        self._RwType = RwType

    @property
    def TransSplit(self):
        """Transaction split
        :rtype: bool
        """
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def AccessMode(self):
        """Connection mode. Valid values:
`nearby`, `balance`.
        :rtype: str
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def OpenConnectionPool(self):
        """Whether to enable the connection pool. Valid values: 
`yes`, `no`.
        :rtype: str
        """
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolType(self):
        """Connection pool type. Valid values:
`ConnectionPoolType`, `SessionConnectionPool`.
        :rtype: str
        """
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def ConnectionPoolTimeOut(self):
        """Connection persistence timeout
        :rtype: int
        """
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
        """Async FlowId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        """Async task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """The unique ID of a resource pack
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def BindClusterIds(self):
        """ID of the cluster to be bound
        :rtype: list of str
        """
        return self._BindClusterIds

    @BindClusterIds.setter
    def BindClusterIds(self, BindClusterIds):
        self._BindClusterIds = BindClusterIds

    @property
    def UnbindClusterIds(self):
        """ID of the cluster to be unbound
        :rtype: list of str
        """
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
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """The unique ID of a resource pack
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        """Custom resource pack name, which can contains up to 120 characters.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyResourcePackagesDeductionPriorityRequest(AbstractModel):
    """ModifyResourcePackagesDeductionPriority request structure.

    """

    def __init__(self):
        r"""
        :param _PackageType: Specifies the resource package type whose priority needs to be modified. CCU: compute resource package. DISK: storage resource package.
        :type PackageType: str
        :param _ClusterId: The modified deduction priority takes effect for which cynos resource.
        :type ClusterId: str
        :param _DeductionPriorities: Resource package deduction priority.
        :type DeductionPriorities: list of PackagePriority
        """
        self._PackageType = None
        self._ClusterId = None
        self._DeductionPriorities = None

    @property
    def PackageType(self):
        """Specifies the resource package type whose priority needs to be modified. CCU: compute resource package. DISK: storage resource package.
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ClusterId(self):
        """The modified deduction priority takes effect for which cynos resource.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DeductionPriorities(self):
        """Resource package deduction priority.
        :rtype: list of PackagePriority
        """
        return self._DeductionPriorities

    @DeductionPriorities.setter
    def DeductionPriorities(self, DeductionPriorities):
        self._DeductionPriorities = DeductionPriorities


    def _deserialize(self, params):
        self._PackageType = params.get("PackageType")
        self._ClusterId = params.get("ClusterId")
        if params.get("DeductionPriorities") is not None:
            self._DeductionPriorities = []
            for item in params.get("DeductionPriorities"):
                obj = PackagePriority()
                obj._deserialize(item)
                self._DeductionPriorities.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcePackagesDeductionPriorityResponse(AbstractModel):
    """ModifyResourcePackagesDeductionPriority response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyServerlessStrategyRequest(AbstractModel):
    """ModifyServerlessStrategy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Specifies the serverless cluster id.
        :type ClusterId: str
        :param _AutoPause: Specifies whether the cluster automatically pauses. valid values for the optional range.
<li>yes</li>
<li>no</li>
        :type AutoPause: str
        :param _AutoPauseDelay: Specifies the delay for cluster auto-pause in seconds. the value range is [600,691200]. the default value is 600.
        :type AutoPauseDelay: int
        :param _AutoScaleUpDelay: The parameter is temporarily unavailable.
        :type AutoScaleUpDelay: int
        :param _AutoScaleDownDelay: The parameter is temporarily unavailable.
        :type AutoScaleDownDelay: int
        :param _MinCpu: Minimum value of cpu. for the optional range, refer to the API response of DescribeServerlessInstanceSpecs.
        :type MinCpu: float
        :param _MaxCpu: Maximum value of cpu, optional range refers to the API response of DescribeServerlessInstanceSpecs.
        :type MaxCpu: float
        :param _MinRoCpu: Minimum cpu value of a read-only instance. for valid values, refer to the API response of DescribeServerlessInstanceSpecs.
        :type MinRoCpu: float
        :param _MaxRoCpu: Maximum value of read-only cpu, optional range refer to the API response of DescribeServerlessInstanceSpecs.
        :type MaxRoCpu: float
        :param _MinRoCount: Specifies the minimum count of read-only nodes.
        :type MinRoCount: int
        :param _MaxRoCount: Maximum number of read-only nodes.
        :type MaxRoCount: int
        """
        self._ClusterId = None
        self._AutoPause = None
        self._AutoPauseDelay = None
        self._AutoScaleUpDelay = None
        self._AutoScaleDownDelay = None
        self._MinCpu = None
        self._MaxCpu = None
        self._MinRoCpu = None
        self._MaxRoCpu = None
        self._MinRoCount = None
        self._MaxRoCount = None

    @property
    def ClusterId(self):
        """Specifies the serverless cluster id.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AutoPause(self):
        """Specifies whether the cluster automatically pauses. valid values for the optional range.
<li>yes</li>
<li>no</li>
        :rtype: str
        """
        return self._AutoPause

    @AutoPause.setter
    def AutoPause(self, AutoPause):
        self._AutoPause = AutoPause

    @property
    def AutoPauseDelay(self):
        """Specifies the delay for cluster auto-pause in seconds. the value range is [600,691200]. the default value is 600.
        :rtype: int
        """
        return self._AutoPauseDelay

    @AutoPauseDelay.setter
    def AutoPauseDelay(self, AutoPauseDelay):
        self._AutoPauseDelay = AutoPauseDelay

    @property
    def AutoScaleUpDelay(self):
        """The parameter is temporarily unavailable.
        :rtype: int
        """
        return self._AutoScaleUpDelay

    @AutoScaleUpDelay.setter
    def AutoScaleUpDelay(self, AutoScaleUpDelay):
        self._AutoScaleUpDelay = AutoScaleUpDelay

    @property
    def AutoScaleDownDelay(self):
        """The parameter is temporarily unavailable.
        :rtype: int
        """
        return self._AutoScaleDownDelay

    @AutoScaleDownDelay.setter
    def AutoScaleDownDelay(self, AutoScaleDownDelay):
        self._AutoScaleDownDelay = AutoScaleDownDelay

    @property
    def MinCpu(self):
        """Minimum value of cpu. for the optional range, refer to the API response of DescribeServerlessInstanceSpecs.
        :rtype: float
        """
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        """Maximum value of cpu, optional range refers to the API response of DescribeServerlessInstanceSpecs.
        :rtype: float
        """
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def MinRoCpu(self):
        """Minimum cpu value of a read-only instance. for valid values, refer to the API response of DescribeServerlessInstanceSpecs.
        :rtype: float
        """
        return self._MinRoCpu

    @MinRoCpu.setter
    def MinRoCpu(self, MinRoCpu):
        self._MinRoCpu = MinRoCpu

    @property
    def MaxRoCpu(self):
        """Maximum value of read-only cpu, optional range refer to the API response of DescribeServerlessInstanceSpecs.
        :rtype: float
        """
        return self._MaxRoCpu

    @MaxRoCpu.setter
    def MaxRoCpu(self, MaxRoCpu):
        self._MaxRoCpu = MaxRoCpu

    @property
    def MinRoCount(self):
        """Specifies the minimum count of read-only nodes.
        :rtype: int
        """
        return self._MinRoCount

    @MinRoCount.setter
    def MinRoCount(self, MinRoCount):
        self._MinRoCount = MinRoCount

    @property
    def MaxRoCount(self):
        """Maximum number of read-only nodes.
        :rtype: int
        """
        return self._MaxRoCount

    @MaxRoCount.setter
    def MaxRoCount(self, MaxRoCount):
        self._MaxRoCount = MaxRoCount


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AutoPause = params.get("AutoPause")
        self._AutoPauseDelay = params.get("AutoPauseDelay")
        self._AutoScaleUpDelay = params.get("AutoScaleUpDelay")
        self._AutoScaleDownDelay = params.get("AutoScaleDownDelay")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._MinRoCpu = params.get("MinRoCpu")
        self._MaxRoCpu = params.get("MaxRoCpu")
        self._MinRoCount = params.get("MinRoCount")
        self._MaxRoCount = params.get("MaxRoCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServerlessStrategyResponse(AbstractModel):
    """ModifyServerlessStrategy response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async process id.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async process id.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceGrpId(self):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        """Instance group ID
        :rtype: str
        """
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        self._InstanceGrpId = InstanceGrpId

    @property
    def Vip(self):
        """Target IP to be modified
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Target port to be modified
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def DbType(self):
        """Database type. Valid values: 
<li> MYSQL </li>
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def OldIpReserveHours(self):
        """Valid hours of old IPs. If it is set to `0` hours, the IPs will be released immediately.
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Whether it is supported. Valid values: `yes`, `no`.
        :rtype: str
        """
        return self._IsDisable

    @IsDisable.setter
    def IsDisable(self, IsDisable):
        self._IsDisable = IsDisable

    @property
    def ModuleName(self):
        """Module name
        :rtype: str
        """
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
        :param _Vip: Private IP address
        :type Vip: str
        :param _Vport: Specifies the private network port number.
        :type Vport: int
        :param _WanDomain: Specifies the public network domain name.
        :type WanDomain: str
        :param _WanPort: Specifies the public network port number.
        :type WanPort: int
        :param _NetType: Network type (ro - read-only, rw/ha - read-write).
        :type NetType: str
        :param _UniqSubnetId: Specifies the subnet ID.
        :type UniqSubnetId: str
        :param _UniqVpcId: Specifies the virtual private cloud ID.
        :type UniqVpcId: str
        :param _Description: Description information
        :type Description: str
        :param _WanIP: Public IP address
        :type WanIP: str
        :param _WanStatus: Specifies the public network status.
        :type WanStatus: str
        :param _InstanceGroupId: Instance group ID
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
        """Private IP address
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Specifies the private network port number.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def WanDomain(self):
        """Specifies the public network domain name.
        :rtype: str
        """
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanPort(self):
        """Specifies the public network port number.
        :rtype: int
        """
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def NetType(self):
        """Network type (ro - read-only, rw/ha - read-write).
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def UniqSubnetId(self):
        """Specifies the subnet ID.
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def UniqVpcId(self):
        """Specifies the virtual private cloud ID.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Description(self):
        """Description information
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WanIP(self):
        """Public IP address
        :rtype: str
        """
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanStatus(self):
        """Specifies the public network status.
        :rtype: str
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def InstanceGroupId(self):
        """Instance group ID
        :rtype: str
        """
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
        """Account name, which can contain 1-16 letters, digits, and underscores. It must begin with a letter and end with a letter or digit.
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        """Password, which can contain 8-64 characters.
        :rtype: str
        """
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def Host(self):
        """Host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MaxUserConnections(self):
        """Maximum number of user connections, which cannot be above 10,240.
        :rtype: int
        """
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
        :param _TaskId: Task auto-increment ID.
        :type TaskId: int
        :param _TaskType: Task type
        :type TaskType: str
        :param _TaskStatus: Status of tasks.
        :type TaskStatus: str
        :param _ObjectId: Task ID (cluster ID | instance group ID | instance ID).
        :type ObjectId: str
        :param _ObjectType: Task type
        :type ObjectType: str
        """
        self._TaskId = None
        self._TaskType = None
        self._TaskStatus = None
        self._ObjectId = None
        self._ObjectType = None

    @property
    def TaskId(self):
        """Task auto-increment ID.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        """Task type
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskStatus(self):
        """Status of tasks.
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ObjectId(self):
        """Task ID (cluster ID | instance group ID | instance ID).
        :rtype: str
        """
        return self._ObjectId

    @ObjectId.setter
    def ObjectId(self, ObjectId):
        self._ObjectId = ObjectId

    @property
    def ObjectType(self):
        """Task type
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdList(self):
        """Instance ID array
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :type Vip: str
        :param _Vport: Port
        :type Vport: int
        :param _ReturnTime: Expect recycle time.
        :type ReturnTime: str
        """
        self._Vip = None
        self._Vport = None
        self._ReturnTime = None

    @property
    def Vip(self):
        """IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Port
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def ReturnTime(self):
        """Expect recycle time.
        :rtype: str
        """
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        """Log retention period
        :rtype: int
        """
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HighLogExpireDay(self):
        """Frequent log retention period
        :rtype: int
        """
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay

    @property
    def AuditRuleFilters(self):
        warnings.warn("parameter `AuditRuleFilters` is deprecated", DeprecationWarning) 

        """Audit rule. If both this parameter and `RuleTemplateIds` are left empty, full audit will be applied.
        :rtype: list of AuditRuleFilters
        """
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        warnings.warn("parameter `AuditRuleFilters` is deprecated", DeprecationWarning) 

        self._AuditRuleFilters = AuditRuleFilters

    @property
    def RuleTemplateIds(self):
        """Rule template ID. If both this parameter and `AuditRuleFilters` are left empty, full audit will be applied.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ValidatePasswordLength(self):
        """Password length
        :rtype: int
        """
        return self._ValidatePasswordLength

    @ValidatePasswordLength.setter
    def ValidatePasswordLength(self, ValidatePasswordLength):
        self._ValidatePasswordLength = ValidatePasswordLength

    @property
    def ValidatePasswordMixedCaseCount(self):
        """Number of letters
        :rtype: int
        """
        return self._ValidatePasswordMixedCaseCount

    @ValidatePasswordMixedCaseCount.setter
    def ValidatePasswordMixedCaseCount(self, ValidatePasswordMixedCaseCount):
        self._ValidatePasswordMixedCaseCount = ValidatePasswordMixedCaseCount

    @property
    def ValidatePasswordSpecialCharCount(self):
        """Number of symbols
        :rtype: int
        """
        return self._ValidatePasswordSpecialCharCount

    @ValidatePasswordSpecialCharCount.setter
    def ValidatePasswordSpecialCharCount(self, ValidatePasswordSpecialCharCount):
        self._ValidatePasswordSpecialCharCount = ValidatePasswordSpecialCharCount

    @property
    def ValidatePasswordNumberCount(self):
        """Number of digits
        :rtype: int
        """
        return self._ValidatePasswordNumberCount

    @ValidatePasswordNumberCount.setter
    def ValidatePasswordNumberCount(self, ValidatePasswordNumberCount):
        self._ValidatePasswordNumberCount = ValidatePasswordNumberCount

    @property
    def ValidatePasswordPolicy(self):
        """Password strength. Valid values: `MEDIUM`, `STRONG`.
        :rtype: str
        """
        return self._ValidatePasswordPolicy

    @ValidatePasswordPolicy.setter
    def ValidatePasswordPolicy(self, ValidatePasswordPolicy):
        self._ValidatePasswordPolicy = ValidatePasswordPolicy

    @property
    def ValidatePasswordDictionary(self):
        """Data dictionary
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Port: Port
        :type Port: str
        :param _SecurityGroupIds: Security group ID.
        :type SecurityGroupIds: list of str
        """
        self._ClusterId = None
        self._Port = None
        self._SecurityGroupIds = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Port(self):
        """Port
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SecurityGroupIds(self):
        """Security group ID.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Port = params.get("Port")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenClusterReadOnlyInstanceGroupAccessResponse(AbstractModel):
    """OpenClusterReadOnlyInstanceGroupAccess response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Initiate process ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Initiate process ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OpenClusterTransparentEncryptRequest(AbstractModel):
    """OpenClusterTransparentEncrypt request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _KeyType: Key type (cloud, custom).
        :type KeyType: str
        :param _KeyId: Key Id.
        :type KeyId: str
        :param _KeyRegion: Key region.
        :type KeyRegion: str
        """
        self._ClusterId = None
        self._KeyType = None
        self._KeyId = None
        self._KeyRegion = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def KeyType(self):
        """Key type (cloud, custom).
        :rtype: str
        """
        return self._KeyType

    @KeyType.setter
    def KeyType(self, KeyType):
        self._KeyType = KeyType

    @property
    def KeyId(self):
        """Key Id.
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyRegion(self):
        """Key region.
        :rtype: str
        """
        return self._KeyRegion

    @KeyRegion.setter
    def KeyRegion(self, KeyRegion):
        self._KeyRegion = KeyRegion


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._KeyType = params.get("KeyType")
        self._KeyId = params.get("KeyId")
        self._KeyRegion = params.get("KeyRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenClusterTransparentEncryptResponse(AbstractModel):
    """OpenClusterTransparentEncrypt response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Asynchronous task ID.


        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Asynchronous task ID.


        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class OpenReadOnlyInstanceExclusiveAccessRequest(AbstractModel):
    """OpenReadOnlyInstanceExclusiveAccess request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Please use the cluster information description (https://intl.cloud.tencent.com/document/api/1003/48086?from_cn_redirect=1) to obtain the clusterId.
        :type ClusterId: str
        :param _InstanceId: Please use the cluster information description (https://intl.cloud.tencent.com/document/api/1003/48086?from_cn_redirect=1) to obtain the instanceId.
        :type InstanceId: str
        :param _VpcId: Specifies the designated vpc ID. please use the "query vpc list" to obtain the vpc ID.
        :type VpcId: str
        :param _SubnetId: Specified subnet ID. if vpc ID is set, SubnetId is required. please use query subnet list (https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) to get SubnetId.
        :type SubnetId: str
        :param _Port: User-Defined port.
        :type Port: int
        :param _SecurityGroupIds: Security group ID. use [view security group](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) to obtain the SecurityGroupId.
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
        """Please use the cluster information description (https://intl.cloud.tencent.com/document/api/1003/48086?from_cn_redirect=1) to obtain the clusterId.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceId(self):
        """Please use the cluster information description (https://intl.cloud.tencent.com/document/api/1003/48086?from_cn_redirect=1) to obtain the instanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcId(self):
        """Specifies the designated vpc ID. please use the "query vpc list" to obtain the vpc ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Specified subnet ID. if vpc ID is set, SubnetId is required. please use query subnet list (https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) to get SubnetId.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Port(self):
        """User-Defined port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SecurityGroupIds(self):
        """Security group ID. use [view security group](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) to obtain the SecurityGroupId.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Activation process ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        """Instance group ID
        :rtype: str
        """
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Task flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _AppId: AppID
        :type AppId: int
        :param _PackageId: The unique ID of the resource package.
        :type PackageId: str
        :param _PackageName: Resource package name.
        :type PackageName: str
        :param _PackageType: Specifies the resource package type.
CCU: compute resource package. DISK: storage resource package.
        :type PackageType: str
        :param _PackageRegion: Resource package region of use.
China - common in the chinese mainland. overseas - universally applicable in hong kong (china), macao (china), taiwan (china), and overseas.
        :type PackageRegion: str
        :param _Status: Specifies the status of the resource package.
creating - indicates that it is in the process of being created.
{using} specifies that it is in use.
expired-expired;.
normal_finish - specifies that it is used up.
`Apply_refund`: apply for a refund.
Specifies that the fee has been refunded.
        :type Status: str
        :param _PackageTotalSpec: Total resource package quantity.
        :type PackageTotalSpec: float
        :param _PackageUsedSpec: Used amount of resource package.
        :type PackageUsedSpec: float
        :param _HasQuota: Whether there is inventory surplus.
        :type HasQuota: bool
        :param _BindInstanceInfos: Specifies the bound instance information.
        :type BindInstanceInfos: list of BindInstanceInfo
        :param _StartTime: Specifies the effective time: 2022-07-01 00:00:00.
        :type StartTime: str
        :param _ExpireTime: Specifies the expiration time: 2022-08-01 00:00:00.
        :type ExpireTime: str
        :param _HistoryBindResourceInfos: Information of the instance historically bound (now unbound) to the resource pack.
        :type HistoryBindResourceInfos: list of BindInstanceInfo
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
        self._HistoryBindResourceInfos = None

    @property
    def AppId(self):
        """AppID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PackageId(self):
        """The unique ID of the resource package.
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        """Resource package name.
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageType(self):
        """Specifies the resource package type.
CCU: compute resource package. DISK: storage resource package.
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageRegion(self):
        """Resource package region of use.
China - common in the chinese mainland. overseas - universally applicable in hong kong (china), macao (china), taiwan (china), and overseas.
        :rtype: str
        """
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def Status(self):
        """Specifies the status of the resource package.
creating - indicates that it is in the process of being created.
{using} specifies that it is in use.
expired-expired;.
normal_finish - specifies that it is used up.
`Apply_refund`: apply for a refund.
Specifies that the fee has been refunded.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PackageTotalSpec(self):
        """Total resource package quantity.
        :rtype: float
        """
        return self._PackageTotalSpec

    @PackageTotalSpec.setter
    def PackageTotalSpec(self, PackageTotalSpec):
        self._PackageTotalSpec = PackageTotalSpec

    @property
    def PackageUsedSpec(self):
        """Used amount of resource package.
        :rtype: float
        """
        return self._PackageUsedSpec

    @PackageUsedSpec.setter
    def PackageUsedSpec(self, PackageUsedSpec):
        self._PackageUsedSpec = PackageUsedSpec

    @property
    def HasQuota(self):
        """Whether there is inventory surplus.
        :rtype: bool
        """
        return self._HasQuota

    @HasQuota.setter
    def HasQuota(self, HasQuota):
        self._HasQuota = HasQuota

    @property
    def BindInstanceInfos(self):
        """Specifies the bound instance information.
        :rtype: list of BindInstanceInfo
        """
        return self._BindInstanceInfos

    @BindInstanceInfos.setter
    def BindInstanceInfos(self, BindInstanceInfos):
        self._BindInstanceInfos = BindInstanceInfos

    @property
    def StartTime(self):
        """Specifies the effective time: 2022-07-01 00:00:00.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        """Specifies the expiration time: 2022-08-01 00:00:00.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def HistoryBindResourceInfos(self):
        """Information of the instance historically bound (now unbound) to the resource pack.
        :rtype: list of BindInstanceInfo
        """
        return self._HistoryBindResourceInfos

    @HistoryBindResourceInfos.setter
    def HistoryBindResourceInfos(self, HistoryBindResourceInfos):
        self._HistoryBindResourceInfos = HistoryBindResourceInfos


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
        if params.get("HistoryBindResourceInfos") is not None:
            self._HistoryBindResourceInfos = []
            for item in params.get("HistoryBindResourceInfos"):
                obj = BindInstanceInfo()
                obj._deserialize(item)
                self._HistoryBindResourceInfos.append(obj)
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
        :param _AppId: AppId account ID.
        :type AppId: int
        :param _PackageId: The unique ID of the resource package.
        :type PackageId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SuccessDeductSpec: Successfully deduct capacity.
        :type SuccessDeductSpec: float
        :param _PackageTotalUsedSpec: The used capacity of the resource package up to the present.
        :type PackageTotalUsedSpec: float
        :param _StartTime: Deduction start time.
        :type StartTime: str
        :param _EndTime: Deduction end time.
        :type EndTime: str
        :param _ExtendInfo: Extension Information
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
        """AppId account ID.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PackageId(self):
        """The unique ID of the resource package.
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SuccessDeductSpec(self):
        """Successfully deduct capacity.
        :rtype: float
        """
        return self._SuccessDeductSpec

    @SuccessDeductSpec.setter
    def SuccessDeductSpec(self, SuccessDeductSpec):
        self._SuccessDeductSpec = SuccessDeductSpec

    @property
    def PackageTotalUsedSpec(self):
        """The used capacity of the resource package up to the present.
        :rtype: float
        """
        return self._PackageTotalUsedSpec

    @PackageTotalUsedSpec.setter
    def PackageTotalUsedSpec(self, PackageTotalUsedSpec):
        self._PackageTotalUsedSpec = PackageTotalUsedSpec

    @property
    def StartTime(self):
        """Deduction start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Deduction end time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExtendInfo(self):
        """Extension Information
        :rtype: str
        """
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
        


class PackagePriority(AbstractModel):
    """Resource package deduction priority.

    """

    def __init__(self):
        r"""
        :param _PackageId: The resource pack whose deduction priority needs to be customized.
        :type PackageId: str
        :param _DeductionPriority: Custom deduction priority.
        :type DeductionPriority: int
        """
        self._PackageId = None
        self._DeductionPriority = None

    @property
    def PackageId(self):
        """The resource pack whose deduction priority needs to be customized.
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def DeductionPriority(self):
        """Custom deduction priority.
        :rtype: int
        """
        return self._DeductionPriority

    @DeductionPriority.setter
    def DeductionPriority(self, DeductionPriority):
        self._DeductionPriority = DeductionPriority


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._DeductionPriority = params.get("DeductionPriority")
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
        :param _EnumValue: Optional enumerated values of the parameter. if it is a non-enumerated value, it is empty.
        :type EnumValue: list of str
        :param _IsGlobal: Valid values: `1` (global parameter),  `0`  (non-global parameter).
        :type IsGlobal: int
        :param _MatchType: The match type. Valid value: `multiVal`.
        :type MatchType: str
        :param _MatchValue: Match values, which will be separated by comma when `MatchType` is `multiVal`.
        :type MatchValue: str
        :param _IsFunc: true - indicates a formula. false - indicates it is not a formula.
        :type IsFunc: bool
        :param _Func: Specifies that when the parameter is set as a formula, Func returns the set formula content.
        :type Func: str
        :param _ModifiableInfo: Whether the parameter is modifiable.
        :type ModifiableInfo: :class:`tencentcloud.cynosdb.v20190107.models.ModifiableInfo`
        :param _FuncPattern: The default formula style of parameters that support formulas.
        :type FuncPattern: str
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
        self._FuncPattern = None

    @property
    def ParamName(self):
        """Parameter name
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamType(self):
        """Parameter type. Valid values:  `integer`, `enum`, `float`, `string`, `func`.
        :rtype: str
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def SupportFunc(self):
        """Whether `func` is supported. Valid values: `true` (supported), `false` (not supported).
        :rtype: bool
        """
        return self._SupportFunc

    @SupportFunc.setter
    def SupportFunc(self, SupportFunc):
        self._SupportFunc = SupportFunc

    @property
    def Default(self):
        """Default value
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        """Parameter description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        """Current value of the parameter
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        """Whether to restart the database for the modified parameters to take effect. Valid values:  `0` (no), `1` (yes).
        :rtype: int
        """
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        """Maximum value of the parameter
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        """Minimum value of the parameter
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        """Optional enumerated values of the parameter. if it is a non-enumerated value, it is empty.
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def IsGlobal(self):
        """Valid values: `1` (global parameter),  `0`  (non-global parameter).
        :rtype: int
        """
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def MatchType(self):
        """The match type. Valid value: `multiVal`.
        :rtype: str
        """
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def MatchValue(self):
        """Match values, which will be separated by comma when `MatchType` is `multiVal`.
        :rtype: str
        """
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def IsFunc(self):
        """true - indicates a formula. false - indicates it is not a formula.
        :rtype: bool
        """
        return self._IsFunc

    @IsFunc.setter
    def IsFunc(self, IsFunc):
        self._IsFunc = IsFunc

    @property
    def Func(self):
        """Specifies that when the parameter is set as a formula, Func returns the set formula content.
        :rtype: str
        """
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func

    @property
    def ModifiableInfo(self):
        """Whether the parameter is modifiable.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifiableInfo`
        """
        return self._ModifiableInfo

    @ModifiableInfo.setter
    def ModifiableInfo(self, ModifiableInfo):
        self._ModifiableInfo = ModifiableInfo

    @property
    def FuncPattern(self):
        """The default formula style of parameters that support formulas.
        :rtype: str
        """
        return self._FuncPattern

    @FuncPattern.setter
    def FuncPattern(self, FuncPattern):
        self._FuncPattern = FuncPattern


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
        self._FuncPattern = params.get("FuncPattern")
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
        :param _EnumValue: If the parameter is of type enum/string/bool, the available options list.
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
        :param _IsGlobal: Whether it is a global parameter.
        :type IsGlobal: int
        :param _ModifiableInfo: Whether the parameter is modifiable.
        :type ModifiableInfo: :class:`tencentcloud.cynosdb.v20190107.models.ModifiableInfo`
        :param _IsFunc: Whether it is a function.
        :type IsFunc: bool
        :param _Func: Function.
        :type Func: str
        :param _FuncPattern: The default formula style of parameters that support formulas.
        :type FuncPattern: str
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
        self._FuncPattern = None

    @property
    def CurrentValue(self):
        """Current value
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Default(self):
        """Default value
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def EnumValue(self):
        """If the parameter is of type enum/string/bool, the available options list.
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Max(self):
        """Maximum value when parameter type is `float` or `integer`.
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        """Minimum value when parameter type is `float` or `integer`.
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ParamName(self):
        """Parameter name
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def NeedReboot(self):
        """Whether to restart the instance for the modified parameters to take effect.
        :rtype: int
        """
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def ParamType(self):
        """Parameter type: `integer`, `float`, `string`, `enum`, `bool`.
        :rtype: str
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def MatchType(self):
        """Match type. Regex can be used when parameter type is `string`. Valid value: `multiVal`.
        :rtype: str
        """
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def MatchValue(self):
        """Match values, which will be separated by semicolon when match type is `multiVal`.
        :rtype: str
        """
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def Description(self):
        """Parameter description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsGlobal(self):
        """Whether it is a global parameter.
        :rtype: int
        """
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def ModifiableInfo(self):
        """Whether the parameter is modifiable.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifiableInfo`
        """
        return self._ModifiableInfo

    @ModifiableInfo.setter
    def ModifiableInfo(self, ModifiableInfo):
        self._ModifiableInfo = ModifiableInfo

    @property
    def IsFunc(self):
        """Whether it is a function.
        :rtype: bool
        """
        return self._IsFunc

    @IsFunc.setter
    def IsFunc(self, IsFunc):
        self._IsFunc = IsFunc

    @property
    def Func(self):
        """Function.
        :rtype: str
        """
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func

    @property
    def FuncPattern(self):
        """The default formula style of parameters that support formulas.
        :rtype: str
        """
        return self._FuncPattern

    @FuncPattern.setter
    def FuncPattern(self, FuncPattern):
        self._FuncPattern = FuncPattern


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
        self._FuncPattern = params.get("FuncPattern")
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
        """Parameter name
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def CurrentValue(self):
        """New value
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def OldValue(self):
        """Original value
        :rtype: str
        """
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
        :param _IsFunc: Whether the type is a formula.
        :type IsFunc: bool
        :param _Func: Parameter configuration formula.
        :type Func: str
        :param _FuncPattern: The default formula style of parameters that support formulas.
        :type FuncPattern: str
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
        self._FuncPattern = None

    @property
    def CurrentValue(self):
        """Current value
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Default(self):
        """Default value
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def EnumValue(self):
        """Enumerated values of the parameter It is null if the parameter is non-enumerated.
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def IsGlobal(self):
        """Valid values: `1` (global parameter),  `0`  (non-global parameter).
        :rtype: int
        """
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def Max(self):
        """Maximum value
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        """Minimum value
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def NeedReboot(self):
        """Whether to restart the database for the modified parameters to take effect. Valid values:  `0` (no), `1` (yes)
        :rtype: int
        """
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def ParamName(self):
        """Parameter name
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamType(self):
        """Parameter type. Valid values:  `integer`, `enum`, `float`, `string`, `func`.
        :rtype: str
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Description(self):
        """Parameter description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsFunc(self):
        """Whether the type is a formula.
        :rtype: bool
        """
        return self._IsFunc

    @IsFunc.setter
    def IsFunc(self, IsFunc):
        self._IsFunc = IsFunc

    @property
    def Func(self):
        """Parameter configuration formula.
        :rtype: str
        """
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func

    @property
    def FuncPattern(self):
        """The default formula style of parameters that support formulas.
        :rtype: str
        """
        return self._FuncPattern

    @FuncPattern.setter
    def FuncPattern(self, FuncPattern):
        self._FuncPattern = FuncPattern


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
        self._FuncPattern = params.get("FuncPattern")
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
        """Parameter template ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TemplateName(self):
        """Parameter template name
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        """Parameter template description
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def EngineVersion(self):
        """Engine version
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def DbMode(self):
        """Database Type. Valid values: `NORMAL`, `SERVERLESS`.
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def ParamInfoSet(self):
        """Parameter template details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TemplateParamInfo
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ForcePause(self):
        """Whether to pause forcibly and ignore the current user connections. Valid values: `0` (no), `1` (yes). Default value: `1`
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Policy, which can be `ACCEPT` or `DROP`
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        """Source IP or source IP range, such as 192.168.0.0/16
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        """Port
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        """Network protocol, such as UDP and TCP
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def ServiceModule(self):
        """Protocol port ID or protocol port group ID.
        :rtype: str
        """
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def AddressModule(self):
        """IP address ID or IP address group ID.
        :rtype: str
        """
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def Id(self):
        """id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Desc(self):
        """Description
        :rtype: str
        """
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
        :param _ConnectionPoolTimeOut: Specifies the persistence threshold of the connection pool. the unit is seconds.
        :type ConnectionPoolTimeOut: int
        :param _OpenConnectionPool: Whether the connection pool is enabled.
        :type OpenConnectionPool: str
        :param _ConnectionPoolType: Specifies the connection pool type. valid values: SessionConnectionPool (session-level connection pool).
        :type ConnectionPoolType: str
        """
        self._ConnectionPoolTimeOut = None
        self._OpenConnectionPool = None
        self._ConnectionPoolType = None

    @property
    def ConnectionPoolTimeOut(self):
        """Specifies the persistence threshold of the connection pool. the unit is seconds.
        :rtype: int
        """
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut

    @property
    def OpenConnectionPool(self):
        """Whether the connection pool is enabled.
        :rtype: str
        """
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolType(self):
        """Specifies the connection pool type. valid values: SessionConnectionPool (session-level connection pool).
        :rtype: str
        """
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
        :type ClusterId: str
        :param _AppId: User AppId
        :type AppId: int
        :param _OpenRw: Specifies that a read-write node activates the database proxy.
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
        """Database proxy group ID
        :rtype: str
        """
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyNodeCount(self):
        """Number of nodes in the proxy group
        :rtype: int
        """
        return self._ProxyNodeCount

    @ProxyNodeCount.setter
    def ProxyNodeCount(self, ProxyNodeCount):
        self._ProxyNodeCount = ProxyNodeCount

    @property
    def Status(self):
        """Database proxy group status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CurrentProxyVersion(self):
        """Current proxy version
        :rtype: str
        """
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AppId(self):
        """User AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OpenRw(self):
        """Specifies that a read-write node activates the database proxy.
        :rtype: str
        """
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
        :param _ProxyGroup: Database proxy group.
        :type ProxyGroup: :class:`tencentcloud.cynosdb.v20190107.models.ProxyGroup`
        :param _ProxyGroupRwInfo: Database proxy group read-write separation information.
        :type ProxyGroupRwInfo: :class:`tencentcloud.cynosdb.v20190107.models.ProxyGroupRwInfo`
        :param _ProxyNodes: Node information of the database proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyNodes: list of ProxyNodeInfo
        :param _ConnectionPool: Database proxy connection pool information.
        :type ConnectionPool: :class:`tencentcloud.cynosdb.v20190107.models.ProxyConnectionPoolInfo`
        :param _NetAddrInfos: Network information for database proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetAddrInfos: list of NetAddr
        :param _Tasks: Database proxy task set.
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
        """Database proxy group.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ProxyGroup`
        """
        return self._ProxyGroup

    @ProxyGroup.setter
    def ProxyGroup(self, ProxyGroup):
        self._ProxyGroup = ProxyGroup

    @property
    def ProxyGroupRwInfo(self):
        """Database proxy group read-write separation information.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ProxyGroupRwInfo`
        """
        return self._ProxyGroupRwInfo

    @ProxyGroupRwInfo.setter
    def ProxyGroupRwInfo(self, ProxyGroupRwInfo):
        self._ProxyGroupRwInfo = ProxyGroupRwInfo

    @property
    def ProxyNodes(self):
        """Node information of the database proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ProxyNodeInfo
        """
        return self._ProxyNodes

    @ProxyNodes.setter
    def ProxyNodes(self, ProxyNodes):
        self._ProxyNodes = ProxyNodes

    @property
    def ConnectionPool(self):
        """Database proxy connection pool information.
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ProxyConnectionPoolInfo`
        """
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def NetAddrInfos(self):
        """Network information for database proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of NetAddr
        """
        return self._NetAddrInfos

    @NetAddrInfos.setter
    def NetAddrInfos(self, NetAddrInfos):
        self._NetAddrInfos = NetAddrInfos

    @property
    def Tasks(self):
        """Database proxy task set.
        :rtype: list of ObjectTask
        """
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
        :param _OpenRw: Whether to enable read-write nodes. valid values: yes, no.
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
        """Consistency type. Valid values: `eventual` (eventual consistency), `session` (session consistency), `global` (global consistency).
        :rtype: str
        """
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def ConsistencyTimeOut(self):
        """Consistency timeout period
        :rtype: int
        """
        return self._ConsistencyTimeOut

    @ConsistencyTimeOut.setter
    def ConsistencyTimeOut(self, ConsistencyTimeOut):
        self._ConsistencyTimeOut = ConsistencyTimeOut

    @property
    def WeightMode(self):
        """Weight mode. Valid values: `system` (auto-assigned), `custom`.
        :rtype: str
        """
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def FailOver(self):
        """Whether to enable failover
        :rtype: str
        """
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        """Whether to automatically add read-only instance. Valid value: `yes`, `no`.
        :rtype: str
        """
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def InstanceWeights(self):
        """Instance weight array
        :rtype: list of ProxyInstanceWeight
        """
        return self._InstanceWeights

    @InstanceWeights.setter
    def InstanceWeights(self, InstanceWeights):
        self._InstanceWeights = InstanceWeights

    @property
    def OpenRw(self):
        """Whether to enable read-write nodes. valid values: yes, no.
        :rtype: str
        """
        return self._OpenRw

    @OpenRw.setter
    def OpenRw(self, OpenRw):
        self._OpenRw = OpenRw

    @property
    def RwType(self):
        """Read/write attribute. Valid values: `READWRITE`, `READONLY`.
        :rtype: str
        """
        return self._RwType

    @RwType.setter
    def RwType(self, RwType):
        self._RwType = RwType

    @property
    def TransSplit(self):
        """Transaction split
        :rtype: bool
        """
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def AccessMode(self):
        """Connection mode. Valid values: `balance`, `nearby`.
        :rtype: str
        """
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
        """InstanID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        """Instance weight
        :rtype: int
        """
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
        :param _OssProxyNodeName: 
        :type OssProxyNodeName: str
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
        self._OssProxyNodeName = None

    @property
    def ProxyNodeId(self):
        """Database proxy node ID
        :rtype: str
        """
        return self._ProxyNodeId

    @ProxyNodeId.setter
    def ProxyNodeId(self, ProxyNodeId):
        self._ProxyNodeId = ProxyNodeId

    @property
    def ProxyNodeConnections(self):
        """Current node connections, which is not returned by the `DescribeProxyNodes` API.
        :rtype: int
        """
        return self._ProxyNodeConnections

    @ProxyNodeConnections.setter
    def ProxyNodeConnections(self, ProxyNodeConnections):
        self._ProxyNodeConnections = ProxyNodeConnections

    @property
    def Cpu(self):
        """CPU of the database proxy node
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        """Memory of the database proxy node
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Status(self):
        """Status of the database proxy node
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProxyGroupId(self):
        """Database proxy group ID
        :rtype: str
        """
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AppId(self):
        """User AppID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def OssProxyNodeName(self):
        """
        :rtype: str
        """
        return self._OssProxyNodeName

    @OssProxyNodeName.setter
    def OssProxyNodeName(self, OssProxyNodeName):
        self._OssProxyNodeName = OssProxyNodeName


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
        self._OssProxyNodeName = params.get("OssProxyNodeName")
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
        """Number of database proxy CPU cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        """Database proxy memory
        :rtype: int
        """
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
        


class ProxyVersionInfo(AbstractModel):
    """The proxy version information supported by TDSQL-C for MySQL.

    """

    def __init__(self):
        r"""
        :param _ProxyVersion: proxy version number.
        :type ProxyVersion: str
        :param _ProxyVersionType: Version description: GA: stable version. BETA: BETA version. DEPRECATED: outdated.
        :type ProxyVersionType: str
        """
        self._ProxyVersion = None
        self._ProxyVersionType = None

    @property
    def ProxyVersion(self):
        """proxy version number.
        :rtype: str
        """
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def ProxyVersionType(self):
        """Version description: GA: stable version. BETA: BETA version. DEPRECATED: outdated.
        :rtype: str
        """
        return self._ProxyVersionType

    @ProxyVersionType.setter
    def ProxyVersionType(self, ProxyVersionType):
        self._ProxyVersionType = ProxyVersionType


    def _deserialize(self, params):
        self._ProxyVersion = params.get("ProxyVersion")
        self._ProxyVersionType = params.get("ProxyVersionType")
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
        """AZ of the proxy node
        :rtype: str
        """
        return self._ProxyNodeZone

    @ProxyNodeZone.setter
    def ProxyNodeZone(self, ProxyNodeZone):
        self._ProxyNodeZone = ProxyNodeZone

    @property
    def ProxyNodeCount(self):
        """The number of proxy nodes
        :rtype: int
        """
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
        """Search field. Valid values: "InstanceId", "ProjectId", "InstanceName", "Vip"
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Values(self):
        """Search string
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        """Whether to use exact match
        :rtype: bool
        """
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch

    @property
    def Name(self):
        """Search field
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Operator(self):
        """Operator
        :rtype: str
        """
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
        """Search field. Valid values: "InstanceId", "ProjectId", "InstanceName", "Vip"
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Values(self):
        """Search string
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        """Whether to use exact match
        :rtype: bool
        """
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
        """The unique ID of a resource pack
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealNames = None
        self._RequestId = None

    @property
    def DealNames(self):
        """Each item has only one `dealName`, through which you can ensure the idempotency of the delivery API.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        """Database proxy group ID
        :rtype: str
        """
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
        """Async flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        """Async task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SlaveZone(self):
        """Replica AZ
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async FlowId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Database account name
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        """New password of the database account
        :rtype: str
        """
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Host(self):
        """Host. Default value: `%`
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _PackageId: The unique ID of the resource package.
        :type PackageId: str
        :param _PackageType: Resource package type: CCU: compute resource package.
DISK: storage resource package.
        :type PackageType: str
        :param _DeductionPriority: Deduction priority of the current resource package bound to the current instance.
        :type DeductionPriority: int
        """
        self._PackageId = None
        self._PackageType = None
        self._DeductionPriority = None

    @property
    def PackageId(self):
        """The unique ID of the resource package.
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageType(self):
        """Resource package type: CCU: compute resource package.
DISK: storage resource package.
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def DeductionPriority(self):
        """Deduction priority of the current resource package bound to the current instance.
        :rtype: int
        """
        return self._DeductionPriority

    @DeductionPriority.setter
    def DeductionPriority(self, DeductionPriority):
        self._DeductionPriority = DeductionPriority


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._PackageType = params.get("PackageType")
        self._DeductionPriority = params.get("DeductionPriority")
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
        """Instance ID
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
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance response structure.

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
        """Async task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Start time
        :rtype: str
        """
        return self._TimeRangeStart

    @TimeRangeStart.setter
    def TimeRangeStart(self, TimeRangeStart):
        self._TimeRangeStart = TimeRangeStart

    @property
    def TimeRangeEnd(self):
        """End time
        :rtype: str
        """
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
        """Filter parameter name of the audit rule. Valid values: `host` (client IP), `user` (database account), `dbName` (database name), `sqlType` (SQL type), `sql` (SQL statement).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        """Filter match type of the audit rule. Valid values: `INC` (including), `EXC` (excluding), `EQS` (equal to), `NEQ` (not equal to).
        :rtype: str
        """
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        """Filter match value of the audit rule
        :rtype: list of str
        """
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
        


class RuleTemplateInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _RuleTemplateId: Rule template ID.
        :type RuleTemplateId: str
        :param _RuleTemplateName: Rule template name.
        :type RuleTemplateName: str
        :param _RuleFilters: The rule content.
        :type RuleFilters: list of RuleFilters
        :param _AlarmLevel: Alarm level. valid values: 1 (low risk), 2 (medium risk), 3 (high risk).
        :type AlarmLevel: int
        :param _AlarmPolicy: Alarm policy. 0 - no alert, 1 - alert.
        :type AlarmPolicy: int
        :param _Description: Rule description.
        :type Description: str
        """
        self._RuleTemplateId = None
        self._RuleTemplateName = None
        self._RuleFilters = None
        self._AlarmLevel = None
        self._AlarmPolicy = None
        self._Description = None

    @property
    def RuleTemplateId(self):
        """Rule template ID.
        :rtype: str
        """
        return self._RuleTemplateId

    @RuleTemplateId.setter
    def RuleTemplateId(self, RuleTemplateId):
        self._RuleTemplateId = RuleTemplateId

    @property
    def RuleTemplateName(self):
        """Rule template name.
        :rtype: str
        """
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def RuleFilters(self):
        """The rule content.
        :rtype: list of RuleFilters
        """
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def AlarmLevel(self):
        """Alarm level. valid values: 1 (low risk), 2 (medium risk), 3 (high risk).
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmPolicy(self):
        """Alarm policy. 0 - no alert, 1 - alert.
        :rtype: int
        """
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy

    @property
    def Description(self):
        """Rule description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RuleTemplateId = params.get("RuleTemplateId")
        self._RuleTemplateName = params.get("RuleTemplateName")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmPolicy = params.get("AlarmPolicy")
        self._Description = params.get("Description")
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
        :param _PackageRegion: Resource package region of use.
        :type PackageRegion: str
        :param _PackageType: Specifies the resource package type.
CCU - compute resource package.
Storage resource package.
        :type PackageType: str
        :param _PackageVersion: Resource pack version.
base - basic version; common - general version; enterprise - enterprise edition.
        :type PackageVersion: str
        :param _MinPackageSpec: Minimum number of resources in the current version of the resource package. compute resource unit: pieces; storage resource: GB.
        :type MinPackageSpec: float
        :param _MaxPackageSpec: Specifies the maximum number of resources in the current version of the resource package. valid values: compute resource unit: pieces; storage resource: GB.
        :type MaxPackageSpec: float
        :param _ExpireDay: Specifies the resource pack validity period. the measurement unit is day.
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
        """Resource package region of use.
        :rtype: str
        """
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def PackageType(self):
        """Specifies the resource package type.
CCU - compute resource package.
Storage resource package.
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageVersion(self):
        """Resource pack version.
base - basic version; common - general version; enterprise - enterprise edition.
        :rtype: str
        """
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def MinPackageSpec(self):
        """Minimum number of resources in the current version of the resource package. compute resource unit: pieces; storage resource: GB.
        :rtype: float
        """
        return self._MinPackageSpec

    @MinPackageSpec.setter
    def MinPackageSpec(self, MinPackageSpec):
        self._MinPackageSpec = MinPackageSpec

    @property
    def MaxPackageSpec(self):
        """Specifies the maximum number of resources in the current version of the resource package. valid values: compute resource unit: pieces; storage resource: GB.
        :rtype: float
        """
        return self._MaxPackageSpec

    @MaxPackageSpec.setter
    def MaxPackageSpec(self, MaxPackageSpec):
        self._MaxPackageSpec = MaxPackageSpec

    @property
    def ExpireDay(self):
        """Specifies the resource pack validity period. the measurement unit is day.
        :rtype: int
        """
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
        """Region name
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        """Numeric ID of a region
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionZh(self):
        """Region name
        :rtype: str
        """
        return self._RegionZh

    @RegionZh.setter
    def RegionZh(self, RegionZh):
        self._RegionZh = RegionZh

    @property
    def ZoneSet(self):
        """List of purchasable AZs
        :rtype: list of SaleZone
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def DbType(self):
        """Engine type
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Modules(self):
        """Supported modules in a region
        :rtype: list of Module
        """
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
        :param _HasPermission: Whether the user has AZ permission.
        :type HasPermission: bool
        :param _IsWholeRdmaZone: Whether it is a full-linkage RDMA AZ.
        :type IsWholeRdmaZone: str
        :param _IsSupportCreateCluster: Specifies whether a newly purchased cluster is allowed in the current availability zone. valid values: 1 (allowed), 0 (not allowed).
        :type IsSupportCreateCluster: int
        """
        self._Zone = None
        self._ZoneId = None
        self._ZoneZh = None
        self._IsSupportServerless = None
        self._IsSupportNormal = None
        self._PhysicalZone = None
        self._HasPermission = None
        self._IsWholeRdmaZone = None
        self._IsSupportCreateCluster = None

    @property
    def Zone(self):
        """AZ name
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        """Numeric ID of an AZ
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneZh(self):
        """AZ name
        :rtype: str
        """
        return self._ZoneZh

    @ZoneZh.setter
    def ZoneZh(self, ZoneZh):
        self._ZoneZh = ZoneZh

    @property
    def IsSupportServerless(self):
        """Whether serverless cluster is supported. Valid values: <br>
`0`: No<br>
`1`: Yes
        :rtype: int
        """
        return self._IsSupportServerless

    @IsSupportServerless.setter
    def IsSupportServerless(self, IsSupportServerless):
        self._IsSupportServerless = IsSupportServerless

    @property
    def IsSupportNormal(self):
        """Whether standard cluster is supported. Valid values: <br>
`0`: No<br>
`1`: Yes
        :rtype: int
        """
        return self._IsSupportNormal

    @IsSupportNormal.setter
    def IsSupportNormal(self, IsSupportNormal):
        self._IsSupportNormal = IsSupportNormal

    @property
    def PhysicalZone(self):
        """Physical zone
        :rtype: str
        """
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def HasPermission(self):
        """Whether the user has AZ permission.
        :rtype: bool
        """
        return self._HasPermission

    @HasPermission.setter
    def HasPermission(self, HasPermission):
        self._HasPermission = HasPermission

    @property
    def IsWholeRdmaZone(self):
        """Whether it is a full-linkage RDMA AZ.
        :rtype: str
        """
        return self._IsWholeRdmaZone

    @IsWholeRdmaZone.setter
    def IsWholeRdmaZone(self, IsWholeRdmaZone):
        self._IsWholeRdmaZone = IsWholeRdmaZone

    @property
    def IsSupportCreateCluster(self):
        """Specifies whether a newly purchased cluster is allowed in the current availability zone. valid values: 1 (allowed), 0 (not allowed).
        :rtype: int
        """
        return self._IsSupportCreateCluster

    @IsSupportCreateCluster.setter
    def IsSupportCreateCluster(self, IsSupportCreateCluster):
        self._IsSupportCreateCluster = IsSupportCreateCluster


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneZh = params.get("ZoneZh")
        self._IsSupportServerless = params.get("IsSupportServerless")
        self._IsSupportNormal = params.get("IsSupportNormal")
        self._PhysicalZone = params.get("PhysicalZone")
        self._HasPermission = params.get("HasPermission")
        self._IsWholeRdmaZone = params.get("IsWholeRdmaZone")
        self._IsSupportCreateCluster = params.get("IsSupportCreateCluster")
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
        """The cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def MatchType(self):
        """Whether to search exactly
Valid values: `0` (fuzzy search), `1` (exact search). 
Default value: `0`.
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Databases = None
        self._RequestId = None

    @property
    def Databases(self):
        """Database List
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """Data table name
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def TableType(self):
        """Data table type. Valid values:
`view`: Only return to view,
`base_table`: Only return to basic table,
`all`: Return to view and table.
        :rtype: str
        """
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
        :param _Tables: Data table list.
        :type Tables: list of DatabaseTables
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tables = None
        self._RequestId = None

    @property
    def Tables(self):
        """Data table list.
        :rtype: list of DatabaseTables
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        """Creation time in the format of yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Inbound(self):
        """Inbound rule
        :rtype: list of PolicyRule
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        """Outbound rule
        :rtype: list of PolicyRule
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def SecurityGroupId(self):
        """Security group ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        """Security group name
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        """Security group remarks
        :rtype: str
        """
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
        


class ServerlessSpec(AbstractModel):
    """serverless specification.

    """

    def __init__(self):
        r"""
        :param _MinCpu: Specifies the minimum value of the cpu.
        :type MinCpu: float
        :param _MaxCpu: Maximum value of cpu.
        :type MaxCpu: float
        :param _MaxStorageSize: Maximum storage space.
        :type MaxStorageSize: int
        :param _IsDefault: Specifies whether it is the default specification.
        :type IsDefault: int
        :param _HasStock: Whether there is inventory.
        :type HasStock: bool
        :param _StockCount: Inventory quantity.
        :type StockCount: int
        :param _ZoneStockInfos: Availability zone inventory information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneStockInfos: list of ServerlessZoneStockInfo
        """
        self._MinCpu = None
        self._MaxCpu = None
        self._MaxStorageSize = None
        self._IsDefault = None
        self._HasStock = None
        self._StockCount = None
        self._ZoneStockInfos = None

    @property
    def MinCpu(self):
        """Specifies the minimum value of the cpu.
        :rtype: float
        """
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        """Maximum value of cpu.
        :rtype: float
        """
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def MaxStorageSize(self):
        """Maximum storage space.
        :rtype: int
        """
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def IsDefault(self):
        """Specifies whether it is the default specification.
        :rtype: int
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def HasStock(self):
        """Whether there is inventory.
        :rtype: bool
        """
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock

    @property
    def StockCount(self):
        """Inventory quantity.
        :rtype: int
        """
        return self._StockCount

    @StockCount.setter
    def StockCount(self, StockCount):
        self._StockCount = StockCount

    @property
    def ZoneStockInfos(self):
        """Availability zone inventory information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ServerlessZoneStockInfo
        """
        return self._ZoneStockInfos

    @ZoneStockInfos.setter
    def ZoneStockInfos(self, ZoneStockInfos):
        self._ZoneStockInfos = ZoneStockInfos


    def _deserialize(self, params):
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._MaxStorageSize = params.get("MaxStorageSize")
        self._IsDefault = params.get("IsDefault")
        self._HasStock = params.get("HasStock")
        self._StockCount = params.get("StockCount")
        if params.get("ZoneStockInfos") is not None:
            self._ZoneStockInfos = []
            for item in params.get("ZoneStockInfos"):
                obj = ServerlessZoneStockInfo()
                obj._deserialize(item)
                self._ZoneStockInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessZoneStockInfo(AbstractModel):
    """serverless type availability zone inventory information.

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone
        :type Zone: str
        :param _StockCount: Specifies the stored amount.
        :type StockCount: int
        :param _HasStock: Whether it contains inventory.
        :type HasStock: bool
        :param _SlaveZoneStockInfos: Inventory information from availability zone.
        :type SlaveZoneStockInfos: list of SlaveZoneStockInfo
        """
        self._Zone = None
        self._StockCount = None
        self._HasStock = None
        self._SlaveZoneStockInfos = None

    @property
    def Zone(self):
        """Availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def StockCount(self):
        """Specifies the stored amount.
        :rtype: int
        """
        return self._StockCount

    @StockCount.setter
    def StockCount(self, StockCount):
        self._StockCount = StockCount

    @property
    def HasStock(self):
        """Whether it contains inventory.
        :rtype: bool
        """
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock

    @property
    def SlaveZoneStockInfos(self):
        """Inventory information from availability zone.
        :rtype: list of SlaveZoneStockInfo
        """
        return self._SlaveZoneStockInfos

    @SlaveZoneStockInfos.setter
    def SlaveZoneStockInfos(self, SlaveZoneStockInfos):
        self._SlaveZoneStockInfos = SlaveZoneStockInfos


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._StockCount = params.get("StockCount")
        self._HasStock = params.get("HasStock")
        if params.get("SlaveZoneStockInfos") is not None:
            self._SlaveZoneStockInfos = []
            for item in params.get("SlaveZoneStockInfos"):
                obj = SlaveZoneStockInfo()
                obj._deserialize(item)
                self._SlaveZoneStockInfos.append(obj)
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
        """ID of the instance to be manipulated
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def AutoRenewFlag(self):
        """Auto-renewal flag. 0: normal renewal, 1: auto-renewal, 2: no renewal.
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        """Number of successfully manipulated instances
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _Zone: Availability zone
        :type Zone: str
        :param _BinlogSyncWay: binlog synchronization mode.
        :type BinlogSyncWay: str
        """
        self._Zone = None
        self._BinlogSyncWay = None

    @property
    def Zone(self):
        """Availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def BinlogSyncWay(self):
        """binlog synchronization mode.
        :rtype: str
        """
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
        


class SlaveZoneStockInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _SlaveZone: Replica AZ.
        :type SlaveZone: str
        :param _StockCount: Inventory quantity in spare availability zone.	
        :type StockCount: int
        :param _HasStock: Whether there is inventory in the spare availability zone.	
        :type HasStock: bool
        """
        self._SlaveZone = None
        self._StockCount = None
        self._HasStock = None

    @property
    def SlaveZone(self):
        """Replica AZ.
        :rtype: str
        """
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def StockCount(self):
        """Inventory quantity in spare availability zone.	
        :rtype: int
        """
        return self._StockCount

    @StockCount.setter
    def StockCount(self, StockCount):
        self._StockCount = StockCount

    @property
    def HasStock(self):
        """Whether there is inventory in the spare availability zone.	
        :rtype: bool
        """
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock


    def _deserialize(self, params):
        self._SlaveZone = params.get("SlaveZone")
        self._StockCount = params.get("StockCount")
        self._HasStock = params.get("HasStock")
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
        :param _SyncReadCountRemote: Remote reading count.
Specifies that the database kernel version is larger than 3.1.12.
        :type SyncReadCountRemote: int
        :param _SyncReadBytesRemote: Number of remote read bytes.
Specifies that the database kernel version is larger than 3.1.12.
        :type SyncReadBytesRemote: int
        :param _SyncReadTimeRemote: Time spent on remote reads (µs).
Specifies that the database kernel version is larger than 3.1.12.
        :type SyncReadTimeRemote: int
        :param _SyncWriteCountRemote: Remote write count.
Specifies that the database kernel version is larger than 3.1.12.
        :type SyncWriteCountRemote: int
        :param _SyncWriteBytesRemote: Specifies the number of remote written bytes.
Specifies that the database kernel version is larger than 3.1.12.
        :type SyncWriteBytesRemote: int
        :param _SyncWriteTimeRemote: Time spent on remote writing (µs).
Specifies that the database kernel version is larger than 3.1.12.
        :type SyncWriteTimeRemote: int
        :param _TrxCommitDelay: Transaction submission delay (µs).
Specifies that the database kernel version is larger than 3.1.12.
        :type TrxCommitDelay: int
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
        self._SyncReadCountRemote = None
        self._SyncReadBytesRemote = None
        self._SyncReadTimeRemote = None
        self._SyncWriteCountRemote = None
        self._SyncWriteBytesRemote = None
        self._SyncWriteTimeRemote = None
        self._TrxCommitDelay = None

    @property
    def Timestamp(self):
        """Execution timestamp
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def QueryTime(self):
        """Execution duration in seconds
        :rtype: float
        """
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def SqlText(self):
        """SQL statement
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def UserHost(self):
        """Client host
        :rtype: str
        """
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def UserName(self):
        """Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        """Database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def LockTime(self):
        """Lock duration in seconds
        :rtype: float
        """
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def RowsExamined(self):
        """Number of scanned rows
        :rtype: int
        """
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsSent(self):
        """Number of returned rows
        :rtype: int
        """
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def SqlTemplate(self):
        """SQL template
        :rtype: str
        """
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def SqlMd5(self):
        """MD5 value of the SQL statement
        :rtype: str
        """
        return self._SqlMd5

    @SqlMd5.setter
    def SqlMd5(self, SqlMd5):
        self._SqlMd5 = SqlMd5

    @property
    def SyncReadCountRemote(self):
        """Remote reading count.
Specifies that the database kernel version is larger than 3.1.12.
        :rtype: int
        """
        return self._SyncReadCountRemote

    @SyncReadCountRemote.setter
    def SyncReadCountRemote(self, SyncReadCountRemote):
        self._SyncReadCountRemote = SyncReadCountRemote

    @property
    def SyncReadBytesRemote(self):
        """Number of remote read bytes.
Specifies that the database kernel version is larger than 3.1.12.
        :rtype: int
        """
        return self._SyncReadBytesRemote

    @SyncReadBytesRemote.setter
    def SyncReadBytesRemote(self, SyncReadBytesRemote):
        self._SyncReadBytesRemote = SyncReadBytesRemote

    @property
    def SyncReadTimeRemote(self):
        """Time spent on remote reads (µs).
Specifies that the database kernel version is larger than 3.1.12.
        :rtype: int
        """
        return self._SyncReadTimeRemote

    @SyncReadTimeRemote.setter
    def SyncReadTimeRemote(self, SyncReadTimeRemote):
        self._SyncReadTimeRemote = SyncReadTimeRemote

    @property
    def SyncWriteCountRemote(self):
        """Remote write count.
Specifies that the database kernel version is larger than 3.1.12.
        :rtype: int
        """
        return self._SyncWriteCountRemote

    @SyncWriteCountRemote.setter
    def SyncWriteCountRemote(self, SyncWriteCountRemote):
        self._SyncWriteCountRemote = SyncWriteCountRemote

    @property
    def SyncWriteBytesRemote(self):
        """Specifies the number of remote written bytes.
Specifies that the database kernel version is larger than 3.1.12.
        :rtype: int
        """
        return self._SyncWriteBytesRemote

    @SyncWriteBytesRemote.setter
    def SyncWriteBytesRemote(self, SyncWriteBytesRemote):
        self._SyncWriteBytesRemote = SyncWriteBytesRemote

    @property
    def SyncWriteTimeRemote(self):
        """Time spent on remote writing (µs).
Specifies that the database kernel version is larger than 3.1.12.
        :rtype: int
        """
        return self._SyncWriteTimeRemote

    @SyncWriteTimeRemote.setter
    def SyncWriteTimeRemote(self, SyncWriteTimeRemote):
        self._SyncWriteTimeRemote = SyncWriteTimeRemote

    @property
    def TrxCommitDelay(self):
        """Transaction submission delay (µs).
Specifies that the database kernel version is larger than 3.1.12.
        :rtype: int
        """
        return self._TrxCommitDelay

    @TrxCommitDelay.setter
    def TrxCommitDelay(self, TrxCommitDelay):
        self._TrxCommitDelay = TrxCommitDelay


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
        self._SyncReadCountRemote = params.get("SyncReadCountRemote")
        self._SyncReadBytesRemote = params.get("SyncReadBytesRemote")
        self._SyncReadTimeRemote = params.get("SyncReadTimeRemote")
        self._SyncWriteCountRemote = params.get("SyncWriteCountRemote")
        self._SyncWriteBytesRemote = params.get("SyncWriteBytesRemote")
        self._SyncWriteTimeRemote = params.get("SyncWriteTimeRemote")
        self._TrxCommitDelay = params.get("TrxCommitDelay")
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def UniqVpcId(self):
        """VPC ID in string
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        """Subnet ID in string
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def OldIpReserveHours(self):
        """Valid hours of old IP
        :rtype: int
        """
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
        """Async task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def OldZone(self):
        """The current AZ
        :rtype: str
        """
        return self._OldZone

    @OldZone.setter
    def OldZone(self, OldZone):
        self._OldZone = OldZone

    @property
    def NewZone(self):
        """New AZ
        :rtype: str
        """
        return self._NewZone

    @NewZone.setter
    def NewZone(self, NewZone):
        self._NewZone = NewZone

    @property
    def IsInMaintainPeriod(self):
        """Valid values: `yes` (execute during maintenance time), `no` (execute now)
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async FlowId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def UniqVpcId(self):
        """VPC ID in string
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        """Subnet ID in string
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def OldIpReserveHours(self):
        """Valid hours of old IP
        :rtype: int
        """
        return self._OldIpReserveHours

    @OldIpReserveHours.setter
    def OldIpReserveHours(self, OldIpReserveHours):
        self._OldIpReserveHours = OldIpReserveHours

    @property
    def ProxyGroupId(self):
        """Database proxy group ID (required), which can be obtained through the `DescribeProxies` API.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Database name
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def TableName(self):
        """Table name
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Privileges(self):
        """Permission list
        :rtype: list of str
        """
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
        """Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
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
        


class TemplateParamInfo(AbstractModel):
    """Parameter template details

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _Default: Default value
        :type Default: str
        :param _EnumValue: The collection of optional value types when the parameter type is `enum`.
        :type EnumValue: list of str
        :param _Max: The maximum value when the parameter type is float/integer.
        :type Max: str
        :param _Min: Minimum value when the parameter type is float/integer.
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
        """Current value
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Default(self):
        """Default value
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def EnumValue(self):
        """The collection of optional value types when the parameter type is `enum`.
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Max(self):
        """The maximum value when the parameter type is float/integer.
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        """Minimum value when the parameter type is float/integer.
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ParamName(self):
        """Parameter name
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def NeedReboot(self):
        """Whether to restart the instance for the parameter to take effect
        :rtype: int
        """
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Description(self):
        """Parameter description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParamType(self):
        """Parameter type. Valid value: `integer`, `float`, `string`, `enum`.
        :rtype: str
        """
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
        :param _TotalPrice: Resource total price under prepaid mode, excluding discounts. unit: cent.
        :type TotalPrice: int
        :param _Discount: Total discount. `100` means no discount.
        :type Discount: float
        :param _TotalPriceDiscount: Discounted total price under prepaid mode, unit: fen. for example, the user enjoys a Discount = TotalPrice × Discount.
        :type TotalPriceDiscount: int
        :param _UnitPrice: Unit resource price in postpaid mode, excluding discounts. unit: cent.
        :type UnitPrice: int
        :param _UnitPriceDiscount: Unit resource price in postpaid mode after Discount, unit: fen. for example, the user enjoys a Discount = unitprice × Discount.
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
        """Resource total price under prepaid mode, excluding discounts. unit: cent.
        :rtype: int
        """
        return self._TotalPrice

    @TotalPrice.setter
    def TotalPrice(self, TotalPrice):
        self._TotalPrice = TotalPrice

    @property
    def Discount(self):
        """Total discount. `100` means no discount.
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def TotalPriceDiscount(self):
        """Discounted total price under prepaid mode, unit: fen. for example, the user enjoys a Discount = TotalPrice × Discount.
        :rtype: int
        """
        return self._TotalPriceDiscount

    @TotalPriceDiscount.setter
    def TotalPriceDiscount(self, TotalPriceDiscount):
        self._TotalPriceDiscount = TotalPriceDiscount

    @property
    def UnitPrice(self):
        """Unit resource price in postpaid mode, excluding discounts. unit: cent.
        :rtype: int
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        """Unit resource price in postpaid mode after Discount, unit: fen. for example, the user enjoys a Discount = unitprice × Discount.
        :rtype: int
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def ChargeUnit(self):
        """Price unit
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def PackageIds(self):
        """The unique ID of a resource pack. If this parameter is left empty, all resource packs of the instance will be unbound.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CynosVersion(self):
        """Kernel version
        :rtype: str
        """
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def UpgradeType(self):
        """Upgrade time type. Valid values: `upgradeImmediate`, `upgradeInMaintain`.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async task ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cpu(self):
        """Database CPU
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Database memory in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def UpgradeType(self):
        """Upgrade type. Valid values: upgradeImmediate, upgradeInMaintain
        :rtype: str
        """
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

    @property
    def StorageLimit(self):
        """This parameter has been disused.
        :rtype: int
        """
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def AutoVoucher(self):
        """Whether to automatically select a voucher. 1: yes; 0: no. Default value: 0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def DbType(self):
        """This parameter has been disused.
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DealMode(self):
        """Transaction mode. Valid values: `0` (place and pay for an order), `1` (place an order)
        :rtype: int
        """
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def UpgradeMode(self):
        """Valid values: `NormalUpgrade` (Normal mode), `FastUpgrade` (QuickChange). If the system detects that the configuration modification process will cause a momentary disconnection, the process will be terminated.
        :rtype: str
        """
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
        :param _TranId: Frozen transaction ID.
        :type TranId: str
        :param _BigDealIds: Large order number.
        :type BigDealIds: list of str
        :param _DealNames: Order ID
        :type DealNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TranId = None
        self._BigDealIds = None
        self._DealNames = None
        self._RequestId = None

    @property
    def TranId(self):
        """Frozen transaction ID.
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def BigDealIds(self):
        """Large order number.
        :rtype: list of str
        """
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def DealNames(self):
        """Order ID
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Cpu(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        """Memory
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def ProxyCount(self):
        """Number of nodes in the proxy group
        :rtype: int
        """
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def ProxyGroupId(self):
        """ID of the database proxy group (disused)
        :rtype: str
        """
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ReloadBalance(self):
        """Load rebalance mode. Valid values: `auto`, `manual`
        :rtype: str
        """
        return self._ReloadBalance

    @ReloadBalance.setter
    def ReloadBalance(self, ReloadBalance):
        self._ReloadBalance = ReloadBalance

    @property
    def IsInMaintainPeriod(self):
        """Upgrade time. Valid values: `no` (upon upgrade completion), `timeWindow` (upgrade during instance maintenance time)
        :rtype: str
        """
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod

    @property
    def ProxyZones(self):
        """Node information of the atabase proxy
        :rtype: list of ProxyZone
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """Async flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        """Async task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SrcProxyVersion(self):
        """Current version of database proxy
        :rtype: str
        """
        return self._SrcProxyVersion

    @SrcProxyVersion.setter
    def SrcProxyVersion(self, SrcProxyVersion):
        self._SrcProxyVersion = SrcProxyVersion

    @property
    def DstProxyVersion(self):
        """Target version of database proxy
        :rtype: str
        """
        return self._DstProxyVersion

    @DstProxyVersion.setter
    def DstProxyVersion(self, DstProxyVersion):
        self._DstProxyVersion = DstProxyVersion

    @property
    def ProxyGroupId(self):
        """Database proxy group ID
        :rtype: str
        """
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def IsInMaintainPeriod(self):
        """Upgrade time. Valid values: `no` (upon upgrade completion), `yes` (upgrade during instance maintenance time)
        :rtype: str
        """
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
        """Async flow ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        """Async task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _DbHost: Client IP
        :type DbHost: str
        :param _DbPrivilege: User permission
        :type DbPrivilege: str
        """
        self._DbUserName = None
        self._DbHost = None
        self._DbPrivilege = None

    @property
    def DbUserName(self):
        """Authorized user
        :rtype: str
        """
        return self._DbUserName

    @DbUserName.setter
    def DbUserName(self, DbUserName):
        self._DbUserName = DbUserName

    @property
    def DbHost(self):
        """Client IP
        :rtype: str
        """
        return self._DbHost

    @DbHost.setter
    def DbHost(self, DbHost):
        self._DbHost = DbHost

    @property
    def DbPrivilege(self):
        """User permission
        :rtype: str
        """
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
        :param _SlaveZoneStockInfos: Available zone inventory information.
        :type SlaveZoneStockInfos: list of SlaveZoneStockInfo
        """
        self._Zone = None
        self._HasStock = None
        self._StockCount = None
        self._SlaveZoneStockInfos = None

    @property
    def Zone(self):
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def HasStock(self):
        """Whether there is an inventory.
        :rtype: bool
        """
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock

    @property
    def StockCount(self):
        """Quantity in stock
        :rtype: int
        """
        return self._StockCount

    @StockCount.setter
    def StockCount(self, StockCount):
        self._StockCount = StockCount

    @property
    def SlaveZoneStockInfos(self):
        """Available zone inventory information.
        :rtype: list of SlaveZoneStockInfo
        """
        return self._SlaveZoneStockInfos

    @SlaveZoneStockInfos.setter
    def SlaveZoneStockInfos(self, SlaveZoneStockInfos):
        self._SlaveZoneStockInfos = SlaveZoneStockInfos


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._HasStock = params.get("HasStock")
        self._StockCount = params.get("StockCount")
        if params.get("SlaveZoneStockInfos") is not None:
            self._SlaveZoneStockInfos = []
            for item in params.get("SlaveZoneStockInfos"):
                obj = SlaveZoneStockInfo()
                obj._deserialize(item)
                self._SlaveZoneStockInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        