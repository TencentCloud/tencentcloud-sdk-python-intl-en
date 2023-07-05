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


class ActionTimer(AbstractModel):
    """Scheduled tasks.

    """

    def __init__(self):
        r"""
        :param _TimerAction: Timer action. Valid value: `TerminateInstances`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TimerAction: str
        :param _ActionTime: Action time, which follows the ISO8601 standard and uses UTC time. It must be 5 minutes later than the current time. Format: YYYY-MM-DDThh:mm:ssZ. For example: 2018-05-29T11:26:40Z.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ActionTime: str
        :param _Externals: Extended data
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        """
        self._TimerAction = None
        self._ActionTime = None
        self._Externals = None

    @property
    def TimerAction(self):
        return self._TimerAction

    @TimerAction.setter
    def TimerAction(self, TimerAction):
        self._TimerAction = TimerAction

    @property
    def ActionTime(self):
        return self._ActionTime

    @ActionTime.setter
    def ActionTime(self, ActionTime):
        self._ActionTime = ActionTime

    @property
    def Externals(self):
        return self._Externals

    @Externals.setter
    def Externals(self, Externals):
        self._Externals = Externals


    def _deserialize(self, params):
        self._TimerAction = params.get("TimerAction")
        self._ActionTime = params.get("ActionTime")
        if params.get("Externals") is not None:
            self._Externals = Externals()
            self._Externals._deserialize(params.get("Externals"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateHostsRequest(AbstractModel):
    """AllocateHosts request structure.

    """

    def __init__(self):
        r"""
        :param _Placement: Instance location. This parameter is used to specify the attributes of an instance, such as its availability zone and project.
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _ClientToken: A string used to ensure the idempotency of the request.
        :type ClientToken: str
        :param _HostChargePrepaid: Configuration of prepaid instances. You can use the parameter to specify the attributes of prepaid instances, such as the subscription period and the auto-renewal plan. This parameter is required for prepaid instances.
        :type HostChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.ChargePrepaid`
        :param _HostChargeType: Instance billing model, only monthly or yearly subscription supported. Default value: `PREPAID'.
        :type HostChargeType: str
        :param _HostType: CDH instance model. Default value: `HS1`.
        :type HostType: str
        :param _HostCount: Quantity of CDH instances purchased. Default value: 1.
        :type HostCount: int
        :param _TagSpecification: Tag description. You can specify the parameter to associate a tag with an instance.
        :type TagSpecification: list of TagSpecification
        """
        self._Placement = None
        self._ClientToken = None
        self._HostChargePrepaid = None
        self._HostChargeType = None
        self._HostType = None
        self._HostCount = None
        self._TagSpecification = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def HostChargePrepaid(self):
        return self._HostChargePrepaid

    @HostChargePrepaid.setter
    def HostChargePrepaid(self, HostChargePrepaid):
        self._HostChargePrepaid = HostChargePrepaid

    @property
    def HostChargeType(self):
        return self._HostChargeType

    @HostChargeType.setter
    def HostChargeType(self, HostChargeType):
        self._HostChargeType = HostChargeType

    @property
    def HostType(self):
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def HostCount(self):
        return self._HostCount

    @HostCount.setter
    def HostCount(self, HostCount):
        self._HostCount = HostCount

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ClientToken = params.get("ClientToken")
        if params.get("HostChargePrepaid") is not None:
            self._HostChargePrepaid = ChargePrepaid()
            self._HostChargePrepaid._deserialize(params.get("HostChargePrepaid"))
        self._HostChargeType = params.get("HostChargeType")
        self._HostType = params.get("HostType")
        self._HostCount = params.get("HostCount")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateHostsResponse(AbstractModel):
    """AllocateHosts response structure.

    """

    def __init__(self):
        r"""
        :param _HostIdSet: IDs of created instances
        :type HostIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HostIdSet = None
        self._RequestId = None

    @property
    def HostIdSet(self):
        return self._HostIdSet

    @HostIdSet.setter
    def HostIdSet(self, HostIdSet):
        self._HostIdSet = HostIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HostIdSet = params.get("HostIdSet")
        self._RequestId = params.get("RequestId")


class AssociateInstancesKeyPairsRequest(AbstractModel):
    """AssociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). The maximum number of instances in each request is 100. <br>You can obtain the available instance IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the instance IDs. <br><li>Call [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceIds: list of str
        :param _KeyIds: Key ID(s). The maximum number of key pairs in each request is 100. The key pair ID is in the format of `skey-3glfot13`. <br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) and look for `KeyId` in the response.
        :type KeyIds: list of str
        :param _ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before associating a key pair with it. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE.
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._KeyIds = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._KeyIds = params.get("KeyIds")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateInstancesKeyPairsResponse(AbstractModel):
    """AssociateInstancesKeyPairs response structure.

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


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: ID of the security group to be associated, such as `sg-efil73jd`. Only one security group can be associated.
        :type SecurityGroupIds: list of str
        :param _InstanceIds: ID of the instance bound in the format of ins-lesecurk. You can specify up to 100 instances in each request.
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

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


class ChargePrepaid(AbstractModel):
    """Parameters related to the prepaid billing method, including the subscription period, the auto renewal logic, etc.

    """

    def __init__(self):
        r"""
        :param _Period: Purchased usage period, in month. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36
        :type Period: int
        :param _RenewFlag: Auto renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify upon expiration nor renew automatically <br><br>Default value: NOTIFY_AND_AUTO_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis if the account balance is sufficient.
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChcDeployExtraConfig(AbstractModel):
    """Configuration options for MiniOS of the CHC deployment network

    """


class ChcHost(AbstractModel):
    """CHC host information

    """

    def __init__(self):
        r"""
        :param _ChcId: CHC host ID
        :type ChcId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _SerialNumber: Server serial number
        :type SerialNumber: str
        :param _InstanceState: CHC host status<br/>
<ul>
<li>REGISTERED: The CHC host is registered, but the out-of-band network and deployment network are not configured.</li>
<li>VPC_READY: The out-of-band network and deployment network are configured.</li>
<li>PREPARED: It’s ready and can be associated with a CVM.</li>
<li>ONLINE: It’s already associated with a CVM.</li>
</ul>
        :type InstanceState: str
        :param _DeviceType: Device type
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeviceType: str
        :param _Placement: Availability zone
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _BmcVirtualPrivateCloud: Out-of-band network
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BmcVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _BmcIp: Out-of-band network IP
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BmcIp: str
        :param _BmcSecurityGroupIds: Out-of-band network security group ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BmcSecurityGroupIds: list of str
        :param _DeployVirtualPrivateCloud: Deployment network
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _DeployIp: Deployment network IP
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployIp: str
        :param _DeploySecurityGroupIds: Deployment network security group ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeploySecurityGroupIds: list of str
        :param _CvmInstanceId: ID of the associated CVM
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CvmInstanceId: str
        :param _CreatedTime: Server creation time
        :type CreatedTime: str
        :param _HardwareDescription: Instance hardware description, including CPU cores, memory capacity and disk capacity.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HardwareDescription: str
        :param _CPU: CPU cores of the CHC host
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CPU: int
        :param _Memory: Memory capacity of the CHC host (unit: GB)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Memory: int
        :param _Disk: Disk capacity of the CHC host
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Disk: str
        :param _BmcMAC: MAC address assigned under the out-of-band network
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BmcMAC: str
        :param _DeployMAC: MAC address assigned under the deployment network
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployMAC: str
        :param _TenantType: Management type
HOSTING: Hosting
TENANT: Leasing
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TenantType: str
        :param _DeployExtraConfig: CHC DHCP option, which is used for MiniOS debugging.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployExtraConfig: :class:`tencentcloud.cvm.v20170312.models.ChcDeployExtraConfig`
        """
        self._ChcId = None
        self._InstanceName = None
        self._SerialNumber = None
        self._InstanceState = None
        self._DeviceType = None
        self._Placement = None
        self._BmcVirtualPrivateCloud = None
        self._BmcIp = None
        self._BmcSecurityGroupIds = None
        self._DeployVirtualPrivateCloud = None
        self._DeployIp = None
        self._DeploySecurityGroupIds = None
        self._CvmInstanceId = None
        self._CreatedTime = None
        self._HardwareDescription = None
        self._CPU = None
        self._Memory = None
        self._Disk = None
        self._BmcMAC = None
        self._DeployMAC = None
        self._TenantType = None
        self._DeployExtraConfig = None

    @property
    def ChcId(self):
        return self._ChcId

    @ChcId.setter
    def ChcId(self, ChcId):
        self._ChcId = ChcId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SerialNumber(self):
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def BmcVirtualPrivateCloud(self):
        return self._BmcVirtualPrivateCloud

    @BmcVirtualPrivateCloud.setter
    def BmcVirtualPrivateCloud(self, BmcVirtualPrivateCloud):
        self._BmcVirtualPrivateCloud = BmcVirtualPrivateCloud

    @property
    def BmcIp(self):
        return self._BmcIp

    @BmcIp.setter
    def BmcIp(self, BmcIp):
        self._BmcIp = BmcIp

    @property
    def BmcSecurityGroupIds(self):
        return self._BmcSecurityGroupIds

    @BmcSecurityGroupIds.setter
    def BmcSecurityGroupIds(self, BmcSecurityGroupIds):
        self._BmcSecurityGroupIds = BmcSecurityGroupIds

    @property
    def DeployVirtualPrivateCloud(self):
        return self._DeployVirtualPrivateCloud

    @DeployVirtualPrivateCloud.setter
    def DeployVirtualPrivateCloud(self, DeployVirtualPrivateCloud):
        self._DeployVirtualPrivateCloud = DeployVirtualPrivateCloud

    @property
    def DeployIp(self):
        return self._DeployIp

    @DeployIp.setter
    def DeployIp(self, DeployIp):
        self._DeployIp = DeployIp

    @property
    def DeploySecurityGroupIds(self):
        return self._DeploySecurityGroupIds

    @DeploySecurityGroupIds.setter
    def DeploySecurityGroupIds(self, DeploySecurityGroupIds):
        self._DeploySecurityGroupIds = DeploySecurityGroupIds

    @property
    def CvmInstanceId(self):
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def HardwareDescription(self):
        return self._HardwareDescription

    @HardwareDescription.setter
    def HardwareDescription(self, HardwareDescription):
        self._HardwareDescription = HardwareDescription

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

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
    def BmcMAC(self):
        return self._BmcMAC

    @BmcMAC.setter
    def BmcMAC(self, BmcMAC):
        self._BmcMAC = BmcMAC

    @property
    def DeployMAC(self):
        return self._DeployMAC

    @DeployMAC.setter
    def DeployMAC(self, DeployMAC):
        self._DeployMAC = DeployMAC

    @property
    def TenantType(self):
        return self._TenantType

    @TenantType.setter
    def TenantType(self, TenantType):
        self._TenantType = TenantType

    @property
    def DeployExtraConfig(self):
        return self._DeployExtraConfig

    @DeployExtraConfig.setter
    def DeployExtraConfig(self, DeployExtraConfig):
        self._DeployExtraConfig = DeployExtraConfig


    def _deserialize(self, params):
        self._ChcId = params.get("ChcId")
        self._InstanceName = params.get("InstanceName")
        self._SerialNumber = params.get("SerialNumber")
        self._InstanceState = params.get("InstanceState")
        self._DeviceType = params.get("DeviceType")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("BmcVirtualPrivateCloud") is not None:
            self._BmcVirtualPrivateCloud = VirtualPrivateCloud()
            self._BmcVirtualPrivateCloud._deserialize(params.get("BmcVirtualPrivateCloud"))
        self._BmcIp = params.get("BmcIp")
        self._BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self._DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self._DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self._DeployIp = params.get("DeployIp")
        self._DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._CreatedTime = params.get("CreatedTime")
        self._HardwareDescription = params.get("HardwareDescription")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._BmcMAC = params.get("BmcMAC")
        self._DeployMAC = params.get("DeployMAC")
        self._TenantType = params.get("TenantType")
        if params.get("DeployExtraConfig") is not None:
            self._DeployExtraConfig = ChcDeployExtraConfig()
            self._DeployExtraConfig._deserialize(params.get("DeployExtraConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChcHostDeniedActions(AbstractModel):
    """Describe details of actions not allowed for a CHC instance

    """

    def __init__(self):
        r"""
        :param _ChcId: CHC instance ID
        :type ChcId: str
        :param _State: CHC instance status
        :type State: str
        :param _DenyActions: Actions not allowed for the current CHC instance
        :type DenyActions: list of str
        """
        self._ChcId = None
        self._State = None
        self._DenyActions = None

    @property
    def ChcId(self):
        return self._ChcId

    @ChcId.setter
    def ChcId(self, ChcId):
        self._ChcId = ChcId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def DenyActions(self):
        return self._DenyActions

    @DenyActions.setter
    def DenyActions(self, DenyActions):
        self._DenyActions = DenyActions


    def _deserialize(self, params):
        self._ChcId = params.get("ChcId")
        self._State = params.get("State")
        self._DenyActions = params.get("DenyActions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcAssistVpcRequest(AbstractModel):
    """ConfigureChcAssistVpc request structure.

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC host IDs
        :type ChcIds: list of str
        :param _BmcVirtualPrivateCloud: Out-of-band network information
        :type BmcVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _BmcSecurityGroupIds: Out-of-band network security group list
        :type BmcSecurityGroupIds: list of str
        :param _DeployVirtualPrivateCloud: Deployment network information
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _DeploySecurityGroupIds: Deployment network security group list
        :type DeploySecurityGroupIds: list of str
        """
        self._ChcIds = None
        self._BmcVirtualPrivateCloud = None
        self._BmcSecurityGroupIds = None
        self._DeployVirtualPrivateCloud = None
        self._DeploySecurityGroupIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

    @property
    def BmcVirtualPrivateCloud(self):
        return self._BmcVirtualPrivateCloud

    @BmcVirtualPrivateCloud.setter
    def BmcVirtualPrivateCloud(self, BmcVirtualPrivateCloud):
        self._BmcVirtualPrivateCloud = BmcVirtualPrivateCloud

    @property
    def BmcSecurityGroupIds(self):
        return self._BmcSecurityGroupIds

    @BmcSecurityGroupIds.setter
    def BmcSecurityGroupIds(self, BmcSecurityGroupIds):
        self._BmcSecurityGroupIds = BmcSecurityGroupIds

    @property
    def DeployVirtualPrivateCloud(self):
        return self._DeployVirtualPrivateCloud

    @DeployVirtualPrivateCloud.setter
    def DeployVirtualPrivateCloud(self, DeployVirtualPrivateCloud):
        self._DeployVirtualPrivateCloud = DeployVirtualPrivateCloud

    @property
    def DeploySecurityGroupIds(self):
        return self._DeploySecurityGroupIds

    @DeploySecurityGroupIds.setter
    def DeploySecurityGroupIds(self, DeploySecurityGroupIds):
        self._DeploySecurityGroupIds = DeploySecurityGroupIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        if params.get("BmcVirtualPrivateCloud") is not None:
            self._BmcVirtualPrivateCloud = VirtualPrivateCloud()
            self._BmcVirtualPrivateCloud._deserialize(params.get("BmcVirtualPrivateCloud"))
        self._BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self._DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self._DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self._DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcAssistVpcResponse(AbstractModel):
    """ConfigureChcAssistVpc response structure.

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


class ConfigureChcDeployVpcRequest(AbstractModel):
    """ConfigureChcDeployVpc request structure.

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC instance ID
        :type ChcIds: list of str
        :param _DeployVirtualPrivateCloud: Deployment network information
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _DeploySecurityGroupIds: Deployment network security group list
        :type DeploySecurityGroupIds: list of str
        """
        self._ChcIds = None
        self._DeployVirtualPrivateCloud = None
        self._DeploySecurityGroupIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

    @property
    def DeployVirtualPrivateCloud(self):
        return self._DeployVirtualPrivateCloud

    @DeployVirtualPrivateCloud.setter
    def DeployVirtualPrivateCloud(self, DeployVirtualPrivateCloud):
        self._DeployVirtualPrivateCloud = DeployVirtualPrivateCloud

    @property
    def DeploySecurityGroupIds(self):
        return self._DeploySecurityGroupIds

    @DeploySecurityGroupIds.setter
    def DeploySecurityGroupIds(self, DeploySecurityGroupIds):
        self._DeploySecurityGroupIds = DeploySecurityGroupIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self._DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self._DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self._DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcDeployVpcResponse(AbstractModel):
    """ConfigureChcDeployVpc response structure.

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


class CreateDisasterRecoverGroupRequest(AbstractModel):
    """CreateDisasterRecoverGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name of the spread placement group. The name must be 1-60 characters long and can contain both Chinese characters and English letters.
        :type Name: str
        :param _Type: Type of the spread placement group. Valid values: <br><li>HOST: physical machine <br><li>SW: switch <br><li>RACK: rack
        :type Type: str
        :param _ClientToken: A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed. <br>For more information, see 'How to ensure idempotency'.
        :type ClientToken: str
        """
        self._Name = None
        self._Type = None
        self._ClientToken = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisasterRecoverGroupResponse(AbstractModel):
    """CreateDisasterRecoverGroup response structure.

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupId: List of spread placement group IDs.
        :type DisasterRecoverGroupId: str
        :param _Type: Type of the spread placement group. Valid values: <br><li>HOST: physical machine <br><li>SW: switch <br><li>RACK: rack.
        :type Type: str
        :param _Name: Name of the spread placement group. The name must be 1-60 characters long and can contain both Chinese characters and English letters.
        :type Name: str
        :param _CvmQuotaTotal: The maximum number of CVMs in a placement group.
        :type CvmQuotaTotal: int
        :param _CurrentNum: The current number of CVMs in a placement group.
        :type CurrentNum: int
        :param _CreateTime: Creation time of the placement group.
        :type CreateTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DisasterRecoverGroupId = None
        self._Type = None
        self._Name = None
        self._CvmQuotaTotal = None
        self._CurrentNum = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def DisasterRecoverGroupId(self):
        return self._DisasterRecoverGroupId

    @DisasterRecoverGroupId.setter
    def DisasterRecoverGroupId(self, DisasterRecoverGroupId):
        self._DisasterRecoverGroupId = DisasterRecoverGroupId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CvmQuotaTotal(self):
        return self._CvmQuotaTotal

    @CvmQuotaTotal.setter
    def CvmQuotaTotal(self, CvmQuotaTotal):
        self._CvmQuotaTotal = CvmQuotaTotal

    @property
    def CurrentNum(self):
        return self._CurrentNum

    @CurrentNum.setter
    def CurrentNum(self, CurrentNum):
        self._CurrentNum = CurrentNum

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._CvmQuotaTotal = params.get("CvmQuotaTotal")
        self._CurrentNum = params.get("CurrentNum")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage request structure.

    """

    def __init__(self):
        r"""
        :param _ImageName: Image name
        :type ImageName: str
        :param _InstanceId: ID of the instance from which an image will be created. This parameter is required when using instance to create an image.
        :type InstanceId: str
        :param _ImageDescription: Image description
        :type ImageDescription: str
        :param _ForcePoweroff: Whether to force shut down an instance to create an image when a soft shutdown fails
        :type ForcePoweroff: str
        :param _Sysprep: Whether to enable Sysprep when creating a Windows image.
Valid values: `TRUE` and `FALSE`; default value: `FALSE`.

Click [here](https://intl.cloud.tencent.com/document/product/213/43498?from_cn_redirect=1) to learn more about Sysprep.
        :type Sysprep: str
        :param _DataDiskIds: IDs of data disks included in the image. 
        :type DataDiskIds: list of str
        :param _SnapshotIds: Specified snapshot ID used to create an image. A system disk snapshot must be included. It cannot be passed together with `InstanceId`.
        :type SnapshotIds: list of str
        :param _DryRun: Success status of this request, without affecting the resources involved
        :type DryRun: bool
        :param _TagSpecification: Tag description list. This parameter is used to bind a tag to a custom image.
        :type TagSpecification: list of TagSpecification
        """
        self._ImageName = None
        self._InstanceId = None
        self._ImageDescription = None
        self._ForcePoweroff = None
        self._Sysprep = None
        self._DataDiskIds = None
        self._SnapshotIds = None
        self._DryRun = None
        self._TagSpecification = None

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageDescription(self):
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def ForcePoweroff(self):
        return self._ForcePoweroff

    @ForcePoweroff.setter
    def ForcePoweroff(self, ForcePoweroff):
        self._ForcePoweroff = ForcePoweroff

    @property
    def Sysprep(self):
        return self._Sysprep

    @Sysprep.setter
    def Sysprep(self, Sysprep):
        self._Sysprep = Sysprep

    @property
    def DataDiskIds(self):
        return self._DataDiskIds

    @DataDiskIds.setter
    def DataDiskIds(self, DataDiskIds):
        self._DataDiskIds = DataDiskIds

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._ImageName = params.get("ImageName")
        self._InstanceId = params.get("InstanceId")
        self._ImageDescription = params.get("ImageDescription")
        self._ForcePoweroff = params.get("ForcePoweroff")
        self._Sysprep = params.get("Sysprep")
        self._DataDiskIds = params.get("DataDiskIds")
        self._SnapshotIds = params.get("SnapshotIds")
        self._DryRun = params.get("DryRun")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage response structure.

    """

    def __init__(self):
        r"""
        :param _ImageId: Image ID.
Note: This field may return null, indicating that no valid value was found.
        :type ImageId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImageId = None
        self._RequestId = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair request structure.

    """

    def __init__(self):
        r"""
        :param _KeyName: Name of the key pair, which can contain numbers, letters, and underscores, with a maximum length of 25 characters.
        :type KeyName: str
        :param _ProjectId: The ID of the project to which the new key pair belongs.
You can query the project IDs in two ways:
<li>Query the project IDs in the project list.
<li>Call `DescribeProject` and look for `projectId` in the response.
        :type ProjectId: int
        :param _TagSpecification: Tag description list. This parameter is used to bind a tag to a key pair.
        :type TagSpecification: list of TagSpecification
        """
        self._KeyName = None
        self._ProjectId = None
        self._TagSpecification = None

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair response structure.

    """

    def __init__(self):
        r"""
        :param _KeyPair: Key pair information.
        :type KeyPair: :class:`tencentcloud.cvm.v20170312.models.KeyPair`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyPair = None
        self._RequestId = None

    @property
    def KeyPair(self):
        return self._KeyPair

    @KeyPair.setter
    def KeyPair(self, KeyPair):
        self._KeyPair = KeyPair

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyPair") is not None:
            self._KeyPair = KeyPair()
            self._KeyPair._deserialize(params.get("KeyPair"))
        self._RequestId = params.get("RequestId")


class CreateLaunchTemplateVersionRequest(AbstractModel):
    """CreateLaunchTemplateVersion request structure.

    """

    def __init__(self):
        r"""
        :param _Placement: Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone, project, and CDH (for dedicated CVMs)
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _LaunchTemplateId: Instance launch template ID. This parameter is used as a basis for creating new template versions.
        :type LaunchTemplateId: str
        :param _LaunchTemplateVersion: This parameter, when specified, is used to create instance launch templates. If this parameter is not specified, the default version will be used.
        :type LaunchTemplateVersion: int
        :param _LaunchTemplateVersionDescription: Description of instance launch template versions. This parameter can contain 2-256 characters.
        :type LaunchTemplateVersionDescription: str
        :param _InstanceType: The instance model. Different resource specifications are specified for different instance models.
<br><li>To view specific values for `PREPAID` or `POSTPAID_BY_HOUR` instances, you can call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1). If this parameter is not specified, the system will specify the default model according to the dynamic resource sales in the current region. <br><li>For `CDHPAID` instances, the value of this parameter is in the format of `CDH_XCXG` based on the number of CPU cores and memory capacity. For example, if you want to create a CDH instance with a single-core CPU and 1 GB memory, you need to specify this parameter as `CDH_1C1G`.
        :type InstanceType: str
        :param _ImageId: The [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are four types of images:<br/><li>Public images</li><li>Custom images</li><li>Shared images</li><li>Marketplace images (for Chinese mainland only)</li><br/>To check the image ID:<br/><li>For public images, custom images, and shared images, go to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE). For marketplace images, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1), pass in `InstanceType` to retrieve the list of images supported by the current model, and then find the `ImageId` in the response.</li>
        :type ImageId: str
        :param _SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: The configuration information of instance data disks. If this parameter is not specified, no data disk will be purchased by default. When purchasing, you can specify 21 data disks, which can contain at most 1 LOCAL_BASIC or LOCAL_SSD data disk, and at most 20 CLOUD_BASIC, CLOUD_PREMIUM, or CLOUD_SSD data disks.
        :type DataDisks: list of DataDisk
        :param _VirtualPrivateCloud: Configuration information of VPC. This parameter is used to specify VPC ID and subnet ID, etc. If this parameter is not specified, the classic network is used by default. If a VPC IP is specified in this parameter, it indicates the primary ENI IP of each instance. The value of parameter InstanceCount must be same as the number of VPC IPs, which cannot be greater than 20.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _InternetAccessible: Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _InstanceCount: Number of instances to be purchased. Value range for monthly-subscribed instances: [1, 300]. Value range for pay-as-you-go instances: [1, 100]. Default value: 1. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user. For more information on quota, see CVM instance [Purchase Limits](https://intl.cloud.tencent.com/document/product/213/2664).
        :type InstanceCount: int
        :param _InstanceName: Instance name to be displayed. <br><li>If this parameter is not specified, "Unnamed" will be displayed by default. </li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`. </li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and the instance name body is `server_`, the instance names will be `server_1` and `server_2`. </li><li>This parameter can contain up to 60 characters, including the pattern string.
        :type InstanceName: str
        :param _LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will be associated with default security groups.
        :type SecurityGroupIds: list of str
        :param _EnhancedService: Enhanced service. You can use this parameter to specify whether to enable services such as Anti-DDoS and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Anti-DDoS are enabled for public images by default. However, for custom images and images from the marketplace, Anti-DDoS and Cloud Monitor are not enabled by default. The original services in the image will be retained.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param _HostName: Host name of the CVM. <br><li>Dots (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name. <br><li>For Windows instances, the host name must be 2-15 characters long and can contain uppercase and lowercase letters, numbers, and hyphens (-). It cannot contain dots (.) or contain only numbers. <br><li>For other instances, such as Linux instances, the host name must be 2-60 characters long. It supports multiple dots (.) and allows uppercase and lowercase letters, numbers, and hyphens (-) between any two dots (.).
        :type HostName: str
        :param _ActionTimer: Scheduled tasks. You can use this parameter to specify scheduled tasks for the instance. Only scheduled termination is supported.
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param _DisasterRecoverGroupIds: Placement group ID. You can only specify one.
        :type DisasterRecoverGroupIds: list of str
        :param _TagSpecification: The tag description list. This parameter is used to bind a tag to a resource instance. A tag can only be bound to CVM instances.
        :type TagSpecification: list of TagSpecification
        :param _InstanceMarketOptions: Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param _UserData: User data provided to the instance. This parameter needs to be encoded in base64 format with the maximum size of 16KB. For more information on how to get the value of this parameter, see the commands you need to execute on startup for [Windows](https://intl.cloud.tencent.com/document/product/213/17526) or [Linux](https://intl.cloud.tencent.com/document/product/213/17525).
        :type UserData: str
        :param _DryRun: Whether the request is a dry run only.
`true`: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available.
If the dry run fails, the corresponding error code will be returned.
If the dry run succeeds, the RequestId will be returned.
`false` (default value): send a normal request and create instance(s) if all the requirements are met.
        :type DryRun: bool
        :param _CamRoleName: CAM role name, which can be obtained from the `roleName` field in the response of the [`DescribeRoleList`](https://intl.cloud.tencent.com/document/product/598/36223?from_cn_redirect=1) API.
        :type CamRoleName: str
        :param _HpcClusterId: HPC cluster ID. The HPC cluster must and can only be specified for a high-performance computing instance.
        :type HpcClusterId: str
        :param _InstanceChargeType: Instance [billing mode](https://intl.cloud.tencent.com/document/product/213/2180?from_cn_redirect=1). Valid values: <br><li>`PREPAID`: monthly subscription <br><li>`POSTPAID_BY_HOUR`: pay-as-you-go on an hourly basis <br><li>`CDHPAID`: billed on the associated CDH instance. <br><li>`SPOTPAID`: spot instances. <br>Default value: `POSTPAID_BY_HOUR`.
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _DisableApiTermination: Whether the termination protection is enabled. Values: <br><li>`TRUE`: Enable instance protection, which means that this instance can not be deleted by an API action.<br><li>`FALSE`: Do not enable the instance protection.<br><br>Default value: `FALSE`.
        :type DisableApiTermination: bool
        """
        self._Placement = None
        self._LaunchTemplateId = None
        self._LaunchTemplateVersion = None
        self._LaunchTemplateVersionDescription = None
        self._InstanceType = None
        self._ImageId = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceCount = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._ClientToken = None
        self._HostName = None
        self._ActionTimer = None
        self._DisasterRecoverGroupIds = None
        self._TagSpecification = None
        self._InstanceMarketOptions = None
        self._UserData = None
        self._DryRun = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._DisableApiTermination = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateVersion(self):
        return self._LaunchTemplateVersion

    @LaunchTemplateVersion.setter
    def LaunchTemplateVersion(self, LaunchTemplateVersion):
        self._LaunchTemplateVersion = LaunchTemplateVersion

    @property
    def LaunchTemplateVersionDescription(self):
        return self._LaunchTemplateVersionDescription

    @LaunchTemplateVersionDescription.setter
    def LaunchTemplateVersionDescription(self, LaunchTemplateVersionDescription):
        self._LaunchTemplateVersionDescription = LaunchTemplateVersionDescription

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def ActionTimer(self):
        return self._ActionTimer

    @ActionTimer.setter
    def ActionTimer(self, ActionTimer):
        self._ActionTimer = ActionTimer

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        self._LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self._InstanceType = params.get("InstanceType")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._ClientToken = params.get("ClientToken")
        self._HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self._ActionTimer = ActionTimer()
            self._ActionTimer._deserialize(params.get("ActionTimer"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._UserData = params.get("UserData")
        self._DryRun = params.get("DryRun")
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaunchTemplateVersionResponse(AbstractModel):
    """CreateLaunchTemplateVersion response structure.

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateVersionNumber: Version number of the new instance launch template.
        :type LaunchTemplateVersionNumber: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LaunchTemplateVersionNumber = None
        self._RequestId = None

    @property
    def LaunchTemplateVersionNumber(self):
        return self._LaunchTemplateVersionNumber

    @LaunchTemplateVersionNumber.setter
    def LaunchTemplateVersionNumber(self, LaunchTemplateVersionNumber):
        self._LaunchTemplateVersionNumber = LaunchTemplateVersionNumber

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LaunchTemplateVersionNumber = params.get("LaunchTemplateVersionNumber")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Describes data disk information.

    """

    def __init__(self):
        r"""
        :param _DiskSize: Data disk size (in GB). The minimum adjustment increment is 10 GB. The value range varies by data disk type. For more information on limits, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). The default value is 0, indicating that no data disk is purchased. For more information, see the product documentation.
        :type DiskSize: int
        :param _DiskType: Data disk type. For more information about limits on different data disk types, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values: <br><li>LOCAL_BASIC: local disk<br><li>LOCAL_SSD: local SSD disk<br><li>LOCAL_NVME: local NVME disk, specified in the `InstanceType`<br><li>LOCAL_PRO: local HDD disk, specified in the `InstanceType`<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium Cloud Storage<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD<br><li>CLOUD_TSSD: Tremendous SSD<br><li>CLOUD_BSSD: Balanced SSD<br><br>Default value: LOCAL_BASIC.<br><br>This parameter is invalid for the `ResizeInstanceDisk` API.
        :type DiskType: str
        :param _DiskId: Data disk ID. Note that it’s not available for `LOCAL_BASIC` and `LOCAL_SSD` disks.
It is only used as a response parameter for APIs such as `DescribeInstances`, and cannot be used as a request parameter for APIs such as `RunInstances`.
        :type DiskId: str
        :param _DeleteWithInstance: Whether to terminate the data disk when its CVM is terminated. Valid values:
<li>TRUE: terminate the data disk when its CVM is terminated. This value only supports pay-as-you-go cloud disks billed on an hourly basis.
<li>FALSE: retain the data disk when its CVM is terminated.<br>
Default value: TRUE<br>
Currently this parameter is only used in the `RunInstances` API.
Note: This field may return null, indicating that no valid value is found.
        :type DeleteWithInstance: bool
        :param _SnapshotId: Data disk snapshot ID. The size of the selected data disk snapshot must be smaller than that of the data disk.
Note: This field may return null, indicating that no valid value is found.
        :type SnapshotId: str
        :param _Encrypt: Specifies whether the data disk is encrypted. Valid values: 
<li>TRUE: encrypted
<li>FALSE: not encrypted<br>
Default value: FALSE<br>
This parameter is only used with `RunInstances`.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Encrypt: bool
        :param _KmsKeyId: ID of the custom CMK in the format of UUID or “kms-abcd1234”. This parameter is used to encrypt cloud disks.

Currently, this parameter is only used in the `RunInstances` API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KmsKeyId: str
        :param _ThroughputPerformance: Cloud disk performance, in MB/s
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ThroughputPerformance: int
        :param _CdcId: ID of the dedicated cluster to which the instance belongs.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CdcId: str
        """
        self._DiskSize = None
        self._DiskType = None
        self._DiskId = None
        self._DeleteWithInstance = None
        self._SnapshotId = None
        self._Encrypt = None
        self._KmsKeyId = None
        self._ThroughputPerformance = None
        self._CdcId = None

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def KmsKeyId(self):
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def CdcId(self):
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._SnapshotId = params.get("SnapshotId")
        self._Encrypt = params.get("Encrypt")
        self._KmsKeyId = params.get("KmsKeyId")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoverGroupsRequest(AbstractModel):
    """DeleteDisasterRecoverGroups request structure.

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupIds: ID list of spread placement groups, obtainable via the [DescribeDisasterRecoverGroups](https://intl.cloud.tencent.com/document/api/213/17810?from_cn_redirect=1) API. You can operate up to 100 spread placement groups in each request.
        :type DisasterRecoverGroupIds: list of str
        """
        self._DisasterRecoverGroupIds = None

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds


    def _deserialize(self, params):
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoverGroupsResponse(AbstractModel):
    """DeleteDisasterRecoverGroups response structure.

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


class DeleteImagesRequest(AbstractModel):
    """DeleteImages request structure.

    """

    def __init__(self):
        r"""
        :param _ImageIds: List of the IDs of the instances to be deleted.
        :type ImageIds: list of str
        :param _DeleteBindedSnap: Whether to delete the snapshot associated with the image
        :type DeleteBindedSnap: bool
        :param _DryRun: Check whether deleting an image is supported
        :type DryRun: bool
        """
        self._ImageIds = None
        self._DeleteBindedSnap = None
        self._DryRun = None

    @property
    def ImageIds(self):
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

    @property
    def DeleteBindedSnap(self):
        return self._DeleteBindedSnap

    @DeleteBindedSnap.setter
    def DeleteBindedSnap(self, DeleteBindedSnap):
        self._DeleteBindedSnap = DeleteBindedSnap

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        self._DeleteBindedSnap = params.get("DeleteBindedSnap")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImagesResponse(AbstractModel):
    """DeleteImages response structure.

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


class DeleteKeyPairsRequest(AbstractModel):
    """DeleteKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: Key ID(s). The maximum number of key pairs in each request is 100. <br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) and look for `KeyId` in the response.
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKeyPairsResponse(AbstractModel):
    """DeleteKeyPairs response structure.

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


class DeleteLaunchTemplateRequest(AbstractModel):
    """DeleteLaunchTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: The launch template ID
        :type LaunchTemplateId: str
        """
        self._LaunchTemplateId = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchTemplateResponse(AbstractModel):
    """DeleteLaunchTemplate response structure.

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


class DeleteLaunchTemplateVersionsRequest(AbstractModel):
    """DeleteLaunchTemplateVersions request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: The launch template ID
        :type LaunchTemplateId: str
        :param _LaunchTemplateVersions: List of instance launch template versions.
        :type LaunchTemplateVersions: list of int
        """
        self._LaunchTemplateId = None
        self._LaunchTemplateVersions = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateVersions(self):
        return self._LaunchTemplateVersions

    @LaunchTemplateVersions.setter
    def LaunchTemplateVersions(self, LaunchTemplateVersions):
        self._LaunchTemplateVersions = LaunchTemplateVersions


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateVersions = params.get("LaunchTemplateVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchTemplateVersionsResponse(AbstractModel):
    """DeleteLaunchTemplateVersions response structure.

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


class DescribeChcDeniedActionsRequest(AbstractModel):
    """DescribeChcDeniedActions request structure.

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC instance ID
        :type ChcIds: list of str
        """
        self._ChcIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChcDeniedActionsResponse(AbstractModel):
    """DescribeChcDeniedActions response structure.

    """

    def __init__(self):
        r"""
        :param _ChcHostDeniedActionSet: Actions not allowed for the CHC instance
        :type ChcHostDeniedActionSet: list of ChcHostDeniedActions
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ChcHostDeniedActionSet = None
        self._RequestId = None

    @property
    def ChcHostDeniedActionSet(self):
        return self._ChcHostDeniedActionSet

    @ChcHostDeniedActionSet.setter
    def ChcHostDeniedActionSet(self, ChcHostDeniedActionSet):
        self._ChcHostDeniedActionSet = ChcHostDeniedActionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ChcHostDeniedActionSet") is not None:
            self._ChcHostDeniedActionSet = []
            for item in params.get("ChcHostDeniedActionSet"):
                obj = ChcHostDeniedActions()
                obj._deserialize(item)
                self._ChcHostDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChcHostsRequest(AbstractModel):
    """DescribeChcHosts request structure.

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC host ID. Up to 100 instances per request is allowed. `ChcIds` and `Filters` cannot be specified at the same time.
        :type ChcIds: list of str
        :param _Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>availability zone</strong>, such as `ap-guangzhou-1`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p><p style="padding-left: 30px;">Valid values: See <a href="https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1">Regions and Availability Zones</a></p>
<li><strong>instance-name</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>instance name</strong>.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>instance-state</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>instance status</strong>. For status details, see [InstanceStatus](https://intl.cloud.tencent.com/document/api/213/15753?from_cn_redirect=1#InstanceStatus).</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>device-type</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>device type</strong>.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>vpc-id</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>unique VPC ID</strong>.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>subnet-id</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>unique VPC subnet ID</strong>.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
        :type Filters: list of Filter
        :param _Offset: The offset. Default value: `0`. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: The number of returned results. Default value: `20`. Maximum value: `100`. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self._ChcIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

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
        self._ChcIds = params.get("ChcIds")
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
        


class DescribeChcHostsResponse(AbstractModel):
    """DescribeChcHosts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances
        :type TotalCount: int
        :param _ChcHostSet: List of returned instances
        :type ChcHostSet: list of ChcHost
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ChcHostSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ChcHostSet(self):
        return self._ChcHostSet

    @ChcHostSet.setter
    def ChcHostSet(self, ChcHostSet):
        self._ChcHostSet = ChcHostSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ChcHostSet") is not None:
            self._ChcHostSet = []
            for item in params.get("ChcHostSet"):
                obj = ChcHost()
                obj._deserialize(item)
                self._ChcHostSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupQuotaRequest(AbstractModel):
    """DescribeDisasterRecoverGroupQuota request structure.

    """


class DescribeDisasterRecoverGroupQuotaResponse(AbstractModel):
    """DescribeDisasterRecoverGroupQuota response structure.

    """

    def __init__(self):
        r"""
        :param _GroupQuota: The maximum number of placement groups that can be created.
        :type GroupQuota: int
        :param _CurrentNum: The number of placement groups that have been created by the current user.
        :type CurrentNum: int
        :param _CvmInHostGroupQuota: Quota on instances in a physical-machine-type disaster recovery group.
        :type CvmInHostGroupQuota: int
        :param _CvmInSwGroupQuota: Quota on instances in a switch-type disaster recovery group.
        :type CvmInSwGroupQuota: int
        :param _CvmInRackGroupQuota: Quota on instances in a rack-type disaster recovery group.
        :type CvmInRackGroupQuota: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupQuota = None
        self._CurrentNum = None
        self._CvmInHostGroupQuota = None
        self._CvmInSwGroupQuota = None
        self._CvmInRackGroupQuota = None
        self._RequestId = None

    @property
    def GroupQuota(self):
        return self._GroupQuota

    @GroupQuota.setter
    def GroupQuota(self, GroupQuota):
        self._GroupQuota = GroupQuota

    @property
    def CurrentNum(self):
        return self._CurrentNum

    @CurrentNum.setter
    def CurrentNum(self, CurrentNum):
        self._CurrentNum = CurrentNum

    @property
    def CvmInHostGroupQuota(self):
        return self._CvmInHostGroupQuota

    @CvmInHostGroupQuota.setter
    def CvmInHostGroupQuota(self, CvmInHostGroupQuota):
        self._CvmInHostGroupQuota = CvmInHostGroupQuota

    @property
    def CvmInSwGroupQuota(self):
        return self._CvmInSwGroupQuota

    @CvmInSwGroupQuota.setter
    def CvmInSwGroupQuota(self, CvmInSwGroupQuota):
        self._CvmInSwGroupQuota = CvmInSwGroupQuota

    @property
    def CvmInRackGroupQuota(self):
        return self._CvmInRackGroupQuota

    @CvmInRackGroupQuota.setter
    def CvmInRackGroupQuota(self, CvmInRackGroupQuota):
        self._CvmInRackGroupQuota = CvmInRackGroupQuota

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupQuota = params.get("GroupQuota")
        self._CurrentNum = params.get("CurrentNum")
        self._CvmInHostGroupQuota = params.get("CvmInHostGroupQuota")
        self._CvmInSwGroupQuota = params.get("CvmInSwGroupQuota")
        self._CvmInRackGroupQuota = params.get("CvmInRackGroupQuota")
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupsRequest(AbstractModel):
    """DescribeDisasterRecoverGroups request structure.

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupIds: ID list of spread placement groups. You can operate up to 100 spread placement groups in each request.
        :type DisasterRecoverGroupIds: list of str
        :param _Name: Name of a spread placement group. Fuzzy match is supported.
        :type Name: str
        :param _Offset: Offset; default value: 0. For more information on `Offset`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377).
        :type Offset: int
        :param _Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). 
        :type Limit: int
        """
        self._DisasterRecoverGroupIds = None
        self._Name = None
        self._Offset = None
        self._Limit = None

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisasterRecoverGroupsResponse(AbstractModel):
    """DescribeDisasterRecoverGroups response structure.

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupSet: Information on spread placement groups.
        :type DisasterRecoverGroupSet: list of DisasterRecoverGroup
        :param _TotalCount: Total number of placement groups of the user.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DisasterRecoverGroupSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DisasterRecoverGroupSet(self):
        return self._DisasterRecoverGroupSet

    @DisasterRecoverGroupSet.setter
    def DisasterRecoverGroupSet(self, DisasterRecoverGroupSet):
        self._DisasterRecoverGroupSet = DisasterRecoverGroupSet

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
        if params.get("DisasterRecoverGroupSet") is not None:
            self._DisasterRecoverGroupSet = []
            for item in params.get("DisasterRecoverGroupSet"):
                obj = DisasterRecoverGroup()
                obj._deserialize(item)
                self._DisasterRecoverGroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostsRequest(AbstractModel):
    """DescribeHosts request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">Filter by the availability zone, such as `ap-guangzhou-1`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p><p style="padding-left: 30px;">Valid values: See <a href="https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1">Regions and Availability Zones</a></p>
<li><strong>project-id</strong></li>
<p style="padding-left: 30px;">Filter by the project ID. You can query the list of created projects by calling `DescribeProject` or logging in to the [CVM console](https://console.cloud.tencent.com/cvm/index). You can also call `AddProject` to create projects. The project ID is like 1002189. </p><p style="padding-left: 30px;">Type: Integer</p><p style="padding-left: 30px;">Optional</p>
<li><strong>host-id</strong></li>
<p style="padding-left: 30px;">Filter by the CDH instance ID. Format: host-xxxxxxxx. </p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>host-name</strong></li>
<p style="padding-left: 30px;">Filter by the host name.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>host-state</strong></li>
<p style="padding-left: 30px;">Filter by the CDH instance status. (`PENDING`: Creating | `LAUNCH_FAILURE`: Failed to create | `RUNNING`: Running | `EXPIRED`: Expired)</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
Each request can have up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Offset; default value: 0.
        :type Offset: int
        :param _Limit: Number of results returned; default value: 20; maximum: 100.
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

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
        


class DescribeHostsResponse(AbstractModel):
    """DescribeHosts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of CDH instances meeting the query conditions
        :type TotalCount: int
        :param _HostSet: Information on CDH instances
        :type HostSet: list of HostItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._HostSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HostSet(self):
        return self._HostSet

    @HostSet.setter
    def HostSet(self, HostSet):
        self._HostSet = HostSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("HostSet") is not None:
            self._HostSet = []
            for item in params.get("HostSet"):
                obj = HostItem()
                obj._deserialize(item)
                self._HostSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImageQuotaRequest(AbstractModel):
    """DescribeImageQuota request structure.

    """


class DescribeImageQuotaResponse(AbstractModel):
    """DescribeImageQuota response structure.

    """

    def __init__(self):
        r"""
        :param _ImageNumQuota: The image quota of an account
        :type ImageNumQuota: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImageNumQuota = None
        self._RequestId = None

    @property
    def ImageNumQuota(self):
        return self._ImageNumQuota

    @ImageNumQuota.setter
    def ImageNumQuota(self, ImageNumQuota):
        self._ImageNumQuota = ImageNumQuota

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageNumQuota = params.get("ImageNumQuota")
        self._RequestId = params.get("RequestId")


class DescribeImageSharePermissionRequest(AbstractModel):
    """DescribeImageSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param _ImageId: The ID of the image to be shared
        :type ImageId: str
        """
        self._ImageId = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSharePermissionResponse(AbstractModel):
    """DescribeImageSharePermission response structure.

    """

    def __init__(self):
        r"""
        :param _SharePermissionSet: Information on image sharing.
        :type SharePermissionSet: list of SharePermission
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SharePermissionSet = None
        self._RequestId = None

    @property
    def SharePermissionSet(self):
        return self._SharePermissionSet

    @SharePermissionSet.setter
    def SharePermissionSet(self, SharePermissionSet):
        self._SharePermissionSet = SharePermissionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SharePermissionSet") is not None:
            self._SharePermissionSet = []
            for item in params.get("SharePermissionSet"):
                obj = SharePermission()
                obj._deserialize(item)
                self._SharePermissionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages request structure.

    """

    def __init__(self):
        r"""
        :param _ImageIds: List of image IDs, such as `img-gvbnzy6f`. For the format of array-type parameters, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response. <br><li>View the image IDs in the [Image Console](https://console.cloud.tencent.com/cvm/image).
        :type ImageIds: list of str
        :param _Filters: Filters. Each request can have up to 10 `Filters`, and 5 `Filters.Values` for each filter. `ImageIds` and `Filters` cannot be specified at the same time. See details:

<li><strong>image-id</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>image ID</strong>.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>image-type</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>image type</strong>.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p><p style="padding-left: 30px;">Options:</p><p style="padding-left: 30px;">`PRIVATE_IMAGE`: Private images (images created by this account)</p><p style="padding-left: 30px;">`PUBLIC_IMAGE`: Public images (Tencent Cloud official images)</p><p style="padding-left: 30px;">`SHARED_IMAGE`: Shared images (images shared by other accounts to this account)</p>
<li><strong>image-name</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>image name</strong>.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>platform</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>image operating system</strong>, such as `CentOS`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>tag-key</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>tag key</strong>.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>tag-value</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>tag value</strong>.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
<li><strong>tag:tag-key</strong></li>
<p style="padding-left: 30px;">Filter by the <strong>tag key-value pair</strong>. Replace “tag-key” with the actual value. </p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
        :type Filters: list of Filter
        :param _Offset: Offset; default value: 0. For more information on `Offset`, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/568?from_cn_redirect=1#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).
        :type Offset: int
        :param _Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/568?from_cn_redirect=1#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).
        :type Limit: int
        :param _InstanceType: Instance type, e.g. `S1.SMALL1`
        :type InstanceType: str
        """
        self._ImageIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._InstanceType = None

    @property
    def ImageIds(self):
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

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
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages response structure.

    """

    def __init__(self):
        r"""
        :param _ImageSet: Information on an image, including its state and attributes.
        :type ImageSet: list of Image
        :param _TotalCount: Number of images meeting the filtering conditions.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImageSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ImageSet(self):
        return self._ImageSet

    @ImageSet.setter
    def ImageSet(self, ImageSet):
        self._ImageSet = ImageSet

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
        if params.get("ImageSet") is not None:
            self._ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self._ImageSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs request structure.

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs response structure.

    """

    def __init__(self):
        r"""
        :param _ImportImageOsListSupported: Supported operating system types of imported images.
        :type ImportImageOsListSupported: :class:`tencentcloud.cvm.v20170312.models.ImageOsList`
        :param _ImportImageOsVersionSet: Supported operating system versions of imported images. 
        :type ImportImageOsVersionSet: list of OsVersion
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImportImageOsListSupported = None
        self._ImportImageOsVersionSet = None
        self._RequestId = None

    @property
    def ImportImageOsListSupported(self):
        return self._ImportImageOsListSupported

    @ImportImageOsListSupported.setter
    def ImportImageOsListSupported(self, ImportImageOsListSupported):
        self._ImportImageOsListSupported = ImportImageOsListSupported

    @property
    def ImportImageOsVersionSet(self):
        return self._ImportImageOsVersionSet

    @ImportImageOsVersionSet.setter
    def ImportImageOsVersionSet(self, ImportImageOsVersionSet):
        self._ImportImageOsVersionSet = ImportImageOsVersionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImportImageOsListSupported") is not None:
            self._ImportImageOsListSupported = ImageOsList()
            self._ImportImageOsListSupported._deserialize(params.get("ImportImageOsListSupported"))
        if params.get("ImportImageOsVersionSet") is not None:
            self._ImportImageOsVersionSet = []
            for item in params.get("ImportImageOsVersionSet"):
                obj = OsVersion()
                obj._deserialize(item)
                self._ImportImageOsVersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceFamilyConfigsRequest(AbstractModel):
    """DescribeInstanceFamilyConfigs request structure.

    """


class DescribeInstanceFamilyConfigsResponse(AbstractModel):
    """DescribeInstanceFamilyConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyConfigSet: List of instance model families
        :type InstanceFamilyConfigSet: list of InstanceFamilyConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceFamilyConfigSet = None
        self._RequestId = None

    @property
    def InstanceFamilyConfigSet(self):
        return self._InstanceFamilyConfigSet

    @InstanceFamilyConfigSet.setter
    def InstanceFamilyConfigSet(self, InstanceFamilyConfigSet):
        self._InstanceFamilyConfigSet = InstanceFamilyConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfigSet") is not None:
            self._InstanceFamilyConfigSet = []
            for item in params.get("InstanceFamilyConfigSet"):
                obj = InstanceFamilyConfig()
                obj._deserialize(item)
                self._InstanceFamilyConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesOperationLimitRequest(AbstractModel):
    """DescribeInstancesOperationLimit request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Query by instance ID(s). You can obtain the instance IDs from the value of `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API. For example, instance ID: ins-xxxxxxxx. (For the specific format, refer to section `ids.N` of the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).) You can query up to 100 instances in each request.
        :type InstanceIds: list of str
        :param _Operation: Operation on the instance(s).
<li> INSTANCE_DEGRADE: downgrade the instance configurations</li>
        :type Operation: str
        """
        self._InstanceIds = None
        self._Operation = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesOperationLimitResponse(AbstractModel):
    """DescribeInstancesOperationLimit response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceOperationLimitSet: The maximum number of times you can modify the instance configurations (degrading the configurations)
        :type InstanceOperationLimitSet: list of OperationCountLimit
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceOperationLimitSet = None
        self._RequestId = None

    @property
    def InstanceOperationLimitSet(self):
        return self._InstanceOperationLimitSet

    @InstanceOperationLimitSet.setter
    def InstanceOperationLimitSet(self, InstanceOperationLimitSet):
        self._InstanceOperationLimitSet = InstanceOperationLimitSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceOperationLimitSet") is not None:
            self._InstanceOperationLimitSet = []
            for item in params.get("InstanceOperationLimitSet"):
                obj = OperationCountLimit()
                obj._deserialize(item)
                self._InstanceOperationLimitSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Query by instance ID(s). For example, instance ID: `ins-xxxxxxxx`. For the specific format, refer to section `Ids.N` of the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You can query up to 100 instances in each request. However, `InstanceIds` and `Filters` cannot be specified at the same time.
        :type InstanceIds: list of str
        :param _Filters: Filters
<li> `zone` - String - Optional - Filter by the availability zone.</li>
<li> `project-id` - Integer - Optional - Filter by the project ID. You can query the list of created projects by calling `DescribeProject` or logging in to the [CVM console](https://console.cloud.tencent.com/cvm/index). You can also call `AddProject` to create projects. </li>
<li> `host-id` - String - Optional - Filter by the CDH instance ID. Format: `host-xxxxxxxx`.</li>
</li>`vpc-id` - String - Optional - Filter by the VPC ID. Format: `vpc-xxxxxxxx`.</li>
<li> `subnet-id` - String - Optional - Filter by the subnet ID. Format: `subnet-xxxxxxxx`.</li>
</li>`instance-id` - String - Optional - Filter by the instance ID. Format: `ins-xxxxxxxx`.</li>
</li>`security-group-id` - String - Optional - Filter by the security group ID. Format: `sg-8jlk3f3r`.</li>
</li>`instance-name` - String - Optional - Filter by the instance name.</li>
</li>`instance-charge-type` - String - Optional - Filter by the instance billing method. `POSTPAID_BY_HOUR`: pay-as-you-go | `CDHPAID`: You are only billed for [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances, not the CVMs running on the [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances.</li>
</li>`private-ip-address` - String - Optional - Filter by the private IP address of the instance's primary ENI.</li>
</li>`public-ip-address` - String - Optional - Filter by the public IP address of the instance's primary ENI, including the IP addresses automatically assigned during the instance creation and the EIPs manually associated after the instance creation.</li>
<li> `tag-key` - String - Optional - Filter by the tag key.</li>
</li>`tag-value` - String - Optional - Filter by the tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter by the tag key-value pair. Replace `tag-key` with the actual tag keys. See example 2.</li>
Each request can have up to 10 `Filters` and 5 `Filters.Values`. You cannot specify `InstanceIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Offset: Offset; default value: 0. For more information on `Offset`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377).
        :type Offset: int
        :param _Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). 
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
        self._InstanceIds = params.get("InstanceIds")
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
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instances meeting the filtering conditions.
        :type TotalCount: int
        :param _InstanceSet: Detailed instance information.
        :type InstanceSet: list of Instance
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
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesStatusRequest(AbstractModel):
    """DescribeInstancesStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Query by instance ID(s). For example, instance ID: `ins-xxxxxxxx`. For the specific format, refer to section `Ids.N` of the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You can query up to 100 instances in each request.
        :type InstanceIds: list of str
        :param _Offset: Offset; default value: 0. For more information on `Offset`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377).
        :type Offset: int
        :param _Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377).
        :type Limit: int
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesStatusResponse(AbstractModel):
    """DescribeInstancesStatus response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instance states meeting the filtering conditions.
        :type TotalCount: int
        :param _InstanceStatusSet: [Instance status](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) list.
        :type InstanceStatusSet: list of InstanceStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceStatusSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceStatusSet(self):
        return self._InstanceStatusSet

    @InstanceStatusSet.setter
    def InstanceStatusSet(self, InstanceStatusSet):
        self._InstanceStatusSet = InstanceStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceStatusSet") is not None:
            self._InstanceStatusSet = []
            for item in params.get("InstanceStatusSet"):
                obj = InstanceStatus()
                obj._deserialize(item)
                self._InstanceStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInternetChargeTypeConfigsRequest(AbstractModel):
    """DescribeInternetChargeTypeConfigs request structure.

    """


class DescribeInternetChargeTypeConfigsResponse(AbstractModel):
    """DescribeInternetChargeTypeConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _InternetChargeTypeConfigSet: List of network billing methods.
        :type InternetChargeTypeConfigSet: list of InternetChargeTypeConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InternetChargeTypeConfigSet = None
        self._RequestId = None

    @property
    def InternetChargeTypeConfigSet(self):
        return self._InternetChargeTypeConfigSet

    @InternetChargeTypeConfigSet.setter
    def InternetChargeTypeConfigSet(self, InternetChargeTypeConfigSet):
        self._InternetChargeTypeConfigSet = InternetChargeTypeConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InternetChargeTypeConfigSet") is not None:
            self._InternetChargeTypeConfigSet = []
            for item in params.get("InternetChargeTypeConfigSet"):
                obj = InternetChargeTypeConfig()
                obj._deserialize(item)
                self._InternetChargeTypeConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKeyPairsRequest(AbstractModel):
    """DescribeKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: Key pair ID(s) in the format of `skey-11112222`. This API supports using multiple IDs as filters at the same time. For more information on the format of this parameter, see the `id.N` section in [API Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You cannot specify `KeyIds` and `Filters` at the same time. You can log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the key pair IDs.
        :type KeyIds: list of str
        :param _Filters: Filters
<li> `project-id` - Integer - Optional - Filter by project ID. To view the list of project IDs, you can go to [Project Management](https://console.cloud.tencent.com/project), or call the `DescribeProject` API and look for `projectId` in the response.</li>
<li> `key-name` - String - Optional - Filter by key pair name.</li>You cannot specify `KeyIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Offset: Offset; default value: 0. For more information on `Offset`, see the corresponding sections in API [Introduction](https://intl.cloud.tencent.com/document/product/377). Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). 
        :type Offset: int
        :param _Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). 
        :type Limit: int
        """
        self._KeyIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

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
        self._KeyIds = params.get("KeyIds")
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
        


class DescribeKeyPairsResponse(AbstractModel):
    """DescribeKeyPairs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of key pairs meeting the filtering conditions.
        :type TotalCount: int
        :param _KeyPairSet: Detailed information on key pairs.
        :type KeyPairSet: list of KeyPair
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._KeyPairSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KeyPairSet(self):
        return self._KeyPairSet

    @KeyPairSet.setter
    def KeyPairSet(self, KeyPairSet):
        self._KeyPairSet = KeyPairSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KeyPairSet") is not None:
            self._KeyPairSet = []
            for item in params.get("KeyPairSet"):
                obj = KeyPair()
                obj._deserialize(item)
                self._KeyPairSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLaunchTemplateVersionsRequest(AbstractModel):
    """DescribeLaunchTemplateVersions request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: The launch template ID
        :type LaunchTemplateId: str
        :param _LaunchTemplateVersions: List of instance launch templates.
        :type LaunchTemplateVersions: list of int non-negative
        :param _MinVersion: The minimum version number specified, which defaults to 0.
        :type MinVersion: int
        :param _MaxVersion: The maximum version number specified, which defaults to 30.
        :type MaxVersion: int
        :param _Offset: The offset. Default value: 0. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: The number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _DefaultVersion: Specify whether to query the default version. This parameter and `LaunchTemplateVersions` cannot be specified at the same time.
        :type DefaultVersion: bool
        """
        self._LaunchTemplateId = None
        self._LaunchTemplateVersions = None
        self._MinVersion = None
        self._MaxVersion = None
        self._Offset = None
        self._Limit = None
        self._DefaultVersion = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateVersions(self):
        return self._LaunchTemplateVersions

    @LaunchTemplateVersions.setter
    def LaunchTemplateVersions(self, LaunchTemplateVersions):
        self._LaunchTemplateVersions = LaunchTemplateVersions

    @property
    def MinVersion(self):
        return self._MinVersion

    @MinVersion.setter
    def MinVersion(self, MinVersion):
        self._MinVersion = MinVersion

    @property
    def MaxVersion(self):
        return self._MaxVersion

    @MaxVersion.setter
    def MaxVersion(self, MaxVersion):
        self._MaxVersion = MaxVersion

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
    def DefaultVersion(self):
        return self._DefaultVersion

    @DefaultVersion.setter
    def DefaultVersion(self, DefaultVersion):
        self._DefaultVersion = DefaultVersion


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateVersions = params.get("LaunchTemplateVersions")
        self._MinVersion = params.get("MinVersion")
        self._MaxVersion = params.get("MaxVersion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DefaultVersion = params.get("DefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLaunchTemplateVersionsResponse(AbstractModel):
    """DescribeLaunchTemplateVersions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instance launch templates.
        :type TotalCount: int
        :param _LaunchTemplateVersionSet: Set of instance launch template versions.
        :type LaunchTemplateVersionSet: list of LaunchTemplateVersionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LaunchTemplateVersionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LaunchTemplateVersionSet(self):
        return self._LaunchTemplateVersionSet

    @LaunchTemplateVersionSet.setter
    def LaunchTemplateVersionSet(self, LaunchTemplateVersionSet):
        self._LaunchTemplateVersionSet = LaunchTemplateVersionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LaunchTemplateVersionSet") is not None:
            self._LaunchTemplateVersionSet = []
            for item in params.get("LaunchTemplateVersionSet"):
                obj = LaunchTemplateVersionInfo()
                obj._deserialize(item)
                self._LaunchTemplateVersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLaunchTemplatesRequest(AbstractModel):
    """DescribeLaunchTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateIds: Instance launch template ID. ID of one or more instance launch templates. If not specified, all templates of the user will be displayed.
        :type LaunchTemplateIds: list of str
        :param _Filters: <p style="padding-left: 30px;">Filter by [<strong>LaunchTemplateName</strong>].</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
The maximum number of `Filters` in each request is 10. The upper limit for `Filter.Values` is 5. This parameter cannot specify `LaunchTemplateIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param _Offset: The offset. Default value: 0. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: The number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self._LaunchTemplateIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def LaunchTemplateIds(self):
        return self._LaunchTemplateIds

    @LaunchTemplateIds.setter
    def LaunchTemplateIds(self, LaunchTemplateIds):
        self._LaunchTemplateIds = LaunchTemplateIds

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
        self._LaunchTemplateIds = params.get("LaunchTemplateIds")
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
        


class DescribeLaunchTemplatesResponse(AbstractModel):
    """DescribeLaunchTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instance templates.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _LaunchTemplateSet: List of instance details
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateSet: list of LaunchTemplateInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LaunchTemplateSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LaunchTemplateSet(self):
        return self._LaunchTemplateSet

    @LaunchTemplateSet.setter
    def LaunchTemplateSet(self, LaunchTemplateSet):
        self._LaunchTemplateSet = LaunchTemplateSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LaunchTemplateSet") is not None:
            self._LaunchTemplateSet = []
            for item in params.get("LaunchTemplateSet"):
                obj = LaunchTemplateInfo()
                obj._deserialize(item)
                self._LaunchTemplateSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of regions
        :type TotalCount: int
        :param _RegionSet: List of regions
        :type RegionSet: list of RegionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReservedInstancesConfigInfosRequest(AbstractModel):
    """DescribeReservedInstancesConfigInfos request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: zone
Filters by the availability zones in which the reserved instance can be purchased, such as `ap-guangzhou-1`.
Type: String
Required: no
Valid values: list of regions/availability zones

product-description
Filters by the platform description (operating system) of the reserved instance, such as `linux`.
Type: String
Required: no
Valid value: linux

duration
Filters by the **validity** of the reserved instance, which is the purchased usage period. For example, `31536000`.
Type: Integer
Unit: second
Required: no
Valid value: 31536000 (1 year)
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesConfigInfosResponse(AbstractModel):
    """DescribeReservedInstancesConfigInfos response structure.

    """

    def __init__(self):
        r"""
        :param _ReservedInstanceConfigInfos: Static configurations of the reserved instance.
        :type ReservedInstanceConfigInfos: list of ReservedInstanceConfigInfoItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReservedInstanceConfigInfos = None
        self._RequestId = None

    @property
    def ReservedInstanceConfigInfos(self):
        return self._ReservedInstanceConfigInfos

    @ReservedInstanceConfigInfos.setter
    def ReservedInstanceConfigInfos(self, ReservedInstanceConfigInfos):
        self._ReservedInstanceConfigInfos = ReservedInstanceConfigInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReservedInstanceConfigInfos") is not None:
            self._ReservedInstanceConfigInfos = []
            for item in params.get("ReservedInstanceConfigInfos"):
                obj = ReservedInstanceConfigInfoItem()
                obj._deserialize(item)
                self._ReservedInstanceConfigInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReservedInstancesOfferingsRequest(AbstractModel):
    """DescribeReservedInstancesOfferings request structure.

    """

    def __init__(self):
        r"""
        :param _DryRun: Dry run. Default value: false.
        :type DryRun: bool
        :param _Offset: The offset. Default value: 0. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: The number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _MaxDuration: The maximum duration as a filter, 
in seconds.
Default value: 94608000.
        :type MaxDuration: int
        :param _MinDuration: The minimum duration as a filter, 
in seconds.
Default value: 2592000.
        :type MinDuration: int
        :param _Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">Filters by the <strong>availability zones</strong> in which the Reserved Instances can be purchased, such as ap-guangzhou-1.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: please see <a href="https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1">Availability Zones</a></p>
<li><strong>duration</strong></li>
<p style="padding-left: 30px;">Filters by the <strong>duration</strong> of the Reserved Instance, in seconds. For example, 31536000.</p><p style="padding-left: 30px;">Type: Integer</p><p style="padding-left: 30px;">Unit: second</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: 31536000 (1 year) | 94608000 (3 years)</p>
<li><strong>instance-type</strong></li>
<p style="padding-left: 30px;">Filters by <strong>type of the Reserved Instance</strong>, such as `S3.MEDIUM4`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: please see <a href="https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1">Instance Types</a></p>
<li><strong>offering-type</strong></li>
<p style="padding-left: 30px;">Filters by **<strong>payment term</strong>**, such as `All Upfront`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid value: All Upfront</p>
<li><strong>product-description</strong></li>
<p style="padding-left: 30px;">Filters by the <strong>platform description</strong> (operating system) of the Reserved Instance, such as `linux`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid value: linux</p>
<li><strong>reserved-instances-offering-id</strong></li>
<p style="padding-left: 30px;">Filters by <strong>Reserved Instance ID</strong>, in the form of 650c138f-ae7e-4750-952a-96841d6e9fc1.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p>
Each request can have up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        """
        self._DryRun = None
        self._Offset = None
        self._Limit = None
        self._MaxDuration = None
        self._MinDuration = None
        self._Filters = None

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

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
    def MaxDuration(self):
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def MinDuration(self):
        return self._MinDuration

    @MinDuration.setter
    def MinDuration(self, MinDuration):
        self._MinDuration = MinDuration

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DryRun = params.get("DryRun")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MaxDuration = params.get("MaxDuration")
        self._MinDuration = params.get("MinDuration")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesOfferingsResponse(AbstractModel):
    """DescribeReservedInstancesOfferings response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of Reserved Instances that meet the condition.
        :type TotalCount: int
        :param _ReservedInstancesOfferingsSet: The list of Reserved Instances that meet the condition.
        :type ReservedInstancesOfferingsSet: list of ReservedInstancesOffering
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ReservedInstancesOfferingsSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReservedInstancesOfferingsSet(self):
        return self._ReservedInstancesOfferingsSet

    @ReservedInstancesOfferingsSet.setter
    def ReservedInstancesOfferingsSet(self, ReservedInstancesOfferingsSet):
        self._ReservedInstancesOfferingsSet = ReservedInstancesOfferingsSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ReservedInstancesOfferingsSet") is not None:
            self._ReservedInstancesOfferingsSet = []
            for item in params.get("ReservedInstancesOfferingsSet"):
                obj = ReservedInstancesOffering()
                obj._deserialize(item)
                self._ReservedInstancesOfferingsSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeZoneInstanceConfigInfos request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: <li> instance-charge-type-String-required: no-(filter) billing mode of instances. (POSTPAID_BY_HOUR: pay-as-you-go billing by hour | SPOTPAID: spot billing, which is suitable for a [spot instance] (https://intl.cloud.Tencent.com/document/product/213/17817) | CDHPAID: CDH billing, that is, billing only for CDH, but not for the instances on CDH. )  </li>
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeZoneInstanceConfigInfos response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceTypeQuotaSet: List of model configurations for the availability zone.
        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceTypeQuotaSet = None
        self._RequestId = None

    @property
    def InstanceTypeQuotaSet(self):
        return self._InstanceTypeQuotaSet

    @InstanceTypeQuotaSet.setter
    def InstanceTypeQuotaSet(self, InstanceTypeQuotaSet):
        self._InstanceTypeQuotaSet = InstanceTypeQuotaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceTypeQuotaSet") is not None:
            self._InstanceTypeQuotaSet = []
            for item in params.get("InstanceTypeQuotaSet"):
                obj = InstanceTypeQuotaItem()
                obj._deserialize(item)
                self._InstanceTypeQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of availability zones.
        :type TotalCount: int
        :param _ZoneSet: List of availability zones.
        :type ZoneSet: list of ZoneInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). The maximum number of instances in each request is 100. <br><br>You can obtain the available instance IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the instance IDs. <br><li>Call [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceIds: list of str
        :param _KeyIds: List of key pair IDs. The maximum number of key pairs in each request is 100. The key pair ID is in the format of `skey-11112222`. <br><br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) and look for `KeyId` in the response.
        :type KeyIds: list of str
        :param _ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before disassociating a key pair from it. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE.
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._KeyIds = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._KeyIds = params.get("KeyIds")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs response structure.

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


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: ID of the security group to be disassociated, such as `sg-efil73jd`. Only one security group can be disassociated.
        :type SecurityGroupIds: list of str
        :param _InstanceIds: ID(s) of the instance(s) to be disassociated,such as `ins-lesecurk`. You can specify multiple instances.
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

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


class DisasterRecoverGroup(AbstractModel):
    """Information on disaster recovery groups

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupId: ID of a spread placement group.
        :type DisasterRecoverGroupId: str
        :param _Name: Name of a spread placement group, which must be 1-60 characters long.
        :type Name: str
        :param _Type: Type of a spread placement group. Valid values: <br><li>HOST: physical machine <br><li>SW: switch <br><li>RACK: rack.
        :type Type: str
        :param _CvmQuotaTotal: The maximum number of CVMs that can be hosted in a spread placement group.
        :type CvmQuotaTotal: int
        :param _CurrentNum: The current number of CVMs in a spread placement group.
        :type CurrentNum: int
        :param _InstanceIds: The list of CVM IDs in a spread placement group.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceIds: list of str
        :param _CreateTime: Creation time of a spread placement group.
Note: This field may return null, indicating that no valid value is found.
        :type CreateTime: str
        """
        self._DisasterRecoverGroupId = None
        self._Name = None
        self._Type = None
        self._CvmQuotaTotal = None
        self._CurrentNum = None
        self._InstanceIds = None
        self._CreateTime = None

    @property
    def DisasterRecoverGroupId(self):
        return self._DisasterRecoverGroupId

    @DisasterRecoverGroupId.setter
    def DisasterRecoverGroupId(self, DisasterRecoverGroupId):
        self._DisasterRecoverGroupId = DisasterRecoverGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CvmQuotaTotal(self):
        return self._CvmQuotaTotal

    @CvmQuotaTotal.setter
    def CvmQuotaTotal(self, CvmQuotaTotal):
        self._CvmQuotaTotal = CvmQuotaTotal

    @property
    def CurrentNum(self):
        return self._CurrentNum

    @CurrentNum.setter
    def CurrentNum(self, CurrentNum):
        self._CurrentNum = CurrentNum

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CvmQuotaTotal = params.get("CvmQuotaTotal")
        self._CurrentNum = params.get("CurrentNum")
        self._InstanceIds = params.get("InstanceIds")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnhancedService(AbstractModel):
    """Describes the configuration of enhanced services, such as Cloud Security and Cloud Monitor.

    """

    def __init__(self):
        r"""
        :param _SecurityService: Enables cloud security service. If this parameter is not specified, the cloud security service will be enabled by default.
        :type SecurityService: :class:`tencentcloud.cvm.v20170312.models.RunSecurityServiceEnabled`
        :param _MonitorService: Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.cvm.v20170312.models.RunMonitorServiceEnabled`
        :param _AutomationService: Whether to enable the TAT service. If this parameter is not specified, the TAT service is enabled for public images and disabled for other images by default.
        :type AutomationService: :class:`tencentcloud.cvm.v20170312.models.RunAutomationServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._AutomationService = None

    @property
    def SecurityService(self):
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def AutomationService(self):
        return self._AutomationService

    @AutomationService.setter
    def AutomationService(self, AutomationService):
        self._AutomationService = AutomationService


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = RunSecurityServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = RunMonitorServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self._AutomationService = RunAutomationServiceEnabled()
            self._AutomationService._deserialize(params.get("AutomationService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportImagesRequest(AbstractModel):
    """ExportImages request structure.

    """

    def __init__(self):
        r"""
        :param _BucketName: COS bucket name
        :type BucketName: str
        :param _ImageIds: List of image IDs
        :type ImageIds: list of str
        :param _ExportFormat: Format of the exported image file. Valid values: `RAW`, `QCOW2`, `VHD` and `VMDK`. Default value: `RAW`.
        :type ExportFormat: str
        :param _FileNamePrefixList: Prefix list of the name of exported files
        :type FileNamePrefixList: list of str
        :param _OnlyExportRootDisk: Whether to export only the system disk
        :type OnlyExportRootDisk: bool
        :param _DryRun: Check whether the image can be exported
        :type DryRun: bool
        :param _RoleName: Role name (Default: `CVM_QcsRole`). Before exporting the images, make sure the role exists, and it has write permission to COS.
        :type RoleName: str
        """
        self._BucketName = None
        self._ImageIds = None
        self._ExportFormat = None
        self._FileNamePrefixList = None
        self._OnlyExportRootDisk = None
        self._DryRun = None
        self._RoleName = None

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def ImageIds(self):
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

    @property
    def ExportFormat(self):
        return self._ExportFormat

    @ExportFormat.setter
    def ExportFormat(self, ExportFormat):
        self._ExportFormat = ExportFormat

    @property
    def FileNamePrefixList(self):
        return self._FileNamePrefixList

    @FileNamePrefixList.setter
    def FileNamePrefixList(self, FileNamePrefixList):
        self._FileNamePrefixList = FileNamePrefixList

    @property
    def OnlyExportRootDisk(self):
        return self._OnlyExportRootDisk

    @OnlyExportRootDisk.setter
    def OnlyExportRootDisk(self, OnlyExportRootDisk):
        self._OnlyExportRootDisk = OnlyExportRootDisk

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._ImageIds = params.get("ImageIds")
        self._ExportFormat = params.get("ExportFormat")
        self._FileNamePrefixList = params.get("FileNamePrefixList")
        self._OnlyExportRootDisk = params.get("OnlyExportRootDisk")
        self._DryRun = params.get("DryRun")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportImagesResponse(AbstractModel):
    """ExportImages response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the image export task
        :type TaskId: int
        :param _CosPaths: List of COS filenames of the exported images
        :type CosPaths: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._CosPaths = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CosPaths(self):
        return self._CosPaths

    @CosPaths.setter
    def CosPaths(self, CosPaths):
        self._CosPaths = CosPaths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._CosPaths = params.get("CosPaths")
        self._RequestId = params.get("RequestId")


class Externals(AbstractModel):
    """Additional data

    """

    def __init__(self):
        r"""
        :param _ReleaseAddress: Release address
Note: This field may return null, indicating that no valid value is found.
        :type ReleaseAddress: bool
        :param _UnsupportNetworks: Not supported network. Value: <br><li>BASIC: classic network<br><li>VPC1.0: VPC1.0
Note: This field may return null, indicating that no valid value was found.
        :type UnsupportNetworks: list of str
        :param _StorageBlockAttr: Attributes of local HDD storage
Note: This field may return null, indicating that no valid value is found.
        :type StorageBlockAttr: :class:`tencentcloud.cvm.v20170312.models.StorageBlock`
        """
        self._ReleaseAddress = None
        self._UnsupportNetworks = None
        self._StorageBlockAttr = None

    @property
    def ReleaseAddress(self):
        return self._ReleaseAddress

    @ReleaseAddress.setter
    def ReleaseAddress(self, ReleaseAddress):
        self._ReleaseAddress = ReleaseAddress

    @property
    def UnsupportNetworks(self):
        return self._UnsupportNetworks

    @UnsupportNetworks.setter
    def UnsupportNetworks(self, UnsupportNetworks):
        self._UnsupportNetworks = UnsupportNetworks

    @property
    def StorageBlockAttr(self):
        return self._StorageBlockAttr

    @StorageBlockAttr.setter
    def StorageBlockAttr(self, StorageBlockAttr):
        self._StorageBlockAttr = StorageBlockAttr


    def _deserialize(self, params):
        self._ReleaseAddress = params.get("ReleaseAddress")
        self._UnsupportNetworks = params.get("UnsupportNetworks")
        if params.get("StorageBlockAttr") is not None:
            self._StorageBlockAttr = StorageBlock()
            self._StorageBlockAttr._deserialize(params.get("StorageBlockAttr"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """> Key-value pair filters used for conditional queries, such as filtering results by ID, name, and state.
    > * If there are multiple `Filter` parameters, they are evaluated using the logical `AND` operator.
    > * If a `Filter` contains multiple `Values`, they are evaluated using the logical `OR` operator.
    >
    > Take [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) as an example. You can use the following filters to query the instances in availability zone (`zone`) Guangzhou Zone 1 ***and*** whose billing plan (`instance-charge-type`) is pay-as-you-go:
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        r"""
        :param _Name: Filters.
        :type Name: str
        :param _Values: Filter values.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GPUInfo(AbstractModel):
    """GPU information of the instance

    """

    def __init__(self):
        r"""
        :param _GPUCount: Number of GPUs. 
Note: this field may return `null`, indicating that no valid value can be found.
        :type GPUCount: float
        :param _GPUId: GPU address
Note: this field may return `null`, indicating that no valid value can be found.
        :type GPUId: list of str
        :param _GPUType: GPU type of the instance.
Note: this field may return `null`, indicating that no valid value can be found.
        :type GPUType: str
        """
        self._GPUCount = None
        self._GPUId = None
        self._GPUType = None

    @property
    def GPUCount(self):
        return self._GPUCount

    @GPUCount.setter
    def GPUCount(self, GPUCount):
        self._GPUCount = GPUCount

    @property
    def GPUId(self):
        return self._GPUId

    @GPUId.setter
    def GPUId(self, GPUId):
        self._GPUId = GPUId

    @property
    def GPUType(self):
        return self._GPUType

    @GPUType.setter
    def GPUType(self, GPUType):
        self._GPUType = GPUType


    def _deserialize(self, params):
        self._GPUCount = params.get("GPUCount")
        self._GPUId = params.get("GPUId")
        self._GPUType = params.get("GPUType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostItem(AbstractModel):
    """CDH instance details

    """

    def __init__(self):
        r"""
        :param _Placement: CDH instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _HostId: CDH instance ID
        :type HostId: str
        :param _HostType: CDH instance type
        :type HostType: str
        :param _HostName: CDH instance name
        :type HostName: str
        :param _HostChargeType: CDH instance billing mode
        :type HostChargeType: str
        :param _RenewFlag: CDH instance renewal flag
        :type RenewFlag: str
        :param _CreatedTime: CDH instance creation time
        :type CreatedTime: str
        :param _ExpiredTime: CDH instance expiry time
        :type ExpiredTime: str
        :param _InstanceIds: List of IDs of CVMs created on a CDH instance
        :type InstanceIds: list of str
        :param _HostState: CDH instance status
        :type HostState: str
        :param _HostIp: CDH instance IP
        :type HostIp: str
        :param _HostResource: CDH instance resource information
        :type HostResource: :class:`tencentcloud.cvm.v20170312.models.HostResource`
        :param _CageId: Cage ID of the CDH instance. This parameter is only valid for CDH instances in the cages of finance availability zones.
Note: This field may return null, indicating that no valid value is found.
        :type CageId: str
        """
        self._Placement = None
        self._HostId = None
        self._HostType = None
        self._HostName = None
        self._HostChargeType = None
        self._RenewFlag = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._InstanceIds = None
        self._HostState = None
        self._HostIp = None
        self._HostResource = None
        self._CageId = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def HostType(self):
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def HostChargeType(self):
        return self._HostChargeType

    @HostChargeType.setter
    def HostChargeType(self, HostChargeType):
        self._HostChargeType = HostChargeType

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def HostState(self):
        return self._HostState

    @HostState.setter
    def HostState(self, HostState):
        self._HostState = HostState

    @property
    def HostIp(self):
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def HostResource(self):
        return self._HostResource

    @HostResource.setter
    def HostResource(self, HostResource):
        self._HostResource = HostResource

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._HostId = params.get("HostId")
        self._HostType = params.get("HostType")
        self._HostName = params.get("HostName")
        self._HostChargeType = params.get("HostChargeType")
        self._RenewFlag = params.get("RenewFlag")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._InstanceIds = params.get("InstanceIds")
        self._HostState = params.get("HostState")
        self._HostIp = params.get("HostIp")
        if params.get("HostResource") is not None:
            self._HostResource = HostResource()
            self._HostResource._deserialize(params.get("HostResource"))
        self._CageId = params.get("CageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostResource(AbstractModel):
    """Resource information of the CDH instance

    """

    def __init__(self):
        r"""
        :param _CpuTotal: Total number of CPU cores in the CDH instance
        :type CpuTotal: int
        :param _CpuAvailable: Number of available CPU cores in the CDH instance
        :type CpuAvailable: int
        :param _MemTotal: Total memory size of the CDH instance (unit: GiB)
        :type MemTotal: float
        :param _MemAvailable: Available memory size of the CDH instance (unit: GiB)
        :type MemAvailable: float
        :param _DiskTotal: Total disk size of the CDH instance (unit: GiB)
        :type DiskTotal: int
        :param _DiskAvailable: Available disk size of the CDH instance (unit: GiB)
        :type DiskAvailable: int
        :param _DiskType: Disk type of the CDH instance
        :type DiskType: str
        :param _GpuTotal: Total number of GPU cards in the CDH instance
        :type GpuTotal: int
        :param _GpuAvailable: Number of available GPU cards in the CDH instance
        :type GpuAvailable: int
        """
        self._CpuTotal = None
        self._CpuAvailable = None
        self._MemTotal = None
        self._MemAvailable = None
        self._DiskTotal = None
        self._DiskAvailable = None
        self._DiskType = None
        self._GpuTotal = None
        self._GpuAvailable = None

    @property
    def CpuTotal(self):
        return self._CpuTotal

    @CpuTotal.setter
    def CpuTotal(self, CpuTotal):
        self._CpuTotal = CpuTotal

    @property
    def CpuAvailable(self):
        return self._CpuAvailable

    @CpuAvailable.setter
    def CpuAvailable(self, CpuAvailable):
        self._CpuAvailable = CpuAvailable

    @property
    def MemTotal(self):
        return self._MemTotal

    @MemTotal.setter
    def MemTotal(self, MemTotal):
        self._MemTotal = MemTotal

    @property
    def MemAvailable(self):
        return self._MemAvailable

    @MemAvailable.setter
    def MemAvailable(self, MemAvailable):
        self._MemAvailable = MemAvailable

    @property
    def DiskTotal(self):
        return self._DiskTotal

    @DiskTotal.setter
    def DiskTotal(self, DiskTotal):
        self._DiskTotal = DiskTotal

    @property
    def DiskAvailable(self):
        return self._DiskAvailable

    @DiskAvailable.setter
    def DiskAvailable(self, DiskAvailable):
        self._DiskAvailable = DiskAvailable

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def GpuTotal(self):
        return self._GpuTotal

    @GpuTotal.setter
    def GpuTotal(self, GpuTotal):
        self._GpuTotal = GpuTotal

    @property
    def GpuAvailable(self):
        return self._GpuAvailable

    @GpuAvailable.setter
    def GpuAvailable(self, GpuAvailable):
        self._GpuAvailable = GpuAvailable


    def _deserialize(self, params):
        self._CpuTotal = params.get("CpuTotal")
        self._CpuAvailable = params.get("CpuAvailable")
        self._MemTotal = params.get("MemTotal")
        self._MemAvailable = params.get("MemAvailable")
        self._DiskTotal = params.get("DiskTotal")
        self._DiskAvailable = params.get("DiskAvailable")
        self._DiskType = params.get("DiskType")
        self._GpuTotal = params.get("GpuTotal")
        self._GpuAvailable = params.get("GpuAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """Details about an image, including its state and attributes.

    """

    def __init__(self):
        r"""
        :param _ImageId: Image ID
        :type ImageId: str
        :param _OsName: Operating system of the image
        :type OsName: str
        :param _ImageType: Image type
        :type ImageType: str
        :param _CreatedTime: Creation time of the image
        :type CreatedTime: str
        :param _ImageName: Image name
        :type ImageName: str
        :param _ImageDescription: Image description
        :type ImageDescription: str
        :param _ImageSize: Image size
        :type ImageSize: int
        :param _Architecture: Image architecture
        :type Architecture: str
        :param _ImageState: Image state
        :type ImageState: str
        :param _Platform: Source platform of the image
        :type Platform: str
        :param _ImageCreator: Image creator
        :type ImageCreator: str
        :param _ImageSource: Image source
        :type ImageSource: str
        :param _SyncPercent: Synchronization percentage
Note: This field may return null, indicating that no valid value is found.
        :type SyncPercent: int
        :param _IsSupportCloudinit: Whether the image supports cloud-init
Note: This field may return null, indicating that no valid value is found.
        :type IsSupportCloudinit: bool
        :param _SnapshotSet: Information on the snapshots associated with the image
Note: This field may return null, indicating that no valid value is found.
        :type SnapshotSet: list of Snapshot
        :param _Tags: The list of tags bound to the image.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _LicenseType: Image license type
        :type LicenseType: str
        """
        self._ImageId = None
        self._OsName = None
        self._ImageType = None
        self._CreatedTime = None
        self._ImageName = None
        self._ImageDescription = None
        self._ImageSize = None
        self._Architecture = None
        self._ImageState = None
        self._Platform = None
        self._ImageCreator = None
        self._ImageSource = None
        self._SyncPercent = None
        self._IsSupportCloudinit = None
        self._SnapshotSet = None
        self._Tags = None
        self._LicenseType = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageDescription(self):
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def ImageSize(self):
        return self._ImageSize

    @ImageSize.setter
    def ImageSize(self, ImageSize):
        self._ImageSize = ImageSize

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def ImageState(self):
        return self._ImageState

    @ImageState.setter
    def ImageState(self, ImageState):
        self._ImageState = ImageState

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ImageCreator(self):
        return self._ImageCreator

    @ImageCreator.setter
    def ImageCreator(self, ImageCreator):
        self._ImageCreator = ImageCreator

    @property
    def ImageSource(self):
        return self._ImageSource

    @ImageSource.setter
    def ImageSource(self, ImageSource):
        self._ImageSource = ImageSource

    @property
    def SyncPercent(self):
        return self._SyncPercent

    @SyncPercent.setter
    def SyncPercent(self, SyncPercent):
        self._SyncPercent = SyncPercent

    @property
    def IsSupportCloudinit(self):
        return self._IsSupportCloudinit

    @IsSupportCloudinit.setter
    def IsSupportCloudinit(self, IsSupportCloudinit):
        self._IsSupportCloudinit = IsSupportCloudinit

    @property
    def SnapshotSet(self):
        return self._SnapshotSet

    @SnapshotSet.setter
    def SnapshotSet(self, SnapshotSet):
        self._SnapshotSet = SnapshotSet

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._OsName = params.get("OsName")
        self._ImageType = params.get("ImageType")
        self._CreatedTime = params.get("CreatedTime")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        self._ImageSize = params.get("ImageSize")
        self._Architecture = params.get("Architecture")
        self._ImageState = params.get("ImageState")
        self._Platform = params.get("Platform")
        self._ImageCreator = params.get("ImageCreator")
        self._ImageSource = params.get("ImageSource")
        self._SyncPercent = params.get("SyncPercent")
        self._IsSupportCloudinit = params.get("IsSupportCloudinit")
        if params.get("SnapshotSet") is not None:
            self._SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self._SnapshotSet.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOsList(AbstractModel):
    """Supported operating systems. They are divided into two categories, Windows and Linux.

    """

    def __init__(self):
        r"""
        :param _Windows: Supported Windows OS
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Windows: list of str
        :param _Linux: Supported Linux OS
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Linux: list of str
        """
        self._Windows = None
        self._Linux = None

    @property
    def Windows(self):
        return self._Windows

    @Windows.setter
    def Windows(self, Windows):
        self._Windows = Windows

    @property
    def Linux(self):
        return self._Linux

    @Linux.setter
    def Linux(self, Linux):
        self._Linux = Linux


    def _deserialize(self, params):
        self._Windows = params.get("Windows")
        self._Linux = params.get("Linux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageRequest(AbstractModel):
    """ImportImage request structure.

    """

    def __init__(self):
        r"""
        :param _Architecture: OS architecture of the image to be imported, `x86_64` or `i386`.
        :type Architecture: str
        :param _OsType: OS type of the image to be imported. You can call `DescribeImportImageOs` to obtain the list of supported operating systems.
        :type OsType: str
        :param _OsVersion: OS version of the image to be imported. You can call `DescribeImportImageOs` to obtain the list of supported operating systems.
        :type OsVersion: str
        :param _ImageUrl: Address on COS where the image to be imported is stored.
        :type ImageUrl: str
        :param _ImageName: Image name
        :type ImageName: str
        :param _ImageDescription: Image description
        :type ImageDescription: str
        :param _DryRun: Dry run to check the parameters without performing the operation
        :type DryRun: bool
        :param _Force: Whether to force import the image. For more information, see [Forcibly Import Image](https://intl.cloud.tencent.com/document/product/213/12849).
        :type Force: bool
        :param _TagSpecification: Tag description list. This parameter is used to bind a tag to a custom image.
        :type TagSpecification: list of TagSpecification
        :param _LicenseType: The license type used to activate the OS after importing an image.
Valid values:
`TencentCloud`: Tencent Cloud official license
`BYOL`: Bring Your Own License
        :type LicenseType: str
        :param _BootMode: Boot mode
        :type BootMode: str
        """
        self._Architecture = None
        self._OsType = None
        self._OsVersion = None
        self._ImageUrl = None
        self._ImageName = None
        self._ImageDescription = None
        self._DryRun = None
        self._Force = None
        self._TagSpecification = None
        self._LicenseType = None
        self._BootMode = None

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def OsType(self):
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OsVersion(self):
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageDescription(self):
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def BootMode(self):
        return self._BootMode

    @BootMode.setter
    def BootMode(self, BootMode):
        self._BootMode = BootMode


    def _deserialize(self, params):
        self._Architecture = params.get("Architecture")
        self._OsType = params.get("OsType")
        self._OsVersion = params.get("OsVersion")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        self._DryRun = params.get("DryRun")
        self._Force = params.get("Force")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._LicenseType = params.get("LicenseType")
        self._BootMode = params.get("BootMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageResponse(AbstractModel):
    """ImportImage response structure.

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


class ImportKeyPairRequest(AbstractModel):
    """ImportKeyPair request structure.

    """

    def __init__(self):
        r"""
        :param _KeyName: Key pair name, which can contain numbers, letters, and underscores, with a maximum length of 25 characters.
        :type KeyName: str
        :param _ProjectId: The project ID to which the key pair belongs after it is created. <br><br>You can obtain the project ID in the following ways: <br><li>Check the project list in the [Project management](https://console.cloud.tencent.com/project) page.<br><li>Call the `DescribeProject` API and view the `projectId` in the response.

If you want to use the default project, specify 0 for the parameter.
        :type ProjectId: int
        :param _PublicKey: Content of the public key in the key pair in the `OpenSSH RSA` format.
        :type PublicKey: str
        :param _TagSpecification: Tag description list. This parameter is used to bind a tag to a key pair.
        :type TagSpecification: list of TagSpecification
        """
        self._KeyName = None
        self._ProjectId = None
        self._PublicKey = None
        self._TagSpecification = None

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._ProjectId = params.get("ProjectId")
        self._PublicKey = params.get("PublicKey")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyPairResponse(AbstractModel):
    """ImportKeyPair response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Key pair ID
        :type KeyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class InquirePricePurchaseReservedInstancesOfferingRequest(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceCount: The number of the reserved instances you are purchasing.
        :type InstanceCount: int
        :param _ReservedInstancesOfferingId: The ID of the reserved instance offering.
        :type ReservedInstancesOfferingId: str
        :param _DryRun: Dry run.
        :type DryRun: bool
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.<br>For more information, see Ensuring Idempotency.
        :type ClientToken: str
        :param _ReservedInstanceName: Reserved instance name.<br><li>The RI name defaults to “unnamed” if this parameter is left empty.</li><li>You can enter any name within 60 characters (including the pattern string).</li>
        :type ReservedInstanceName: str
        """
        self._InstanceCount = None
        self._ReservedInstancesOfferingId = None
        self._DryRun = None
        self._ClientToken = None
        self._ReservedInstanceName = None

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def ReservedInstancesOfferingId(self):
        return self._ReservedInstancesOfferingId

    @ReservedInstancesOfferingId.setter
    def ReservedInstancesOfferingId(self, ReservedInstancesOfferingId):
        self._ReservedInstancesOfferingId = ReservedInstancesOfferingId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ReservedInstanceName(self):
        return self._ReservedInstanceName

    @ReservedInstanceName.setter
    def ReservedInstanceName(self, ReservedInstanceName):
        self._ReservedInstanceName = ReservedInstanceName


    def _deserialize(self, params):
        self._InstanceCount = params.get("InstanceCount")
        self._ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self._DryRun = params.get("DryRun")
        self._ClientToken = params.get("ClientToken")
        self._ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePricePurchaseReservedInstancesOfferingResponse(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price of the reserved instance with specified configuration.
        :type Price: :class:`tencentcloud.cvm.v20170312.models.ReservedInstancePrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = ReservedInstancePrice()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResetInstanceRequest(AbstractModel):
    """InquiryPriceResetInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param _ImageId: [Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For IDs of `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information; for IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
        :type ImageId: str
        :param _SystemDisk: Configuration of the system disk of the instance. For instances with a cloud disk as the system disk, you can expand the system disk by using this parameter to specify the new capacity after reinstallation. If the parameter is not specified, the system disk capacity remains unchanged by default. You can only expand the capacity of the system disk; reducing its capacity is not supported. When reinstalling the system, you can only modify the capacity of the system disk, not the type.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Monitor and Cloud Security. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        """
        self._InstanceId = None
        self._ImageId = None
        self._SystemDisk = None
        self._LoginSettings = None
        self._EnhancedService = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstanceResponse(AbstractModel):
    """InquiryPriceResetInstance response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price of reinstalling the instance with the specified configuration.
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100. When changing the bandwidth of instances with `BANDWIDTH_PREPAID` or `BANDWIDTH_POSTPAID_BY_HOUR` as the network billing method, you can only specify one instance at a time.
        :type InstanceIds: list of str
        :param _InternetAccessible: Configuration of public network egress bandwidth. The maximum bandwidth varies among different models. For more information, see the documentation on bandwidth limits. Currently only the `InternetMaxBandwidthOut` parameter is supported.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _StartTime: Date from which the new bandwidth takes effect. Format: `YYYY-MM-DD`, such as `2016-10-30`. The starting date cannot be earlier than the current date. If the starting date is the current date, the new bandwidth takes effect immediately. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned.
        :type StartTime: str
        :param _EndTime: Date until which the new bandwidth is effective. Format: `YYYY-MM-DD`, such as `2016-10-30`. The validity period of the new bandwidth covers the end date. The end date cannot be later than the expiration date of a prepaid instance. You can query the expiration time of an instance by calling [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728) and looking for `ExpiredTime` in the response. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned.
        :type EndTime: str
        """
        self._InstanceIds = None
        self._InternetAccessible = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

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


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price of the new bandwidth
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResetInstancesTypeRequest(AbstractModel):
    """InquiryPriceResetInstancesType request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). You can obtain the instance IDs from the value of `InstanceId` returned by the [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API. The maximum number of instances in each request is 1.
        :type InstanceIds: list of str
        :param _InstanceType: Instance model. Resources vary with the instance model. Specific values can be found in the tables of [Instance Types] (https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1) or in the latest specifications via the [DescribeInstanceTypeConfigs] (https://intl.cloud.tencent.com/document/product/213/15749?from_cn_redirect=1) API.
        :type InstanceType: str
        """
        self._InstanceIds = None
        self._InstanceType = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstancesTypeResponse(AbstractModel):
    """InquiryPriceResetInstancesType response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price of the instance using the specified model
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResizeInstanceDisksRequest(AbstractModel):
    """InquiryPriceResizeInstanceDisks request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param _DataDisks: The configuration of data disks to be expanded. Currently, you can only use the API to expand non-elastic data disks whose [disk type](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#DataDisk) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://intl.cloud.tencent.com/document/api/362/16315?from_cn_redirect=1) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is non-elastic. Data disk capacity unit: GB; minimum increment: 10 GB. For more information about selecting a data disk type, see the product overview on cloud disks. Available data disk types are subject to the instance type (`InstanceType`). In addition, the maximum capacity allowed for expansion varies by data disk type.
        :type DataDisks: list of DataDisk
        :param _ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally.
        :type ForceStop: bool
        """
        self._InstanceId = None
        self._DataDisks = None
        self._ForceStop = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResizeInstanceDisksResponse(AbstractModel):
    """InquiryPriceResizeInstanceDisks response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price of the disks after being expanded to the specified configurations
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRunInstancesRequest(AbstractModel):
    """InquiryPriceRunInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Placement: Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone and project.
 <b>Note: `Placement` is required when `LaunchTemplate` is not specified. If both the parameters are passed in, `Placement` prevails.</b>
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _ImageId: [Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images: <br/><li>Public images</li><li>Custom images</li><li>Shared images</li><br/>You can obtain the available image IDs in the following ways: <br/><li>For IDs of `public images`, `custom images`, and `shared images`, log in to the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information. </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
 <b>Note: `ImageId` is required when `LaunchTemplate` is not specified. If both the parameters are passed in, `ImageId` prevails.</b>
        :type ImageId: str
        :param _InstanceChargeType: The instance [billing method](https://intl.cloud.tencent.com/document/product/213/2180?from_cn_redirect=1).<br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis<br>Default value: POSTPAID_BY_HOUR.
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`. 
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _InstanceType: The instance model. Different resource specifications are specified for different models. For specific values, call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) to retrieve the latest specification list or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1). If the parameter is not specified, `S1.SMALL1` will be used by default.
        :type InstanceType: str
        :param _SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: Data disk configuration of the instance. If the parameter is not specified, no data disk will be purchased by default. If you want to purchase data disks, you can specify 21 data disks, including up to 1 `LOCAL_BASIC` data disk or `LOCAL_SSD` data disk and up to 20 `CLOUD_BASIC` data disks, `CLOUD_PREMIUM` data disks, or `CLOUD_SSD` data disks.
        :type DataDisks: list of DataDisk
        :param _VirtualPrivateCloud: VPC configurations (VPC ID, subnet ID, etc). If it’s not specified, the classic network will be used by default. If a VPC IP is specified in this parameter, the `InstanceCount` can only be 1.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _InternetAccessible: Configuration of public network bandwidth. If it’s not specified, 0 Mbps is used by default.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _InstanceCount: Number of instances to purchase. Value range: 1 (default) to 100. It cannot exceed the remaining CVM quota of the user. For more information on quota, see [Restrictions on CVM Instance Purchase](https://intl.cloud.tencent.com/document/product/213/2664).
        :type InstanceCount: int
        :param _InstanceName: Instance name (up to 60 characters)<br><li>If this parameter is not specified, **Unnamed** will be displayed by default. </li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`. </li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and the instance name body is `server_`, the instance names will be `server_1` and `server_2`. </li>
        :type InstanceName: str
        :param _LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance, or keep the original login settings of the image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will not be associated with any security group by default.
        :type SecurityGroupIds: list of str
        :param _EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.<br>For more information, see Ensuring Idempotency.
        :type ClientToken: str
        :param _HostName: Host name of the CVM. <br><li>Periods (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name.<br><li>Windows: 2-15 characters, containing [a-z], [A-Z], [0-9] and hyphens (-). Digit-only strings are not allowed.<br><li>For other instances, such as Linux instances, the host name must be 2-30 characters long. It supports multiple periods (.) and allows uppercase and lowercase letters, numbers, and hyphens (-) between any two periods (.).
        :type HostName: str
        :param _TagSpecification: The tag description list. This parameter is used to bind a tag to a resource instance. A tag can only be bound to CVM instances.
        :type TagSpecification: list of TagSpecification
        :param _InstanceMarketOptions: The market options of the instance.
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param _HpcClusterId: HPC cluster ID.
        :type HpcClusterId: str
        """
        self._Placement = None
        self._ImageId = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceCount = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._ClientToken = None
        self._HostName = None
        self._TagSpecification = None
        self._InstanceMarketOptions = None
        self._HpcClusterId = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ImageId = params.get("ImageId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._ClientToken = params.get("ClientToken")
        self._HostName = params.get("HostName")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._HpcClusterId = params.get("HpcClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRunInstancesResponse(AbstractModel):
    """InquiryPriceRunInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price of the instance with the specified configurations.
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Describes information on an instance

    """

    def __init__(self):
        r"""
        :param _Placement: Location of the instance
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _InstanceId: Instance `ID`
        :type InstanceId: str
        :param _InstanceType: Instance model
        :type InstanceType: str
        :param _CPU: Number of CPU cores of the instance; unit: core
        :type CPU: int
        :param _Memory: Memory capacity; unit: `GB`.
        :type Memory: int
        :param _RestrictState: Instance status. Valid values: <br><li>NORMAL: instance is normal. <br><li>EXPIRED: instance expired. <br><li>PROTECTIVELY_ISOLATED: instance is protectively isolated.
        :type RestrictState: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceChargeType: Instance billing plan. Valid values:<br><li>`POSTPAID_BY_HOUR`: pay after use. You are billed by the hour, by traffic.<br><li>`CDHPAID`: `CDH` billing plan. Applicable to `CDH` only, not the instances on the host.<br>
        :type InstanceChargeType: str
        :param _SystemDisk: Information on the system disk of the instance
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: Information of the instance data disks.
        :type DataDisks: list of DataDisk
        :param _PrivateIpAddresses: List of private IPs of the instance's primary ENI.
        :type PrivateIpAddresses: list of str
        :param _PublicIpAddresses: List of public IPs of the instance's primary ENI.
Note: This field may return null, indicating that no valid value is found.
        :type PublicIpAddresses: list of str
        :param _InternetAccessible: Information on instance bandwidth.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _VirtualPrivateCloud: Information on the VPC where the instance resides.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _ImageId: `ID` of the image used to create the instance.
        :type ImageId: str
        :param _RenewFlag: Auto renewal flag. Valid values: <br><li>`NOTIFY_AND_MANUAL_RENEW`: notify upon expiration, but do not renew automatically <br><li>`NOTIFY_AND_AUTO_RENEW`: notify upon expiration and renew automatically <br><li>`DISABLE_NOTIFY_AND_MANUAL_RENEW`: do not notify upon expiration and do not renew automatically.
<br><li>Note: this parameter is `null` for postpaid instances.
        :type RenewFlag: str
        :param _CreatedTime: Creation time following the `ISO8601` standard and using `UTC` time in the format of `YYYY-MM-DDThh:mm:ssZ`.
        :type CreatedTime: str
        :param _ExpiredTime: Expiration time in UTC format following the `ISO8601` standard: `YYYY-MM-DDThh:mm:ssZ`. Note: this parameter is `null` for postpaid instances.
        :type ExpiredTime: str
        :param _OsName: Operating system name.
        :type OsName: str
        :param _SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response.
        :type SecurityGroupIds: list of str
        :param _LoginSettings: Login settings of the instance. Currently only the key associated with the instance is returned.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _InstanceState: Instance state. Valid values: <br><li>PENDING: creating <br></li><li>LAUNCH_FAILED: creation failed <br></li><li>RUNNING: running <br></li><li>STOPPED: shut down <br></li><li>STARTING: starting <br></li><li>STOPPING: shutting down <br></li><li>REBOOTING: rebooting <br></li><li>SHUTDOWN: shut down and to be terminated <br></li><li>TERMINATING: terminating. <br></li>
        :type InstanceState: str
        :param _Tags: List of tags associated with the instance.
        :type Tags: list of Tag
        :param _StopChargingMode: Instance billing method after shutdown.
Valid values: <br><li>KEEP_CHARGING: billing continues after shutdown <br><li>STOP_CHARGING: billing stops after shutdown <li>NOT_APPLICABLE: the instance is not shut down or stopping billing after shutdown is not applicable to the instance. <br>
        :type StopChargingMode: str
        :param _Uuid: Globally unique ID of the instance.
        :type Uuid: str
        :param _LatestOperation: Last operation of the instance, such as StopInstances or ResetInstance.
        :type LatestOperation: str
        :param _LatestOperationState: The latest operation status of the instance. Valid values:<br><li>SUCCESS: operation succeeded<br><li>OPERATING: operation in progress<br><li>FAILED: operation failed
        :type LatestOperationState: str
        :param _LatestOperationRequestId: Unique request ID for the last operation of the instance.
        :type LatestOperationRequestId: str
        :param _DisasterRecoverGroupId: ID of a spread placement group.
Note: this field may return null, indicating that no valid value is obtained.
        :type DisasterRecoverGroupId: str
        :param _IPv6Addresses: IPv6 address of the instance.
Note: this field may return null, indicating that no valid value is obtained.
        :type IPv6Addresses: list of str
        :param _CamRoleName: CAM role name.
Note: this field may return null, indicating that no valid value is obtained.
        :type CamRoleName: str
        :param _HpcClusterId: HPC cluster ID.
Note: this field may return null, indicating that no valid value was found.
        :type HpcClusterId: str
        :param _RdmaIpAddresses: IP list of HPC cluster.
Note: this field may return null, indicating that no valid value was found.
        :type RdmaIpAddresses: list of str
        :param _IsolatedSource: The isolation status of the instance. Valid values:<br><li>`ARREAR`: isolated due to overdue payment;<br></li><li>`EXPIRE`: isolated upon expiration;<br></li><li>`MANMADE`: isolated after manual returning;<br></li><li>`NOTISOLATED`: not isolated<br></li>
Note: this field may return null, indicating that no valid value was found.
        :type IsolatedSource: str
        :param _GPUInfo: GPU information. This field is only returned for GPU instances.
Note: this field may return null, indicating that no valid value was found.
        :type GPUInfo: :class:`tencentcloud.cvm.v20170312.models.GPUInfo`
        :param _LicenseType: Instance OS license type. Default value: `TencentCloud`
        :type LicenseType: str
        :param _DisableApiTermination: Whether the termination protection is enabled. Values: <br><li>`TRUE`: Enable instance protection, which means that this instance can not be deleted by an API action.<br><li>`FALSE`: Do not enable the instance protection.<br><br>Default value: `FALSE`.
        :type DisableApiTermination: bool
        :param _DefaultLoginUser: Default login user
        :type DefaultLoginUser: str
        :param _DefaultLoginPort: Default login port
        :type DefaultLoginPort: int
        :param _LatestOperationErrorMsg: Latest operation errors of the instance.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LatestOperationErrorMsg: str
        """
        self._Placement = None
        self._InstanceId = None
        self._InstanceType = None
        self._CPU = None
        self._Memory = None
        self._RestrictState = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._PrivateIpAddresses = None
        self._PublicIpAddresses = None
        self._InternetAccessible = None
        self._VirtualPrivateCloud = None
        self._ImageId = None
        self._RenewFlag = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._OsName = None
        self._SecurityGroupIds = None
        self._LoginSettings = None
        self._InstanceState = None
        self._Tags = None
        self._StopChargingMode = None
        self._Uuid = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestId = None
        self._DisasterRecoverGroupId = None
        self._IPv6Addresses = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._RdmaIpAddresses = None
        self._IsolatedSource = None
        self._GPUInfo = None
        self._LicenseType = None
        self._DisableApiTermination = None
        self._DefaultLoginUser = None
        self._DefaultLoginPort = None
        self._LatestOperationErrorMsg = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def RestrictState(self):
        return self._RestrictState

    @RestrictState.setter
    def RestrictState(self, RestrictState):
        self._RestrictState = RestrictState

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def StopChargingMode(self):
        return self._StopChargingMode

    @StopChargingMode.setter
    def StopChargingMode(self, StopChargingMode):
        self._StopChargingMode = StopChargingMode

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def LatestOperation(self):
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestId(self):
        return self._LatestOperationRequestId

    @LatestOperationRequestId.setter
    def LatestOperationRequestId(self, LatestOperationRequestId):
        self._LatestOperationRequestId = LatestOperationRequestId

    @property
    def DisasterRecoverGroupId(self):
        return self._DisasterRecoverGroupId

    @DisasterRecoverGroupId.setter
    def DisasterRecoverGroupId(self, DisasterRecoverGroupId):
        self._DisasterRecoverGroupId = DisasterRecoverGroupId

    @property
    def IPv6Addresses(self):
        return self._IPv6Addresses

    @IPv6Addresses.setter
    def IPv6Addresses(self, IPv6Addresses):
        self._IPv6Addresses = IPv6Addresses

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def RdmaIpAddresses(self):
        return self._RdmaIpAddresses

    @RdmaIpAddresses.setter
    def RdmaIpAddresses(self, RdmaIpAddresses):
        self._RdmaIpAddresses = RdmaIpAddresses

    @property
    def IsolatedSource(self):
        return self._IsolatedSource

    @IsolatedSource.setter
    def IsolatedSource(self, IsolatedSource):
        self._IsolatedSource = IsolatedSource

    @property
    def GPUInfo(self):
        return self._GPUInfo

    @GPUInfo.setter
    def GPUInfo(self, GPUInfo):
        self._GPUInfo = GPUInfo

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination

    @property
    def DefaultLoginUser(self):
        return self._DefaultLoginUser

    @DefaultLoginUser.setter
    def DefaultLoginUser(self, DefaultLoginUser):
        self._DefaultLoginUser = DefaultLoginUser

    @property
    def DefaultLoginPort(self):
        return self._DefaultLoginPort

    @DefaultLoginPort.setter
    def DefaultLoginPort(self, DefaultLoginPort):
        self._DefaultLoginPort = DefaultLoginPort

    @property
    def LatestOperationErrorMsg(self):
        return self._LatestOperationErrorMsg

    @LatestOperationErrorMsg.setter
    def LatestOperationErrorMsg(self, LatestOperationErrorMsg):
        self._LatestOperationErrorMsg = LatestOperationErrorMsg


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceId = params.get("InstanceId")
        self._InstanceType = params.get("InstanceType")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._RestrictState = params.get("RestrictState")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ImageId = params.get("ImageId")
        self._RenewFlag = params.get("RenewFlag")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._OsName = params.get("OsName")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._InstanceState = params.get("InstanceState")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._StopChargingMode = params.get("StopChargingMode")
        self._Uuid = params.get("Uuid")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestId = params.get("LatestOperationRequestId")
        self._DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self._IPv6Addresses = params.get("IPv6Addresses")
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        self._RdmaIpAddresses = params.get("RdmaIpAddresses")
        self._IsolatedSource = params.get("IsolatedSource")
        if params.get("GPUInfo") is not None:
            self._GPUInfo = GPUInfo()
            self._GPUInfo._deserialize(params.get("GPUInfo"))
        self._LicenseType = params.get("LicenseType")
        self._DisableApiTermination = params.get("DisableApiTermination")
        self._DefaultLoginUser = params.get("DefaultLoginUser")
        self._DefaultLoginPort = params.get("DefaultLoginPort")
        self._LatestOperationErrorMsg = params.get("LatestOperationErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """Describes the billing method of an instance.

    """

    def __init__(self):
        r"""
        :param _Period: Subscription period (in month). Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, `36`, `48’, `60`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Period: int
        :param _RenewFlag: Auto-renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: Notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: Notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify upon expiration nor renew automatically <br><br>Default value: `NOTIFY_AND_MANUAL_RENEW`. When `NOTIFY_AND_AUTO_RENEW` is specified, the instance is automatically renewed on a monthly basis if the account has sufficient balance.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyConfig(AbstractModel):
    """Describes the model family of the instance.
    Examples: {'InstanceFamilyName': 'Standard S1', 'InstanceFamily': 'S1'}, {'InstanceFamilyName': 'Network-optimized N1', 'InstanceFamily': 'N1'}, {'InstanceFamilyName': 'High IO I1', 'InstanceFamily': 'I1'}, etc.

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyName: Full name of the model family.
        :type InstanceFamilyName: str
        :param _InstanceFamily: Acronym of the model family.
        :type InstanceFamily: str
        """
        self._InstanceFamilyName = None
        self._InstanceFamily = None

    @property
    def InstanceFamilyName(self):
        return self._InstanceFamilyName

    @InstanceFamilyName.setter
    def InstanceFamilyName(self, InstanceFamilyName):
        self._InstanceFamilyName = InstanceFamilyName

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily


    def _deserialize(self, params):
        self._InstanceFamilyName = params.get("InstanceFamilyName")
        self._InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMarketOptionsRequest(AbstractModel):
    """Options related to bidding requests

    """

    def __init__(self):
        r"""
        :param _SpotOptions: Spot-related options
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SpotOptions: :class:`tencentcloud.cvm.v20170312.models.SpotMarketOptions`
        :param _MarketType: Market type. Valid value: `spot`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MarketType: str
        """
        self._SpotOptions = None
        self._MarketType = None

    @property
    def SpotOptions(self):
        return self._SpotOptions

    @SpotOptions.setter
    def SpotOptions(self, SpotOptions):
        self._SpotOptions = SpotOptions

    @property
    def MarketType(self):
        return self._MarketType

    @MarketType.setter
    def MarketType(self, MarketType):
        self._MarketType = MarketType


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self._SpotOptions = SpotMarketOptions()
            self._SpotOptions._deserialize(params.get("SpotOptions"))
        self._MarketType = params.get("MarketType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStatus(AbstractModel):
    """Describes instance states. For state types, see [here](https://intl.cloud.tencent.com/document/api/213/15753?from_cn_redirect=1#InstanceStatus).

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance `ID`.
        :type InstanceId: str
        :param _InstanceState: The instance state. Valid values: <br><li>PENDING: creating<br></li><li>LAUNCH_FAILED: creation failed<br></li><li>RUNNING: running<br></li><li>STOPPED: shut down<br></li><li>STARTING: starting<br></li><li>STOPPING: shutting down<br></li><li>REBOOTING: rebooting<br></li><li>SHUTDOWN: shut down and to be terminated<br></li><li>TERMINATING: terminating.<br></li>
        :type InstanceState: str
        """
        self._InstanceId = None
        self._InstanceState = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceState = params.get("InstanceState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeQuotaItem(AbstractModel):
    """Describes instance model quota.

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone.
        :type Zone: str
        :param _InstanceType: Instance model.
        :type InstanceType: str
        :param _InstanceChargeType: Instance billing plan. Valid values: <br><li>POSTPAID_BY_HOUR: pay after use. You are billed for your traffic by the hour.<br><li>`CDHPAID`: [`CDH`](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) billing plan. Applicable to `CDH` only, not the instances on the host.
        :type InstanceChargeType: str
        :param _NetworkCard: ENI type. For example, 25 represents an ENI of 25 GB.
        :type NetworkCard: int
        :param _Externals: Additional data.
Note: This field may return null, indicating that no valid value is found.
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param _Cpu: Number of CPU cores of an instance model.
        :type Cpu: int
        :param _Memory: Instance memory capacity; unit: `GB`.
        :type Memory: int
        :param _InstanceFamily: Instance model family.
        :type InstanceFamily: str
        :param _TypeName: Model name.
        :type TypeName: str
        :param _LocalDiskTypeList: List of local disk specifications. If the parameter returns null, it means that local disks cannot be created.
        :type LocalDiskTypeList: list of LocalDiskType
        :param _Status: Whether an instance model is available. Valid values: <br><li>SELL: available <br><li>SOLD_OUT: sold out
        :type Status: str
        :param _Price: Price of an instance model.
        :type Price: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        :param _SoldOutReason: Details of out-of-stock items
Note: this field may return null, indicating that no valid value is obtained.
        :type SoldOutReason: str
        :param _InstanceBandwidth: Private network bandwidth, in Gbps.
        :type InstanceBandwidth: float
        :param _InstancePps: The max packet sending and receiving capability (in 10k PPS).
        :type InstancePps: int
        :param _StorageBlockAmount: Number of local storage blocks.
        :type StorageBlockAmount: int
        :param _CpuType: CPU type.
        :type CpuType: str
        :param _Gpu: Number of GPUs of the instance.
        :type Gpu: int
        :param _Fpga: Number of FPGAs of the instance.
        :type Fpga: int
        :param _Remark: Descriptive information of the instance.
        :type Remark: str
        :param _GpuCount: 
        :type GpuCount: float
        :param _Frequency: CPU clock rate of the instance
        :type Frequency: str
        """
        self._Zone = None
        self._InstanceType = None
        self._InstanceChargeType = None
        self._NetworkCard = None
        self._Externals = None
        self._Cpu = None
        self._Memory = None
        self._InstanceFamily = None
        self._TypeName = None
        self._LocalDiskTypeList = None
        self._Status = None
        self._Price = None
        self._SoldOutReason = None
        self._InstanceBandwidth = None
        self._InstancePps = None
        self._StorageBlockAmount = None
        self._CpuType = None
        self._Gpu = None
        self._Fpga = None
        self._Remark = None
        self._GpuCount = None
        self._Frequency = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def NetworkCard(self):
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard

    @property
    def Externals(self):
        return self._Externals

    @Externals.setter
    def Externals(self, Externals):
        self._Externals = Externals

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
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def LocalDiskTypeList(self):
        return self._LocalDiskTypeList

    @LocalDiskTypeList.setter
    def LocalDiskTypeList(self, LocalDiskTypeList):
        self._LocalDiskTypeList = LocalDiskTypeList

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def SoldOutReason(self):
        return self._SoldOutReason

    @SoldOutReason.setter
    def SoldOutReason(self, SoldOutReason):
        self._SoldOutReason = SoldOutReason

    @property
    def InstanceBandwidth(self):
        return self._InstanceBandwidth

    @InstanceBandwidth.setter
    def InstanceBandwidth(self, InstanceBandwidth):
        self._InstanceBandwidth = InstanceBandwidth

    @property
    def InstancePps(self):
        return self._InstancePps

    @InstancePps.setter
    def InstancePps(self, InstancePps):
        self._InstancePps = InstancePps

    @property
    def StorageBlockAmount(self):
        return self._StorageBlockAmount

    @StorageBlockAmount.setter
    def StorageBlockAmount(self, StorageBlockAmount):
        self._StorageBlockAmount = StorageBlockAmount

    @property
    def CpuType(self):
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Gpu(self):
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def Fpga(self):
        return self._Fpga

    @Fpga.setter
    def Fpga(self, Fpga):
        self._Fpga = Fpga

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def GpuCount(self):
        return self._GpuCount

    @GpuCount.setter
    def GpuCount(self, GpuCount):
        self._GpuCount = GpuCount

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._NetworkCard = params.get("NetworkCard")
        if params.get("Externals") is not None:
            self._Externals = Externals()
            self._Externals._deserialize(params.get("Externals"))
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._InstanceFamily = params.get("InstanceFamily")
        self._TypeName = params.get("TypeName")
        if params.get("LocalDiskTypeList") is not None:
            self._LocalDiskTypeList = []
            for item in params.get("LocalDiskTypeList"):
                obj = LocalDiskType()
                obj._deserialize(item)
                self._LocalDiskTypeList.append(obj)
        self._Status = params.get("Status")
        if params.get("Price") is not None:
            self._Price = ItemPrice()
            self._Price._deserialize(params.get("Price"))
        self._SoldOutReason = params.get("SoldOutReason")
        self._InstanceBandwidth = params.get("InstanceBandwidth")
        self._InstancePps = params.get("InstancePps")
        self._StorageBlockAmount = params.get("StorageBlockAmount")
        self._CpuType = params.get("CpuType")
        self._Gpu = params.get("Gpu")
        self._Fpga = params.get("Fpga")
        self._Remark = params.get("Remark")
        self._GpuCount = params.get("GpuCount")
        self._Frequency = params.get("Frequency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """Describes the accessibility of an instance in the public network, including its network billing method, maximum bandwidth, etc.

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: Network connection billing plan. Valid value: <br><li>TRAFFIC_POSTPAID_BY_HOUR: pay after use. You are billed for your traffic, by the hour.
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: The maximum outbound bandwidth of the public network, in Mbps. The default value is 0 Mbps. The upper limit of bandwidth varies for different models. For more information, see [Purchase Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/12523?from_cn_redirect=1).
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: Whether to assign a public IP. Valid values: <br><li>TRUE: Assign a public IP <br><li>FALSE: Do not assign a public IP <br><br>If the public network bandwidth is greater than 0 Mbps, you can choose whether to assign a public IP; by default a public IP will be assigned. If the public network bandwidth is 0 Mbps, you will not be able to assign a public IP.
        :type PublicIpAssigned: bool
        :param _BandwidthPackageId: Bandwidth package ID. To obatin the IDs, you can call [`DescribeBandwidthPackages`](https://intl.cloud.tencent.com/document/api/215/19209?from_cn_redirect=1) and look for the `BandwidthPackageId` fields in the response.
        :type BandwidthPackageId: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._PublicIpAssigned = None
        self._BandwidthPackageId = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetChargeTypeConfig(AbstractModel):
    """Describes network billing.

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: Network billing method.
        :type InternetChargeType: str
        :param _Description: Description of the network billing method.
        :type Description: str
        """
        self._InternetChargeType = None
        self._Description = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """Describes pricing information.

    """

    def __init__(self):
        r"""
        :param _UnitPrice: The original unit price for pay-as-you-go mode in USD. <br><li>When a billing tier is returned, it indicates the price fo the returned billing tier. For example, if `UnitPriceSecondStep` is returned, it refers to the unit price for the usage between 0 to 96 hours. Otherwise, it refers to that the unit price for unlimited usage.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPrice: float
        :param _ChargeUnit: Billing unit for pay-as-you-go mode. Valid values: <br><li>HOUR: billed on an hourly basis. It's used for hourly postpaid instances (`POSTPAID_BY_HOUR`). <br><li>GB: bill by traffic in GB. It's used for postpaid products that are billed by the hourly traffic (`TRAFFIC_POSTPAID_BY_HOUR`).
Note: this field may return null, indicating that no valid value is obtained.
        :type ChargeUnit: str
        :param _OriginalPrice: The original price of a pay-in-advance instance, in USD.
Note: this field may return null, indicating that no valid value is obtained.
        :type OriginalPrice: float
        :param _DiscountPrice: Discount price of a prepaid instance, in USD.
Note: this field may return null, indicating that no valid value is obtained.
        :type DiscountPrice: float
        :param _Discount: Percentage of the original price. For example, if you enter "20.0", the discounted price will be 20% of the original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Discount: float
        :param _UnitPriceDiscount: The discounted unit price for pay-as-you-go mode in USD. <br><li>When a billing tier is returned, it indicates the price fo the returned billing tier. For example, if `UnitPriceSecondStep` is returned, it refers to the unit price for the usage between 0 to 96 hours. Otherwise, it refers to that the unit price for unlimited usage.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceDiscount: float
        :param _UnitPriceSecondStep: Original unit price for the usage between 96 to 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceSecondStep: float
        :param _UnitPriceDiscountSecondStep: Discounted unit price for the usage between 96 to 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceDiscountSecondStep: float
        :param _UnitPriceThirdStep: Original unit price for the usage after 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceThirdStep: float
        :param _UnitPriceDiscountThirdStep: Discounted unit price for the usage after 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceDiscountThirdStep: float
        :param _OriginalPriceThreeYear: Original 3-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type OriginalPriceThreeYear: float
        :param _DiscountPriceThreeYear: Discounted 3-year upfront payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountPriceThreeYear: float
        :param _DiscountThreeYear: Discount for 3-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountThreeYear: float
        :param _OriginalPriceFiveYear: Original 5-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type OriginalPriceFiveYear: float
        :param _DiscountPriceFiveYear: Discounted 5-year upfront payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountPriceFiveYear: float
        :param _DiscountFiveYear: Discount for 5-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountFiveYear: float
        :param _OriginalPriceOneYear: Original 1-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type OriginalPriceOneYear: float
        :param _DiscountPriceOneYear: Discounted 1-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountPriceOneYear: float
        :param _DiscountOneYear: Discount for 1-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountOneYear: float
        """
        self._UnitPrice = None
        self._ChargeUnit = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Discount = None
        self._UnitPriceDiscount = None
        self._UnitPriceSecondStep = None
        self._UnitPriceDiscountSecondStep = None
        self._UnitPriceThirdStep = None
        self._UnitPriceDiscountThirdStep = None
        self._OriginalPriceThreeYear = None
        self._DiscountPriceThreeYear = None
        self._DiscountThreeYear = None
        self._OriginalPriceFiveYear = None
        self._DiscountPriceFiveYear = None
        self._DiscountFiveYear = None
        self._OriginalPriceOneYear = None
        self._DiscountPriceOneYear = None
        self._DiscountOneYear = None

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def UnitPriceSecondStep(self):
        return self._UnitPriceSecondStep

    @UnitPriceSecondStep.setter
    def UnitPriceSecondStep(self, UnitPriceSecondStep):
        self._UnitPriceSecondStep = UnitPriceSecondStep

    @property
    def UnitPriceDiscountSecondStep(self):
        return self._UnitPriceDiscountSecondStep

    @UnitPriceDiscountSecondStep.setter
    def UnitPriceDiscountSecondStep(self, UnitPriceDiscountSecondStep):
        self._UnitPriceDiscountSecondStep = UnitPriceDiscountSecondStep

    @property
    def UnitPriceThirdStep(self):
        return self._UnitPriceThirdStep

    @UnitPriceThirdStep.setter
    def UnitPriceThirdStep(self, UnitPriceThirdStep):
        self._UnitPriceThirdStep = UnitPriceThirdStep

    @property
    def UnitPriceDiscountThirdStep(self):
        return self._UnitPriceDiscountThirdStep

    @UnitPriceDiscountThirdStep.setter
    def UnitPriceDiscountThirdStep(self, UnitPriceDiscountThirdStep):
        self._UnitPriceDiscountThirdStep = UnitPriceDiscountThirdStep

    @property
    def OriginalPriceThreeYear(self):
        return self._OriginalPriceThreeYear

    @OriginalPriceThreeYear.setter
    def OriginalPriceThreeYear(self, OriginalPriceThreeYear):
        self._OriginalPriceThreeYear = OriginalPriceThreeYear

    @property
    def DiscountPriceThreeYear(self):
        return self._DiscountPriceThreeYear

    @DiscountPriceThreeYear.setter
    def DiscountPriceThreeYear(self, DiscountPriceThreeYear):
        self._DiscountPriceThreeYear = DiscountPriceThreeYear

    @property
    def DiscountThreeYear(self):
        return self._DiscountThreeYear

    @DiscountThreeYear.setter
    def DiscountThreeYear(self, DiscountThreeYear):
        self._DiscountThreeYear = DiscountThreeYear

    @property
    def OriginalPriceFiveYear(self):
        return self._OriginalPriceFiveYear

    @OriginalPriceFiveYear.setter
    def OriginalPriceFiveYear(self, OriginalPriceFiveYear):
        self._OriginalPriceFiveYear = OriginalPriceFiveYear

    @property
    def DiscountPriceFiveYear(self):
        return self._DiscountPriceFiveYear

    @DiscountPriceFiveYear.setter
    def DiscountPriceFiveYear(self, DiscountPriceFiveYear):
        self._DiscountPriceFiveYear = DiscountPriceFiveYear

    @property
    def DiscountFiveYear(self):
        return self._DiscountFiveYear

    @DiscountFiveYear.setter
    def DiscountFiveYear(self, DiscountFiveYear):
        self._DiscountFiveYear = DiscountFiveYear

    @property
    def OriginalPriceOneYear(self):
        return self._OriginalPriceOneYear

    @OriginalPriceOneYear.setter
    def OriginalPriceOneYear(self, OriginalPriceOneYear):
        self._OriginalPriceOneYear = OriginalPriceOneYear

    @property
    def DiscountPriceOneYear(self):
        return self._DiscountPriceOneYear

    @DiscountPriceOneYear.setter
    def DiscountPriceOneYear(self, DiscountPriceOneYear):
        self._DiscountPriceOneYear = DiscountPriceOneYear

    @property
    def DiscountOneYear(self):
        return self._DiscountOneYear

    @DiscountOneYear.setter
    def DiscountOneYear(self, DiscountOneYear):
        self._DiscountOneYear = DiscountOneYear


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._ChargeUnit = params.get("ChargeUnit")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Discount = params.get("Discount")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._UnitPriceSecondStep = params.get("UnitPriceSecondStep")
        self._UnitPriceDiscountSecondStep = params.get("UnitPriceDiscountSecondStep")
        self._UnitPriceThirdStep = params.get("UnitPriceThirdStep")
        self._UnitPriceDiscountThirdStep = params.get("UnitPriceDiscountThirdStep")
        self._OriginalPriceThreeYear = params.get("OriginalPriceThreeYear")
        self._DiscountPriceThreeYear = params.get("DiscountPriceThreeYear")
        self._DiscountThreeYear = params.get("DiscountThreeYear")
        self._OriginalPriceFiveYear = params.get("OriginalPriceFiveYear")
        self._DiscountPriceFiveYear = params.get("DiscountPriceFiveYear")
        self._DiscountFiveYear = params.get("DiscountFiveYear")
        self._OriginalPriceOneYear = params.get("OriginalPriceOneYear")
        self._DiscountPriceOneYear = params.get("DiscountPriceOneYear")
        self._DiscountOneYear = params.get("DiscountOneYear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPair(AbstractModel):
    """Describes key pair information.

    """

    def __init__(self):
        r"""
        :param _KeyId: Key pair `ID`, the unique identifier of a key pair.
        :type KeyId: str
        :param _KeyName: Key pair name.
        :type KeyName: str
        :param _ProjectId: `ID` of the project to which a key pair belongs.
        :type ProjectId: int
        :param _Description: Key pair description.
        :type Description: str
        :param _PublicKey: Content of public key in a key pair.
        :type PublicKey: str
        :param _PrivateKey: Content of private key in a key pair. Tencent Cloud do not keep private keys. Please keep it properly.
        :type PrivateKey: str
        :param _AssociatedInstanceIds: `ID` list of instances associated with a key.
        :type AssociatedInstanceIds: list of str
        :param _CreatedTime: Creation time, which follows the `ISO8601` standard and uses `UTC` time in the format of `YYYY-MM-DDThh:mm:ssZ`.
        :type CreatedTime: str
        :param _Tags: The list of tags bound to the key.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tags: list of Tag
        """
        self._KeyId = None
        self._KeyName = None
        self._ProjectId = None
        self._Description = None
        self._PublicKey = None
        self._PrivateKey = None
        self._AssociatedInstanceIds = None
        self._CreatedTime = None
        self._Tags = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def AssociatedInstanceIds(self):
        return self._AssociatedInstanceIds

    @AssociatedInstanceIds.setter
    def AssociatedInstanceIds(self, AssociatedInstanceIds):
        self._AssociatedInstanceIds = AssociatedInstanceIds

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyName = params.get("KeyName")
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._PublicKey = params.get("PublicKey")
        self._PrivateKey = params.get("PrivateKey")
        self._AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplate(AbstractModel):
    """Instance launch template. This parameter enables you to create an instance using the preset parameters in the template.

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: Instance launch template ID. This parameter enables you to create an instance using the preset parameters in the template.
        :type LaunchTemplateId: str
        :param _LaunchTemplateVersion: Instance launch template version number. If specified, this parameter will be used to create a new instance launch template.
        :type LaunchTemplateVersion: int
        """
        self._LaunchTemplateId = None
        self._LaunchTemplateVersion = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateVersion(self):
        return self._LaunchTemplateVersion

    @LaunchTemplateVersion.setter
    def LaunchTemplateVersion(self, LaunchTemplateVersion):
        self._LaunchTemplateVersion = LaunchTemplateVersion


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateInfo(AbstractModel):
    """Information of instance launch template.

    """

    def __init__(self):
        r"""
        :param _LatestVersionNumber: Instance launch template version number.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LatestVersionNumber: int
        :param _LaunchTemplateId: Instance launch template ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateId: str
        :param _LaunchTemplateName: Instance launch template name.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateName: str
        :param _DefaultVersionNumber: Default instance launch template version number.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DefaultVersionNumber: int
        :param _LaunchTemplateVersionCount: Total number of versions that the instance launch template contains.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateVersionCount: int
        :param _CreatedBy: UIN of the user who created the template.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreatedBy: str
        :param _CreationTime: Creation time of the template.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreationTime: str
        """
        self._LatestVersionNumber = None
        self._LaunchTemplateId = None
        self._LaunchTemplateName = None
        self._DefaultVersionNumber = None
        self._LaunchTemplateVersionCount = None
        self._CreatedBy = None
        self._CreationTime = None

    @property
    def LatestVersionNumber(self):
        return self._LatestVersionNumber

    @LatestVersionNumber.setter
    def LatestVersionNumber(self, LatestVersionNumber):
        self._LatestVersionNumber = LatestVersionNumber

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateName(self):
        return self._LaunchTemplateName

    @LaunchTemplateName.setter
    def LaunchTemplateName(self, LaunchTemplateName):
        self._LaunchTemplateName = LaunchTemplateName

    @property
    def DefaultVersionNumber(self):
        return self._DefaultVersionNumber

    @DefaultVersionNumber.setter
    def DefaultVersionNumber(self, DefaultVersionNumber):
        self._DefaultVersionNumber = DefaultVersionNumber

    @property
    def LaunchTemplateVersionCount(self):
        return self._LaunchTemplateVersionCount

    @LaunchTemplateVersionCount.setter
    def LaunchTemplateVersionCount(self, LaunchTemplateVersionCount):
        self._LaunchTemplateVersionCount = LaunchTemplateVersionCount

    @property
    def CreatedBy(self):
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime


    def _deserialize(self, params):
        self._LatestVersionNumber = params.get("LatestVersionNumber")
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateName = params.get("LaunchTemplateName")
        self._DefaultVersionNumber = params.get("DefaultVersionNumber")
        self._LaunchTemplateVersionCount = params.get("LaunchTemplateVersionCount")
        self._CreatedBy = params.get("CreatedBy")
        self._CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateVersionData(AbstractModel):
    """Information of instance launch template versions

    """

    def __init__(self):
        r"""
        :param _Placement: Location of the instance.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _InstanceType: Instance model.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _InstanceName: Instance name.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _InstanceChargeType: Instance billing mode. Valid values: <br><li>`POSTPAID_BY_HOUR`: postpaid for pay-as-you-go instances <br><li>`CDHPAID`: billed for CDH instances, not the CVMs running on the CDHs.<br>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceChargeType: str
        :param _SystemDisk: Instance system disk information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: Instance data disk information. This parameter only covers the data disks purchased together with the instance.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: Instance bandwidth information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _VirtualPrivateCloud: Information of the VPC where the instance resides.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _ImageId: `ID` of the image used to create the instance.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageId: str
        :param _SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroupIds: list of str
        :param _LoginSettings: Login settings of the instance. Currently, only the key associated with the instance is returned.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _CamRoleName: CAM role name.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CamRoleName: str
        :param _HpcClusterId: HPC cluster `ID`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HpcClusterId: str
        :param _InstanceCount: Number of instances purchased.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceCount: int
        :param _EnhancedService: Enhanced service.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _UserData: User data provided to the instance. This parameter needs to be encoded in base64 format with the maximum size of 16KB.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UserData: str
        :param _DisasterRecoverGroupIds: Placement group ID. You can only specify one.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DisasterRecoverGroupIds: list of str
        :param _ActionTimer: Scheduled tasks. You can use this parameter to specify scheduled tasks for the instance. Only scheduled termination is supported.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param _InstanceMarketOptions: Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param _HostName: Hostname of a CVM.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HostName: str
        :param _ClientToken: A string used to ensure the idempotency of the request.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClientToken: str
        :param _InstanceChargePrepaid: Prepaid mode. This parameter indicates relevant parameter settings for monthly-subscribed instances.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _TagSpecification: List of tag description. By specifying this parameter, the tag can be bound to the corresponding CVM and CBS instances at the same time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TagSpecification: list of TagSpecification
        :param _DisableApiTermination: Whether to enable termination protection. Valid values:

TRUE: Termination protection is enabled.
FALSE: Termination protection is disabled.

Default value: `FALSE`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DisableApiTermination: bool
        """
        self._Placement = None
        self._InstanceType = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._VirtualPrivateCloud = None
        self._ImageId = None
        self._SecurityGroupIds = None
        self._LoginSettings = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._InstanceCount = None
        self._EnhancedService = None
        self._UserData = None
        self._DisasterRecoverGroupIds = None
        self._ActionTimer = None
        self._InstanceMarketOptions = None
        self._HostName = None
        self._ClientToken = None
        self._InstanceChargePrepaid = None
        self._TagSpecification = None
        self._DisableApiTermination = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def ActionTimer(self):
        return self._ActionTimer

    @ActionTimer.setter
    def ActionTimer(self, ActionTimer):
        self._ActionTimer = ActionTimer

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceType = params.get("InstanceType")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ImageId = params.get("ImageId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        self._InstanceCount = params.get("InstanceCount")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._UserData = params.get("UserData")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("ActionTimer") is not None:
            self._ActionTimer = ActionTimer()
            self._ActionTimer._deserialize(params.get("ActionTimer"))
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._HostName = params.get("HostName")
        self._ClientToken = params.get("ClientToken")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateVersionInfo(AbstractModel):
    """Set of instance launch template versions.

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateVersion: Instance launch template version number.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateVersion: int
        :param _LaunchTemplateVersionData: Details of instance launch template versions.
        :type LaunchTemplateVersionData: :class:`tencentcloud.cvm.v20170312.models.LaunchTemplateVersionData`
        :param _CreationTime: Creation time of the instance launch template version.
        :type CreationTime: str
        :param _LaunchTemplateId: Instance launch template ID.
        :type LaunchTemplateId: str
        :param _IsDefaultVersion: Specifies whether it’s the default launch template version.
        :type IsDefaultVersion: bool
        :param _LaunchTemplateVersionDescription: Information of instance launch template version description.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateVersionDescription: str
        :param _CreatedBy: Creator account
        :type CreatedBy: str
        """
        self._LaunchTemplateVersion = None
        self._LaunchTemplateVersionData = None
        self._CreationTime = None
        self._LaunchTemplateId = None
        self._IsDefaultVersion = None
        self._LaunchTemplateVersionDescription = None
        self._CreatedBy = None

    @property
    def LaunchTemplateVersion(self):
        return self._LaunchTemplateVersion

    @LaunchTemplateVersion.setter
    def LaunchTemplateVersion(self, LaunchTemplateVersion):
        self._LaunchTemplateVersion = LaunchTemplateVersion

    @property
    def LaunchTemplateVersionData(self):
        return self._LaunchTemplateVersionData

    @LaunchTemplateVersionData.setter
    def LaunchTemplateVersionData(self, LaunchTemplateVersionData):
        self._LaunchTemplateVersionData = LaunchTemplateVersionData

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def IsDefaultVersion(self):
        return self._IsDefaultVersion

    @IsDefaultVersion.setter
    def IsDefaultVersion(self, IsDefaultVersion):
        self._IsDefaultVersion = IsDefaultVersion

    @property
    def LaunchTemplateVersionDescription(self):
        return self._LaunchTemplateVersionDescription

    @LaunchTemplateVersionDescription.setter
    def LaunchTemplateVersionDescription(self, LaunchTemplateVersionDescription):
        self._LaunchTemplateVersionDescription = LaunchTemplateVersionDescription

    @property
    def CreatedBy(self):
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy


    def _deserialize(self, params):
        self._LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        if params.get("LaunchTemplateVersionData") is not None:
            self._LaunchTemplateVersionData = LaunchTemplateVersionData()
            self._LaunchTemplateVersionData._deserialize(params.get("LaunchTemplateVersionData"))
        self._CreationTime = params.get("CreationTime")
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._IsDefaultVersion = params.get("IsDefaultVersion")
        self._LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self._CreatedBy = params.get("CreatedBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskType(AbstractModel):
    """Describes local disk specifications.

    """

    def __init__(self):
        r"""
        :param _Type: Type of a local disk.
        :type Type: str
        :param _PartitionType: Attributes of a local disk.
        :type PartitionType: str
        :param _MinSize: Minimum size of a local disk.
        :type MinSize: int
        :param _MaxSize: Maximum size of a local disk.
        :type MaxSize: int
        :param _Required: Whether a local disk is required during purchase. Valid values:<br><li>REQUIRED: required<br><li>OPTIONAL: optional
        :type Required: str
        """
        self._Type = None
        self._PartitionType = None
        self._MinSize = None
        self._MaxSize = None
        self._Required = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PartitionType(self):
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._PartitionType = params.get("PartitionType")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """Describes login settings of an instance.

    """

    def __init__(self):
        r"""
        :param _Password: Login password of the instance. <br><li>For Linux instances, the password must include 8-30 characters, and contain at least two of the following character sets: [a-z], [A-Z], [0-9] and [()\`~!@#$%^&*-+=|{}[]:;',.?/]. <br><li>For Windows instances, the password must include 12-30 characters, and contain at least three of the following character sets: [a-z], [A-Z], [0-9] and [()\`~!@#$%^&*-+=|{}[]:;',.?/]. <br><br>If it's not specified, the user needs to set the login password using the **Reset password** option in the CVM console or calling the API `ResetInstancesPassword` to complete the creation of the CVM instance(s).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Password: str
        :param _KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call [`DescribeKeyPairs`](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) to obtain `KeyId`. You cannot specify a key and a password at the same time. Windows instances do not support keys.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KeyIds: list of str
        :param _KeepImageLogin: Whether to keep the original settings of an image. You cannot specify this parameter and `Password` or `KeyIds.N` at the same time. You can specify this parameter as `TRUE` only when you create an instance using a custom image, a shared image, or an imported image. Valid values: <br><li>TRUE: keep the login settings of the image <br><li>FALSE: do not keep the login settings of the image <br><br>Default value: FALSE.
Note: This field may return null, indicating that no valid value is found.
        :type KeepImageLogin: str
        """
        self._Password = None
        self._KeyIds = None
        self._KeepImageLogin = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        return self._KeepImageLogin

    @KeepImageLogin.setter
    def KeepImageLogin(self, KeepImageLogin):
        self._KeepImageLogin = KeepImageLogin


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._KeyIds = params.get("KeyIds")
        self._KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChcAttributeRequest(AbstractModel):
    """ModifyChcAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC host IDs
        :type ChcIds: list of str
        :param _InstanceName: CHC host name
        :type InstanceName: str
        :param _DeviceType: Server type
        :type DeviceType: str
        :param _BmcUser: Valid characters: Letters, numbers, hyphens and underscores
        :type BmcUser: str
        :param _Password: The password can contain 8 to 16 characters, including letters, numbers and special symbols (()`~!@#$%^&*-+=_|{}).
        :type Password: str
        :param _BmcSecurityGroupIds: BMC network security group list
        :type BmcSecurityGroupIds: list of str
        """
        self._ChcIds = None
        self._InstanceName = None
        self._DeviceType = None
        self._BmcUser = None
        self._Password = None
        self._BmcSecurityGroupIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def BmcUser(self):
        return self._BmcUser

    @BmcUser.setter
    def BmcUser(self, BmcUser):
        self._BmcUser = BmcUser

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def BmcSecurityGroupIds(self):
        return self._BmcSecurityGroupIds

    @BmcSecurityGroupIds.setter
    def BmcSecurityGroupIds(self, BmcSecurityGroupIds):
        self._BmcSecurityGroupIds = BmcSecurityGroupIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        self._InstanceName = params.get("InstanceName")
        self._DeviceType = params.get("DeviceType")
        self._BmcUser = params.get("BmcUser")
        self._Password = params.get("Password")
        self._BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChcAttributeResponse(AbstractModel):
    """ModifyChcAttribute response structure.

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


class ModifyDisasterRecoverGroupAttributeRequest(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupId: Spread placement group ID, which can be obtained by calling the [DescribeDisasterRecoverGroups](https://intl.cloud.tencent.com/document/api/213/17810?from_cn_redirect=1) API.
        :type DisasterRecoverGroupId: str
        :param _Name: Name of a spread placement group. The name must be 1-60 characters long and can contain both Chinese characters and English letters.
        :type Name: str
        """
        self._DisasterRecoverGroupId = None
        self._Name = None

    @property
    def DisasterRecoverGroupId(self):
        return self._DisasterRecoverGroupId

    @DisasterRecoverGroupId.setter
    def DisasterRecoverGroupId(self, DisasterRecoverGroupId):
        self._DisasterRecoverGroupId = DisasterRecoverGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisasterRecoverGroupAttributeResponse(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute response structure.

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


class ModifyHostsAttributeRequest(AbstractModel):
    """ModifyHostsAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _HostIds: CDH instance ID(s).
        :type HostIds: list of str
        :param _HostName: CDH instance name to be displayed. You can specify any name you like, but its length cannot exceed 60 characters.
        :type HostName: str
        :param _RenewFlag: Auto renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify upon expiration nor renew automatically <br><br>If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis if the account balance is sufficient.
        :type RenewFlag: str
        :param _ProjectId: Project ID. You can use the `AddProject` API to create projects, and obtain the `projectId` field in the response of the `DescribeProject` API. When using the [DescribeHosts](https://intl.cloud.tencent.com/document/api/213/16474?from_cn_redirect=1) API to query instances later, you can filter the results by the project ID.
        :type ProjectId: int
        """
        self._HostIds = None
        self._HostName = None
        self._RenewFlag = None
        self._ProjectId = None

    @property
    def HostIds(self):
        return self._HostIds

    @HostIds.setter
    def HostIds(self, HostIds):
        self._HostIds = HostIds

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._HostIds = params.get("HostIds")
        self._HostName = params.get("HostName")
        self._RenewFlag = params.get("RenewFlag")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsAttributeResponse(AbstractModel):
    """ModifyHostsAttribute response structure.

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


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ImageId: Image ID such as `img-gvbnzy6f`. You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response. <br><li>Look for the information in the [Image Console](https://console.cloud.tencent.com/cvm/image).
        :type ImageId: str
        :param _ImageName: New image name, which must meet the following requirements: <br> <li>No more than 20 characters. <br> <li>Must be unique.
        :type ImageName: str
        :param _ImageDescription: New image description, which must meet the following requirement: <br> <li> No more than 60 characters.
        :type ImageDescription: str
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageDescription = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageDescription(self):
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute response structure.

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


class ModifyImageSharePermissionRequest(AbstractModel):
    """ModifyImageSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param _ImageId: Image ID such as `img-gvbnzy6f`. You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response. <br><li>Look for the information in the [Image Console](https://console.cloud.tencent.com/cvm/image). <br>You can only specify an image in the `NORMAL` state. For more information on image states, see [here](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#image_state).
        :type ImageId: str
        :param _AccountIds: List of account IDs with which an image is shared. For the format of array-type parameters, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/568?from_cn_redirect=1). The account ID is different from the QQ number. You can find the account ID in [Account Information](https://console.cloud.tencent.com/developer). 
        :type AccountIds: list of str
        :param _Permission: Operations. Valid values: `SHARE`, sharing an image; `CANCEL`, cancelling an image sharing. 
        :type Permission: str
        """
        self._ImageId = None
        self._AccountIds = None
        self._Permission = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def AccountIds(self):
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._AccountIds = params.get("AccountIds")
        self._Permission = params.get("Permission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageSharePermissionResponse(AbstractModel):
    """ModifyImageSharePermission response structure.

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


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param _InstanceName: The instance name, which can not exceed 60 characters
<dx-alert infotype="explain" title="">Either `InstanceName` or `SecurityGroups` must be specified, but they can not be both specified.</dx-alert>
        :type InstanceName: str
        :param _SecurityGroups: IDs of security groups associated with the specified instance. You can associate with a security group by adding its ID, or cancel the association with a security group by removing its ID. <dx-alert infotype="explain" title="">Either `InstanceName` or `SecurityGroups` must be specified, but they cannot be both set.</dx-alert>
        :type SecurityGroups: list of str
        :param _CamRoleName: The role bound with the instance. If it is not specified, it indicates to unbind the current role of the CVM.
        :type CamRoleName: str
        :param _HostName: Host name of the instance. <br><li>Hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name. <br><li>Windows: 2-15 characters, including [a-z], [A-Z], [0-9] and hyphens (-). Digit-only strings are not allowed. <br><li>Other OS: 2-60 characters, including [a-z], [A-Z], [0-9] and [.-]. Separate characters with dots. 
        :type HostName: str
        :param _DisableApiTermination: Whether the termination protection is enabled. Values: <br><li>`TRUE`: enable instance protection, which means that this instance can not be deleted by an API action.<br><li>`FALSE`: do not enable the instance protection.<br><br>Default Value: `FALSE`.
        :type DisableApiTermination: bool
        :param _CamRoleType: The role type, which is used in conjunction with `CamRoleName`. The value is obtained in `RoleType` field, returning by `CAM DescribeRoleList` and `GetRole` APIs. Valid value: `user`, `system` and `service_linked`.
For example, when `LinkedRoleIn` is contained in `CamRoleName` (such as `TKE_QCSLinkedRoleInPrometheusService`), the returned `RoleType` of `DescribeRoleList` and `GetRoleis` is `service_linked`, and the `CamRoleType` `service_linked`.
When the value obtained in `RoleType` is `user` (default) or `system`, `CamRoleType` can be left empty.
        :type CamRoleType: str
        """
        self._InstanceIds = None
        self._InstanceName = None
        self._SecurityGroups = None
        self._CamRoleName = None
        self._HostName = None
        self._DisableApiTermination = None
        self._CamRoleType = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SecurityGroups(self):
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination

    @property
    def CamRoleType(self):
        return self._CamRoleType

    @CamRoleType.setter
    def CamRoleType(self, CamRoleType):
        self._CamRoleType = CamRoleType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceName = params.get("InstanceName")
        self._SecurityGroups = params.get("SecurityGroups")
        self._CamRoleName = params.get("CamRoleName")
        self._HostName = params.get("HostName")
        self._DisableApiTermination = params.get("DisableApiTermination")
        self._CamRoleType = params.get("CamRoleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute response structure.

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


class ModifyInstancesProjectRequest(AbstractModel):
    """ModifyInstancesProject request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance IDs. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. You can operate up to 100 instances in each request.
        :type InstanceIds: list of str
        :param _ProjectId: Project ID. You can use the API `AddProject` to create projects, and obtain the `projectId` field in the response of the `DescribeProject` API. When using the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API to query instances later, you can filter the results by the project ID.
        :type ProjectId: int
        """
        self._InstanceIds = None
        self._ProjectId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesProjectResponse(AbstractModel):
    """ModifyInstancesProject response structure.

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


class ModifyInstancesVpcAttributeRequest(AbstractModel):
    """ModifyInstancesVpcAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceIds: list of str
        :param _VirtualPrivateCloud: VPC configurations. You can use this parameter to specify the VPC ID, subnet ID, VPC IP, etc. If the specified VPC ID and subnet ID (the subnet must be in the same availability zone as the instance) are different from the VPC where the specified instance resides, the instance will be migrated to a subnet of the specified VPC. You can use `PrivateIpAddresses` to specify the VPC subnet IP. If you want to specify the subnet IP, you will need to specify a subnet IP for each of the specified instances, and each `InstanceIds` will match a `PrivateIpAddresses`. If `PrivateIpAddresses` is not specified, the VPC subnet IP will be assigned randomly.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _ForceStop: Whether to force shut down a running instances. Default value: TRUE.
        :type ForceStop: bool
        :param _ReserveHostName: Whether to keep the host name. Default value: FALSE.
        :type ReserveHostName: bool
        """
        self._InstanceIds = None
        self._VirtualPrivateCloud = None
        self._ForceStop = None
        self._ReserveHostName = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def ReserveHostName(self):
        return self._ReserveHostName

    @ReserveHostName.setter
    def ReserveHostName(self, ReserveHostName):
        self._ReserveHostName = ReserveHostName


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ForceStop = params.get("ForceStop")
        self._ReserveHostName = params.get("ReserveHostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesVpcAttributeResponse(AbstractModel):
    """ModifyInstancesVpcAttribute response structure.

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


class ModifyKeyPairAttributeRequest(AbstractModel):
    """ModifyKeyPairAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Key pair ID in the format of `skey-xxxxxxxx`. <br><br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) and look for `KeyId` in the response.
        :type KeyId: str
        :param _KeyName: New key pair name, which can contain numbers, letters, and underscores, with a maximum length of 25 characters.
        :type KeyName: str
        :param _Description: New key pair description. You can specify any name you like, but its length cannot exceed 60 characters.
        :type Description: str
        """
        self._KeyId = None
        self._KeyName = None
        self._Description = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyName = params.get("KeyName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyKeyPairAttributeResponse(AbstractModel):
    """ModifyKeyPairAttribute response structure.

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


class ModifyLaunchTemplateDefaultVersionRequest(AbstractModel):
    """ModifyLaunchTemplateDefaultVersion request structure.

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: The launch template ID
        :type LaunchTemplateId: str
        :param _DefaultVersion: The number of the version that you want to set as the default version
        :type DefaultVersion: int
        """
        self._LaunchTemplateId = None
        self._DefaultVersion = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def DefaultVersion(self):
        return self._DefaultVersion

    @DefaultVersion.setter
    def DefaultVersion(self, DefaultVersion):
        self._DefaultVersion = DefaultVersion


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._DefaultVersion = params.get("DefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLaunchTemplateDefaultVersionResponse(AbstractModel):
    """ModifyLaunchTemplateDefaultVersion response structure.

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


class OperationCountLimit(AbstractModel):
    """Describes the maximum number of times you can perform an operation on a single instance.

    """

    def __init__(self):
        r"""
        :param _Operation: Instance operation. Valid values: <br><li>`INSTANCE_DEGRADE`: downgrade an instance<br><li>`INTERNET_CHARGE_TYPE_CHANGE`: modify the billing plan of the network connection
        :type Operation: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _CurrentCount: Number of operations already performed. If it returns `-1`, it means there is no limit on the times of the operation.
        :type CurrentCount: int
        :param _LimitCount: Maximum number of times you can perform an operation. If it returns `-1`, it means there is no limit on the times of the operation. If it returns `0`, it means that configuration modification is not supported.
        :type LimitCount: int
        """
        self._Operation = None
        self._InstanceId = None
        self._CurrentCount = None
        self._LimitCount = None

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CurrentCount(self):
        return self._CurrentCount

    @CurrentCount.setter
    def CurrentCount(self, CurrentCount):
        self._CurrentCount = CurrentCount

    @property
    def LimitCount(self):
        return self._LimitCount

    @LimitCount.setter
    def LimitCount(self, LimitCount):
        self._LimitCount = LimitCount


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._InstanceId = params.get("InstanceId")
        self._CurrentCount = params.get("CurrentCount")
        self._LimitCount = params.get("LimitCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsVersion(AbstractModel):
    """Supported operating system types.

    """

    def __init__(self):
        r"""
        :param _OsName: Operating system type
        :type OsName: str
        :param _OsVersions: Supported operating system versions
        :type OsVersions: list of str
        :param _Architecture: Supported operating system architecture
        :type Architecture: list of str
        """
        self._OsName = None
        self._OsVersions = None
        self._Architecture = None

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def OsVersions(self):
        return self._OsVersions

    @OsVersions.setter
    def OsVersions(self, OsVersions):
        self._OsVersions = OsVersions

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture


    def _deserialize(self, params):
        self._OsName = params.get("OsName")
        self._OsVersions = params.get("OsVersions")
        self._Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """Placement of an instance, including its availability zone, project, host (for CDH products only), master host IP, etc.

    """

    def __init__(self):
        r"""
        :param _Zone: ID of the availability zone where the instance resides. You can call the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/35071) API and obtain the ID in the returned `Zone` field.
        :type Zone: str
        :param _ProjectId: ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` returned by [DescribeProject](https://intl.cloud.tencent.com/document/api/651/78725?from_cn_redirect=1). If this is left empty, the default project is used.
        :type ProjectId: int
        :param _HostIds: ID list of CDHs from which the instance can be created. If you have purchased CDHs and specify this parameter, the instances you purchase will be randomly deployed on the CDHs.
        :type HostIds: list of str
        :param _HostIps: IPs of the hosts to create CVMs
        :type HostIps: list of str
        :param _HostId: The ID of the CDH to which the instance belongs, only used as an output parameter.
        :type HostId: str
        """
        self._Zone = None
        self._ProjectId = None
        self._HostIds = None
        self._HostIps = None
        self._HostId = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def HostIds(self):
        return self._HostIds

    @HostIds.setter
    def HostIds(self, HostIds):
        self._HostIds = HostIds

    @property
    def HostIps(self):
        return self._HostIps

    @HostIps.setter
    def HostIps(self, HostIps):
        self._HostIps = HostIps

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        self._HostIds = params.get("HostIds")
        self._HostIps = params.get("HostIps")
        self._HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """Price.

    """

    def __init__(self):
        r"""
        :param _InstancePrice: Instance price.
        :type InstancePrice: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        :param _BandwidthPrice: Network price.
        :type BandwidthPrice: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        """
        self._InstancePrice = None
        self._BandwidthPrice = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def BandwidthPrice(self):
        return self._BandwidthPrice

    @BandwidthPrice.setter
    def BandwidthPrice(self, BandwidthPrice):
        self._BandwidthPrice = BandwidthPrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = ItemPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self._BandwidthPrice = ItemPrice()
            self._BandwidthPrice._deserialize(params.get("BandwidthPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurchaseReservedInstancesOfferingRequest(AbstractModel):
    """PurchaseReservedInstancesOffering request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceCount: The number of the Reserved Instance you are purchasing.
        :type InstanceCount: int
        :param _ReservedInstancesOfferingId: The ID of the Reserved Instance.
        :type ReservedInstancesOfferingId: str
        :param _DryRun: Dry run
        :type DryRun: bool
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.<br>For more information, see Ensuring Idempotency.
        :type ClientToken: str
        :param _ReservedInstanceName: Reserved instance name.<br><li>The RI name defaults to “unnamed” if this parameter is left empty.</li><li>You can enter any name within 60 characters (including the pattern string).</li>
        :type ReservedInstanceName: str
        """
        self._InstanceCount = None
        self._ReservedInstancesOfferingId = None
        self._DryRun = None
        self._ClientToken = None
        self._ReservedInstanceName = None

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def ReservedInstancesOfferingId(self):
        return self._ReservedInstancesOfferingId

    @ReservedInstancesOfferingId.setter
    def ReservedInstancesOfferingId(self, ReservedInstancesOfferingId):
        self._ReservedInstancesOfferingId = ReservedInstancesOfferingId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ReservedInstanceName(self):
        return self._ReservedInstanceName

    @ReservedInstanceName.setter
    def ReservedInstanceName(self, ReservedInstanceName):
        self._ReservedInstanceName = ReservedInstanceName


    def _deserialize(self, params):
        self._InstanceCount = params.get("InstanceCount")
        self._ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self._DryRun = params.get("DryRun")
        self._ClientToken = params.get("ClientToken")
        self._ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurchaseReservedInstancesOfferingResponse(AbstractModel):
    """PurchaseReservedInstancesOffering response structure.

    """

    def __init__(self):
        r"""
        :param _ReservedInstanceId: The ID of the Reserved Instance purchased.
        :type ReservedInstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReservedInstanceId = None
        self._RequestId = None

    @property
    def ReservedInstanceId(self):
        return self._ReservedInstanceId

    @ReservedInstanceId.setter
    def ReservedInstanceId(self, ReservedInstanceId):
        self._ReservedInstanceId = ReservedInstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReservedInstanceId = params.get("ReservedInstanceId")
        self._RequestId = params.get("RequestId")


class RebootInstancesRequest(AbstractModel):
    """RebootInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance IDs. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. You can operate up to 100 instances in each request.
        :type InstanceIds: list of str
        :param _ForceReboot: Whether to forcibly restart an instance after a normal restart fails. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default value: `FALSE`. This parameter has been disused. We recommend using `StopType` instead. Note that `ForceReboot` and `StopType` parameters cannot be specified at the same time.
        :type ForceReboot: bool
        :param _StopType: Shutdown type. Valid values: <br><li>SOFT: soft shutdown<br><li>HARD: hard shutdown<br><li>SOFT_FIRST: perform a soft shutdown first, and perform a hard shutdown if the soft shutdown fails<br><br>Default value: SOFT.
        :type StopType: str
        """
        self._InstanceIds = None
        self._ForceReboot = None
        self._StopType = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ForceReboot(self):
        return self._ForceReboot

    @ForceReboot.setter
    def ForceReboot(self, ForceReboot):
        self._ForceReboot = ForceReboot

    @property
    def StopType(self):
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ForceReboot = params.get("ForceReboot")
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances response structure.

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


class RegionInfo(AbstractModel):
    """Region information.

    """

    def __init__(self):
        r"""
        :param _Region: Region name, such as `ap-guangzhou`
        :type Region: str
        :param _RegionName: Region description, such as South China (Guangzhou)
        :type RegionName: str
        :param _RegionState: Whether the region is available
        :type RegionState: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcAssistVpcRequest(AbstractModel):
    """RemoveChcAssistVpc request structure.

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC ID
        :type ChcIds: list of str
        """
        self._ChcIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcAssistVpcResponse(AbstractModel):
    """RemoveChcAssistVpc response structure.

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


class RemoveChcDeployVpcRequest(AbstractModel):
    """RemoveChcDeployVpc request structure.

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC ID
        :type ChcIds: list of str
        """
        self._ChcIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcDeployVpcResponse(AbstractModel):
    """RemoveChcDeployVpc response structure.

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


class ReservedInstanceConfigInfoItem(AbstractModel):
    """Static configurations of the reserved instance. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param _Type: Abbreviation name of the instance type.
        :type Type: str
        :param _TypeName: Full name of the instance type.
        :type TypeName: str
        :param _Order: Priority.
        :type Order: int
        :param _InstanceFamilies: List of instance families.
        :type InstanceFamilies: list of ReservedInstanceFamilyItem
        """
        self._Type = None
        self._TypeName = None
        self._Order = None
        self._InstanceFamilies = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def InstanceFamilies(self):
        return self._InstanceFamilies

    @InstanceFamilies.setter
    def InstanceFamilies(self, InstanceFamilies):
        self._InstanceFamilies = InstanceFamilies


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TypeName = params.get("TypeName")
        self._Order = params.get("Order")
        if params.get("InstanceFamilies") is not None:
            self._InstanceFamilies = []
            for item in params.get("InstanceFamilies"):
                obj = ReservedInstanceFamilyItem()
                obj._deserialize(item)
                self._InstanceFamilies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstanceFamilyItem(AbstractModel):
    """RI-related instance family. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param _InstanceFamily: Instance family.
        :type InstanceFamily: str
        :param _Order: Priority.
        :type Order: int
        :param _InstanceTypes: List of instance types.
        :type InstanceTypes: list of ReservedInstanceTypeItem
        """
        self._InstanceFamily = None
        self._Order = None
        self._InstanceTypes = None

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes


    def _deserialize(self, params):
        self._InstanceFamily = params.get("InstanceFamily")
        self._Order = params.get("Order")
        if params.get("InstanceTypes") is not None:
            self._InstanceTypes = []
            for item in params.get("InstanceTypes"):
                obj = ReservedInstanceTypeItem()
                obj._deserialize(item)
                self._InstanceTypes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancePrice(AbstractModel):
    """Price of the reserved instance. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param _OriginalFixedPrice: Original upfront payment, in USD.
        :type OriginalFixedPrice: float
        :param _DiscountFixedPrice: Discounted upfront payment, in USD.
        :type DiscountFixedPrice: float
        :param _OriginalUsagePrice: Original subsequent unit price, in USD/hr.
        :type OriginalUsagePrice: float
        :param _DiscountUsagePrice: Discounted subsequent unit price, in USD/hr.
        :type DiscountUsagePrice: float
        """
        self._OriginalFixedPrice = None
        self._DiscountFixedPrice = None
        self._OriginalUsagePrice = None
        self._DiscountUsagePrice = None

    @property
    def OriginalFixedPrice(self):
        return self._OriginalFixedPrice

    @OriginalFixedPrice.setter
    def OriginalFixedPrice(self, OriginalFixedPrice):
        self._OriginalFixedPrice = OriginalFixedPrice

    @property
    def DiscountFixedPrice(self):
        return self._DiscountFixedPrice

    @DiscountFixedPrice.setter
    def DiscountFixedPrice(self, DiscountFixedPrice):
        self._DiscountFixedPrice = DiscountFixedPrice

    @property
    def OriginalUsagePrice(self):
        return self._OriginalUsagePrice

    @OriginalUsagePrice.setter
    def OriginalUsagePrice(self, OriginalUsagePrice):
        self._OriginalUsagePrice = OriginalUsagePrice

    @property
    def DiscountUsagePrice(self):
        return self._DiscountUsagePrice

    @DiscountUsagePrice.setter
    def DiscountUsagePrice(self, DiscountUsagePrice):
        self._DiscountUsagePrice = DiscountUsagePrice


    def _deserialize(self, params):
        self._OriginalFixedPrice = params.get("OriginalFixedPrice")
        self._DiscountFixedPrice = params.get("DiscountFixedPrice")
        self._OriginalUsagePrice = params.get("OriginalUsagePrice")
        self._DiscountUsagePrice = params.get("DiscountUsagePrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancePriceItem(AbstractModel):
    """Price information of the reserved instance based on the payment method. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param _OfferingType: Payment method. Valid values: All Upfront, Partial Upfront, and No Upfront.
        :type OfferingType: str
        :param _FixedPrice: Upfront payment, in USD.
        :type FixedPrice: float
        :param _UsagePrice: Subsequent unit price, in USD/hr.
        :type UsagePrice: float
        :param _ReservedInstancesOfferingId: The ID of the reserved instance offering.
        :type ReservedInstancesOfferingId: str
        :param _Zone: The availability zone in which the reserved instance can be purchased.
        :type Zone: str
        :param _Duration: The **validity** of the reserved instance in seconds, which is the purchased usage period. For example, `31536000`.
Unit: second
        :type Duration: int
        :param _ProductDescription: The operating system of the reserved instance, such as `Linux`.
Valid value: `Linux`.
        :type ProductDescription: str
        """
        self._OfferingType = None
        self._FixedPrice = None
        self._UsagePrice = None
        self._ReservedInstancesOfferingId = None
        self._Zone = None
        self._Duration = None
        self._ProductDescription = None

    @property
    def OfferingType(self):
        return self._OfferingType

    @OfferingType.setter
    def OfferingType(self, OfferingType):
        self._OfferingType = OfferingType

    @property
    def FixedPrice(self):
        return self._FixedPrice

    @FixedPrice.setter
    def FixedPrice(self, FixedPrice):
        self._FixedPrice = FixedPrice

    @property
    def UsagePrice(self):
        return self._UsagePrice

    @UsagePrice.setter
    def UsagePrice(self, UsagePrice):
        self._UsagePrice = UsagePrice

    @property
    def ReservedInstancesOfferingId(self):
        return self._ReservedInstancesOfferingId

    @ReservedInstancesOfferingId.setter
    def ReservedInstancesOfferingId(self, ReservedInstancesOfferingId):
        self._ReservedInstancesOfferingId = ReservedInstancesOfferingId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription


    def _deserialize(self, params):
        self._OfferingType = params.get("OfferingType")
        self._FixedPrice = params.get("FixedPrice")
        self._UsagePrice = params.get("UsagePrice")
        self._ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self._Zone = params.get("Zone")
        self._Duration = params.get("Duration")
        self._ProductDescription = params.get("ProductDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstanceTypeItem(AbstractModel):
    """Reserved instance specification. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param _InstanceType: Instance type.
        :type InstanceType: str
        :param _Cpu: Number of CPU cores.
        :type Cpu: int
        :param _Memory: Memory size.
        :type Memory: int
        :param _Gpu: Number of GPUs.
        :type Gpu: int
        :param _Fpga: Number of FPGAs.
        :type Fpga: int
        :param _StorageBlock: Number of local storage blocks.
        :type StorageBlock: int
        :param _NetworkCard: Number of NICs.
        :type NetworkCard: int
        :param _MaxBandwidth: Maximum bandwidth.
        :type MaxBandwidth: float
        :param _Frequency: CPU frequency.
        :type Frequency: str
        :param _CpuModelName: CPU type.
        :type CpuModelName: str
        :param _Pps: Packet forwarding rate.
        :type Pps: int
        :param _Externals: Other information.
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param _Remark: Remarks.
        :type Remark: str
        :param _Prices: Price information about the reserved instance.
        :type Prices: list of ReservedInstancePriceItem
        """
        self._InstanceType = None
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._Fpga = None
        self._StorageBlock = None
        self._NetworkCard = None
        self._MaxBandwidth = None
        self._Frequency = None
        self._CpuModelName = None
        self._Pps = None
        self._Externals = None
        self._Remark = None
        self._Prices = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

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
    def Gpu(self):
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def Fpga(self):
        return self._Fpga

    @Fpga.setter
    def Fpga(self, Fpga):
        self._Fpga = Fpga

    @property
    def StorageBlock(self):
        return self._StorageBlock

    @StorageBlock.setter
    def StorageBlock(self, StorageBlock):
        self._StorageBlock = StorageBlock

    @property
    def NetworkCard(self):
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard

    @property
    def MaxBandwidth(self):
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def CpuModelName(self):
        return self._CpuModelName

    @CpuModelName.setter
    def CpuModelName(self, CpuModelName):
        self._CpuModelName = CpuModelName

    @property
    def Pps(self):
        return self._Pps

    @Pps.setter
    def Pps(self, Pps):
        self._Pps = Pps

    @property
    def Externals(self):
        return self._Externals

    @Externals.setter
    def Externals(self, Externals):
        self._Externals = Externals

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Prices(self):
        return self._Prices

    @Prices.setter
    def Prices(self, Prices):
        self._Prices = Prices


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        self._Fpga = params.get("Fpga")
        self._StorageBlock = params.get("StorageBlock")
        self._NetworkCard = params.get("NetworkCard")
        self._MaxBandwidth = params.get("MaxBandwidth")
        self._Frequency = params.get("Frequency")
        self._CpuModelName = params.get("CpuModelName")
        self._Pps = params.get("Pps")
        if params.get("Externals") is not None:
            self._Externals = Externals()
            self._Externals._deserialize(params.get("Externals"))
        self._Remark = params.get("Remark")
        if params.get("Prices") is not None:
            self._Prices = []
            for item in params.get("Prices"):
                obj = ReservedInstancePriceItem()
                obj._deserialize(item)
                self._Prices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancesOffering(AbstractModel):
    """The information of the Reserved Instance offering.

    """

    def __init__(self):
        r"""
        :param _Zone: The availability zones in which the Reserved Instance can be purchased, such as ap-guangzhou-1.
Valid value: <a href="https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1">Availability Zones</a>
        :type Zone: str
        :param _CurrencyCode: The billing currency of the Reserved Instance you are purchasing. It's specified using ISO 4217 standard currency.
Value: USD.
        :type CurrencyCode: str
        :param _Duration: The **validity** of the Reserved Instance in seconds, which is the purchased usage period. For example, 31536000.
Unit: second
        :type Duration: int
        :param _FixedPrice: The purchase price of the Reserved Instance, such as 4000.0.
Unit: this field uses the currency code specified in `currencyCode`, and only supports “USD” at this time.
        :type FixedPrice: float
        :param _InstanceType: The instance model of the Reserved Instance, such as S3.MEDIUM4.
Valid values: please see <a href="https://intl.cloud.tencent.com/document/product/213/11518">Reserved Instance Types</a>
        :type InstanceType: str
        :param _OfferingType: The payment term of the Reserved Instance, such as **All Upfront**.
Valid value: All Upfront.
        :type OfferingType: str
        :param _ReservedInstancesOfferingId: The ID of the Reserved Instance offering, such as 650c138f-ae7e-4750-952a-96841d6e9fc1.
        :type ReservedInstancesOfferingId: str
        :param _ProductDescription: The operating system of the Reserved Instance, such as **linux**.
Valid value: linux.
        :type ProductDescription: str
        :param _UsagePrice: The hourly usage price of the Reserved Instance, such as 0.0.
Currently, the only supported payment mode is **All Upfront**, so the default value of `UsagePrice` is 0 USD/hr.
Unit: USD/hr. This field uses the currency code specified in `currencyCode`, and only supports “USD” at this time.
        :type UsagePrice: float
        """
        self._Zone = None
        self._CurrencyCode = None
        self._Duration = None
        self._FixedPrice = None
        self._InstanceType = None
        self._OfferingType = None
        self._ReservedInstancesOfferingId = None
        self._ProductDescription = None
        self._UsagePrice = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CurrencyCode(self):
        return self._CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, CurrencyCode):
        self._CurrencyCode = CurrencyCode

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FixedPrice(self):
        return self._FixedPrice

    @FixedPrice.setter
    def FixedPrice(self, FixedPrice):
        self._FixedPrice = FixedPrice

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OfferingType(self):
        return self._OfferingType

    @OfferingType.setter
    def OfferingType(self, OfferingType):
        self._OfferingType = OfferingType

    @property
    def ReservedInstancesOfferingId(self):
        return self._ReservedInstancesOfferingId

    @ReservedInstancesOfferingId.setter
    def ReservedInstancesOfferingId(self, ReservedInstancesOfferingId):
        self._ReservedInstancesOfferingId = ReservedInstancesOfferingId

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def UsagePrice(self):
        return self._UsagePrice

    @UsagePrice.setter
    def UsagePrice(self, UsagePrice):
        self._UsagePrice = UsagePrice


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._CurrencyCode = params.get("CurrencyCode")
        self._Duration = params.get("Duration")
        self._FixedPrice = params.get("FixedPrice")
        self._InstanceType = params.get("InstanceType")
        self._OfferingType = params.get("OfferingType")
        self._ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self._ProductDescription = params.get("ProductDescription")
        self._UsagePrice = params.get("UsagePrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceRequest(AbstractModel):
    """ResetInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param _ImageId: Specified effective [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are four types of images:<br/><li>Public images</li><li>Custom images</li><li>Shared images</li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways:<br/><li>for IDs of `public images`, `custom images`, and `shared images`, log in to the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE); for IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list).</li><li>Call the API [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
<br>Default value: current image.
        :type ImageId: str
        :param _SystemDisk: Configurations of the system disk. For an instance whose system disk is a cloud disk, this parameter can be used to expand the system disk by specifying a new capacity after reinstallation. The system disk capacity can only be expanded but not shrunk. Reinstalling the system can only resize rather than changing the type of the system disk.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Monitor and Cloud Security. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _HostName: Host name of the CVM, editable during the system reinstallation. <br><li>Periods (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name.<br><li>For Windows instances, the host name must consist of 2-15 characters , including uppercase and lowercase letters, numbers, or hyphens (-). It cannot contain periods (.) or contain only numbers.<br><li>For other instances, such as Linux instances, the host name must consist of 2-60 characters, including multiple periods (.), and allows uppercase and lowercase letters, numbers, or hyphens (-) between any two periods (.).
        :type HostName: str
        :param _UserData: User data provided to the instance. This parameter needs to be encoded in base64 format with the maximum size of 16 KB. For more information on how to get the value of this parameter, see the commands you need to execute on startup for [Windows](https://intl.cloud.tencent.com/document/product/213/17526) or [Linux](https://intl.cloud.tencent.com/document/product/213/17525).
        :type UserData: str
        """
        self._InstanceId = None
        self._ImageId = None
        self._SystemDisk = None
        self._LoginSettings = None
        self._EnhancedService = None
        self._HostName = None
        self._UserData = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._HostName = params.get("HostName")
        self._UserData = params.get("UserData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceResponse(AbstractModel):
    """ResetInstance response structure.

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


class ResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """ResetInstancesInternetMaxBandwidth request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100. When changing the bandwidth of instances with `BANDWIDTH_PREPAID` or `BANDWIDTH_POSTPAID_BY_HOUR` as the network billing method, you can only specify one instance at a time.
        :type InstanceIds: list of str
        :param _InternetAccessible: Configuration of public network egress bandwidth. The maximum bandwidth varies among different models. For more information, see the documentation on bandwidth limits. Currently only the `InternetMaxBandwidthOut` parameter is supported.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _StartTime: Date from which the new bandwidth takes effect. Format: `YYYY-MM-DD`, such as `2016-10-30`. The starting date cannot be earlier than the current date. If the starting date is the current date, the new bandwidth takes effect immediately. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned.
        :type StartTime: str
        :param _EndTime: Date until which the new bandwidth is effective. Format: `YYYY-MM-DD`, such as `2016-10-30`. The validity period of the new bandwidth covers the end date. The end date cannot be later than the expiration date of a prepaid instance. You can query the expiration time of an instance by calling [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728) and looking for `ExpiredTime` in the response. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned.
        :type EndTime: str
        """
        self._InstanceIds = None
        self._InternetAccessible = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

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


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """ResetInstancesInternetMaxBandwidth response structure.

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


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param _Password: Login password of the instance. The password requirements vary among different operating systems:
For a Linux instance, the password must be 8 to 30 characters in length; password with more than 12 characters is recommended. It cannot begin with "/", and must contain at least one character from three of the following categories: <br><li>Lowercase letters: [a-z]<br><li>Uppercase letters: [A-Z]<br><li>Numbers: 0-9<br><li>Special characters: ()\`\~!@#$%^&\*-+=\_|{}[]:;'<>,.?/
For a Windows CVM, the password must be 12 to 30 characters in length. It cannot begin with "/" or contain a username. It must contain at least one character from three of the following categories: <br><li>Lowercase letters: [a-z]<br><li>Uppercase letters: [A-Z]<br><li>Numbers: 0-9<br><li>Special characters: ()\`\~!@#$%^&\*-+=\_|{}[]:;' <>,.?/<br><li>If the specified instances include both `Linux` and `Windows` instances, you will need to follow the password requirements for `Windows` instances.
        :type Password: str
        :param _UserName: Username of the instance operating system for which the password needs to be reset. This parameter is limited to 64 characters.
        :type UserName: str
        :param _ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally.
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._Password = None
        self._UserName = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Password = params.get("Password")
        self._UserName = params.get("UserName")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword response structure.

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


class ResetInstancesTypeRequest(AbstractModel):
    """ResetInstancesType request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). To obtain the instance IDs, you can call the [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API and find the value `InstanceId` in the response. The maximum number of instances in each request is 1.
        :type InstanceIds: list of str
        :param _InstanceType: Instance model. Different resource specifications are specified for different models. For specific values, call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) to get the latest specification list or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1).
        :type InstanceType: str
        :param _ForceStop: Forced shutdown of a running instances. We recommend you firstly try to shut down a running instance manually. Valid values: <br><li>TRUE: forced shutdown of an instance after a normal shutdown fails.<br><li>FALSE: no forced shutdown of an instance after a normal shutdown fails.<br><br>Default value: FALSE.<br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force a CVM to shut off if the normal shutdown fails.
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._InstanceType = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceType = params.get("InstanceType")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesTypeResponse(AbstractModel):
    """ResetInstancesType response structure.

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


class ResizeInstanceDisksRequest(AbstractModel):
    """ResizeInstanceDisks request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param _DataDisks: Configuration of data disks to be expanded. Currently you can only use the API to expand non-elastic data disks whose [disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://intl.cloud.tencent.com/document/api/362/16315?from_cn_redirect=1) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is not elastic. Data disk capacity unit: GB; minimum increment: 10 GB. For more information on selecting the data disk type, see the [product overview on cloud disks](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1). Available data disk types are subject to the instance type (`InstanceType`). In addition, the maximum capacity allowed for expansion varies by data disk type.
        :type DataDisks: list of DataDisk
        :param _ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally.
        :type ForceStop: bool
        :param _SystemDisk: Configuration of the system disk to be expanded. Only cloud disks are supported.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _ResizeOnline: Whether the cloud disk is expanded online.
        :type ResizeOnline: bool
        """
        self._InstanceId = None
        self._DataDisks = None
        self._ForceStop = None
        self._SystemDisk = None
        self._ResizeOnline = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def ResizeOnline(self):
        return self._ResizeOnline

    @ResizeOnline.setter
    def ResizeOnline(self, ResizeOnline):
        self._ResizeOnline = ResizeOnline


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._ForceStop = params.get("ForceStop")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._ResizeOnline = params.get("ResizeOnline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeInstanceDisksResponse(AbstractModel):
    """ResizeInstanceDisks response structure.

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


class RunAutomationServiceEnabled(AbstractModel):
    """Describes the TAT service information.

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable the TAT service. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default: `FALSE`.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesRequest(AbstractModel):
    """RunInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: Instance [billing type](https://intl.cloud.tencent.com/document/product/213/2180?from_cn_redirect=1). <br><li>`POSTPAID_BY_HOUR`: Hourly-based pay-as-you-go <br><li>`CDHPAID`: Dedicated CVM (associated with a dedicated host. Resource usage of the dedicated host is free of charge.) <br><li>`SPOTPAID`: [Spot instance](https://intl.cloud.tencent.com/document/product/213/17817)<br>Default value: `POSTPAID_BY_HOUR`.
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _Placement: Location of the instance. You can use this parameter to specify the availability zone, project, and CDH (for dedicated CVMs).
 <b>Note: `Placement` is required when `LaunchTemplate` is not specified. If both the parameters are passed in, `Placement` prevails.</b>
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _InstanceType: The instance model. 
<br><li>To view specific values for `POSTPAID_BY_HOUR` instances, you can call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1). If this parameter is not specified, `S1.SMALL1` will be used by default.<br><li>For `CDHPAID` instances, the value of this parameter is in the format of `CDH_XCXG` based on the number of CPU cores and memory capacity. For example, if you want to create a CDH instance with a single-core CPU and 1 GB memory, specify this parameter as `CDH_1C1G`.
        :type InstanceType: str
        :param _ImageId: The [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images:<br/><li>Public images</li><li>Custom images</li><li>Shared images</li><br/>To check the image ID:<br/><li>For public images, custom images, and shared images, go to the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE). </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1), pass in `InstanceType` to retrieve the list of images supported by the current model, and then find the `ImageId` in the response.</li>
 <b>Note: `ImageId` is required when `LaunchTemplate` is not specified. If both the parameters are passed in, `ImageId` prevails.</b>
        :type ImageId: str
        :param _SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: The configuration information of instance data disks. If this parameter is not specified, no data disk will be purchased by default. When purchasing, you can specify 21 data disks, which can contain at most 1 LOCAL_BASIC or LOCAL_SSD data disk, and at most 20 CLOUD_BASIC, CLOUD_PREMIUM, or CLOUD_SSD data disks.
        :type DataDisks: list of DataDisk
        :param _VirtualPrivateCloud: Configuration information of VPC. This parameter is used to specify VPC ID and subnet ID, etc. If a VPC IP is specified in this parameter, it indicates the primary ENI IP of each instance. The value of parameter InstanceCount must be the same as the number of VPC IPs, which cannot be greater than 20.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _InternetAccessible: Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _InstanceCount: The number of instances to be purchased. Value range for pay-as-you-go instances: [1, 100]. Default value: `1`. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user. For more information on the quota, see [Quota for CVM Instances](https://intl.cloud.tencent.com/document/product/213/2664).
        :type InstanceCount: int
        :param _InstanceName: Instance name to be displayed. <br><li>If this parameter is not specified, "Unnamed" will be displayed by default. </li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`. </li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and the instance name body is `server_`, the instance names will be `server_1` and `server_2`. </li><li>This parameter can contain up to 60 characters, including the pattern string.
        :type InstanceName: str
        :param _LoginSettings: Instance login settings. You can use this parameter to set the login method, password and key of the instance, or keep the original login settings of the image. If it's not specified, the user needs to set the login password using the "Reset password" option in the CVM console or calling the API `ResetInstancesPassword` to complete the creation of the CVM instance(s).
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will be associated with default security groups.
        :type SecurityGroupIds: list of str
        :param _EnhancedService: Enhanced service. You can use this parameter to specify whether to enable services such as Anti-DDoS and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Anti-DDoS are enabled for public images by default. However, for custom images and images from the marketplace, Anti-DDoS and Cloud Monitor are not enabled by default. The original services in the image will be retained.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idem-potency of the request cannot be guaranteed.
        :type ClientToken: str
        :param _HostName: Instance hostname. <br><li>Dots (.) and dashes (-) can not be used as the first or last character of HostName nor used consecutively. <br<li>Windows instances: 2 to 15 characters, including English letters (case-insensitive), numbers and dashes (-). Dots and numeric-only names are not allowed. <br><li>Other instances (Linux, etc.): 2 to 60 characters, including English letters (case-insensitive), numbers, dashes (-) and dots. Note that consecutive dots are not allowed.<br><li>Batch naming: use `{R:x}` for batch naming if multiple instances are purchased. `x` is the serial number of the instance. It’s generated by [x, x+n-1], where `n` refers to the number of instances purchased. For example, if `server{R:3}` is input, if you purchase one instance, the hostname is `server3`. If you purchase two instances, the hostnames are `server3` and `server4` respectively. You can specify multiple pattern strings `{R:x}`. </li><br><li>Purchasing multiple instances: If no pattern string is specified, you shall add suffixes `1, 2...n` to the instance hostname. `n` represents the number of purchased instances. For example, if the instance hostname is `server`,  when two instances are purchased, the hostnames of instances purchased are respectively `server1` and `server2`.
        :type HostName: str
        :param _ActionTimer: Scheduled tasks. You can use this parameter to specify scheduled tasks for the instance. Only scheduled termination is supported.
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param _DisasterRecoverGroupIds: Placement group ID. You can only specify one.
        :type DisasterRecoverGroupIds: list of str
        :param _TagSpecification: List of tag description. By specifying this parameter, the tag can be bound to the corresponding CVM and CBS instances at the same time.
        :type TagSpecification: list of TagSpecification
        :param _InstanceMarketOptions: The market options of the instance.
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param _UserData: User data provided to the instance. This parameter needs to be encoded in base64 format with the maximum size of 16 KB. For more information on how to get the value of this parameter, see the commands you need to execute on startup for [Windows](https://intl.cloud.tencent.com/document/product/213/17526) or [Linux](https://intl.cloud.tencent.com/document/product/213/17525).
        :type UserData: str
        :param _DryRun: Whether the request is a dry run only.
`true`: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available.
If the dry run fails, the corresponding error code will be returned.
If the dry run succeeds, the RequestId will be returned.
`false` (default value): Send a normal request and create instance(s) if all the requirements are met.
        :type DryRun: bool
        :param _CamRoleName: CAM role name, which can be obtained from the `roleName` field in the response of the [`DescribeRoleList`](https://intl.cloud.tencent.com/document/product/598/36223?from_cn_redirect=1) API.
        :type CamRoleName: str
        :param _HpcClusterId: HPC cluster ID. The HPC cluster must and can only be specified for a high-performance computing instance.
        :type HpcClusterId: str
        :param _LaunchTemplate: Instance launch template.
        :type LaunchTemplate: :class:`tencentcloud.cvm.v20170312.models.LaunchTemplate`
        :param _DedicatedClusterId: Specify the ID of the dedicated cluster where the CVM is created.
        :type DedicatedClusterId: str
        :param _ChcIds: Specify the CHC physical server that used to create the CHC CVM.
        :type ChcIds: list of str
        :param _DisableApiTermination: Whether the termination protection is enabled. Values: <br><li>`TRUE`: Enable instance protection, which means that this instance can not be deleted by an API action.<br><li>`FALSE`: Do not enable the instance protection.<br><br>Default value: `FALSE`.
        :type DisableApiTermination: bool
        """
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._Placement = None
        self._InstanceType = None
        self._ImageId = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceCount = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._ClientToken = None
        self._HostName = None
        self._ActionTimer = None
        self._DisasterRecoverGroupIds = None
        self._TagSpecification = None
        self._InstanceMarketOptions = None
        self._UserData = None
        self._DryRun = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._LaunchTemplate = None
        self._DedicatedClusterId = None
        self._ChcIds = None
        self._DisableApiTermination = None

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def ActionTimer(self):
        return self._ActionTimer

    @ActionTimer.setter
    def ActionTimer(self, ActionTimer):
        self._ActionTimer = ActionTimer

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def LaunchTemplate(self):
        return self._LaunchTemplate

    @LaunchTemplate.setter
    def LaunchTemplate(self, LaunchTemplate):
        self._LaunchTemplate = LaunchTemplate

    @property
    def DedicatedClusterId(self):
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceType = params.get("InstanceType")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._ClientToken = params.get("ClientToken")
        self._HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self._ActionTimer = ActionTimer()
            self._ActionTimer._deserialize(params.get("ActionTimer"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._UserData = params.get("UserData")
        self._DryRun = params.get("DryRun")
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        if params.get("LaunchTemplate") is not None:
            self._LaunchTemplate = LaunchTemplate()
            self._LaunchTemplate._deserialize(params.get("LaunchTemplate"))
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._ChcIds = params.get("ChcIds")
        self._DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    """RunInstances response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: If you use this API to create instance(s), this parameter will be returned, representing one or more instance IDs. Retuning the instance ID list does not necessarily mean that the instance(s) were created successfully. To check whether the instance(s) were created successfully, you can call [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and check the status of the instances in `InstancesSet` in the response. If the status of an instance changes from "PENDING" to "RUNNING", it means that the instance has been created successfully.
        :type InstanceIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Monitor service.

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable [Cloud Monitor](https://intl.cloud.tencent.com/document/product/248?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Monitor <br><li>FALSE: do not enable Cloud Monitor <br><br>Default value: TRUE.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Security service.

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable [Cloud Security](https://intl.cloud.tencent.com/document/product/296?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Security <br><li>FALSE: do not enable Cloud Security <br><br>Default value: TRUE.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SharePermission(AbstractModel):
    """Describes image sharing information.

    """

    def __init__(self):
        r"""
        :param _CreatedTime: Time when an image was shared.
        :type CreatedTime: str
        :param _AccountId: ID of the account with which the image is shared.
        :type AccountId: str
        """
        self._CreatedTime = None
        self._AccountId = None

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId


    def _deserialize(self, params):
        self._CreatedTime = params.get("CreatedTime")
        self._AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """Describes information on the snapshot associated with an image.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID.
        :type SnapshotId: str
        :param _DiskUsage: Type of the cloud disk used to create the snapshot. Valid values:
SYSTEM_DISK: system disk
DATA_DISK: data disk
        :type DiskUsage: str
        :param _DiskSize: Size of the cloud disk used to create the snapshot; unit: GB.
        :type DiskSize: int
        """
        self._SnapshotId = None
        self._DiskUsage = None
        self._DiskSize = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpotMarketOptions(AbstractModel):
    """Options related to bidding.

    """

    def __init__(self):
        r"""
        :param _MaxPrice: Bidding price
        :type MaxPrice: str
        :param _SpotInstanceType: Bidding request type. Currently only "one-time" is supported.
        :type SpotInstanceType: str
        """
        self._MaxPrice = None
        self._SpotInstanceType = None

    @property
    def MaxPrice(self):
        return self._MaxPrice

    @MaxPrice.setter
    def MaxPrice(self, MaxPrice):
        self._MaxPrice = MaxPrice

    @property
    def SpotInstanceType(self):
        return self._SpotInstanceType

    @SpotInstanceType.setter
    def SpotInstanceType(self, SpotInstanceType):
        self._SpotInstanceType = SpotInstanceType


    def _deserialize(self, params):
        self._MaxPrice = params.get("MaxPrice")
        self._SpotInstanceType = params.get("SpotInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    """StartInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
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
        


class StartInstancesResponse(AbstractModel):
    """StartInstances response structure.

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


class StopInstancesRequest(AbstractModel):
    """StopInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param _ForceStop: (Disused. Please use `StopType` instead.) Whether to forcibly shut down an instance after a normal shutdown fails. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default value: `FALSE`. 
        :type ForceStop: bool
        :param _StopType: Instance shutdown mode. Valid values: <br><li>SOFT_FIRST: perform a soft shutdown first, and force shut down the instance if the soft shutdown fails <br><li>HARD: force shut down the instance directly <br><li>SOFT: soft shutdown only <br>Default value: SOFT.
        :type StopType: str
        :param _StoppedMode: Billing method of a pay-as-you-go instance after shutdown.
Valid values: <br><li>KEEP_CHARGING: billing continues after shutdown <br><li>STOP_CHARGING: billing stops after shutdown <br>Default value: KEEP_CHARGING.
This parameter is only valid for some pay-as-you-go instances using cloud disks. For more information, see [No charges when shut down for pay-as-you-go instances](https://intl.cloud.tencent.com/document/product/213/19918).
        :type StoppedMode: str
        """
        self._InstanceIds = None
        self._ForceStop = None
        self._StopType = None
        self._StoppedMode = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def StopType(self):
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType

    @property
    def StoppedMode(self):
        return self._StoppedMode

    @StoppedMode.setter
    def StoppedMode(self, StoppedMode):
        self._StoppedMode = StoppedMode


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ForceStop = params.get("ForceStop")
        self._StopType = params.get("StopType")
        self._StoppedMode = params.get("StoppedMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    """StopInstances response structure.

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


class StorageBlock(AbstractModel):
    """Information on local HDD storage.

    """

    def __init__(self):
        r"""
        :param _Type: Local HDD storage type. Value: LOCAL_PRO.
Note: This field may return null, indicating that no valid value is found.
        :type Type: str
        :param _MinSize: Minimum capacity of local HDD storage
Note: This field may return null, indicating that no valid value is found.
        :type MinSize: int
        :param _MaxSize: Maximum capacity of local HDD storage
Note: This field may return null, indicating that no valid value is found.
        :type MaxSize: int
        """
        self._Type = None
        self._MinSize = None
        self._MaxSize = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImage(AbstractModel):
    """Image sync information

    """

    def __init__(self):
        r"""
        :param _ImageId: Image ID
        :type ImageId: str
        :param _Region: Region
        :type Region: str
        """
        self._ImageId = None
        self._Region = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImagesRequest(AbstractModel):
    """SyncImages request structure.

    """

    def __init__(self):
        r"""
        :param _ImageIds: List of image IDs. You can obtain the image IDs in two ways: <br><li>Call the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) API and find the value of `ImageId` in the response. <br><li>Find the image IDs in the [Image Console](https://console.cloud.tencent.com/cvm/image). <br>The specified images must meet the following requirement: <br><li>the images must be in the `NORMAL` state. <br>For more information on image status, see [Image Data Table](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#Image).
        :type ImageIds: list of str
        :param _DestinationRegions: List of destination regions for synchronization. Limits:<br><li>It must be a valid region.<br><li>For a custom image, the destination region cannot be the source region.<br><li>For a shared image, the destination region must be the source region, which indicates to create a copy of the image as a custom image in the same region.<br><li>Image synchronization is only available in limited regions.<br>See [Region](https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1).
        :type DestinationRegions: list of str
        :param _DryRun: Checks whether image synchronization can be initiated.
        :type DryRun: bool
        :param _ImageName: Destination image name.
        :type ImageName: str
        :param _ImageSetRequired: Whether to return the ID of image created in the destination region
        :type ImageSetRequired: bool
        """
        self._ImageIds = None
        self._DestinationRegions = None
        self._DryRun = None
        self._ImageName = None
        self._ImageSetRequired = None

    @property
    def ImageIds(self):
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

    @property
    def DestinationRegions(self):
        return self._DestinationRegions

    @DestinationRegions.setter
    def DestinationRegions(self, DestinationRegions):
        self._DestinationRegions = DestinationRegions

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageSetRequired(self):
        return self._ImageSetRequired

    @ImageSetRequired.setter
    def ImageSetRequired(self, ImageSetRequired):
        self._ImageSetRequired = ImageSetRequired


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        self._DestinationRegions = params.get("DestinationRegions")
        self._DryRun = params.get("DryRun")
        self._ImageName = params.get("ImageName")
        self._ImageSetRequired = params.get("ImageSetRequired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImagesResponse(AbstractModel):
    """SyncImages response structure.

    """

    def __init__(self):
        r"""
        :param _ImageSet: ID of the image created in the destination region
        :type ImageSet: list of SyncImage
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImageSet = None
        self._RequestId = None

    @property
    def ImageSet(self):
        return self._ImageSet

    @ImageSet.setter
    def ImageSet(self, ImageSet):
        self._ImageSet = ImageSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageSet") is not None:
            self._ImageSet = []
            for item in params.get("ImageSet"):
                obj = SyncImage()
                obj._deserialize(item)
                self._ImageSet.append(obj)
        self._RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """Describes information on the block device where the operating system is stored, i.e., the system disk.

    """

    def __init__(self):
        r"""
        :param _DiskType: System disk type. For more information about the limits of system disk types, please see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values:<br><li>LOCAL_BASIC: local disk<br><li>LOCAL_SSD: local SSD disk<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_SSD: SSD cloud disk<br><li>CLOUD_PREMIUM: Premium cloud storage<br><li>CLOUD_BSSD: Balanced SSD<br><br>The disk currently in stock will be used by default.
        :type DiskType: str
        :param _DiskId: System disk ID. System disks whose type is `LOCAL_BASIC` or `LOCAL_SSD` do not have an ID and do not support this parameter.
It is only used as a response parameter for APIs such as `DescribeInstances`, and cannot be used as a request parameter for APIs such as `RunInstances`.
        :type DiskId: str
        :param _DiskSize: System disk size; unit: GB; default value: 50 GB.
        :type DiskSize: int
        :param _CdcId: ID of the dedicated cluster to which the instance belongs.
        :type CdcId: str
        """
        self._DiskType = None
        self._DiskId = None
        self._DiskSize = None
        self._CdcId = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def CdcId(self):
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Key-value pair of a tag.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class TagSpecification(AbstractModel):
    """Description of tags associated with resource instances during instance creation.

    """

    def __init__(self):
        r"""
        :param _ResourceType: Resource type. Valid values: `instance` (CVM), `host` (CDH), `image` (for image), and `keypair` (for key).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param _Tags: Tag pairs
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
        self._ResourceType = None
        self._Tags = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param _ReleasePrepaidDataDisks: Release the monthly subscribed data disks attached to the instance
        :type ReleasePrepaidDataDisks: bool
        """
        self._InstanceIds = None
        self._ReleasePrepaidDataDisks = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ReleasePrepaidDataDisks(self):
        return self._ReleasePrepaidDataDisks

    @ReleasePrepaidDataDisks.setter
    def ReleasePrepaidDataDisks(self, ReleasePrepaidDataDisks):
        self._ReleasePrepaidDataDisks = ReleasePrepaidDataDisks


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ReleasePrepaidDataDisks = params.get("ReleasePrepaidDataDisks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances response structure.

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


class VirtualPrivateCloud(AbstractModel):
    """Describes information on VPC, including subnets, IP addresses, etc.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID in the format of `vpc-xxx`. To obtain valid VPC IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/vpc?rid=1) or call the [DescribeVpcEx](https://intl.cloud.tencent.com/document/api/215/1372?from_cn_redirect=1) API and look for the `unVpcId` fields in the response. If you specify `DEFAULT` for both `VpcId` and `SubnetId` when creating an instance, the default VPC will be used.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID in the format `subnet-xxx`. To obtain valid subnet IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/subnet?rid=1) or call [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) and look for the `unSubnetId` fields in the response. If you specify `DEFAULT` for both `SubnetId` and `VpcId` when creating an instance, the default VPC will be used.
        :type SubnetId: str
        :param _AsVpcGateway: Whether to use a CVM instance as a public gateway. The public gateway is only available when the instance has a public IP and resides in a VPC. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default: `FALSE`.
        :type AsVpcGateway: bool
        :param _PrivateIpAddresses: Array of VPC subnet IPs. You can use this parameter when creating instances or modifying VPC attributes of instances. Currently you can specify multiple IPs in one subnet only when creating multiple instances at the same time.
        :type PrivateIpAddresses: list of str
        :param _Ipv6AddressCount: Number of IPv6 addresses randomly generated for the ENI.
        :type Ipv6AddressCount: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._AsVpcGateway = None
        self._PrivateIpAddresses = None
        self._Ipv6AddressCount = None

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
    def AsVpcGateway(self):
        return self._AsVpcGateway

    @AsVpcGateway.setter
    def AsVpcGateway(self, AsVpcGateway):
        self._AsVpcGateway = AsVpcGateway

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Ipv6AddressCount(self):
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AsVpcGateway = params.get("AsVpcGateway")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """Information on availability zones.

    """

    def __init__(self):
        r"""
        :param _Zone: Availability zone name, such as `ap-guangzhou-3`.
The following is a list of all availability zones:
<li> ap-chongqing-1 </li>
<li> ap-seoul-1 </li>
<li> ap-seoul-2 </li>
<li> ap-chengdu-1 </li>
<li> ap-chengdu-2 </li>
<li> ap-hongkong-1 (resource out of stock)</li>
<li> ap-hongkong-2 </li>
<li> ap-hongkong-3 </li>
<li> ap-shenzhen-fsi-1 </li>
<li> ap-shenzhen-fsi-2 </li>
<li> ap-shenzhen-fsi-3 </li>
<li> ap-guangzhou-1 (resource out of stock)</li>
<li> ap-guangzhou-2 (resource out of stock)</li>
<li> ap-guangzhou-3 </li>
<li> ap-guangzhou-4 </li>
<li> ap-guangzhou-6 </li>
<li> ap-guangzhou-7 </li>
<li> ap-tokyo-1 </li>
<li> ap-tokyo-2 </li>
<li> ap-singapore-1 </li>
<li> ap-singapore-2 </li>
<li> ap-singapore-3 </li>
<li>ap-singapore-4 </li>
<li> ap-shanghai-fsi-1 </li>
<li> ap-shanghai-fsi-2 </li>
<li> ap-shanghai-fsi-3 </li>
<li> ap-bangkok-1 </li>
<li> ap-bangkok-2 </li>
<li> ap-shanghai-1 (resource out of stock) </li>
<li> ap-shanghai-2 </li>
<li> ap-shanghai-3 </li>
<li> ap-shanghai-4 </li>
<li> ap-shanghai-5 </li>
<li> ap-shanghai-8 </li>
<li> ap-mumbai-1 </li>
<li> ap-mumbai-2 </li>
<li> eu-moscow-1 </li>
<li> ap-beijing-1 (resource out of stock) </li>
<li> ap-beijing-2 </li>
<li> ap-beijing-3 </li>
<li> ap-beijing-4 </li>
<li> ap-beijing-5 </li>
<li> ap-beijing-6 </li>
<li> ap-beijing-7 </li>
<li> na-siliconvalley-1 </li>
<li> na-siliconvalley-2 </li>
<li> eu-frankfurt-1 </li>
<li> eu-frankfurt-2 </li>
<li> na-toronto-1 </li>
<li> na-ashburn-1 </li>
<li> na-ashburn-2 </li>
<li> ap-nanjing-1 </li>
<li> ap-nanjing-2 </li>
<li> ap-nanjing-3 </li>
<li> sa-saopaulo-1</li>
<li> ap-jakarta-1 </li>
<li> ap-jakarta-2 </li>
        :type Zone: str
        :param _ZoneName: Availability zone description, such as Guangzhou Zone 3.
        :type ZoneName: str
        :param _ZoneId: Availability zone ID.
        :type ZoneId: str
        :param _ZoneState: Availability zone status. Valid values: `AVAILABLE`: available; `UNAVAILABLE`: unavailable.
        :type ZoneState: str
        """
        self._Zone = None
        self._ZoneName = None
        self._ZoneId = None
        self._ZoneState = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneState(self):
        return self._ZoneState

    @ZoneState.setter
    def ZoneState(self, ZoneState):
        self._ZoneState = ZoneState


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneState = params.get("ZoneState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        